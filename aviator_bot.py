import os
import random
from PIL import Image, ImageDraw, ImageFont
import streamlit as st

# Hàm tạo ảnh kết quả
def create_prediction_image(prediction_text):
    font_path = os.path.join(os.path.dirname(__file__), "Roboto-Regular.ttf")
    font = ImageFont.truetype(font_path, size=30)
    text_position = (50, 50)

    base = Image.open("aviator_logo.png").convert("RGBA")
    draw = ImageDraw.Draw(base)
    draw.text(text_position, prediction_text, font=font, fill="white")

    base.save("prediction_result.png")

# Giao diện người dùng với Streamlit
st.set_page_config(page_title="Dự đoán Aviator", page_icon="🎯")
st.title("🎯 Dự đoán Aviator")

# Giao diện tương tác
st.markdown("### Tuỳ chỉnh trước khi dự đoán:")

max_value = st.slider("🔢 Chọn giới hạn tối đa", min_value=2.0, max_value=100.0, value=40.0, step=1.0)

prediction_type = st.radio(
    "🎲 Chọn kiểu dự đoán:",
    ("Ngẫu nhiên", "Cao", "Thấp")
)

if st.button("🚀 Dự đoán ngay"):
    if prediction_type == "Ngẫu nhiên":
        prediction = round(random.uniform(1.00, max_value), 2)
    elif prediction_type == "Cao":
        prediction = round(random.uniform(max_value / 2, max_value), 2)
    else:
        prediction = round(random.uniform(1.00, max_value / 2), 2)

    prediction_text = f"Kết quả dự đoán: {prediction}x"
    create_prediction_image(prediction_text)

    st.image("prediction_result.png", caption=prediction_text)
