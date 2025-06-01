import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('E-commerce Company Insights')
st.write('Here is our LLM generated dashboard')
import matplotlib.pyplot as plt

# Data
countries = ['Brasil', 'Japan', 'United States', 'Colombia', 'Spain', 'China', 'Australia', 'France', 'Germany', 'Belgium', 'South Korea', 'Poland', 'United Kingdom']
users = [2676, 432, 3963, 3, 726, 6000, 327, 894, 771, 192, 960, 51, 699]

# Plotting
plt.figure(figsize=(10, 8))
plt.barh(countries, users, color='skyblue')
plt.xlabel('Number of Users')
plt.ylabel('Country')
plt.title('Number of Users Coming via Facebook by Country')
plt.tight_layout()

st.pyplot()
