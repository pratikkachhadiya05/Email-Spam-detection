# Email Spam Detection

A simple web application to detect whether an email is spam or not using machine learning.

## Features

- Input email text and get instant prediction
- Built with Flask and scikit-learn
- Web interface with HTML, CSS, and JavaScript

## Installation

1. Clone the repository or download the files.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Ensure the model files (`model.pkl` and `fetur_extractor.pkl`) are present in the root directory. If not, run the Jupyter notebook `Spam_email.ipynb` to train and save the model.

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```
2. Open your web browser and go to `http://localhost:5000`
3. Enter email text in the form and click "Check" to see if it's spam or not.

## Project Structure

- `app.py`: Main Flask application
- `Spam_email.ipynb`: Jupyter notebook for model training
- `Datasets/email.csv`: Dataset used for training
- `templates/index.html`: HTML template for the web interface
- `static/css/style.css`: CSS styles
- `static/js/main.js`: JavaScript for interactivity
- `requirements.txt`: Python dependencies

## Technologies Used

- Python
- Flask
- scikit-learn
- HTML/CSS/JavaScript