import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

df = pd.read_csv("notebooks/suicide_dataset-11.csv")
df = df.replace({'Yes': True, 'No': False})
df2015 = df[df["year"] == 2015]
df2015g = df2015[df2015["sex"] != "Both"]
df2015b = df2015[df2015["sex"] == "Both"]
df2016 = df[df["year"] == 2016]
df2016g = df2016[df2016["sex"] != "Both"]
df2016b = df2016[df2016["sex"] == "Both"]

st.title("What accommodations best prevent suicide?")

# And now we make things with our things
st.write("The dataset I used covered 2015 and 2016. In the analysis, I focussed on 2016 for being more recent and having more data to work with. The numbers by country weren't very different.")
yrbutton = st.radio("Year", ("2015", "2016"))

if yrbutton == "2015":
    world = px.choropleth(df2015b, projection="winkel tripel", locations="iso", color="suicide_rate", color_continuous_scale=px.colors.sequential.Bluered)
    hist = px.histogram(df2015b, x="suicide_rate")

if yrbutton == "2016":
    world = px.choropleth(df2016b, projection="winkel tripel", locations="iso", color="suicide_rate", color_continuous_scale=px.colors.sequential.Bluered)
    hist = px.histogram(df2016b, x="suicide_rate")

st.plotly_chart(world)

st.write("If it looks like there are more countries with lower rates, it's because there are.")
st.plotly_chart(hist)

st.write("I looked at most of the variables the dataset had to offer, and of all the scatterplots I made for 2016, there were two with an R² that was even over .05, and the one with the bigger one had a positive trend. Here they are. First for the number of mental hospitals per 100 000 people:")
mentalh_g = st.checkbox("Gendered", key="mentalh")

if mentalh_g:
    if yrbutton == "2015":
        mentalh = px.scatter(df2015g[df2015g["mental_hospitals_per_100k"] < 0.5], x="mental_hospitals_per_100k", y="suicide_rate", trendline="ols", color="sex")
    if yrbutton == "2016":
        mentalh = px.scatter(df2016g[df2016g["mental_hospitals_per_100k"] < 0.5], x="mental_hospitals_per_100k", y="suicide_rate", trendline="ols", color="sex")
else:
    if yrbutton == "2015":
        mentalh = px.scatter(df2015b[df2015b["mental_hospitals_per_100k"] < 0.5], x="mental_hospitals_per_100k", y="suicide_rate", trendline="ols")
    if yrbutton == "2016":
        mentalh = px.scatter(df2016b[df2016b["mental_hospitals_per_100k"] < 0.5], x="mental_hospitals_per_100k", y="suicide_rate", trendline="ols")
st.plotly_chart(mentalh)

st.write("And here for psychiatrists:")
psyiatr_g = st.checkbox("Gendered", key="psyiatr")

if psyiatr_g:
    if yrbutton == "2015":
        psyiatr = px.scatter(df2015g[df2015g["psychiatrists_per_100k"] < 2], x="psychiatrists_per_100k", y="suicide_rate", trendline="ols", color="sex")
    if yrbutton == "2016":
        psyiatr = px.scatter(df2016g[df2016g["psychiatrists_per_100k"] < 2], x="psychiatrists_per_100k", y="suicide_rate", trendline="ols", color="sex")
else:
    if yrbutton == "2015":
        psyiatr = px.scatter(df2015b[df2015b["psychiatrists_per_100k"] < 2], x="psychiatrists_per_100k", y="suicide_rate", trendline="ols")
    if yrbutton == "2016":
        psyiatr = px.scatter(df2016b[df2016b["psychiatrists_per_100k"] < 2], x="psychiatrists_per_100k", y="suicide_rate", trendline="ols")
st.plotly_chart(psyiatr)
st.write("You can see what I mean with the \"not as much data\" thing.")