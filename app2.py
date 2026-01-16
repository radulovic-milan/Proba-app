import streamlit as st
import pandas as pd

st.title("Kalkulator")

st.write("---")

num1 = st.number_input(label="First number")

num2 = st.number_input (label="Second number")

st.write("Operation")

operation = st.radio("Select:",("Add","Substract"))


ans = 0

def calculate():
    if operation == "Add": 
     ans = num1 + num2
    elif operation == "Substract": 
     ans = num1 - num2
    st.success(f"Answer = {ans}")
        
if st.button("Calculate"): 
        calculate()
        




