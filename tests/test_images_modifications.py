import cv2
import os 
from mediafier.image.modifications import blur

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