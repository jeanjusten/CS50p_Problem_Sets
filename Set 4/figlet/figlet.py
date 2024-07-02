from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figlet_fonts = figlet.getFonts()

if len(sys.argv) >= 2 and sys.argv[1] == "-f" and sys.argv[2] in figlet_fonts:
    font_choice = sys.argv[2]
    text_input = input("Input: ")
    figlet.setFont(font=font_choice)
    print(figlet.renderText(text_input))

elif len(sys.argv) == 1:
    font_choice = random.choice(figlet_fonts)
    text_input = input("Input: ")
    figlet.setFont(font=font_choice)
    print(figlet.renderText(text_input))
    
else:
    sys.exit("Invalid Usage")