import cv2

from ..utils.utils import intdetector, str2bool
from ..image.size import addBorders

def crop(img, x, y, w, h, fill=False):
    """
    This function retrieves the image sent by the user cropped with the coordinates that the user inputs.

    Args:
        img (:obj: array, mandatory): 
            Image to crop
        x (:obj: int, mandatory): 
            X coordinate of the closest point to the 0,0
        y (:obj: int, mandatory): 
            Y coordinate of the closest point to the 0,0
        w (:obj: int, mandatory): 
            Width of the crop in pixels
        h (:obj: int, mandatory): 
            Height of the crop in pixels
        fill (:obj: bool, optional): 
            If the image dimensions should be mantained filling the borders

    Returns:
        :obj: array:
            The resulting object is the image, in the same format as inputted, but with the transformation applied.

    Raises:
        ValueError: Raised if any of the values of the size is not positive.
        ArgumentTypeError: Raised if any of the values of the is not an int or the fill is not a bool.
    """

    for n in [x, y, w, h]:
        intdetector(n)
        if n < 0:
            raise ValueError("All values must be positive")
    str2bool(fill)
    
    if fill == False:
        return img[y:y+h, x:x+w]
    else:
        org_w, org_h = img.shape[0], img.shape[1]
        img = img[y:y+h, x:x+w]
        return addBorders(img, y, org_h-(y+h), x, org_w-(x+w), 'constant', 'black')


def slice(img, rows=2, cols=2):
    """
    This function retrieves the image sent by the user sliced in several images, depending on the rows and cols that the user inputs.

    Args:
        img (:obj: array, mandatory): 
            Image to slice.
        rows (:obj: int, mandatory): 
            Number of rows that will slice the image.
            Default is 2.
        cols (:obj: int, mandatory): 
            Number of columns that will slice the image.
            Default is 2.

    Returns:
        :obj: array[array]:
            The resulting object an array with the images. They will be ordered by from the up-left one to the bottom-right one,
            following a first row - later column fashion.

    Raises:
        ValueError: Raised if any of the values of the size is not positive and over zero.
        ArgumentTypeError: Raised if any of the values of the is not an int or the fill is not a bool.
    """
    
    for n in [rows, cols]:
        intdetector(n)
        if n <= 0:
            raise ValueError("All values must be positive and over zero")

    if rows == 1 and cols == 1:
        return [img]

    height, width = img.shape[0], img.shape[1]

    height_chunk = height/rows
    width_chunk = width/cols

    sliced = []
    w, h = 0, 0
    while h < height:
        while w < width:
            sliced.append(crop(img, int(w), int(h), int(width_chunk), int(height_chunk), False))
            w += width_chunk
        w = 0
        h += height_chunk
    return sliced
            


    