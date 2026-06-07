# Fake News Detection System

## Overview

This project is a Machine Learning and Natural Language Processing (NLP) based Fake News Detection System.

The system analyzes news articles and predicts whether the news is Fake or Real using TF-IDF Vectorization and Logistic Regression.

A Streamlit web application is also developed to allow users to enter news articles and get real-time predictions.

---

## Features

* Detects Fake and Real News Articles
* Uses Natural Language Processing (NLP)
* TF-IDF Text Vectorization
* Logistic Regression Classification
* Interactive Streamlit Web Application
* Real-Time Prediction
* Confidence Score Display

---

## Dataset Information

The dataset contains more than 44,000 news articles.

### Dataset Columns

* title
* text
* subject
* date

### Labels Used

* 0 → Fake News
* 1 → Real News

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* TF-IDF Vectorizer
* Logistic Regression

---

## Machine Learning Workflow

### 1. Data Collection

Loaded Fake.csv and True.csv datasets.

### 2. Data Preprocessing

* Added labels
* Merged datasets
* Shuffled data
* Checked missing values

### 3. Feature Engineering

Applied TF-IDF Vectorization to convert text into numerical features.

### 4. Train-Test Split

Dataset split into:

* 80% Training Data
* 20% Testing Data

### 5. Model Training

Used Logistic Regression for text classification.

### 6. Model Evaluation

Evaluated model using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### 7. Deployment

Developed and deployed a Streamlit web application.

---

## Model Performance

### Accuracy

98.33%

### Classification Metrics

* Precision: 98–99%
* Recall: 98–99%
* F1 Score: 98%

---

## Project Structure

Fake_News_Detection/

├── data/

├── screenshots/

├── model.pkl

├── vectorizer.pkl

├── app.py

├── notebook.ipynb

├── requirements.txt

├── README.md

└── .gitignore

---

## Installation

Clone the repository:

git clone https://github.com/your-username/fake-news-detection.git

Move to project directory:

cd fake-news-detection

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

## Future Improvements

* Deep Learning Models
* LSTM and Transformer Models
* News Source Verification
* Confidence Visualization Dashboard
* Multilingual News Detection

---

## Author

Vansh Kumar

Aspiring Data Scientist and AI Enthusiast
