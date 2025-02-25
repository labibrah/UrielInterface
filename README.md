Hosted at: https://uriel-leelab.streamlit.app/
For reference and setup follow: https://docs.streamlit.io/get-started/fundamentals/main-concepts

# URIEL Database UI

This Python script utilizes Streamlit to create a simple user interface (UI) for interacting with the URIEL database. The UI offers two main functionalities for the user to choose from:

1. Impute data into the URIEL database
2. Calculate the distance between languages

Below is a detailed commentary on each section of the code:

## Step 1: Understanding the Code

### Initial Setup

```python
df = pd.DataFrame({
    'calculation options': ['Calculate distance between languages', 'Impute the URIEL database'],
    # 'second column': [10, 20, 30, 40]
})
```

A DataFrame is created using pandas with a single column, `calculation options`, that lists two user options: 
- "Calculate distance between languages"
- "Impute the URIEL database"

**Note:** The second column is commented out and is not currently being used. It could be part of future functionality or an unfinished feature under debugging.

### User Interaction: Select an Option

```python
option = st.selectbox(
    'What would you like to do using the URIEL database?',
    df['calculation options'],
    index=None,
)
'You selected: ', option
```

A selectbox is presented to the user with the two options from the DataFrame. Based on the user's selection, the UI will display the chosen option. The `index=None` indicates no default selection is made, so the user must actively select an option.

### Conditional Block: Impute the URIEL Database

```python
if (option == 'Impute the URIEL database'):
    df = pd.DataFrame({
        'impute options': ['Updated SAPhon', 'BDProto', 'Grambank', 'APiCS', 'eWave', 'Inferred', 'All'],
    })
    impute_option = st.selectbox(
        'Which database would you like to impute into the URIEL database?',
        df['impute options'],
        index=None,
        help= IMPUTE_OPTIONS_HELP)
    if st.button('Impute'):
        'The URIEL database was successfully imputed.'
```

- **Contextual Changes:** If the user selects "Impute the URIEL database," a new DataFrame is created listing available impute options like "Updated SAPhon," "BDProto," etc.
- The selectbox lets the user choose an impute option. 
- If the user presses the 'Impute' button, a success message is displayed: "The URIEL database was successfully imputed."
- The `help` parameter in the selectbox provides additional context or explanations to users through `IMPUTE_OPTIONS_HELP` (which is defined elsewhere in the code).

### Conditional Block: Calculate Distance Between Languages

```python
elif (option == 'Calculate distance between languages'):
    df = pd.DataFrame({
        'distance options': ['Geographic', 'Featural', 'Genetic', 'Morphological', 'Inventory', 'Phonological', 'Syntactic'],
    })
    distance_option = st.selectbox(
        'What kind of distance would you like to calculate?',
        df['distance options'],
        index=None,
        help=DISTANCE_OPTIONS_HELP
    )
    if distance_option != None and distance_option[0] != None:
        options = st.multiselect(
            "Choose languages to calculate distance of",
            ["English", "Japanese", "Bengali", "Hindi"],
            help="Choose two or more languages to calculate the distance of."
        )
        if st.button('Compute'):
            'The distance ' + str(round(rnd.random(), 2))
```

- **Contextual Changes:** If the user selects "Calculate distance between languages," a new DataFrame presents a list of distance options such as "Geographic," "Featural," "Genetic," etc.
  
- **Language Selection:** After selecting a distance option, the user is prompted to select languages for the calculation. The available languages are:
    - "English"
    - "Japanese"
    - "Bengali"
    - "Hindi"
  
- **Computation:** When the user clicks the 'Compute' button, the system should compute the distance between the selected languages. The current implementation uses `rnd.random()` to simulate the calculation with a random value. This may be a placeholder and should be replaced with a proper function to compute the actual distance between languages.

- The `help` text provides guidance for choosing languages: "Choose two or more languages to calculate the distance of."
