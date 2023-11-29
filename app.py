from flask import Flask, render_template, request 
import jsonify # serializes data to JSOn format, wraps it in a Response object with the application/json mimetype
import pickle # used for serializing and de-serializing a Python object structure
import datetime as dt
from datetime import datetime
import numpy as np

app = Flask(__name__) # Intsantiate an object Flask
model = pickle.load(open('./model/seoul_bike_sharing_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        date = request.form['date']
        hour = int(request.form['hour'])
        temperature = float(request.form['temperature'])
        humidity = int(request.form['humidity'])
        wind_speed = float(request.form['windSpeed'])
        visibility = int(request.form['visibility'])
        solar_radiation = float(request.form['solarRadiation'])
        rainfall = float(request.form['rainfall'])
        snowfall = float(request.form['snowfall'])
        season = request.form['season']
        holiday = request.form['holiday']

        # Change the value of date
        date = datetime.strptime(date, '%Y-%m-%d').date()
        year = date.year
        month = date.month
        day = date.weekday()

        january, february, march, april, may, june, july, august, september, october, november, december = [0 for i in range(12)]
        monday, tuesday, wednesday, thursday, friday, saturday, sunday = [0 for i in range(7)]

        if month == 1:
            january = 1
        elif month == 2:
            february = 1
        elif month == 3:
            march = 1
        elif month == 4:
            april = 1
        elif month == 5:
            may = 1
        elif month == 6:
            june = 1
        elif month == 7:
            july = 1
        elif month == 8:
            august = 1
        elif month == 9:
            september = 1
        elif month == 10:
            october = 1
        elif month == 11:
            november = 1
        elif month == 12:
            december = 1

        if day == 0:
            monday = 1
        elif day == 1:
            tuesday = 1
        elif day == 2:
            wednesday = 1
        elif day == 3:
            thursday = 1
        elif day == 4:
            friday = 1
        elif day == 5:
            saturday = 1
        elif day == 6:
            sunday = 1



        # Change the value of hour
        hour_list = [0 for i in range(0,25)]
        hour_list[hour] = 1

        hour_dict = {f"hour_{i}": hour_list[i] for i in range(25)}


        # Change the value of season
        season_values = {
            'Winter': [1, 0, 0, 0],
            'Summer': [0, 1, 0, 0],
            'Autumn': [0, 0, 1, 0],
            'Spring': [0, 0, 0, 1]
        }

        if season in season_values:
            season_Winter, season_Summer, season_Autumn, season_Spring = season_values[season]
        else:
            season_Winter, season_Summer, season_Autumn, season_Spring = [0, 0, 0, 0]

        # Change the value for Holiday
        holiday_num = 0
        if holiday == "Holiday":
            holiday_num = 1

        features = [temperature, humidity, wind_speed, visibility, solar_radiation, rainfall, snowfall, year, holiday_num, 
                    season_Autumn, season_Spring, season_Summer, season_Winter, hour_dict["hour_0"], hour_dict["hour_1"], hour_dict["hour_2"], hour_dict["hour_3"], hour_dict["hour_4"],
                    hour_dict["hour_5"], hour_dict["hour_6"], hour_dict["hour_7"], hour_dict["hour_8"], hour_dict["hour_9"], hour_dict["hour_10"],
                    hour_dict["hour_11"], hour_dict["hour_12"], hour_dict["hour_13"], hour_dict["hour_14"], hour_dict["hour_15"], hour_dict["hour_16"],
                    hour_dict["hour_17"], hour_dict["hour_18"], hour_dict["hour_19"], hour_dict["hour_20"], hour_dict["hour_21"], hour_dict["hour_22"],
                    hour_dict["hour_23"], hour_dict["hour_24"], friday, monday, saturday, sunday, thursday, tuesday, wednesday, april, august, december, 
                    february, january, july, june, march, may, november, october, september]
        prediction = model.predict([features])
        return render_template('index.html',prediction_text="The predicted number of bikes for hour {} is {}.".format(hour, prediction))
    
if __name__ == "__main__":
    app.run(debug=True)