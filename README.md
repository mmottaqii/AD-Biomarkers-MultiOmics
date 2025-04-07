# PRISM-ML: Integrating Interpretable Machine Learning and Multi-Omics Systems Biology for Alzheimer’s Disease

This repository contains the code and analyses for our paper on the PRISM-ML framework, which integrates interpretable machine learning and multi-omics data to identify patient-specific biomarkers and potential drug repurposing candidates in Alzheimer’s Disease (AD). Our goal is to uncover novel biomarkers and disease mechanisms that can guide more effective diagnostic and therapeutic strategies.

![PRISM-ML Pipeline](figures/Fig1.png)

## Project Overview

Alzheimer’s Disease (AD) is a multifactorial neurodegenerative condition, characterized by complex molecular changes in the brain. Our project employs bulk RNA-seq data and genomic variants from multiple large-scale AD studies to:

- Identify patient-level and subtissue-specific biomarkers using a Random Forest classifier with SHAP (interpretable machine learning).
- Build network models to find critical “bottleneck” genes that link genetic risk factors and expression-based biomarkers.
- Explore multi-target drug repurposing strategies by systematically querying knowledge graphs and validating candidates in real-world data.

## Repository Structure

- **scripts/**: Contains computational notebooks for data processing, analysis, and figure generation.
  - **Part1_RNAseq_data_ML_clustering_biomarkers.ipynb**  
    Implements data loading, cleaning, and interpretable machine learning (Random Forest + SHAP) to identify patient-level AD biomarkers.
  - **Part2_genomics_network_analysis_drug_repurposing.ipynb**  
    Performs network construction, identifies “bottleneck” genes, and carries out a knowledge-graph-based drug repurposing analysis.
  - **Figures_tables_final_statistics.ipynb**  
    Gathers results, generates final figures and tables used in the paper, and calculates summary statistics across tissues.
    
- **figures/**: Stores static resources and figures for this repository.


## Getting Started

To replicate or extend the analysis presented here:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/PRISM-ML_AD_Analysis.git
   cd PRISM-ML_AD_Analysis
  
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
