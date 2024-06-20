import streamlit as st
from pathlib import Path

# Function to get sample image files from the specified directory
@st.cache_data
def get_sample_image_files():
    sample_images_path = Path('sample_images')  # Using a relative path
    try:
        return {
            image_file.name: image_file
            for image_file in sample_images_path.iterdir()
            if image_file.is_file()
        }
    except FileNotFoundError:
        st.error("The specified directory does not exist.")
        return {}
    except PermissionError:
        st.error("You do not have permission to access this directory.")
        return {}

# Function to classify images into benign, malignant, and normal
def classify_image(image_name):
    # Placeholder classification logic
    if "benign" in image_name.lower():
        return "Benign"
    elif "malignant" in image_name.lower():
        return "Malignant"
    elif "normal" in image_name.lower():
        return "Normal"
    else:
        return "Unknown"

# Streamlit app setup
def main():
    st.title("Breast Cancer Detection")

    sample_images = get_sample_image_files()

    if sample_images:
        st.write("Sample Images:")
        for image_name, image_path in sample_images.items():
            st.write(f"Image: {image_name}")
            classification = classify_image(image_name)
            st.write(f"Classification: {classification}")
            st.image(str(image_path))

if __name__ == "__main__":
    main()
