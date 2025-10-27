import os
import sys
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Read input CSV (e.g., gene expression data)
input_file = sys.argv[1]
batch_name = os.path.basename(input_file).replace(".csv","")
data = pd.read_csv(input_file)
# Calculate mean of numeric columns
result = data.select_dtypes(include='number').mean()
# Save result to output CSV
os.makedirs('/app/output', exist_ok=True)
output_file = f'/app/output/{batch_name}_output.csv'
result.to_csv(output_file)
print(f"Processed data and saved to output.csv") #this will be captured by the docker logs command
#postgres connection 
table_name = f'{batch_name}_means'
engine = create_engine('postgresql+psycopg2://balu:bn@postgres:5432/mydata')
result.to_sql(table_name, engine, if_exists='replace',index=True)
print(f"Result stored in the postgres table {table_name}")