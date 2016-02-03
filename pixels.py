#!/usr/bin/env python

from Tkinter import Tk, Canvas
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
        radius = 50
        for pixelIndex in xrange(pixelCount):
            angle = pixelIndex * (2.0*pi/pixelCount)
            position = [int(center-radius*sin(angle)),
                        int(center-radius*cos(angle))]
            self.pixels.append(Pixel(position, '#000000'))

    def begin(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=300, height=300)

    def setPixelColor(self, pixelIndex, color):
        """Set the color for pixel pixelIndex to color"""
        colorString = '#'
        colorString += '%0.2x' % color[0]
        colorString += '%0.2x' % color[1]
        colorString += '%0.2x' % color[2]
        self.pixels[pixelIndex].color = colorString

    def show(self):
        """Send the updated pixel color to the hardware"""
        print '\n'.join([pix.color for pix in self.pixels])
