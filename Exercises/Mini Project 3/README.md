# Titanic Dataset Analysis Report

## Initial Data Preparation
- Necessary libraries were imported, followed by loading the data into a dataframe stored in the variable `titanic`.
- Began examining the records of this dataframe and plotted their correlations.

## Data Cleaning
- Removed irrelevant columns such as names and saved the rest in the variable `X`.
- Searched for missing values and filled them using median, mode, and numpy commands.
- Encoded the non-numeric columns using `LabelEncoder`.

## Data Visualization
- Several different charts were drawn using the data, as shown below.
- It is observed that a higher number of men perished.

## Data Splitting for Training and Testing
- After plotting the charts, the data was divided for training and testing, with twenty percent allocated to the test set.

## Model Training and Evaluation
- The first approach was logistic regression, achieving an accuracy of about 81%.
- Then the data was trained using the K-Nearest Neighbors (KNN) method, reaching an accuracy of about 87%. The best `k` was found using a for loop.

## Further Methodologies
- Employed the Naïve Bayes method, yielding an efficiency of about 81%.
- Moved on to Artificial Neural Networks (ANN), achieving an accuracy of about 84%.
- Used Support Vector Machines (SVM) next, also reaching an accuracy of 84%. The optimal parameters were found using Grid Search.

## Decision Tree and Random Forest
- Applied the decision tree method and achieved an accuracy of about 81%.
- Used the random forest method, enhancing the yield to 83%.

## Final Steps with XGBoost
- In the final stage, the XGBoost method was utilized, resulting in a performance similar to the KNN method.

## Confusion Matrix and Test Predictions
- For these two methods, the confusion matrix was drawn.
- The test file was then predicted using these two methods and saved in `test_pred_knn` and `test_pred_xgb`.
- Cross-validation was used in all the above methods to measure the accuracy of learning.
