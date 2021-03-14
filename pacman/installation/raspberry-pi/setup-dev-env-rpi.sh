##
# Install Pygame Zero 1.2 on Raspberry Pi 4 in miniconda dev environment
##

# Uninstall pygame if you notice issues trying to run existing pgzero
# sudo apt -y autoremove python3-pygame

# Download miniconda installation (32-bit version)
curl "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-armv7l.sh" -o "Miniconda.sh"

# Run miniconda manual installation
bash ./Miniconda.sh

# Add Raspberry Pi channel for conda installations
conda config --add channels rpi

# Update conda
conda update conda

# Create conda environment called pacman
conda create -y -n pacman python=3.5

# Activate pacman environment
source activate pacman

# Install Pygame 1.9.4
sudo apt -y install libatlas-base-dev
sudo apt -y install python3-pygame

# Install Pygame 1.9.4
pip install pygame==1.9.4

# Install Pygame Zero. Dependency Pygame 1.9.4
pip install pgzero==1.2
