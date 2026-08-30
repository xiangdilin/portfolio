# Temporal Avian Contact Networks for Epidemic Simulation and Prediction

A research project investigating community structures and temporal network dynamics in avian contact networks, with applications to epidemic simulation and disease-spread prediction.

**You can find the project writeup PDF in this repo through either the navigation sidebar or a link at the end of this README.** 

**Visit our drive for code implementation and relevant `.py` & `.ipynb` files: [Drive](https://drive.google.com/drive/folders/1itn32cpfIFIWM-eH7Fjp2XWq_FvS_0AE)**

**Code contributed solely by myself is located at: [My Code](https://drive.google.com/drive/folders/19VV5W8KC0sJTmm-RpShi_5Mw0CC7CrVX)**

## Overview

Understanding how disease spreads through wildlife populations requires analyzing not only who interacts with whom, but also **when those interactions occur**. Traditional static network representations can lose important temporal information and may provide an incomplete picture of the structure through which infections spread.

In this project, we analyzed temporal contact networks of wild birds to investigate how network structure and node centrality influence epidemic spread. Applied single- and multilayer community detection methods, including Louvain, Leiden, and Weighted Simultaneous Symmetric Non-Negative Matrix Tri-Factorization (WSSNMTF), to characterize community structures across time. Developed Time-Weighted Degree Centrality (TWDC) and TWDC with Decay to incorporate both interaction weights and temporal dynamics, and evaluated their effectiveness through SI-model infection simulations on a synthetic 100-day network. Results showed that temporal centrality measures better predicted disease-spreading potential than static centrality measures, while high-centrality nodes within communities led to faster simulated outbreaks.

## My Contributions

I was primarily responsible for the project's **community detection analysis**, including both single-layer and multilayer approaches.

- Implemented and analyzed **single-layer community detection** using Louvain and Leiden algorithms.
- Evaluated community partitions using **modularity** and investigated how the number of communities affected the resulting network structure.
- Implemented and analyzed **Weighted Simultaneous Symmetric Non-Negative Matrix Tri-Factorization (WSSNMTF)** for multilayer community detection, treating interactions observed on different days as separate network layers.
- Investigated the differences between static and multilayer community structures and analyzed their interpretability in the context of the three observation locations.
- Analyzed how **community modularity changed during simulated epidemic outbreaks** and connected these structural changes to the progression of infection.
- Contributed to the analysis of how community structure could be incorporated into the evaluation of temporal centrality measures and epidemic simulations.

The community detection work provided the structural foundation for the later analysis of **temporal centrality and epidemic spread**, allowing us to investigate not only which birds were important for transmission, but also how their positions within network communities influenced outbreak dynamics.

## Community Detection

We investigated the community structure of the Aves Wildbird Network using both **single-layer and multilayer community detection** approaches.

For single-layer analysis, we aggregated interactions across the six observed days and evaluated community partitions using modularity. We applied the **Louvain** and **Leiden** algorithms to identify densely connected groups of birds and examined how the number of detected communities affected modularity. The baseline analysis generally favored a six-community partition when interactions were aggregated across time.

To preserve the temporal structure of the network, we also applied **Weighted Simultaneous Symmetric Non-Negative Matrix Tri-Factorization (WSSNMTF)** to model the daily interaction networks as separate layers. The method jointly factorizes the adjacency matrices of different days while learning a shared community indicator matrix, allowing community structure to be inferred across multiple network layers.

The multilayer analysis produced different community structures from the static baseline. In particular, a three-community partition was relatively more meaningful under WSSNMTF, consistent with the three locations represented in the original dataset. This comparison highlighted how preserving temporal and multilayer structure can lead to different interpretations of network organization.

We further examined how community structure changed during simulated disease outbreaks. As infection spread through the network, modularity decreased substantially, particularly during the early stages of the outbreak, suggesting that epidemic spread was associated with changes in the network's community organization.

## Temporal Centrality

We compared traditional network centrality measures with temporal centrality measures that explicitly account for the timing of interactions. Because the same pair of birds may interact with different weights at different times, aggregating these interactions into a static network can discard important temporal information.

The project developed **Time-Weighted Degree Centrality (TWDC)**, which incorporates both interaction strength and temporal distance. We further introduced **TWDC with Decay**, a recursive extension that incorporates the centrality of neighboring nodes from previous time steps while applying a temporal decay factor.

Across the experiments, TWDC and TWDC with Decay showed stronger relationships with the infection index than the other evaluated centrality measures, demonstrating the value of incorporating temporal information when identifying potentially influential nodes in dynamic contact networks.

## Epidemic Simulation

To evaluate the relationship between network structure and disease transmission, we constructed a synthetic **100-day temporal network** based on the original six-day Aves Wildbird Network dataset while preserving the observed daily numbers of nodes and edges.

We simulated disease transmission using an **SI model**, selecting one or more initial infected birds and propagating infection through temporal interactions. The probability of transmission was proportional to the interaction weight and an infection-rate parameter. We introduced an **infection index** based on the timing of massive infection to quantify how effectively each node could initiate an outbreak.

The simulations were subsequently used to evaluate whether nodes identified as highly central within their communities were more effective at initiating outbreaks than randomly selected nodes.

## Results

The experiments demonstrated three main findings:

- **Temporal information matters:** Temporal centrality measures generally correlated more strongly with the infection index than static centrality measures.
- **Community structure affects epidemic dynamics:** Modularity decreased substantially during the early stages of simulated outbreaks, indicating changes in network organization as infection spread.
- **High-centrality nodes accelerate outbreaks:** Simulations initialized with high-TWDC nodes from different communities reached major infection milestones faster than simulations using randomly selected initial infected nodes, supporting TWDC as a useful measure of disease-spreading potential.

## Contributors
Zi Zhu, You Wu, Dakota Lin, Yizhuo Chang, Stephanie Su, Guolei Mao

## Report

[📄 Download the Full Report (PDF)](./Temporal_Avian_Contact_Networks_for_Epidemic_Simulation_and_Prediction.pdf)

> For the best viewing experience, please download the PDF.

## License

This project is licensed under the MIT License. 
