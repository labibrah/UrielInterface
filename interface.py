import streamlit as st
import pandas as pd
import random as rnd

## Global settings variables



'Welcome to URIEL+'

## Settings button and logic to change configurations

if st.button("Settings", icon=":material/settings:"):
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        cache_toggle = st.toggle("Activate caching", help='Caching is default false to save memory, setting it true means updates to databases or imputation are saved to files')
    with middle_column:
        avg_aggregation_toggle = st.toggle("Set aggregation to average", help='Aggregation is default set to union of typological feature data across sources in URIEL+, toggling this will set aggregation to average of typological feature data across sources')
    with right_column:
        fill_with_base_lang_toggle = st.toggle("Fill with base language", help="""
### Aggregating Typological Feature Data

When aggregating typological feature data, the data from a language's parent is used to fill in any missing information for that language. For example, **English** serves as the parent language for **Hong Kong English**, providing data to complete any gaps in typological features for Hong Kong English.

By default, this configuration is set to `True` because it ensures:

- **Better feature coverage**: Maximizing the completeness of data across languages.
- **High imputation quality**: Maintaining reliable and consistent data accuracy.

This approach enhances the overall quality of typological analysis and minimizes data loss due to incomplete entries.
""")
# else:
#      ''






df = pd.DataFrame({
    'calculation options': ['Calculate distance between languages','Impute the URIEL database'],
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
     help= """
1. **Updated SAPhon**:  
   A revised and expanded database of South American phonological inventories, focusing on phoneme systems and their typological features.

2. **BDProto**:  
   A database for studying protolanguages, providing reconstructed linguistic data to understand historical language evolution.

3. **Grambank**:  
   A global comparative database of grammatical structures, capturing cross-linguistic diversity in syntactic and morphological features.

4. **APiCS**:  
   The Atlas of Pidgin and Creole Language Structures, documenting structural features of creole and pidgin languages worldwide.

5. **eWave**:  
   The electronic World Atlas of Varieties of English, detailing linguistic features and variation across English dialects.

6. **Inferred**:  
   A dataset containing linguistically inferred or derived features, often used for comparative or evolutionary studies.

7. **All**:  
   Refers to the collective use of all the above databases for comprehensive linguistic analysis and cross-referencing.
"""

     )
    if st.button('Impute'):
            'The URIEL database was successfully imputed.'

elif (option == 'Calculate distance between languages'):
    df = pd.DataFrame({
    'distance options': ['Geographic','Featural','Genetic','Morphological','Inventory','Phonological','Syntactic'],
    # 'second column': [10, 20, 30, 40]
    })
    distance_option = st.selectbox(
    'What kind of distance would you like to calculate?',
     df['distance options'],
     index=None,
     help="""# Types of Language Distances

1. **Geographic**:  
   Measures the physical distance between the regions where languages are spoken, often reflecting historical contact or isolation.

2. **Featural**:  
   Compares specific linguistic features (e.g., word order, inflection) to quantify structural similarities or differences.

3. **Genetic**:  
   Based on historical and evolutionary relationships, tracing back to a common ancestral language.

4. **Morphological**:  
   Examines how languages form words, focusing on aspects like inflection, derivation, and word-building strategies.

5. **Inventory**:  
   Compares the sets of phonemes (vowels, consonants) present in languages, assessing sound system similarities.

6. **Phonological**:  
   Studies the systems of sounds and rules governing pronunciation and sound patterns in languages.

7. **Syntactic**:  
   Analyzes differences in sentence structure and grammatical rules, such as subject-verb-object order.
"""""
     )
   
    if distance_option != None and distance_option[0] != None:
        options = st.multiselect(
        "Choose languages to calculate distance of",
        ["English", "Japanese", "Bengali", "Hindi"],
        help="Chose two or more languages to calculate the distance of."
        )
        if st.button('Compute'):
            'The distance  ' + str(round(rnd.random(),2))
    

