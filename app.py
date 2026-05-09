# =========================================
# app.py
# =========================================

import streamlit as st
import os
import sys

# =========================================
# Fix Module Path
# =========================================

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# =========================================
# Import Modules
# =========================================

from modules.audio_tools import audio_toolkit
from modules.video_tools import video_toolkit
from modules.analyzer import media_analyzer
from modules.frame_processor import frame_processor
from modules.visualizer import audio_visualizer
from modules.batch_processing import batch_processing

# =========================================
# Create Required Folders
# =========================================

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
os.makedirs("temp", exist_ok=True)

# =========================================
# Streamlit Config
# =========================================

st.set_page_config(
    page_title="Audio + Video Utility Studio",
    page_icon="🎵",
    layout="wide"
)

# =========================================
# Main Title
# =========================================

st.title("🎵🎥 Audio + Video Utility Studio")

st.markdown("""
Welcome to the multimedia processing platform built using Python.

### Features
- Audio Processing
- Video Editing
- Media Analysis
- Frame Processing
- Audio Visualization
- Batch Processing
""")

# =========================================
# Sidebar Menu
# =========================================

menu = st.sidebar.selectbox(
    "Select Module",
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

# =========================================
# Home Page
# =========================================

if menu == "Home":

    st.header("🚀 Project Overview")

    st.write("""
    This project combines multiple multimedia utilities
    into one platform using Python libraries.

    Technologies Used:
    - Streamlit
    - OpenCV
    - MoviePy
    - Librosa
    - Pydub
    """)

# =========================================
# Audio Toolkit
# =========================================

elif menu == "Audio Toolkit":
    audio_toolkit()

# =========================================
# Video Toolkit
# =========================================

elif menu == "Video Toolkit":
    video_toolkit()

# =========================================
# Media Analyzer
# =========================================

elif menu == "Media Analyzer":
    media_analyzer()

# =========================================
# Frame Processor
# =========================================

elif menu == "Frame Processor":
    frame_processor()

# =========================================
# Audio Visualizer
# =========================================

elif menu == "Audio Visualizer":
    audio_visualizer()

# =========================================
# Batch Processing
# =========================================

elif menu == "Batch Processing":
    batch_processing()

# =========================================
# Footer
# =========================================

st.sidebar.markdown("---")
st.sidebar.write("Built with ❤️ using Python + Streamlit")
