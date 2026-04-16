# Car Price Prediction using Regression Analysis in R

## 📌 Project Overview

This project focuses on building regression models to predict car prices using data collected from:
- Online car advertisements
- Public data from Statistiska Centralbyrån (SCB) via their API

The main goal is to apply regression analysis techniques to both predict car prices and draw conclusions about the broader population.


## 🎯 Objectives

At the start of the project, three key questions were defined:
1. What factors have the greatest impact on car prices?
2. How well do prediction intervals align with actual prices?
3. Is there a price difference between cars sold by private sellers and companies?



## 🛠️ Methodology

### Data Collection
- Scraped data from online car listings
- Retrieved complementary socioeconomic data from SCB via API

### Data Processing
- Cleaning and preprocessing of structured and semi-structured data
- Feature engineering to construct meaningful predictors

### Modeling Approach

All modeling was conducted using R programming.

### The workflow includes:
- Implementing multiple regression models
- Iterative model refinement through:
- Model selection
- Diagnostics
- Transformation and adjustments

### Feature Selection
- Best Subset Selection was used to identify the most relevant variables

### Model Evaluation
- Cross-validation was used to evaluate model performance
- RMSE (Root Mean Squared Error) served as the primary evaluation metric
- Top 3 models were compared based on cross-validation results
- The best model was selected and evaluated on test data



## 📊 Key Results

### Important Predictors

#### The most significant variables influencing car prices were:
- Car age
- Horsepower
- Mileage

#### Seller Type Impact
- Cars sold by private individuals tend to have lower prices compared to those sold by companies

#### Model Performance
- The final model achieved the lowest RMSE on validation and test data
- Prediction intervals were evaluated against actual prices to assess reliability

#### Statistical Inference
- The final model was also analyzed from a statistical perspective to:
- Interpret coefficients
- Assess significance
- Draw conclusions about the population



## 📈 Conclusion

This project demonstrates how regression analysis can be used to:
- Predict car prices with reasonable accuracy
- Identify key factors influencing price
- Provide insights into market behavior, such as differences between seller types

The iterative modeling approach, combined with robust evaluation techniques, resulted in an interpretable predictive model.


## 🧰 Technologies Used
- R-programming
- Regression modeling techniques
- Cross-validation
- API data collection (SCB)
