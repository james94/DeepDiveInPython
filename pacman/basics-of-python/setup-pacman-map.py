import pgzrun

##
# Pygame Zero sets the window size to 600 x 660 using variables WIDTH and HEIGHT. Pygame Zero
# then calls draw() function to draw a header for game info and a square maze onto the window.
# Note: Pygame Zero gets the header and colourmap from the images/ dir in same folder
##

WIDTH = 600
HEIGHT = 660

header_filename = "header"
colourmap_filename = "colourmap"

def draw():
    screen.clear()
    screen.blit(header_filename, (0, 0))
    screen.blit(colourmap_filename, (0, 80))

pgzrun.go()