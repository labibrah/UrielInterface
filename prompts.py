URIEL_INTRO = ("""
    ## 🌍 URIEL: A Language Knowledge Base  

**URIEL** is a comprehensive knowledge base offering **geographical, phylogenetic, and typological vector representations** for **7,970 languages**. It includes **distance measures** between these vectors for **4,005 languages**, which are accessible via the **lang2vec** tool.  

### 🔹 URIEL+ Expansion  
**URIEL+** builds upon URIEL by expanding **typological feature coverage** for **2,898 languages**. It also provides **robust and customizable distance calculations** to better suit various research and learning needs.  

### 🛠️ Using This Tool  
This tool allows you to utilize the **URIEL+ application** **without writing any code**. It is designed for **researchers, linguists, and general learners** who want to explore language relationships effortlessly.  

> **💡 Note:** You can **impute the database**, **integrate additional ones** or **aggegate** by going into their respective **"Settings"**. This will generate additional values and fill in missing data points.

""")

# Help text for "Activate caching"
ACTIVATE_CACHING_HELP = (
    "Caching is default false to save memory, setting it true means updates to databases or imputation are saved to files."
)

# Help text for "Set cosine distance"
COSINE_DISTANCE_HELP = (
    "Distance metric is default 'angular'. The distance metric chosen is how language vectors are compared for language distance calculations."
)

# Help text for "Set aggregation to average"
AGGREGATION_HELP = (
    "Aggregation is default set to union of typological feature data across sources in URIEL+, toggling this will set aggregation to average of typological feature data across sources."
)

# Help text for "Fill with base language"
FILL_WITH_BASE_LANGUAGE_HELP = """
### Aggregating Typological Feature Data

When aggregating typological feature data, the data from a language's parent is used to fill in any missing information for that language. For example, **English** serves as the parent language for **Hong Kong English**, providing data to complete any gaps in typological features for Hong Kong English.

By default, this configuration is set to `True` because it ensures:

- **Better feature coverage**: Maximizing the completeness of data across languages.
- **High imputation quality**: Maintaining reliable and consistent data accuracy.

This approach enhances the overall quality of typological analysis and minimizes data loss due to incomplete entries.
"""

# Help text for impute options
IMPUTE_OPTIONS_HELP = """
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

# Help text for distance options
DISTANCE_OPTIONS_HELP = """
# Types of Language Distances

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
"""

#
DIALECTS = {
    52: ['scf'], 53: ['lth'], 58: ['xia'], 76: ['axe'], 93: ['ajt'],
    195: ['fat', 'twi'], 204: ['gac'], 206: ['mlz'], 251: ['ais'], 316: ['ajp'],
    350: ['sqr'], 376: ['lsb'], 505: ['kgw'], 571: ['bgm'], 640: ['egm'],
    701: ['ubl', 'rbl', 'lbl', 'fbl'], 766: ['ebk', 'obk'], 820: ['krm'],
    826: ['bzo'], 970: ['xvi'], 1236: ['czk'], 1280: ['meg'], 1395: ['qwm'],
    1491: ['lda', 'dnj'], 1597: ['dit'], 1730: ['kzj', 'ktr', 'kzt', 'tdu'],
    1739: ['uth', 'uss'], 1745: ['dwy', 'dwu'], 1788: ['nzu'], 1893: ['mct'],
    1900: ['bqe'], 1966: ['tvx'], 1969: ['xno', 'nrf', 'frm'], 2015: ['ilw'],
    2050: ['xby'], 2148: ['wkr'], 2202: ['dhx'], 2308: ['xri'], 2309: ['ggn'],
    2373: ['qgg', 'xdm', 'obm'], 2374: ['ckm'], 2448: ['sgj'], 2540: ['snb'],
    2608: ['szk'], 2615: ['ilp', 'ilm'], 2631: ['inj'], 2641: ['wbs'],
    2642: ['dnv'], 2701: ['ixj', 'ixi'], 2706: ['eza', 'iqw', 'izz', 'gmz'],
    2724: ['jjr', 'jgk'], 2730: ['lja'], 2859: ['tne'], 2874: ['gmr'],
    2924: ['rwl'], 2925: ['xbj'], 2928: ['wtb'], 2943: ['zkn', 'zkd'],
    2947: ['ncp'], 3005: ['tbv'], 3025: ['thi'], 3035: ['xhm'], 3153: ['smd'],
    3284: ['olr'], 3296: ['kxl'], 3317: ['lak'], 3332: ['gyo'], 3353: ['aue'],
    3446: ['pat'], 3449: ['uki'], 3488: ['dgl', 'xnz'], 3528: ['ltg', 'xzm'],
    3650: ['olt', 'sgs'], 3661: ['krq', 'pun'], 3735: ['imt', 'lgo', 'lqr'],
    3824: ['ska', 'sno'], 3859: ['vjk'], 3866: ['anr', 'dcc'], 3943: ['mbm'],
    4123: ['mjb'], 4192: ['xyt', 'xyj', 'xyk', 'wnn'], 4203: ['xnt', 'xpq'],
    4523: ['myc'], 4537: ['nns'], 4543: ['xpt', 'xwk'], 4610: ['tpq'],
    4753: ['npx'], 4772: ['rpn'], 4775: ['yry'], 4818: ['nrn'],
    4822: ['nob', 'nno'], 4945: ['lal'], 4947: ['ssq', 'nea'], 4967: ['okc'],
    4976: ['xbp', 'xgg', 'pnj', 'xwj', 'wxw'], 5003: ['xoc'], 5011: ['frk'],
    5123: ['xhr'], 5157: ['jeg', 'skk'], 5269: ['pmu'], 5309: ['bgl'],
    5425: ['xsv'], 5446: ['bke', 'eni', 'lnt', 'ogn', 'sdd', 'srj'],
    5519: ['sbv', 'spx'], 5541: ['qxt'], 5595: ['xra'], 5697: ['mol'],
    5719: ['rsk'], 5809: ['zir'], 5814: ['sdf'], 5823: ['sdq'], 5847: ['shz'],
    5862: ['ghc', 'mga'], 6044: ['asd'], 6081: ['seb'], 6185: ['osn'],
    6263: ['mqc'], 6373: ['mju'], 6379: ['caj', 'gqn'], 6398: ['bjp'],
    6402: ['drw'], 6506: ['ukk'], 6596: ['pog', 'tpk', 'tpw'], 6608: ['gub'],
    6710: ['ota'], 6773: ['nyw', 'tmp'], 6791: ['zgh'], 6868: ['ajn'],
    7004: ['zkv'], 7075: ['act', 'drt', 'sdz', 'stl', 'twd', 'vel'],
    7080: ['lur'], 7106: ['nol', 'wnw'], 7194: ['jbw'], 7238: ['wyn', 'wdt'],
    7240: ['dgw'], 7253: ['drh'], 7260: ['zkb'], 7288: ['xgr', 'emm'],
    7301: ['ebc', 'gef'], 7436: ['yms'], 7512: ['xvo'], 7547: ['yxy'],
    7556: ['lnz', 'ppp'], 7604: ['kel'], 7643: ['yrm', 'yyr'], 7688: ['hrp'],
    7722: ['rts'], 7805: ['zcd', 'zsr'], 7844: ['xsj'], 7846: ['xma'],
    7957: ['nbl']
}

DIALECTS_HELP = """
### Help Description

This data structure provides a mapping of **parent languages** to their respective **dialects**. It is used during the aggregation of typological features to fill in missing data for a parent language by leveraging data from its associated dialects. This process ensures better coverage and accuracy of typological information.

#### Key Points:
- **Parent Language ID**: A unique numeric identifier for each parent language.
- **Dialects**: A list of language codes representing the dialects linked to the parent language.
- **Purpose**: If a parent language lacks certain typological features, data from its dialects can be used to fill those gaps.

#### Example:
- Parent language with ID `52` has the dialect `scf`.
- Parent language with ID `701` has multiple dialects: `ubl`, `rbl`, `lbl`, and `fbl`.

#### How to Use:
- Use this dictionary to understand which dialects correspond to each parent language.
- Leverage this information to aggregate or fill in missing typological data during analysis. 
"""


LANG_ISO = {
    "English": "eng",
    "Japanese": "jpn",
    "Bengali": "ben",
    "Hindi": "hin",
    "Spanish": "spa",
    "French": "fra",
    "German": "deu",
    "Chinese": "zho",
    "Russian": "rus",
    "Portuguese": "por",
    "Arabic": "ara",
    "Italian": "ita",
    "Korean": "kor",
    "Turkish": "tur",
    "Dutch": "nld",
    "Swedish": "swe",
    "Greek": "ell",
    "Thai": "tha",
    "Vietnamese": "vie",
    "Hebrew": "heb",
    "Polish": "pol",
    "Czech": "ces",
    "Hungarian": "hun",
    "Finnish": "fin",
    "Danish": "dan",
    "Norwegian": "nor",
    "Romanian": "ron",
    "Indonesian": "ind",
    "Malay": "zsm",
    "Filipino": "fil",
    "Urdu": "urd",
    "Tamil": "tam",
    "Telugu": "tel",
    "Marathi": "mar",
    "Gujarati": "guj",
    "Punjabi": "pan",
    "Swahili": "swa",
    "Hausa": "hau",
    "Yoruba": "yor",
    "Igbo": "ibo",
    "Burmese": "mya",
    "Khmer": "khm",
    "Lao": "lao",
    "Serbian": "srp",
    "Croatian": "hrv",
    "Bulgarian": "bul",
    "Slovak": "slk",
    "Ukrainian": "ukr",
    "Persian": "fas",
    "Pashto": "pus",
    "Kurdish": "kur",
    "Malayalam": "mal",
    "Sinhala": "sin",
    "Mongolian": "mon",
    "Nepali": "nep",
    "Zulu": "zul",
    "Xhosa": "xho",
    "Basque": "eus",
    "Catalan": "cat",
    "Galician": "glg",
    "Estonian": "est",
    "Lithuanian": "lit",
    "Latvian": "lav",
    "Macedonian": "mkd",
    "Albanian": "sqi",
    "Georgian": "kat",
    "Armenian": "hye",
    "Tajik": "tgk",
    "Turkmen": "tuk",
    "Kazakh": "kaz",
    "Uzbek": "uzb",
    "Kyrgyz": "kir",
    "Tatar": "tat",
    "Uighur": "uig",
    "Bashkir": "bak",
    "Chechen": "che",
    "Azerbaijani": "aze",
    "Belarusian": "bel",
    "Bosnian": "bos",
    "Luxembourgish": "ltz",
    "Icelandic": "isl",
    "Maltese": "mlt",
    "Welsh": "cym",
    "Irish": "gle",
    "Scottish Gaelic": "gla",
    "Breton": "bre",
    "Sami": "sme"
}
