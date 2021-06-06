import cv2
import numpy as np
from sklearn.cluster import KMeans

from ..utils.utils import floatdetector, intdetector, stringdetector


def modifyContrast(img, value=1, method='default'):
    """
        This function retrieves an image with the contrast modified from an image.
        In case of using the CLAHE method, the image must be in the BGR colorspace.

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


def modifyBrightness(img, value=1):
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
 

def changeBGRColorspace(img, to='gray'):
    """
        This function, from a BGR image, retrieves another one with the colorspace modified.

        Args:
            img (:obj: array, mandatory): 
                Image to flip.
            to (:obj: str, optional): 
                The colorspace that the image is going to be converted to
                The accepted values are:
                    - gray
                    - hsv
                    - hls
                    - lab
                    - luv
                    - yuv
                    - rgb
                Defaults to 'gray'

        Returns:
            :obj: array:
                The resulting object is the image, in the same format as inputted, but with the transformation applied.

        Raises:
            ValueError: Raised if the value inputted is not between the accepted.
            ArgumentTypeError: Raised if any value does not have its correct format.
    """


    def _checks(to):
        stringdetector(to)
        to = to.lower()
        if to not in ['gray', 'hsv', 'hls', 'lab', 'luv', 'yuv', 'rgb']:
            raise ValueError("Not an accepted colorspace to convert to")
        return to
    
    to = _checks(to)

    if to == "gray":
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif to == "hsv":
        return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif to == "hls":
        return cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    elif to == "lab":
        return cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    elif to == "luv":
        return cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
    elif to == "yuv":
        return cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    elif to == "rgb":
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    else:
        return img


def findMostCommonColor(img, method='frequency', clusters=3):
    """
        This function finds the most common color of the image using different methods.

        Args:
            img (:obj: array, mandatory): 
                Image to flip.
            method (:obj: str, optional): 
                Method that will be applied.
                Possible values are:
                    - average: This method brings back the average color of the image
                    - frequency: This method brings back the most common color of the image
                    - kmeans: This method, using kmeans, brings back the most common colors of the image
                Defaults to 'frequency'.
            clusters (:obj: int, optional):
                Number of clusters, and therefore colors, that the kmeans will train to get the colors.
                Defaults to 3.

        Returns:
            Methods average and frequency:
            :obj: array:
                The resulting object an array with the colors in BGR format.
            :obj: array:
                Image ready to be painted with the main color.

            Method kmeans:
            :obj: array:
                The resulting object an array of arrays with the colors in BGR format for every centroid.
            :obj: array:
                Image ready to be painted with the palette of the main colors.

        Raises:
            ValueError: Raised if the value inputted is less than one or the param is not between the accepted.
            ArgumentTypeError: Raised if any value does not have its correct format.
    """

    def _checks(method, clusters):
        stringdetector(method)
        method = method.lower()
        if method not in ['average', 'frequency', 'kmeans']:
            raise ValueError("Method must be 'average', 'frequency' or 'kmeans'")
        
        if method == 'kmeans':
            intdetector(clusters)
            if clusters < 1:
                raise ValueError("Value of clusters must be one or above")

        return method

    def _palette(clusters):
        width=300
        palette = np.zeros((50, width, 3), np.uint8)
        steps = width/clusters.cluster_centers_.shape[0]
        for idx, centers in enumerate(clusters.cluster_centers_): 
            palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers
        return palette

    method = _checks(method, clusters)

    if method == 'average':
        img_temp = img.copy()
        img_temp[:,:,0], img_temp[:,:,1], img_temp[:,:,2] = np.average(img, axis=(0,1))

        return [np.unique(img_temp[:,:,0]), 
                np.unique(img_temp[:,:,1]), 
                np.unique(img_temp[:,:,2])], img_temp

    elif method == 'frequency':
        img_temp = img.copy()
        unique, counts = np.unique(img_temp.reshape(-1, 3), axis=0, return_counts=True)
        img_temp[:,:,0], img_temp[:,:,1], img_temp[:,:,2] = unique[np.argmax(counts)]
        return [np.unique(img_temp[:,:,0]), 
                np.unique(img_temp[:,:,1]), 
                np.unique(img_temp[:,:,2])], img_temp

    elif method == 'kmeans':
        img_temp = img.copy()
        clt_3 = KMeans(n_clusters=clusters)
        clt_3.fit(img_temp.reshape(-1, 3))
        return clt_3.cluster_centers_, _palette(clt_3)