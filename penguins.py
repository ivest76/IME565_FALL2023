# Import packages
import streamlit as st
import pandas as pd

# Create a title for our app
st.title("Palmer’s Penguins")

# Import data
penguins_df = pd.read_csv("penguins.csv")

# Display rows using st.write() function
st.write(penguins_df.head())

# Import packages
import matplotlib.pyplot as plt 
import seaborn as sns

# Main title of the app
st.title("Palmer’s Penguins")

# Our subtitle
#NOTE: st.markdown() enables the use of Markdown, a markup language
# especially useful for writing math equations
st.markdown("Use this Streamlit app to make your own scatterplot about penguins!")

# Select box for species
#selected_species = st.selectbox(
#"What species would you like to visualize?", # First comes the message/question
#["Adelie", "Gentoo", "Chinstrap"], # Then the options within a list
# )

# Select box for x_var
selected_x_var = st.selectbox(
"What do you want the x variable to be?",
["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"], )

# Select box for y_var
selected_y_var = st.selectbox(
"What about the y?",
["bill_depth_mm", "bill_length_mm", "flipper_length_mm", "body_mass_g"], )


# Import data
penguins_df = pd.read_csv("penguins.csv")
# Filter by species
#penguins_df = penguins_df[penguins_df["species"] == selected_species]

# Create scatterplot
fig, ax = plt.subplots()
ax = sns.scatterplot(x = penguins_df[selected_x_var], 
                     y = penguins_df[selected_y_var], 
                     hue = penguins_df["species"], 
                     style = penguins_df["species"])
#sns.se
plt.xlabel(selected_x_var) 
plt.ylabel(selected_y_var)
plt.title("Scatterplot of Palmer's Penguins") 
st.pyplot(fig)

