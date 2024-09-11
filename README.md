# Readmission prediction for heart failure patients

## Problem Statement
Heart failure is a very common ailment leading to fatalities if not 
attended to promptly. Even for the patients who get proper treatment, hospital readmissions result in a significant risk of death and a financial burden for patients, their 
families as well as the already overburdened healthcare systems. Prediction of at-risk 
patients for readmission allows for targeted interventions that reduce morbidity and 
mortality.
1. Develop a machine learning model with the end objective to predict readmission of 
heart-failure patients within 30-days of discharge from the hospital. 
2. We have provided a subset of tables at the below one-Drive link for this problem.
Veersa Hackathon Submission 2024
3. Participants will further decide which tables they will use to solve the problem.
4. Link to mimic-III table descriptions. - https://mimic.mit.edu/docs/iii/tables/
5. Before actual prediction, detailed data analysis is expected to support the model.
6. Below are the list of Diagnosis codes (Icd9_codes) representing heart-failure: 
('39891','40201','40211','40291','40401','40403','40411','40413','40491','40493','4280','4
281','42820','42821','42822','42823','42830','42831','42832','42833','42840','42841','428
42','42843','4289')
## Dataset
The dataset used for this project includes patient information, admissions, and discharge details from hospital records. It includes features such as patient demographics, diagnoses, treatment records, and severity scores.

### Columns:
- `row_id`
- `subject_id`
- `hadm_id`
- `drg_type`
- `drg_code`
- `description`
- `drg_severity`
- `drg_mortality`

## Project Overview
This project aims to predict the likelihood of a patient being readmitted to the hospital within 30 days after being discharged due to heart failure. The model is designed to help healthcare providers identify at-risk patients, improving patient care and reducing hospital readmissions.

### Steps in the Project:
1. **Data Wrangling**: Cleaning the dataset by handling missing values, duplicates, and outliers.
2. **Feature Engineering**: Creating relevant features to improve the model's prediction accuracy.
3. **Exploratory Data Analysis**: Generating visualizations and summary statistics to understand the dataset.
4. **Model Building**: Using machine learning models like Random Forest, Logistic Regression, and XGBoost to predict 30-day readmission.
5. **Evaluation**: Measuring model performance using metrics such as precision, recall, F1 score, and ROC-AUC.

## Models Used:
- Logistic Regression
- Random Forest
- XGBoost
- Decision Tree 

## Performance Metrics
Due to class imbalance, accuracy alone isn’t sufficient for evaluating model performance. The following metrics are used:
- **Precision**
- **Recall**
- **F1-Score**
- **ROC-AUC**

## Conclusion
The prediction model helps healthcare providers take preventive measures to avoid heart failure readmissions within 30 days. This reduces financial costs and improves patient outcomes by providing targeted interventions to those most at risk.
