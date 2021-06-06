import cv2

from ..utils.utils import intdetector, str2bool, stringdetector

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


def addBorders(img, top=0, bottom=0, left=0, right=0, borderType='constant', color='black'):
    """
        This function adds borders to the sides of the image the user wants.
        This borders can be white or black, or may have other effects, like reflections.

        Args:
            img (:obj: array, mandatory): 
                Image which is going to be added borders.
            top (:obj: int, optional): 
                Integer which indicates the number of pixels to add in top of the image.
                Defaults to 0.
            bottom (:obj: int, optional): 
                Integer which indicates the number of pixels to add in the bottom of the image.
                Defaults to 0.
            left (:obj: int, optional): 
                Integer which indicates the number of pixels to add in the left side of the image.
                Defaults to 0.
            right (:obj: int, optional): 
                Integer which indicates the number of pixels to add in the right side of the image.
                Defaults to 0.
            borderType(:obj: string, optional): 
                Type of border that the user wants to add to the image.
                There are several options:
                    - Constant: Solid border, and the user can choose color.
                    - Reflect: The border will mirror the border elements.
                    - Default: Quite similar to 'reflect', but with slight changes.
                    - Replicate: Replicates the last element of the image.
                Defaults to constant.
            color(:obj: string, optional):
                This param is only triggered if borderType is constant.
                The user can choose between two colors to add:
                    - Black
                    - White
                Defaults to black.

        Returns:
            :obj: array:
                The resulting object is the image, in the same format as inputted, but with the transformation applied.

        Raises:
            ValueError: Raised if any of the values is negative or not expected.
            ArgumentTypeError: Raised if any of the values is not the type that it is supposed to.
    """

    def _checks(img, top, bottom, left, right, borderType, color):
        intdetector(top)
        intdetector(bottom)
        intdetector(left)
        intdetector(right)
        if top < 0 or bottom < 0 or left < 0 or right < 0:
            raise ValueError("Values must be over zero")
        stringdetector(borderType)
        borderType = borderType.lower()
        if borderType not in ['constant', 'reflect', 'default', 'replicate']:
            raise ValueError("Border types are 'constant', 'reflect', 'default' and 'replicate'")
        if borderType == 'constant':
            stringdetector(color)
            color = color.lower()
            if color not in ['black', 'white']:
                raise ValueError("Supported colors are 'black' and 'white'")
        return borderType, color

    
    def _borderChoice(borderType):
        if borderType == 'constant':
            return cv2.BORDER_CONSTANT
        elif borderType == 'reflect':
            return cv2.BORDER_REFLECT
        elif borderType == 'default':
            return cv2.BORDER_DEFAULT
        else:
            return cv2.BORDER_REPLICATE


    def _colorChoice(color):
        if color == 'black':
            return [0, 0, 0]
        else:
            return [255, 255, 255]


    borderType, color = _checks(img, top, bottom, left, right, borderType, color)
    border = _borderChoice(borderType)

    if top == 0 and bottom == 0 and left == 0 and right == 0:
        return img

    if borderType == 'constant':
        color = _colorChoice(color)
        return cv2.copyMakeBorder(img, top, bottom, left, right, border, value=color)
    else:
        return cv2.copyMakeBorder(img, top, bottom, left, right, border)

    
