# interactive_story_selection.py

import streamlit as st
from meta_ai_api import MetaAI

# Initialize the MetaAI language model
ai = MetaAI()

# Define predefined lists for each category
character_names = ["Bunny", "Fox", "Lion", "Elephant", "Tiger"]
character_types = ["rabbit", "fox", "lion", "elephant", "tiger"]
locations = ["forest", "jungle", "desert", "mountains", "savannah"]
objects_found = ["shiny stone", "mysterious box", "old map", "ancient book", "glowing orb"]
location_features = ["sparkling brook", "tall mountain", "hidden cave", "deep valley", "mystic lake"]

# Sidebar for choosing elements
st.sidebar.header("Choose Story Elements")

# Selectboxes to choose different elements for the story
selected_character_name = st.sidebar.selectbox("Choose Character Name", character_names)
selected_character_type = st.sidebar.selectbox("Choose Character Type", character_types)
selected_location = st.sidebar.selectbox("Choose Location", locations)
selected_object_found = st.sidebar.selectbox("Choose Object Found", objects_found)
selected_location_feature = st.sidebar.selectbox("Choose Location Feature", location_features)

# Main content area to display the selected elements
st.title("Interactive Story Generator")
st.write("Select different elements from the sidebar to build your story!")

# Display the selected elements
st.subheader("Selected Elements:")
st.write(f"**Character Name:** {selected_character_name}")
st.write(f"**Character Type:** {selected_character_type}")
st.write(f"**Location:** {selected_location}")
st.write(f"**Object Found:** {selected_object_found}")
st.write(f"**Location Feature:** {selected_location_feature}")



# Button to invoke the language model and enhance the story
if st.button("Craft my Story!"):
    st.session_state.story_template = f"""
    Once upon a time, in a {selected_location}, there was a {selected_character_type} named {selected_character_name}. 
    {selected_character_name} loved to explore new places. One day, while exploring near a {selected_location_feature}, 
    {selected_character_name} stumbled upon a mysterious {selected_object_found}. Curious and a little nervous, 
    {selected_character_name} decided to take a closer look. What happened next was an adventure 
    {selected_character_name} would never forget!
    """
    # Create a prompt for the LLM to enhance the story
    prompt = f"Please enhance the following story by adding more detail, vivid imagery, and depth, without asking any questions or adding preamble other than the story. This story is intended for 4-7 year olds. Makre sure the vocabulary and the lnaguage is appropriate for this age. The story is as follows:\n\n{st.session_state.story_template}."

    # Call the language model to enhance the story
    response = ai.prompt(message=prompt)
    # Display enhanced story if it exists
    st.subheader("Enojoy your story!")
    st.write(response["message"])
