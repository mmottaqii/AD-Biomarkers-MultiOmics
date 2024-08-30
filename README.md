# Integrative Multi-Omics Biomarker Discovery for Alzheimer’s Disease

This repository details our research efforts focused on identifying biomarkers for Alzheimer’s Disease (AD) through the integration of multiple omics datasets. Utilizing advanced data processing and machine learning techniques, we aim to uncover novel biomarkers that could lead to improved diagnostic and therapeutic strategies for AD.

## Project Overview

Alzheimer's Disease is a complex neurodegenerative condition characterized by cognitive decline and neuropathological changes. Our project leverages genomic, transcriptomic, and additional omics data to dissect the molecular underpinnings of AD, facilitating the discovery of diagnostic and prognostic biomarkers.

## Repository Structure

- `scripts/`: Contains computational notebooks and scripts for data processing, analysis, and model development.
  - `AD_SHAP_GWAS_dataprocessing.ipynb`: Integrates genomic data with transcriptomic profiles to identify significant biomarkers using SHAP values and GWAS insights.
  - `review_aug_26.ipynb`: Conducts a comprehensive review and analysis of the data processed in August, focusing on PCA analysis of RNA-seq data, merging of datasets, and preparation for further machine learning analysis.
  - `review_july_24.ipynb`: Summarizes the initial preprocessing steps, data integration, and exploratory data analysis conducted in July, setting the stage for in-depth biomarker discovery.
- `assets/`: Includes essential omics data files, notably RNA-seq data, used in the analyses.

## Getting Started

To utilize this repository for research or educational purposes:

1. Clone this repository.
2. Install required dependencies from `requirements.txt`.
3. Execute notebooks within the `scripts/` directory sequentially to replicate or extend the analyses.

## Data Description

This project employs datasets sourced from the Synapse platform, focusing on three major studies:
- ROSMAP (Religious Orders Study and Memory and Aging Project)
- MSBB (Mount Sinai Brain Bank)
- Mayo Clinic Study of Aging

These datasets include comprehensive genomic and transcriptomic data essential for multi-layered biomarker analysis.

## Dependencies

- Python 3.11
- Jupyter
- Pandas
- NumPy
- Scikit-learn
- Matplotlib, Seaborn
- PyTorch (for advanced modeling techniques)

## License

This project is licensed under the MIT License.

## Contact

For inquiries or collaboration proposals, please contact me at mmottaqi@gradcenter.cuny.edu

## Acknowledgments

Thanks to all data providers, collaborators, and institutions that support this research. Special thanks to the funding agencies for their crucial support.
