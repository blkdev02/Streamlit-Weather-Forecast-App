import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                    ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place} ")

if place:

    try:
        # Get the temperature/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [temp_list["main"]["temp"] /10 for temp_list in filtered_data]
            print(temperatures)
            dates = [dates["dt_txt"] for dates in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [sky_weather["weather"][0]["main"] for sky_weather in filtered_data]
            sky_images = {"Clear": "images/clear.png", "Rain": "images/rain.png", "Clouds": "images/cloud.png",
                            "Snow": "images/snow.png"}
            image_paths = [sky_images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("Error: City Not Found. Please try again.")

