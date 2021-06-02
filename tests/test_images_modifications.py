import cv2
import os 
from mediafier.image.modifications import blur, pixelate

SRC_IMG_DIR = os.path.join('test_media', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_media', 'imgs_result_test', 'modifications')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_image_modifications_blur():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    """Transform contrast default"""
    params=[
        {
            'image': img,
            'method': 'default',
            'value': 'low'
        },
        {
            'image': img,
            'method': 'default',
            'value': 'medium'
        },
        {
            'image': img,
            'method': 'default',
            'value': 'high'
        },
        {
            'image': img,
            'method': 'default',
            'value': 'extreme'
        },
        {
            'image': img,
            'method': 'gaussian',
            'value': 'extreme'
        },
        {
            'image': img,
            'method': 'gaussian',
            'value': 'high'
        },
        {
            'image': img,
            'method': 'gaussian',
            'value': 'medium'
        },
        {
            'image': img,
            'method': 'gaussian',
            'value': 'low'
        }
    ]

    for param in params:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_blur_{param['method']}_{param['value']}.png"), blur(param['image'], param['method'], param['value']))
    
        
    """Failure example"""
    #blur(img, -1)
    #blur(img, "another")
    #blur(img, "default", -1)
    #blur(img, "gaussian", "a")


def test_image_modifications_pixelate():

    img1 = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))
    img2 = cv2.imread(os.path.join(SRC_IMG_DIR, 'notBlurry.jpg'))

    params=[
        {
            'image': img1,
            'value': 'low'
        },
        {
            'image': img1,
            'value': 'medium'
        },
        {
            'image': img1,
            'value': 'high'
        },
        {
            'image': img1,
            'value': 'extreme'
        }
    ]

    for param in params:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_pixelate_1_{param['value']}.png"), pixelate(param['image'], param['value']))

    params = [
        {
            'image': img2,
            'value': 'low'
        },
        {
            'image': img2,
            'value': 'medium'
        },
        {
            'image': img2,
            'value': 'high'
        },
        {
            'image': img2,
            'value': 'extreme'
        }
    ]

    for param in params:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_pixelate_2_{param['value']}.png"), pixelate(param['image'], param['value']))

    """Failure example"""
    #pixelate(img2, "a")
    #pixelate(img2, 1)