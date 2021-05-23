import cv2
import os 
from mediafier.transformations.color import modify_contrast, modify_brightness

SRC_IMG_DIR = os.path.join('test_imgs', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_imgs', 'imgs_result_test', 'transformations', 'color')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_transformation_color_contrast():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    """Transform contrast default"""
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_contrast_1_default.png'), modify_contrast(img, 1))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_contrast_3_default.png'), modify_contrast(img, 3))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_contrast_05_default.png'), modify_contrast(img, 0.5))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_contrast_0_default.png'), modify_contrast(img, 0))

    """Transform contrast CLAHE"""
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_contrast_1_CLAHE.png'), modify_contrast(img, 1,    "CLAHE"))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_contrast_3_CLAHE.png'), modify_contrast(img, 2,    "CLAHE"))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_contrast_05_CLAHE.png'), modify_contrast(img, 0.5, "CLAHE"))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_contrast_0_CLAHE.png'), modify_contrast(img, 0, "CLAHE"))
    
    """Failure example"""
    
    #modify_contrast(img, "a")
    #modify_contrast(img, 1, ':S')
    #modify_contrast(img, -1)


def test_transformation_color_brightness():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    """Transform brightness"""
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_brightness_1.png'), modify_brightness(img, 1))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_brightness_15.png'), modify_brightness(img, 1.5))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_brightness_2.png'), modify_brightness(img, 2))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_brightness_05.png'), modify_brightness(img, 0.5))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_brightness_0.png'), modify_brightness(img, 0))
    
    """Failure example"""
    
    #modify_brightness(img, "a")
    #modify_brightness(img, 1, ':S')
    #modify_brightness(img, -1)