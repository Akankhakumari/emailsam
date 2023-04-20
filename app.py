import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

model= pickle.load(open("Emailspam.pkl", "rb"))
c= pickle.load(open("c.pkl", "rb"))

@app.route('/')
def home():
    
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = [request.form['text']]
    t_data = c.transform(data)
    output = model.predict(t_data)

    if(len(data[0])==0):
        return render_template('home.html', msg = "Enter your e-mail text above...")
    
    if output=='ham':
        return render_template('home.html', ham = "NO SPAM")
    else:
        return render_template('home.html', spam = "SPAM MAIL")

# In[ ]:



if __name__=="__main__":
    app.run(debug=True)

