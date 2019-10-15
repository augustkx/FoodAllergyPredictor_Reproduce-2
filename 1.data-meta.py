
import pyreadr
result = pyreadr.read_r('DIABIMMUNE_Karelia_metadata.RData') # also works for Rds
# result is a dictionary where keys are the name of objects and the values python objects
print(result.keys()) #  check what objects we got
df = result["metadata"] # extract the pandas data frame for object df1
#print(result.index)
#print(df.columns)
print(df)
df1 = df[['subjectID','gid_wgs','country', 'age_at_collection','allergy_milk', 'allergy_egg','allergy_peanut']]
print(df1)
df1=df1.dropna(subset=['gid_wgs', 'allergy_milk', 'allergy_egg','allergy_peanut'])
print(df1)

#Add an "allergy" column, where it indicates "TRUE" if the sample comes from a subject who is allergic to egg, milk, or peanuts,
# and "FALSE" otherwise.
df1['allergy'] =( (df1['allergy_milk'] ==1)| (df1[ 'allergy_egg']==1) | (df1['allergy_peanut']==1))
df1 = df1[['subjectID','gid_wgs','country', 'age_at_collection','allergy']]
print(df1)





df1.to_csv(r'metadata_h.csv')