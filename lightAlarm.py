#!/usr/bin/env python

import time


def colorWipe(pixels, color, wait):
    for pixelIndex in xrange(pixels.pixelCount):
        pixels.setPixelColor(pixelIndex, color)
        time.sleep(wait)
        pixels.show()


if __name__=='__main__':
    from pixels import *
    pixels = Pixels()
    colorWipe(pixels, [127, 127, 127], 1)
