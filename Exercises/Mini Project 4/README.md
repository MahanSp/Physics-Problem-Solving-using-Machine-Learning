# Market Data Analysis Report

## Data Preparation
- Necessary libraries were imported.
- Data was loaded into a variable named `Market` and was subsequently examined. The dataset contained no missing values.

## Visualization and Model Training
- The K Means clustering method was initially applied for model training. Charts for various values of K were plotted to identify the optimal number of clusters.

## Determining the Optimal Number of Clusters
- The analysis of the elbow plot revealed that the optimal number of clusters (K) is 5. A clustering chart was then created using K Means with K set to 5.

## DBSCAN Clustering
- The DBSCAN clustering method was also applied, and the resulting clusters were visualized in a chart.

## Method Comparison and Final Insights
- A comparison of the K Means and DBSCAN methods indicated that K Means provides more appropriate clustering for this particular dataset.
