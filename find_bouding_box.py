from ultralytics import YOLOv10
import os
import cv2
import numpy as np
import shutil

def detect_and_save(images):

    # Load model
    TRAINED_MODEL_PATH = "C:\\AIO\\Bai_tap\\yolov10\\runs\\detect\\train\\weights\\best.pt"
    model = YOLOv10(TRAINED_MODEL_PATH)

    output_dir = "predict_img"
    conf_threshold = 0.3

    # Nếu thư mục tồn tại thì xóa đi
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # Tạo lại thư mục mới
    os.makedirs(output_dir)

    for idx, img_input in enumerate(images):
        # Kiểm tra nếu là đường dẫn file
        if isinstance(img_input, str):
            img = cv2.imread(img_input)
            if img is None:
                print(f"Lỗi: Không thể đọc ảnh {img_input}")
                continue
            filename = os.path.basename(img_input)

        # Nếu là UploadedFile của Streamlit
        elif hasattr(img_input, "read"):
            # Đọc nội dung file thành mảng numpy
            file_bytes = np.asarray(bytearray(img_input.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            filename = img_input.name  # giữ tên gốc

        # Nếu là OpenCV image
        elif isinstance(img_input, np.ndarray):
            img = img_input
            filename = f"image_{idx}.jpg"
        else:
            print(f"Không hỗ trợ kiểu dữ liệu: {type(img_input)}")
            continue

        # Dự đoán với YOLO
        results = model.predict(source=img, imgsz=416, conf=conf_threshold)

        # Lấy ảnh có bounding box
        annotated_img = results[0].plot()

        # Lưu ảnh kết quả
        save_path = os.path.join(output_dir, filename)
        cv2.imwrite(save_path, annotated_img)
        print(f"Đã lưu kết quả: {save_path}")


# image_list = [
#     "C:\\AIO\\Bai_tap\\yolov10\\image\\image.jpg"
# ]
#
# # Gọi hàm
# detect_and_save(image_list)
