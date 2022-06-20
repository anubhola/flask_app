#importing the lilbrary

import pickle
from flask import Flask,render_template,request
app = Flask(__name__)
loadedmodel=pickle.load(open('model.pkl','rb'))

#Global variable

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/prediction',methods=['POST'])
def prediction():
    battery_power=request.form["Battery_power"]
    int_memory=request.form['int_memory']
    ram=request.form['ram']

    prediction=loadedmodel.predict([[battery_power,int_memory,ram]])

    print(prediction)

    if prediction[0]==0:
         prediction="Low cost"

    elif prediction[0]==1:
             prediction="Medium cost" 
             
    elif prediction[0]==2:
             prediction="High cost"
    else:
              
        prediction="very high cost"
    return render_template('form.html',api_output=prediction)


if __name__ == '__main__':
    app.run(debug=True)





   
