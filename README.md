# Dakota Lin's Portfolio

Welcome! I'm Dakota, an M.S. student at **Stanford University Institute for Computational and Mathematical Engineering (ICME)** graduating in 2028, with a background in applied mathematics, machine learning, and computational research.

My work combines mathematical methods with practical computational tools to extract patterns from complex datasets and build interpretable solutions. This repository showcases selected projects spanning machine learning, natural language processing, network analysis, image processing, remote sensing, and data-driven modeling.

It also includes interactive web applications I built out of personal interest and for my own use.

## 🔬 Projects

> **Research & coursework.** Each project includes a full writeup (PDF), and some include code. 🚧 marks ongoing work.

| # | Project | Area | Key Methods |
|---|---------|------|-------------|
| 🚧 | [Mapping Global Aquaculture Ponds](#mapping-global-aquaculture-ponds--satellite-imagery--machine-learning-in-progress) *(in progress)* | Remote Sensing · Computer Vision | Sentinel-1/2, Earth Foundation Models, Multimodal LLM Validation |
| 1 | [AI for Justice: Detecting Patterns in Wrongful Convictions](#1-ai-for-justice-detecting-patterns-in-wrongful-convictions) | NLP · Classification | Kernel SSNMF, LLM Embeddings, SVM |
| 2 | [Machine Learning Analysis of Lyme Disease Data](#2-machine-learning-analysis-of-lyme-disease-data) | Health ML · Network Analysis | NMF, Anomaly Detection, Community Detection |
| 3 | [Predicting Health Insurance Premiums](#3-predicting-health-insurance-premiums--regression-modeling--feature-selection) | Regression · Feature Selection | Lasso, RFE, SVR, Neural Networks, Clustered Linear Regression |
| 4 | [Temporal Avian Contact Networks](#4-temporal-avian-contact-networks--community-detection--epidemic-simulation) | Network Science | Louvain, Leiden, WSSNMTF, Epidemic Simulation |
| 5 | [Artificial Painting Toolbox](#5-artificial-painting-toolbox--image-processing-in-matlab) | Image Processing | Histogram Analysis, Filtering, Edge Detection |

---

### Mapping Global Aquaculture Ponds — Satellite Imagery & Machine Learning (In Progress)

🚧 **Status: In progress (Fall 2026, ICME Xplore)**

**Focus:** Remote Sensing · Machine Learning · Computer Vision · Earth Foundation Models · Multimodal LLMs

Part of a three-person team developing a scalable machine learning workflow to detect and map **land-based aquaculture ponds** from satellite imagery, under the guidance of mentors from the Stanford Doerr School of Sustainability. Aquaculture supplies a growing share of the world's aquatic food, but the global spatial distribution of its ponds remains poorly documented, which limits our ability to track its expansion and its relationships with land-use change, biodiversity, and water resources.

The project aims to produce a **high-resolution global map of aquaculture ponds** with confidence estimates and a reproducible pipeline, building on existing aquaculture datasets, **Sentinel-1 and Sentinel-2** imagery, and representations from **Earth foundation models**.

**What we're building**

* Training labels built from **pixel-level agreement** across existing aquaculture maps, with disagreements flagged for review
* A baseline using spectral, temporal, and geometric features, followed by an **Earth foundation model** for pond detection and segmentation
* A **multimodal LLM validation stage** to reduce false positives from look-alike features such as rice fields, salt pans, and reservoirs
* Evaluation on **geographically separated regions** using precision, recall, F1 score, and IoU

**Tech:** Remote Sensing · Sentinel-1/2 · Earth Foundation Models · Image Segmentation · Multimodal LLMs

📄 **[Read the Project Proposal (PDF)](./projects/aquaculture-mapping/Project_Proposal.pdf)**

---

### 1. AI for Justice: Detecting Patterns in Wrongful Convictions

**Focus:** Machine Learning · NLP · LLM Embeddings · Dimensionality Reduction · Classification

Developed an AI-based analytical framework to support innocence organizations in investigating potential wrongful convictions. Using a dataset of **140 murder cases across 39 U.S. states**, we explored how machine learning could identify patterns and features associated with exonerated and non-exonerated cases.

I implemented and evaluated **Semi-NMF, Convex NMF, SSNMF, and Kernel SSNMF**, including a novel kernel-based extension designed to handle mixed-sign LLM embeddings. The resulting low-dimensional representations were evaluated using SVM classification, with Kernel SSNMF demonstrating improved classification performance across different topic dimensions.

**My contributions**

* Developed **Convex Kernel Semi-Supervised NMF (Kernel SSNMF)**
* Worked with **LLM embeddings** and high-dimensional representations
* Conducted SVM-based classification and model evaluation
* Analyzed model performance and interpretability in the context of wrongful-conviction investigations

**Tech:** Python · Machine Learning · Dimensionality Reduction · Kernel Methods · LLM Embeddings · SVM

📄 **[Download the Full Report (PDF)](./projects/ai-for-justice/REU_2024_AI_for_Justice.pdf)** · 🔒 **Code is not public due to data sensitivity.**

---

### 2. Machine Learning Analysis of Lyme Disease Data

**Focus:** Machine Learning · NMF · Classification · Anomaly Detection · Network Analysis

Explored a large survey dataset of individuals affected by Lyme disease using a combination of **matrix factorization, supervised learning, anomaly detection, and network analysis**.

NMF was used to uncover latent patterns in symptoms and identify factors associated with neurological manifestations. Classification models including **Logistic Regression and SVM** were used to distinguish between chronic and early Lyme disease cases and predict diagnosis timing.

**My contributions**

* Developed helper functions based on feature similarity to improve the method
* Constructed and analyzed a **patient similarity network**
* Implemented a **multiplex community detection algorithm** to identify interpretable patient communities

**Tech:** Python · NMF · Neural NMF · Anomaly Detection · Logistic Regression · Classification · Network Analysis

📄 **[Download the Full Report (PDF)](./projects/ai-for-health/REU_2023_AI_for_Health.pdf)** · 🔒 **Code is not public due to data sensitivity.**

---

### 3. Predicting Health Insurance Premiums — Regression Modeling & Feature Selection

**Focus:** Machine Learning · Regression · Feature Selection · Data Visualization · Network Analysis

Analyzed a Kaggle dataset of US health insurance records to understand which factors drive premium charges and to compare models for predicting them. Working with a **10,000-record sample** of the original one-million-row dataset, we combined exploratory visualization, feature selection, and a range of regression models.

We compared **k-NN, Linear Regression, Support Vector Regression, Neural Networks, and Clustered Linear Regression**, with Clustered Linear Regression performing best (**R² ≈ 0.995**) and revealing a two-cluster structure in the data. To test how realistic the synthetic dataset was, we also analyzed real **CMS Medicare spending data**, which showed regional cost differences that the primary dataset failed to capture.

**My contributions**

* Created visualizations of charges against BMI, smoking status, gender, and medical history
* Performed supplementary analysis of **CMS National Health Expenditure data** with interactive choropleth maps
* Prepared the data for modeling, including feature encoding, standardization, and train/test splitting
* Applied **Lasso and Recursive Feature Elimination (RFE)** to select the top 21 of 30 features and studied the effect of feature count on accuracy
* Implemented the **WSSNMTF** multilayer community detection algorithm from the literature to explore clustering structure

**Tech:** Python · scikit-learn · TensorFlow/Keras · Lasso · RFE · PCA · SVR · k-NN · Clustered Linear Regression · Community Detection

📄 **[Download the Full Report (PDF)](./projects/insurance-premiums-prediction/Project_Report.pdf)** · 💻 **[View the Code (Jupyter Notebook)](./projects/insurance-premiums-prediction/predicting_premiums.ipynb)**

---

### 4. Temporal Avian Contact Networks — Community Detection & Epidemic Simulation

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

**Tech:** Python · NetworkX · Community Detection · Louvain · Leiden · NMTF · Centrality Measures · Epidemic Simulation

📄 **[Download the Full Report (PDF)](./projects/network-analysis/Temporal_Avian_Contact_Networks_for_Epidemic_Simulation_and_Prediction.pdf)** · 💻 **[Browse the Code](./projects/network-analysis/code_files)**

---

### 5. Artificial Painting Toolbox — Image Processing in MATLAB

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

📄 **[Download the Full Report (PDF)](./projects/mathematical-imaging/Artificial_Painting_Toolbox.pdf)** · 💻 **[Browse the Code](./projects/mathematical-imaging/code_files)**

---

## 🌐 Live Sites

> **Personal web apps.** Unlike the research projects above, these are interactive tools I designed and built for my own use. Click a site name to open it.

| Site | What it does | Built with |
|------|--------------|------------|
| 🧳 **[California · Stanford Move-in Trip](https://california-trip-2026.xiangdi-lin.workers.dev)** | A bilingual, mobile-first travel dashboard for my relocation to Stanford. It brings flights, hotels, rental cars, and move-in logistics into one place, with a live time-zone-aware countdown, interactive route maps with satellite view, one-click Google Maps navigation, and a Chinese / English switch. The public version excludes all sensitive details. | HTML · CSS · JavaScript · SVG · Leaflet · Cloudflare Workers |
| 🍸 **[Cocktail Field Guide](https://my-cocktails.xiangdi-lin.workers.dev/)** | A bilingual interactive guide to 70+ classic and modern cocktails, filterable by base spirit, flavor, and occasion, with search, a random-pick button, and custom SVG illustrations in a vintage pinned-note layout. Fully static, with no backend or database. | HTML · CSS · JavaScript · SVG · Cloudflare Workers |

---

## Technical Interests

* **Machine Learning:** Supervised Learning · Semi-Supervised Learning · Matrix Factorization · Classification · Regression · Anomaly Detection
* **Data Science:** Exploratory Data Analysis · Statistical Modeling · Feature Engineering · Feature Selection · Data Visualization
* **Natural Language Processing:** LLM Embeddings · Topic Modeling · Representation Learning
* **Network Science:** Community Detection · Centrality · Temporal Networks · Network Epidemiology
* **Computational Methods:** Numerical Methods · Optimization · Mathematical Modeling
* **Programming:** Python · MATLAB · SQL · R

## Tools & Libraries

**Python:** NumPy · Pandas · scikit-learn · NetworkX · PyTorch · TensorFlow/Keras · Gensim · Plotly

**Other:** MATLAB · R · SQL · Mathematica · HTML

## About

I'm particularly interested in applying **mathematical and computational methods to real-world data problems**, with current interests spanning machine learning, data science, and quantitative modeling.

More projects and updates will be added as I continue developing my portfolio.
