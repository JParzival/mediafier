import cv2

from ..utils.utils import intdetector, str2bool

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
        return cv2.copyMakeBorder(img, y, org_h-(y+h), x, org_w-(x+w), cv2.BORDER_CONSTANT, 0)

