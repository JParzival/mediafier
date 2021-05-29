import cv2
import os 
from mediafier.image.checks import isBlurry

SRC_IMG_DIR = os.path.join('test_media', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_media', 'imgs_result_test', 'checks')

if not os.path.exists(SAVE_IMG_DIR):
    os.makedirs(SAVE_IMG_DIR)

def test_image_color_contrast():
    img1 = cv2.imread(os.path.join(SRC_IMG_DIR, 'blurry.jpg'))
    img2 = cv2.imread(os.path.join(SRC_IMG_DIR, 'notBlurry.jpg'))

    """Transform contrast default"""
    params_1=[
        {
            'image': img1,
            'strictness': 'high'
        },
        {
            'image': img1,
            'strictness': 'medium'
        },
        {
            'image': img1,
            'strictness': 'low'
        },
        {
            'image': img1,
            'customStrictness': 2500000
        },
        {
            'image': img1,
            'customStrictness': 25000000
        }
    ]

    params_2=[
        {
            'image': img2,
            'strictness': 'high'
        },
        {
            'image': img2,
            'strictness': 'medium'
        },
        {
            'image': img2,
            'strictness': 'low'
        },
        {
            'image': img2,
            'customStrictness': 25000000
        },
        {
            'image': img2,
            'customStrictness': 250000000
        }
    ]
        
    for param in params_1:
        try:
            mybool, myvalue = isBlurry(param['image'], customStrictness=param['customStrictness'])
            with open(os.path.join(SAVE_IMG_DIR, f"img1_isBlurry_{param['customStrictness']}.txt"), 'w') as file:
                file.write("BOOL: " + str(mybool) + "| VALUE: " + str(myvalue))
        except:
            mybool, myvalue = isBlurry(param['image'], param['strictness'])
            with open(os.path.join(SAVE_IMG_DIR, f"img1_isBlurry_{param['strictness']}.txt"), 'w') as file:
                file.write("BOOL: " + str(mybool) + "| VALUE: " + str(myvalue))

    for param in params_2:
        try:
            mybool, myvalue = isBlurry(param['image'], customStrictness=param['customStrictness'])
            with open(os.path.join(SAVE_IMG_DIR, f"img2_isBlurry_{param['customStrictness']}.txt"), 'w') as file:
                file.write("BOOL: " + str(mybool) + "| VALUE: " + str(myvalue))
        except:
            mybool, myvalue = isBlurry(param['image'], param['strictness'])
            with open(os.path.join(SAVE_IMG_DIR, f"img2_isBlurry_{param['strictness']}.txt"), 'w') as file:
                file.write("BOOL: " + str(mybool) + "| VALUE: " + str(myvalue))
        
    """Failure example"""
    #isBlurry(img1, -1)
    #isBlurry(img1, "mid")
    #isBlurry(img1, "high", -1)
    #isBlurry(img1, "high", "a")