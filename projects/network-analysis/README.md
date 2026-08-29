# Temporal Avian Contact Networks for Epidemic Simulation and Prediction

A research project investigating community structures and temporal network dynamics in avian contact networks, with applications to epidemic simulation and disease-spread prediction.

**You can find the project writeup PDF in this repo.** 

**Visit our drive for code implementation and relevant `.py` & `.ipynb` files: https://drive.google.com/drive/folders/1itn32cpfIFIWM-eH7Fjp2XWq_FvS_0AE**

**Code implementation contributed solely by myself is located at: https://drive.google.com/drive/folders/19VV5W8KC0sJTmm-RpShi_5Mw0CC7CrVX**

## Overview

Understanding how disease spreads through wildlife populations requires analyzing not only who interacts with whom, but also **when those interactions occur**. Traditional static network representations can lose important temporal information and may provide an incomplete picture of the structure through which infections spread.

In this project, we analyzed the **Aves Wildbird Network (AWN)** dataset, which records interactions among wild birds across six consecutive days. We investigated community structures in the network and examined how these structures relate to simulated disease spread.

The project combined **single-layer and multilayer community detection** with temporal network analysis and infection simulations.

## My Contribution

I was responsible for **all community detection components** of the project, including the implementation, analysis, and evaluation of both single-layer and multilayer community detection methods.

### Single-Layer Community Detection

I implemented and evaluated multiple community detection approaches on aggregated avian contact networks:

- **Louvain Algorithm**
- **Leiden Algorithm**
  - ModularityVertexPartition
  - RBConfigurationVertexPartition

For the baseline analysis, interactions across the six-day observation period were aggregated into a weighted network. I evaluated different numbers of communities using **modularity** and compared the resulting community structures.

The baseline analysis found that partitions with **six communities** generally achieved the highest modularity among the single-layer methods.

### Multilayer Community Detection

To preserve the temporal structure of the original data, I also analyzed the network using **Weighted Simultaneous Symmetric Non-Negative Matrix Tri-Factorization (WSSNMTF)**.

Instead of aggregating interactions across time, each observation day was treated as a separate network layer. WSSNMTF jointly factorizes these layers using a shared community indicator matrix:

\[
A^{(i)} \approx HS^{(i)}H^T
\]

This approach allowed us to investigate community structures while retaining information about interactions across different days.

The multilayer analysis suggested that a **three-community structure** was more meaningful than the six-community structure identified by the single-layer baseline, illustrating how temporal information can substantially affect inferred network structure.

## Community Detection Analysis

We compared community structures using modularity and examined how the detected communities changed during simulated disease outbreaks.

One important finding was the difference between static and multilayer approaches:

- **Single-layer methods:** Aggregating interactions across time generally favored a six-community partition.
- **Multilayer WSSNMTF:** Preserving daily network layers suggested a three-community structure.
- This difference demonstrates the potential information loss associated with collapsing a temporal network into a static representation.

We also investigated how **modularity changed during epidemic simulations**. A substantial decrease in modularity was observed during the early stages of infection, particularly around Days 1–2, coinciding with a rapid increase in the number of infected birds.

These results suggest a relationship between the evolution of community structure and the progression of an epidemic.

## Disease Spread Simulation

The community structures identified through the above methods were subsequently used in epidemic simulations.

The simulation was performed on a synthetic 100-day extension of the original AWN dataset. Initial infected nodes ("patient zero") were selected under different strategies, and infection propagated through network interactions according to edge weights and an infection-rate parameter.

We compared simulations initialized with:

- High-centrality nodes within detected communities
- Randomly selected nodes across the network

This allowed us to investigate how network structure and node importance influence epidemic progression.

## Key Findings

- Static community detection methods identified strong community structures in the avian contact network, with six communities generally producing the highest modularity.
- Multilayer community detection produced different structural insights, with three communities appearing relatively more meaningful when temporal layers were preserved.
- The discrepancy between static and multilayer results highlights the importance of **temporal information in network community detection**.
- Network modularity decreased substantially during the early stages of simulated infection, coinciding with rapid disease spread.
- Community structure provided an additional framework for evaluating the effectiveness of temporal centrality measures in predicting epidemic progression.

## Technical Methods

**Community Detection**
- Louvain
- Leiden
- Modularity Optimization
- Resolution-based Community Detection
- WSSNMTF
- Multilayer Community Detection

**Network Analysis**
- Weighted Graphs
- Temporal Networks
- Community Structure
- Modularity
- Node Centrality

**Epidemic Modeling**
- SI Infection Model
- Random-Walk-Based Infection Simulation
- Infection Progression Analysis

**Mathematical Methods**
- Non-Negative Matrix Factorization
- Matrix Tri-Factorization
- Optimization
- Graph Theory

## Dataset

The project uses the **Aves Wildbird Network (AWN)** dataset, which records interactions between wild birds across six consecutive days.

Because the original observation period was short, we generated a synthetic 100-day network while preserving the approximate daily distribution of nodes and edges. This extended dataset was used for epidemic simulations.

## Results

The results demonstrate that incorporating temporal information can lead to substantially different conclusions about community structure compared with static network analysis.

The combination of community detection and epidemic simulation also provided a framework for studying how structural properties of wildlife contact networks influence disease propagation.

## Report

[📄 Download the Full Report (PDF)](./Temporal_Avian_Contact_Networks_for_Epidemic_Simulation_and_Prediction.pdf)

> For the best viewing experience, please download the PDF.
