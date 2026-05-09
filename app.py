import streamlit as st
import os

# Import modules
from modules.audio_tools import audio_toolkit
from modules.video_tools import video_toolkit
from modules.analyzer import media_analyzer
from modules.frame_processor import frame_processor
from modules.visualizer import audio_visualizer
from modules.batch_processing import batch_processing

# -----------------------------
# Create Required Folders
# -----------------------------
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
os.makedirs("temp", exist_ok=True)

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="Audio + Video Utility Studio",
    page_icon="🎵",
    layout="wide"
)

# -----------------------------
# Main Title
# -----------------------------
st.title("🎵🎥 Audio + Video Utility Studio")

st.markdown("""
Welcome to the **Audio + Video Utility Studio**  
A Python-based multimedia processing platform.

### Features:
- 🎵 Audio Processing
- 🎥 Video Editing
- 📊 Media Analysis
- 🖼 Frame Processing
- 📈 Audio Visualization
- 📦 Batch Processing
""")

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
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

# -----------------------------
# Home Page
# -----------------------------
if menu == "Home":

    st.header("🚀 Project Overview")

    st.write("""
    This project helps users perform basic multimedia operations
    directly in the browser using Python.

    It is built using:
    - Streamlit
    - OpenCV
    - MoviePy
    - Librosa
    - Pydub
    - NumPy
    """)

    st.subheader("📌 Main Modules")

    col1, col2 = st.columns(2)

    with col1:
        st.success("🎵 Audio Toolkit")
        st.success("🎥 Video Toolkit")
        st.success("📊 Media Analyzer")

    with col2:
        st.info("🖼 Frame Processor")
        st.info("📈 Audio Visualizer")
        st.info("📦 Batch Processing")

    st.subheader("💡 Future Scope")

    st.write("""
    - AI Subtitle Generator
    - Noise Reduction
    - Video-to-GIF Converter
    - Cloud Storage
    - Mobile Version
    """)

# -----------------------------
# Audio Toolkit
# -----------------------------
elif menu == "Audio Toolkit":
    audio_toolkit()

# -----------------------------
# Video Toolkit
# -----------------------------
elif menu == "Video Toolkit":
    video_toolkit()

# -----------------------------
# Media Analyzer
# -----------------------------
elif menu == "Media Analyzer":
    media_analyzer()

# -----------------------------
# Frame Processor
# -----------------------------
elif menu == "Frame Processor":
    frame_processor()

# -----------------------------
# Audio Visualizer
# -----------------------------
elif menu == "Audio Visualizer":
    audio_visualizer()

# -----------------------------
# Batch Processing
# -----------------------------
elif menu == "Batch Processing":
    batch_processing()

# -----------------------------
# Footer
# -----------------------------
st.sidebar.markdown("---")
st.sidebar.caption("Built with ❤️ using Python + Streamlit")
