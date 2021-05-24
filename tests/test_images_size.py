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
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_sNone_iNone.png'), resize(img, 100))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r150_sNone_iNone.png'), resize(img, 150))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r50_sNone_iNone.png'),  resize(img, 50))

    """Resize by size: Bigger"""
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_s1280x720_iNone.png'),  resize(img, size=(1280, 720)))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_s1280x720_iLinear.png'),  resize(img, size=(1280, 720), interpolation='linear'))

    """Resize by size: Smaller"""
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_s300x200_iNone.png'),  resize(img, size=(300, 200)))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_s300x200_iArea.png'),  resize(img, size=(300, 200), interpolation='area'))
    cv2.imwrite(os.path.join(SAVE_IMG_DIR, 'img_resize_r100_s300x200_iNearest.png'),  resize(img, size=(300, 200), interpolation='nearest'))

    """Failure example"""
    #resize(img, -1)
    #resize(img, "a")
    #resize(img, size=(-1, 1))
    #resize(img, size=("a", 1))
