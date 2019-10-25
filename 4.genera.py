#draw 215 genera
import pandas as pd
import numpy as np

otu = pd.read_csv('OTU_matrix.csv',  index_col = 0)
otu_=pd.read_csv('OTU_matrix.csv')
#meta = pd.read_csv(r'metadata.csv', index_col = 0)
#print(meta)
#df = otu[(otu.T != 0.0).any()]delete the row that are 0 for all samples. No such microbiome exist in samples.
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #print(df.iloc[0:50,0:2])
p=otu.iloc[:,0:0]
p.to_csv(r'vis.txt', header=False)
#======================
#save the taxonomic path, and split into kimdom,phylum, class, order, family,  genus, species.

tax=pd.read_csv('vis.txt',sep='|', names=["k", "p", "c", "o","f","g","s"])
#print(tax)
tax.to_csv(r'tax.txt')
#=======================
tax2=pd.read_csv('tax.txt')
tax_g=tax2[['g','s']]
#print(tax_g)
#select those that is not NaN at 'g',and NaN at 's'
tax_g=tax_g[tax_g['g'].notnull()]
tax_g=tax_g[pd.isnull(tax_g['s'])]
#print(tax_g)

otu_new = otu_[otu_.index.isin(tax_g.index)]
print(otu_new)

otu_new.to_csv(r'OTU_final.csv',index=False)


