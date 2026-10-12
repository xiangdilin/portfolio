# Temporal Avian Contact Networks for Epidemic Simulation and Prediction

A research project investigating community structures and temporal network dynamics in avian contact networks, with applications to epidemic simulation and disease-spread prediction.

**You can find the project code and the project writeup PDF in this repo through either the navigation sidebar or the links at the end of this README.**

## Overview

Understanding how disease spreads through wildlife populations requires analyzing not only who interacts with whom, but also **when those interactions occur**. Traditional static network representations can lose important temporal information and may provide an incomplete picture of the structure through which infections spread.

In this project, we analyzed temporal contact networks of wild birds from the **Aves Wildbird Network (AWN)** dataset to investigate how network structure and node centrality influence epidemic spread. We applied single- and multilayer community detection methods, developed new temporal centrality measures, and evaluated them through infection simulations on a synthetic 100-day network.

## Project Goals

- Characterize the **community structure** of a temporal wildbird contact network using single-layer and multilayer methods.
- Develop **temporal centrality measures** that incorporate both interaction weights and the timing of interactions.
- Evaluate how well different centrality measures predict **disease-spreading potential** through epidemic simulation.
- Investigate how **community structure** relates to the progression of simulated outbreaks.

## Methods

1. **Community Detection**
   - Applied **Louvain** and **Leiden** algorithms to the network aggregated across the six observed days, and evaluated partitions using **modularity**.
   - Applied **Weighted Simultaneous Symmetric Non-Negative Matrix Tri-Factorization (WSSNMTF)** to model each day's interactions as a separate network layer, jointly factorizing the layers while learning a shared community indicator matrix.

2. **Temporal Centrality**
   - Developed **Time-Weighted Degree Centrality (TWDC)**, which incorporates both interaction strength and temporal distance.
   - Introduced **TWDC with Decay**, a recursive extension that incorporates the centrality of neighboring nodes from previous time steps with a temporal decay factor.
   - Compared these measures against traditional static centrality measures.

3. **Epidemic Simulation**
   - Constructed a synthetic **100-day temporal network** from the original six-day dataset, preserving the observed daily numbers of nodes and edges.
   - Simulated transmission with an **SI model**, where infection probability is proportional to interaction weight and an infection-rate parameter.
   - Introduced an **infection index** based on the timing of massive infection to quantify how effectively each node can initiate an outbreak.

## Key Findings

- **Static vs. multilayer communities:** On the aggregated network, the baseline analysis generally favored a six-community partition. Under WSSNMTF, a three-community partition was relatively more meaningful, consistent with the three observation locations in the original dataset.
- **Temporal centrality:** TWDC and TWDC with Decay showed stronger relationships with the infection index than the other evaluated centrality measures.
- **Community structure during outbreaks:** Modularity decreased substantially, particularly in the early stages of simulated outbreaks.
- **High-centrality nodes:** Simulations started from high-TWDC nodes in different communities reached major infection milestones faster than simulations started from random nodes.

## My Contributions

I was primarily responsible for the project's **community detection analysis**, including both single-layer and multilayer approaches.

- Implemented and analyzed **single-layer community detection** using Louvain and Leiden algorithms
- Evaluated community partitions using **modularity** and investigated how the number of communities affected the resulting network structure
- Implemented and analyzed **WSSNMTF** for multilayer community detection, treating interactions observed on different days as separate network layers
- Investigated the differences between static and multilayer community structures and analyzed their interpretability in the context of the three observation locations
- Analyzed how **community modularity changed during simulated epidemic outbreaks** and connected these structural changes to the progression of infection
- Contributed to the analysis of how community structure could be incorporated into the evaluation of temporal centrality measures and epidemic simulations

## Technologies & Methods

**Programming:** Python

**Network Analysis:** Community Detection, Louvain, Leiden, Multilayer Networks, Modularity

**Matrix Factorization:** WSSNMTF (Non-Negative Matrix Tri-Factorization)

**Temporal Networks:** Time-Weighted Degree Centrality (TWDC), TWDC with Decay, Centrality Measures

**Epidemic Modeling:** SI Model, Infection Simulation, Infection Index

**Data:** Aves Wildbird Network (AWN) from the [Network Data Repository](https://networkrepository.com/)

## Results

The experiments demonstrated three main findings. First, **temporal information matters**: temporal centrality measures generally correlated more strongly with the infection index than static ones. Second, **community structure affects epidemic dynamics**: the sharp drop in modularity early in simulated outbreaks indicates that infection spread is tied to changes in network organization. Third, **high-centrality nodes accelerate outbreaks**: initial infections at high-TWDC nodes spread faster than random ones, supporting TWDC as a useful measure of disease-spreading potential.

The community detection work provided the structural foundation for the analysis of temporal centrality and epidemic spread, allowing us to study not only which birds were important for transmission, but also how their positions within network communities influenced outbreak dynamics.

## Contributors

Yizhuo Chang, Dakota Lin, Guolei Mao, Stephanie Su, You Wu, Zi Zhu.

> Listed in alphabetical order by last name.

Special thanks to Prof. Mason Porter for his guidance throughout this study and our Teaching Assistant, Michael Johnson, for his constant support and advice.

## Code

**My code** (community detection) is in [`code_files`](./code_files):

- [`Community Detection - Aves Wildbird (AWN).ipynb`](./code_files/Community%20Detection%20-%20Aves%20Wildbird%20%28AWN%29.ipynb): single-layer and multilayer community detection analysis on the AWN dataset
- [`WSSNMTF.py`](./code_files/WSSNMTF.py): implementation of the WSSNMTF algorithm
- [`aves-wildbird-network/`](./code_files/aves-wildbird-network): the Aves Wildbird Network dataset used in this project

**Team code** (temporal centrality, epidemic simulation, and other members' work) is available in our shared [Google Drive folder](https://drive.google.com/drive/folders/1itn32cpfIFIWM-eH7Fjp2XWq_FvS_0AE).

## Report

[📄 Download the Full Report (PDF)](./Temporal_Avian_Contact_Networks_for_Epidemic_Simulation_and_Prediction.pdf)

> For the best viewing experience, please download the PDF.

## License

This project is licensed under the MIT License.
