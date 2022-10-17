import streamlit as st
import numpy as np
import cv2
from PIL import Image
from io import BytesIO
buf = BytesIO()


nav = st.sidebar.radio("Navigation", ["Home", "About"], index=0)

if nav=="Home":

    banner = Image.open("banner.jpg")
    new_image = banner.resize((970, 450))
    st.image(new_image)

    st.title("Coloured Image to B&W Converter")
    uploaded_file = st.file_uploader("Upload Image Here",['png','jpg','jpeg'])
    # print(uploaded_file)
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        # print(img)
        img_array=np.array(img)
        # print(imag_array)
        converted = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY) # numpy array

        inpt,otpt = st.columns(2) # containers
        otpt.subheader("Result:")
        otpt.image(converted)
        inpt.subheader("Original:")
        inpt.image(uploaded_file)

        st.balloons()
        img_file = Image.fromarray(converted) # converted numpy array to image file
        img_file.save(buf, format='JPEG') # saving this image file to buffer memory

        byte_im = buf.getvalue() # data for st.download_button parameter
        btn = otpt.download_button(
        label="Download Image",
        data=byte_im,
        file_name="output.jpg",
        mime="image/jpeg",
        )

else:
    me = Image.open("developer.png")
    me_resized = me.resize((200, 200))
    st.image(me_resized)
    st.markdown("This web application is developed by [Akshay Rajput](https://www.linkedin.com/in/akshay-189a48200/)")
