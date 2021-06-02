import cv2
import os 
from mediafier.video.common import extractFrames, modifyFps

SRC_IMG_DIR = os.path.join('test_media', 'video_src_test')
SAVE_IMG_DIR = os.path.join('test_media', 'video_result_test', 'common')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_video_common_extractFrames():

    """
    Not with the other tests fashion, cause it would be much more work to make it that fashion for no benefit
    """

    video = os.path.join(SRC_IMG_DIR, 'test2.mp4')

    """Extract in memory one of every 20"""
    frames = extractFrames(video, every=20)
    i = 0
    savepath = os.path.join(SAVE_IMG_DIR, 'test1')
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    for frame in frames:
        cv2.imwrite(os.path.join(savepath, f'frame_{i}.png'), frame)
        i += 1

    """Extract in disk in png"""
    savepath = os.path.join(SAVE_IMG_DIR, 'test2')
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    ok = extractFrames(video, save='disk', savePath=savepath)

    """Extract in disk in jpg"""
    savepath = os.path.join(SAVE_IMG_DIR, 'test3')
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    ok = extractFrames(video, save='disk', savePath=savepath, format='jpg')

    """Extract in disk in jpg every 30"""
    savepath = os.path.join(SAVE_IMG_DIR, 'test4')
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    ok = extractFrames(video, save='disk', savePath=savepath, format='jpg', every=30)

    """Extract in disk every 30 resizing the jpg"""
    savepath = os.path.join(SAVE_IMG_DIR, 'test5')
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    ok = extractFrames(video, save='disk', savePath=savepath, format='jpg', every=30, resizeImg=True, newWidth=200, newHeight=200)
    
    """Failure example"""
    #video = os.path.join(SRC_IMG_DIR, 'test.mp4')
    #extractFrames(video, 'nowhere')
    #extractFrames(video, 'disk')
    #extractFrames(video, every=0)
    #extractFrames(video, format='mine')


def test_video_common_modifyFps():

    video = os.path.join(SRC_IMG_DIR, 'test2.mp4')

    params = [
        {
            'videoPath': video,
            'newFps': 10,
            'output': os.path.join(SAVE_IMG_DIR, "modifyFps_10.avi")
        },
        {
            'videoPath': video,
            'newFps': 60,
            'output': os.path.join(SAVE_IMG_DIR, "modifyFps_60.avi")
        },
        {
            'videoPath': video,
            'newFps': 120,
            'output': os.path.join(SAVE_IMG_DIR, "modifyFps_120.avi")
        },
        {
            'videoPath': video,
            'newFps': 120,
            'output': os.path.join(SAVE_IMG_DIR, "modifyFps_120.mp4")
        }
    ]

    for param in params:
        modifyFps(param['videoPath'], param['newFps'], param['output'])

    """Failure example"""
    #modifyFps(video, "a")
    #modifyFps(video, -1)
    #modifyFps(video, 120, "modifyFps_60.mov")
    #modifyFps(video, 120, "modifyFps_60")