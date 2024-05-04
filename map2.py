import streamlit as st
import pandas as pd
import pydeck as pdk

@st.cache_data
def load_data():
    # Load your data from a CSV file
    data = pd.read_csv('extracted_coordinates.csv')
    return data

def create_pydeck_map(data):
    # Define the initial view state of the map
    view_state = pdk.ViewState(
        latitude=data['Latitude'].mean(),
        longitude=data['Longitude'].mean(),
        zoom=12,
        pitch=50
    )

    # Create a layer for the 3D scatter plot
    layer = pdk.Layer(
        "ScatterplotLayer",
        data,
        get_position=['Longitude', 'Latitude'],
        get_color='[200, 30, 0, 160]',  # RGBA color format: Red with some transparency
        get_radius=30,  # Radius is measured in meters
    )

    # Create the deck.gl map
    deck_map = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style='mapbox://styles/mapbox/light-v9'
    )

    return deck_map

def main():
    st.title("Interactive Map of Potholes")
    data = load_data()
    deck_map = create_pydeck_map(data)
    st.pydeck_chart(deck_map)

if __name__ == "__main__":
    main()
