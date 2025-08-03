import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

# Load Haar cascade
CASCADE_PATH = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

def blur_faces(image, blur_strength=55):
    # Convert to grayscale for detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    # Apply blur to each detected face
    for (x, y, w, h) in faces:
        roi = image[y:y+h, x:x+w]
        roi_blurred = cv2.GaussianBlur(roi, (blur_strength, blur_strength), 30)
        image[y:y+h, x:x+w] = roi_blurred

    return image, len(faces)

def main():
    st.set_page_config(page_title="Face Blur Privacy Tool", layout="centered")
    st.title("🕶️ Face Blur Privacy Tool")
    st.write("Upload or capture an image. We'll blur the detected faces to protect privacy.")

    source = st.radio("Image Source:", ["Upload Image", "Webcam Capture"])

    image = None

    if source == "Upload Image":
        uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            image = Image.open(uploaded_file).convert("RGB")
    else:
        picture = st.camera_input("Take a picture")
        if picture:
            image = Image.open(picture).convert("RGB")

    if image is not None:
        st.image(image, use_container_width=True)

        blur_strength = st.slider("Blur Strength", 15, 99, 55, step=2)

        with st.spinner("Detecting and blurring faces..."):
            image_np = np.array(image)
            image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
            output_img, faces_detected = blur_faces(image_bgr, blur_strength)
            output_rgb = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)
            result = Image.fromarray(output_rgb)

        st.image(result, caption=f"Blurred Image (Faces detected: {faces_detected})", use_container_width=True)

        # Download
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="📥 Download Blurred Image",
            data=byte_im,
            file_name="blurred_image.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
