import streamlit as st
from find_bouding_box import detect_and_save
import os

st.title("YOLOv10 Object Detection với Streamlit")
st.write("Upload nhiều ảnh và nhận kết quả object detection.")

uploaded_files = st.file_uploader(
    "Upload images",
    accept_multiple_files=True,
    type=["jpg", "jpeg", "png", "webp", "tiff", "gif"]
)
if uploaded_files:
    st.write(f"Bạn đã upload {len(uploaded_files)} ảnh.")

    if st.button("Bắt đầu xử lý"):
        detect_and_save(uploaded_files)

        # Lấy toàn bộ ảnh trong thư mục kết quả
        output_dir = "predict_img"
        if os.path.exists(output_dir):
            image_files = [f for f in os.listdir(output_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

            st.subheader("Kết quả Object Detection:")
            for img_file in image_files:
                img_path = os.path.join(output_dir, img_file)
                st.image(img_path, caption=img_file, use_container_width=True)
