# vision_api.py
import io
import os
from google.cloud import vision
from google.cloud.vision_v1 import types, AnnotateImageResponse
from config import GOOGLE_APPLICATION_CREDENTIALS, IMAGE_FILE_PATH

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS

client = vision.ImageAnnotatorClient()

def detect_text_from_image(image_location):
    file_name = os.path.abspath(IMAGE_FILE_PATH)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)  # returns textAnnotation

    # serialize / deserialize proto (binary)
    serialized_proto_plus = AnnotateImageResponse.serialize(response)
    response = AnnotateImageResponse.deserialize(serialized_proto_plus)

    return response.full_text_annotation.text
