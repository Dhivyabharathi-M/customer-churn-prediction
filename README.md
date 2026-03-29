# Customer Churn Prediction + Rule-Based Logic

## Project Overview

This project focuses on predicting customer churn using Machine Learning models and comparing them with a Rule-Based system.

The goal is to identify customers who are likely to leave (churn) and provide insights that can help businesses retain them.

---

## Dataset Used

### IBM Telco Customer Churn Dataset (Extended Version)

Dataset Link:  
https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset

###  Dataset Description

- Total Records: 7,043 customers  
- Total Features: 33 columns  
- Includes:
  - Customer demographics (including **Age**)
  - Service details
  - Account information
  - Financial data
  - Churn details (Churn Label, Churn Score, Churn Reason)

---

## 🎯 Why This Dataset Was Chosen

This dataset perfectly aligns with the assignment requirements:

| Assignment Field | Dataset Column | Match |
|----------------|---------------|------|
| Age | Age | Direct |
| Income | Monthly Charges / Revenue | Strong Match |
| Purchases | Total Charges | Strong Match |
| Membership | Contract | ✅ Direct |
| Churn | Churn Label / Value | ✅ Direct |

-> This eliminates the need for complex feature mapping and makes the dataset highly suitable.

---

## 🔍 Project Workflow

### 1. Data Loading
- Dataset was loaded from Excel format
- Initial inspection performed

---

### 2. Exploratory Data Analysis (EDA)

EDA was performed to understand:
- Distribution of features
- Relationship between features and churn
- Class imbalance

### Key Observations:
- Customers with **high monthly charges** tend to churn more
- **Month-to-month contracts** have higher churn
- Customers with **low tenure** are more likely to leave

---

### 3. Data Preprocessing

Based on EDA insights:
- Removed irrelevant and leakage columns
- Converted categorical data to numeric
- Handled data types
- Performed feature engineering

### Feature Engineering:
- Average monthly spend
- New customer flag
- Contract type flag

---

### 4. Machine Learning Models

The following models were used:

- Logistic Regression (baseline)
- Random Forest (ensemble – bagging)
- XGBoost (ensemble – boosting)
- SVM (Support Vector Machine)

---

## Why These Models Were Chosen

These models were selected based on research from:
- Kaggle implementations
- Medium articles
- Research papers

### 🔹 Logistic Regression
- Simple baseline model
- Helps understand linear relationships

### 🔹 Random Forest
- Handles non-linear data
- Reduces overfitting

### 🔹 XGBoost
- Advanced boosting algorithm
- Captures complex patterns
- Performs best on structured data

### SVM
- Effective for high-dimensional data
- Uses kernel trick for non-linear classification

---

## Challenges Faced

- Initial model accuracy was below 80%
- Dataset contains:
  - Noise
  - Overlapping patterns
  - Complex customer behavior

---

## 5. Hyperparameter Tuning

To improve performance:
- RandomizedSearchCV was used
- Models tuned:
  - Random Forest
  - XGBoost

### Result:
- XGBoost improved from ~78% → ~81% accuracy

Further improvements were limited due to real-world data complexity.

---

## 6. Model Evaluation

Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

-> Not only accuracy, but all metrics were considered for fair comparison.

---

## 7. Rule-Based Model

A simple rule-based system was implemented using conditions such as:
- High monthly charges
- Low tenure
- Month-to-month contract

### Advantages:
- Easy to understand
- Quick decision-making

### Limitations:
- Cannot adapt automatically
- Lower accuracy
- Cannot detect complex patterns

---

## 8. Final Conclusion

- **Best Model:** Tuned XGBoost  
- **Accuracy:** ~81%  

### Why XGBoost is Best:
- Captures complex patterns
- Handles structured data effectively
- Performs better across multiple evaluation metrics

---

## ML vs Rule-Based

| Aspect | ML Model | Rule-Based |
|------|--------|----------|
| Accuracy | High | Low |
| Adaptability | High | Low |
| Interpretability | Medium | High |

-> ML model is better for prediction  
-> Rule-based is useful for quick insights

---

## End-to-End Deployment

The model was deployed using Flask:
- User inputs customer details
- Model predicts churn probability
- Displays risk level (Low / Medium / High)

---
customer-churn-prediction/
│
├── data/
│ └── telco_customer_churn.xlsx
│
├── notebooks/
│ └── churn_prediction.ipynb
│
├── models/
│ ├── model.pkl
│ └── scaler.pkl
│
├── app/
│ ├── app.py
│ └── templates/
│ └── index.html
│
├── requirements.txt
└── README.md
---

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Flask
- Matplotlib, Seaborn

---

## Final Note

This project demonstrates:
- Data analysis
- Machine learning modeling
- Model comparison
- Real-world deployment

It provides a complete pipeline from raw data to prediction system.
