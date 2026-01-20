
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

vectorizer = pickle.load(open(os.path.join(BASE_DIR, "api/fetur_extractor.pkl"), "rb"))
model = pickle.load(open(os.path.join(BASE_DIR, "api/model.pkl"), "rb"))


app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, "templates"),
            static_folder=os.path.join(BASE_DIR, "static"))

app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

# Load the model and vectorizer
# model = pickle.load(open('model.pkl', 'rb'))
# vectorizer = pickle.load(open('fetur_extractor.pkl', 'rb'))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email_text = request.form.get('email')
        if email_text:

            features = vectorizer.transform([email_text])
            pred = model.predict(features)[0]
            prediction = "Spam" if pred == 1 else "Not Spam"
            # store letest reult f
            session['email'] = email_text
            session['prediction'] = prediction
        
        # Check if it's an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'prediction': prediction})
        else:
            return redirect(url_for('home'))
    
    email = session.get('email', '')
    prediction = session.get('prediction', None)
    return render_template("index.html", email=email, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)