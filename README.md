# Dakota Xiangdi Lin — Portfolio

Welcome! I’m **Dakota**, a M.S. student at **Stanford’s Institute for Computational and Mathematical Engineering (ICME)** graduating in 2028, with a background in applied mathematics, machine learning, and computational research.

This repository showcases selected projects spanning **machine learning, natural language processing, network analysis, image processing, and data-driven modeling**. My work combines mathematical methods with practical computational tools to extract patterns from complex datasets and build interpretable solutions.

For code implementation, please visit the project specific pages in this repo. For the UCLA REU projects (AI for justice and health), the actual data will not be available here for confidential reasons. 

## Projects

### 1. AI for Justice — LLM Embeddings & Semi-Supervised NMF

**Focus:** Machine Learning · NLP · LLM Embeddings · Dimensionality Reduction · Classification

Developed an AI-based analytical framework to support innocence organizations in investigating potential wrongful convictions. Using a dataset of **140 murder cases across 39 U.S. states**, we explored how machine learning could identify patterns and features associated with exonerated and non-exonerated cases.

I implemented and evaluated **Semi-NMF, Convex NMF, SSNMF, and Kernel SSNMF**, including a novel kernel-based extension designed to handle mixed-sign LLM embeddings. The resulting low-dimensional representations were evaluated using SVM classification, with Kernel SSNMF demonstrating improved classification performance across different topic dimensions.

**My contributions**

* Developed **Convex Kernel Semi-Supervised NMF (Kernel SSNMF)**
* Worked with **LLM embeddings** and high-dimensional representations
* Conducted SVM-based classification and model evaluation
* Analyzed model performance and interpretability in the context of wrongful-conviction investigations

**Tech:** Python · Machine Learning · NMF · Semi-Supervised Learning · LLM Embeddings · SVM

📄 **[Download the Full Report (PDF)](./projects/ai-for-justice/REU_2024_AI_for_Justice.pdf)**

---

### 2. Lyme Disease Data Analysis — Machine Learning & Matrix Factorization

**Focus:** Machine Learning · NMF · Classification · Anomaly Detection · Network Analysis

Explored a large survey dataset of individuals affected by Lyme disease using a combination of **matrix factorization, supervised learning, anomaly detection, and network analysis**.

NMF was used to uncover latent patterns in symptoms and identify factors associated with neurological manifestations. Classification models including **Logistic Regression and SVM** were used to distinguish between chronic and early Lyme disease cases and predict diagnosis timing.

**My contributions**

* Developed helper functions based on feature similarity to improve the method
* Contributed to network-based analysis using patient similarity and community structure
* Constructed and analyzed a **patient similarity network**
* Implemented a **multiplex community detection algorithm** to identify interpretable patient communities

**Tech:** Python · NMF · Neural NMF · Semi-Supervised Learning · Logistic Regression · SVM · Network Analysis

📄 **[Download the Full Report (PDF)](./projects/ai-for-health/REU_2023_AI_for_Health.pdf)**

---

### 3. Temporal Avian Contact Networks — Community Detection & Epidemic Simulation

**Focus:** Network Science · Community Detection · Temporal Networks · Epidemic Simulation

Analyzed temporal contact networks of wild birds to investigate how network structure and node importance influence disease transmission. Using the **Aves Wildbird Network (AWN)** dataset, we studied both single-layer and multilayer community structures and evaluated their relationship with simulated disease outbreaks.

The project combined **Louvain and Leiden community detection**, multilayer **WSSNMTF**, temporal centrality measures, and infection simulations. We also developed **Time-Weighted Degree Centrality (TWDC)** and a recursive version with temporal decay to better capture the importance of nodes in dynamic networks.

**My contributions**

* Led the **community detection** component of the project
* Implemented and evaluated **Louvain and Leiden** algorithms
* Investigated single-layer vs. multilayer community structures
* Applied **WSSNMTF** to identify communities across temporal network layers
* Analyzed the relationship between community structure, modularity, and epidemic spread
* Contributed to methodology and data analysis

**Tech:** Python · NetworkX · Community Detection · Louvain · Leiden · NMTF · Temporal Networks · Epidemic Simulation

📄 **[Download the Full Report (PDF)](./projects/network-analysis/Temporal_Avian_Contact_Networks_for_Epidemic_Simulation_and_Prediction.pdf)**

---

### 4. Artificial Painting Toolbox — Image Processing in MATLAB

**Focus:** Image Processing · Computer Vision · Mathematical Modeling

Developed an image-processing toolbox that transforms photographs into different artistic styles, including **pencil sketch, comic, oil painting, Van Gogh-inspired strokes, and Cubism-like effects**.

The project explored how classical image-processing techniques can reproduce visual characteristics of traditional artistic media without relying on deep learning or neural style transfer.

**My contributions**

* Implemented and analyzed the **oil painting effect**
* Used local RGB histograms to identify dominant colors and generate brush-like regions
* Investigated improvements to reduce artifacts around sharp edges and uniform regions
* Contributed to the initial development and evaluation of the **Van Gogh-inspired stroke effect**
* Applied image-processing techniques including filtering, color manipulation, and local neighborhood analysis

**Tech:** MATLAB · Image Processing · Histogram Analysis · Filtering · Edge Detection · Color Manipulation

📄 **[Download the Full Report (PDF)](./projects/mathematical-imaging/Artificial_Painting_Toolbox.pdf)**

---

## Technical Interests

* **Machine Learning:** Supervised Learning · Semi-Supervised Learning · Matrix Factorization · Classification · Anomaly Detection
* **Data Science:** Exploratory Data Analysis · Statistical Modeling · Feature Engineering · Data Visualization
* **Natural Language Processing:** LLM Embeddings · Topic Modeling · Representation Learning
* **Network Science:** Community Detection · Centrality · Temporal Networks · Network Epidemiology
* **Computational Methods:** Numerical Methods · Optimization · Mathematical Modeling
* **Programming:** Python · MATLAB · R · SQL

## Tools & Libraries

**Python:** NumPy · Pandas · scikit-learn · NetworkX · PyTorch · TensorFlow/Keras · Gensim · Plotly

**Other:** MATLAB · R · SQL · Mathematica

## About

I’m particularly interested in applying **mathematical and computational methods to real-world data problems**, with current interests spanning machine learning, data science, and quantitative modeling.

More projects and updates will be added as I continue developing my portfolio.
