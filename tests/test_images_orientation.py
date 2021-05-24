import cv2
import os 
from mediafier.image.orientation import flip, rotate

SRC_IMG_DIR = os.path.join('test_media', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_media', 'imgs_result_test', 'image', 'orientation')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_image_orientation_flip():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    params = [
        {
            'image': img,
            'orientation': 'vertical'
        },
        {
            'image': img,
            'orientation': 'horizontal'
        },
        {
            'image': img,
            'orientation': 'both'
        }
    ]

    for param in params:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_flip_{param['orientation']}.png"), flip(param['image'], param['orientation']))

    """Failure example"""
    #img_flip_b = flip(img, 1)



def test_image_orientation_rotation():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    """Easy rotations"""
    params_ez = [
        {
            'image': img,
            'orientation': 90
        },
        {
            'image': img,
            'orientation': 180
        },
        {
            'image': img,
            'orientation': 270
        }
    ]

    for param in params_ez:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_rotate_{param['orientation']}.png"),  rotate(param['image'], param['orientation']))


    """Complex rotations"""
    params_ez = [
        {
            'image': img,
            'orientation': 45,
            'forcefit': False
        },
        {
            'image': img,
            'orientation': 45,
            'forcefit': True
        },
        {
            'image': img,
            'orientation': 245,
            'forcefit': False
        },
        {
            'image': img,
            'orientation': 245,
            'forcefit': True
        }
    ]

    for param in params_ez:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_rotate_{param['orientation']}_{param['forcefit']}.png"), rotate(param['image'], param['orientation'], force_fit=param['forcefit']))



    """Failure example"""
    #rotate(img, -5)
    #rotate(img, "a")