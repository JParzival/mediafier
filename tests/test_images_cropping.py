import cv2
import os 
from mediafier.image.cropping import crop, slice

SRC_IMG_DIR = os.path.join('test_media', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_media', 'imgs_result_test', 'image', 'cropping')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_image_cropping_crop():
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


def test_image_cropping_slice():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    """Default slice"""
    images = slice(img)
    i = 0
    for image in images:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f'img_slice_default_{i}.png'), image)
        i += 1

    """One x One slice"""
    images = slice(img, 1, 1)
    i = 0
    for image in images:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f'img_slice_1x1_{i}.png'), image)
        i += 1

    """Other"""
    images = slice(img, 3, 3)
    i = 0
    for image in images:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f'img_slice_3x3_{i}.png'), image)
        i += 1

    images = slice(img, 4, 4)
    i = 0
    for image in images:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f'img_slice_4x4_{i}.png'), image)
        i += 1

    images = slice(img, 1, 3)
    i = 0
    for image in images:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f'img_slice_1x3_{i}.png'), image)
        i += 1

    images = slice(img, 2, 1)
    i = 0
    for image in images:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f'img_slice_2x1_{i}.png'), image)
        i += 1

    """Failure example"""
    #slice(img, -1, -1)
    #slice()
    #slice(img, "a", "a")