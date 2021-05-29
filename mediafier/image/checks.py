import cv2
import os
import numpy as np

from ..utils.utils import intdetector, str2bool, stringdetector


def isBlurry(img, strictness='high', customStrictness=None):
    """
    This function checks if an image is blurry or not.
    As images can have a wide spectrum of cases, both a general parameter of blurriness and a 
    custom one has been provided so that the user can use the function in any case.

    Args:
        img (:obj: array, mandatory): 
            Image to check.
        strictness (:obj: str, optional): 
            Level of strictness to apply to check if the image is blurry or not.
            The possible values are:
                - High: Very restrictive
                - Medium: Midly restrictive
                - Low: Barely restrictive
            Default is high.
        customStrictness (:obj: int, optional):
            As explained before, images can have a wide variety of cases that make this blurriness detector obsolete.
            The user can input a custom value after trying some of his/her use case that fits perfectly for them.
            If used, this parameter overrides the strictness one.

    Returns:
        :obj: bool:
            The result of the function is a boolean, checking if the image is blurry or not.
        :obj: int:
            A second output is the value of blurriness, so that the user can know the amount of blurriness.

    Raises:
        ValueError: Raised if the value inputted is less than/or zero or the param is not among the accepted.
        ArgumentTypeError: Raised if any value does not have its correct format.

    Appendix:
        This function uses the fast fourier transform to check whether an image is blurry or not.
    """

    integer_types = (int)
    def _fftshift(fft, axes=None):
        x = np.asarray(fft)
        if axes is None:
            axes = tuple(range(x.ndim))
            shift = [dim // 2 for dim in x.shape]
        elif isinstance(axes, integer_types):
            shift = x.shape[axes] // 2
        else:
            shift = [x.shape[ax] // 2 for ax in axes]
        return np.roll(x, shift, axes)


    def _ifftshift(fftShift, axes=None):
        x = np.asarray(fftShift)
        if axes is None:
            axes = tuple(range(x.ndim))
            shift = [-(dim // 2) for dim in x.shape]
        elif isinstance(axes, integer_types):
            shift = -(x.shape[axes] // 2)
        else:
            shift = [-(x.shape[ax] // 2) for ax in axes]
        return np.roll(x, shift, axes)

    def _detect_blur_fft(image, size=60, thresh=50000000):
        (h, w) = image.shape
        (cX, cY) = (int(w / 2.0), int(h / 2.0))

        fft = cv2.dft(np.float32(image))
        fftShift = _fftshift(fft)
        fftShift[cY - size:cY + size, cX - size:cX + size] = 0
        fftShift = _ifftshift(fftShift)
        recon = cv2.idft(fftShift)
        
        magnitude = 20 * np.abs(recon)
        mean = np.mean(magnitude)
        if mean > thresh:
            var = False
        else:
            var = True
        return (mean, var)

    def _blur_process(frame_gray, blurthresh):
        (mean, blurry) = _detect_blur_fft(frame_gray, size=60, thresh=blurthresh)
        return blurry, mean

    def _thresholds(strictness):
        if strictness == 'low':
            return 30000000
        elif strictness == 'medium':
            return 50000000
        else:
            return 70000000

    def _checks(img, strictness, customStrictness):
        if customStrictness is not None:
            intdetector(customStrictness)
            if customStrictness <= 0:
                raise ValueError("CustomStrictness cannot be negative nor zero")
            return strictness, customStrictness
        else:
            stringdetector(strictness)
            strictness = strictness.lower()
            if strictness not in ['low', 'medium', 'high']:
                raise ValueError("Strictness parameter should be 'high', 'medium' or 'low'")
            return strictness, customStrictness

        
    strictness, customStrictness = _checks(img, strictness, customStrictness)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if customStrictness is None:
        return _blur_process(img_gray, _thresholds(strictness))
    else:
        return _blur_process(img_gray, customStrictness)