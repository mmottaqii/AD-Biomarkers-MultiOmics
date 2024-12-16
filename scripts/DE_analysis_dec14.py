# Set default library paths
.libPaths(c("/home/vmottaqi/.conda/envs/renv_1/lib/R/library"))

library(Matrix)
library(ggplot2)
library(Seurat)
library(data.table)
library(dplyr)
library(MAST)

# Load data
data_rds <- readRDS("~/oud_rnaseq/OUD_SCT_Dec1024_scaledvis.rds")

# Correct column renaming from 'Batch' to 'Diagnosis'
colnames(data_rds@meta.data)[colnames(data_rds@meta.data) == "Batch"] <- "Diagnosis"

# Change the values within the 'Diagnosis' column
data_rds@meta.data$Diagnosis <- ifelse(data_rds@meta.data$Diagnosis == "Mash", "ctrl", "OUD")

# Create new column for combined cell type and diagnosis
data_rds@meta.data$celltype_diagnosis <- paste(data_rds@meta.data$celltype, data_rds@meta.data$Diagnosis, sep = "_")

# Set identities based on celltype and diagnosis
Idents(data_rds) <- "celltype_diagnosis"

# Extract unique cell types
unique_cell_types <- unique(sub("_.*", "", data_rds@meta.data$celltype))

# Initialize list for results
results_list <- list()

# Differential expression analysis for each cell type
for (cell_type in unique_cell_types) {
    ident1 <- paste(cell_type, "OUD", sep = "_")
    ident2 <- paste(cell_type, "ctrl", sep = "_")
    
    # Run differential expression
    de_results <- FindMarkers(data_rds, 
                              assay = "SCT", 
                              ident.1 = ident1, 
                              ident.2 = ident2, 
                              verbose = TRUE, 
                              test.use = "MAST", 
                              logfc.threshold = 0.2, 
                              min.pct = 0.01, 
                              random.seed = 1376, 
                              densify = TRUE)
    
    # Add the cell type as a new column
    de_results$celltype <- cell_type
    
    # Append the results to the list
    results_list[[cell_type]] <- de_results
}

# Combine all results into one dataframe
final_results <- do.call(rbind, results_list)

# Save results to CSV
write.csv(final_results, "~/oud_rnaseq/DE_Results_All_CellTypes_Dec152024.csv", row.names = FALSE)
