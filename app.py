import pickle

from flask import Flask, render_template, request
import flasgger
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)
model = pickle.load(open('cat_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender_val = request.form['Gender_Type']
        if(Gender_val=='Female'):
            Gender_val=1
        else:
            Gender_val = 2
        Age_value = int(request.form['Age'])
        region_val=request.form['Region_Type']
        if (region_val == 'RG268'):
            region_val = 1
        elif (region_val == 'RG277'):
            region_val = 2
        else:
            region_val = 3
        occup_val= request.form['ocup_Type']
        if(occup_val=='Other'):
             occup_val=1
        elif(occup_val=='Salaried'):
             occup_val = 2
        elif (occup_val == 'Self_Employed'):
             occup_val = 3
        else:
             occup_val = 4
        Channel_val = request.form['channel_Type']
        if (Channel_val == 'X3'):
             Channel_val = 3
        elif (Channel_val == 'X1'):
             Channel_val = 1
        elif (Channel_val == 'X2'):
             Channel_val = 2
        else:
             Channel_val = 4
        vintage_value=int(request.form['vintage'])
        Avg_Account_val = int(request.form['Avg_Account'])
        credit_val = request.form['credit']
        if (credit_val == 'No'):
            credit_val = 1
        elif (credit_val == 'Yes'):
            credit_val = 2
        Active_value=request.form['active']
        if (Active_value == 'No'):
             Active_value = 1
        else:
             Active_value = 2


        prediction=model.predict([[Gender_val,Age_value,region_val,occup_val,Channel_val,vintage_value,credit_val,Avg_Account_val,Active_value]])
        output=prediction
        if output==0:
            return render_template('index.html',prediction_texts="you Dont Have the Lead")
        else:
            return render_template('index.html',prediction_text="you Have the Lead")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port="8080")

