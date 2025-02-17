# Import the contextlib module to redirect stdout to None
import contextlib
with contextlib.redirect_stdout(None):
    # Import the pygame module
    import pygame

# Initialize pygame
pygame.init()

# Import the colors module
import colors as clr

# Define a class for a text block
class TextBlock:
    def __init__(self, font: pygame.freetype.Font, text: str, size: int, x: int, y: int, margin: int=10,
                 background: tuple[int, int, int]=clr.BACKGROUND, 
                 foreground: tuple[int, int, int]=clr.FOREGROUND):
        # Initialize the text block with the given font, text, size, position, and colors
        self.font = font
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin
        self.background = background
        self.foreground = foreground

        # Render the text using the font and colors
        textSurface, textRect = self.font.render(self.text, self.foreground, self.background, size = self.size)

        # Create a surface for the text block with a margin
        blockSurface = pygame.Surface((textRect.width + 2 * self.margin, textRect.height + 2 * self.margin))
        blockRect = blockSurface.get_rect(center = (self.x, self.y))
        blockSurface.fill(self.background)
        blockSurface.blit(textSurface, (self.margin, self.margin))

        # Store the surface and rect for the text block
        self.surface = blockSurface
        self.rect = blockRect

    def draw(self, window):
        # Draw the text block on the given window
        window.blit(self.surface, self.rect)

class TextInput:
    def __init__(self, font: pygame.freetype.Font, text: str, size: int, x: int, y: int, margin: int=10,
                 background: tuple[int, int, int]=clr.BACKGROUND, 
                 foreground: tuple[int, int, int]=clr.FOREGROUND):
        # Initialize the text block with the given font, text, size, position, and colors
        self.font = font
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin
        self.background = background
        self.foreground = foreground

        # Render the text using the font and colors
        textSurface, textRect = self.font.render(self.text, self.foreground, self.background, size = self.size)

        # Create a surface for the text block with a margin
        blockSurface = pygame.Surface((textRect.width + 2 * self.margin, textRect.height + 2 * self.margin))
        blockRect = blockSurface.get_rect(center = (self.x, self.y))
        blockSurface.fill(self.background)
        blockSurface.blit(textSurface, (self.margin, self.margin))

        # Store the surface and rect for the text block
        self.surface = blockSurface
        self.rect = blockRect

    def draw(self, window):
        # Draw the text block on the given window
        window.blit(self.surface, self.rect)
    
    def update(self, event):
        #Update text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
            else:
                self.text += event.unicode
        
        # Render the text using the font and colors
        textSurface, textRect = self.font.render(self.text, self.foreground, self.background, size = self.size)

        # Create a surface for the text block with a margin
        blockSurface = pygame.Surface((textRect.width + 2 * self.margin, textRect.height + 2 * self.margin))
        blockRect = blockSurface.get_rect(center = (self.x, self.y))
        blockSurface.fill(self.background)
        blockSurface.blit(textSurface, (self.margin, self.margin))

        # Store the surface and rect for the text block
        self.surface = blockSurface
        self.rect = blockRect

# Define a class for a button
class Button:
    def __init__(self, font: pygame.freetype.Font, text: str, size: int, x: int, y: int, margin: int=10,
                 background: tuple[int, int, int]=clr.BACKGROUND, 
                 foreground: tuple[int, int, int]=clr.FOREGROUND):
        # Initialize the button with the given font, text, size, position, and colors
        self.font = font
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin
        self.background = background
        self.foreground = foreground

        # Create a normal button and a dark button
        normalButton = TextBlock(self.font, self.text, self.size, self.x, self.y, self.margin, self.background, self.foreground)
        darkBackground = (max(0, self.background[0] - 20), max(0, self.background[1] - 20), max(0, self.background[2] - 20))
        darkButton = TextBlock(self.font, self.text, self.size, self.x, self.y, self.margin, darkBackground, self.foreground)

        # Store the surfaces and rect for the buttons
        self.surface = normalButton.surface
        self.surfaceDark = darkButton.surface
        self.rect = normalButton.rect

    def draw(self, window, cursor):
        # Draw the button on the given window, using the dark button if the cursor is over it
        if self.rect.collidepoint(cursor):
            window.blit(self.surfaceDark, self.rect)
        else:
            window.blit(self.surface, self.rect)

# Define a class for an image block
class ImageBlock:
    def __init__(self, img: pygame.Surface, size: int, x: int, y: int, margin: int=10, background: tuple[int, int, int]=clr.BACKGROUND):
        # Initialize the image block with the given image, size, position, and background color
        self.img = pygame.transform.scale(img, (size, size))
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin
        self.background = background

        # Create a surface for the image block with a margin
        blockSurface = pygame.Surface((self.size + 2 * self.margin, self.size + 2 * self.margin))
        blockRect = blockSurface.get_rect(center = (self.x, self.y))
        blockSurface.fill(self.background)
        blockSurface.blit(self.img, (self.margin, self.margin))

        # Store the surface and rect for the image block
        self.surface = blockSurface
        self.rect = blockRect

    def draw(self, window):
        # Draw the image block on the given window
        window.blit(self.surface, self.rect)

# Define a class for an image button
class ImageButton:
    def __init__(self, img: pygame.Surface, size: int, x: int, y: int, margin:int=10,
                 background: tuple[int, int, int]=clr.BACKGROUND,):
        # Initialize the image button with the given image, size, position, and background color
        self.img = pygame.transform.scale(img, (size, size))
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin
        self.background = background

        # Create a normal button and a dark button
        normalButton = ImageBlock(self.img, self.size, self.x, self.y, self.margin)
        darkBackground = (max(0, self.background[0] - 20), max(0, self.background[1] - 20), max(0, self.background[2] - 20))
        darkButton = ImageBlock(self.img, self.size, self.x, self.y, self.margin, darkBackground)

        # Store the surfaces and rect for the buttons
        self.surface = normalButton.surface
        self.surfaceDark = darkButton.surface
        self.rect = normalButton.rect

    def draw(self, window, cursor):
        # Draw the button on the given window, using the dark button if the cursor is over it
        if self.rect.collidepoint(cursor):
            window.blit(self.surfaceDark, self.rect)
        else:
            window.blit(self.surface, self.rect)

# Define a class for a color button
class ColorButton:
    def __init__(self, color: tuple[int, int, int], size: int, x: int, y: int, margin: int=10):
        # Initialize the color button with the given color, size, position, and margin
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin

        # Create a color surface and an image button
        colorSurface = pygame.Surface((self.size, self.size))
        colorSurface.fill(self.color)

        colorButton = ImageButton(colorSurface, self.size, self.x, self.y, self.margin)

        # Store the surfaces and rect for the button
        self.surface = colorButton.surface
        self.surfaceDark = colorButton.surfaceDark
        self.rect = colorButton.rect

    def draw(self, window, cursor):
        # Draw the button on the given window, using the dark button if the cursor is over it
        if self.rect.collidepoint(cursor):
            window.blit(self.surfaceDark, self.rect)
        else:
            window.blit(self.surface, self.rect)

# Define a class for a color block
class ColorBlock:
    def __init__(self, color: tuple[int, int, int], size: int, x: int, y: int, margin: int=10, isBase: bool=True):
        # Initialize the color block with the given color, size, position, margin, and base status
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin
        self.isBase = isBase

        # Create a color surface and an image block
        colorSurface = pygame.Surface((self.size, self.size))
        colorSurface.fill(self.color)

        colorBlock = ImageBlock(colorSurface, self.size, self.x, self.y, self.margin)

        # Store the surface and rect for the block
        self.surface = colorBlock.surface
        self.rect = colorBlock.rect

    def draw(self, window):
        # Draw the block on the given window
        window.blit(self.surface, self.rect)

# Define a class for a canvas
class Canvas:
    def __init__(self, top: int, left: int, pixel_size: int, width: int, height: int, background: tuple[int, int, int]=clr.BACKGROUND, pixels: list[list[ColorBlock]]=[]):
        # Initialize the canvas with the given top, left, pixel size, width, height, background color, and pixels
        self.top = top
        self.left = left
        self.pixel_size = pixel_size
        self.width = width
        self.height = height
        self.background = background

        # Create a surface for the canvas
        self.surface = pygame.Surface((width * pixel_size + 2 * self.pixel_size, height * pixel_size + 2 * self.pixel_size))
        self.surface.fill(self.background)
        self.rect = self.surface.get_rect(topleft=(left, top))

        # Initialize the pixels
        self.pixels = pixels
        if not self.pixels:
            for i in range(height):
                self.pixels.append([])
                for j in range(width):
                    pixel_x = j * pixel_size + self.pixel_size
                    pixel_y = i * pixel_size + self.pixel_size
                    self.pixels[i].append(ColorBlock(clr.WHITE, pixel_size, pixel_x, pixel_y, 0))
                    self.surface.blit(self.pixels[i][j].surface, self.pixels[i][j].rect)
        else:
            for i in pixels:
                for j in i:
                    self.surface.blit(j.surface, j.rect)

    def draw(self, window, cursor, click, color):
        # Draw the canvas on the given window, with the given cursor, click, and color
        window.blit(self.surface, self.rect)

        if click:
            cursor = (cursor[0] - self.rect.left, cursor[1] - self.rect.top)
            for row in self.pixels:
                for pixel in row:
                    if pixel.rect.collidepoint(cursor):
                        if pixel.color == color:
                            return
                        index = row.index(pixel)

                        newPixel = ColorBlock(color, pixel.size, pixel.x, pixel.y, pixel.margin, False)
                        row[index] = newPixel
                        self.surface.blit(newPixel.surface, newPixel.rect)

    def getPixels(self):
        # Return the pixels
        return self.pixels

    #Buil numeric matrix
    def getNumericPixels(self): 
        pixels = []

        for i in range(len(self.pixels)):
            pixels.append([])
            for j in range(len(self.pixels[i])):
                color = self.pixels[i][j].color
                num = clr.getColorNumber(color)
                pixels[i].append(num)

        return pixels

    #Build ASCII matrix
    def getASCIIpixels(self):
        pixels = []

        for i in range(len(self.pixels)):
            pixels.append([])
            for j in range(len(self.pixels[i])):
                color = self.pixels[i][j].color
                symbol = clr.getAsciiArtSymbol(color)
                pixels[i].append(symbol)

        return pixels

    #Build high contrast matrix
    def getHighContrastPixels(self):
        pixels = []

        for i in range(len(self.pixels)):
            pixels.append([])
            for j in range(len(self.pixels[i])):
                oldPixel = self.pixels[i][j]
                newColor = clr.getHighContrastColor(oldPixel.color)
                newPixel = ColorBlock(newColor, oldPixel.size, oldPixel.x, oldPixel.y, oldPixel.margin, oldPixel.isBase)
                pixels[i].append(newPixel)

        return pixels

    #Build inverse color matrix
    def getInversePixels(self):
        pixels = []

        for i in range(len(self.pixels)):
            pixels.append([])
            for j in range(len(self.pixels[i])):
                oldPixel = self.pixels[i][j]
                newColor = clr.getInverseColor(oldPixel.color)
                newPixel = ColorBlock(newColor, oldPixel.size, oldPixel.x, oldPixel.y, oldPixel.margin, oldPixel.isBase)
                pixels[i].append(newPixel)

        return pixels

    #Clear the canvas
    def clear(self):
        # Clear the canvas
        for row in self.pixels:
            for pixel in row:
                if not pixel.isBase or pixel.color != clr.WHITE:
                    newPixel = ColorBlock(clr.WHITE, pixel.size, pixel.x, pixel.y, pixel.margin, pixel.isBase)
                    row[row.index(pixel)] = newPixel
                    self.surface.blit(newPixel.surface, newPixel.rect)


    #Redraw the canvas
    def reDraw(self):
        self.surface.fill(self.background)
        for row in self.pixels:
            for pixel in row:
                self.surface.blit(pixel.surface, pixel.rect)

    #Update the pixel coordinates based on their matrix coordinates
    def updatePixelCords(self):
        # Update the pixel coordinates
        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[i])):
                pixelX = j * self.pixel_size + self.pixel_size
                pixelY = i * self.pixel_size + self.pixel_size
                self.pixels[i][j].x = pixelX
                self.pixels[i][j].y = pixelY
                self.pixels[i][j].rect.center = (pixelX, pixelY)

        self.reDraw()

    #Rotate the canvas and its pixels
    def rotate(self, clockwise: bool):
        # Rotate the canvas
        if clockwise:
            self.pixels = list(map(list, zip(*self.pixels[::-1])))
        else:
            self.pixels = list(map(list, zip(*self.pixels)))[::-1]

        self.updatePixelCords()

    def reflect(self, vertical: bool):
        # Reflect the canvas
        if vertical:
            self.pixels = self.pixels[::-1]
        else:
            self.pixels = [row[::-1] for row in self.pixels]

        self.updatePixelCords()

        self.reDraw()

    def magnifyingGlass(self, cursor: tuple[int, int], size: int=100):
        # Create a magnifying glass effect
        cursor = (cursor[0] - self.rect.left, cursor[1] - self.rect.top)

        crop_x = cursor[0] - size // 2
        crop_y = cursor[1] - size // 2
        crop_w = size // 2
        crop_h = size // 2

        if crop_x < 0:
            crop_x = 0
        if crop_y < 0:
            crop_y = 0
        if crop_x + size > self.surface.get_width():
            crop_x = self.surface.get_width() - size
        if crop_y + size > self.surface.get_height():
            crop_y = self.surface.get_height() - size

        croppedRegion = self.surface.subsurface((crop_x, crop_y, crop_w, crop_h))
        magnifiedSurface = pygame.transform.smoothscale(croppedRegion, (size, size))
        finalSF = ImageBlock(croppedRegion, size, crop_x, crop_y, 2).surface

        print(f"Cursor: {cursor}")
        print(f"crop_x: {crop_x}, crop_y: {crop_y}")
        print(f"crop_w: {crop_w}, crop_h: {crop_h}")

        return finalSF