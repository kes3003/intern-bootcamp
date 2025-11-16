# Model Evaluation & Interpretation  


## 1. Overview

The Logistic Regression model trained on engineered features was evaluated on the held-out 20% test set.  

Attrition is **16%** in this dataset (237/1470), meaning the model must handle a **highly imbalanced** classification problem.

---

## 2. Confusion Matrix

### Interpretation:
- **191 true negatives:** model correctly identifies most employees who stay  
- **30 true positives:** correctly identifies employees likely to leave  
- **17 false negatives:** misses some at-risk employees  
- **56 false positives:** flags some employees as at-risk who do not leave  

Overall, the model balances both classes reasonably well given the imbalance.

---

## 3. Classification Metrics

| Metric | Value |
|--------|--------|
| **Accuracy** | 0.75 |
| **F1 Score (Attrition)** | 0.45 |
| **Precision (Attrition)** | 0.35 |
| **Recall (Attrition)** | 0.64 |
| **ROC AUC** | **0.80** |

### Interpretation:
- **Recall = 0.64** - the model correctly captures most employees who actually leave  
- **Precision = 0.35** - some false alarms, which is expected in imbalance  
- **F1 = 0.45** - strongest score among all models tested  
- **ROC AUC = 0.80** - model has good ability to separate leavers vs stayers  

This confirms that **Logistic Regression was the best overall model**.

---

## 4. ROC Curve Interpretation

- The ROC curve rises well above the diagonal line.  
- AUC of **0.80** indicates strong discriminative capability.  
- The model is significantly better than random guessing.

This shows that the model **effectively ranks employees by attrition risk**, even if thresholds need calibration.

---

## 5. Precision–Recall Curve

- Precision drops as recall increases which is typical for imbalanced datasets.  
- PR curve is more informative than ROC because attrition is only 16%.  
- The curve shows the model makes a useful tradeoff between catching at-risk employees (recall) and limiting false positives (precision).

---

## 6. Feature Importance (Logistic Regression Coefficients)

### Top Factors **increasing attrition** (positive coefficients):
- JobRole_Laboratory Technician
- JobRole_Sales Representative
- BusinessTravel_Travel_Frequently
- OverTime_Yes
- EducationField_Human Resources

### Top Factors **reducing attrition** (negative coefficients):
- JobRole_Research Director
- BusinessTravel_Non-Travel
- OverTime_No
- TotalWorkingYears
- EnvironmentSatisfaction
- JobSatisfaction
- YearsWithCurrManager

### Interpretation:
- Lack of satisfaction (job/environment) strongly correlates with attrition risk.  
- More stable employees (more experience, more years with manager) tend to stay.  
- Frequent business travel and overtime increase burnout risk, leading to attrition.  
- Some Job Roles (e.g., Sales, Lab Technicians) have higher churn.

---

## Final Conclusion

**Logistic Regression remains the most reliable and balanced model** for predicting employee attrition, offering:
- strong recall,  
- good discrimination (AUC = 0.80),  
- the best F1 score, and  
- clear, actionable feature insights for HR.

    