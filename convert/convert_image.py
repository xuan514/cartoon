from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'path/to/your/upload/folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/convert', methods=['POST'])
def convert():
    if 'imageUpload' in request.files:
        file = request.files['imageUpload']
        if file.filename != '':
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return jsonify({'imagePath': filepath})
    elif 'videoUpload' in request.files:
        file = request.files['videoUpload']
        if file.filename != '':
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return jsonify({'videoPath': filepath})
    return jsonify({'error': 'No file uploaded'})

if __name__ == '__main__':
    app.run(debug=True)
