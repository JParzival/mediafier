import cv2

from ..utils.utils import intdetector, str2bool

def resize(img, ratio=100, size=None, interpolation=None):
    """
    This function retrieves the image sent by the user resized with the ratio or the size inputted by the user.
    The ratio has priority over the size in case that it is modified from the default value.

    Args:
        img (:obj: array, mandatory): 
            Image to rotate.
        size (:obj: tuple, optional): 
            Tuple with the new size of the image in (width, height) format.
        ratio(:obj: int, optional): 
            Number, in percentage, that indicates the percentage of upscaling or downscaling that the image will have applied.
            Default is returning the image as it is.
        interpolation(:obj: string, optional):
            Type of interpolation that will be applied to the image.
            Default is area if resize is not to a bigger one. In case of smaller resize, linear interpolation is the default.

    Returns:
        :obj: array:
            The resulting object is the image, in the same format as inputted, but with the transformation applied.
            If force_fit == True, remember that the width and height of the image will change if degrees not in 0, 90, 180, 270.

    Raises:
        ValueError: Raised if any of the values of the size is negative.
        ArgumentTypeError: Raised if any of the values of the size tuple is not an int or the ratio is not a positive int.
    """

    def _interpolation_choice(interpolation):
        if interpolation is None:              # Set a default
            if size is not None:
                if (ratio >= 100) or (size[0] >= img.shape[0]) or (size[1] >= img.shape[1]):
                    interpolation = cv2.INTER_AREA
                else:
                    interpolation = cv2.INTER_LINEAR
            else:
                if ratio >= 100:
                    interpolation = cv2.INTER_AREA
                else:
                    interpolation = cv2.INTER_LINEAR

        elif interpolation in ["nearest", cv2.INTER_NEAREST]:
            interpolation = cv2.INTER_NEAREST
        elif interpolation in ["linear", cv2.INTER_LINEAR]:
            interpolation = cv2.INTER_LINEAR
        elif interpolation in ["area", cv2.INTER_AREA]:
            interpolation = cv2.INTER_AREA
        else:
            interpolation = cv2.INTER_CUBIC
        
        return interpolation

    # Checks over ratio
    intdetector(ratio)
    if ratio <= 0:
        raise ValueError("Expected ratio parameter to be over zero")

    # Checks over size if necessary
    if size is not None:
        intdetector(size[0])
        intdetector(size[1])
        if size[0] == img.shape[0] and size[1] == img.shape[1]:
            return img
        if size[0] < 0 or size[1] < 0:
            raise ValueError("Expected size parameter to be a tuple with values over 0")

    interpolation = _interpolation_choice(interpolation)

    if ratio != 100:    # Ratio has the priority if inputted
        size = ( int(img.shape[1] * ratio / 100), int(img.shape[0] * ratio / 100) )
        return cv2.resize(img, size, interpolation = interpolation)
    if size is not None:   # If ratio has not been modified, let's check size if inputted
        return cv2.resize(img, size, interpolation = interpolation)
    else:
        return img

def crop(img, x, y, w, h, fill=False):
    """
    This function retrieves the image sent by the user resized with the ratio or the size inputted by the user.
    The ratio has priority over the size in case that it is modified from the default value.

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
        ArgumentTypeError: Raised if any of the values of the size tuple is not an int.
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
