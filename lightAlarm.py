#!/usr/bin/env python

import time

OFF = (0, 0, 0)
ON = (255, 255, 255)

class PixelControl:
    def __init__(self, pixels):
        self.pixels = pixels
        self.pixels.begin()

    def colorWipe(self, color, wait):
        for pixelIndex in xrange(self.pixels.pixelCount):
            self.pixels.setPixelColor(pixelIndex, color)
            self.pixels.show()
            time.sleep(wait)

    def setAllPixels(self, color):
        for pixelIndex in xrange(self.pixels.pixelCount):
            self.pixels.setPixelColor(pixelIndex, color)

    def clearPixels(self):
        self.setAllPixels(OFF)

    def wrap(self, index):
        if index >= self.pixels.pixelCount:
            index -= self.pixels.pixelCount
        if index < 0:
            index += self.pixels.pixelCount
        return index

    def clock(self, hour, minute):
        self.clearPixels()
        hourIndex = self.wrap(int(hour * self.pixels.pixelCount / 12.))
        previousHourIndex = self.wrap(hourIndex - 1)
        nextHourIndex = self.wrap(hourIndex + 1)
        self.pixels.setPixelColor(previousHourIndex, (255, 0, 0))
        self.pixels.setPixelColor(hourIndex, (255, 0, 0))
        self.pixels.setPixelColor(nextHourIndex, (255, 0, 0))
        minuteIndex = self.wrap(int(minute * self.pixels.pixelCount / 60.0))
        self.pixels.setPixelColor(minuteIndex, (0, 0, 255))
        self.pixels.show()

    def clockSweep(self):
        done = False
        hour = 1
        minute = 0
        while not done:
            self.clock(hour, minute)
            time.sleep(0.05)
            minute += 1
            if minute > 60:
                minute = 0
                hour += 1
            if hour > 12:
                done = True

    def percentOn(self, index, count):
        value = int(255 * (index+1) / count)
        return (value, value, value)

    def sunrise(self):
        halfwayPoint = self.pixels.pixelCount / 2
        for step in xrange(halfwayPoint):
            color = self.percentOn(step, halfwayPoint+1)
            upperIndex = self.wrap(halfwayPoint + step)
            lowerIndex = self.wrap(halfwayPoint - step)
            for pixelIndex in xrange(upperIndex - lowerIndex + 1):
                self.pixels.setPixelColor(lowerIndex + pixelIndex, color)
            self.pixels.show()
            time.sleep(1)
        self.setAllPixels(ON)
        self.pixels.show()
        time.sleep(2)

if __name__=='__main__':
    from pixels import *
    pixels = Pixels()
    pixels.begin()
    colorWipe(pixels, (127, 127, 0), 0.01)
    colorWipe(pixels, (0, 255, 0), 0.01)
    control = PixelControl(Pixels())
    #control.sunrise()
    control.clockSweep()
    control.colorWipe((127, 127, 0), 0.2)
