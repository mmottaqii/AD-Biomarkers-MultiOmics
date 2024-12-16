# Set default library paths
.libPaths(c("/home/vmottaqi/.conda/envs/renv_1/lib/R/library"))

library(Matrix)
library(ggplot2)
library(Seurat)
library(data.table)
library(dplyr)
library(sctransform)


data_rds <- readRDS("~/oud_rnaseq/GSE240457_filtered_samples_genes_Dec924.rds")
print("rds file loaded successfully!")


# Place this line before running SCTransform
options(future.globals.maxSize = 6000 * 1024^2)  # Set to 4 GB, adjust as necessary


print("starting scTransform")

data_rds <- SCTransform(
  object = data_rds, 
  assay = "RNA",
  reference.SCT.model = NULL,
  do.correct.umi = TRUE, 
  new.assay.name = "SCT",
  ncells = 5000,
  residual.features = NULL,
  variable.features.n = 5000,
  vars.to.regress = c('percent.mt', 'Batch', 'nCount_RNA'),
  do.scale = FALSE,
  do.center = FALSE,
  vst.flavor = "v2",
  conserve.memory = TRUE,
  seed.use = 1998,
  verbose = TRUE, 
  return.only.var.genes = FALSE
)


print("scTransform Done!, now saving the rds file")

saveRDS(data_rds, "~/oud_rnaseq/GSE240457_normalized_SCT_Dec1024_5kgenes.rds")
print("File Saved!")


