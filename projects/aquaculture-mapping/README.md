# Mapping Global Aquaculture Ponds with Satellite Imagery and Machine Learning

A research project developing a scalable machine learning workflow to detect and map land-based aquaculture ponds from satellite imagery, as part of **ICME Xplore (Fall 2026)** at Stanford University.

> 🚧 **Status: In progress.** This project is currently underway (Fall 2026). This README describes the project plan and will be updated as results become available.

**You can find the project proposal PDF in this repo through either the navigation sidebar or a link at the end of this README.**

## Overview

Aquaculture supplies a growing share of the world's aquatic food and plays an important role in food security and livelihoods. Land-based ponds account for much of this production, but their global spatial distribution remains poorly documented. Without consistent, high-resolution spatial data, researchers cannot reliably assess where aquaculture is expanding or evaluate its relationships with land-use change, biodiversity, water resources, and surrounding ecosystems.

Existing remote-sensing studies provide an important foundation but remain incomplete in geographic coverage, temporal extent, or spatial resolution. Prior work has produced a global map of pond clusters from 2020 Sentinel-2 imagery (Wang et al., 2022), mapped individual ponds across the coastal zone of Asia using Sentinel-1 and Sentinel-2 time series (Ottinger et al., 2022), and reconstructed coastal pond changes in China and Southeast Asia from 1990 to 2020 using Landsat imagery (Jiang et al., 2024). However, no existing study provides complete global coverage, consistent pond-level delineation, and systematic validation across diverse geographic regions.

This project aims to fill that gap by combining existing aquaculture datasets, multispectral and potentially radar imagery, and representations from Earth foundation models into a reproducible mapping pipeline.

## Project Goals

- Develop a **scalable machine learning workflow** for detecting and mapping aquaculture ponds from satellite imagery.
- Integrate **existing aquaculture datasets** with Sentinel-1 and Sentinel-2 imagery to build reliable training data.
- Distinguish aquaculture ponds from visually similar features such as **rice fields, salt pans, reservoirs, and natural water bodies**.
- Investigate whether a **multimodal LLM validation stage** can reduce false positives and flag uncertain detections for human review.
- Produce a **high-resolution global map of aquaculture ponds** with confidence estimates and a reproducible pipeline.

## Planned Methods

1. **Data Collection & Preprocessing**
   - Assemble existing aquaculture maps and corresponding satellite imagery, initially focusing on **Sentinel-1 and Sentinel-2**.
   - Harmonize datasets across spatial resolutions, geographic regions, and observation periods.

2. **Training Data Development**
   - Use existing aquaculture maps as preliminary labels for candidate pond locations.
   - Compare overlapping products and construct pixel-level labels based on agreement: unanimous agreement gives high-confidence positive or negative labels, while disagreements are flagged for closer review.
   - Build representative positive and negative samples across regions and pond types.

3. **Aquaculture Pond Detection**
   - Establish a baseline using conventional **spectral, temporal, and geometric features**.
   - Evaluate an **Earth foundation model** for pond detection or segmentation.

4. **LLM-Based Validation**
   - Use a **multimodal large language model** to review candidate detections with satellite imagery and geographic context.
   - Compare against lower-cost alternatives such as rule-based geometric filtering, depending on the cost of LLM-based validation.

5. **Evaluation & Global Mapping**
   - Evaluate models on **geographically separated training and test regions** using precision, recall, F1 score, and intersection over union (IoU).
   - Apply the best-performing workflow at larger scale to generate a global aquaculture pond map.

## Timeline

| Weeks | Milestone |
|-------|-----------|
| 1 | Set up and evaluate technical needs |
| 2–4 | Preprocessing and training data development |
| 5–7 | Baseline and model building |
| 8–9 | Validation |
| 10 | Project wrap-up |

> This is the rough plan from our proposal. We will assess and adjust as the quarter progresses. If time permits, we plan to explore extensions to historical mapping and classification by broad taxonomic or production groups.

## My Role

I am part of a three-person team working on this project. My specific contributions will be added here as the project progresses.

## Technologies & Methods

**Remote Sensing:** Sentinel-1 (radar), Sentinel-2 (multispectral), satellite image analysis

**Machine Learning:** Pond detection and segmentation, Earth foundation models, baseline models using spectral, temporal, and geometric features

**LLM Validation:** Multimodal large language models for reviewing uncertain detections

**Evaluation:** Precision, recall, F1 score, intersection over union (IoU), geographic cross-validation

**Data:** Existing global and regional aquaculture pond maps (Wang et al., 2022; Ottinger et al., 2022; Jiang et al., 2024)

## Expected Outcomes

- A **high-resolution global map of aquaculture ponds**, with confidence estimates
- A **reproducible mapping pipeline** that can be applied to new regions and time periods
- An assessment of whether **multimodal LLM validation** improves detection quality and reduces false positives

## Contributors

Astoria Li, Iris Li, Dakota Lin.

> Listed in alphabetical order by last name.

This project is part of **ICME Xplore**, led by mentors **Dr. Alex Wiebe** (Postdoctoral Scholar) and **Prof. Sebastian Heilpern** (Assistant Professor) in the Department of Earth System Science at the Stanford Doerr School of Sustainability.

## Proposal

[📄 Download the Project Proposal (PDF)](./Project_Proposal.pdf)

> Detailed results, code, and a full report will be added as the project develops.
