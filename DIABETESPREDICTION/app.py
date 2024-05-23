from flask import Flask,render_template,request
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
model=joblib.load("C:/Users/SriRam/Desktop/DIABETESPREDICTION/predict.joblib")
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def show_form():
    return render_template("diabetes.html")
@app.route('/diabetes',methods=['GET','POST'])
def diabetes():
    if request.method == 'POST':
        glucose= float(request.form['glucose'])
        bp=float(request.form['bp'])
        skinthickness=float(request.form['skinthickness'])
        insulin=float(request.form['insulin'])
        bmi=float(request.form['bmi'])
        diabetespercent=float(request.form['diabetespercent'])
        age=float(request.form['age'])
        Gender=float(request.form['Gender'])
        features=np.array([glucose,bp,skinthickness,insulin,bmi,diabetespercent,age,Gender]).reshape(1,-1)
        predictions = model.predict(features)
        if predictions==0:
            return render_template('diabetes.html', fruit="No Diabetes")
        else:
            return render_template('diabetes.html', fruit="Chance of Diabetes")
    return render_template('diabetes.html')
if __name__ == '__main__':
    app.run(debug=True)