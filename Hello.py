import streamlit as st
import requests

st.title("Air Quality and Temperature Checker")

city_name = st.text_input("Enter City Name", " ")
api_key = "20603187918692cee3d46974dd9d53db6cc40084"

# Construct API URL
url = f"https://api.waqi.info/feed/{city_name}/?token={api_key}"

# Make the request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse JSON response
    json_data = response.json()
    
    # Extract AQI data
    aqi = json_data['data']['aqi']
    
    # Extract temperature data
    temperature = json_data['data']['iaqi'].get('t', {}).get('v', 'N/A')
    
    # Extract other details
    city = json_data['data']['city']['name']
    country = json_data['data']['city'].get('country',  'INDIA')  # country name 
    dominant_pollutant = json_data['data'].get('dominentpol', 'N/A')  # Use .get() to handle KeyError
    
    # Display the details
    st.write(f"**City:** {city}, **Country:** {country}")
    st.write(f"**Air Quality Index (AQI):** {aqi}")
    st.write(f"**Temperature:** {temperature}°C")
    st.write(f"**Dominant Pollutant:** {dominant_pollutant}")
else:
    st.error("Failed to retrieve data. Please check your API key or city name.")
