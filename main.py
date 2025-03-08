# import streamlit as st
# from datetime import datetime
# from zoneinfo import ZoneInfo


# TIME_ZONES = [
#     "UTC",
#     "Asia/Karachi",
#     "America/New_York",
#     "Europe/London",
#     "Asia/Tokyo",
#     "Australia/Sydney",
#     "America/Los_Angeles",
#     "Europe/Berlin",
#     "Asia/Dubai",
#     "Asia/Kolkata"
# ]

# st.title("Time Zone App")

# selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

# st.subheader("Slected Timezones")

# for tz in selected_timezone:
#     current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
#     st.write(f"**{tz}**: {current_time}")


# st.subheader("Convert Time Between Timeszones")

# current_time = st.time_input("Current Time", value=datetime.now().time())

# from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

# to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# if st.button("Convert"):
#     dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    
#     converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    
#     st.success(f"Converted Time in {to_tz}: {converted_time}")

import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata"
]

st.title("Time Zone App")

selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.subheader("Selected Timezones")

for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

st.subheader("Convert Time Between Timezones")

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Default time from selected 'from_tz'
default_time = datetime.now(ZoneInfo(from_tz)).time()
current_time = st.time_input("Current Time", value=default_time)

if st.button("Convert"):
    dt = datetime.combine(datetime.today(), current_time)
    dt = dt.replace(tzinfo=ZoneInfo(from_tz))  # Set timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    
    st.success(f"Converted Time in {to_tz}: {converted_time}")
