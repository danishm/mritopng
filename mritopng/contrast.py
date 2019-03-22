import numpy as np
from .models import GrayscaleImage

def shade_at_percentile(hist, percentile):
    """ Assumes the argument percentile,
        to be less 1.
    """
    n = np.sum(hist)
    cumulative_sum = np.cumsum(hist)
    
    return np.argmax(cumulative_sum/n >= percentile)

def auto_contrast(image):
    """ Apply auto contrast to an image using
        https://stackoverflow.com/questions/9744255/instagram-lux-effect/9761841#9761841
    """
    hist, _ = np.histogram(image.image.ravel(), bins=np.arange(0, 256))
    p_low = shade_at_percentile(hist, .01)
    p_high = shade_at_percentile(hist, .99)
    a = 255.0/(p_high - p_low)
    b = -1.0 * a * p_low

    result = (image.image.astype(float) * a) + b
    result = result.clip(0, 255.0)
    
    return GrayscaleImage(np.uint8(result), image.width, image.height)