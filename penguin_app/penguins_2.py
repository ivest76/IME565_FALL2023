import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Palmer’s Penguins")

# Our subtitle
st.markdown("Use this Streamlit app to make your own scatterplot about penguins!")

# Import CSV file provided by user (if not, use default)
penguin_file = st.file_uploader("Select Your Local Penguins CSV (default provided)")
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file) # User provided file
else:
    penguins_df = pd.read_csv("penguins.csv") # Default file

# Select box for x_var
selected_x_var = st.selectbox(
"What do you want the x variable to be?",
["bill_length_mm", "bill_depth_mm", "flipper_length_mm", " body_mass_g"],
)
# Select box for y_var
selected_y_var = st.selectbox(
"What about the y?", ["bill_depth_mm", "bill_length_mm", "flipper_length_mm", "body_mass_g"], )

# Seaborn dark grid theme
sns.set_style("darkgrid")

# Marker shape for each species type
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap": "o"}

# Marker color for each species type
palette = {"Adelie": "green", "Gentoo": "blue", "Chinstrap": "orange"}

# Create scatterplot
#hue defines marker color, style is for marker shape
fig, ax = plt.subplots()
ax = sns.scatterplot(data = penguins_df , x = selected_x_var , y = selected_y_var , hue = "species",
palette = palette , markers = markers , style = "species")
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var) 
plt.title("Scatterplot of Palmer’s Penguins")
st.pyplot(fig)