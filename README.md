<img width="1536" height="1024" alt="Solar Intelligence Prediction Dashboard" src="https://github.com/user-attachments/assets/c9249464-eb6c-4ca1-9215-2e390164aa27" />

# ☀️ Solar Power Generation Prediction Using Machine Learning

A machine learning-based web application that predicts solar power generation using solar-site information, weather conditions, and temporal features. The project combines data preprocessing, exploratory data analysis, regression models, and a Flask web application to provide solar generation predictions through a user-friendly interface.

## 🌐 Live Website

**Try the application here:**
https://solar-power-generation-prediction-vt3h.onrender.com

Users can enter site, atmospheric, and time-related parameters to obtain a predicted solar generation value.

## 📌 Project Overview

Solar power generation depends on multiple factors, including weather conditions, location, and time. Understanding these factors can help improve the planning and utilization of solar energy systems.

This project explores historical solar generation and weather data to develop machine learning models that estimate solar power generation. The selected model is integrated into a Flask web application and deployed online using Render.

## 🎯 Objectives

* Analyze historical solar power generation and weather data.
* Perform data cleaning, preprocessing, and exploratory data analysis.
* Identify patterns and relationships between solar generation and relevant features.
* Train and compare multiple machine learning regression models.
* Optimize the selected model for practical deployment.
* Develop a Flask-based web application for generating predictions.
* Deploy the application online for public access.

## 📊 Dataset

The project uses the **UNISOLAR solar power generation dataset**, which contains photovoltaic generation measurements and associated weather and solar-site information.

**Dataset source:** [UNISOLAR — Solar Power Generation Dataset on Kaggle](https://www.kaggle.com/datasets/cdaclab/unisolar)

The dataset includes information such as:

* Solar generation measurements
* Campus and site identifiers
* Timestamps
* Apparent temperature
* Air temperature
* Dew point temperature
* Relative humidity
* Solar-site and panel information in the original source data

## 🧹 Data Preprocessing

The raw solar and weather datasets were cleaned and prepared before model development.

Key preprocessing steps included:

* Removing records with missing solar generation values.
* Examining missing values and duplicate records.
* Excluding weather campuses with extensive missing-data blocks.
* Handling remaining missing weather values.
* Merging solar generation and weather data.
* Converting timestamps to datetime format.
* Extracting temporal features such as year, month, day, hour, and day of the week.
* Sorting records chronologically.
* Preparing training and testing datasets.

The final processed dataset contained **1,123,099 rows and 13 columns**, with no missing values.

## 🔍 Exploratory Data Analysis

Exploratory data analysis was performed to understand the dataset and identify useful patterns.

Key observations included:

* Solar generation generally rises during the morning, reaches higher levels around midday, and decreases during the afternoon.
* Air temperature showed a positive relationship with solar generation in the analyzed data.
* Relative humidity showed a negative relationship with solar generation.
* Site-related and temporal features provided useful information for predicting generation.

These observations helped guide feature selection and model development.

## 🤖 Machine Learning Models

The following regression algorithms were evaluated:

1. Linear Regression
2. K-Nearest Neighbors (KNN) Regression
3. Decision Tree Regression
4. Random Forest Regression
5. Gradient Boosting Regression

The models were compared using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and the coefficient of determination (R²).

### Final Deployment Model

A smaller **Random Forest Regressor** was trained specifically for deployment. The model uses fewer trees and a restricted maximum tree depth to reduce storage requirements while retaining comparable predictive performance.

| Parameter                | Value                   |
| ------------------------ | ----------------------- |
| Algorithm                | Random Forest Regressor |
| Number of trees          | 20                      |
| Maximum tree depth       | 12                      |
| Minimum samples to split | 2                       |
| Minimum samples per leaf | 1                       |
| Random state             | 42                      |
| Saved model              | `deployment_model.pkl`  |
| Compressed file size     | Approximately 3.44 MB   |

### Model Evaluation Results

The deployment model was evaluated on the test dataset.

| Evaluation Metric              | Result |
| ------------------------------ | -----: |
| Mean Absolute Error (MAE)      | 2.7039 |
| Root Mean Squared Error (RMSE) | 5.1504 |
| R² Score                       | 0.8305 |

An R² score of 0.8305 indicates that the model explains approximately 83.05% of the variance in the target values on the evaluated test set.

### Model Size Optimization

The original tuned Random Forest model occupied approximately 997 MB. A smaller deployment-specific model was created and saved using compression.

* Original model size: approximately 997 MB
* Deployment model size: approximately 3.44 MB
* Approximate size reduction: 99.65%

The smaller model provides a practical alternative for hosting the web application, with a modest change in the reported evaluation metrics.

## 🖥️ Web Application

The project includes a Flask web application with a dark, technology-inspired interface focused on solar intelligence.

### Features

* Project landing page and overview
* Interactive solar generation prediction form
* Solar-site configuration inputs
* Weather and atmospheric inputs
* Temporal parameter inputs
* Prediction results page
* Responsive interface
* Integration with the trained Random Forest model

### Application Workflow

**User Input → Flask Application → Feature Preparation → Random Forest Model → Solar Generation Prediction → Results Page**

1. The user opens the prediction form.
2. The user enters site, weather, and temporal parameters.
3. Flask arranges the input values in the feature order expected by the model.
4. The deployment model generates a prediction.
5. The application displays the predicted solar generation value.

## 🛠️ Technologies Used

* **Programming language:** Python
* **Data processing:** Pandas, NumPy
* **Machine learning:** Scikit-learn
* **Model serialization:** Joblib
* **Web framework:** Flask
* **Web server:** Gunicorn
* **Frontend:** HTML, CSS
* **Version control:** Git and GitHub
* **Deployment platform:** Render

## 📁 Project Structure

```text
Solar-Power-Generation-Prediction/
│
├── app.py
├── deployment_model.pkl
├── requirements.txt
├── README.md
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
└── data/
    ├── raw_data/
    └── processed_data/
        └── solar_power_generation_preprocessed.csv
```

*Note: The data directories and notebook files may be maintained locally rather than included in the deployment repository.*

## 🚀 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/dhruvacad25-spec/Solar-Power-Generation-Prediction.git
```

### 2. Open the project directory

```bash
cd Solar-Power-Generation-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask application

```bash
python app.py
```

### 5. Open the website

Visit:

http://127.0.0.1:5000

Ensure that `deployment_model.pkl` is present in the project directory alongside `app.py`.

## 📈 Key Outcomes

* Processed more than 1.1 million solar generation records.
* Conducted exploratory analysis of solar generation and weather patterns.
* Compared multiple regression algorithms.
* Developed a compact Random Forest deployment model.
* Reduced the saved model size by approximately 99.65%.
* Integrated the model into a Flask web application.
* Deployed the application on Render with a publicly accessible URL.

## 🔮 Future Enhancements

* Incorporate additional weather forecasts for future generation estimates.
* Explore time-series forecasting techniques.
* Improve model evaluation across different sites and seasonal conditions.
* Add interactive visualizations of historical and predicted generation.
* Develop monitoring and model-retraining workflows.

## 👥 Project Team

* Adheena Sunil
* Bilsa Binu
* Dhruva C
* Ashhad M

## 📚 References

1. S. Wimalaratne, D. Haputhanthri, S. Kahawala, G. Gamage, D. Alahakoon, and A. Jennings, “UNISOLAR: An Open Dataset of Photovoltaic Solar Energy Generation in a Large Multi-Campus University Setting,” *2022 15th International Conference on Human System Interaction (HSI)*, 2022. [DOI: 10.1109/HSI55341.2022.9869474](https://doi.org/10.1109/HSI55341.2022.9869474)

2. J. Antonanzas et al., “Review of photovoltaic power forecasting,” *Solar Energy*, vol. 136, pp. 78–111, 2016. [DOI: 10.1016/j.solener.2016.06.069](https://doi.org/10.1016/j.solener.2016.06.069)

3. “Solar Photovoltaic Energy Forecasting Using Machine Learning and Deep Learning Technique,” *2022 IEEE 9th Uttar Pradesh Section International Conference on Electrical, Electronics and Computer Engineering (UPCON)*, 2022. [DOI: 10.1109/UPCON56432.2022.9986446](https://doi.org/10.1109/UPCON56432.2022.9986446)

4. [Python Documentation](https://docs.python.org/3/)

5. [Pandas Documentation](https://pandas.pydata.org/docs/)

6. [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

---

**Project Status:** Developed and deployed. The Flask web application is available online through Render.

**Live Application:** https://solar-power-generation-prediction-vt3h.onrender.com
