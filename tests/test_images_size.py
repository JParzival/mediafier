import cv2
import os 
from mediafier.image.size import resize, addBorders

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


def test_image_size_addBorders():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    params = [
        {
            'image': img,
            'top': 100,
            'bottom': 100,
            'left': 100,
            'right': 100,
            'borderType': 'constant',
            'color': 'black'
        },
        {
            'image': img,
            'top': 100,
            'bottom': 100,
            'left': 100,
            'right': 100,
            'borderType': 'constant',
            'color': 'white'
        },
        {
            'image': img,
            'top': 0,
            'bottom': 0,
            'left': 0,
            'right': 0,
            'borderType': 'constant',
            'color': 'white'
        },
        {
            'image': img,
            'top': 100,
            'bottom': 0,
            'left': 0,
            'right': 0,
            'borderType': 'constant',
            'color': 'white'
        },
        {
            'image': img,
            'top': 100,
            'bottom': 100,
            'left': 0,
            'right': 0,
            'borderType': 'constant',
            'color': 'white'
        },
        {
            'image': img,
            'top': 100,
            'bottom': 100,
            'left': 100,
            'right': 0,
            'borderType': 'constant',
            'color': 'black'
        },
        {
            'image': img,
            'top': 100,
            'bottom': 100,
            'left': 100,
            'right': 100,
            'borderType': 'reflect',
            'color': 'black'
        },
        {
            'image': img,
            'top': 100,
            'bottom': 100,
            'left': 100,
            'right': 100,
            'borderType': 'default',
            'color': 'black'
        },
        {
            'image': img,
            'top': 100,
            'bottom': 100,
            'left': 100,
            'right': 100,
            'borderType': 'replicate',
            'color': 'black'
        }
    ]
    
    for param in params:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_addBorders_{str(param['top'])}_{str(param['bottom'])}_{str(param['left'])}_{str(param['right'])}_{param['borderType']}_{param['color']}.png"), 
                    addBorders(param['image'], top=param['top'], bottom=param['bottom'], left=param['left'], right=param['right'], borderType=param['borderType'], color=param['color']))

    """Failure example"""
    #addBorders(img, -1)
    #addBorders(img, "a")
    #addBorders(img, 1, 1, 1, 1, 'noclue')
    #addBorders(img, 1, 1, 1, 1, 'constant', 'pink')