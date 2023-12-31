# Data Visualization: SF Trees
# Using Matplotlib and Seaborn: Static Visualizations
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'
         ' a dataset kindly provided by SF DPW')

# Loading dataset
trees_df = pd.read_csv('trees.csv')

# Extracting the age of each tree in days
# Create a new column 'age' which stores the 
# difference tree planting date and today
trees_df['age'] = (pd.to_datetime('today') -
                   pd.to_datetime(trees_df['date'])).dt.days


# Distribution of age - Seaborn Histogram
st.subheader('Seaborn Chart')
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_sb)

# Distribution of age - Matplotlib Histogram
st.subheader('Matploblib Chart')
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_mpl)

# NOTE: st.pyplot() is used to insert each graph onto our Streamlit app 