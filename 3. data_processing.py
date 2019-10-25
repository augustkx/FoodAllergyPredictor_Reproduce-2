import pandas as pd
import numpy as np

otu = pd.read_csv('OTU_matrix_2.csv',  index_col = 0)
meta = pd.read_csv(r'metadata_2.csv', index_col = 0)

# Remove samples from subjects with less than 3 time points.
#resulting in 658 samples??
print(meta)
meta['freq'] = meta.groupby('subjectID')['subjectID'].transform('count')
meta_new=meta.loc[meta.freq>2]#delete in the meta data file
print(meta_new)#641-1=640,but in the paper the number is 658!!!???
q=meta_new['subjectID'].value_counts()
print(q)#137 subjects, but in the paper, the numner is 148!!!???
meta_new.drop(columns='freq', inplace=True)

#delete in the OTU files=====================
ind=otu.columns & meta_new['gid_wgs']
out_new=otu[ind]
print(out_new)
print(meta_new)

#==check country summary.===
s=meta_new.groupby('country')['subjectID'].value_counts()
print(s)
s2=meta_new.groupby('country')['country'] .value_counts()
print(s2)


out_new.to_csv(r'OTU_matrix.csv')
meta_new.to_csv(r'metadata.csv')