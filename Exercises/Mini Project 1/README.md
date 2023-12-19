# Data Analysis Report on Google Apps Dataset

## Initial Data Loading and Observation
- Imported essential libraries: `matplotlib`, `seaborn`, `pandas`, `numpy`.
- Loaded the CSV file into a variable `google_app`.
- Examined the first 7 rows of the dataset.

## Dataframe Overview
- Used `info()` function to gather general information.
- Identified missing values in the 'Rating' column.

## Handling Missing Values
- Stored rows with missing values in `Missing_value`.
- Observed the first 20 rows of this subset.

## Rating Analysis
- Calculated the proportion of records with 'Rating' >= 4.5 (around 25% of total records).
- Categorized records using `crosstab` by 'Rating' and 'Type', revealing a prevalence of 'Free' type in higher ratings.

## Data Sorting and Review Analysis
- Sorted records by 'Rating' and saved in `rating_sorted`.
- Converted 'Reviews' column to numeric for comparison.
- Identified the highest number of reviews in the dataset.
- Plotted the distribution of apps based on 'Rating'.

## Distribution Analysis by App Type
- Separated the distribution plot by 'Type' of apps.
- Isolated records with 'Rating' > 3.5 in `Rate`.
- Created scatter plots of reviews against ratings, showing most reviews in the 4.1 to 4.3 rating range.
- Further separated plots by 'Type', highlighting the dominance of 'Free' apps.

## Additional Visualizations
- Created bar charts for the previous plots.
- Generated a count plot.
- Created a plot based on 'Rating' using `relplot`.
- Plotted reviews by app type for `Missing_value` data, reaffirming higher views for 'Free' apps.
- Plotted views of `Rate` data by 'Type', separating data based on 'Rating', which showed most views for apps rated between 4.0 and 4.3.

## Data Correction
- Corrected a problematic record in the original dataset.