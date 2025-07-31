Customer Churn Prediction using Machine Learning
Project Overview
This project focuses on building a machine learning model to predict customer churn for a telecommunications company. Customer churn, the act of customers discontinuing their service, is a critical business problem as retaining existing customers is often more cost-effective than acquiring new ones. This analysis aims to identify customers at risk of churning and understand the key factors driving churn, providing actionable insights for retention strategies.

Skills and Technologies Demonstrated
Data Analysis & Manipulation: Pandas, NumPy

Data Visualization: Matplotlib, Seaborn

Machine Learning: Scikit-learn (Logistic Regression, Decision Tree, Random Forest Classifier)

Preprocessing: Handling missing values, Label Encoding, One-Hot Encoding, Feature Scaling (StandardScaler)

Model Evaluation: Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC AUC Curve

Feature Importance Analysis

Jupyter Notebook for interactive development and documentation

Git & GitHub for version control and project hosting

Dataset
The dataset used for this project is the IBM Telco Customer Churn dataset, publicly available on Kaggle. It contains information about a telecommunications company's customers, including various demographic, service, and account information, and whether they churned or not.

Key Findings & Model Performance
After comprehensive Exploratory Data Analysis (EDA) and robust preprocessing, a Random Forest Classifier was trained to predict churn.

ROC AUC Score: 0.8250 - This indicates a strong ability of the model to distinguish between churning and non-churning customers.

Accuracy: 0.7850

Precision (for Churn=1): 0.6272

Recall (for Churn=1): 0.4679

F1-Score (for Churn=1): 0.5360

Confusion Matrix:

[[931 104]
 [199 175]]

True Positives (TP): 175 (Correctly predicted churn)

False Negatives (FN): 199 (Missed actual churners)

Key Churn Drivers Identified (Feature Importance):
Through feature importance analysis, the following factors were found to be most influential in predicting customer churn:

Tenure: Customers with shorter tenure are significantly more likely to churn.

Contract Type: Month-to-month contracts are strongly associated with higher churn rates.

Internet Service: Customers with Fiber Optic internet service show higher churn.

Online Security: Lack of online security services is a strong indicator of churn.

Monthly Charges: Higher monthly charges show a positive correlation with churn.

These insights can help the telecommunications company focus its retention efforts on high-risk customer segments.

How to Run the Project
Clone the Repository:

git clone [YOUR_GITHUB_REPO_LINK_HERE]
cd Customer-Churn-Prediction-ML

Download Dataset:

Download WA_Fn-UseC_-Telco-Customer-Churn.csv from Kaggle and place it in the project directory.

Install Dependencies:

pip install pandas numpy scikit-learn matplotlib seaborn

Run Jupyter Notebook:

jupyter notebook Customer_Churn_Prediction.ipynb

Follow the steps in the notebook to execute the code and reproduce the analysis.

Future Enhancements (Optional)
Experiment with advanced imbalance handling techniques (e.g., SMOTE, ADASYN).

Perform hyperparameter tuning for the Random Forest model using GridSearchCV or RandomizedSearchCV.

Explore other classification algorithms like XGBoost or LightGBM for comparison.

Build a simple web application (e.g., using Flask/Streamlit) to deploy the trained model for interactive predictions.