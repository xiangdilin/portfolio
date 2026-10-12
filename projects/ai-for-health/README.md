# Machine Learning Analysis of Lyme Disease Data

A research project exploring machine learning and mathematical methods to identify patterns, classify patient groups, and detect atypical symptom profiles in Lyme disease survey data.

**You can find the project writeup PDF in this repo through either the navigation sidebar or a link at the end of this README.**

## Overview

Lyme disease can present with a wide range of symptoms and disease manifestations, making it challenging to identify meaningful patterns across patients. This project explores Lyme disease patient data using mathematical and machine learning techniques to uncover symptom patterns, predict disease characteristics, detect unusual patient profiles, and develop fairer low-dimensional representations.

Using survey data from MyLymeData, we applied Non-Negative Matrix Factorization (NMF), classification methods, anomaly detection, network analysis, and fair dimensionality reduction. The project combines unsupervised and supervised learning to investigate patterns associated with disease status, neurological manifestations, and unusual symptom profiles.

## Research Objectives

- Identify underlying **symptom patterns** among Lyme disease patients using unsupervised NMF.
- Predict **neurological manifestations** and distinguish between different patient groups using supervised learning.
- Classify patients based on characteristics such as **chronic vs. early Lyme disease** and time to diagnosis.
- Detect patients with **unusual or extreme symptom profiles** using anomaly detection.
- Explore relationships among patients through **network-based community detection**.
- Develop a **fair dimensionality reduction** method that produces more equitable low-dimensional representations across patient subgroups.

## Methods

1. **Symptom Pattern Discovery**
   - Applied unsupervised **Non-Negative Matrix Factorization (NMF)** to extract underlying symptom patterns and reduce the dimensionality of the patient data.

2. **Classification**
   - Applied **Logistic Regression, SVM, and Semi-Supervised NMF (SSNMF)** to classify Lyme disease patients.
   - Studied distinctions between chronic and early Lyme patients and predicted neurological manifestations.

3. **Anomaly Detection**
   - Used **Isolation Forest (iForest)** and **Local Outlier Factor (LOF)** to identify patients with unusual symptom profiles.
   - Applied supervised NMF to further investigate patterns associated with detected anomalies.

4. **Network Analysis**
   - Constructed a patient network and applied **multiplex community detection** to identify groups of patients with shared characteristics.

5. **Neural NMF**
   - Developed two feature-similarity-based helper functions to improve the performance of **Neural NMF**.

6. **Fair Dimensionality Reduction**
   - Proposed **Fair NMF**, an NMF-based approach designed to reduce disparities between subgroups in low-dimensional representations.
   - Explored rescaling, a weighted-average dictionary matrix, and an early-stopping strategy based on subgroup loss convergence.

## Key Findings

- **Symptom Patterns:** NMF revealed underlying patterns in Lyme disease symptoms and identified patterns associated with neurological manifestations.
- **Classification:** Logistic Regression, SVM, and SSNMF successfully differentiated patient groups, including chronic vs. early Lyme patients and patients based on time to diagnosis.
- **Anomaly Detection:** Isolation Forest and LOF identified patients with unusual symptom profiles, which were further analyzed using supervised NMF.
- **Patient Networks:** Multiplex community detection provided an interpretable representation of relationships and shared characteristics among patients.
- **Neural NMF:** Feature-similarity-based helper functions improved the performance of the Neural NMF approach.
- **Fair NMF:** The proposed Fair NMF algorithm achieved better subgroup convergence while maintaining lower-rank representations compared with vanilla NMF and early stopping.

## My Contributions

- Explored and reproduced machine learning algorithms from the research literature for Lyme disease data analysis
- Implemented and evaluated **NMF-based methods** for latent pattern discovery
- Constructed and analyzed a **patient similarity network**
- Implemented a **multiplex community detection algorithm** (WSSNMTF) to identify interpretable patient communities, and later packaged it as a standalone Python library, [`wssnmtf`](./wssnmtf) ([v0.1.0 release](https://github.com/xiangdilin/portfolio/releases/tag/wssnmtf-v0.1.0))

## Technologies & Methods

**Programming:** Python

**Machine Learning:** Non-Negative Matrix Factorization (NMF), Semi-Supervised NMF (SSNMF), Neural NMF, Logistic Regression, Support Vector Machine (SVM)

**Anomaly Detection:** Isolation Forest, Local Outlier Factor (LOF)

**Network Analysis:** Patient Similarity Networks, Community Detection, Multiplex Networks

**Fair Machine Learning:** Fair NMF, Fair Dimensionality Reduction, Subgroup Loss Analysis

**Data:** [MyLymeData](https://www.lymedisease.org/mylymedata-lyme-disease-research/)

## Results

Our experiments demonstrated that NMF-based methods can effectively uncover meaningful structure in high-dimensional Lyme disease patient data. Unsupervised NMF revealed symptom patterns, while supervised NMF and conventional classification methods enabled the prediction of patient characteristics and neurological manifestations.

Anomaly detection methods identified patients with unusual symptom profiles, which could then be further investigated using supervised NMF. We also developed a patient network with multiplex community detection to provide additional insight into shared patient characteristics.

For fair dimensionality reduction, the proposed **Fair NMF** algorithm demonstrated improved subgroup convergence and lower-rank representations compared with vanilla NMF and early stopping. Together, these results demonstrate the potential of combining matrix factorization, classification, anomaly detection, network analysis, and fairness-aware dimensionality reduction for analyzing complex Lyme disease data.

## Contributors

Xinyu Dong, Haowen Geng, Nika Jafar Nia, Abby Hultquist, Aoxi Li, Dakota Lin, Jingyi Liu, Chelsea Nguyen.

> Listed in alphabetical order by last name.

Special thanks to our PI Prof. Deanna Needell (UCLA Math), Mentor Dr. Lara Kassab (UCLA Math), and consultant CEO Lorraine Johnson ([LymeDisease.org](https://www.lymedisease.org/)).

## Software Package: `wssnmtf`

A general-purpose implementation of the multiplex community detection algorithm used in this project, **Weighted Simultaneous Symmetric Non-negative Matrix Tri-Factorization (WSSNMTF)**, is available as a Python package in [`wssnmtf/`](./wssnmtf). It finds a shared community indicator matrix across multiple network layers over the same set of nodes.

- Latest release: [`wssnmtf-v0.1.0`](https://github.com/xiangdilin/portfolio/releases/tag/wssnmtf-v0.1.0)
- Includes synthetic multilayer-network generators, plotting helpers, clustering metrics, and unit tests
- See the [package README](./wssnmtf/README.md) for the full API and usage

```bash
pip install "git+https://github.com/xiangdilin/portfolio.git#subdirectory=projects/ai-for-health/wssnmtf"
```

```python
import wssnmtf as ws

division = [[0, 49], [50, 99], [100, 149]]
layers = {i: ws.synthetic_layer(150, division, max_entry=5, random_seed=i) for i in range(2)}
H, S = ws.WSSNMTF(layers, k=3, weights="all", n_init=10)
labels = ws.actual_assignment(H)
```

## Code Availability

The code used to analyze the patient survey data is **not publicly released** due to the sensitive nature of the data. The methods are documented in detail in the project report, including pseudocode for the NMF-based algorithms and the multiplex community detection procedure, along with the experimental setup and results.

The standalone [`wssnmtf`](./wssnmtf) package is the exception: it implements the community detection algorithm only, contains **no patient data**, and is demonstrated on synthetic networks. Note that it is a later, refactored version of the algorithm with additional options, not the exact analysis code used on the survey data.

## Report

[📄 Download the Full Report (PDF)](./REU_2023_AI_for_Health.pdf)

> For the best viewing experience, please download the PDF.
