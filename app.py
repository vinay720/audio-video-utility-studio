import streamlit as st
import os
import sys

# Ensure the current directory is in the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now import your custom module
try:
    from modules.audio_tools import audio_toolkit
except ModuleNotFoundError as e:
    st.error(f"Module Import Error: {e}")
    st.info("Check if 'modules' folder has an '__init__.py' file.")

def main():
    st.title("Audio-Video Utility Studio")
    st.write("Welcome to your utility studio!")

    # Example usage of your toolkit
    # audio_toolkit.run() 

if __name__ == "__main__":
    main()
