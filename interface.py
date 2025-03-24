import ast
import time
import cohere
import numpy as np
import streamlit as st
import pandas as pd
import requests
import random
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
st.set_page_config(
    page_title="Uriel UI",
    page_icon=":speech_balloon:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={

        'About': "# This is an *extremely* cool app built with hardwork by Labib Rahman!"
    }
)

GREETING = """
Welcome to **ExploRIEL:** An easy to use interface for the URIEL+ knowledge base.
"""


def stream_data():
    for word in URIEL_INTRO.split(" "):
        yield word + " "
        time.sleep(0.02)


# st.write_stream(stream_data)
st.title(GREETING)
st.divider()

st.header('What is URIEL?')
st.write(URIEL_INTRO)



# Base URL for the API
BASE_URL = "https://uriel-api-p-197469327377.us-east1.run.app"


HEADERS = {
    "URIEL-API-key": st.secrets["API_KEY"]
}


## Chat bot implementation
# Initialize session state for settings visibility and toggle values
if "show_settings" not in st.session_state:
    st.session_state.show_settings = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "show_integrate_settings" not in st.session_state:
    st.session_state.show_integrate_settings = False
if "show_aggregate_settings" not in st.session_state:
    st.session_state.show_aggregate_settings = False
if "show_impute_settings" not in st.session_state:
    st.session_state.show_impute_settings = False

if "cache_toggle_value" not in st.session_state:
    st.session_state.cache_toggle_value = False
if "distance_option_value" not in st.session_state:
    st.session_state.distance_option_value = False
if "avg_aggregation_toggle" not in st.session_state:
    st.session_state.avg_aggregation_toggle = False
if "fill_with_base_lang_toggle" not in st.session_state:
    st.session_state.fill_with_base_lang_toggle = False

if "show_dialects" not in st.session_state:
    st.session_state.show_dialects = False
if st.button("Parent languages and dialects", icon="📜", help=DIALECTS_HELP):
    st.session_state.show_dialects = not st.session_state.show_dialects

co = cohere.ClientV2(st.secrets["COHERE"]) # This is your trial API key

# print(response)
# Create a custom system message
system_message="""## Task and Context
You are an assistant who assists with use of the Uriel database related to language queries.

## Style Guide
Be professional. Keep your answers concise to a maxiumum three or four sentences."""

# Streamed response emulator
def response_generator():
    response = co.chat(
        model='d28bb7fb-f7d7-435a-90b6-712f32563038-ft',
        messages=st.session_state.messages)
    print(response.message.content[0].text)
    for word in response.message.content[0].text.split():
        yield word + " "
        time.sleep(0.05)
    return response.message.content[0].text

# Initialize chat history


def message_generator():
    for message in st.session_state.messages:
        print(message,"\n")
def message_appender(message):
    st.session_state.messages.append(
        {"role": "assistant", "content": message})
# Using "with" notation
with st.sidebar:
    st.title("Uriel conversational agent")

    # Display chat messages from history on app rerun
    # for message in st.session_state.messages:
    #     with st.chat_message(message["role"]):
    #         st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask me questions about Uriel!"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
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
        print("Custom Distance Response:", response.text)
    else:
        print("Error try a different database or feature list:", response.status_code, response.text)
    return response.text



# Example: GET /feature_coverage
# def get_feature_coverage(resource_options,distance_type):
#     """
#     Example query parameter: {"lang": "eng"}
#     """
#     params = {
#         "resource_level": resource_options,  # Ensure this matches the API docs
#         "distance_type": distance_type  # Convert list to CSV string
#     }
#     # response = requests.get(f"{BASE_URL}/set_glottocodes", headers=HEADERS)
#     # st.write(headers)
#     # time.sleep(5)
#     st.write(params)
#     # response = requests.get(f"{BASE_URL}/feature_coverage", headers=HEADERS,params=params)
#     if response.status_code == 200:
#         print("Feature Coverage Response:", response.text)
#         return response.text
#     else:
#         print("Error:", response.status_code, response.text)

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
                message_appender("The confidence Score Response for " + str(params) + " is " + str(confidence_score) + " for Agreement and and Missing Values respectively.")
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
        message_appender("The distance vector of type " + type + " for " + languages + "which used to calculate language distance metrics is " + response.text)

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



def get_loaded_feature(params):
    """
    Example query parameters: {"lang1": "eng", "lang2": "jpn"}
    """
    response = requests.get(f"{BASE_URL}/loaded_feature_array", headers=HEADERS, params=params)
    if response.status_code == 200:
        print("Distance Response:", response.json())
        message_appender("The loaded feature array of vector type " + params["vector_type"] + " and feature type " + params["feature_type"] +" is:" + response.text)

    else:
        print("Error:", response.status_code, response.text)
    return response.json()

def integrate_database(databases):
    results = {}
    for db in databases:
        params = {"databases": db}
        response = requests.get(f"{BASE_URL}/integrate", headers=HEADERS, params=params)
        # response.text
        if response.status_code == 200:
            results[db] = response.text
            message_appender("The database " + db +" has been integrated for more values.")
        else:
            st.error(f"Failed to integrate {db}. Please try again.")

    return results
def aggregate_database(strategy):
    params = {
        "strategy": strategy,
    }
    response = requests.get(f"{BASE_URL}/aggregate", headers=HEADERS, params=params)
    # response.text
    if response.status_code == 200:
        st.write("Aggregated successfully")
    else:
        st.error(f"Failed to aggregate. Please try again.")
    return response.text
def impute_database(strategy):
    params = {
        "strategy": strategy,
    }
    response = requests.get(f"{BASE_URL}/impute", headers=HEADERS, params=params)
    # response.text
    if response.status_code == 200:
        st.write("Imputed successfully")
    else:
        st.error(f"Failed to impute. Please try again.")
    return response.text




if st.session_state.show_dialects:
    df = pd.DataFrame(DIALECTS.items(), columns=["ID", "Dialects"])
    st.dataframe(df, height=500)

st.header("Settings")
st.divider()
# Toggle the visibility of the settings section
# if st.button("Settings", icon=":material/settings:"):
# if st.button("Settings", icon="⚙️"):
#     st.session_state.show_settings = not st.session_state.show_settings
#
# # Display the settings section if it's toggled on
# if st.session_state.show_settings:
#     if "show_dialects" not in st.session_state:
#       st.session_state.show_dialects = False
#     if st.button("Parent languages and dialects", icon="📜", help=DIALECTS_HELP):
#         st.session_state.show_dialects = not st.session_state.show_dialects
#     if st.session_state.show_dialects:
#         df = pd.DataFrame(DIALECTS.items(), columns=["ID", "Dialects"])
#
#         st.dataframe(df, height=500)
#     left_column, middle_column, right_column = st.columns(3)
#     with left_column:
#         # if st.button("Integrate", type="primary"):
#         #     selected = st.multiselect(
#         #         "Select databases to impute:",
#         #         ["UPDATED_SAPHON", "BDPROTO", "GRAMBANK", "APICS", "EWAVE"],
#         #     )
#         #
#         #     if selected:
#         #         st.write(selected)
#         #         with st.spinner("Imputing databases..."):
#         #             result = impute_database(selected)
#
#                 # if result:
#                 #     st.success("Database imputation successful!")
#                 #     st.json(result)  # Display API response
#
#         st.session_state.cache_toggle_value = st.checkbox(
#             "Activate caching",
#             value=st.session_state.get("cache_toggle_value", False),
#             help=ACTIVATE_CACHING_HELP
#         )
#         # st.session_state.distance_option_value = st.checkbox(
#         #     "Set distance to cosine",
#         #     value=st.session_state.get("distance_option_value", False),
#         #     help=COSINE_DISTANCE_HELP
#         # )
#     with middle_column:
#         if st.button("Aggregate", icon=":material/settings:"):
#             st.write("Imputing Dialects")
#         # st.session_state.avg_aggregation_toggle = st.checkbox(
#         #     "Set aggregation to average",
#         #     value=st.session_state.get("avg_aggregation_toggle", False),
#         #     help=AGGREGATION_HELP
#         # )
#     with right_column:
#         if st.button("Impute", icon=":material/settings:"):
#             st.write("Imputing Dialects")
#         # st.session_state.fill_with_base_lang_toggle = st.checkbox(
#         #     "Fill with base language",
#         #     value=st.session_state.get("fill_with_base_lang_toggle", False),
#         #     help=FILL_WITH_BASE_LANGUAGE_HELP
#         # )


if st.button("Add Other Databases (Integrate Settings)", type="secondary"):
    st.session_state.show_integrate_settings = not st.session_state.show_integrate_settings

if st.session_state.show_integrate_settings:
        selected = st.multiselect(
            "Select databases to impute:",
            ["UPDATED_SAPHON", "BDPROTO", "GRAMBANK", "APICS", "EWAVE"],
        )
        if st.button("Integrate"):
            # st.write(selected)
            with st.spinner("Integrating databases...(this may take a while)"):
                result = integrate_database(selected)

            if result:
                st.success("Successful integrations below:")
                st.json(result)  # Display API response

if st.button("Combine Data (Aggregation Settings)", type="secondary"):
    st.session_state.show_aggregate_settings = not st.session_state.show_aggregate_settings
if  st.session_state.show_aggregate_settings:
    selected = st.selectbox(
        "Select aggregation strategy:",
        ["Union", "Average"],
    )
    if st.button("Aggreate"):
        dict = {
            "Union":"U",
            "Average":"A",
        }
        with st.spinner("Aggregating databases...(this may take a while)"):
            # st.write(dict[selected])
            result = aggregate_database(dict[selected])
            # if result:
            #     st.success("Database aggregation successful!")
                # st.json(result)  # Display API response

if st.button("Add Missing Values (Imputation Settings)", type="secondary"):
    st.session_state.show_impute_settings = not st.session_state.show_impute_settings
if st.session_state.show_impute_settings:
    # knn omitted
    selected = st.selectbox(
        "Select strategy to impute with:",
        ["Midaspy", "Softimpute","Mean"],
    )
    if st.button("Impute"):
        selected = selected.lower()
        with st.spinner("Imputing databases...(this may take a while)"):
            response = impute_database(selected)



# Display the current states (for debugging purposes)
# st.write("Prompts below are for testing only:")
# st.write("Settings state:", st.session_state.show_settings)
# st.write("Caching active:", st.session_state.cache_toggle_value)
# st.write("Distance option active:", st.session_state.distance_option_value)
# st.write("Aggregation toggle:", st.session_state.avg_aggregation_toggle)
# st.write("Fill with base language:", st.session_state.fill_with_base_lang_toggle)
st.header("Calculations")
st.divider()
df = pd.DataFrame({
    'calculation options': ['Calculate specific distance between languages','Calculate custom distance between languages using features','Calculate confidence score betweeen two languages based on distance-type','View distance vector used for calculation','Get loaded feature array'],
    # 'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'What would you like to do using the URIEL database?',
     df['calculation options'],
      index=None,
     )

##Going through the different options
##If they choose to impute the database, give them option to choose which ones to impute or just impute all
if (option == 'Calculate specific distance between languages'):
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
            "Choose two or more languages to calculate distance of",
            list(languages.keys()),  # Get language names dynamically
            help="Choose two or more languages to calculate the distance of."
        )

        if options:
            selected_iso_codes = [languages[lang] for lang in options]  # Convert selected names to ISO
            selected_languages = ",".join(selected_iso_codes)  # Create a comma-separated string

            distance_type = str(distance_option.lower())

            if st.button('Compute'):
                response = get_distance({"languages": selected_languages, "type": distance_type})
                message_appender("The distance type of " + distance_type + " for " + selected_languages + " was " + (str)(response))
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
                    st.write(response)
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
            distance_type = str(distance_options.lower())
            response = get_distance_vector_(distance_type, languages[language_options])
            # Convert string to dictionary safely
            response = ast.literal_eval(response)
            # Ensure it's a dictionary
            if isinstance(response, dict):
                for lang, scores in response.items():
                    df = pd.DataFrame(scores, columns=[f"Vector for ({language_options}) based on {distance_options} distance:"])
                    st.dataframe(df)  # Displays scores in a scrollable table
# elif (option == 'Get feature coverage'):
#     df = pd.DataFrame({
#         'Resource level': ["High-resource", "Medium-resource", "Low-resource"],
#     })
#     resource_options = st.selectbox(
#         "Choose resource level of the languages to check feature coverage of.",
#         df,  # Get language names dynamically
#         help="Choose resource level of the languages to check feature coverage of.",
#     )
#     if resource_options:
#         df = pd.DataFrame({
#             'distance options': [ "Geographic","Genetic","Featural", "Syntactic", "Phonological", "Inventory", "Morphological"],
#         })
#         distance_options = st.selectbox(
#             "Choose the type of distance to view vector for.",
#             df['distance options'],  # Get language names dynamically
#             help="Choose type of distance to view vector for.",
#         )
#         if st.button('View'):
#             resource_options = str(resource_options.lower())
#             distance_type = str(distance_options.lower())
#             response = get_feature_coverage(resource_options,distance_type)
#             # response
#             # Convert string to dictionary safely
#             # response = ast.literal_eval(response)
#             st.write(f"The feature coverage based on resource level is: " + str(response.text))
elif (option == 'Get loaded feature array'):
    df = pd.DataFrame({
            'vectors': ["Phylogeny","Typological", "Geography"],
        })
    vector_options = st.selectbox(
            "Choose vector type to get loaded feature array of.",
            df['vectors'],  # Get language names dynamically
            help="Choose vector type to get loaded feature array of.",
        )
    if vector_options:
        df = pd.DataFrame({
            'features': ["Features", "Languages", "Data", "Sources"],
        })
        feature_options = st.selectbox(
            "Choose feature type to get loaded feature array of.",
            df['features'],  # Get language names dynamically
            help="Choose feature type to get loaded feature array of.",
        )
        if st.button('View'):
            vector_options = vector_options.lower()
            feature_options = feature_options.lower()
            response = get_loaded_feature({"vector_type": vector_options, "feature_type": feature_options})
            df = pd.DataFrame(response, columns=["Features"])

            st.dataframe(df, height=500)











    

