import streamlit as st
from PIL import Image


# Adding an expander so the browser will wait for the camera allowance till the user press the expander button
with st.expander("Start Camera"):

    # Start the camera
    camera_image = st.camera_input('Camera')

# Checking if there is an image != None
if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)

# Adding expander so the browser will wait the user if they prefer to upload image
with st.expander("Upload Image"):
    # Upload image filed
    uploaded_image = st.file_uploader("Select Image")

# Checking if there is an image != None
if uploaded_image:
    # Create a pillow image instance
    img = Image.open(uploaded_image)

    # Convert the image to greyscale
    grey_img = img.convert('L')

    # Render the greyscale image to the webpage
    st.image(grey_img)









