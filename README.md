# YOLOv10 Object Detection – Safety Helmet Detection

## Giới thiệu
Dự án này thực hiện Object Detection nhằm phát hiện mũ bảo hộ (Safety Helmet) trong môi trường công nghiệp và xây dựng.  
Mô hình sử dụng là YOLOv10, được fine-tuning trên bộ dữ liệu Safety Helmet Dataset.  

Ứng dụng chính:
- Giám sát an toàn lao động trong công trường.  
- Hỗ trợ hệ thống camera thông minh.  
- Cảnh báo khi phát hiện người không đội mũ bảo hộ.  

---

## Các bước chính

### 1. Chuẩn bị dữ liệu
- Dataset: Safety Helmet Dataset.  
- Dữ liệu được annotate theo định dạng YOLO.  
- Chia thành các tập train/valid/test.  

### 2. Huấn luyện mô hình
- Sử dụng YOLOv10.  
- Fine-tune trên dataset với các tham số (batch size, epochs, imgsz).  
- Các tham số đuọc sử dụng để fine tuning:
  - EPOCHS = 20 
  - IMG_SIZE = 416 
  - BATCH_SIZE = 32
Ví dụ lệnh huấn luyện:  

### 3. Triển khai với Streamlit

Xây dựng web-app đơn giản cho phép:
  - Upload nhiều ảnh. 
  - Thực hiện nhận diện với YOLOv10. 
  - Hiển thị kết quả trực quan với bounding box.
Chạy ứng dụng:
`````bash`````
        streamlit run object_detection_app.py
````` `````
### 4. Cấu trúc thư mục 
```text
    project/
    ├── object_detection_app.py      # Streamlit web app
    ├── find_bounding_box.py         # Xử lý YOLO và lưu ảnh kết quả
    ├── runs/                        # Lưu checkpoints sau khi train (file best.pt)
    ├── predict_img/                 # Lưu ảnh kết quả detect
    ├── Safety_Helmet_Dataset/       # Bộ dữ liệu dùng để fine tuning
    ├── requirements.txt             # Thư viện cần thiết
    └── README.md                    # File mô tả project
```
### 5. Công nghệ sử dụng

  - YOLOv10 
  - Python (OpenCV, Numpy, Streamlit, Ultralytics)
  - Dataset: Safety Helmet Dataset

### 6. Kết quả

Mô hình đạt mAP@50 ≈ 76% sau khi fine-tune.
Phát hiện chính xác các đối tượng:
  - Người có đội mũ bảo hộ. 
  - Người không đội mũ bảo hộ.

### 7. Demo 
![Giao diện](C:\anh\web.png)
![Predict1](C:\anh\predict1.png)
![Predict2](C:\anh\predict2.png)
![Predict3](C:\anh\predict3.png)
