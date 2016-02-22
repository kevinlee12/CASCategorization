set -x
set -e

CACHED=1

echo "Checking if Conda is installed"
if [ ! -e ~/miniconda/ ]; then
  echo "Conda was not installed, installing Conda"
  CACHED=0
  echo "Downloading Conda latest v3"
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
  echo "Installing Conda latest v3"
  bash ~/miniconda.sh -b -p $HOME/miniconda
fi


echo "Appending Conda path to bashrc file"
echo PATH="$HOME/miniconda/bin:$PATH" >> ~/.bashrc
echo "Activating bashrc file"
source ~/.bashrc
echo "Updating Conda"
conda update conda --yes

if [ $CACHED == 0 ]; then
  echo "Creating cas environment"
  conda env create -f environment.yml
fi
