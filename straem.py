import pandas as pd
import streamlit as st
import numpy as np
import folium
from streamlit_folium import st_folium

st.title("Local SDG Tracker")

# Deed와 Event 추가 함수
def add_deed():
    deed_date = st.date_input('Date of Good Deed')
    sdg_type = st.selectbox('Sustainable Development Goal', 
        ['1. No Poverty', '2. Zero Hunger', '3. Good Health and Well-being', 
         '4. Quality Education', '5. Gender Equality', '6. Clean Water and Sanitation', 
         '7. Affordable and Clean Energy', '8. Decent Work and Economic Growth', 
         '9. Industry, Innovation, and Infrastructure', '10. Reduced Inequality', 
         '11. Sustainable Cities and Communities', '12. Responsible Consumption and Production', 
         '13. Climate Action', '14. Life Below Water', '15. Life on Land', 
         '16. Peace and Justice Strong Institutions', '17. Partnerships to achieve the Goal'])
    deed_description = st.text_input('Description of Good Deed')
    deed_lat = st.number_input('Latitude of Good Deed')
    deed_long = st.number_input('Longitude of Good Deed')
    add_deed_button = st.button('Add Deed')

    if 'deed_lats' not in st.session_state:
        st.session_state.deed_lats = []
    if 'deed_longs' not in st.session_state:
        st.session_state.deed_longs = []

    if add_deed_button:
        st.session_state.deed_lats.append(deed_lat)
        st.session_state.deed_longs.append(deed_long)
        st.success('Deed added!')

def add_event():
    event_name = st.text_input('Name of Event')
    event_date = st.date_input('Date of Event')
    event_description = st.text_input('Description of Event')
    event_lat = st.number_input('Latitude of Event')
    event_long = st.number_input('Longitude of Event')
    add_event_button = st.button('Add Event')

    if 'event_lats' not in st.session_state:
        st.session_state.event_lats = []
    if 'event_longs' not in st.session_state:
        st.session_state.event_longs = []

    if add_event_button:
        st.session_state.event_lats.append(event_lat)
        st.session_state.event_longs.append(event_long)
        st.success('Event added!')

# 시작 버튼
start_button = st.checkbox('Start')

if start_button:
    deed_dict = {'Deed Date': [], 'Deed Type': [], 'Deed Description': [], 'Deed Lat': [], 'Deed Long': []}
    event_dict = {'Event Name': [], 'Event Date': [], 'Event Description': [], 'Event Lat': [], 'Event Long': []}
    
    main_map = folium.Map(location=[0, 0], zoom_start=2)

    if st.checkbox("Add a Deed"):
        add_deed()
        
    if st.checkbox("Add an Event"):
        add_event()

    if st.checkbox("Show Map"):
        for i in range(len(st.session_state.get('deed_lats', []))):
            folium.Marker([st.session_state.deed_lats[i], st.session_state.deed_longs[i]], popup='Good Deed').add_to(main_map)
        
        for i in range(len(st.session_state.get('event_lats', []))):
            folium.Marker([st.session_state.event_lats[i], st.session_state.event_longs[i]], popup='Event').add_to(main_map)
        
        map = st_folium(main_map)
