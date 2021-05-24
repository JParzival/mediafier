import cv2
import os 
from mediafier.image.size import resize

SRC_IMG_DIR = os.path.join('test_media', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_media', 'imgs_result_test', 'image', 'size')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_image_size_resize():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    """Resize by ratio"""
    params_ratio = [
        {
            'image': img,
            'ratio': 100
        },
        {
            'image': img,
            'ratio': 150
        },
        {
            'image': img,
            'ratio': 50
        }
    ]

    for param in params_ratio:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_resize_r{param['ratio']}_sNone_iNone.png"), resize(param['image'], param['ratio']))


    """Resize by size"""
    params_size = [
        {
            'image': img,
            'size': (1280, 720)
        },
        {
            'image': img,
            'size': (300, 200)
        }
    ]

    for param in params_size:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_resize_r100_s{param['size'][0]}x{param['size'][1]}_iNone.png"), resize(param['image'], size=param['size']))
    
    
    """Resize by size and interpolation"""
    params_size_int = [
        {
            'image': img,
            'size': (1280, 720),
            'interpolation': 'linear'
        },
        {
            'image': img,
            'size': (300, 200),
            'interpolation': 'area'
        },
        {
            'image': img,
            'size': (300, 200),
            'interpolation': 'nearest'
        }
    ]

    for param in params_size_int:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_resize_r100_s{param['size'][0]}x{param['size'][1]}_i{param['interpolation']}.png"), resize(param['image'], size=param['size'], interpolation=param['interpolation']))



    """Failure example"""
    #resize(img, -1)
    #resize(img, "a")
    #resize(img, size=(-1, 1))
    #resize(img, size=("a", 1))
