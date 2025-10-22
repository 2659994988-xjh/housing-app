import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()
st.title('California Housing Data Analysis')

df = pd.read_csv('housing.csv')
# note that you have to use 0.0 and 40.0 given that the data type of populatio

population_filter = st.slider('Minimal Median House Price:', 0, 500001,200000)  # mi
# min, max, default
# create a multi select
capital_filter = st.sidebar.multiselect(
                        'Choose the location type',
                        df.ocean_proximity.unique(),  # options
                        df.ocean_proximity.unique())  # defaults
 # create a ratio button
form = st.sidebar.radio("Choose income level",
['Low', 'Medium', 'High']
)
# filter by population
if form == 'Low':
    df = df[df.median_income <= 2.5]
elif form == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income <= 4.5)]
else:
    df = df[df.median_income > 4.5]
# filter by capital
st.subheader('See more fliters in the sidebar:')#添加小标题
# show on map
st.map(df)

# show the plot

fig, ax = plt.subplots(figsize=(20,5))
a = df.median_house_value
a.plot.hist(ax=ax,bins=30)
st.pyplot(fig)