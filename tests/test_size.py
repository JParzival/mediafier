import cv2
import os 
from mediafier.image.size import resize, crop

SRC_IMG_DIR = os.path.join('test_imgs', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_imgs', 'imgs_result_test', 'transformations', 'size')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_transformation_size_resize():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    """Resize by ratio"""
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_sNone_iNone.png'), resize(img, 100))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r150_sNone_iNone.png'), resize(img, 150))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r50_sNone_iNone.png'),  resize(img, 50))

    """Resize by size: Bigger"""
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_s1280x720_iNone.png'),  resize(img, size=(1280, 720)))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_s1280x720_iLinear.png'),  resize(img, size=(1280, 720), interpolation='linear'))

    """Resize by size: Smaller"""
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_s300x200_iNone.png'),  resize(img, size=(300, 200)))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_s300x200_iArea.png'),  resize(img, size=(300, 200), interpolation='area'))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_s300x200_iNearest.png'),  resize(img, size=(300, 200), interpolation='nearest'))

    """Failure example"""
    #resize(img, -1)
    #resize(img, "a")
    #resize(img, size=(-1, 1))
    #resize(img, size=("a", 1))


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