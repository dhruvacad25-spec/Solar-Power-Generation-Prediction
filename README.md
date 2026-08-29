# ☀️ Solar Power Generation Prediction

A machine learning project that aims to analyze weather conditions and time-based factors to predict solar power generation.

## 📌 Project Overview

Solar power generation is highly dependent on environmental and weather conditions. Accurate prediction of solar energy generation can help improve energy planning, resource management, and renewable energy utilization.

This project focuses on preparing and analyzing a large-scale solar power generation dataset. Weather conditions and time-based features are integrated to create a clean dataset that will later be used for machine learning-based solar power generation prediction.

---

## 🎯 Problem Statement

Solar power generation varies depending on weather conditions, location, time, and seasonal patterns. The variability of solar energy makes accurate prediction challenging.

The objective of this project is to develop a machine learning-based system that can analyze historical solar generation and weather data to predict solar power generation.

---

## 🎯 Objectives

- Analyze historical solar power generation data.
- Study the relationship between weather conditions and solar generation.
- Clean and preprocess large-scale time-series data.
- Handle missing values and inconsistent records.
- Extract useful time-based features from timestamps.
- Prepare a machine learning-ready dataset.
- Develop and evaluate machine learning models for solar power generation prediction in the next phase.

---

## 📊 Dataset

The project initially uses four datasets:

### 1. Solar Power Generation Data

Contains:

- `CampusKey`
- `SiteKey`
- `Timestamp`
- `SolarGeneration`

**Original records:** 2,731,946

### 2. Weather Conditions Data

Contains:

- `CampusKey`
- `Timestamp`
- `ApparentTemperature`
- `AirTemperature`
- `DewPointTemperature`
- `RelativeHumidity`
- `WindSpeed`
- `WindDirection`

**Original records:** 371,769

### 3. Solar Site Information

Contains information about:

- Campus
- Solar site
- kWp
- Number of panels
- Panel
- Inverter
- Optimizers
- Location coordinates

**Original records:** 42

### 4. Monthly Solar Generation Summary

Contains:

- `SiteKey`
- `Year`
- `Month`
- `DataStatus`
- `AverageSolarGeneration`
- `MaxSolarGeneration`
- `MinSolarGeneration`

**Original records:** 1,176

---

## 🔄 Data Preprocessing

The following preprocessing steps were performed:

### 1. Missing Value Analysis

All datasets were analyzed for missing values.

The solar generation dataset contained a significant number of missing target values, while the weather dataset contained missing values in multiple weather features.

### 2. Target Value Cleaning

Rows with missing `SolarGeneration` values were removed because the target variable cannot be reliably used for supervised model training.

- Original solar generation records: **2,731,946**
- Records after removing missing target values: **1,195,645**

### 3. Weather Data Analysis

The missing-value patterns were analyzed across different campuses.

Campuses 4 and 5 contained extremely large consecutive gaps in weather data. To avoid unrealistic large-scale data imputation, these campuses were excluded from the weather-based modeling dataset.

The final modeling dataset uses:

- Campus 1
- Campus 2
- Campus 3

### 4. Weather Data Cleaning

For short gaps in weather data:

- Limited linear interpolation was applied.
- The interpolation limit was set to 96 records, representing approximately 24 hours of 15-minute interval data.
- Interpolation was performed separately for each campus.

Remaining missing values in:

- `ApparentTemperature`
- `AirTemperature`
- `DewPointTemperature`
- `RelativeHumidity`

were filled using the median value of the corresponding campus.

### 5. Wind Feature Handling

`WindSpeed` and `WindDirection` contained a large number of missing values after interpolation.

These features were removed from the final modeling dataset to avoid excessive artificial data imputation.

### 6. Dataset Integration

The cleaned solar generation data was merged with the cleaned weather dataset using:

```text
CampusKey + Timestamp
