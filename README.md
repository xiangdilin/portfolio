# Dakota Lin's Portfolio

Welcome! I’m Dakota, a M.S. student at **Stanford University Institute for Computational and Mathematical Engineering (ICME)** graduating in 2028, with a background in applied mathematics, machine learning, and computational research.

This repository showcases selected projects spanning **machine learning, natural language processing, network analysis, image processing, data-driven modeling, and interactive web applications**. My work combines mathematical methods with practical computational tools to extract patterns from complex datasets and build interpretable solutions.

**For the best viewing experience of the project writeups, please download the PDFs.**

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

**Tech:** Python · Machine Learning · Dimensionality Reduction · Kernel Methods · LLM Embeddings · SVM

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

**Tech:** Python · NMF · Neural NMF · Anomaly Detection · Logistic Regression · Classification · Network Analysis

📄 **[Download the Full Report (PDF)](./projects/ai-for-health/REU_2023_AI_for_Health.pdf)**

---

### 3. California · Stanford Move-in Trip — Bilingual Travel Dashboard

**Focus:** Front-End Development · Product Design · Interactive Maps · Time-Zone-Aware Scheduling · Deployment

Designed and deployed a bilingual, mobile-first travel dashboard for a real California relocation and Stanford move-in journey. The site consolidates international flights, rental cars, hotel stays, moving logistics, university housing check-in, shopping, dining, sightseeing, and airport transportation into a single interactive interface.

The project was built around real travel constraints, including fixed flight schedules, cross-time-zone timing, long-distance driving, university move-in logistics, advance reservations, public-facing privacy requirements, and the need for fast mobile access while traveling.

**Key features**

* Built a live **next-event countdown** using explicit time-zone-aware timestamps across China, Hong Kong, and California
* Designed an interactive **California itinerary map** using geographically scaled coordinates and day-specific route overlays
* Added **Map / Satellite switching**, with an offline vector map by default and satellite imagery loaded on demand
* Implemented interactive **zooming, panning, and map reset controls** for both the trip overview and individual daily routes
* Integrated one-click **Google Maps navigation** for destinations, hotels, rental-car locations, shopping, and multi-stop routes
* Added location-aware **Yelp restaurant recommendations** and nearby grocery / shopping links directly within relevant itinerary entries
* Built a persistent **Chinese / English language switch** across the full interface
* Implemented both automatic and manual **light / dark mode**, with user preferences saved locally
* Added a mobile-friendly **Quick Nav** for jumping directly to current status, overview, reservations, daily itinerary, to-do items, and travel tips
* Created a unified **status system** for confirmed reservations, pending items, action items, recommended bookings, and required reservations
* Designed custom lightweight **inline SVG illustrations** for trip statistics and route visualization
* Structured the interface around mobile readability, fast access, clear information hierarchy, and minimal interaction overhead
* Designed the public-facing version to exclude sensitive information such as passport details, reservation numbers, access codes, payment information, and exact residential unit information
* Connected GitHub to **Cloudflare Workers** for automatic deployment whenever the repository is updated

**Tech:** HTML · CSS · Vanilla JavaScript · SVG · Leaflet · Esri World Imagery · Google Maps · Yelp · GitHub · Cloudflare Workers

🌐 **[View the Live Site](https://california-trip-2026.xiangdi-lin.workers.dev)**

![California Stanford Move-in Trip Preview](./projects/trip-organizer/assets/preview.png)

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

📄 **[Download the Full Report (PDF)](./projects/network-analysis/Temporal_Avian_Contact_Networks_for_Epidemic_Simulation_and_Prediction.pdf)**

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

📄 **[Download the Full Report (PDF)](./projects/mathematical-imaging/Artificial_Painting_Toolbox.pdf)**

---

## Technical Interests

* **Machine Learning:** Supervised Learning · Semi-Supervised Learning · Matrix Factorization · Classification · Anomaly Detection
* **Data Science:** Exploratory Data Analysis · Statistical Modeling · Feature Engineering · Data Visualization
* **Natural Language Processing:** LLM Embeddings · Topic Modeling · Representation Learning
* **Network Science:** Community Detection · Centrality · Temporal Networks · Network Epidemiology
* **Computational Methods:** Numerical Methods · Optimization · Mathematical Modeling
* **Programming:** Python · MATLAB · SQL · R

## Tools & Libraries

**Python:** NumPy · Pandas · scikit-learn · NetworkX · PyTorch · TensorFlow/Keras · Gensim · Plotly

**Other:** MATLAB · R · SQL · Mathematica · HTML

## About

I’m particularly interested in applying **mathematical and computational methods to real-world data problems**, with current interests spanning machine learning, data science, and quantitative modeling.

More projects and updates will be added as I continue developing my portfolio.
