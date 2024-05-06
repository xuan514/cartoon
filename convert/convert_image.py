from flask import Flask, request, jsonify, send_file
from PIL import Image
import io

app = Flask(__name__)

# 處理圖片轉換
def convert_image(image):
    # 在這裡加入您的圖片轉換程式碼
    # 這只是一個範例，請替換為您的實際轉換邏輯
    image = Image.open(image)
    # 這裡只是一個示例，您可以將圖片轉換成黑白
    converted_image = image.convert('L')
    return converted_image

@app.route('/index.html', methods=['POST'])
def handle_image_conversion():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected image'}), 400

    converted_image = convert_image(image_file)
    # 儲存轉換後的圖片
    converted_image_path = 'converted_image.jpg'  # 可以自訂儲存路徑
    converted_image.save(converted_image_path)

    # 返回轉換後的圖片路徑
    return jsonify({'message': 'Image converted successfully', 'converted_image_path': converted_image_path})

@app.route('/', methods=['GET'])
def download_converted_image():
    # 從查詢字串中獲取轉換後的圖片路徑
    converted_image_path = request.args.get('path')
    # 使用 Flask 的 send_file 函數傳送檔案
    return send_file(converted_image_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
