# ================================
# app.py
# ================================

import streamlit as st
import os

# Import all modules
from modules.audio_tools import audio_toolkit
from modules.video_tools import video_toolkit
from modules.analyzer import media_analyzer
from modules.frame_processor import frame_processor
from modules.visualizer import audio_visualizer
from modules.batch_processing import batch_processing

# ================================
# Create Required Folders
# ================================

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
os.makedirs("temp", exist_ok=True)

# ================================
# Streamlit Page Config
# ================================

st.set_page_config(
    page_title="Audio + Video Utility Studio",
    page_icon="🎵",
    layout="wide"
)

# ================================
# Main Title
# ================================

st.title("🎵🎥 Audio + Video Utility Studio")

st.markdown("""
A Python-based multimedia toolkit for:
- Audio Processing
- Video Editing
- Media Analysis
- Frame Processing
- Audio Visualization
- Batch Processing
""")

# ================================
# Sidebar Navigation
# ================================

st.sidebar.title("📂 Navigation")

menu = st.sidebar.radio(
    "Choose Module",
    [
        "Home",
        "Audio Toolkit",
        "Video Toolkit",
        "Media Analyzer",
        "Frame Processor",
        "Audio Visualizer",
        "Batch Processing"
    ]
)

# ================================
# Home Page
# ================================

if menu == "Home":

    st.header("🚀 Welcome")

    st.write("""
    This application allows users to process
    audio and video files directly in the browser.

    Built using:
    - Streamlit
    - OpenCV
    - MoviePy
    - Librosa
    - Pydub
    - NumPy
    """)

    st.subheader("✨ Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("🎵 Audio Processing")
        st.success("🎥 Video Editing")
        st.success("📊 Media Analysis")

    with col2:
        st.info("🖼 Frame Extraction")
        st.info("📈 Audio Visualization")
        st.info("📦 Batch Processing")

    st.subheader("💡 Future Scope")

    st.write("""
    - AI Subtitle Generator
    - Video-to-GIF Converter
    - Cloud Deployment
    - Mobile App Version
    """)

# ================================
# Audio Toolkit
# ================================

elif menu == "Audio Toolkit":
    audio_toolkit()

# ================================
# Video Toolkit
# ================================

elif menu == "Video Toolkit":
    video_toolkit()

# ================================
# Media Analyzer
# ================================

elif menu == "Media Analyzer":
    media_analyzer()

# ================================
# Frame Processor
# ================================

elif menu == "Frame Processor":
    frame_processor()

# ================================
# Audio Visualizer
# ================================

elif menu == "Audio Visualizer":
    audio_visualizer()

# ================================
# Batch Processing
# ================================

elif menu == "Batch Processing":
    batch_processing()

# ================================
# Footer
# ================================

st.sidebar.markdown("---")
st.sidebar.caption("Built with ❤️ using Python + Streamlit")
