# Seoul-Bike-Sharing-Demand
<hr>

## Project Description
Bike sharing is a transportation system that allows individuals to rent bicycles for short periods, typically for a few hours or less, and return them to designated stations 
or docking points. It offers a convenient and flexible means of transportation, especially for short-distance trips within urban areas. By analyzing historical bike rental 
data along with other relevant factors such as weather conditions, holidays, and time of day we can develop models to predict the demand for bikes in the future. 
This information is crucial for bike-sharing operators to ensure an adequate supply of bikes at each location, optimize bike distribution, and meet the demand of users 
especially during peak hours or busy periods.

This project aims to **predict the number of bikes required at each hour for a stable supply of rental bikes in urban cities**. The prediction of bike count is based on various factors such as weather conditions, holidays, and functional hours.
<hr>

## Team
This project was made in a group of 3. You can find the LinkedIn of the teammates who contributed to the project below:
<div style="margin: 0 auto;">
  <a href="linkedin.com/in/houssem-rezgui-933378239" style="style-decoration: none; text-align:center;">
    <img src="https://media.licdn.com/dms/image/D4D03AQF-TLjsRvf4cQ/profile-displayphoto-shrink_400_400/0/1696193737692?e=1706140800&v=beta&t=-UsLJKIpwIY9jltG9Cn0LFwioWDjfYdYcMwag_03XAo" alt="Profile Photo" style="border-radius: 50%;" height="100px" width="100px"/>
  </a>
  
  <a href="linkedin.com/in/yahya-el-oudouni" style="style-decoration: none; text-align:center;">
    <img src="https://media.licdn.com/dms/image/D4E03AQEI2joaLyNfZA/profile-displayphoto-shrink_400_400/0/1685883749673?e=1706140800&v=beta&t=lkacIAxIEdK0SQSh_fxXej7D4c0w7ZF3NqKoBOEr7fc" alt="Profile Photo" style="border-radius: 50%; margin-left:20px;" height="100px" width="100px"/>
  </a>
</div>
<hr>

## Data
The dataset used in this project contains the count of public bicycles rented per hour in the Seoul Bike Sharing System with corresponding weather data and holiday 
information. It includes the following variables:
- **Date**: year-month-day
- **Rented Bike count**: Count of bikes rented at each hour
- **Hour**: Hour of he day
- **Temperature**: Temperature in Celsius
- **Humidity**: %
- **Windspeed**: m/s
- **Visibility**: 10m
- **Dew point temperature**: Celsius 
- **Solar radiation**: MJ/m2
- **Rainfall**: mm
- **Snowfall**: cm
- **Seasons**: Winter, Spring, Summer, Autumn
- **Holiday**: Holiday/No holiday
- **Functional Day**: NoFunc(Non Functional Hours), Fun(Functional hours)

Seoul Bike Sharing Demand. (2020). UCI Machine Learning Repository. <a href="https://doi.org/10.24432/C5F62R">Link to Data</a>.
<hr>

## Project Structure
The project structure is as follows:

<ol>
    <li><a>Importing libraries and data</a></li>
    <li>
        <a>Data Manipulation</a>
        <ul>
            <li><a>Loading the dataset</a></li>
            <li><a>Understanding the data</a></li>
            <li><a>Preprocessing the data</a></li>
            <ul>
                <li><a>Null Values</a></li>
                <li><a>Unique Values</a></li>
                <li><a>Duplicated Values</a></li>
                <li><a>Outliers</a></li>
            </ul>
        </ul>
    </li>
    <li>
        <a>Feature Extraction</a>
        <ul>
            <li><a>Look at the number of bike rented for functional days and non functional days</a></li>
            <li><a>Add new date type columns</a></li>
        </ul>
    </li>
    <li>
        <a>Exploratory Data Analysis</a>
        <ul>
            <li><a>Describe</a></li>
            <li><a>Influence that the features have on the number of bikes rented</a></li>
            <li><a>Scatter</a></li>
            <li><a>Correlation</a></li>
        </ul>
    </li>
    <li>
        <a>Feature Engineering</a>
        <ul>
            <li><a>Feature Encoding</a></li>
            <li><a>Transformation of the target variable</a></li>
            <li><a>Feature selection</a></li>
            <li><a>Splitting data into Train & Test sets</a></li>
            <li><a>Feature Scaling</a></li>
        </ul>
    </li>
    <li>
        <a>Model Building</a>
        <ul>
            <li><a>Function to train model</a></li>
            <li><a>Function to evaluate performance</a></li>
            <li><a>Function to plot</a></li>
            <li><a>Linear Regression</a></li>
            <li><a>Polynomial Regression</a></li>
            <li><a>Lasso Regression</a></li>
            <li><a>Ridge Regression</a></li>
            <li><a>Decision Tree Regression</a></li>
            <li><a>Random Forest Regression</a></li>
            <li><a>Model Evaluation</a></li>
        </ul>
    </li>
    <li><a>Flask API for model deployment</a></li>
</ol>

Please refer to the corresponding sections in the code for detailed implementation and analysis.
<hr>

## Tools & Technologies
- Jupyter Notebook
- Python
- Web
  - HTML
- Python Libraries:
  - Numpy
  - Pandas
  - Matplotlib
  - Seaborn
  - Sklearn
- Frameworks
  - Flask
  - Bootstrap
<hr>

## Findings

### Analysis
- The number of bikes rented is higher during the Summer and Autumn seasons, likely due to the warmer weather. This observation supports the strong correlation between temperature and bike rentals, as temperatures are generally warmer in summer. Additionally, the season with the lowest number of rented bikes is Winter, which can be attributed to colder weather conditions.
![image](https://github.com/Kepler56/Seoul-Bike-Sharing-Demand/assets/98602898/eda1f589-898f-417e-8697-7f49ca15060c)

- The number of bikes rented is higher during non-holiday periods, indicating that people are more likely to utilize bikes for daily commuting rather than recreational purposes during holidays. This finding aligns with the assumption that individuals use bikes for transportation to work. 
![image](https://github.com/Kepler56/Seoul-Bike-Sharing-Demand/assets/98602898/d04155d6-3dba-42bd-9747-de62b7f6bc14)

- During weekdays, there is a noticeable trend in bike rental times, with two prominent peaks occurring around 8 am and 6 pm. These peaks indicate that people are using bikes for their daily commute to work in the morning and returning home in the evening. Moreover, even though there is a lower number of rented bicycles during the weekend, there is still a gradual increase in rentals during the afternoons. 
![image](https://github.com/Kepler56/Seoul-Bike-Sharing-Demand/assets/98602898/04a26b01-7482-45e7-ab2f-cf062eae9a9a)

### Models

Among the various models we evaluated, the **Random Forest Regression** had the best performance. It achieved an impressive **R2 score of 0.88**, 
indicating its ability to explain a significant portion of the variance in the data. During training, the model exhibited exceptional accuracy with 
a **score of 0.98**.

Here is the barplot indicating the comparison between the different models:
![image](https://github.com/Kepler56/Seoul-Bike-Sharing-Demand/assets/98602898/93d0c0d9-32be-4a04-99ae-48880b93f48f)

Here is the graph showing the **Actual vs Predicted values** of the Random Forest Model:
![image](https://github.com/Kepler56/Seoul-Bike-Sharing-Demand/assets/98602898/a835c9a2-abfa-479d-a135-24e55573894a)

<hr>

## Flask API

We decided to implement the model deployment of our Random Forest Regression model using the **Flask API**. You can observe the demonstration in the video below:
.
<hr>

## Contact
If you have any questions or feedback, please contact me at [saschacauchon.pro@gmail.com] (or through my <a href="https://www.linkedin.com/in/scauchon/">(LinkedIn)</a>) 
or any of my teammates mentioned above.
