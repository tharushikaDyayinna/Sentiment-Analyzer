# Sentiment-Analyzer

## Introduction
This tool is designed to analyze the sentiment of text input, helping users understand the emotional tone conveyed in their messages, documents, or social media posts. Whether you're a developer looking to integrate sentiment analysis into your applications or a user curious about the sentiment of your text, this tool has you covered.

## Features
### Main Functionality: 
The project aims to detect emotions in text data using machine learning techniques. It utilizes a pre-trained sentiment analysis model to predict the emotion associated with input text.
Streamlit Interface: The project includes a user-friendly interface built with Streamlit, a Python library for creating web applications. Users can input text and receive predictions for the associated emotion.

![Screenshot (547)](https://github.com/tharushikaDyayinna/Sentiment-Analyzer/assets/102175958/c8426144-e409-4b6a-9d0e-c0373adf4200)

### Trained Model: 
The sentiment analyzer uses a trained machine learning model stored in a Pickle file (text_emotion2.pkl). This model has been trained on a dataset of text samples labeled with corresponding emotions.

### Emotion Prediction: 
The predict_emotions function takes input text and uses the trained model to predict the associated emotion. It returns the predicted emotion as a string.

### Prediction Probabilities: 
The get_prediction_proba function returns the probabilities of each emotion class as predicted by the model. These probabilities can provide insight into the confidence of the model's predictions.

### Visualization: 
The project includes visualizations of prediction probabilities using Altair, a declarative statistical visualization library for Python. It generates a bar chart to display the probabilities of each emotion class.

### User Input and Output: 
Users interact with the sentiment analyzer through a text area input field where they can enter text. After submitting the input, the predicted emotion, confidence score, and prediction probabilities are displayed.

### Styling and Presentation: 
The interface is styled using HTML and CSS to enhance the visual presentation. 

## Contributing
Contributions are welcome! If you'd like to contribute to the development of the Sentiment Analyzer

## Contact
If you have any questions, suggestions, or feedback, feel free to reach out to the project maintainer at tdyn.6910@gmail.com
