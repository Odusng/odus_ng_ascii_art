# Install pyfiglet before running
# pip install pyfiglet

import pyfiglet

# Define colors using ANSI escape codes
ORANGE = '\033[38;2;255;103;31m'
WHITE  = '\033[38;2;255;255;255m'
GREEN  = '\033[38;2;0;128;0m'
PINK   = '\033[38;2;255;105;180m'
RESET  = '\033[0m'  # Reset color to default

# Generate ASCII text
font = pyfiglet.figlet_format('Odus.ng !')

# Print in pink color
print(GREEN + font + RESET)
