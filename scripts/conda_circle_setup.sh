set -x
set -e

echo "Downloading Conda latest v3"
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
echo "Installing Conda latest v3"
bash ~/miniconda.sh -b -p $HOME/miniconda

echo "Appending Conda path to bashrc file"
echo PATH="$HOME/miniconda/bin:$PATH" >> ~/.bashrc
echo "Activating bashrc file"
source ~/.bashrc
echo "Updating Conda"
conda update conda --yes

echo "Creating cas environment"
conda env create -f environment.yml
