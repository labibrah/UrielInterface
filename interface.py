import streamlit as st
import pandas as pd
import random as rnd
import requests
import os
from dotenv import load_dotenv

from prompts import (
    URIEL_INTRO,
    ACTIVATE_CACHING_HELP,
    COSINE_DISTANCE_HELP,
    AGGREGATION_HELP,
    FILL_WITH_BASE_LANGUAGE_HELP,
    IMPUTE_OPTIONS_HELP,
    DISTANCE_OPTIONS_HELP,
    DIALECTS,
    DIALECTS_HELP
)

st.title('Welcome to the URIEL UI')
st.header('What is URIEL?')
st.write(URIEL_INTRO)

# # Settings button and logic to change configurations
#
# # Initial toggle values
# if "cache_toggle_value" not in st.session_state:
#     st.session_state.cache_toggle_value = False
# st.session_state.cache_toggle_value
#
# # Initialize session state for settings visibility and toggle values
# if "show_settings" not in st.session_state:
#     st.session_state.show_settings = False
# # Changing toggle values
# def cache_toggle():
#     st.session_state.cache_toggle_value = not st.session_state.cache_toggle_value
#     'hello'
#
# # Toggle the visibility of the settings section
# if st.button("Settings", icon=":material/settings:"):
#     st.session_state.show_settings = not st.session_state.show_settings
#
# # Display the settings section if it's toggled on
# if st.session_state.show_settings:
#    left_column, middle_column, right_column = st.columns(3)
#    with left_column:
#         cache_toggle = st.toggle(
#             "Activate caching",
#             help=ACTIVATE_CACHING_HELP,
#             # value= not st.session_state.cache_toggle_value,
#             key="cache_toggle_value",
#             # on_change=cache_toggle
#         )
#         distance_option = st.toggle(
#             "Set cosine distance",
#             help=COSINE_DISTANCE_HELP
#         )
#    with middle_column:
#         avg_aggregation_toggle = st.toggle(
#             "Set aggregation to average",
#             help=AGGREGATION_HELP
#         )
#    with right_column:
#         fill_with_base_lang_toggle = st.toggle(
#             "Fill with base language",
#             help=FILL_WITH_BASE_LANGUAGE_HELP
#         )
#
# Load the .env file
load_dotenv()

# Retrieve the API key
API_KEY = os.getenv("URIEL_API_KEY")


# Base URL for the API
BASE_URL = "https://uriel-api-p-197469327377.us-east1.run.app"


# Headers for authentication
HEADERS = {
    "URIEL-API-key": API_KEY
}
#
# # Example: Test the root endpoint
def test_root():
    response = requests.get(f"{BASE_URL}/start_session", headers=HEADERS)
    if response.status_code == 200:
        try:
            # Try to parse JSON response
            print("Root Response (JSON):", response.json())
        except requests.exceptions.JSONDecodeError:
            # If it's not JSON, fallback to plain text
            print("Root Response (Text):", response.text)
    else:
        print("Error:", response.status_code, response.text)
    return response.text

# # Example: GET /distance
def get_distance(params):
    """
    Example query parameters: {"lang1": "eng", "lang2": "jpn"}
    """
    response = requests.get(f"{BASE_URL}/distance", headers=HEADERS, params=params)
    if response.status_code == 200:
        print("Distance Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)
    return response.json()

# # Example: POST /custom_distance
def post_custom_distance(data):
    """
    Example payload:
    {
        "lang1": "eng",
        "lang2": "jpn",
        "features": ["phonological", "syntactic"]
    }
    """
    response = requests.post(f"{BASE_URL}/custom_distance", headers=HEADERS, json=data)
    if response.status_code == 200:
        print("Custom Distance Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)
    return response.text

# Example: GET /distance_vector
def get_distance_vector(lang):
    """
    Example query parameter: {"lang": "eng"}
    """
    response = requests.get(f"{BASE_URL}/distance_vector", headers=HEADERS, params={"lang": lang})
    if response.status_code == 200:
        print("Distance Vector Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)

# Example: GET /feature_coverage
def get_feature_coverage(lang):
    """
    Example query parameter: {"lang": "eng"}
    """
    response = requests.get(f"{BASE_URL}/feature_coverage", headers=HEADERS, params={"lang": lang})
    if response.status_code == 200:
        print("Feature Coverage Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)

# Example: GET /confidence_score
def get_confidence_score(lang):
    """
    Example query parameter: {"lang": "eng"}
    """
    response = requests.get(f"{BASE_URL}/confidence_score", headers=HEADERS, params={"lang": lang})
    if response.status_code == 200:
        print("Confidence Score Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)

# # Test the root endpoint
# # st.write(test_root())
# # Tested and works
# st.write('Distance check: ' + (str)(get_distance({"languages": 'eng,ben,hin', "type":"genetic"})))
# # st.write('Custom distance check: ' + (str)(post_custom_distance({"features": ["F_Germanic", "S_SVO", "P_NASAL_VOWELS"],"languages": ['eng','fra']
# # , "source":"WALS"})))
# #
# # st.write(test_root())
# # st.write(test_root())
# # st.write(test_root())







# Initialize session state for settings visibility and toggle values
if "show_settings" not in st.session_state:
    st.session_state.show_settings = False
if "cache_toggle_value" not in st.session_state:
    st.session_state.cache_toggle_value = False
if "distance_option_value" not in st.session_state:
    st.session_state.distance_option_value = False
if "avg_aggregation_toggle" not in st.session_state:
    st.session_state.avg_aggregation_toggle = False
if "fill_with_base_lang_toggle" not in st.session_state:
    st.session_state.fill_with_base_lang_toggle = False

# Toggle the visibility of the settings section
# if st.button("Settings", icon=":material/settings:"):
if st.button("Settings", icon="⚙️"):
    st.session_state.show_settings = not st.session_state.show_settings

# Display the settings section if it's toggled on
if st.session_state.show_settings:
    if "show_dialects" not in st.session_state:
      st.session_state.show_dialects = False
    if st.button("Parent languages and dialects", icon="📜", help=DIALECTS_HELP):
        st.session_state.show_dialects = not st.session_state.show_dialects
    if st.session_state.show_dialects:
        st.write(DIALECTS)
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.session_state.cache_toggle_value = st.checkbox(
            "Activate caching",
            value=st.session_state.get("cache_toggle_value", False),
            help=ACTIVATE_CACHING_HELP
        )
        st.session_state.distance_option_value = st.checkbox(
            "Set cosine distance",
            value=st.session_state.get("distance_option_value", False),
            help=COSINE_DISTANCE_HELP
        )
    with middle_column:
        st.session_state.avg_aggregation_toggle = st.checkbox(
            "Set aggregation to average",
            value=st.session_state.get("avg_aggregation_toggle", False),
            help=AGGREGATION_HELP
        )
    with right_column:
        st.session_state.fill_with_base_lang_toggle = st.checkbox(
            "Fill with base language",
            value=st.session_state.get("fill_with_base_lang_toggle", False),
            help=FILL_WITH_BASE_LANGUAGE_HELP
        )
        
        

# Display the current states (for debugging purposes)
st.write("Prompts below are for testing only:")
st.write("Settings state:", st.session_state.show_settings)
st.write("Caching active:", st.session_state.cache_toggle_value)
st.write("Distance option active:", st.session_state.distance_option_value)
st.write("Aggregation toggle:", st.session_state.avg_aggregation_toggle)
st.write("Fill with base language:", st.session_state.fill_with_base_lang_toggle)

df = pd.DataFrame({
    'calculation options': ['Calculate distance between languages','Impute the URIEL database'],
    # 'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'What would you like to do using the URIEL database?',
     df['calculation options'],
      index=None,
     )

'You selected: ', option

##Going through the different options
##If they choose to impute the database, give them option to choose which ones to impute or just impute all
if (option == 'Impute the URIEL database'):
    df = pd.DataFrame({
    'impute options': ['Updated SAPhon', 
    'BDProto', 
    'Grambank', 
    'APiCS', 
    'eWave', 
    'Inferred', 
    'All'],
    })
    impute_option = st.selectbox(
    'Which database would you like to impute into the URIEL database?',
     df['impute options'],
     index=None,
     help= IMPUTE_OPTIONS_HELP)
    if st.button('Impute'):
            'The URIEL database was successfully imputed.'

elif (option == 'Calculate distance between languages'):
    df = pd.DataFrame({
    'distance options': ['Geographic','Featural','Genetic','Morphological','Inventory','Phonological','Syntactic'],
    })
    distance_option = st.selectbox(
    'What kind of distance would you like to calculate?',
     df['distance options'],
     index=None,
     help=DISTANCE_OPTIONS_HELP)
   
    if distance_option != None and distance_option[0] != None:
        options = st.multiselect(
        "Choose languages to calculate distance of",
        ["English", "Japanese", "Bengali", "Hindi"],
        help="Chose two or more languages to calculate the distance of."
        )
        languages = {
            "English": "eng",
            "Japanese": "jpn",
            "Bengali": "ben",
            "Hindi": "hin"
        }
        selected_languages = ",".join(languages[lang] for lang in options)
        st.write(selected_languages)
        distance_type = str(distance_option.lower())
        st.write(distance_type)
        if st.button('Compute'):
            response = get_distance({"languages": selected_languages, "type": distance_type})

            if isinstance(response, list):  # Ensure response is a list (matrix)
                st.write(f"The {distance_type} distance matrix is:")

                # Convert to DataFrame for better display
                selected_langs = selected_languages.split(",")  # Convert back to list
                df = pd.DataFrame(response, index=selected_langs, columns=selected_langs)

                st.dataframe(df.style.format(precision=4))  # Nicely formatted table
            else:
                st.error("Unexpected response format. Check the API response.")
    

