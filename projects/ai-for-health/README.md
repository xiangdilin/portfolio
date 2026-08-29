# Machine Learning Analysis of Lyme Disease Data

A research project exploring machine learning and mathematical methods to identify patterns, classify patient groups, and detect atypical symptom profiles in Lyme disease survey data.

## Overview

Lyme disease can present with a wide range of symptoms and disease manifestations, making it challenging to identify meaningful patterns across patients. In this project, we analyzed survey data collected from individuals affected by Lyme disease and applied a variety of machine learning and mathematical techniques to uncover latent patterns and distinguish different patient groups.

The study focused on identifying symptom patterns associated with neurological manifestations, differentiating chronic and early Lyme disease cases, predicting the timing of diagnosis relative to symptom onset, and identifying patients with uncommon or extreme symptom profiles.

## Research Objectives

- Discover latent patterns in Lyme disease symptoms
- Identify features associated with neurological manifestations
- Classify patients into chronic vs. early Lyme disease groups
- Predict whether diagnosis occurred before or after one year from symptom onset
- Detect patients with unusual or extreme symptom profiles
- Develop interpretable low-dimensional representations of patient data
- Explore fairness in dimensionality reduction across different patient subgroups

## Methods

We explored several machine learning and mathematical approaches:

### Nonnegative Matrix Factorization

- **NMF** for uncovering latent symptom patterns
- **Neural NMF** for nonlinear representation learning
- **Semi-Supervised NMF** for analyzing anomalous patient groups
- **Fair NMF** for obtaining lower-dimensional representations across different subgroups

### Classification

We applied supervised learning methods including:

- **Logistic Regression**
- **Support Vector Machines (SVM)**

These models were used to distinguish chronic vs. early Lyme disease cases and predict the timing of diagnosis relative to symptom onset.

### Anomaly Detection

Anomaly detection was used to identify patients with uncommon symptom profiles. These cases were subsequently analyzed using semi-supervised NMF to investigate whether meaningful patterns could be identified within atypical patient groups.

### Patient Network Analysis

We constructed a patient similarity network based on symptom and feature similarity and applied a **multiplex community detection algorithm** to identify interpretable patient communities.

## Key Findings

NMF revealed underlying patterns in the survey data that provided insight into Lyme disease symptoms, including patterns associated with neurological manifestations.

Classification models achieved strong performance in distinguishing **chronic vs. early Lyme disease** and predicting whether diagnosis occurred before or after one year from symptom onset.

Anomaly detection identified patients with uncommon symptom profiles, which were further analyzed using semi-supervised NMF to uncover additional structure within these atypical cases.

The study also explored **Fair NMF**, demonstrating how incorporating subgroup considerations into matrix factorization can produce lower-dimensional representations with improved fairness across different groups.

## My Contributions

- Explored and reproduced machine learning algorithms from the research literature for Lyme disease data analysis
- Implemented and evaluated **NMF-based methods** for latent pattern discovery
- Developed two helper functions based on **feature similarity** to improve upon Neural NMF
- Applied **semi-supervised NMF** to analyze anomalous patient groups
- Constructed and analyzed a **patient similarity network**
- Implemented a **multiplex community detection algorithm** to identify interpretable patient communities

## Technologies & Methods

**Programming:** Python

**Machine Learning:** NMF, Neural NMF, Semi-Supervised Learning, Fair NMF, Logistic Regression, SVM, Anomaly Detection

**Network Analysis:** Patient Similarity Networks, Community Detection, Multiplex Networks

**Mathematical Methods:** Matrix Factorization, Dimensionality Reduction, Feature Similarity

**Data:** Lyme Disease Survey Data

## Results

The combination of matrix factorization, classification, anomaly detection, and network analysis provided complementary perspectives on the Lyme disease survey data. The results demonstrate how mathematical and machine learning techniques can be combined to uncover latent structure, identify atypical cases, and produce interpretable representations of complex health-related data.

## Report

[View the full research report](./REU_2023_AI_for_Health.pdf)
