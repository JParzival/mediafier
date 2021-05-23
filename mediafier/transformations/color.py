import cv2
import numpy as np

from ..utils.utils import floatdetector, stringdetector


def modify_contrast(img, value=1, method='default'):
    """
    This function retrieves an image with the contrast modified.

    Args:
        img (:obj: array, mandatory): 
            Image to flip.
        value (:obj: float, optional): 
            If the method is 'default', it will be the weight of the contrast applied.
            If the method is CLAHE, it will be the clip limit while applying the method.
        method (:obj: str, optional):
            With the default method, a more common constrast technique is applied.
            With the CLAHE method, the AHE method is applied. Check the appendix for an explanation.

    Returns:
        :obj: array:
            The resulting object is the image, in the same format as inputted, but with the transformation applied.

    Raises:
        ValueError: Raised if the value inputted is less than zero or the param is not between the accepted.
        ArgumentTypeError: Raised if any value does not have its correct format.

    Appendix:
        (CL) AHE is a computer image processing technique used to improve contrast in images. 
        It differs in some things from the ordinary histogram equalization, like in the respect that the adaptive method computes several histograms, 
        each corresponding to a completely distinct section of the image, and uses them to redistribute the lightness values of the image. 
        AHE is therefore suitable for improving the local contrast and enhancing the definitions of edges in each region of an image. 
        And, also, AHE has a tendency to over-amplify noise in relatively homogeneous regions of an image, so be careful not to overextend the clip value.
    """

    floatdetector(value)
    stringdetector(method)
    method = method.lower()
    if method not in ['default', 'clahe']:
        raise ValueError("Expected method parameter to be 'default', or 'CLAHE', got %s." % (method))
    if value < 0:
        raise ValueError("Expected value parameter to be positive, got %s." % (value))

    if method == "clahe":
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=value, tileGridSize=(8,8))
        limg = cv2.merge((clahe.apply(l),a,b))
        return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    else:
        return cv2.addWeighted(img, value, img, 0, 1)


def modify_brightness(img, value=1):
    """
    This function retrieves an image with the brightness modified.

    Args:
        img (:obj: array, mandatory): 
            Image to flip.
        value (:obj: float, optional): 
            The weight of the brightness applied.

    Returns:
        :obj: array:
            The resulting object is the image, in the same format as inputted, but with the transformation applied.

    Raises:
        ValueError: Raised if the value inputted is less than zero or the param is not between the accepted.
        ArgumentTypeError: Raised if any value does not have its correct format.
    """

    floatdetector(value)

    if value == 1:
        return img
    else:
        return cv2.convertScaleAbs(img, alpha=value, beta=1)
 