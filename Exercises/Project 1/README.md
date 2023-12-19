# Data Analysis and Preprocessing Report

## Data Examination
- The dataset was examined to understand its structure and identify missing values.
- The count of missing values was found to be significantly high in some columns.
- Columns with an excessive number of missing values were removed, resulting in the dataset taking on a new form.

## Data Transformation
- Non-numeric columns were converted to numeric using label encoding.
- Missing values were filled with the column means.

## Data Scaling and Visualization
- Data were scaled using the standard scaler.
- A distribution chart was plotted based on the date, revealing that approximately two hundred encoded vaccines were most frequently administered on a given day.
- Additionally, the distribution of vaccine types was charted.
- This chart indicates that vaccine type 28 had the highest count across all vaccines.
- A correlation chart of the data was also drawn.

## Correlation Observations
- The correlation chart shows that dependencies to a single digit are very low.

## Model Training and Evaluation
- Initial training was performed using linear regression, which yielded a very low return.
- Polynomial regression was then utilized, resulting in higher but still low performance.
- All methods were evaluated using the R-squared metric.

## Challenges and Further Methods
- The Support Vector Regression (SVR) method was applied, which led to overfitting and did not yield a good response.
- Subsequently, the decision tree method was used, resulting in a response close to one, indicating it as a suitable method.
- Comparable results were obtained for both random forest and XGBoost methods, but XGBoost provided the highest figures among them.
