# Mini ML Project Summary – HR Attrition Prediction  

## Project Goal  
Build a predictive model to identify employees at risk of leaving the company, enabling HR teams to improve retention, reduce hiring costs, and proactively support at-risk talent.

---

## Dataset Overview  
- **Total rows:** 1,470  
- **Attrition rate:** 16% (237/1470)  
- **Target:** `Attrition` (0 = Stay, 1 = Leave)  
- **Features after preprocessing:** 52 numeric & encoded columns  
- **Processed dataset used:** `data/processed/features.csv`  

---

## ML Pipeline Steps  
1. Loaded processed dataset from Day 2  
2. Split into train/test (80/20, stratified)  
3. Trained Logistic Regression with class balancing  
4. Generated evaluation metrics (precision, recall, F1, ROC AUC)  
5. Created all evaluation plots  
6. Interpreted feature coefficients  
7. Saved final model as `final_attrition_model.pkl`  

---

## Best Model: Logistic Regression  

| Metric | Score |
|--------|-------|
| **Accuracy** | 0.75 |
| **F1 Score (Attrition)** | 0.45 |
| **Recall (Attrition)** | 0.64 |
| **Precision (Attrition)** | 0.35 |
| **ROC AUC** | 0.80 |

### Why Logistic Regression?  
- Highest F1 score across all tested models  
- Strong recall for minority class  
- Excellent ROC AUC  
- Fast, stable, and interpretable  
- Coefficients clearly show what drives attrition  

---

## Evaluation Highlights  

### **Confusion Matrix**

| Pred No | Pred Yes |
|--------|-------|
| Actual No | 191 | 56 |
| Actual Yes | 17 | 30 |

- Catches majority of actual leavers (good recall)  
- Accepts some false positives (acceptable in HR risk systems)  

### **ROC AUC = 0.80**  
Strong separability between leavers and non-leavers.

### **PR Curve**
Shows realistic performance under class imbalance.

---

## Feature Interpretation  

### **Top Predictors of Higher Attrition**
- OverTime_Yes  
- BusinessTravel_Travel_Frequently  
- JobRole_Sales Representative  
- JobRole_Laboratory Technician  
- MaritalStatus_Single  

### **Top Predictors of Retention**
- High JobSatisfaction  
- High EnvironmentSatisfaction  
- Long tenure & experience  
- Strong relationship with manager  
- OverTime_No  

---

## Business Recommendations  
- **Monitor overtime patterns** and adjust workload  
- Improve **satisfaction metrics** (job & environment)  
- Focus retention programs on **high-churn job roles**  
- Provide flexibility for **long-distance commuters**  
- Strengthen **manager–employee relationships**  
