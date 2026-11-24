# Business Insights & Recommendations

## 1. Key Business Insights

### Contract Type and Customer Churn
Month-to-month customers have the highest churn rate at 42.71%, compared to 11.27% for one-year contracts and 2.83% for two-year contracts.

This indicates that customers with shorter contract commitments are more likely to leave the service.

### Customer Tenure and Churn
Customers with a tenure of 0–12 months have the highest churn rate at 47.44%. The churn rate decreases as customer tenure increases.

This suggests that the first year of the customer lifecycle is a critical period for retention.

### Machine Learning Results
The tuned Random Forest model achieved 81% recall for the churn class.

The model successfully identified 303 out of 374 actual churn customers, although 305 non-churn customers were incorrectly classified as potential churn customers.

## 2. Business Recommendations

1. **Contract Retention Strategy:** Offer incentives to encourage month-to-month customers to consider longer-term contracts.

2. **Customer Onboarding:** Develop onboarding and follow-up programs during the first 12 months to improve customer engagement.

3. **Predictive Retention:** Use the churn prediction model to identify customers who may need additional attention.

4. **Retention Campaign Optimization:** Evaluate the effectiveness and cost of retention campaigns, especially for customers incorrectly predicted as churn.

## 3. Overall Conclusion

Customer churn is strongly associated with contract type and customer tenure in this dataset. Customers with month-to-month contracts and shorter tenure represent important segments for retention efforts.

The machine learning model can support customer retention strategies by identifying potential churn customers. However, business decisions should also consider the costs of retention campaigns and prediction errors.