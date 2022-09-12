import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)
st.sidebar.title('Olympic Data Analysis')

user_menu = st.sidebar.radio(
     'Select an Option',
     ('Medal Tally' , 'Overall Analysis' , 'Athlete-wise-Analysis')
)

if user_menu == 'Medal Tally':
     st.sidebar.title('Medal Tally')
     years,team = helper.country_year_list(df)
     selected_year = st.sidebar.selectbox('select year',years)
     selected_team = st.sidebar.selectbox('select country',team)

     medal_tally = helper.fetch_medal_tally(df,selected_year,selected_team)

     if selected_year == "overall" and selected_team == "overall":
          st.title("Overall Performance")
     if selected_year != "overall" and selected_team == "overall":
          st.title("Performance in " + str(selected_year))
     if selected_year == "overall" and selected_team != "overall":
          st.title("Performance in " + selected_team)
     if selected_year != "overall" and selected_team != "overall":
          st.title("Overall Performance in " + str(selected_year)+" " + selected_team)
     st.table(medal_tally)


if user_menu == 'Overall Analysis':
     edition = df['Year'].unique().shape[0] - 1
     city = df['City'].unique().shape[0]
     sport = df['Sport'].unique().shape[0]
     event = df['Event'].unique().shape[0]
     name = df['Name'].unique().shape[0]
     region = df['region'].unique().shape[0]

     st.title("Top Statistics")
     col1,col2,col3 = st.columns(3)
     with col1:
          st.header("Editions")
          st.title(edition)
     with col2:
          st.header("City")
          st.title(city)
     with col3:
          st.header("Sport")
          st.title(sport)

     col1, col2, col3 = st.columns(3)
     with col1:
          st.header("Event")
          st.title(event)
     with col2:
          st.header("Athletes")
          st.title(name)
     with col3:
          st.header("Region")
          st.title(region)
     st.title(" ")
     st.title("Participating Nation over the Year")
     overtime = helper.overtime(df)
     fig = px.line(overtime, x='edition', y='total_country')
     st.plotly_chart(fig)

     st.title("No of Events over the Year")
     overtim = helper.overtime_event(df)
     figur = px.line(overtim, x='edition', y='total_event')
     st.plotly_chart(figur)


if user_menu == 'Athlete-wise-Analysis':
     st.header("Most Successful Athletes")
     sport = helper.sport_find(df)
     selected_sport = st.sidebar.selectbox('select sport', sport)
     if selected_sport != 'overall':
           successful = helper.most_successful(df,selected_sport)
           st.table(successful)
     else:
          over_succes = helper.most_successful_overall(df)
          st.table(over_succes)
