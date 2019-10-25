
import pandas as pd
import numpy as np

otu = pd.read_csv('diabimmune_karelia_metaphlan_table.txt',  delimiter='\t',index_col = 0)
meta = pd.read_csv(r'metadata_h.csv',index_col = 0)
ind=otu.columns & meta['gid_wgs']#keep those samples that are in both file, mainly because the missing data of allergy in metafile.
print(ind)
otu_new=otu[ind]
meta_new=meta.loc[meta['gid_wgs'].isin(ind)]
print(otu_new)
print(meta_new.shape)
print(otu_new.count())
#print(otu_new[otu_new.columns[0]])
#print('----------------------------')
#df = otu_new[(otu_new.T != 0.0).any()]
#print(df)
#==check subjects=====
q=meta_new['subjectID'].value_counts()
print(q)# 195 subjects, right!
print(q[136])
#==check country summary.===
s=meta_new.groupby('country')['subjectID'].value_counts()
print(s)
s2=meta_new.groupby('country')['country'] .value_counts()
print(s2)

#df1.drop(columns='freq', inplace=True)


otu_new.to_csv(r'OTU_matrix_2.csv')
meta_new.to_csv(r'metadata_2.csv')
