#!/bin/sh
set -e

OS=`uname`

# Set the working directory to the root of the git repo.
cd $(git rev-parse --show-toplevel)

if [[ "${OS}" == "Darwin" ]]; then
	miniconda_file="Miniconda3-latest-MacOSX-x86_64.sh"
else
	miniconda_file="Miniconda3-latest-Linux-x86_64.sh"
fi
miniconda_link="https://repo.continuum.io/miniconda/${miniconda_file}"

echo "Installing git hooks."
cd .git/hooks
ln --force --symbolic ../../scripts/pre-push.sh pre-push
cd -

echo "Checking if Conda is installed..."
if [ ! -e ~/miniconda*/ ]; then
	echo "Conda is not installed."
	echo "Downloading Conda."
	curl -O $miniconda_link
	echo "Installing Conda."
	bash $miniconda_file
	rm $miniconda_file
fi
echo "Conda is installed."

echo "Appending conda path to a new '.conda_profile' file."
echo PATH="$HOME/miniconda/bin:$PATH" >> ~/.conda_profile
source ~/.conda_profile

echo "Creating cas environment."
if [[ "${OS}" == "Darwin" ]]; then
	sed -i '' "/scipy/d" environment.yml
fi
conda env create -f environment.yml 2>/dev/null
git checkout -- environment.yml

echo "Updating conda environment packages."
conda env update

echo "Activating the environment and installing requirements."
source activate cas
pip install -r requirements.txt

if [[ "${OS}" == "Darwin" ]]; then
	cat <<-DB
		Warning: Database setup may fail.
		You may need to append the following to ~/.conda_profile
		for setup to succeed:
		export DYLD_LIBRARY_PATH=*YOUR_OPENSSL_INSTALL_PATH/lib
	DB
	mac_db_message=$(cat <<-SETVAR
	You may need to uncomment the DYLD_LIBRARY_PATH export
	for pip commands to work while in the cas environment.
	SETVAR
	)
	sleep 3
fi

echo "Setting up the database..."
bash db_setup.sh
if [ $? -ne 0 ]; then
	echo "db_setup.sh: Error setting up cas database."
	exit 1
fi

echo "Running database migration and application tests..."
python manage.py migrate
if [ $? -ne 0 ]; then
	echo "Failed to migrate!"
	exit 1
fi
python manage.py test

cat <<CAS
Setup complete!
This project must run in the conda 'cas' environment to work properly.
Miniconda has its own version of python, so its install path has been
placed in .conda_profile.

Run the following to activate miniconda's python:
	source ~/.conda_profile

Update packages for cas environment:
	conda env update

Activate the cas environment:
	source activate cas

To exit the cas environment:
	source deactivate

${mac_db_message}

Happy CASegorizing!
CAS
