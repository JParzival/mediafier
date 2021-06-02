import cv2

from ..utils.utils import intdetector, stringdetector, str2bool

def blur(img, method='default', value='medium'):
    """
        This function retrieves an image with the amount of blur that the user inputs.

        Args:
            img (:obj: array, mandatory): 
                Image to modify.
            method (:obj: str, optional): 
                Method that will be applied to make the transformation.
                Possible values are:
                    - default
                    - gaussian
                Defaults to 'default'
            value (:obj: str, optional): 
                Amount of blurriness that will be applied to the image.
                Possible values are:
                    - extreme
                    - high
                    - medium
                    - low
                Defaults to 'medium'

        Returns:
            :obj: array:
                The resulting object is the image, in the same format as inputted, but with the transformation applied.

        Raises:
            ValueError: Raised if any of the values is not inputted properly.
            ArgumentTypeError: Raised if any of the values does not have the proper type.
        """

    def _checks(img, method, value):
        stringdetector(method)
        method = method.lower()
        if method not in ['default', 'gaussian']:
            raise ValueError("Method parameter must be 'default' or 'gaussian'")

        stringdetector(value)
        value = value.lower()
        if value not in ['extreme', 'high', 'medium', 'low']:
            raise ValueError("Value must be 'extreme', 'high', 'medium' or 'low'")

        return method, value

    def _valuechoice(method, value):
        if method == 'default':
            if value == 'extreme':
                return (75,75)
            elif value == 'high':
                return (50, 50)
            elif value == 'medium':
                return (35, 35)
            else:
                return (10, 10)
        else:       # In gaussian, return odd values
            if value == 'extreme':
                return (149, 149)
            elif value == 'high':
                return (99, 99)
            elif value == 'medium':
                return (49, 49)
            else:
                return (25, 25)

    method, value = _checks(img, method, value)

    if method == 'default':
        return cv2.blur(img, _valuechoice(method, value))
    else:
        return cv2.GaussianBlur(img, _valuechoice(method, value), 0, 0)