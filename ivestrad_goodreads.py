import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import math


reads = pd.read_csv("goodreads_history.csv")

st.title("Goodreads User Analytics")

st.subheader("How many books does the user read each year?")

#converting to datetime to get years
reads["Year"] = pd.DatetimeIndex(reads["Date Read"]).year
reads["Year"] = reads["Year"].astype(float)
reads["Year"].value_counts()

#creating bar plot to showcase number of books
Years = ["2018", "2019", "2020", "2021"]
Books = [1, 48, 71, 19]

df = pd.DataFrame(list(zip(Years, Books)), columns= ['Years', 'Books'])

plt.bar(df['Years'], df['Books'], color = 'hotpink')
plt.ylabel('Number of Books')
plt.xlabel('Year')
plt.title('Reading Frequency from 2018-21')
st.pyplot(plt)
st.write("The user read 1 book in 2018, 48 books in 2019, 71 books in 2020, "
         "and 19 books in 2021. It could be that the large spike in reading "
         "was affected by the COVID-19 lockdown in 2020, so the user had "
         "more downtime.")


st.subheader("How long does it take for the user to finish a book that they started?")

#converting date added and date read to date types 
reads["Date Added"] = pd.to_datetime(reads['Date Added'])
reads["Date Read"] = pd.to_datetime(reads['Date Read'])

#subtracting to get number of days
reads["reading_time"] = reads["Date Read"] - reads["Date Added"]

#getting rid of days string so convert back to float. cant do int
#since there are obs with no values
reads["reading_time"] = reads["reading_time"].dt.days.astype(float)
#did this because there was a negative value, one of the dates may have been switched
reads["reading_time"] = abs(reads["reading_time"])

#average and histogram to describe trends and centrality
fig2, ax2 = plt.subplots()
ax2 = plt.hist(reads['reading_time'], color='skyblue')
plt.xlabel("Number of Days")
plt.ylabel("Frequency")
plt.title("Distribution of Reading Times for 2018-2021")
st.pyplot(fig2)
st.write("On average, it takes the user 131 days to read a book. This makes sense "
         "when we look at the next graph and analyze book lengths. Additionally, "
         "since we have reading times going into the 800s, it could be that "
         "the user was reading multiple books at a time or started reading "
         "a book and had to come back to it.")


st.subheader("How long are the books that the user has read?")

#doing a histogram again 
fig3, ax3 = plt.subplots()
ax3 = plt.hist(reads["Number of Pages"], color='mediumorchid')
plt.xlabel("Number of Pages")
plt.ylabel("Frequency")
plt.title("Distribution of Book Lengths for 2018-2021")
st.pyplot(fig3)
st.write("On average, the user's books are around 346 pages long. The "
         "distribution of book lengths could be related to the "
         "distribution of reading times since both are right skewed. "
         "Although reading times have a stronger tail than book lengths, "
         "this could be impacted by the lack of dates for creating the "
         "previous graph.")


st.subheader("How old are the books that the user has read?")

#creating a new data frame because I have some missing values for year published
#and i dont want to return a 2023 year old book. not the most efficient way to do this?
years = pd.DataFrame()
years["Year"] = reads["Year Published"].dropna()
years["Year"] = years["Year"].astype(int)
years["Age"] = 2023 - years["Year"]

#another one
fig4, ax4 = plt.subplots()
ax4 = plt.hist(years["Age"], color='darkcyan')
plt.title("Distribution of Book Ages")
plt.xlabel("Years")
plt.ylabel("Frequency")
st.pyplot(fig4)
st.write("On average, the books the user reads are about 12 years old. "
         "The distribution of ages is skewed right since they prefer "
         "newer books.")