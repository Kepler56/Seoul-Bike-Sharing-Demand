# Import the necessary libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle

# Load the dataset
file_path = "C:\\Users\\Sascha\\OneDrive\\Desktop\\Seoul Bike Sharing Analysis\\data\\SeoulBikeData.csv"
df = pd.read_csv(file_path, encoding='unicode_escape')

# Rename the columns
renamed_columns = ['date', 'rented_bike_count', 'hour', 'temperature', 'humidity', 
                   'wind_speed', 'visibility', 'dew_point_temperature', 'solar_radiation', 
                   'rainfall', 'snowfall', 'seasons', 'holiday', 'functional_day']
df.columns = renamed_columns

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

# Only keep the functional days
df = df[df['functional_day'] == "Yes"]
df.drop('functional_day', inplace=True, axis=1)

# Drop Dew Point Temperature -> Multicolinearity
df.drop('dew_point_temperature', inplace=True, axis=1)

# Create new columns from the date column
years = list(df['date'].dt.year)
months_list = list(df['date'].dt.month)
days_list = list(df['date'].dt.day_of_week)

month_dictionary = {
    1: 'January',
    2: 'February',
    3: 'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September', 
    10:'October',
    11:'November',
    12:'December'
}
day_dictionary = {
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday' 
}

months = [month_dictionary[month] for month in months_list]
days = [day_dictionary[day] for day in days_list]

# Add the new information to the dataframe 
df['years'] = years
df['months'] = months
df['days'] = days

# Drop the date column as it is no longer needed 
df.drop(columns=['date'], inplace=True)

# One hot encoding
new_df = pd.get_dummies(df, columns=['holiday', 'seasons', 'hour', 'days', 'months'], dtype='int64')

# Transform the target variable
#new_df['rented_bike_count'] = np.sqrt(new_df['rented_bike_count'])

# Select independent and dependent variables
x = new_df.drop('rented_bike_count', axis=1)
y = new_df['rented_bike_count']

# Split the data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Feature scaling with Standardization
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

# Instantiate the model
rf_Model = RandomForestRegressor(n_estimators=400, max_depth=25, min_samples_split=2, max_features='sqrt')

# Fit the model
rf_Model.fit(x_train, y_train)

# Pickle file of our model
# open a file, where you ant to store the data
file = open('./model/seoul_bike_sharing_model.pkl', 'wb')
# dump information to that file
pickle.dump(rf_Model, file)

