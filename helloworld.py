import streamlit as st
import pandas as pd
import folium
 
st.write("""
# My first app
Hello *world!*
""")
 
#df = pd.read_csv("my_data.csv")
#st.line_chart(df)

uploaded_file = st.file_uploader("Upload CSV", type=".csv")
st.markdown("### Data preview")
st.dataframe(df.head())

# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)

