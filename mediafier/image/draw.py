import cv2

from ..utils.utils import intdetector, str2bool, stringdetector

def drawBBox(img, x, y, w, h, color='black', thickness=2):
    """
    This function retrieves an image with the bounding box that the user inputs painted.

    Args:
        img (:obj: array, mandatory): 
            Image to flip.
        x (:obj: int, mandatory): 
            X point of the first point (uppermost and leftmost)
        y (:obj: int, mandatory): 
            Y point of the first point (uppermost and leftmost)
        w (:obj: int, mandatory): 
            Width of the bounding box
        h (:obj: int, mandatory): 
            Height of the bounding box
        color (:obj: str, optional): 
            Color that the bounding box will have.
            Options are:
                - black
                - white
                - red
                - blue
            Defaults to black
        thickness (:obj: int, optional):
            Thickness that the bounding box will have.
            Defaults to 2.

    Returns:
        :obj: array:
            The resulting object is the image, in the same format as inputted, but with the transformation applied.

    Raises:
        ValueError: Raised if any of the values is not inputted properly.
        ArgumentTypeError: Raised if any of the values does not have the proper type.
    """

    def _checks(x, y, w, h, color, thickness):
        stringdetector(color)
        color = color.lower()

        if color not in ['black', 'white', 'red', 'blue']:
            raise ValueError("Supported colors are 'black', 'white', 'red' and 'blue'")

        intdetector(x)
        intdetector(y)
        intdetector(w)
        intdetector(h)

        if x < 0 or y < 0 or w < 0 or h < 0:
            raise ValueError("Values must be positive!")
        
        intdetector(thickness)
        if thickness <= 0:
            raise ValueError("Thickness must be over zero!")

        return color

    def _colorChoice(color):
        if color == 'black':
            return (0, 0, 0)
        elif color == 'white':
            return (255, 255, 255)
        elif color == 'red':
            return (0, 0, 255)
        elif color == 'blue':
            return (255, 0, 0)


    color = _checks(x, y, w, h, color, thickness)
    color = _colorChoice(color)

    return cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness)