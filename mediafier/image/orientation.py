import cv2
import imutils

from ..utils.utils import intdetector, stringdetector, str2bool


def flip(img, axis='horizontal'):
    """
    This function retrieves an image with the flipping desired by the user.

    Args:
        img (:obj: array, mandatory): 
            Image to flip.
        axis (:obj: str, optional): 
            Orientation in which the image has to be flipped (horizontal, vertical or both).
            Default is horizontal.

    Returns:
        :obj: array:
            The resulting object is the image, in the same format as inputted, but with the transformation applied.

    Raises:
        ValueError: Raised if the axis is not inputted correctly.
        ArgumentTypeError: Raised if the axis value is not a string.
    """

    stringdetector(axis)

    if axis == 'horizontal':
        img = cv2.flip(img, 1)
    elif axis == 'vertical':
        img = cv2.flip(img, 0)
    elif axis == 'both':
        img = cv2.flip(img, -1)
    else:
        raise ValueError("Expected axis parameter to be 'horizontal', 'vertical' or 'both', got %s." % (axis))
    return img


def rotate(img, degrees=0, force_fit=False):
    """
    This function retrieves an image with the rotation desired by the user.

    Args:
        img (:obj: array, mandatory): 
            Image to rotate.
        degrees (:obj: int, optional): 
            Degrees (clockwise) that the image has to be rotated. 
            Default is returning the image as it is.
        force_fit(:obj: bool, optional): 
            If the image has to keep the same width and height when rotated (it will be cropped) or it can be resized.
            Default is False.

    Returns:
        :obj: array:
            The resulting object is the image, in the same format as inputted, but with the transformation applied.
            If force_fit == True, remember that the width and height of the image will change if degrees not in 0, 90, 180, 270.

    Raises:
        ValueError: Raised if the axis is not inputted correctly
        ArgumentTypeError: Raised if the axis value is not a string or the force_fit is not a boolean or something convertible to boolean.
    """

    def _easy_rotation(img, degrees):
        if degrees == 0:
            return img
        elif degrees == 90:
            return cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
        elif degrees == 180:
            return cv2.rotate(img, cv2.cv2.ROTATE_180)
        elif degrees == 270:
            return cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

    intdetector(degrees)
    str2bool(force_fit)

    if degrees in [0, 90, 180, 270]:
        return _easy_rotation(img, degrees)
    else:
        if degrees > 359 or degrees < 0:
            raise ValueError("Expected degrees parameter to be among 0 and 359, got %s." % (degrees))

        if not force_fit:
            (h, w) = img.shape[:2]
            (cX, cY) = (w // 2, h // 2)

            # Perform the rotation
            M = cv2.getRotationMatrix2D((cX, cY), -degrees, 1.0)
            return cv2.warpAffine(img, M, (w, h))
        else:
            return imutils.rotate_bound(img, degrees)
