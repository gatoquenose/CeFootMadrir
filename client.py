# Import the contextlib module to redirect stdout to None
import contextlib

import pygame.freetype
with contextlib.redirect_stdout(None):
    # Import the pygame module
    import pygame

import guiTools as gt
import colors as clr

pygame.init()
pygame.display.set_caption("Proyecto 2 Fundamentos")

windowWith = 900
windowHeight = 600
window = pygame.display.set_mode((windowWith, windowHeight))

font = pygame.freetype.Font("inconsolataNerdFont.ttf", 32)

inputNumberText = gt.TextBlock(font, "Ingrese un numero del 0 al 7", 40, windowWith//2, 200)
textInput = gt.TextInput(font, "", 40, windowWith//2, 400)



clock = pygame.time.Clock()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():
                if int(event.unicode) in range (0,7+1):
                    if len(textInput.text) < 1:
                        textInput.update(event)
            elif event.key == pygame.K_BACKSPACE:
                textInput.update(event)

    window.fill(clr.BACKGROUND)
    inputNumberText.draw(window)
    textInput.draw(window)
    pygame.display.flip()

pygame.quit()