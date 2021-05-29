import cv2
import os 
from mediafier.image.draw import drawBBox

SRC_IMG_DIR = os.path.join('test_media', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_media', 'imgs_result_test', 'draw')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_image_size_resize():

    params = [
        {
            'x': 100, 
            'y': 100, 
            'w': 100, 
            'h': 100, 
            'color': 'black',
            'thickness': 2
        },
        {
            'x': 100, 
            'y': 100, 
            'w': 100, 
            'h': 100, 
            'color': 'red',
            'thickness': 2
        },
        {
            'x': 100, 
            'y': 100, 
            'w': 100, 
            'h': 100, 
            'color': 'blue',
            'thickness': 2
        },
        {
            'x': 0, 
            'y': 0, 
            'w': 100, 
            'h': 100, 
            'color': 'black',
            'thickness': 2
        },
        {
            'x': 0, 
            'y': 0, 
            'w': 100, 
            'h': 100, 
            'color': 'black',
            'thickness': 4
        }
    ]

    for param in params:
        img = cv2.imread(os.path.join(SRC_IMG_DIR, 'test.png'))
        
        cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_drawBBox_{str(param['x'])}_{str(param['y'])}_{str(param['w'])}_{str(param['h'])}_{param['color']}_{str(param['thickness'])}.png"), 
                     drawBBox(img, x=param['x'], y=param['y'], w=param['w'], h=param['h'], color=param['color'], thickness=param['thickness']))


    """Failure example"""
    #drawBBox(img, -1)
    #drawBBox(img, "a")
    #drawBBox(img, 1, 1, 1, 1, 'noclue')
    #drawBBox(img, 1, 1, 1, 1, 'black', '2')