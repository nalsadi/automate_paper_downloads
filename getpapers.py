import os 
import pandas as pd 

os.system("pip install PyPaperbot")
str1 = "python -m PyPaperBot --doi="

doi = "10.3390/s20226503"
dir = ' --dwn-dir="PDFs" '

df = pd.read_csv('publistfinal.csv')
print(df.columns)
for doi in df['Unnamed: 2']:
    print(doi)
    os.system( str1 + doi + dir )
