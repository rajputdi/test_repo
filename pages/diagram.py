import streamlit as st
from PIL import Image


def diagram():
    image = Image.open("pages/part2_architecture.png")
    st.image(image, caption="Architecture Diagram", width=700, height=700)
