import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Create pandas dataframe to store readings
df = pd.DataFrame(columns=["Date", "Breakfast", "Lunch", "Dinner", "Bedtime"])

# Function to add new reading
def add_reading(breakfast, lunch, dinner, bedtime):
  today = datetime.today().strftime('%Y-%m-%d')
  df = df.append({"Date": today, "Breakfast": breakfast, "Lunch": lunch, "Dinner": dinner, "Bedtime": bedtime}, ignore_index=True)
  st.session_state["df"] = df.to_json()  # Update session state for persistence

# Load data from session state (if available)
if "df" in st.session_state:
  df = pd.read_json(st.session_state["df"])

# Setup Main Page Area
st.set_page_config(layout="wide")
st.title('**Blood Sugar Tracker**')

with st.expander('About this app'):
    st.write('Enter you blood suagr readings through the day, the app will automatically\n'
            'show your bood sugar readings for the last 25 days.'
            'show your last weekly and monthly average (compqared to previous)'
             'and a graph of your daily averages.')
    st.write('Email seany42@gmail.com with any feedback, or raise an issues on GitHub https://github.com/PositivePython42/PandOura/issues')


# Input fields for readings
breakfast = st.number_input("Breakfast", min_value=0, format=%d)
lunch = st.number_input("Lunch", min_value=0, format=%d)
dinner = st.number_input("Dinner", min_value=0, format=%d)
bedtime = st.number_input("Bedtime", min_value=0, format=%d)

# Button to submit reading
if st.button("Record Reading"):
  add_reading(breakfast, lunch, dinner, bedtime)
  st.success("Sucessfully Recorded!")

# Display the last 20 days of readings
filtered_df = df[df["Date"] >= (datetime.today() - timedelta(days=20))]
st.subheader("Last 20 Days Readings")
st.dataframe(filtered_df)

# Explanation about reading interpretation (optional)
st.write("Always Seek Medical Advice About Your Blood Sugar Readings.")
