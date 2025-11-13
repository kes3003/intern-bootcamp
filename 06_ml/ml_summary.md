## Baseline Model Summary – Logistic Regression

### Goal
The goal is to predict employee attrition based on demographic, job satisfaction, and workload-related features. This helps HR identify potential leavers early and implement proactive retention strategies.

### Dataset Overview
- **Total records:** 1,470 employees   
- **Target variable:** Attrition (1 = Yes, 0 = No)      
- **Attrition rate:** ~16% (237 of 1,470 employees)

| Split | Records | Columns |
|--------|----------|----------|
| Training set | 1,176 | 14 |
| Testing set | 294 | 14 |

---

### Model Used
**Algorithm:** Logistic Regression (Baseline)  
**Data split:** 80% training / 20% testing  
**Scaling:** StandardScaler applied to numeric features  
**Class balancing:** Handled using `class_weight='balanced'`

---

### Model Performance
| Metric | Score |
|---------|--------|
| **Accuracy** | 0.76 |
| **F1 Score (Attrition = 1)** | 0.51 |
| **Recall (Attrition = 1)** | 0.79 |
| **Precision (Attrition = 1)** | 0.38 |

**Interpretation:**  
The model correctly predicts 76% of overall cases.  
It captures 79% of actual leavers (high recall) but has moderate precision (some false positives).  

---

### Top Predictors of Attrition

| Driver | Coefficient | Impact |
|---------|--------------|--------|
| **OverTime_Yes** | +0.64 | Strongest predictor of leaving; employees working overtime are much more likely to leave. |
| **MaritalStatus_Single** | +0.49 | Single employees show higher attrition tendency. |
| **DistanceFromHome** | +0.24 | Longer commute slightly increases likelihood of leaving. |
| **MonthlyIncome** | −0.19 | Higher income lowers attrition risk. |
| **YearsAtCompany** | −0.16 | Longer tenure reduces attrition. |
| **JobSatisfaction** | −0.35 | Employees satisfied with their jobs are less likely to leave. |
| **EnvironmentSatisfaction** | −0.38 | Positive work environment promotes retention. |
| **WorkLifeBalance** | −0.23 | Balanced workload reduces risk of attrition. |

---

### Confusion Matrix Interpretation

[[186 61]
[ 10 37]]

- **True Negatives (186):** Stayed and correctly predicted to stay  
- **False Positives (61):** Predicted to leave but actually stayed  
- **False Negatives (10):** Predicted to stay but actually left  
- **True Positives (37):** Correctly predicted leavers  

The model identifies most employees who left (recall = 0.79) but flags some false leavers (precision = 0.38).

---

### Business Insights
- Overtime, single marital status, and long commutes are major attrition risk factors.  
- Job satisfaction, environment satisfaction, and fair compensation are strong retention levers.  
- HR should monitor employees working excessive overtime or expressing low satisfaction and address their concerns proactively.


