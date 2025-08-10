from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle 
# from waitress import serve


# creating flask app
app = Flask(__name__)       # __name__ default argument

@ app.route('/')
def index():
    return render_template('index.html')
@ app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        N	= int(request.form['N'])
        P	= int(request.form['P'])
        K	= int(request.form['K'])
        temperature	= float(request.form['temperature'])
        humidity	= float(request.form['humidity'])
        ph	= float(request.form['ph'])
        rainfall    = float(request.form['rainfall'])
        
        model = pickle.load(open('OAP.pkl', 'rb'))
        
        prediction = model.predict(np.array([[N, P, K, temperature, humidity, ph, rainfall]]))
        
        return render_template('index.html',prediction=prediction )
# python main
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=8000)