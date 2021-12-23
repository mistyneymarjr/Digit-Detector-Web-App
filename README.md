# Digit-Detector-Web-App
A simple Model which takes the input by user in a drawable canvas and predicts the output.

[streamlit](https://www.streamlit.io/) is an open-source app framework, which is the easiest way for data scientists and machine learning engineers to create beautiful, performant apps. All in pure Python, no longer fiddling with javascript.

This demo contains two parts: training a simple digit recognition model using mnist dataset and a webapp to live demo that model.
 
## Running demo

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

