import cv2
import os

from ..utils.utils import intdetector, stringdetector, str2bool
from ..image import size

def extractFrames(videoPath, save='memory', savePath=None, format='png', every=1, resize=False, newWidth=None, newHeight=None):
    """
        This function extracts the frames of a video that the user inputs by a path.
        It has several parameters that make it fully customisable, that are explained in the following lines

        Args:
            videoPath (:obj: str, mandatory): 
                Path to the video, with the video included in the string. (e.g. path/to/video.avi)
            save (:obj: str, optional): 
                String that makes the decision of where to save the frames of the video.
                There are two options:
                    - memory: The frames will be stored in a list that will be returned.
                    - disk: The frames will be saved in the 'savePath' path.
                Default: memory
            savePath (:obj: str, optional): 
                Used if save='disk'.
                Path to the folder where the frames will be saved. (e.g. /path/to/folder/)
            format (:obj: string, optional):
                Used if save='disk'.
                Format in which the frames are going to be saved.
                There are two options:
                    - png: To store the images in PNG format.
                    - jpg: To store the images in JPG format.
                Default: 'png'
            every (:obj: int, optional):
                Indicates if every frame has to be saved or some of them have to be skipped.
                E.g.: every = 1 saves every frame, while every=2 saves one of every two frames.
                Default: 1
            resize (:obj: bool, optional):
                Indicates if the frames have to be resized before storing them.
                Default: False
            newWidth (:obj: int, optional):
                Used only if resize = True.
                Indicates the new width, in pixels, that the image will have.
            newHeight (:obj: int, optional):
                Used only if resize = True.
                Indicates the new height, in pixels, that the image will have.
        Returns:
            if save is memory:
                :obj: array:
                    An array of images is returned, being the first one the first frame and the last one the last frame of the video
            if save is disk:
                :obj: bool:
                    A True is returned when the process has ended

        Raises:
            ValueError: Raised if any of the values is not correct.
            ArgumentTypeError: Raised if any of the types of the values is not proper.
        """

    def _prep(save, format):
        save = save.lower()
        format = format.lower()

        if format == '.png':
            format = 'png'
        elif format == '.jpg':
            format = 'jpg'
        return save, format

    def _checks(videoPath, save, savePath, format, every, resize):
        stringdetector(videoPath)
        if not os.path.exists(videoPath):
            os.makedirs(videoPath)

        stringdetector(save)
        if save not in ['memory', 'disk']:
            raise ValueError("Save parameter must be 'memory' or 'disk'")

        if save == 'disk':
            if savePath is None:
                raise ValueError("As we are saving on disk, please, provide a proper savePath")
            stringdetector(savePath)

        stringdetector(format)
        if format not in ['jpg', 'png']:
            raise ValueError("Format parameter must be 'png' or 'jpg'")

        intdetector(every)
        if every <= 0:
            raise ValueError("Every parameter must be over zero")

        str2bool(resize)
        if resize == True:
            intdetector(newWidth)
            intdetector(newHeight)
            if newWidth <= 0 or newHeight <= 0:
                raise ValueError("The new values of height and width must be over zero")

    save, format = _prep(save, format)
    _checks(videoPath, save, savePath, format, every, resize)

    video = cv2.VideoCapture(videoPath)

    obsFrames = 0
    saved_frames = []
    while(video.isOpened()):
        ret, frame = video.read()

        if obsFrames % every != 0:
            obsFrames = obsFrames + 1
            continue

        if not ret: #End of video or sudden death :)
            break

        if resize:
            size.resize(frame, size=(newWidth, newHeight))

        if save == 'disk':
            if not os.path.exists(savePath):
                os.makedirs(savePath)
            cv2.imwrite(os.path.join(savePath, f"frame_{str(obsFrames)}.{format}"), frame)
        elif save == 'memory':
            saved_frames.append(frame)
        obsFrames = obsFrames + 1

    video.release()

    if save == 'disk':
        return True
    elif save == 'memory':
        return saved_frames