# Data Visualization: SF Trees
# Using PyDeck - Part 1
import streamlit as st
import pandas as pd
import pydeck as pdk 

st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'
         ' a dataset kindly provided by SF DPW')
trees_df = pd.read_csv('trees.csv')

# Removing null values before mapping
trees_df.dropna(how = 'any', inplace = True)

# Creating a base map of SF with city center (37.77, -122.4)
# Defining initial state/base map
sf_initial_view = pdk.ViewState(
    latitude = 37.77,
    longitude = -122.4,
    zoom = 11,
    pitch = 30
    )

# Adding layers to base map
# Option 1: Displaying trees as scatter points
sp_layer = pdk.Layer(
    'ScatterplotLayer',
    data = trees_df,
    get_position = ['longitude', 'latitude'],
    get_radius = 30)

# Option 2: Hexagon layer, colored based on the density of trees
hx_layer = pdk.Layer(
    'HexagonLayer',
    data = trees_df,
    get_position = ['longitude', 'latitude'],
    radius = 100,
    extruded = True)

# Using light map style for better visibility
st.pydeck_chart(pdk.Deck(
    map_style = 'mapbox://styles/mapbox/light-v9',
    initial_view_state = sf_initial_view, # base map
    layers = [hx_layer] # select the layer to display
    ))