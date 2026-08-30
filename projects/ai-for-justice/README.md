# AI for Justice: Detecting Patterns in Wrongful Convictions

A research project investigating the use of machine learning and AI to support innocence organizations in identifying patterns associated with wrongful convictions.

**You can find the project writeup PDF in this repo through either the navigation sidebar or a link at the end of this README.**

## Overview

Wrongful convictions are a persistent challenge in the U.S. criminal justice system, with systemic disparities disproportionately affecting minority groups. This project investigates the use of AI and machine learning to support innocence organizations in identifying patterns and key features associated with wrongful convictions. We developed a data-driven framework that combines legal document embeddings with Non-Negative Matrix Factorization (NMF)-based methods to classify exonerated and non-exonerated cases.

The dataset contains 140 murder cases from 39 U.S. states, including both exonerated and non-exonerated cases. Our work focuses on developing reliable and transparent computational methods that can assist with legal case analysis and appeal investigations.

## Research Objectives

- Identify patterns and key features associated with wrongful convictions
- Develop interpretable machine learning methods for analyzing heterogeneous legal case data
- Explore the use of **LLM embeddings** to represent textual case information
- Develop tools that can support innocence organizations in appeal investigations
- Evaluate the effectiveness of different matrix factorization methods for classification and feature reconstruction

## Methods

1. **Data Preparation**
   - Compiled a dataset of 140 murder cases from 39 U.S. states, including exonerated and non-exonerated cases.
   - Converted open-source legal documents into text embeddings for downstream analysis.

2. **NMF-Based Modeling**
   - Implemented existing methods including **Semi-NMF, Convex NMF, and SSNMF**.
   - Extended SSNMF with kernel methods to develop **Kernel SSNMF** for high-dimensional data.

3. **Theoretical Analysis**
   - Established convergence results for the proposed algorithms.

4. **Classification**
   - Developed a feature-matrix reconstruction approach for classification using Convex NMF and Kernel SSNMF.
   - Evaluated classification performance using **Support Vector Machines (SVM)**.

5. **Experimental Evaluation**
   - Tested the methods on high-dimensional benchmark datasets, including genomic data, as well as legal text embeddings.
   - Compared Kernel SSNMF against existing NMF-based approaches.

## Key Findings

- Developed a framework for converting open-source legal documents into **text embeddings** for classification.
- Introduced **Kernel Semi-Supervised Non-Negative Matrix Factorization (Kernel SSNMF)** for high-dimensional data analysis and classification.
- Proved the **convergence** of the proposed algorithm.
- Developed a **feature reconstruction-based classification approach** for Convex NMF and Kernel SSNMF.
- Kernel SSNMF **outperformed SSNMF and Convex NMF** on classification tasks involving high-dimensional datasets and LLM embeddings.
- **Polynomial kernels** consistently achieved higher classification accuracy across different numbers of topics.

## My Contributions

- Implemented and reproduced existing **Semi-NMF, Convex NMF, and SSNMF** algorithms
- Developed **Kernel SSNMF**, extending semi-supervised NMF with kernel methods
- Contributed to theoretical analysis and **convergence proofs**
- Applied NMF-based methods to **LLM embeddings** and legal case data
- Evaluated learned representations using **SVM classification**
- Analyzed model performance across different topic dimensions and kernel functions
- Contributed to the development of an AI-based framework for wrongful conviction investigation

## Technologies & Methods

## Technologies & Methods

**Programming**: Python

**Machine Learning**: Semi-NMF, Convex NMF, SSNMF, Kernel SSNMF, Support Vector Machine (SVM)

**Natural Language Processing**: Legal document embeddings, LLM embeddings

**Mathematical Methods**: Non-Negative Matrix Factorization, Kernel methods, Matrix reconstruction, Convergence analysis

**Datasets**: Exonerated and non-exonerated legal cases, UCI Genomic Data, GEMLeR Colon Kidney Data

## Results
Our experiments evaluated the proposed Kernel SSNMF method on publicly available high-dimensional datasets and legal text embeddings. The results showed that Kernel SSNMF consistently achieved better classification performance than both SSNMF and Convex NMF.

In particular, **polynomial kernels produced consistently higher accuracy across different numbers of topics**. These results demonstrate the potential of Kernel SSNMF for classification tasks involving high-dimensional data, including LLM-based legal document embeddings.

We also identified several limitations, including dataset size and coverage. Future work could expand the dataset, improve representation of legal case information, and further investigate methods for improving model interpretability and fairness.

## Contributors
**Team:** Anshuman Singh, Dakota Lin, Shreya Balaji, Kyle Torres. 

Special thanks to our PI Prof. Deanna Needell (UCLA Math), Mentor Dr. Minxin Zhang (UCLA Math), and our consultants Mike Semanchik ([The Innocence Center](https://theinnocencecenter.org/)) and Marissa Bluestine ([Quattrone at UPenn Law](https://www.law.upenn.edu/institutes/quattronecenter/)). 

## Report

[📄 Download the Full Report (PDF)](./REU_2024_AI_for_Justice.pdf)

> For the best viewing experience, please download the PDF.
