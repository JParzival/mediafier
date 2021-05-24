import cv2
import os 
from mediafier.image.cropping import crop, slice

SRC_IMG_DIR = os.path.join('test_media', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_media', 'imgs_result_test', 'image', 'cropping')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_image_cropping_crop():
    img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))

    params_nofill=[
        {
            'image': img,
            'x': 100,
            'y': 100,
            'w': 300,
            'h': 300,
            'name': 'img_crop_100_100_300_300_fill=False.png'
        },
        {
            'image': img,
            'x': 0,
            'y': 0,
            'w': 100,
            'h': 400,
            'name': 'img_crop_0_0_100_400_fill=False.png'
        }
    ]

    params_fill=[
        {
            'image': img,
            'x': 100,
            'y': 100,
            'w': 300,
            'h': 300,
            'fill': True,
            'name': 'img_crop_100_100_300_300_fill=True.png'
        },
        {
            'image': img,
            'x': 100,
            'y': 100,
            'w': 100,
            'h': 400,
            'fill': True,
            'name': 'img_crop_100_100_100_400_fill=True.png'
        },
        {                                                       # This one should return a black image
            'image': img,
            'x': 100,
            'y': 100,
            'w': 0,
            'h': 300,
            'fill': True,
            'name': 'img_crop_100_100_0_300_fill=True.png'
        }
    ]

    for param in params_nofill:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, param['name']), crop(param['image'], param['x'], param['y'], param['w'], param['h']))
    for param in params_fill:
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, param['name']), crop(param['image'], param['x'], param['y'], param['w'], param['h'], param['fill']))

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

    params=[
        {
            'image': img,
            'rows': 1,
            'cols': 1
        },
        {
            'image': img,
            'rows': 3,
            'cols': 3
        },
        {
            'image': img,
            'rows': 4,
            'cols': 4
        },
        {
            'image': img,
            'rows': 1,
            'cols': 3
        },
        {
            'image': img,
            'rows': 2,
            'cols': 1
        }
    ]

    for param in params:
        images = slice(param['image'], param['rows'], param['cols'])
        i = 0
        for image in images:
            cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_slice_{param['rows']}x{param['cols']}_{i}.png"), image)
            i += 1
    
    
    
    """Failure example"""
    #slice(img, -1, -1)
    #slice()
    #slice(img, "a", "a")