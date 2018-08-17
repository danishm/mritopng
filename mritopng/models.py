class GrayscaleImage(object):
    
    def __init__(self, image, width, height):
        self.image = image
        self.width = width
        self.height = height
    
    def __str__(self):
        return '[%dx%d]' % (self.width, self.height)