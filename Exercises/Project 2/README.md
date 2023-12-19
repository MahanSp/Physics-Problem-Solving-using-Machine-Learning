# Data Analysis and Model Training Report

## Data Preparation
- Necessary libraries were imported and the CSV file was saved into a dataframe.
- Checked for missing values and found that the data was complete and without missing entries.

## Data Encoding and Cleaning
- Non-numeric columns were encoded, and columns such as row number and ID, which do not influence the training process, were removed.
- A correlation chart for the data was created, indicating very low interdependence among the data points.

## Data Visualization
- Several charts were plotted using seaborn, which showed that a higher number of females have exited.
- It was also observed that customers who made more purchases and remained active members have stayed, leading to a logical conclusion.

## Data Scaling
- Proceeded to scale the data using the standard scaler.

## Model Training and Optimization
- Different training methods were applied, with the results being observable as follows:
- The above chart pertains to the optimization of the KNN method, where the best K was found to be 29.
- It can be seen that the highest accuracy mostly belongs to the XGBoost method.
- k-fold cross-validation was used in all methods.

## Further Steps and Web Application Development
- Training was also performed with pycaret, saved in the `Project2-Colab.ipynb` file.
- According to calculations, the best method is GBC (Gradient Boosting Classifier), and the top three methods were combined in this file to perform the calculations.
- Additionally, a web application was created using the streamlit library, which is observable in the files.
