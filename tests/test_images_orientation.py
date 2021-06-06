import cv2
import os 
from mediafier.image.orientation import flip, rotate, rotateTextBased

SRC_IMG_DIR = os.path.join('test_media', 'imgs_src_test')
SAVE_IMG_DIR = os.path.join('test_media', 'imgs_result_test', 'orientation')

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


def test_image_orientation_rotateTextBased():
    
    img_text = cv2.imread(os.path.join(SRC_IMG_DIR, 'test_text.jpg'))
    img_text_2 = cv2.imread(os.path.join(SRC_IMG_DIR, 'test_text_2.jpg'))
    img_no_text = cv2.imread(os.path.join(SRC_IMG_DIR, 'test_no_text.jpg'))
    
    params = [
        {
            'image': img_text,
            'pytesseract_path': "C:/Program Files/Tesseract-OCR/tesseract.exe",
            'contrast': False,
            'name': "text"
        },
        {
            'image': img_text,
            'pytesseract_path': "not_a_path",
            'contrast': False,
            'name': "ocr_fail"
        },
        {
            'image': img_text,
            'pytesseract_path': "C:/Program Files/Tesseract-OCR/tesseract.exe",
            'contrast': True,
            'name': "text_contrast"
        },
        {
            'image': img_text_2,
            'pytesseract_path': "C:/Program Files/Tesseract-OCR/tesseract.exe",
            'contrast': False,
            'name': "text_2"
        },
        {
            'image': img_text_2,
            'pytesseract_path': "C:/Program Files/Tesseract-OCR/tesseract.exe",
            'contrast': True,
            'name': "text_2_contrast"
        },
        {
            'image': img_no_text,
            'pytesseract_path': "C:/Program Files/Tesseract-OCR/tesseract.exe",
            'contrast': False,
            'name': "no_text"
        },
        {
            'image': img_no_text,
            'pytesseract_path': "C:/Program Files/Tesseract-OCR/tesseract.exe",
            'contrast': True,
            'name': "no_text_contrast"
        }
    ]

    for param in params:
        try:
            cv2.imwrite(os.path.join(SAVE_IMG_DIR, f"img_rotateTextBased_{param['name']}.png"), rotateTextBased(param['image'], param['pytesseract_path'], param['contrast']))
        except:
            pass

    """Failure example"""
    #img_rotateTextBased_b = rotateTextBased(img, 1)
