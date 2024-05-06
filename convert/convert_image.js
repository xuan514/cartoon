const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const port = 3000;

const UPLOAD_FOLDER = ''; // 設置上傳檔案的目錄

// 創建上傳檔案的目錄
if (!fs.existsSync(UPLOAD_FOLDER)) {
    fs.mkdirSync(UPLOAD_FOLDER);
}

// 設置檔案上傳配置
const upload = multer({ dest: UPLOAD_FOLDER });

// 處理檔案上傳的 POST 請求
app.post('/convert', upload.single('fileUpload'), (req, res) => {
    if (req.file) {
        const filepath = path.join(UPLOAD_FOLDER, req.file.filename);
        fs.renameSync(req.file.path, filepath); // 將上傳的檔案移動到指定目錄
        res.json({ 'filePath': filepath }); // 返回檔案路徑
    } else {
        res.status(400).json({ 'error': 'No file uploaded' }); // 如果沒有檔案上傳，返回錯誤訊息
    }
});

// 監聽端口
app.listen(port, () => {
    console.log(`伺服器正在執行，端口為 ${port}`);
});
