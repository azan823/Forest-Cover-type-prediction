import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

rf = pickle.load(open('rf.pkl','rb'))

st.title("Forest Cover Type")
image = Image.open('main2.png')

st.image(image,caption='myimage',use_column_width=True)
user_input = st.text_input("Enter All Cover type Inputs")
if user_input:
    user_input = user_input.split(',')
    features = np.array([user_input],dtype=float)
    prediction = rf.predict(features).reshape(1,-1)
    prediction = int(prediction[0])
    cover_type_dict = {
    1: {"name": "Spruce/Fir", "image": "spruce fir.jpeg"},
    2: {"name": "Lodgepole Pine", "image": "lodgepole pine.jpeg"},
    3: {"name": "Ponderosa Pine", "image": "pendoresa pine.jpeg"},
    4: {"name": "Cottonwood/Willow", "image": "cotton wood willow.jpeg"},
    5: {"name": "Aspen", "image": "aspen.jpeg"},
    6: {"name": "Douglas-fir", "image": "Daug lis fir.jpeg"},
    7: {"name": "Krummholz", "image": "krumholz.jpeg"}
}
    cover_type_info = cover_type_dict.get(prediction)
    if cover_type_info is not None:
        forest_name = cover_type_info['name']
        forest_image = cover_type_info['image']


    col1,col2 = st.columns([2,3])

    with col1:
        st.write("Predicted Cover type")
        st.write(f"<h1 style='font-size: 40px; font-weight: bold;'>{forest_name}</h1>", unsafe_allow_html=True)
    with col2:
        final_image = Image.open(forest_image)
        st.image(final_image,caption=forest_name,use_column_width=True)