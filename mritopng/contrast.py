import numpy as np
from . import GrayscaleImage

def histogram(image):
    
    hist = dict()

    # Initialize dict
    for shade in range(0, 256):
        hist[shade] = 0
    
    for index, val in np.ndenumerate(image.image):
        hist[val] += 1
      
    return hist


def shade_at_percentile(hist, percentile):

    n = sum(hist.values())
    cumulative_sum = 0.0
    for shade in range(0, 256):
        cumulative_sum += hist[shade]
        if cumulative_sum/n >= percentile:
            return shade
    
    return None

def auto_contrast(image):
    """ Apply auto contrast to an image using
        https://stackoverflow.com/questions/9744255/instagram-lux-effect/9761841#9761841
    """
    hist = histogram(image)
    p5 = shade_at_percentile(hist, 0.05)
    p95 = shade_at_percentile(hist, 0.95)
    a = 255.0/(p95 + p5)
    b = -1.0 * a * p5

    result = (image.image.astype(float) * a) + b
    
    return GrayscaleImage(np.uint8(result), image.width, image.height)