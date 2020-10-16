from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np
filename='Extract_For_Pickle_File.pkl'
regressor=pickle.load(open(filename,'rb'))

app=Flask(__name__)

@app.route('/')
def home():
	return render_template('home_flight.html')


@app.route('/predict',methods=['POST'])
def predict():
	value1=list()

	if request.method == "POST":

		airline=request.form['Airline']
		if airline == 'Air Asia':
			value1 = value1 + [1,0,0,0,0,0,0,0]
		elif airline == 'Air India':
			value1 = value1 + [0,1,0,0,0,0,0,0]
		elif airline == 'GoAir':
			value1 = value1 + [0,0,1,0,0,0,0,0]
		elif airline == 'IndiGo':
			value1 = value1 + [0,0,0,1,0,0,0,0]
		elif airline == 'Jet Airways':
			value1 = value1 + [0,0,0,0,1,0,0,0]
		elif airline == 'Multiple carriers':
			value1 = value1 + [0,0,0,0,0,1,0,0]
		elif airline == 'SpiceJet':
			value1 = value1 + [0,0,0,0,0,0,1,0]
		elif airline == 'Vistara':
			value1 = value1 + [0,0,0,0,0,0,0,1]


		value2=list()

		source=request.form['Source']
		if source == 'Banglore':
			value2 = value2 + [1,0,0,0,0]
		elif source == 'Chennai':
			value2 = value2 + [0,1,0,0,0]
		elif source == 'Delhi':
			value2 = value2 + [0,0,1,0,0]
		elif source == 'Kolkata':
			value2 = value2 + [0,0,0,1,0]
		elif source == 'Mumbai':
			value2 = value2 + [0,0,0,0,1]


		value3=list()

		destination=request.form['Destination']
		if destination == 'Banglore':
			value3 = value3 + [1,0,0,0,0]
		elif destination == 'Cochin':
			value3 = value3 + [0,1,0,0,0]
		elif destination == 'Delhi':
			value3 = value3 + [0,0,1,0,0]
		elif destination == 'Hyderabad':
			value3 = value3 + [0,0,0,1,0]
		elif destination == 'Kolkata':
			value3 = value3 + [0,0,0,0,1]



		total_stops=request.form['Total_Stops']
		if total_stops == 'zero':
			stops = 0
		elif total_stops == 'one':
			stops = 1
		elif total_stops == 'two':
			stops = 2
		elif total_stops == 'three':
			stops = 3
		elif total_stops == 'four':
			stops = 4

	
		start = request.form["Start"]
		Journey_day = float(pd.to_datetime(start, format="%Y-%m-%dT%H:%M").day)
		Journey_mon = float(pd.to_datetime(start, format="%Y-%m-%dT%H:%M").month)
		print("Journey Date : ",Journey_day, Journey_mon)

		Dep_hour = int(pd.to_datetime(start, format ="%Y-%m-%dT%H:%M").hour)
		Dep_min = int(pd.to_datetime(start, format ="%Y-%m-%dT%H:%M").minute)




		final_values=[stops,Journey_day,Journey_mon,Dep_hour,Dep_min] + value1 + value2 + value3

		data=np.array([final_values])
		pred=int(regressor.predict(data)[0])
		return render_template('result.html', price1 = pred-100, price2 = pred+100)

if __name__ == '__main__':
	app.run(debug=True)