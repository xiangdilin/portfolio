# Exploring and Predicting US Health Insurance Premiums

A course project (UCLA PIC 16B) that explores which factors drive health insurance charges in the US and compares machine learning models for predicting premiums.

**You can find the project code (Jupyter notebook) and the project writeup PDF in this repo through either the navigation sidebar or the links at the end of this README.**

## Overview

Health insurance premiums depend on many factors, including age, BMI, smoking status, medical history, and coverage level. This project explores a Kaggle insurance dataset to understand how these factors relate to individual charges, and builds regression models to predict them.

Using a sampled subset of 10,000 records (8,000 train / 2,000 test), we performed exploratory visualization, feature selection (Random Forest importance, Lasso, RFE), and modeling with k-NN, Linear Regression, SVR, Neural Networks, and Clustered Linear Regression. We also validated our findings against real-world CMS Medicare spending data and experimented with PCA and multilayer network community detection.

## Project Goals

- **Explore and visualize** correlations between factors that could affect health insurance premiums.
- **Find the best model** to predict insurance charges for individuals based on the most important features.
- **Check how realistic the dataset is** by comparing our findings with real-world national health expenditure data.

## Methods

1. **Data Preprocessing**
   - Replaced missing medical history entries with `"None"` (no history is informative in itself).
   - One-hot encoded 8 categorical features (30 features in total) and standardized age, BMI, and number of children.
   - Sampled 10,000 records from the 1M-row dataset and split into 8,000 train / 2,000 test.

2. **Exploratory Analysis & Visualization**
   - Boxplots, scatter plots, and regression lines of charges against categorical and numerical features.
   - Supplementary analysis of the **CMS National Health Expenditure** data using interactive choropleth maps of per-enrollee spending by state.

3. **Feature Selection**
   - **Random Forest** feature importance for an initial ranking.
   - **Lasso** coefficients to choose the number of features (top 21 of 30).
   - **Recursive Feature Elimination (RFE)** to confirm accuracy plateaus at around 20 features.

4. **Modeling**
   - **k-NN** (grid search with 5-fold CV over neighbors, weights, and distance metric).
   - **Linear Regression**.
   - **Support Vector Regression** with RBF, polynomial, and sigmoid kernels (randomized search with CV).
   - **Neural Network** (TensorFlow/Keras; ReLU hidden layers, Adam optimizer, MSE loss).
   - **Clustered Linear Regression (CLR)** with the number of clusters chosen by average silhouette score.

5. **Extensions**
   - **PCA** dimension reduction as an alternative to Lasso-based selection.
   - **Network analysis:** implemented the **WSSNMTF** multilayer community detection algorithm from the literature (no public code available) on a 2-layer patient similarity network, evaluated with modularity.

## Key Findings

- **Smoking and medical history matter most:** Smokers have significantly higher charges, and individuals with a heart disease history (personal or family) have the highest charges, followed by diabetes and high blood pressure. Charges also rise with BMI.
- **Region and gender had little effect in the dataset:** Charges were relatively consistent across regions, with males slightly higher than females.
- **The dataset is synthetic and has limits:** Real CMS data shows clear geographic differences (southern and coastal states have higher per-enrollee costs), contradicting the lack of a regional effect in the primary dataset.
- **Model performance:** Linear-type models performed very well, and Clustered Linear Regression was the best overall.
- **PCA hurt performance:** Reducing to 10 components (65% explained variance) performed much worse than Lasso-based feature selection.
- **Weak network communities:** Low modularity scores across 2, 3, and 4 communities indicate weak community structure with our chosen layers and features.

## Model Comparison

Charges were scaled by 1000, so MSE is reported in those units.

| Model | MSE | R² |
|---|---|---|
| k-NN (Manhattan, k=10, distance-weighted) | 2.40 | 0.87 |
| Linear Regression | 0.13 | 0.99 |
| SVR (polynomial kernel, degree 3, C=10) | 0.13 | 0.99 |
| SVR (RBF kernel) | 0.14 | 0.99 |
| SVR (sigmoid kernel) | 0.22 | 0.98 |
| Neural Network (2 hidden layers) | 0.14 | n/a |
| Linear Regression + PCA (10 components) | 4.87 | 0.74 |
| **Clustered Linear Regression (2 clusters)** | **0.089 / 0.083** | **0.995 / 0.996** |

> CLR values are reported per cluster (Cluster 0 / Cluster 1). Centroid analysis suggests Cluster 0 is younger with more smokers and more Premium coverage, while Cluster 1 is older with more children and more Standard coverage.

## My Contributions

- Visualized relationships between features and charges (charges vs. BMI by gender and smoking status; charges vs. age by medical history)
- Performed the supplementary analysis of CMS National Health Expenditure data, including interactive choropleth maps
- Prepared the data for training (feature encoding, standardization, train/test split)
- Performed feature selection with Lasso and RFE and analyzed the effect of the number of features on accuracy
- Implemented the WSSNMTF multilayer network community detection algorithm from the paper and applied it to the insurance data

## Technologies & Methods

**Programming:** Python

**Machine Learning:** k-Nearest Neighbors, Linear Regression, Support Vector Regression, Neural Networks (TensorFlow/Keras), Clustered Linear Regression, Random Forest

**Feature Selection & Dimensionality Reduction:** Lasso, Recursive Feature Elimination (RFE), PCA

**Model Evaluation:** MSE, R², Grid Search, Randomized Search, K-Fold Cross-Validation, Silhouette Score

**Network Analysis:** Multilayer Networks, WSSNMTF Community Detection, Modularity

**Data:**
- [Insurance Dataset for Predicting Health Insurance Premiums in the US (Kaggle)](https://www.kaggle.com/datasets/sridharstreaks/insurance-data-for-machine-learning/data)
- [National Health Expenditure Data by State of Residence (CMS)](https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data/state-residence)

## Results

Our experiments showed that insurance charges in this dataset can be predicted with very high accuracy from a reduced set of 21 features. Most models reached R² of about 0.99, and Clustered Linear Regression slightly outperformed plain Linear Regression, with a clear two-cluster structure separating younger, higher-smoking, Premium-coverage individuals from older, family-oriented, Standard-coverage individuals.

At the same time, the analysis highlighted important limitations. Because the primary dataset is synthetic, features such as region and BMI do not behave as they do in the real world, which we confirmed using real CMS Medicare spending data. We also trained on a small subset because of limited computing power. Future directions include incorporating data from other reliable sources, trying alternative dimension reduction (e.g., kernel PCA), and using more advanced community detection methods such as Louvain or Leiden.

## Contributors

Anshika Khandelwal, Dakota Lin, Sarah Ward.

> Listed in alphabetical order by last name.

## Code

[💻 View the Jupyter Notebook](./predicting_premiums.ipynb)

> The notebook contains the full pipeline: data preprocessing, visualization, feature selection, model training and evaluation, PCA, and network community detection.

## Report

[📄 Download the Full Report (PDF)](./Project_Report.pdf)

> For the best viewing experience, please download the PDF.

## License

This project is licensed under the MIT License.
