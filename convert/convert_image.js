const express = require('express');
const multer  = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const upload = multer({ dest: '/' }); // 設置上傳目錄

// 處理圖片上傳
app.post('/upload/image', upload.single('imageUpload'), (req, res) => {
    const tempPath = req.file.path; // 臨時文件路徑
    const targetPath = path.join(__dirname, 'uploads/image', req.file.originalname); // 目標文件路徑

    fs.rename(tempPath, targetPath, err => {
        if (err) return handleError(err, res);

        res
            .status(200)
            .contentType("text/plain")
            .end("檔案上傳成功");
    });
});

// 處理影片上傳
app.post('/upload/video', upload.single('videoUpload'), (req, res) => {
    const tempPath = req.file.path; // 臨時文件路徑
    const targetPath = path.join(__dirname, 'uploads/video', req.file.originalname); // 目標文件路徑

    fs.rename(tempPath, targetPath, err => {
        if (err) return handleError(err, res);

        res
            .status(200)
            .contentType("text/plain")
            .end("檔案上傳成功");
    });
});

function handleError(err, res) {
    console.error(err);
    res
        .status(500)
        .contentType("text/plain")
        .end("發生錯誤: " + err.message);
}

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
