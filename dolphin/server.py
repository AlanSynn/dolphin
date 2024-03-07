from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from vision_api import detect_text_from_image
from image_processing import ocr_pred
from utils import append_text_to_file
from config import UPLOAD_FOLDER

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/upload", methods=["GET", "POST"])
def upload_predict():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file:
            filename = secure_filename(file.filename)
            image_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_location)

            # Now that the image is saved, we can detect text
            detected_text = detect_text_from_image(image_location)

            # Optionally, process the detected text to perform further actions
            commands = ocr_pred(detected_text)

            # Assuming process_commands returns a list of commands or code snippets to be executed or saved
            for command in commands:
                append_text_to_file("commands.txt", command + "\n")

            # After processing, you might want to return the processed data or a success message
            return jsonify({'message': 'Image processed successfully', 'commands': commands}), 200

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=image>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.run(port=1200, debug=True)
