import pandas as pd
import streamlit as st
import numpy as np

airports = pd.read_csv("airport_location.csv")


##Part 1

st.title("Problem 1: Airport Distance")
st.markdown("Test Haverstine Distance")

selected_latitude_1 = st.number_input("Enter latitude of first location:")
selected_longitude_1 = st.number_input("Enter longitude of first location:")
selected_latitude_2 = st.number_input("Enter latitude of second location:")
selected_longitude_2 = st.number_input("Enter longitude of second location:")

import math

def haversine_formula(selected_latitude_1, selected_longitude_1,
                      selected_latitude_2, selected_longitude_2):
    
    #converting to radians
    lat1 = math.radians(selected_latitude_1)
    lat2 = math.radians(selected_latitude_2)
    long1 = math.radians(selected_longitude_1)
    long2 = math.radians(selected_longitude_2)

    #computing differences
    diff_lat = abs(lat1 - lat2)
    diff_long = abs(long1 - long2)

    a = (math.sin(diff_lat/2))**2 + math.cos(lat1)*math.cos(lat2)*((math.sin(diff_long/2))**2)

    c = 2 * math.atan2(np.sqrt(a), np.sqrt(1-a))

    d = 6371 * c

    return math.trunc(d)


distance = haversine_formula(selected_latitude_1, selected_longitude_1, 
                              selected_latitude_2, selected_longitude_2)

st.write("Your distance is " + str(distance) + " kilometers.")

#Part 2
st.markdown("Identify nearest airports")

selected_airport = st.selectbox("Select airport code", 
                                airports["Airport Code"].values.tolist())

#filtering df and saving selected airport lat and long
airports1 = airports[airports["Airport Code"] == selected_airport]
lat = airports1["Lat"]
long = airports1["Long"]
airports2 = airports[airports["Airport Code"] != selected_airport]

airports2["Distance"] = airports2.apply(lambda x: haversine_formula(lat, long, x["Lat"], x["Long"]), 
                                        axis=1)

airports2.sort_values(by= "Distance", ascending=False, inplace=True)
st.write(airports2)

