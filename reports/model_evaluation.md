# Model Evaluation - Customer Churn Prediction

## 1. Model Information

- Dataset: IBM Telco Customer Churn
- Train-test split: 80:20
- Random state: 42
- Target variable: Churn (0 = No, 1 = Yes)
- Evaluation focus: Precision, Recall, F1-score, and Accuracy

## 2. Logistic Regression

### Model Configuration
- Algorithm: Logistic Regression
- Feature scaling: StandardScaler
- Max iterations: 2000

### Evaluation Results
- Accuracy: 80.77%
- Precision (Churn): 66%
- Recall (Churn): 57%
- F1-score (Churn): 61%

### Initial Findings
Logistic Regression achieved the highest accuracy among the initial models. However, its recall for the churn class was relatively low, meaning that it failed to identify some customers who actually churned.

## 3. Random Forest

### Model Configuration
- Algorithm: Random Forest
- Number of estimators: 200
- Maximum depth: 10
- Class weight: Balanced

### Evaluation Results
- Accuracy: 76%
- Precision (Churn): 54%
- Recall (Churn): 76%
- F1-score (Churn): 63%

### Initial Findings
Random Forest achieved a higher recall and F1-score for the churn class compared to Logistic Regression. This indicates that it was better at identifying customers who were likely to churn, although it generated more false positive predictions.

## 4. Tuned Random Forest

### Hyperparameter Tuning
- Method: GridSearchCV
- Cross-validation: 3 folds
- Scoring metric: Recall

### Best Parameters
- n_estimators: 300
- max_depth: 5
- min_samples_split: 5
- min_samples_leaf: 2

### Evaluation Results
- Cross-validation Recall: 82.54%
- Test Accuracy: 73%
- Precision (Churn): 50%
- Recall (Churn): 81%
- F1-score (Churn): 62%

### Confusion Matrix

                Predicted No Churn | Predicted Churn |
Actual No Churn |       730        |       305       |
Actual Churn    |       71         |       303       |

### Findings
The tuned Random Forest achieved the highest recall for the churn class, successfully identifying 303 out of 374 actual churn customers.

However, it also generated 305 false positive predictions. This means some customers who were not going to churn would potentially receive unnecessary retention offers.

## 5. Model Comparison

            Logistic Regression | Random Forest | Tuned Random Forest |
Accuracy    |       80.77%      |      76%      |         73%         |
Precision   |       66%         |      54%      |         50%         |
Recall      |       57%         |      76%      |         81%         |
F1-score    |       61%         |      63%      |         62%         |

## 6. Overall Conclusion

The tuned Random Forest model achieved the highest recall (81%), making it a promising candidate for customer churn detection.
Although its accuracy and precision were lower than Logistic Regression, it identified more customers who actually churned.
For a customer retention strategy, identifying potential churn customers is important because the company can take preventive actions before customers leave.
However, the final model selection should also consider the cost of false positives and false negatives.