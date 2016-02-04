#!/usr/bin/env python

import time


def colorWipe(pixels, color, wait):
    for pixelIndex in xrange(pixels.pixelCount):
        pixels.setPixelColor(pixelIndex, color)
        pixels.show()
        time.sleep(wait)


if __name__=='__main__':
    from pixels import *
    pixels = Pixels()
    pixels.begin()
    colorWipe(pixels, [127, 127, 127], 1)
