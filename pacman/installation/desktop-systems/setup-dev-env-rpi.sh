# Download miniconda installation (32-bit version)
curl "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-armv7l.sh" -o "Miniconda.sh"

# Run miniconda manual installation
bash ./Miniconda.sh

# Add Raspberry Pi channel for conda installations
conda config --add channels rpi

# Update conda
conda update conda

# Install Pygame Zero
pip install pgzero
