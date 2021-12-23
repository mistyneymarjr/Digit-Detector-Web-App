import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import streamlit.components.v1 as components
def app():
    MODEL_DIR = os.path.join(os.path.dirname(__file__), 'model')
    print(MODEL_DIR)
    if not os.path.isdir(MODEL_DIR):
        os.system('runipy train.ipynb')

    model = load_model('model')
    st.markdown('<style>body{color: Black; background-color: #ffe6ff}</style>', unsafe_allow_html=True)

    st.title('My Digit Recognizer')

    components.html("<html><body><h3>©️ Digit recognizer by Monika Chauhan</h3></body></html>", width=10000, height=125)

 
    # data = np.random.rand(28,28)
    # img = cv2.resize(data, (256, 256), interpolation=cv2.INTER_NEAREST)

    SIZE = 700
    mode = st.checkbox("Draw?", True)

    canvas_result = st_canvas(
        fill_color='#000000',
        stroke_width=20,
        stroke_color='#FFFFFF',
        background_color='#000066',
        width=SIZE,
        height=150,
        drawing_mode="freedraw"  if mode else "transform",
        key='canvas')

    if canvas_result.image_data is not None:
        img = cv2.resize(canvas_result.image_data.astype('uint8'), (28, 28))
        rescaled = cv2.resize(img, (SIZE, 150), interpolation=cv2.INTER_NEAREST)
        st.write('Model Input')
        # st.success("Model Input")
        # components.html("<html><body><h3>Model Input</h3></body></html>", width=10000, height=125)
        
        st.image(rescaled)

    if st.button('Predicting output'):
        test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        val = model.predict(test_x.reshape(1, 28, 28))
        st.write(f'result: {np.argmax(val[0])}')
        st.bar_chart(val[0])

    st.success("Design & Developed By Monika Chauhan 👨‍💻")
