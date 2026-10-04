<img width="1536" height="1024" alt="Solar Intelligence Prediction Dashboard" src="https://github.com/user-attachments/assets/c9249464-eb6c-4ca1-9215-2e390164aa27" />

# ☀️ Solar Power Generation Prediction Using Machine Learning

## 📌 Project Overview

Solar power generation varies with factors such as weather conditions, location, and time. Predicting solar generation can help in understanding expected energy production and support better planning of renewable energy resources.

This project develops a **machine learning-based solar power generation prediction system** using historical solar generation data, weather conditions, site information, and temporal features.

The project includes data preprocessing, exploratory data analysis, machine learning model comparison, model tuning, and a Flask-based web application for prediction.

---

## 🎯 Objectives

- Analyze historical solar power generation data.
- Preprocess and clean solar and weather datasets.
- Identify important factors affecting solar power generation.
- Perform exploratory data analysis.
- Build and compare different machine learning regression models.
- Tune the selected machine learning model.
- Evaluate model performance using suitable regression metrics.
- Develop a web-based interface for solar power generation prediction.

---

## 📊 Dataset

The project uses the **UNISOLAR: An Open Dataset of Photovoltaic Solar Energy Generation in a Large Multi-Campus University Setting** dataset.

The dataset contains solar generation records along with weather conditions and solar site information.

### Main Data Components

- Solar power generation data
- Weather conditions
- Solar site information
- Monthly solar generation summaries

---

## ⚙️ Data Preprocessing

The preprocessing workflow includes:

1. Loading the raw solar generation and weather datasets.
2. Inspecting missing values and duplicate records.
3. Removing solar generation records with missing target values.
4. Identifying weather data with extensive missing blocks.
5. Removing unsuitable weather campuses.
6. Handling remaining missing weather values.
7. Merging solar generation data with weather data.
8. Converting timestamps into datetime format.
9. Extracting temporal features.
10. Preparing the final dataset for machine learning.

### Final Dataset

| Property | Value |
|---|---:|
| Rows | 1,123,099 |
| Columns | 13 |
| Missing Values | 0 |

---

## 🔍 Exploratory Data Analysis

Exploratory analysis was performed to understand the characteristics of solar generation and its relationship with different features.

The analysis included:

- Target variable distribution
- Boxplot analysis
- Correlation analysis
- Weather feature relationships
- Solar generation against temperature
- Solar generation against relative humidity
- Hourly solar generation patterns
- Temporal analysis
- Feature importance analysis

### Key Observations

- Solar generation generally increases during the morning and reaches higher levels around midday.
- Solar generation decreases during the afternoon and remains relatively low during nighttime.
- Weather variables show varying degrees of relationship with solar generation.
- `SiteKey` was the most influential feature in the Random Forest model.
- `Hour` and `RelativeHumidity` were also important predictive features.

---

## 🧠 Machine Learning Problem

This project is formulated as a **regression problem**.

### Features Used

The model uses the following features:

- `CampusKey`
- `SiteKey`
- `ApparentTemperature`
- `AirTemperature`
- `DewPointTemperature`
- `RelativeHumidity`
- `Year`
- `Month`
- `Day`
- `Hour`
- `DayOfWeek`

### Target Variable

```text
SolarGeneration
````

The objective is to predict the amount of solar power generated based on site, weather, and temporal information.

---

## 🤖 Machine Learning Models

The following regression models were evaluated:

| Model                   |      MAE ↓ |       MSE ↓ |     RMSE ↓ |       R² ↑ |
| ----------------------- | ---------: | ----------: | ---------: | ---------: |
| Linear Regression       |     6.9274 |    143.2813 |    11.9700 |     0.0846 |
| KNN Regressor           |     6.2624 |    124.7669 |    11.1699 |     0.2029 |
| Decision Tree           |     3.2457 |     48.3502 |     6.9534 |     0.6911 |
| Random Forest           |     2.4983 |     26.4524 |     5.1432 |     0.8310 |
| Gradient Boosting       |     4.0151 |     50.3227 |     7.0938 |     0.6785 |
| **Tuned Random Forest** | **2.4706** | **26.0050** | **5.0995** | **0.8339** |

### 🏆 Selected Model

The **Tuned Random Forest Regressor** achieved the best performance among the models evaluated in the current experiments.

| Metric   |   Value |
| -------- | ------: |
| MAE      |  2.4706 |
| MSE      | 26.0050 |
| RMSE     |  5.0995 |
| R² Score |  0.8339 |

### Tuned Parameters

```text
n_estimators = 50
max_depth = 20
min_samples_split = 2
min_samples_leaf = 1
random_state = 42
```

---

## 📈 Model Evaluation

The models were evaluated using the following regression metrics:

### Mean Absolute Error (MAE)

Measures the average absolute difference between the actual and predicted values.

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values and gives greater weight to larger errors.

### Root Mean Squared Error (RMSE)

The square root of MSE, representing prediction error in the same scale as the target variable.

### R² Score

Measures how well the model explains the variation in the target variable.

A higher R² score and lower MAE, MSE, and RMSE indicate better model performance.

---

## 🌐 Web Application

A Flask-based web application was developed to provide an interface for solar power generation prediction.

The application allows users to enter:

* Campus information
* Site information
* Temperature values
* Relative humidity
* Date information
* Time information

The trained machine learning model then generates a predicted solar generation value.

### Application Flow

```text
User Input
     ↓
Site + Weather + Temporal Features
     ↓
Flask Application
     ↓
Tuned Random Forest Model
     ↓
Solar Generation Prediction
     ↓
Result Display
```

---

## 🖥️ Web Application Pages

### 🏠 Home Page

Introduces the project, explains the prediction system, and presents the overall workflow.

### 🔢 Prediction Page

Allows users to enter site, weather, and temporal parameters.

### 📊 Result Page

Displays the predicted solar generation value along with model information.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**
* **Jupyter Notebook**
* **Flask**
* **Joblib**
* **HTML**
* **CSS**

---

## 📁 Project Structure

```text
Solar-Power-Generation-Prediction/
│
├── app.py
├── requirements.txt
├── tuned_random_forest_model.pkl
│
├── templates/
│   ├── home.html
│   ├── index.html
│   └── result.html
│
├── static/
│   └── css/
│       └── style.css
│
├── data/
│   ├── raw_data/
│   └── processed_data/
│
└── notebooks/
    ├── data_preprocessing_and_analysis.ipynb
    └── model_training_and_evaluation.ipynb
```

---

## 🔑 Important Features

### Site Features

* Campus
* Site

### Weather Features

* Air Temperature
* Apparent Temperature
* Dew Point Temperature
* Relative Humidity

### Temporal Features

* Year
* Month
* Day
* Hour
* Day of Week

Combining these features allows the model to capture relationships between solar generation, weather conditions, location, and time.

---

## 📌 Key Findings

* Solar generation exhibits a noticeable time-of-day pattern.
* Generation generally increases during the morning and reaches higher levels around midday.
* `SiteKey` was the most important feature in the Random Forest model.
* `Hour` was another important predictive feature.
* `RelativeHumidity` also contributed significantly to the model.
* Random Forest performed substantially better than Linear Regression, KNN, Decision Tree, and Gradient Boosting in the current experiments.
* Hyperparameter tuning provided a small improvement over the baseline Random Forest model.
* The final tuned model achieved an **R² score of 0.8339**.

---

## 🚀 Future Scope

* Improve temporal validation using stricter time-based splitting.
* Perform additional feature engineering.
* Explore further hyperparameter tuning.
* Incorporate additional weather and solar-related features.
* Investigate more advanced machine learning models.
* Explore deep learning approaches for solar forecasting.
* Deploy the prediction application as an online service if required.
* Integrate real-time weather data for dynamic prediction.

---

## 👥 Team Members

* **Adheena Sunil**
* **Bilsa Binu**
* **Dhruva C**
* **Ashhad M**

---

## 📚 References

1. S. Wimalaratne, D. Haputhanthri, S. Kahawala, G. Gamage, D. Alahakoon and A. Jennings, "UNISOLAR: An Open Dataset of Photovoltaic Solar Energy Generation in a Large Multi-Campus University Setting," *2022 15th International Conference on Human System Interaction (HSI)*, 2022, pp. 1–5.

2. J. Antonanzas et al., "Review of photovoltaic power forecasting," *Solar Energy*, vol. 136, pp. 78–111, 2016.

3. "Solar Photovoltaic Energy Forecasting Using Machine Learning and Deep Learning Technique," *2022 IEEE 9th Uttar Pradesh Section International Conference on Electrical, Electronics and Computer Engineering (UPCON)*, 2022.

4. [Python Documentation](https://docs.python.org/3/)

5. [Pandas Documentation](https://pandas.pydata.org/docs/)

6. [Scikit-learn Documentation](https://scikit-learn.org/stable/user_guide.html)

---

## 📌 Project Status

**Development Completed**

The project currently includes:

* Data preprocessing
* Exploratory data analysis
* Machine learning model comparison
* Random Forest model tuning
* Model evaluation
* Flask web application
* Prediction interface
* Result visualization

Online deployment is **subject to project requirements**.


