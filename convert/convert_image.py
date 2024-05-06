import os
from flask import Flask, request, jsonify
# 要更改權限的目錄或檔案路徑
path = os.path.abspath(__name__)  # 取得當前腳本的絕對路徑

# 設置只有擁有者具有讀取和寫入權限
mode = 0o600

# 更改權限
os.chmod(path, mode)
app = Flask(__name__)

UPLOAD_FOLDER = ""
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/convert', methods=['POST'])
def convert():
    if request.files.get('imageUpload'):
        file = request.files.get('imageUpload')
        if file.filename != '':
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return jsonify({'imagePath': filepath})
    elif request.files.get('videoUpload'):
        file = request.files.get('videoUpload')
        if file.filename != '':
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return jsonify({'videoPath': filepath})
    return jsonify({'error': 'No file uploaded'})

if __name__ == '__main__':
    app.run(debug=True)
