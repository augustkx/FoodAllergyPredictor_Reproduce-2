
import pandas as pd
import numpy as np

otu = pd.read_csv('diabimmune_karelia_metaphlan_table.txt',  delimiter='\t')
meta = pd.read_csv(r'/home/khu/Documents/FoodAllergyPredictor/metagonomics/metadata_h.csv', index_col = 0)
print(otu)
print(meta)
'''
#===========================try to delete samples less than 3 time points before the join
meta['freq'] = meta.groupby('subjectID')['subjectID'].transform('count')
meta=meta.loc[meta.freq>2]#delete in the mta data file
print(meta)
q=meta['subjectID'].value_counts()
print(q)
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#===========================
'''

ind=otu.columns & meta['gid_wgs']
out_new=otu[ind]
meta_new=meta.loc[meta['gid_wgs'].isin(ind)]
print(out_new.shape)
print(meta_new.shape)

#==check subjects=====
q=meta_new['subjectID'].value_counts()
print(q)# 195 subjects, right!
print(q[136])


out_new.to_csv(r'OTU_matrix_2.csv')
meta_new.to_csv(r'metadata_2.csv')
