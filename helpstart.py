import streamlit as st
import streamlit.components.v1 as components
import cv2
import numpy as np
import webbrowser



def app():
    st.title("Digit Recogniser using Canvas")
    
    components.html('<div style="width:100%;height:0;padding-bottom:56%;position:relative;"><iframe src="https://giphy.com/embed/YWB5gTzRDhGMM" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>',width=480,height=360)
    # <iframe src="" width="480" height="372" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/YWB5gTzRDhGMM">via GIPHY</a></p>
   
    
    
    
    
    st.markdown('''
                In Machine learning, Artificial Neural Networks (ANN) play a major role in showcasing the power of statistics and mathematics to solve complex and non-linear problems. ANN has been there in the field of machine learning and Artificial Intelligence for a long time, but recent improvements in computational power and big data is helping them to show how powerful they are. They can be used to solve both supervised and unsupervised, classification and regression problems, computer vision etc. In this article, we shall be implementing an ANN from scratch and apply it to solve a simple problem of detecting digits from 0–9.
                Neural Network is similar to logistic regression (perceptron) but with more layers and hidden units. Here’s is what a single layer perceptron (logistic regression) looks like.
   ''')
    First=cv2.imread("1st.png")
    st.image(First,caption='Back-propogation in ANN', channels="BGR", width=500) 
    st.markdown('''            
# 1. Introduction

- The handwritten digit recognition is the ability of computers to recognize human handwritten digits. 
- Developing such a system includes a machine to understand and classify the images of handwritten digits as 0-9.
- The handwritten digit recognition uses the image of a digit and recognizes the digit present in the image.

# 2. Objective and Algorithm 

### 2.1 Objective

- The objective of the project is to create a handwritten digit recognition model that can recognise the handwritten digits 
- Our second objective is to create a web application for our model to make it accessible for the users. The web app will take image as an input and will give the predicted results based on the model evaluations


### 2.2 Algorithm
1. First install all the dependencies

    ```
    pip install -r requirements.txt
    ```

2. Train model

    Run all the cells of [train.ipynb](train.ipynb) manually or run it using runipy.

    ```
    runipy train.ipynb
    ```

3. Run demo web-app

    Demo your model by running [app.py](app.py)

    ```
    streamlit run app.py
    ```
# 4. Methodology

The project can be carried out in the following way:
- Import the libraries and load the dataset
- Preprocess the data
- Create the model
- Train the model
- Evaluate the model
- Create an application to predict digits



# 5. Result
The main objective is achieved the web application can successfully detects Handwritten digit.


# 6. Future Work

There is always a scope of improvement. Here are a few things which can be considered to improve. 
* The model can be modified to detect multiple digits in a single frame of reference.
* We can also write a script to access our web camera and take a real time input.


# 7. Conclusion

Results can be achieved by ML algorithms such as CNN for better results.
Deploying web application will be useful to the users to access the model more easily and efficiently without considering many requirement factors.
With this project I learnt a lot, especially about the platform like Streamlit which is not very commonly used but is very helpful for such implementations.
 
''')
   