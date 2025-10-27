import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("ETL Pipeline Dashboard")
engine = create_engine('postgresql+psycopg2://balu:bn@postgres:5432/mydata')
df=pd.read_sql("SELECT * FROM batch1_means",engine)
st.write("Average of Batch1")
st.dataframe(df)