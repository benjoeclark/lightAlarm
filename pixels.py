#!/usr/bin/env python

from Tkinter import Tk, Canvas, ALL
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
            position = [int(center-radius*sin(angle)),
                        int(center-radius*cos(angle))]
            self.pixels.append(Pixel(position, '#000000'))

    def begin(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=300, height=300)
        self.canvas.pack()
        self.window.mainloop()
        self.show()

    def setPixelColor(self, pixelIndex, color):
        """Set the color for pixel pixelIndex to color"""
        colorString = '#'
        colorString += '%0.2x' % color[0]
        colorString += '%0.2x' % color[1]
        colorString += '%0.2x' % color[2]
        self.pixels[pixelIndex].color = colorString
        #self.canvas.itemconfig(self.ovals[pixelIndex], fill=colorString)

    def show(self):
        """Send the updated pixel color to the hardware"""
        for pixelIndex in xrange(self.pixelCount):
            pixel = self.pixels[pixelIndex]
            oval = self.canvas.create_oval(pixel.position[0]-5,
                                    pixel.position[1]-5,
                                    pixel.position[0]+5,
                                    pixel.position[1]+5,
                                    fill=pixel.color)
        #self.canvas.pack()
        #print '\n'.join([pix.color for pix in self.pixels])
