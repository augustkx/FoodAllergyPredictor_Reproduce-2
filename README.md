# FoodAllergyPredictor_Reproduce
The operations of each file:

### 1.data-meta.py:
Road in DIABIMMUNE_Karelia_metadata.RData to Python pandas Dataframe. 

Remove all the samples without a food allergy class( egg or milk or peanuts).

Add an "allergy" column, where it indicates "TRUE" if the sample comes from a subject who is allergic to egg, milk, or peanuts, and "FALSE" otherwise.

### 2.data_metagenomics.py

Load diabimmune_karelia_metaphlan_table.txt.

Update OTU table file, only keeping those samples that are in both file.Because we deleted some samples with missing data in meta data.

### 3.data_processing.py

Remove samples from subjects with less than 3 time points.

### 4. genera.py

Draw 215 genera features in diabimmune_karelia_metaphlan_table.txt.
