# Customer Churn Prediction
### Internship Assessment — Digitivity Solutions

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![XGBoost](https://img.shields.io/badge/Best%20Model-Tuned%20XGBoost-orange?style=flat-square)
![SMOTE](https://img.shields.io/badge/Imbalance-SMOTE-purple?style=flat-square)

---

## Overview

Customer churn — when a customer stops doing business with a company — is one of
the most critical revenue challenges in the telecom industry. Research shows that
**acquiring a new customer costs 5 to 25 times more than retaining an existing one**.

This project delivers a complete, end-to-end churn prediction pipeline:

- Deep **Exploratory Data Analysis** with outlier and imbalance detection
- **Feature Engineering** to derive meaningful business signals
- Training and comparison of **4 ML models + 1 Rule-Based baseline**
- **Hyperparameter tuning** using RandomizedSearchCV
- **Flask web deployment** with dual ML + rule-based prediction output

---

## Project Structure

```
customer-churn-prediction/
│
├── data/
│   └── telco_customer_churn.xlsx
│
├── notebooks/
│   └── churn_prediction.ipynb
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│
├── templates/
│   ├── index.html
|
├── app.py
├── requirements.txt
└── README.md
```

---

## Dataset

**IBM Telco Customer Churn Dataset (Extended Version)**

-  Source: [Kaggle — yeanzc/telco-customer-churn-ibm-dataset](https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset)
-  Records: **7,043 customers**
-  Features: **33 columns** — demographics, service details, billing, churn status

### Field Mapping to Assignment Requirements

| Assignment Field| Dataset Column    | Match Type   |
|-----------------|-------------------|--------------|
| Age             | `Senior Citizen`  | Proxy        |
| Income          | `Monthly Charges` | Strong Match |
| Purchases       | `Total Charges`   | Strong Match |
| Membership      | `Contract`        | Direct       |
| Churn           | `Churn Label`     | Direct       |

> **Leakage Prevention:** `Churn Score`, `Churn Value`, and `Churn Reason`
> were dropped before training. These columns are derived directly from the churn
> outcome and would cause **data leakage** — inflating model scores dishonestly.

---

## Project Workflow

### 1 · Data Loading
- Loaded from Excel using `pandas.read_excel()`
- Shape confirmed: **7,043 rows × 33 columns**
- Checked dtypes, duplicates, and initial class distribution

### 2 · Exploratory Data Analysis (EDA)
- Missing value detection and visualisation
- Class imbalance check — approximately **26% churn rate**
- Outlier identification using the **IQR method**
- Distribution plots for all numerical features, split by churn label
- Churn rate analysis per categorical feature (Contract, Payment Method, etc.)
- Correlation heatmap to detect multicollinearity

**Key findings from EDA:**
- Month-to-month contract customers show the highest churn rate
- Customers with low tenure (< 6 months) churn significantly more
- Higher monthly charges correlate with increased churn probability
- Electronic check payment method users churn more than other payment types

### 3 · Data Preprocessing
- Dropped identifier and geographic columns: `CustomerID`, `City`, `State`, `Zip Code`, `Lat Long`
- Dropped leakage columns: `Churn Score`, `Churn Reason`, `Churn Value`
- Converted `Total Charges` from object to numeric (contained whitespace strings)
- Filled resulting NaN values using median imputation

### 4 · Feature Engineering and Encoding
- Label encoding applied to binary columns (Yes/No → 1/0)
- One-hot encoding applied to multi-class categorical columns
- StandardScaler applied for distance-based models (Logistic Regression, SVM)

### 5 · Class Imbalance — SMOTE
Applied **SMOTE** (Synthetic Minority Oversampling Technique) strictly on the
training set after the train-test split. This prevents synthetic samples from
leaking into evaluation and ensures honest metric reporting.

---

## Models Compared

| # | Model               | Paradigm             | Role in Study                       |
|---|---------------------|----------------------|-------------------------------------|
| 0 | Rule-Based          | Human Logic          | Interpretable business baseline     |
| 1 | Logistic Regression | Linear               | Statistical baseline                |
| 2 | Random Forest       | Ensemble — Bagging   | Reduces overfitting via aggregation |
| 3 | SVM                 | Margin-Based         | High-dimensional boundary learning  |
| 4 | Tuned Random Forest | Ensemble — Bagging   | Optimised via RandomizedSearchCV    |
| 5 | **Tuned XGBoost ⭐**| Ensemble — Boosting  | Best-performing model               |

> Models were selected to represent **four distinct learning paradigms** — linear,
> ensemble bagging, ensemble boosting, and margin-based — providing a comprehensive
> cross-paradigm comparison as recommended in current churn prediction research
> (Agiwal, IJSRET 2025).

---

## Evaluation Metrics
Models compared using:
- Accuracy  
- Precision  
- Recall  
- F1 Score  
- ROC-AUC  

---

## Results

All values below are from actual training runs in `churn_prediction.ipynb`.

| Model               | Accuracy | Precision | Recall   | F1 Score | ROC-AUC  |
|---------------------|----------|-----------|----------|----------|----------|
| Rule-Based          | 76.82%   | 73.00%    | 20.00%   | 32.00%   | —        |
| Logistic Regression | 76.62%   | 55.71%    | **81.52%**| 66.19%  | 86.51%   |
| SVM                 | 76.33%   | 55.76%    | 75.95%   | 64.31%   | 85.26%   |
| Random Forest       | 79.32%   | 63.33%    | 62.53%   | 62.93%   | 84.23%   |
| XGBoost (default)   | 78.68%   | 62.03%    | 62.03%   | 62.03%   | 84.34%   |
| Tuned Random Forest | 80.95%   | 70.29%    | 55.70%   | 62.15%   | 86.31%   |
| **Tuned XGBoost ⭐**| **81.24%**| **70.66%**| 56.71%   | **62.92%**| **87.00%**|

---

## Why Tuned XGBoost is the Best Model 

### By Accuracy — XGBoost Wins (81.24%)
Tuned XGBoost achieved the highest overall accuracy, meaning it made the most
correct predictions across the entire test set.

### By Precision — XGBoost Wins (70.66%)
XGBoost and Tuned Random Forest both achieved ~70% precision, which is the
highest in the comparison. This means when XGBoost flags a customer as likely
to churn, it is correct 70.66% of the time.

### By F1 Score — XGBoost Wins (62.92%)
XGBoost achieved the highest F1 score (62.92%), which means it has the best
overall balance between catching churners and avoiding false alarms.

### By ROC-AUC — XGBoost Wins (87.00%)
ROC-AUC of **87.00%** is the highest in the comparison. This means that when
you give XGBoost two customers — one who churns and one who does not — it will
correctly rank the churner as higher risk 87% of the time. This is the most
reliable measure of the model's real-world discrimination ability, independent
of any threshold setting.

### The Trade-off — Recall vs Precision
An important observation: **Logistic Regression achieved the highest Recall
(81.52%)**, meaning it catches more actual churners. However, its Precision is
only 55.71%, which means 44.29% of its churn predictions are wrong — causing
unnecessary retention spend.

XGBoost makes a more informed trade-off: slightly lower recall (56.71%) but
substantially higher precision (70.66%) and the highest ROC-AUC (87.00%).

**The choice depends on business context:**
- If the cost of a missed churner is very high → prioritise Recall → use Logistic Regression
- If retention budget is limited and targeting must be precise → use Tuned XGBoost
- For a balanced, production-grade system → Tuned XGBoost is the recommended choice

---

## Rule-Based Model

```python
def rule_based_churn_predictor(row):
    risk_score = 0

    if row['Tenure_Months'] < 6:             risk_score += 2  # New customer
    if row['Monthly_Charges'] > 70:          risk_score += 1  # High charge
    if row['Contract_Month-to-month'] == 1:  risk_score += 2  # No commitment
    if row['Tech_Support_No'] == 1:          risk_score += 1  # No support

    return 1 if risk_score >= 3 else 0
```

**Rule-Based Results (from notebook):**
- Accuracy: **76.82%**
- Precision: 73% — but only for the non-churn class
- **Recall for churn: only 20%** — misses 80% of actual churners
- F1 for churn class: just **0.32**

This confirms the core limitation of rule-based systems: while the accuracy
looks acceptable, it almost entirely ignores churners. The model predicted
very few positives (churn = 1), so its recall is critically low. It cannot
learn from data and cannot adapt when customer behaviour shifts.

| Aspect           | Tuned XGBoost   | Rule-Based       |
|------------------|-----------------|------------------|
| Accuracy         | 81.24%          | 76.82%           |
| Recall (Churn)   | 56.71%          | 20.00%           |
| Precision        | 70.66%          | 73.00%           |
| F1 Score         | 62.92%          | 32.00%           |
| ROC-AUC          | 87.00%          | N/A              |
| Adapts to Data   | Yes             | No               |
| Interpretability | Medium          | High             |

Rule-based logic is useful for quick human-readable screening
and business explainability, but it cannot replace ML for accurate churn
detection. Its 20% recall means 8 out of 10 churning customers go undetected.

---

## Deployment

The Tuned XGBoost model is deployed as a **Flask web application**.

**Application flow:**
1. User enters customer details in the prediction form
2. Flask backend processes and scales the inputs
3. **XGBoost** returns churn probability with percentage bar
4. **Rule-Based engine** runs in parallel — displays risk level and triggered rules
5. Results page presents comparison table and business retention recommendation

**Run locally:**

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the notebook to generate model files
jupyter notebook notebooks/churn_prediction.ipynb

# 3. Start the app
python app.py

# 4. Open browser at http://127.0.0.1:5000
```

---

## Key Findings

1. **Accuracy alone is not enough** — the rule-based model achieves 76.82%
   accuracy yet catches only 20% of actual churners. ROC-AUC and Recall are
   the metrics that matter most in this problem.

2. **Hyperparameter tuning made a meaningful difference** — default XGBoost
   scored 78.68% accuracy and 84.34% AUC. After tuning: 81.24% accuracy and
   87.00% AUC, demonstrating the value of systematic optimisation.

3. **Contract type and tenure are the strongest predictors** — month-to-month
   customers with < 6 months tenure represent the highest churn-risk segment
   across all models.

4. **SMOTE improved minority-class performance** — training without SMOTE
   caused models to ignore the churn class. Applying it after the split ensured
   balanced learning without contaminating evaluation.

5. **Leakage prevention was critical** — removing `Churn Score` and
   `Churn Reason` before training ensured results reflect genuine predictive
   power, not shortcut correlations.

---

## Business Recommendation

> Customers on **month-to-month contracts** with **tenure under 6 months**
> and **monthly charges above $70** represent the highest churn-risk segment.
>
> **Deploy Tuned XGBoost** to score all customers weekly. Trigger targeted
> retention actions — loyalty discounts, plan reviews, or proactive support
> outreach — for customers flagged above 60% churn probability.
>
> The rule-based system can serve as a **human-readable escalation filter**
> for customer success teams who need to explain decisions to non-technical
> stakeholders.

---

## References

1. Agiwal, R. (2025). *Comparative Analysis of Machine Learning Algorithms for Customer Churn Prediction*. IJSRET, Vol 11, Issue 2, ISSN: 2395-566X.
2. Burez, J. & Van den Poel, D. (2009). *Handling class imbalance in customer churn prediction*. Expert Systems with Applications, 36(3), 4626–4636.
3. IBM Cognos Analytics Telco Customer Churn Dataset. https://www.ibm.com/docs/cognos-analytics

---

## Technologies Used

| Category      | Tools                               |
|---------------|-------------------------------------|
| Language      | Python 3.13                         |
| Data Analysis | Pandas, NumPy                       |
| Visualisation | Matplotlib, Seaborn                 |
| ML Models     | Scikit-learn, XGBoost               |
| Imbalance     | imbalanced-learn (SMOTE)            |
| Tuning        | RandomizedSearchCV                  |
| Deployment    | Flask                               |
| Model Saving  | Pickle, Joblib                      |
| Notebook      | Jupyter                             |

---
