import cv2
from vision_api import detect_text_from_image
from translator import translate_text

def ocr_pred(image_path):
    response = detect_text_from_image(image_path)
    image = cv2.imread(image_path)

    # Perform OCR processing on the image dummy for later work
    # Do the main logic here
    output = translate_text(response, image)

    return output
