# Caching in Streamlit
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import time

st.title("Palmer’s Penguins")
st.markdown("Use this Streamlit app to make your own scatterplot about penguins!")
# Import CSV file provided by user (if not, use default)
penguin_file = st.file_uploader("Select Your Local Penguins CSV (default provided)")
# We create a function called load_file()
# It waits 3 seconds and then loads the file that we need
def load_file(penguin_file): 
    time.sleep(6)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv("penguins.csv")
    return(df)

penguins_df = load_file(penguin_file)
# Insert remaining code from the previous gender-based app

# Select box for gender
selected_gender = st.selectbox("What gender do you want to analyze?", 
                               ["male", "female"], )

# Select box for x_var
selected_x_var = st.selectbox("What do you want the x variable to be?", 
                              ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", 
                               "body_mass_g"], )

# Select box for y_var
selected_y_var = st.selectbox( "What about the y?",
                              ["bill_depth_mm", "bill_length_mm", "flipper_length_mm", 
                               "body_mass_g"],)

# Filter by gender
penguins_df = penguins_df[penguins_df["sex"] == selected_gender]

# Create scatterplot
fig, ax = plt.subplots()
ax = sns.scatterplot(x = penguins_df[selected_x_var], 
                     y = penguins_df[selected_y_var], 
                     hue = penguins_df["species"],
                     style = penguins_df["species"])

plt.xlabel(selected_x_var) 
plt.ylabel(selected_y_var)
plt.title("Scatterplot of Palmer's Penguins") 
st.pyplot(fig)

