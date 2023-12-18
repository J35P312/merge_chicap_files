variants=data/23,10,06_Raw_Variants.csv
summary=data/23,10,23_Summary_table_ChiCaP_Caros_copy.csv
gene_info=data/23,07_ChiCaP_Research_Gene_Panel_with_constraints_1.csv

output=chicap_analysis.csv

python add_gene_info.py $variants $gene_info > $variants.annotated.csv
python add_sample_info.py $summary $variants.annotated.csv > $output
