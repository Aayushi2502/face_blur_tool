Face Blur Privacy Tool

A simple, privacy-focused Streamlit web app that detects and blurs faces in uploaded or webcam-captured images using OpenCV Haar Cascades — no machine learning required.

Features:

- Detect faces using Haar cascade classifiers
- Upload or capture images via webcam
- Adjustable blur strength via slider
- Preview both original and blurred images
- Download the blurred image with one click
- Lightweight, no deep learning required

Built With:

- [Streamlit](https://streamlit.io/)
- [OpenCV](https://opencv.org/)
- [Pillow (PIL)](https://python-pillow.org/)

Installation:

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/face-blur-privacy-tool.git
cd face-blur-privacy-tool 

2. Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run the App
streamlit run app.py

