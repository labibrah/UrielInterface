import streamlit as st
import pandas as pd
import ast
import requests
import os
from dotenv import load_dotenv
import json

from prompts import (
    URIEL_INTRO,
    ACTIVATE_CACHING_HELP,
    COSINE_DISTANCE_HELP,
    AGGREGATION_HELP,
    FILL_WITH_BASE_LANGUAGE_HELP,
    IMPUTE_OPTIONS_HELP,
    DISTANCE_OPTIONS_HELP,
    DIALECTS,
    DIALECTS_HELP,
    LANG_ISO
)

st.title('Welcome to the URIEL UI+')
st.header('What is URIEL?')
st.write(URIEL_INTRO)

# If working local, uncomment below Load the .env file
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
def get_distance_vector(params):
    """
    Example query parameter: {"lang": "eng"}
    """
    response = requests.get(f"{BASE_URL}/distance_vector", headers=HEADERS, params=params)
    if response.status_code == 200:
        print("Distance Vector Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)

# Example: GET /feature_coverage
def get_feature_coverage():
    """
    Example query parameter: {"lang": "eng"}
    """
    response = requests.get(f"{BASE_URL}/feature_coverage")
    if response.status_code == 200:
        print("Feature Coverage Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)

# Example: GET /confidence_score


def get_confidence_score(params):
    """ Get confidence score from API """

    full_url = f"{BASE_URL}/confidence_score"
    print("Request URL:", full_url)
    print("Query Params:", params)

    response = requests.get(full_url, headers=HEADERS, params=params)

    # Print actual response content before parsing
    print("Final Request URL:", response.url)
    print("Raw Response Content:", response.text)  # Debugging

    if response.status_code == 200:
        try:
            raw_text = response.text.strip()

            # Handle tuple response manually
            if raw_text.startswith("(") and raw_text.endswith(")"):
                confidence_score = eval(raw_text)  # Converts string tuple to actual tuple
                print("Confidence Score Response:", confidence_score)
                return confidence_score
            else:
                print("Unexpected response format:", raw_text)
                return None

        except Exception as e:
            print("Error:", e)
            return None
    else:
        print("Error:", response.status_code, response.text)
        return None



# Test the function


# # Test the root endpoint
# # st.write(test_root())
# # Tested and works
# st.write('Distance check: ' + (str)(get_distance({"languages": 'eng,ben,hin', "type":"genetic"})))
# st.write('Custom distance check: ' + (str)(post_custom_distance({"features": ["F_Germanic", "S_SVO", "P_NASAL_VOWELS"],"languages": ['eng','fra'], "source":"WALS"})))
# st.write(get_distance_vector({
#     "distance_type": "featural",
#     "languages": ["eng,fra"]  # Ensure it's a list, not a string
# }))
# get_distance_vector("type": "featural","languages": 'eng')
def get_distance_vector_(type, languages):
    params = {
        "type": type,  # Ensure this matches the API docs
        "languages": languages  # Convert list to CSV string
    }

    response = requests.get(f"{BASE_URL}/distance_vector", headers=HEADERS, params=params)

    if response.status_code == 200:
        print("Distance Vector Response:", response.text)
        return response.text
    else:
        print("Error:", response.status_code, response.text)
        return None  # Handle errors gracefully

# Example usage
# st.write(get_distance_vector_("featural", "eng,fra"))
# get_feature_coverage()
# st.write('Distance check: ' )
# get_confidence_score({"language_1": 'eng',"language_2": 'fra', "distance_type":"featural"})
# st.write("hello" + get_feature_coverage())

# get_confidence_score({"language_1": "eng", "language_2": "fra", "distance_type": "featural"})




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
            "Set distance to cosine",
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
# st.write("Prompts below are for testing only:")
# st.write("Settings state:", st.session_state.show_settings)
# st.write("Caching active:", st.session_state.cache_toggle_value)
# st.write("Distance option active:", st.session_state.distance_option_value)
# st.write("Aggregation toggle:", st.session_state.avg_aggregation_toggle)
# st.write("Fill with base language:", st.session_state.fill_with_base_lang_toggle)

df = pd.DataFrame({
    'calculation options': ['Calculate specific distance between languages','Calculate custom distance between languages using features','Calculate confidence score betweeen two languages based on distance-type','Impute the URIEL database','View distance vector used for calculation'],
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

elif (option == 'Calculate specific distance between languages'):
    df = pd.DataFrame({
    'distance options': ['Geographic','Featural','Genetic','Morphological','Inventory','Phonological','Syntactic'],
    })
    distance_option = st.selectbox(
    'What kind of distance would you like to calculate?',
     df['distance options'],
     index=None,
     help=DISTANCE_OPTIONS_HELP)
    languages = LANG_ISO
    if distance_option and distance_option[0]:
          # Dictionary of language names to ISO codes

        options = st.multiselect(
            "Choose languages to calculate distance of",
            list(languages.keys()),  # Get language names dynamically
            help="Choose two or more languages to calculate the distance of."
        )

        if options:
            selected_iso_codes = [languages[lang] for lang in options]  # Convert selected names to ISO
            selected_languages = ",".join(selected_iso_codes)  # Create a comma-separated string

            distance_type = str(distance_option.lower())

            if st.button('Compute'):
                response = get_distance({"languages": selected_languages, "type": distance_type})

                if isinstance(response, list):  # Ensure response is a list (matrix)
                    st.write(f"The {distance_type} distance matrix is:")

                    # Use the original language names instead of ISO codes
                    df = pd.DataFrame(response, index=options, columns=options)

                    st.dataframe(df.style.format(precision=4))  # Nicely formatted table
                else:
                    st.write(f"The {distance_type} distance is: " + (str)(response))
elif (option == 'Calculate custom distance between languages using features'):
    languages = LANG_ISO
    language_options = st.multiselect(
        "Choose languages to calculate distance(s) based on custom features.",
        list(languages.keys()),  # Get language names dynamically
        help="Choose two or more languages to calculate the distance of."
    )
    if language_options:
        #TODO: need to add more features here
        df = pd.DataFrame({
            'feature options': ['F_Germanic', 'S_SVO', 'P_NASAL_VOWELS'],
        })
        feature_options = st.multiselect(
            "Choose features to calculate distance(s) between languages based on custom metrics.",
            df['feature options'],  # Get language names dynamically
            help="Choose two or more languages to calculate the distance of."
        )
        #DONE add more databases
        if feature_options:
            df = pd.DataFrame({
                'source options': ['ETHNO', 'WALS', 'PHOIBLE_UPSID', 'PHOIBLE_SAPHON', 'PHOIBLE_GM', 'PHOIBLE_PH', 'PHOIBLE_AA', 'SSWL', 'PHOIBLE_RA', 'PHOIBLE_SPA', 'BDPROTO', 'GRAMBANK', 'APICS', 'EWAVE','A'],
            })
            source_options = st.selectbox(
                "Choose database to select as source. (Choose A for all databases)",
                df['source options'],  # Get language names dynamically
                help="Choose which database to select as source."
            )
            if st.button('Compute'):
                selected_iso_codes = [languages[lang] for lang in language_options]  # Convert selected names to ISO
                selected_languages = ",".join(selected_iso_codes)  # Create a comma-separated string
                selected_languages = selected_languages.split(",")
                # st.write(selected_languages)
                response = post_custom_distance({"features":feature_options,"languages": selected_languages, "source":source_options})


                if len(language_options) < 3:
                    st.write("The distance based on custom features is: " + response)
                else:
                    response = response.strip("[]")  # Remove outer brackets
                    rows = response.split("], [")  # Split into rows

                    # Convert each row into a list of floats
                    response = [list(map(float, row.split(", "))) for row in rows]
                    if isinstance(response, list):  # Ensure response is a list (matrix)
                        st.write(f"The distance matrix based on custom features is: ")
                    #
                    #     # Use the original language names instead of ISO codes
                        df = pd.DataFrame(response, index=language_options, columns=language_options)
                    #
                        st.dataframe(df.style.format(precision=4))  # Nicely formatted table
                    #     st.table(df)
                    # else:
                    # st.write(f"The distance based on custom features is: " + (str)(response))
elif (option == 'Calculate confidence score betweeen two languages based on distance-type'):
    languages = LANG_ISO
    language_options = st.multiselect(
        "Choose languages to calculate distance(s) based on custom features.",
        list(languages.keys()),  # Get language names dynamically
        help="Choose two languages to calculate the confidence score",
        max_selections=2
    )
    if language_options:
        df = pd.DataFrame({
            'distance options': ["Featural", "Syntactic", "Phonological", "Inventory", "Morphological"],
        })
        distance_options = st.selectbox(
            "Choose the type of distance to calculate confidence score for.",
            df['distance options'],  # Get language names dynamically
            help="Choose type of distance to calculate confidence score for.",
        )
        if st.button('Compute'):
            selected_iso_codes = [languages[lang] for lang in language_options]  # Convert selected names to ISO
            selected_languages = ",".join(selected_iso_codes)  # Create a comma-separated string
            selected_languages = selected_languages.split(",")
            distance_type = str(distance_options.lower())
            response = get_confidence_score({"language_1": selected_languages[0], "language_2": selected_languages[1], "distance_type": distance_type})
            st.write(f"The confidence score based on custom features is: ")
            confidence_score = response  # Convert string tuple to actual tuple
            agreement, missing = confidence_score

            # Display as a Markdown table for readability
            st.markdown(f"""
                            | Metric       | Value  |
                            |-------------|--------|
                            | **Agreement Score**   | `{agreement:.4f}`  |
                            | **Missing Values Score** | `{missing:.4f}`  |
                            """, unsafe_allow_html=True)
elif (option == 'View distance vector used for calculation'):
    languages = LANG_ISO
    language_options = st.selectbox(
        "Choose language to view vector based on a specific feature.",
        list(languages.keys()),  # Get language names dynamically
        help="Choose a language to view vector based on a specific feature.",
    )
    if language_options:
        df = pd.DataFrame({
            'distance options': [ "Geographic","Genetic","Featural", "Syntactic", "Phonological", "Inventory", "Morphological"],
        })
        distance_options = st.selectbox(
            "Choose the type of distance to view vector for.",
            df['distance options'],  # Get language names dynamically
            help="Choose type of distance to view vector for.",
        )
        if st.button('View'):
            languages[language_options]
            # selected_iso_codes = [languages[lang] for lang in language_options]  # Convert selected names to ISO
            # selected_languages = ",".join(selected_iso_codes)  # Create a comma-separated string
            # selected_languages = selected_languages.split(",")
            distance_type = str(distance_options.lower())
            response = get_distance_vector_(distance_type, languages[language_options])
            # response
            # Convert string to dictionary safely
            response = ast.literal_eval(response)

            # Ensure it's a dictionary
            if isinstance(response, dict):
                for lang, scores in response.items():
                    df = pd.DataFrame(scores, columns=[f"Vector for ({language_options}) based on {distance_options} distance:"])
                    st.dataframe(df)  # Displays scores in a scrollable table







    

