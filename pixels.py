#!/usr/bin/env python

import pygame
from math import sin, cos, pi

class Pixel:
    def __init__(self, position, color):
        self.position = position
        self.color = color

class Pixels:
    def __init__(self, pixelCount=24):
        self.pixelCount = pixelCount
        self.pixels = []
        center = 150
        radius = 100
        for pixelIndex in xrange(pixelCount):
            angle = pixelIndex * (2.0*pi/pixelCount)
            position = [int(center+radius*sin(angle)),
                        int(center-radius*cos(angle))]
            self.pixels.append(Pixel(position, (0, 0, 0)))

    def begin(self):
        pygame.init()
        self.window = pygame.display.set_mode((300, 300))
        self.window.fill((0, 0, 0))
        self.show()

    def setPixelColor(self, pixelIndex, color):
        """Set the color for pixel pixelIndex to color"""
        self.pixels[pixelIndex].color = color

    def show(self):
        """Send the updated pixel color to the hardware"""
        self.window.fill((0, 0, 0))
        for pixelIndex in xrange(self.pixelCount):
            pixel = self.pixels[pixelIndex]
            pygame.draw.circle(self.window, pixel.color, pixel.position, 5)
        pygame.display.update()
