# **Model Comparison – HR Attrition Prediction**  

## **Dataset Overview**
- **Rows:** 1,470  
- **Target:** 'Attrition' (0 = Stay, 1 = Leave)  
- **Class Imbalance:**  
  - *Stay:* 1233  
  - *Leave:* 237  
- **Final feature count:** 52 engineered features

---

# **1. Baseline Models Evaluated**
Three supervised classification models were trained and tested:

1. **Logistic Regression**
2. **Decision Tree Classifier**
3. **Random Forest Classifier**

All models evaluated using **5-fold cross-validation (F1 Score)** and a held-out test set.

---

# **2. Cross-Validation Results (5-Fold F1 Score)**

| **Model** | **F1 Scores** | **Mean F1** |
|-----------|----------------|--------------|
| **Logistic Regression** | [0.5588, 0.4604, 0.4741, 0.4658, 0.5139] | **0.4946** |
| *Decision Tree* | [0.3093, 0.3846, 0.4082, 0.3214, 0.3673] | 0.3582 |
| *Random Forest* | [0.1852, 0.3051, 0.3390, 0.2500, 0.3051] | 0.2769 |

***Interpretation:***  
- **Logistic Regression** is the most consistently performing model.  
- Tree-based models show higher variance and struggle with the minority class.  
- Because of class imbalance, **F1 Score** is more meaningful than accuracy.

---

# **3. Test Set Performance**

| **Model** | **Accuracy** | **F1 Score** | **Inference Time** |
|-----------|--------------|--------------|---------------------|
| **Logistic Regression** | 0.752 | **0.451** | 0.0019s |
| *Decision Tree* | 0.772 | 0.323 | 0.0012s |
| *Random Forest* | 0.847 | 0.237 | 0.0093s |
| **Tuned Random Forest** | 0.833 | **0.169** | 0.0165s |

***Interpretation:***  
Although Random Forest shows the highest accuracy, it performs poorly on attrition prediction, missing many “leave” cases.  
**Logistic Regression has the highest F1 score**, making it the most reliable model.

---

# **4. Hyperparameter Tuning (GridSearchCV)**

Best Parameters Found
{'max_depth': 10, 'min_samples_split': 5, 'n_estimators': 200}


**Interpretation:**
Even after tuning, the Random Forest model remained biased toward the majority class and did not improve minority-class recall.

# **5. Final Model Recommendation**
**Best Performing Model: Logistic Regression:**

Chosen because it:
- Achieved the highest F1 score
- Generalized best across all folds
- Handled imbalance effectively using class_weight="balanced"
- Had the fastest inference time
