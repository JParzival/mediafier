import cv2
import os 
from mediafier.image.cropping import crop

SRC_IMG_DIR = os.path.join('test_imgs', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_imgs', 'imgs_result_test', 'transformations', 'cropping')


def test_transformation_size_crop():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    """Crops"""
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_crop_100_100_300_300_fill=False.png'), crop(img, 100, 100, 300, 300))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_crop_100_100_100_400_fill=False.png'), crop(img, 0, 0, 100, 400))

    """Crops with fill"""

    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_crop_100_100_300_300_fill=True.png'), crop(img, 100, 100, 300, 300, True))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_crop_100_100_100_400_fill=True.png'), crop(img, 0, 0, 100, 400, True))

    """Crops with 0 in w or h -> Returns black image"""

    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_crop_100_100_0_300_fill=True.png'), crop(img, 100, 100, 0, 300, True))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_crop_100_100_100_0_fill=True.png'), crop(img, 0, 0, 100, 0, True))

    """Failure example"""
    #crop(img, -1, -1, 1, 1)
    #crop(img, 1)
    #crop(img, "a", "a", "a", "a")
    #crop(img, 100, 100, -50, -50, True)