import cv2
import os 
from mediafier.image.color import modify_contrast, modify_brightness

SRC_IMG_DIR = os.path.join('test_media', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_media', 'imgs_result_test', 'image', 'color')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_image_color_contrast():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    """Transform contrast default"""
    params_default=[
        {
            'image': img,
            'value': 1
        },
        {
            'image': img,
            'value': 3
        },
        {
            'image': img,
            'value': 0.5
        },
        {
            'image': img,
            'value': 0
        },
    ]

    for param in params_default:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_contrast_{param['value']}_default.png"), modify_contrast(param['image'], param['value']))

    
    """Transform contrast CLAHE"""
    params_clahe=[
        {
            'image': img,
            'value': 1,
            'method': 'CLAHE',
            'name': 'img_contrast_1_CLAHE.png'
        },
        {
            'image': img,
            'value': 2,
            'method': 'CLAHE',
            'name': 'img_contrast_2_CLAHE.png'
        },
        {
            'image': img,
            'value': 0.5,
            'method': 'CLAHE',
            'name': 'img_contrast_05_CLAHE.png'
        },
        {
            'image': img,
            'value': 0,
            'method': 'CLAHE',
            'name': 'img_contrast_0_CLAHE.png'
        },
    ]
    
    for param in params_clahe:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_contrast_{param['value']}_CLAHE.png"), modify_contrast(param['image'], param['value'], param['method']))



    """Failure example"""
    
    #modify_contrast(img, "a")
    #modify_contrast(img, 1, ':S')
    #modify_contrast(img, -1)




def test_image_color_brightness():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    """Transform brightness"""
    params_default=[
        {
            'image': img,
            'value': 1
        },
        {
            'image': img,
            'value': 1.5
        },
        {
            'image': img,
            'value': 2
        },
        {
            'image': img,
            'value': 0.5
        },
        {
            'image': img,
            'value': 0
        },
    ]

    for param in params_default:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_brightness_{param['value']}.png"), modify_contrast(param['image'], param['value']))

    
    """Failure example"""
    
    #modify_brightness(img, "a")
    #modify_brightness(img, 1, ':S')
    #modify_brightness(img, -1)