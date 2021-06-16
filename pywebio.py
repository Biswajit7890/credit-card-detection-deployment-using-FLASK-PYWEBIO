from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server

import pickle
import numpy as np
model = pickle.load(open('cat_model.pkl', 'rb'))
app = Flask(__name__)

def predict():
    Gender_val = select('What is the Gender Type', ['Female', 'Male'])
    if (Gender_val == 'Female'):
        Gender_val = 1
    else:
        Gender_val = 2
    Age_value= input("Enter the Age", type=NUMBER)
    region_val= select('What is the Region', ['RG268', 'RG277','RG274'])
    if (region_val == 'RG268'):
        region_val = 1
    elif (region_val == 'RG277'):
        region_val = 2
    else:
        region_val = 3
    occup_val=select('What is the occupation', ['Other', 'Salaried','Self_Employed','Business'])
    if (occup_val == 'Other'):
        occup_val = 1
    elif (occup_val == 'Salaried'):
        occup_val = 2
    elif (occup_val == 'Self_Employed'):
        occup_val = 3
    else:
        occup_val = 4
    Channel_val=select('What is the Channel', ['X3', 'X1','X2','X4'])
    if (Channel_val == 'X3'):
        Channel_val = 3
    elif (Channel_val == 'X1'):
        Channel_val = 1
    elif (Channel_val == 'X2'):
        Channel_val = 2
    else:
        Channel_val = 4
    vintage_value=input("Enter the vintage", type=NUMBER)
    Avg_Account_val=input("Enter the Avg Account Balance", type=FLOAT)
    credit_val=select('What is the Credit', ['No', 'Yes'])
    if (credit_val == 'No'):
        credit_val = 1
    else:
        credit_val = 2
    Active_value=select('What is the Active_value', ['No', 'Yes'])
    if (Active_value == 'No'):
        Active_value = 1
    else:
        Active_value = 2
    prediction = model.predict([[Gender_val, Age_value, region_val, occup_val, Channel_val, vintage_value, credit_val,
    Avg_Account_val, Active_value]])
    output = prediction
    if output==0:
        put_text("Sorry You dont have the lead")

    else:
        put_text("You have the lead")
app.add_url_rule('/tool', 'webio_view', webio_view(predict),methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    app.run(host='localhost', port=80)