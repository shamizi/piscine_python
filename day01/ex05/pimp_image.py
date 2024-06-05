from load_image import ft_load
from PIL import Image
import numpy as np

def ft_invert(array) -> np.ndarray:
    """
    Invert the image colors.
    """
    image = 255 - array
    Image.fromarray(image).show()
    return image

def ft_red(array) -> np.ndarray:
    """
    Converts the image to red.
    """
    image = array.copy()
    image[:,:,1] = 0
    image[:,:,2] = 0
    Image.fromarray(image).show()
    return image

def ft_green(array) -> np.ndarray:
    """
    Converts the image to green.
    """
    image = array.copy()
    image[:,:,0] = 0
    image[:,:,2] = 0
    Image.fromarray(image).show()
    return image

def ft_blue(array) -> np.ndarray:
    """
    Converts the image to blue.
    """
    image = array.copy()
    image[:,:,0] = 0
    image[:,:,1] = 0
    Image.fromarray(image).show()
    return image

def ft_grey(array) -> np.ndarray:
    """
    Converts the image to greyscales.
    """
    red_channel = array[:, :, 0] / 3
    green_channel = array[:, :, 1] / 3
    blue_channel = array[:, :, 2] / 3
    grey_channel = red_channel + green_channel + blue_channel
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)
    Image.fromarray(grey_image.astype(np.uint8)).show()
    return grey_image

array = ft_load("landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)
