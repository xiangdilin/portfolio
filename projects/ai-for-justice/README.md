# AI for Justice: Detecting Patterns in Wrongful Convictions

A research project investigating the use of machine learning and AI to support innocence organizations in identifying patterns associated with wrongful convictions.

## Overview

Wrongful convictions are a persistent challenge in the U.S. criminal justice system, with systemic disparities disproportionately affecting minority groups. This project explores how AI can provide transparent, data-driven tools to assist innocence organizations with case investigation by summarizing case data, identifying relevant features, and supporting complex searches.

Working with guidance from the Innocence Center, we constructed a dataset of **140 murder cases across 39 U.S. states**, including both exonerated and non-exonerated cases. Exonerated cases were sourced from the National Registry of Exonerations, while non-exonerated cases were selected to maintain geographic diversity and match the states represented in the exonerated cases.

## Research Objectives

- Identify patterns and key features associated with wrongful convictions
- Develop interpretable machine learning methods for analyzing heterogeneous legal case data
- Explore the use of **LLM embeddings** to represent textual case information
- Develop tools that can support innocence organizations in appeal investigations
- Evaluate the effectiveness of different matrix factorization methods for classification and feature reconstruction

## Methods

We implemented and evaluated several Nonnegative Matrix Factorization (NMF) and semi-supervised learning approaches:

- **Semi-NMF**
- **Convex NMF**
- **Semi-Supervised NMF (SSNMF)**
- **Kernel SSNMF** — a novel extension developed in this project

Because the dataset contains both mixed-sign and nonnegative features, the algorithms were adapted to accommodate different data characteristics. We also developed **convergence proofs** for the implemented algorithms to establish their theoretical reliability.

For evaluation, the learned representations were used for:

- Feature matrix reconstruction
- Case classification
- SVM-based downstream classification
- Performance comparison across different numbers of topics
- Evaluation on both gene expression data and **LLM embedding representations**

## Key Findings

**Kernel SSNMF consistently outperformed Convex NMF and SSNMF in classification tasks**, particularly when applied with polynomial kernels.

The results demonstrated improved classification accuracy across different numbers of topics on both gene expression data and LLM embedding datasets, suggesting that kernelized semi-supervised NMF can provide useful representations for complex, heterogeneous datasets.

## My Contributions

- Implemented and reproduced existing **Semi-NMF, Convex NMF, and SSNMF** algorithms
- Developed **Kernel SSNMF**, extending semi-supervised NMF with kernel methods
- Contributed to theoretical analysis and **convergence proofs**
- Applied NMF-based methods to **LLM embeddings** and legal case data
- Evaluated learned representations using **SVM classification**
- Analyzed model performance across different topic dimensions and kernel functions
- Contributed to the development of an AI-based framework for wrongful conviction investigation

## Technologies & Methods

**Programming:** Python

**Machine Learning:** NMF, Semi-Supervised Learning, Kernel Methods, SVM, Classification

**AI / NLP:** LLM Embeddings

**Mathematical Methods:** Matrix Factorization, Optimization, Convergence Analysis

**Data:** Legal Case Data, Gene Expression Data, Text Embeddings

## Results

Our experiments suggest that Kernel SSNMF can improve classification performance over existing NMF-based approaches, particularly with polynomial kernels. The study also highlights opportunities for using AI and machine learning to develop more transparent and effective tools for legal case investigation.

The project identified several limitations, including dataset size and coverage. Future work could expand the dataset, improve representation of legal case information, and further investigate methods for improving model interpretability and fairness.

## Report

[📄 Download the Full Report (PDF)](./report.pdf)

> For the best viewing experience, please download the PDF.
