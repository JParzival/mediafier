import cv2
import os 
from imgTransPy.transformations.orientation import flip, rotate

SRC_IMG_DIR = os.path.join('test_imgs', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_imgs', 'imgs_result_test', 'transformations', 'orientation')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_transformation_orientation_flip():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_flip_h.png'), flip(img, 'horizontal'))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_flip_v.png'), flip(img, 'vertical'))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_flip_b.png'), flip(img, 'both'))

    """Failure example"""
    #img_flip_b = flip(img, 1)

def test_transformation_orientation_rotation():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    """Easy rotations"""
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_rotate_90.png'),  rotate(img, 90))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_rotate_180.png'), rotate(img, 180))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_rotate_270.png'), rotate(img, 270))

    """Complex rotations"""
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_rotate_45_ffFalse.png'), rotate(img, degrees=45, force_fit=False))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_rotate_45_ffTrue.png'),  rotate(img, degrees=45, force_fit=True))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_rotate_245_ffFalse.png'), rotate(img, degrees=245, force_fit=False))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_rotate_245_ffTrue.png'),  rotate(img, degrees=245, force_fit=True))

    """Failure example"""
    #rotate(img, -5)
    #rotate(img, "a")