# Modeling Expected Healthcare Costs

# Problem Statement
Thiis project utilizes the Medical Expenditure Panel Survey (MEPS) to build machine learning models that estimates an individual's suggested health insurance premium on key demographics and characteristics including, but not limited to:
* Age
* Gender
* Employment Status
* Poverty  

The model aims to predict health care expeditures, which is used to determine an appropriate insurance premium.

# Dataset
Medical Expenditure Panel Survey:  
[MEPS HC-243: 2022 Full Year Consolidated Data File](https://meps.ahrq.gov/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-243)  

# Variables
* Total Expenditures in 2022:
    * TOTEXP22
* Demographics:
    * Age, Gender, Region, Employment, Poverty Status, Insurance Coverage
* New Columns:
    * Predicted Cost, Suggested Premium

# Tools
* Python:
    * Pandas, Numpy, Scikit-Learn
* Machine Learning:
    * Linear Regression, Random Forest Regressor

# Key Insights
1. Healthcare Costs are Highly Skewed
    - Medical expenditure data is heavily right-skewed. Only a small percentage of individuals account large shares of the total costs. This prediction suggests that log-scaling can improve the model performance.
2. Age is a Strong Predictor
    - Healthcare expenditures increase significantly with age. As shown in the data visualizations, older individuals consistently show higher predicted costs, reflecting greater healthcare utilization and chronic conditions.
3. Random Forest Model Outperformed Linear Regression
    - The Random Forest Model ended up capturing the nonlinear relationships and interactions between variables better than the linear regression, resulting in:
        - Lower r^2 value
        - Better handling of skewed distribution
        - Improved robustness to outliers

# Future Improvements
1. Utilize Additional Predictors and Variables
    - Incorporate chronic condition indicators
    - Add interaction terms
2. Advanced Modeling
    - Use Gradient Bosting Models
    - Create Neural Networks for nonlinear pattern recognition
3. Real-World Considerations
    - Build interactive dashboard using Streamlit
    - Enable scenario analysis for underwriting simulations
    - Automate program for new MEPS data

# Author
**Kevin Chi**  
Incoming Freshman | University of Michigan - Ann Arbor  
Dual Major: Actuarial Mathematics and Data Science  
kevinchi164@gmail.com