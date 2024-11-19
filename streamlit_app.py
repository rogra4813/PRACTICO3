import streamlit as st
import pandas as pd
import conda

pip.main(["install" , "openpyxl"])

st.title("🎈 EJERCICIO PRÁCTICO 3   ******GRUPO 6******")
df = pd.read_excel('cryptos.xlsx')

st.write(df)
