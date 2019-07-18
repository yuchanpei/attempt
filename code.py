import wget 
import os
import pandas as pd

d=pd.read_csv('./test_result.csv',usecols=[0])
d.to_csv("./test_assayid.csv",index=False,sep=',')

lines=[]
lines= list(open("./test_assayid.csv", "r", encoding='utf-8').readlines())
a= [s.strip() for s in lines]
assay_ID=[re.sub(r'"','',s) for s in a]

os.remove('./test_assayid.csv')
