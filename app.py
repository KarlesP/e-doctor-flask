import csv
import diseaseprediction
import pandas as pd
from flask import Flask, render_template, jsonify, request, redirect, url_for
#import mySQLdb

app = Flask(__name__)
#conn = MySQLdb.connect(host='localhost',user='root',password='',db='disease_database')
app._static_folder = 'templates'
with open('templates/Testing.csv', newline='') as f:
        reader = csv.reader(f)
        symptoms = next(reader)
        symptoms = symptoms[:len(symptoms)-1]


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/testServices', methods=['GET'])
def dropdown():
        return render_template('includes/default.html', symptoms=symptoms)

@app.route('/disease_predict', methods=['POST'])
def disease_predict():
    selected_symptoms = []
    if(request.form['Symptom1']!="") and (request.form['Symptom1'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom1'])
    if(request.form['Symptom2']!="") and (request.form['Symptom2'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom2'])
    if(request.form['Symptom3']!="") and (request.form['Symptom3'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom3'])
    if(request.form['Symptom4']!="") and (request.form['Symptom4'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom4'])
    if(request.form['Symptom5']!="") and (request.form['Symptom5'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom5'])
        

    # disease_list = []
    # for i in range(7):
    #     disease = diseaseprediction.dosomething(selected_symptoms)
    #     disease_list.append(disease)
    # return render_template('disease_predict.html',disease_list=disease_list)
    disease = diseaseprediction.dosomething(selected_symptoms)
    return render_template('disease_predict.html',disease=disease,symptoms=symptoms)

@app.route('/api_predict', methods=['POST'])
def api_predict():
    symptoms = request.json
    symptomlist = [symptoms["symptom1"], symptoms["symptom2"],symptoms["symptom3"], symptoms["symptom4"],symptoms["symptom5"]]
    diseasejson = diseaseprediction.dosomething(symptomlist)
    return jsonify(prediction=diseasejson[0])
# @app.route('/default')
# def default():
#         return render_template('includes/default.html')
 

@app.route('/drug', methods=['POST'])
def drugs():
    medicine = request.form['medicine']
    return render_template('homepage.html',medicine=medicine,symptoms=symptoms)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    app.run(debug=True)