import os
import sys
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Read input CSV (e.g., gene expression data)
data = pd.read_csv(sys.argv[1])
# Calculate mean of numeric columns
result = data.select_dtypes(include='number').mean()
# Save result to output CSV
os.makedirs('/app/output', exist_ok=True)
result.to_csv('/app/output/output.csv')
print("Processed data and saved to output.csv") #this will be captured by the docker logs command
#postgres connection 
engine = create_engine('postgresql+psycopg2://balu:bn@postgres:5432/mydata')
result.to_sql('means', engine, if_exists='replace',index=True)
print("result variabe is stored in the mydata postgres database as means table")