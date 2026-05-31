"""
Latin GCSE Mastery Platform - Content Data
Vocabulary from the Eduqas specification (Appendix A).
Top 150 frequency order from school revision pack.

All English glosses on vocab cards MUST come from y11.OFFICIAL_GLOSSES.
Do not hardcode alternative wordings here.
"""

from OFFICIAL_GLOSSES import g as _g

STUDENTS_Y10 = [
    "Caz J", "Juno M", "Lauren M", "Eliza R", "Gianmarco S",
    "Alexa S", "Elijah S", "Sofia V", "Edea X", "Tom C",
    "Frankie C", "Mia C", "Defne E", "Avalon E", "Elda H",
    "Jana H"
]

# Legacy alias — keep for any import that still uses STUDENTS
STUDENTS = STUDENTS_Y10

# ── 1st Conjugation verbs - Top 150 only (13 verbs) ──────────────────────────
# Tuple: (present, infinitive, perfect, ppp_or_None, eng_present, eng_infinitive, eng_perfect, eng_ppp_or_None)
# festino, navigo, appropinquo have NO PPP.
VERBS_1ST_TOP150 = [
    ("amo",         "amare",         "amavi",         "amatus",         "I love",     "to love",     "I loved",      "having been loved"),
    ("clamo",       "clamare",       "clamavi",       "clamatus",       "I shout",    "to shout",    "I shouted",    "having been shouted"),
    ("festino",     "festinare",     "festinavi",     None,             "I hurry",    "to hurry",    "I hurried",    None),
    ("habito",      "habitare",      "habitavi",      "habitatus",      "I live",     "to live",     "I lived",      "having been inhabited"),
    ("impero",      "imperare",      "imperavi",      "imperatus",      "I order",    "to order",    "I ordered",    "having been ordered"),
    ("libero",      "liberare",      "liberavi",      "liberatus",      "I free",     "to free",     "I freed",      "having been freed"),
    ("neco",        "necare",        "necavi",        "necatus",        "I kill",     "to kill",     "I killed",     "having been killed"),
    ("navigo",      "navigare",      "navigavi",      None,             "I sail",     "to sail",     "I sailed",     None),
    ("oppugno",     "oppugnare",     "oppugnavi",     "oppugnatus",     "I attack",   "to attack",   "I attacked",   "having been attacked"),
    ("oro",         "orare",         "oravi",         "oratus",         "I beg",      "to beg",      "I begged",     "having been begged"),
    ("puto",        "putare",        "putavi",        "putatus",        "I think",    "to think",    "I thought",    "having been thought"),
    ("rogo",        "rogare",        "rogavi",        "rogatus",        "I ask",      "to ask",      "I asked",      "having been asked"),
    ("appropinquo", "appropinquare", "appropinquavi", None,             "I approach", "to approach", "I approached", None),
]

# ── Node 1 Sentence Vocabulary — everything NON-VERB for Node 1 ──────────────
# Verbs are taught via VERBS_1ST_TOP150 in the Present: 'I' Form tile.
# This list powers the Sentence Vocabulary tile (tile 3) and covers every
# non-verb lemma that appears in any of the 50 Node 1 sentences (sets 4/8/12/14/16).
# GLOSSES: all english strings come from OFFICIAL_GLOSSES via _g(lemma).
NODE1_VOCAB = [
    # Nouns
    {"id":"puella", "latin":"puella", "english":[_g("puella")], "pos":"noun",
     "derivatives":[
         {"word":"puerile", "meaning":"childish or silly — like a young girl or boy"},
     ]},
    {"id":"dea",    "latin":"dea",    "english":[_g("dea")],    "pos":"noun",
     "derivatives":[
         {"word":"deity",  "meaning":"a god or goddess"},
     ]},
    {"id":"femina", "latin":"femina", "english":[_g("femina")], "pos":"noun",
     "derivatives":[
         {"word":"feminine", "meaning":"womanly — having qualities associated with women"},
         {"word":"female",   "meaning":"a woman or girl"},
     ]},
    {"id":"pater",  "latin":"pater",  "english":[_g("pater")],  "pos":"noun",
     "derivatives":[
         {"word":"paternal",   "meaning":"to do with your father — e.g. paternal love"},
         {"word":"patriotism", "meaning":"love and support for your own country, your 'fatherland'"},
     ]},
    {"id":"filia",  "latin":"filia",  "english":[_g("filia")],  "pos":"noun",
     "derivatives":[
         {"word":"filial", "meaning":"relating to a son or daughter, e.g. filial love means a child's love for a parent"},
     ]},
    {"id":"insula", "latin":"insula", "english":[_g("insula")], "pos":"noun",
     "derivatives":[
         {"word":"insular",   "meaning":"island-like or isolated — cut off like an island"},
         {"word":"peninsula", "meaning":"land almost completely surrounded by water — paene means 'almost'"},
     ]},
    {"id":"regina", "latin":"regina", "english":[_g("regina")], "pos":"noun",
     "derivatives":[
         {"word":"regal",  "meaning":"fit for a queen or king, dignified and impressive"},
         {"word":"reign",  "meaning":"the period of time a ruler is in power"},
     ]},
    {"id":"deus",   "latin":"deus",   "english":[_g("deus")],   "pos":"noun",
     "derivatives":[
         {"word":"deity",  "meaning":"a god or goddess"},
         {"word":"divine", "meaning":"heavenly or godlike"},
     ]},
    {"id":"terra",  "latin":"terra",  "english":[_g("terra")],  "pos":"noun",
     "derivatives":[
         {"word":"terrestrial",    "meaning":"of the earth — living on land, not in water or the air"},
         {"word":"E.T. (extraterrestrial)", "meaning":"beyond the earth — extra means 'beyond'"},
         {"word":"terrace",        "meaning":"a flat raised area of ground, or a row of houses — from the Roman earthwork"},
     ]},
    {"id":"urbs",   "latin":"urbs",   "english":[_g("urbs")],   "pos":"noun",
     "derivatives":[
         {"word":"urban",  "meaning":"relating to a city, e.g. urban area"},
         {"word":"suburb", "meaning":"a residential area just outside a city. Sub means near or under."},
     ]},
    {"id":"navis",  "latin":"navis",  "english":[_g("navis")],  "pos":"noun",
     "derivatives":[
         {"word":"navy",     "meaning":"a country's fleet of warships"},
         {"word":"navigate", "meaning":"to plan and follow a route, especially by sea"},
         {"word":"naval",    "meaning":"relating to ships and the sea"},
     ]},
    {"id":"domum",  "latin":"domum",  "english":[_g("domum")],  "pos":"noun", "notes":"accusative of motion — no preposition needed",
     "derivatives":[
         {"word":"domestic", "meaning":"relating to the home, or to matters within a country"},
     ]},
    # Adjectives
    {"id":"pulcher", "latin":"pulcher", "english":[_g("pulcher")], "pos":"adjective"},
    {"id":"tristis", "latin":"tristis", "english":[_g("tristis")], "pos":"adjective"},
    {"id":"laetus",  "latin":"laetus",  "english":[_g("laetus")],  "pos":"adjective"},
    {"id":"ingens",  "latin":"ingens",  "english":[_g("ingens")],  "pos":"adjective"},
    {"id":"multus",  "latin":"multus",  "english":[_g("multus")],  "pos":"adjective",
     "derivatives":[
         {"word":"multiple",   "meaning":"more than one; existing in many forms"},
         {"word":"multiply",   "meaning":"to increase a number many times over"},
         {"word":"multitude",  "meaning":"a very large number of people or things"},
         {"word":"multimedia", "meaning":"using many different types of media: text, image, video, sound"},
     ]},
    # Pronouns
    {"id":"ego",  "latin":"ego",  "english":[_g("ego")],  "pos":"pronoun", "display_label":"nom",
     "derivatives":[
         {"word":"ego",      "meaning":"your sense of self-importance — 'I am the most important person'"},
         {"word":"egocentric","meaning":"thinking only about yourself, putting yourself at the centre"},
     ]},
    {"id":"me",   "latin":"me",   "english":[_g("me")],   "pos":"pronoun", "display_label":"acc"},
    {"id":"mihi", "latin":"mihi", "english":[_g("mihi")], "pos":"pronoun", "display_label":"dat"},
    # Prepositions
    {"id":"in_acc", "latin":"in",    "english":[_g("in + acc")], "pos":"preposition", "display_label":"+ acc"},
    {"id":"in_abl", "latin":"in",    "english":[_g("in + abl")], "pos":"preposition", "display_label":"+ abl"},
    {"id":"ad",     "latin":"ad",    "english":[_g("ad")],       "pos":"preposition", "display_label":"+ acc"},
    {"id":"per",    "latin":"per",   "english":[_g("per")],      "pos":"preposition", "display_label":"+ acc"},
    {"id":"prope",  "latin":"prope", "english":[_g("prope")],    "pos":"preposition", "display_label":"+ acc"},
    # Conjunctions
    {"id":"et",   "latin":"et",   "english":[_g("et")],  "pos":"conjunction",
     "derivatives":[
         {"word":"et cetera (etc.)", "meaning":"used in English to mean 'and so on'. It literally means 'and the rest'."},
     ]},
    {"id":"sed",  "latin":"sed",  "english":[_g("sed")], "pos":"conjunction"},
    {"id":"nam",  "latin":"nam",  "english":[_g("nam")], "pos":"conjunction", "notes":"used to give a reason"},
    {"id":"que",  "latin":"-que", "english":[_g("-que")],"pos":"conjunction", "notes":"clips onto the end of a word — translate 'and' BEFORE that word"},
    # Adverbs
    {"id":"non",    "latin":"non",    "english":[_g("non")],    "pos":"adverb",
     "derivatives":[
         {"word":"non-",     "meaning":"a prefix meaning 'not', e.g. 'non-fiction', 'non-stop', 'non-violent'"},
     ]},
    {"id":"ibi",    "latin":"ibi",    "english":[_g("ibi")],    "pos":"adverb"},
    {"id":"tum",    "latin":"tum",    "english":[_g("tum")],    "pos":"adverb"},
    {"id":"subito", "latin":"subito", "english":[_g("subito")], "pos":"adverb",
     "derivatives":[
         {"word":"subito",   "meaning":"used in music to mean 'suddenly', e.g. 'subito piano' means suddenly quiet"},
     ]},
    {"id":"etiam",  "latin":"etiam",  "english":[_g("etiam")],  "pos":"adverb"},
]

# ── Derivatives for verbs (keyed by present tense form) ──────────────────────
VERB_DERIVATIVES = {
    "amo": [
        {"word":"amorous",  "meaning":"feeling or showing romantic love"},
        {"word":"amateur",  "meaning":"someone who does something for love, not for money"},
    ],
    "clamo": [
        {"word":"clamour",  "meaning":"a loud uproar or insistent demand from a crowd"},
        {"word":"exclaim",  "meaning":"to shout out suddenly or with force"},
        {"word":"proclaim", "meaning":"to shout something publicly and officially"},
    ],
    "habito": [
        {"word":"habitat",  "meaning":"the natural home of an animal or plant — where it lives"},
        {"word":"inhabit",  "meaning":"to live in a place"},
    ],
    "impero": [
        {"word":"imperial",   "meaning":"giving orders like an emperor — grand and commanding"},
        {"word":"imperative", "meaning":"an order or command — something that must be done"},
    ],
    "libero": [
        {"word":"liberty",  "meaning":"freedom — the right to live as you choose"},
        {"word":"liberate", "meaning":"to set someone free"},
        {"word":"liberal",  "meaning":"believing in freedom, equality, and open-mindedness"},
    ],
    "navigo": [
        {"word":"navigate",   "meaning":"to sail or steer a course, especially by sea"},
        {"word":"navigation", "meaning":"the art of sailing and finding your way"},
    ],
    "oro": [
        {"word":"oration", "meaning":"a formal speech — especially one that begs or persuades"},
    ],
    "puto": [
        {"word":"compute",     "meaning":"to calculate — computers are 'thinking machines'"},
        {"word":"reputation",  "meaning":"what other people think of you"},
        {"word":"dispute",     "meaning":"an argument where two sides disagree"},
    ],
    "rogo": [
        {"word":"interrogate", "meaning":"to question someone closely and at length"},
    ],
}

# ── 'esse' set-piece forms — taught as vocabulary in every node's tile ──────
BE_FORMS = [
    {"id":"est",   "latin":"est",   "english":[_g("est")],   "pos":"verb_form", "notes":"a form of the verb 'to be'"},
    {"id":"sunt",  "latin":"sunt",  "english":[_g("sunt")],  "pos":"verb_form", "notes":"a form of the verb 'to be'"},
    {"id":"erat",  "latin":"erat",  "english":[_g("erat")],  "pos":"verb_form", "notes":"a form of the verb 'to be'"},
    {"id":"erant", "latin":"erant", "english":[_g("erant")], "pos":"verb_form", "notes":"a form of the verb 'to be'"},
]

# ── Tense ID questions - ALL perfect and pluperfect forms scaffolded ──────────
TENSE_ID_QUESTIONS = [
    # Present
    {"form":"rogat",          "plain":"rogat",          "tense":"present",    "translation":"he/she asks"},
    {"form":"clamo",          "plain":"clamo",          "tense":"present",    "translation":"I shout"},
    {"form":"habitant",       "plain":"habitant",       "tense":"present",    "translation":"they live"},
    {"form":"necant",         "plain":"necant",         "tense":"present",    "translation":"they kill"},
    {"form":"putat",          "plain":"putat",          "tense":"present",    "translation":"he/she thinks"},
    # Imperfect
    {"form":"amabat",         "plain":"amabat",         "tense":"imperfect",  "translation":"he/she was loving"},
    {"form":"necabant",       "plain":"necabant",       "tense":"imperfect",  "translation":"they were killing"},
    {"form":"navigabat",      "plain":"navigabat",      "tense":"imperfect",  "translation":"he/she was sailing"},
    {"form":"rogabant",       "plain":"rogabant",       "tense":"imperfect",  "translation":"they were asking"},
    {"form":"putabat",        "plain":"putabat",        "tense":"imperfect",  "translation":"he/she was thinking"},
    # Future
    {"form":"amabit",         "plain":"amabit",         "tense":"future",     "translation":"he/she will love"},
    {"form":"necabunt",       "plain":"necabunt",       "tense":"future",     "translation":"they will kill"},
    {"form":"rogabit",        "plain":"rogabit",        "tense":"future",     "translation":"he/she will ask"},
    {"form":"habitabunt",     "plain":"habitabunt",     "tense":"future",     "translation":"they will live"},
    {"form":"putabit",        "plain":"putabit",        "tense":"future",     "translation":"he/she will think"},
    # Perfect - all scaffolded with -v- marker
    {"form":"ama-v-it",       "plain":"amavit",         "tense":"perfect",    "translation":"he/she loved"},
    {"form":"festina-v-erunt","plain":"festinaverunt",  "tense":"perfect",    "translation":"they hurried"},
    {"form":"neca-v-erunt",   "plain":"necaverunt",     "tense":"perfect",    "translation":"they killed"},
    {"form":"libera-v-it",    "plain":"liberavit",      "tense":"perfect",    "translation":"he/she freed"},
    {"form":"oppugna-v-erunt","plain":"oppugnaverunt",  "tense":"perfect",    "translation":"they attacked"},
    {"form":"puta-v-it",      "plain":"putavit",        "tense":"perfect",    "translation":"he/she thought"},
    # Pluperfect - all scaffolded with -v- marker
    {"form":"ama-v-erat",     "plain":"amaverat",       "tense":"pluperfect", "translation":"he/she had loved"},
    {"form":"neca-v-erant",   "plain":"necaverant",     "tense":"pluperfect", "translation":"they had killed"},
    {"form":"naviga-v-erat",  "plain":"navigaverat",    "tense":"pluperfect", "translation":"he/she had sailed"},
    {"form":"oppugna-v-erant","plain":"oppugnaverant",  "tense":"pluperfect", "translation":"they had attacked"},
    {"form":"puta-v-erat",    "plain":"putaverat",      "tense":"pluperfect", "translation":"he/she had thought"},
]

# ── Parsing questions - all perfect forms scaffolded ─────────────────────────
PARSING_QUESTIONS = [
    # 3rd sg present
    {"form":"rogat",          "tense":"present",    "person":"3rd","number":"singular","translation":"he/she asks"},
    {"form":"orat",           "tense":"present",    "person":"3rd","number":"singular","translation":"he/she begs"},
    {"form":"oppugnat",       "tense":"present",    "person":"3rd","number":"singular","translation":"he/she attacks"},
    {"form":"liberat",        "tense":"present",    "person":"3rd","number":"singular","translation":"he/she frees"},
    {"form":"putat",          "tense":"present",    "person":"3rd","number":"singular","translation":"he/she thinks"},
    # 3rd pl present
    {"form":"navigant",       "tense":"present",    "person":"3rd","number":"plural",  "translation":"they sail"},
    {"form":"necant",         "tense":"present",    "person":"3rd","number":"plural",  "translation":"they kill"},
    {"form":"clamant",        "tense":"present",    "person":"3rd","number":"plural",  "translation":"they shout"},
    {"form":"putant",         "tense":"present",    "person":"3rd","number":"plural",  "translation":"they think"},
    # 3rd sg imperfect
    {"form":"amabat",         "tense":"imperfect",  "person":"3rd","number":"singular","translation":"he/she was loving"},
    {"form":"rogabat",        "tense":"imperfect",  "person":"3rd","number":"singular","translation":"he/she was asking"},
    {"form":"putabat",        "tense":"imperfect",  "person":"3rd","number":"singular","translation":"he/she was thinking"},
    # 3rd pl imperfect
    {"form":"navigabant",     "tense":"imperfect",  "person":"3rd","number":"plural",  "translation":"they were sailing"},
    {"form":"rogabant",       "tense":"imperfect",  "person":"3rd","number":"plural",  "translation":"they were asking"},
    # 3rd sg perfect - all scaffolded
    {"form":"ama-v-it",       "tense":"perfect",    "person":"3rd","number":"singular","translation":"he/she loved",    "scaffolded":True},
    {"form":"neca-v-it",      "tense":"perfect",    "person":"3rd","number":"singular","translation":"he/she killed",   "scaffolded":True},
    {"form":"libera-v-it",    "tense":"perfect",    "person":"3rd","number":"singular","translation":"he/she freed",    "scaffolded":True},
    {"form":"oppugna-v-it",   "tense":"perfect",    "person":"3rd","number":"singular","translation":"he/she attacked", "scaffolded":True},
    {"form":"festina-v-it",   "tense":"perfect",    "person":"3rd","number":"singular","translation":"he/she hurried",  "scaffolded":True},
    # 3rd pl perfect - all scaffolded
    {"form":"neca-v-erunt",   "tense":"perfect",    "person":"3rd","number":"plural",  "translation":"they killed",     "scaffolded":True},
    {"form":"naviga-v-erunt", "tense":"perfect",    "person":"3rd","number":"plural",  "translation":"they sailed",     "scaffolded":True},
    {"form":"oppugna-v-erunt","tense":"perfect",    "person":"3rd","number":"plural",  "translation":"they attacked",   "scaffolded":True},
]

# ── MCQ Translation questions (Translating Forms set) ────────────────────────
MCQ_QUESTIONS = [
    {"form":"ama-v-it",       "correct":"he/she loved",    "options":["he/she loves","he/she loved","they love","they loved"]},
    {"form":"necant",         "correct":"they kill",       "options":["he/she kills","he/she killed","they kill","they killed"]},
    {"form":"naviga-v-erunt", "correct":"they sailed",     "options":["he/she sails","he/she sailed","they sail","they sailed"]},
    {"form":"rogat",          "correct":"he/she asks",     "options":["he/she asks","he/she asked","they ask","they asked"]},
    {"form":"festina-v-it",   "correct":"he/she hurried",  "options":["he/she hurries","he/she hurried","they hurry","they hurried"]},
    {"form":"oppugna-v-erunt","correct":"they attacked",   "options":["he/she attacks","he/she attacked","they attack","they attacked"]},
    {"form":"imperat",        "correct":"he/she orders",   "options":["he/she orders","he/she ordered","they order","they ordered"]},
    {"form":"libera-v-it",    "correct":"he/she freed",    "options":["he/she frees","he/she freed","they free","they freed"]},
    {"form":"habitant",       "correct":"they live",       "options":["he/she lives","he/she lived","they live","they lived"]},
    {"form":"puta-v-erunt",   "correct":"they thought",    "options":["he/she thinks","he/she thought","they think","they thought"]},
    {"form":"orat",           "correct":"he/she begs",     "options":["he/she begs","he/she begged","they beg","they begged"]},
    {"form":"clama-v-it",     "correct":"he/she shouted",  "options":["he/she shouts","he/she shouted","they shout","they shouted"]},
]

# ── Present Tense Forms MCQ
# 6 options per question: all 6 person/number combos for one verb
# presented as a 3×2 grid (I / you / he-she-it  //  we / you pl / they)
QUESTIONS_PRESENT = [
    {"form": "amo",        "correct": "I love",           "options": ["I love","you (sg) love","he/she loves","we love","you (pl) love","they love"]},
    {"form": "amas",       "correct": "you (sg) love",    "options": ["I love","you (sg) love","he/she loves","we love","you (pl) love","they love"]},
    {"form": "amat",       "correct": "he/she loves",     "options": ["I love","you (sg) love","he/she loves","we love","you (pl) love","they love"]},
    {"form": "amamus",     "correct": "we love",          "options": ["I love","you (sg) love","he/she loves","we love","you (pl) love","they love"]},
    {"form": "amatis",     "correct": "you (pl) love",    "options": ["I love","you (sg) love","he/she loves","we love","you (pl) love","they love"]},
    {"form": "amant",      "correct": "they love",        "options": ["I love","you (sg) love","he/she loves","we love","you (pl) love","they love"]},
    {"form": "clamo",      "correct": "I shout",          "options": ["I shout","you (sg) shout","he/she shouts","we shout","you (pl) shout","they shout"]},
    {"form": "clamas",     "correct": "you (sg) shout",   "options": ["I shout","you (sg) shout","he/she shouts","we shout","you (pl) shout","they shout"]},
    {"form": "clamat",     "correct": "he/she shouts",    "options": ["I shout","you (sg) shout","he/she shouts","we shout","you (pl) shout","they shout"]},
    {"form": "clamamus",   "correct": "we shout",         "options": ["I shout","you (sg) shout","he/she shouts","we shout","you (pl) shout","they shout"]},
    {"form": "clamatis",   "correct": "you (pl) shout",   "options": ["I shout","you (sg) shout","he/she shouts","we shout","you (pl) shout","they shout"]},
    {"form": "clamant",    "correct": "they shout",       "options": ["I shout","you (sg) shout","he/she shouts","we shout","you (pl) shout","they shout"]},
    {"form": "rogo",       "correct": "I ask",            "options": ["I ask","you (sg) ask","he/she asks","we ask","you (pl) ask","they ask"]},
    {"form": "rogas",      "correct": "you (sg) ask",     "options": ["I ask","you (sg) ask","he/she asks","we ask","you (pl) ask","they ask"]},
    {"form": "rogat",      "correct": "he/she asks",      "options": ["I ask","you (sg) ask","he/she asks","we ask","you (pl) ask","they ask"]},
    {"form": "rogamus",    "correct": "we ask",           "options": ["I ask","you (sg) ask","he/she asks","we ask","you (pl) ask","they ask"]},
    {"form": "rogatis",    "correct": "you (pl) ask",     "options": ["I ask","you (sg) ask","he/she asks","we ask","you (pl) ask","they ask"]},
    {"form": "rogant",     "correct": "they ask",         "options": ["I ask","you (sg) ask","he/she asks","we ask","you (pl) ask","they ask"]},
    {"form": "festino",    "correct": "I hurry",          "options": ["I hurry","you (sg) hurry","he/she hurries","we hurry","you (pl) hurry","they hurry"]},
    {"form": "festinas",   "correct": "you (sg) hurry",   "options": ["I hurry","you (sg) hurry","he/she hurries","we hurry","you (pl) hurry","they hurry"]},
    {"form": "festinat",   "correct": "he/she hurries",   "options": ["I hurry","you (sg) hurry","he/she hurries","we hurry","you (pl) hurry","they hurry"]},
    {"form": "festinamus", "correct": "we hurry",         "options": ["I hurry","you (sg) hurry","he/she hurries","we hurry","you (pl) hurry","they hurry"]},
    {"form": "festinatis", "correct": "you (pl) hurry",   "options": ["I hurry","you (sg) hurry","he/she hurries","we hurry","you (pl) hurry","they hurry"]},
    {"form": "festinant",  "correct": "they hurry",       "options": ["I hurry","you (sg) hurry","he/she hurries","we hurry","you (pl) hurry","they hurry"]},
    {"form": "neco",       "correct": "I kill",           "options": ["I kill","you (sg) kill","he/she kills","we kill","you (pl) kill","they kill"]},
    {"form": "necas",      "correct": "you (sg) kill",    "options": ["I kill","you (sg) kill","he/she kills","we kill","you (pl) kill","they kill"]},
    {"form": "necat",      "correct": "he/she kills",     "options": ["I kill","you (sg) kill","he/she kills","we kill","you (pl) kill","they kill"]},
    {"form": "necamus",    "correct": "we kill",          "options": ["I kill","you (sg) kill","he/she kills","we kill","you (pl) kill","they kill"]},
    {"form": "necatis",    "correct": "you (pl) kill",    "options": ["I kill","you (sg) kill","he/she kills","we kill","you (pl) kill","they kill"]},
    {"form": "necant",     "correct": "they kill",        "options": ["I kill","you (sg) kill","he/she kills","we kill","you (pl) kill","they kill"]},
    {"form": "libero",     "correct": "I free",           "options": ["I free","you (sg) free","he/she frees","we free","you (pl) free","they free"]},
    {"form": "liberas",    "correct": "you (sg) free",    "options": ["I free","you (sg) free","he/she frees","we free","you (pl) free","they free"]},
    {"form": "liberat",    "correct": "he/she frees",     "options": ["I free","you (sg) free","he/she frees","we free","you (pl) free","they free"]},
    {"form": "liberamus",  "correct": "we free",          "options": ["I free","you (sg) free","he/she frees","we free","you (pl) free","they free"]},
    {"form": "liberatis",  "correct": "you (pl) free",    "options": ["I free","you (sg) free","he/she frees","we free","you (pl) free","they free"]},
    {"form": "liberant",   "correct": "they free",        "options": ["I free","you (sg) free","he/she frees","we free","you (pl) free","they free"]},
    {"form": "puto",       "correct": "I think",          "options": ["I think","you (sg) think","he/she thinks","we think","you (pl) think","they think"]},
    {"form": "putas",      "correct": "you (sg) think",   "options": ["I think","you (sg) think","he/she thinks","we think","you (pl) think","they think"]},
    {"form": "putat",      "correct": "he/she thinks",    "options": ["I think","you (sg) think","he/she thinks","we think","you (pl) think","they think"]},
    {"form": "putamus",    "correct": "we think",         "options": ["I think","you (sg) think","he/she thinks","we think","you (pl) think","they think"]},
    {"form": "putatis",    "correct": "you (pl) think",   "options": ["I think","you (sg) think","he/she thinks","we think","you (pl) think","they think"]},
    {"form": "putant",     "correct": "they think",       "options": ["I think","you (sg) think","he/she thinks","we think","you (pl) think","they think"]},
]

QUESTIONS_IMPERFECT = [
    {"form": "amabam",       "correct": "I was loving",          "options": ["I was loving","you (sg) were loving","he/she was loving","we were loving","you (pl) were loving","they were loving"]},
    {"form": "amabas",       "correct": "you (sg) were loving",  "options": ["I was loving","you (sg) were loving","he/she was loving","we were loving","you (pl) were loving","they were loving"]},
    {"form": "amabat",       "correct": "he/she was loving",     "options": ["I was loving","you (sg) were loving","he/she was loving","we were loving","you (pl) were loving","they were loving"]},
    {"form": "amabamus",     "correct": "we were loving",        "options": ["I was loving","you (sg) were loving","he/she was loving","we were loving","you (pl) were loving","they were loving"]},
    {"form": "amabatis",     "correct": "you (pl) were loving",  "options": ["I was loving","you (sg) were loving","he/she was loving","we were loving","you (pl) were loving","they were loving"]},
    {"form": "amabant",      "correct": "they were loving",      "options": ["I was loving","you (sg) were loving","he/she was loving","we were loving","you (pl) were loving","they were loving"]},
    {"form": "clamabam",     "correct": "I was shouting",        "options": ["I was shouting","you (sg) were shouting","he/she was shouting","we were shouting","you (pl) were shouting","they were shouting"]},
    {"form": "clamabas",     "correct": "you (sg) were shouting","options": ["I was shouting","you (sg) were shouting","he/she was shouting","we were shouting","you (pl) were shouting","they were shouting"]},
    {"form": "clamabat",     "correct": "he/she was shouting",   "options": ["I was shouting","you (sg) were shouting","he/she was shouting","we were shouting","you (pl) were shouting","they were shouting"]},
    {"form": "clamabamus",   "correct": "we were shouting",      "options": ["I was shouting","you (sg) were shouting","he/she was shouting","we were shouting","you (pl) were shouting","they were shouting"]},
    {"form": "clamabatis",   "correct": "you (pl) were shouting","options": ["I was shouting","you (sg) were shouting","he/she was shouting","we were shouting","you (pl) were shouting","they were shouting"]},
    {"form": "clamabant",    "correct": "they were shouting",    "options": ["I was shouting","you (sg) were shouting","he/she was shouting","we were shouting","you (pl) were shouting","they were shouting"]},
    {"form": "rogabam",      "correct": "I was asking",          "options": ["I was asking","you (sg) were asking","he/she was asking","we were asking","you (pl) were asking","they were asking"]},
    {"form": "rogabas",      "correct": "you (sg) were asking",  "options": ["I was asking","you (sg) were asking","he/she was asking","we were asking","you (pl) were asking","they were asking"]},
    {"form": "rogabat",      "correct": "he/she was asking",     "options": ["I was asking","you (sg) were asking","he/she was asking","we were asking","you (pl) were asking","they were asking"]},
    {"form": "rogabamus",    "correct": "we were asking",        "options": ["I was asking","you (sg) were asking","he/she was asking","we were asking","you (pl) were asking","they were asking"]},
    {"form": "rogabatis",    "correct": "you (pl) were asking",  "options": ["I was asking","you (sg) were asking","he/she was asking","we were asking","you (pl) were asking","they were asking"]},
    {"form": "rogabant",     "correct": "they were asking",      "options": ["I was asking","you (sg) were asking","he/she was asking","we were asking","you (pl) were asking","they were asking"]},
    {"form": "necabam",      "correct": "I was killing",         "options": ["I was killing","you (sg) were killing","he/she was killing","we were killing","you (pl) were killing","they were killing"]},
    {"form": "necabas",      "correct": "you (sg) were killing", "options": ["I was killing","you (sg) were killing","he/she was killing","we were killing","you (pl) were killing","they were killing"]},
    {"form": "necabat",      "correct": "he/she was killing",    "options": ["I was killing","you (sg) were killing","he/she was killing","we were killing","you (pl) were killing","they were killing"]},
    {"form": "necabamus",    "correct": "we were killing",       "options": ["I was killing","you (sg) were killing","he/she was killing","we were killing","you (pl) were killing","they were killing"]},
    {"form": "necabatis",    "correct": "you (pl) were killing", "options": ["I was killing","you (sg) were killing","he/she was killing","we were killing","you (pl) were killing","they were killing"]},
    {"form": "necabant",     "correct": "they were killing",     "options": ["I was killing","you (sg) were killing","he/she was killing","we were killing","you (pl) were killing","they were killing"]},
    {"form": "festinabam",   "correct": "I was hurrying",        "options": ["I was hurrying","you (sg) were hurrying","he/she was hurrying","we were hurrying","you (pl) were hurrying","they were hurrying"]},
    {"form": "festinabas",   "correct": "you (sg) were hurrying","options": ["I was hurrying","you (sg) were hurrying","he/she was hurrying","we were hurrying","you (pl) were hurrying","they were hurrying"]},
    {"form": "festinabat",   "correct": "he/she was hurrying",   "options": ["I was hurrying","you (sg) were hurrying","he/she was hurrying","we were hurrying","you (pl) were hurrying","they were hurrying"]},
    {"form": "festinabamus", "correct": "we were hurrying",      "options": ["I was hurrying","you (sg) were hurrying","he/she was hurrying","we were hurrying","you (pl) were hurrying","they were hurrying"]},
    {"form": "festinabatis", "correct": "you (pl) were hurrying","options": ["I was hurrying","you (sg) were hurrying","he/she was hurrying","we were hurrying","you (pl) were hurrying","they were hurrying"]},
    {"form": "festinabant",  "correct": "they were hurrying",    "options": ["I was hurrying","you (sg) were hurrying","he/she was hurrying","we were hurrying","you (pl) were hurrying","they were hurrying"]},
    {"form": "putabam",      "correct": "I was thinking",        "options": ["I was thinking","you (sg) were thinking","he/she was thinking","we were thinking","you (pl) were thinking","they were thinking"]},
    {"form": "putabas",      "correct": "you (sg) were thinking","options": ["I was thinking","you (sg) were thinking","he/she was thinking","we were thinking","you (pl) were thinking","they were thinking"]},
    {"form": "putabat",      "correct": "he/she was thinking",   "options": ["I was thinking","you (sg) were thinking","he/she was thinking","we were thinking","you (pl) were thinking","they were thinking"]},
    {"form": "putabamus",    "correct": "we were thinking",      "options": ["I was thinking","you (sg) were thinking","he/she was thinking","we were thinking","you (pl) were thinking","they were thinking"]},
    {"form": "putabatis",    "correct": "you (pl) were thinking","options": ["I was thinking","you (sg) were thinking","he/she was thinking","we were thinking","you (pl) were thinking","they were thinking"]},
    {"form": "putabant",     "correct": "they were thinking",    "options": ["I was thinking","you (sg) were thinking","he/she was thinking","we were thinking","you (pl) were thinking","they were thinking"]},
]

QUESTIONS_FUTURE = [
    {"form": "amabo",       "correct": "I will love",          "options": ["I will love","you (sg) will love","he/she will love","we will love","you (pl) will love","they will love"]},
    {"form": "amabis",      "correct": "you (sg) will love",   "options": ["I will love","you (sg) will love","he/she will love","we will love","you (pl) will love","they will love"]},
    {"form": "amabit",      "correct": "he/she will love",     "options": ["I will love","you (sg) will love","he/she will love","we will love","you (pl) will love","they will love"]},
    {"form": "amabimus",    "correct": "we will love",         "options": ["I will love","you (sg) will love","he/she will love","we will love","you (pl) will love","they will love"]},
    {"form": "amabitis",    "correct": "you (pl) will love",   "options": ["I will love","you (sg) will love","he/she will love","we will love","you (pl) will love","they will love"]},
    {"form": "amabunt",     "correct": "they will love",       "options": ["I will love","you (sg) will love","he/she will love","we will love","you (pl) will love","they will love"]},
    {"form": "clamabo",     "correct": "I will shout",         "options": ["I will shout","you (sg) will shout","he/she will shout","we will shout","you (pl) will shout","they will shout"]},
    {"form": "clamabis",    "correct": "you (sg) will shout",  "options": ["I will shout","you (sg) will shout","he/she will shout","we will shout","you (pl) will shout","they will shout"]},
    {"form": "clamabit",    "correct": "he/she will shout",    "options": ["I will shout","you (sg) will shout","he/she will shout","we will shout","you (pl) will shout","they will shout"]},
    {"form": "clamabimus",  "correct": "we will shout",        "options": ["I will shout","you (sg) will shout","he/she will shout","we will shout","you (pl) will shout","they will shout"]},
    {"form": "clamabitis",  "correct": "you (pl) will shout",  "options": ["I will shout","you (sg) will shout","he/she will shout","we will shout","you (pl) will shout","they will shout"]},
    {"form": "clamabunt",   "correct": "they will shout",      "options": ["I will shout","you (sg) will shout","he/she will shout","we will shout","you (pl) will shout","they will shout"]},
    {"form": "rogabo",      "correct": "I will ask",           "options": ["I will ask","you (sg) will ask","he/she will ask","we will ask","you (pl) will ask","they will ask"]},
    {"form": "rogabis",     "correct": "you (sg) will ask",    "options": ["I will ask","you (sg) will ask","he/she will ask","we will ask","you (pl) will ask","they will ask"]},
    {"form": "rogabit",     "correct": "he/she will ask",      "options": ["I will ask","you (sg) will ask","he/she will ask","we will ask","you (pl) will ask","they will ask"]},
    {"form": "rogabimus",   "correct": "we will ask",          "options": ["I will ask","you (sg) will ask","he/she will ask","we will ask","you (pl) will ask","they will ask"]},
    {"form": "rogabitis",   "correct": "you (pl) will ask",    "options": ["I will ask","you (sg) will ask","he/she will ask","we will ask","you (pl) will ask","they will ask"]},
    {"form": "rogabunt",    "correct": "they will ask",        "options": ["I will ask","you (sg) will ask","he/she will ask","we will ask","you (pl) will ask","they will ask"]},
    {"form": "necabo",      "correct": "I will kill",          "options": ["I will kill","you (sg) will kill","he/she will kill","we will kill","you (pl) will kill","they will kill"]},
    {"form": "necabis",     "correct": "you (sg) will kill",   "options": ["I will kill","you (sg) will kill","he/she will kill","we will kill","you (pl) will kill","they will kill"]},
    {"form": "necabit",     "correct": "he/she will kill",     "options": ["I will kill","you (sg) will kill","he/she will kill","we will kill","you (pl) will kill","they will kill"]},
    {"form": "necabimus",   "correct": "we will kill",         "options": ["I will kill","you (sg) will kill","he/she will kill","we will kill","you (pl) will kill","they will kill"]},
    {"form": "necabitis",   "correct": "you (pl) will kill",   "options": ["I will kill","you (sg) will kill","he/she will kill","we will kill","you (pl) will kill","they will kill"]},
    {"form": "necabunt",    "correct": "they will kill",       "options": ["I will kill","you (sg) will kill","he/she will kill","we will kill","you (pl) will kill","they will kill"]},
    {"form": "putabo",      "correct": "I will think",         "options": ["I will think","you (sg) will think","he/she will think","we will think","you (pl) will think","they will think"]},
    {"form": "putabis",     "correct": "you (sg) will think",  "options": ["I will think","you (sg) will think","he/she will think","we will think","you (pl) will think","they will think"]},
    {"form": "putabit",     "correct": "he/she will think",    "options": ["I will think","you (sg) will think","he/she will think","we will think","you (pl) will think","they will think"]},
    {"form": "putabimus",   "correct": "we will think",        "options": ["I will think","you (sg) will think","he/she will think","we will think","you (pl) will think","they will think"]},
    {"form": "putabitis",   "correct": "you (pl) will think",  "options": ["I will think","you (sg) will think","he/she will think","we will think","you (pl) will think","they will think"]},
    {"form": "putabunt",    "correct": "they will think",      "options": ["I will think","you (sg) will think","he/she will think","we will think","you (pl) will think","they will think"]},
]

QUESTIONS_PERFECT = [
    {"form": "amavi",       "correct": "I loved",              "options": ["I loved","you (sg) loved","he/she loved","we loved","you (pl) loved","they loved"]},
    {"form": "amavisti",    "correct": "you (sg) loved",       "options": ["I loved","you (sg) loved","he/she loved","we loved","you (pl) loved","they loved"]},
    {"form": "amavit",      "correct": "he/she loved",         "options": ["I loved","you (sg) loved","he/she loved","we loved","you (pl) loved","they loved"]},
    {"form": "amavimus",    "correct": "we loved",             "options": ["I loved","you (sg) loved","he/she loved","we loved","you (pl) loved","they loved"]},
    {"form": "amavistis",   "correct": "you (pl) loved",       "options": ["I loved","you (sg) loved","he/she loved","we loved","you (pl) loved","they loved"]},
    {"form": "amaverunt",   "correct": "they loved",           "options": ["I loved","you (sg) loved","he/she loved","we loved","you (pl) loved","they loved"]},
    {"form": "necavi",      "correct": "I killed",             "options": ["I killed","you (sg) killed","he/she killed","we killed","you (pl) killed","they killed"]},
    {"form": "necavisti",   "correct": "you (sg) killed",      "options": ["I killed","you (sg) killed","he/she killed","we killed","you (pl) killed","they killed"]},
    {"form": "necavit",     "correct": "he/she killed",        "options": ["I killed","you (sg) killed","he/she killed","we killed","you (pl) killed","they killed"]},
    {"form": "necavimus",   "correct": "we killed",            "options": ["I killed","you (sg) killed","he/she killed","we killed","you (pl) killed","they killed"]},
    {"form": "necavistis",  "correct": "you (pl) killed",      "options": ["I killed","you (sg) killed","he/she killed","we killed","you (pl) killed","they killed"]},
    {"form": "necaverunt",  "correct": "they killed",          "options": ["I killed","you (sg) killed","he/she killed","we killed","you (pl) killed","they killed"]},
    {"form": "rogavi",      "correct": "I asked",              "options": ["I asked","you (sg) asked","he/she asked","we asked","you (pl) asked","they asked"]},
    {"form": "rogavisti",   "correct": "you (sg) asked",       "options": ["I asked","you (sg) asked","he/she asked","we asked","you (pl) asked","they asked"]},
    {"form": "rogavit",     "correct": "he/she asked",         "options": ["I asked","you (sg) asked","he/she asked","we asked","you (pl) asked","they asked"]},
    {"form": "rogavimus",   "correct": "we asked",             "options": ["I asked","you (sg) asked","he/she asked","we asked","you (pl) asked","they asked"]},
    {"form": "rogavistis",  "correct": "you (pl) asked",       "options": ["I asked","you (sg) asked","he/she asked","we asked","you (pl) asked","they asked"]},
    {"form": "rogaverunt",  "correct": "they asked",           "options": ["I asked","you (sg) asked","he/she asked","we asked","you (pl) asked","they asked"]},
    {"form": "festinavi",   "correct": "I hurried",            "options": ["I hurried","you (sg) hurried","he/she hurried","we hurried","you (pl) hurried","they hurried"]},
    {"form": "festinavisti","correct": "you (sg) hurried",     "options": ["I hurried","you (sg) hurried","he/she hurried","we hurried","you (pl) hurried","they hurried"]},
    {"form": "festinavit",  "correct": "he/she hurried",       "options": ["I hurried","you (sg) hurried","he/she hurried","we hurried","you (pl) hurried","they hurried"]},
    {"form": "festinavimus","correct": "we hurried",           "options": ["I hurried","you (sg) hurried","he/she hurried","we hurried","you (pl) hurried","they hurried"]},
    {"form": "festinavistis","correct":"you (pl) hurried",     "options": ["I hurried","you (sg) hurried","he/she hurried","we hurried","you (pl) hurried","they hurried"]},
    {"form": "festinaverunt","correct":"they hurried",         "options": ["I hurried","you (sg) hurried","he/she hurried","we hurried","you (pl) hurried","they hurried"]},
    {"form": "putavi",      "correct": "I thought",            "options": ["I thought","you (sg) thought","he/she thought","we thought","you (pl) thought","they thought"]},
    {"form": "putavisti",   "correct": "you (sg) thought",     "options": ["I thought","you (sg) thought","he/she thought","we thought","you (pl) thought","they thought"]},
    {"form": "putavit",     "correct": "he/she thought",       "options": ["I thought","you (sg) thought","he/she thought","we thought","you (pl) thought","they thought"]},
    {"form": "putavimus",   "correct": "we thought",           "options": ["I thought","you (sg) thought","he/she thought","we thought","you (pl) thought","they thought"]},
    {"form": "putavistis",  "correct": "you (pl) thought",     "options": ["I thought","you (sg) thought","he/she thought","we thought","you (pl) thought","they thought"]},
    {"form": "putaverunt",  "correct": "they thought",         "options": ["I thought","you (sg) thought","he/she thought","we thought","you (pl) thought","they thought"]},
]

QUESTIONS_PLUPERFECT = [
    {"form": "amaveram",    "correct": "I had loved",          "options": ["I had loved","you (sg) had loved","he/she had loved","we had loved","you (pl) had loved","they had loved"]},
    {"form": "amaveras",    "correct": "you (sg) had loved",   "options": ["I had loved","you (sg) had loved","he/she had loved","we had loved","you (pl) had loved","they had loved"]},
    {"form": "amaverat",    "correct": "he/she had loved",     "options": ["I had loved","you (sg) had loved","he/she had loved","we had loved","you (pl) had loved","they had loved"]},
    {"form": "amaveramus",  "correct": "we had loved",         "options": ["I had loved","you (sg) had loved","he/she had loved","we had loved","you (pl) had loved","they had loved"]},
    {"form": "amaveratis",  "correct": "you (pl) had loved",   "options": ["I had loved","you (sg) had loved","he/she had loved","we had loved","you (pl) had loved","they had loved"]},
    {"form": "amaverant",   "correct": "they had loved",       "options": ["I had loved","you (sg) had loved","he/she had loved","we had loved","you (pl) had loved","they had loved"]},
    {"form": "necaveram",   "correct": "I had killed",         "options": ["I had killed","you (sg) had killed","he/she had killed","we had killed","you (pl) had killed","they had killed"]},
    {"form": "necaveras",   "correct": "you (sg) had killed",  "options": ["I had killed","you (sg) had killed","he/she had killed","we had killed","you (pl) had killed","they had killed"]},
    {"form": "necaverat",   "correct": "he/she had killed",    "options": ["I had killed","you (sg) had killed","he/she had killed","we had killed","you (pl) had killed","they had killed"]},
    {"form": "necaveramus", "correct": "we had killed",        "options": ["I had killed","you (sg) had killed","he/she had killed","we had killed","you (pl) had killed","they had killed"]},
    {"form": "necaveratis", "correct": "you (pl) had killed",  "options": ["I had killed","you (sg) had killed","he/she had killed","we had killed","you (pl) had killed","they had killed"]},
    {"form": "necaverant",  "correct": "they had killed",      "options": ["I had killed","you (sg) had killed","he/she had killed","we had killed","you (pl) had killed","they had killed"]},
    {"form": "rogaveram",   "correct": "I had asked",          "options": ["I had asked","you (sg) had asked","he/she had asked","we had asked","you (pl) had asked","they had asked"]},
    {"form": "rogaveras",   "correct": "you (sg) had asked",   "options": ["I had asked","you (sg) had asked","he/she had asked","we had asked","you (pl) had asked","they had asked"]},
    {"form": "rogaverat",   "correct": "he/she had asked",     "options": ["I had asked","you (sg) had asked","he/she had asked","we had asked","you (pl) had asked","they had asked"]},
    {"form": "rogaveramus", "correct": "we had asked",         "options": ["I had asked","you (sg) had asked","he/she had asked","we had asked","you (pl) had asked","they had asked"]},
    {"form": "rogaveratis", "correct": "you (pl) had asked",   "options": ["I had asked","you (sg) had asked","he/she had asked","we had asked","you (pl) had asked","they had asked"]},
    {"form": "rogaverant",  "correct": "they had asked",       "options": ["I had asked","you (sg) had asked","he/she had asked","we had asked","you (pl) had asked","they had asked"]},
    {"form": "putaveram",   "correct": "I had thought",        "options": ["I had thought","you (sg) had thought","he/she had thought","we had thought","you (pl) had thought","they had thought"]},
    {"form": "putaveras",   "correct": "you (sg) had thought", "options": ["I had thought","you (sg) had thought","he/she had thought","we had thought","you (pl) had thought","they had thought"]},
    {"form": "putaverat",   "correct": "he/she had thought",   "options": ["I had thought","you (sg) had thought","he/she had thought","we had thought","you (pl) had thought","they had thought"]},
    {"form": "putaveramus", "correct": "we had thought",       "options": ["I had thought","you (sg) had thought","he/she had thought","we had thought","you (pl) had thought","they had thought"]},
    {"form": "putaveratis", "correct": "you (pl) had thought", "options": ["I had thought","you (sg) had thought","he/she had thought","we had thought","you (pl) had thought","they had thought"]},
    {"form": "putaverant",  "correct": "they had thought",     "options": ["I had thought","you (sg) had thought","he/she had thought","we had thought","you (pl) had thought","they had thought"]},
]

# ── Sentence sets ─────────────────────────────────────────────────────────────

SENTENCES_PRESENT_TEST = [
    {
        "latin": "puella deam amat.",
        "english": [
            "The girl loves the goddess.",
            "The girl is loving the goddess.",
            "The girl likes the goddess.",
            "The girl does love the goddess.",
            "A girl loves a goddess.",
            "A girl loves the goddess.",
            "The girl loves a goddess.",
            "A girl likes the goddess.",
            "The girl likes a goddess.",
            "A girl is loving the goddess.",
        ],
        "explanation": (
            "• puella (the girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• am{R:a}{B:t} (loves)\n"
            "  → *amo* (I love) is the dictionary form of this verb\n"
            "  → *am-* (love) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• deam (the goddess)\n"
            "  → *de{T:am}* (goddess) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "pater filiam rogat.",
        "english": [
            "The father asks the daughter.",
            "The father asks his daughter.",
            "The father questions the daughter.",
            "The father is asking the daughter.",
            "The father questions his daughter.",
            "The father is questioning the daughter.",
            "The father does ask the daughter.",
            "The father is asking his daughter.",
            "A father asks the daughter.",
            "The father asks a daughter.",
            "A father asks a daughter.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• rog{R:a}{B:t} (asks)\n"
            "  → *rogo* (I ask) is the dictionary form of this verb\n"
            "  → *rog-* (ask) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• filiam (the daughter)\n"
            "  → *fili{T:am}* (daughter) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "femina in insula habitat.",
        "english": [
            "The woman lives on the island.",
            "The woman is living on the island.",
            "The woman lives in the island.",
            "The woman dwells on the island.",
            "The woman is dwelling on the island.",
            "The woman inhabits the island.",
            "The woman does live on the island.",
            "A woman lives on an island.",
            "A woman is living on the island.",
            "A woman lives on the island.",
            "The woman lives on an island.",
            "The woman lives in an island.",
        ],
        "explanation": (
            "• femina (the woman)\n"
            "  → *femin{T:a}* (woman) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• habit{R:a}{B:t} (lives)\n"
            "  → *habito* (I live) is the dictionary form of this verb\n"
            "  → *habit-* (live) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• in insula (on the island)\n"
            "  → *in* (in or on) is a preposition\n"
            "  → *in* + {T:ablative} can mean 'in' or 'on'\n"
            "  → *insul{T:a}* (island) is a noun, 1st declension feminine singular {T:ablative}"
        ),
    },
    {
        "latin": "dea pulchra ad terram navigat.",
        "english": [
            "The beautiful goddess sails towards the land.",
            "The beautiful goddess sails to the land.",
            "The beautiful goddess is sailing towards the land.",
            "The beautiful goddess is sailing to the land.",
            "The lovely goddess sails to the land.",
            "The lovely goddess sails towards the land.",
            "The pretty goddess sails to the land.",
            "The beautiful goddess sails to the country.",
            "The beautiful goddess sails towards the country.",
            "The beautiful goddess is sailing to the country.",
            "The beautiful goddess voyages to the land.",
            "The beautiful goddess does sail to the land.",
            "A beautiful goddess sails towards the country.",
            "A beautiful goddess sails to the land.",
        ],
        "explanation": (
            "• dea pulchra (the beautiful goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pulchra* (beautiful) is an adjective, and agrees with *dea* (goddess) because they are both feminine singular {T:nominative}\n"
            "• navig{R:a}{B:t} (sails)\n"
            "  → *navigo* (I sail) is the dictionary form of this verb\n"
            "  → *navig-* (sail) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• ad terram (towards the land)\n"
            "  → *ad* (to / towards) is a preposition\n"
            "  → *ad* + {T:accusative} means 'to' or 'towards'\n"
            "  → *terr{T:am}* (land) is a noun, 1st declension feminine singular {T:accusative}"
        ),
    },
    {
        "latin": "regina tristis clamat, nam deus appropinquat.",
        "english": [
            "The sad queen shouts, for the god approaches.",
            "The sad queen is shouting, for the god is approaching.",
            "The unhappy queen shouts, because the god approaches.",
            "The sad queen shouts, for the god draws near.",
            "The sad queen cries out, for the god approaches.",
            "The sad queen calls out, for the god approaches.",
            "The sorrowful queen shouts, for the god approaches.",
            "The unhappy queen is shouting, because the god is approaching.",
            "The sad queen shouts, because the god approaches.",
            "The sad queen shouts, because the god is approaching.",
            "The sad queen shouts, for the god comes near.",
            "The sad queen shouts, for the god is drawing near.",
            "The sad queen does shout, for the god approaches.",
            "The sad queen shouts, for the god does approach.",
        ],
        "explanation": (
            "• regina tristis (the sad queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *tristis* (sad) is an adjective, and agrees with *regina* (queen) because they are both feminine singular {T:nominative}\n"
            "• clam{R:a}{B:t} (shouts)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• nam (for)\n"
            "  → *nam* (for or because) is a conjunction\n"
            "• deus (the god)\n"
            "  → *de{T:us}* (god) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• appropinqu{R:a}{B:t} (approaches)\n"
            "  → *appropinquo* (I approach) is the dictionary form of this verb\n"
            "  → *appropinqu-* (approach) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "puella laeta patri imperat, et pater festinat.",
        "english": [
            "The happy girl orders the father, and the father hurries.",
            "The happy girl orders her father, and the father hurries.",
            "The joyful girl orders the father, and the father rushes.",
            "The happy girl is ordering the father, and the father is hurrying.",
            "The happy girl commands the father, and the father hurries.",
            "The happy girl commands her father, and the father hurries.",
            "The glad girl orders the father, and the father hurries.",
            "The cheerful girl orders the father, and the father hurries.",
            "The happy girl orders the father, and the father hastens.",
            "The happy girl orders the father, and the father rushes.",
            "The happy girl is commanding the father, and the father is hurrying.",
            "The joyful girl orders her father, and her father rushes.",
            "The happy girl does order the father, and the father does hurry.",
        ],
        "explanation": (
            "• puella laeta (the happy girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *laeta* (happy) is an adjective, and agrees with *puella* (girl) because they are both feminine singular {T:nominative}\n"
            "• patri (the father)\n"
            "  → *patr{T:i}* (father) is a noun, 3rd declension masculine singular {T:dative}\n"
            "  → *impero* takes the {T:dative}: the person being ordered is dative, not accusative\n"
            "• imper{R:a}{B:t} (orders)\n"
            "  → *impero* (I order) is the dictionary form of this verb\n"
            "  → *imper-* (order) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• festin{R:a}{B:t} (hurries)\n"
            "  → *festino* (I hurry) is the dictionary form of this verb\n"
            "  → *festin-* (hurry) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "ego feminam oro, sed dea non clamat.",
        "english": [
            "I beg the woman, but the goddess does not shout.",
            "I beg the woman, but the goddess is not shouting.",
            "I myself beg the woman, but the goddess does not shout.",
            "I plead with the woman, but the goddess does not shout.",
            "I beg the woman, but the goddess is not crying out.",
            "I beg the woman, but the goddess does not cry out.",
            "I beg the woman, but the goddess does not call out.",
            "I am begging the woman, but the goddess is not shouting.",
            "I am begging the woman, but the goddess does not shout.",
            "I pray to the woman, but the goddess does not shout.",
            "I plead with the woman, but the goddess is not shouting.",
            "I myself am begging the woman, but the goddess is not shouting.",
            "I do beg the woman, but the goddess does not shout.",
        ],
        "explanation": (
            "• ego (I)\n"
            "  → *ego* (I) is a pronoun — it is already the {N:subject} so the verb ending repeats this\n"
            "• or{B:o} (beg)\n"
            "  → *oro* (I beg) is the dictionary form of this verb\n"
            "  → *or-* (beg) is the stem\n"
            "  → *-{B:o}* shows it is the I form\n"
            "• feminam (the woman)\n"
            "  → *femin{T:am}* (woman) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• dea (the goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• non clam{R:a}{B:t} (does not shout)\n"
            "  → *non* (not) negates the verb\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "multi dei insulam oppugnant, et ibi feminae clamant.",
        "english": [
            "Many gods attack the island, and there the women shout.",
            "Many gods are attacking the island, and there the women are shouting.",
            "Many of the gods attack the island, and the women are shouting there.",
            "Many gods attack the island, and the women shout there.",
            "Many gods assault the island, and there the women shout.",
            "Many gods besiege the island, and there the women shout.",
            "Many gods attack the island, and there the women cry out.",
            "Many gods attack the island, and there the women call out.",
            "Numerous gods attack the island, and there the women shout.",
            "A lot of gods attack the island, and there the women shout.",
            "Many gods are attacking the island, and the women are shouting there.",
            "Many gods attack the island, and the women are shouting there.",
            "Many gods do attack the island, and there the women do shout.",
        ],
        "explanation": (
            "• multi dei (the many gods)\n"
            "  → *de{T:i}* (gods) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *multi* (many) is an adjective, and agrees with *dei* (gods) because they are both masculine plural {T:nominative}\n"
            "• oppugn{R:a}{B:nt} (attack)\n"
            "  → *oppugno* (I attack) is the dictionary form of this verb\n"
            "  → *oppugn-* (attack) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• insulam (the island)\n"
            "  → *insul{T:am}* (island) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• ibi (there)\n"
            "  → *ibi* (there) is an adverb — flexible position in the sentence\n"
            "• feminae (the women)\n"
            "  → *femin{T:ae}* (women) is a noun, 1st declension feminine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• clam{R:a}{B:nt} (shout)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:nt}* shows it is the they form"
        ),
    },
    {
        "latin": "deus ingens per urbem festinat, et regina puellas liberat.",
        "english": [
            "The huge god hurries through the city, and the queen frees the girls.",
            "The enormous god hurries through the city, and the queen sets free the girls.",
            "The huge god rushes through the city, and the queen frees the girls.",
            "The vast god is hurrying through the city, and the queen is freeing the girls.",
            "The massive god hurries through the city, and the queen frees the girls.",
            "The huge god hastens through the city, and the queen frees the girls.",
            "The huge god is hurrying through the city, and the queen frees the girls.",
            "The huge god hurries through the city, and the queen liberates the girls.",
            "The huge god hurries through the city, and the queen releases the girls.",
            "The huge god hurries through the city, and the queen sets the girls free.",
            "The enormous god rushes through the city, and the queen liberates the girls.",
            "The huge god is rushing through the city, and the queen is liberating the girls.",
            "The vast god hurries through the city, and the queen frees the girls.",
        ],
        "explanation": (
            "• deus ingens (the huge god)\n"
            "  → *de{T:us}* (god) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *ingens* (huge) is an adjective, and agrees with *deus* (god) because they are both masculine singular {T:nominative}\n"
            "• festin{R:a}{B:t} (hurries)\n"
            "  → *festino* (I hurry) is the dictionary form of this verb\n"
            "  → *festin-* (hurry) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• per urbem (through the city)\n"
            "  → *per* (through) is a preposition\n"
            "  → *per* + {T:accusative} means 'through'\n"
            "  → *urb{T:em}* (city) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• regina (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• liber{R:a}{B:t} (frees)\n"
            "  → *libero* (I free) is the dictionary form of this verb\n"
            "  → *liber-* (free) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• puellas (the girls)\n"
            "  → *puell{T:as}* (girls) is a noun, 1st declension feminine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "pater puellam necat, et dea tristis deos orat.",
        "english": [
            "The father kills the girl, and the sad goddess begs the gods.",
            "The father kills the girl, and the unhappy goddess begs the gods.",
            "The father murders the girl, and the sad goddess pleads with the gods.",
            "The father is killing the girl, and the sad goddess is praying to the gods.",
            "The father slays the girl, and the sad goddess begs the gods.",
            "The father kills the girl, and the sorrowful goddess begs the gods.",
            "The father murders the girl, and the unhappy goddess pleads with the gods.",
            "The father is murdering the girl, and the sad goddess is begging the gods.",
            "The father kills the girl, and the sad goddess prays to the gods.",
            "The father kills the girl, and the sad goddess pleads with the gods.",
            "The father kills the girl, and the sad goddess is begging the gods.",
            "The father does kill the girl, and the sad goddess does beg the gods.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• nec{R:a}{B:t} (kills)\n"
            "  → *neco* (I kill) is the dictionary form of this verb\n"
            "  → *nec-* (kill) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• puellam (the girl)\n"
            "  → *puell{T:am}* (girl) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• dea tristis (the sad goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *tristis* (sad) is an adjective, and agrees with *dea* (goddess) because they are both feminine singular {T:nominative}\n"
            "• or{R:a}{B:t} (begs)\n"
            "  → *oro* (I beg) is the dictionary form of this verb\n"
            "  → *or-* (beg) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• deos (the gods)\n"
            "  → *de{T:os}* (gods) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
]

SENTENCES_PRESENT_SYSTEM = [
    {
        "latin": "dea clamabat.",
        "english": [
            "The goddess was shouting.",
            "The goddess used to shout.",
            "The goddess kept shouting.",
            "The goddess was crying out.",
            "The goddess was calling out.",
            "The goddess used to cry out.",
            "The goddess kept crying out.",
            "The goddess kept on shouting.",
            "A goddess was shouting.",
        ],
        "explanation": (
            "• de{T:a} (the goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• clam{R:a}{P:ba}{B:t} (was shouting)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "pater navigabit.",
        "english": [
            "The father will sail.",
            "The father will be sailing.",
            "The father is going to sail.",
            "The father will voyage.",
            "The father is going to be sailing.",
            "A father will sail.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• navig{R:a}{P:bi}{B:t} (will sail)\n"
            "  → *navigo* (I sail) is the dictionary form of this verb\n"
            "  → *navig-* (sail) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:bi}-* shows it is future, meaning 'will'\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "puella tum clamabat, et pater navigabat.",
        "english": [
            "The girl was then shouting, and the father was sailing.",
            "Then the girl was shouting, and the father was sailing.",
            "The girl then used to shout, and the father used to sail.",
            "The girl was shouting then, and the father was sailing.",
            "The girl was crying out then, and the father was sailing.",
            "The girl was calling out then, and the father was sailing.",
            "Then the girl used to shout, and the father used to sail.",
            "The girl kept shouting then, and the father kept sailing.",
            "The girl was shouting at that time, and the father was sailing.",
            "Then the girl was shouting, and the father was voyaging.",
            "The girl used to shout then, and the father used to sail.",
        ],
        "explanation": (
            "• puell{T:a} (the girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• tum (then)\n"
            "  → *tum* (then) is an adverb — flexible position in the sentence\n"
            "• clam{R:a}{P:ba}{B:t} (was shouting)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• navig{R:a}{P:ba}{B:t} (was sailing)\n"
            "  → *navigo* (I sail) is the dictionary form of this verb\n"
            "  → *navig-* (sail) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "regina feminam rogabit, et femina deam orabit.",
        "english": [
            "The queen will ask the woman, and the woman will beg the goddess.",
            "The queen is going to ask the woman, and the woman is going to beg the goddess.",
            "The queen will question the woman, and the woman will pray to the goddess.",
            "The queen will be asking the woman, and the woman will be begging the goddess.",
            "The queen will ask the woman, and the woman will plead with the goddess.",
            "The queen will ask the woman, and the woman will pray to the goddess.",
            "The queen will question the woman, and the woman will beg the goddess.",
            "The queen is going to question the woman, and the woman is going to plead with the goddess.",
            "The queen will be questioning the woman, and the woman will be praying to the goddess.",
        ],
        "explanation": (
            "• regin{T:a} (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• rog{R:a}{P:bi}{B:t} (will ask)\n"
            "  → *rogo* (I ask) is the dictionary form of this verb\n"
            "  → *rog-* (ask) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:bi}-* shows it is future, meaning 'will'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• femin{T:am} (the woman)\n"
            "  → *femin{T:am}* (woman) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• femin{T:a} (the woman)\n"
            "  → *femin{T:a}* (woman) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• or{R:a}{P:bi}{B:t} (will beg)\n"
            "  → *oro* (I beg) is the dictionary form of this verb\n"
            "  → *or-* (beg) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:bi}-* shows it is future, meaning 'will'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• de{T:am} (the goddess)\n"
            "  → *de{T:am}* (goddess) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "multi dei subito urbem oppugnabant, sed regina in insula habitabat.",
        "english": [
            "Many gods were suddenly attacking the city, but the queen was living on the island.",
            "Suddenly many gods were attacking the city, but the queen used to live on the island.",
            "Many gods suddenly used to attack the city, but the queen was living on the island.",
            "Many gods were suddenly attacking the city, but the queen lived in the island.",
            "Many gods suddenly were attacking the city, but the queen was dwelling on the island.",
            "Many gods were attacking the city suddenly, but the queen was living on the island.",
            "Suddenly many gods were assaulting the city, but the queen was living on the island.",
            "All of a sudden many gods were attacking the city, but the queen was living on the island.",
            "At once many gods were attacking the city, but the queen was living on the island.",
            "Many gods kept attacking the city suddenly, but the queen kept living on the island.",
            "Suddenly many gods were besieging the city, but the queen used to live on the island.",
            "Numerous gods were suddenly attacking the city, but the queen was inhabiting the island.",
            "Many of the gods were suddenly attacking the city, but the queen was living on the island.",
        ],
        "explanation": (
            "• multi de{T:i} (the many gods)\n"
            "  → *de{T:i}* (gods) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *multi* (many) is an adjective, and agrees with *dei* (gods) because they are both masculine plural {T:nominative}\n"
            "• subito (suddenly)\n"
            "  → *subito* (suddenly) is an adverb — flexible position in the sentence\n"
            "• oppugn{R:a}{P:ba}{B:nt} (were attacking)\n"
            "  → *oppugno* (I attack) is the dictionary form of this verb\n"
            "  → *oppugn-* (attack) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• urb{T:em} (the city)\n"
            "  → *urb{T:em}* (city) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• regin{T:a} (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• habit{R:a}{P:ba}{B:t} (was living)\n"
            "  → *habito* (I live) is the dictionary form of this verb\n"
            "  → *habit-* (live) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• in insula (on the island)\n"
            "  → *in* (in or on) is a preposition\n"
            "  → *in* + {T:ablative} can mean 'in' or 'on'\n"
            "  → *insul{T:a}* (island) is a noun, 1st declension feminine singular {T:ablative}"
        ),
    },
    {
        "latin": "puella pulchra in urbem festinabit, et pater clamabit.",
        "english": [
            "The beautiful girl will hurry into the city, and the father will shout.",
            "The beautiful girl will rush into the city, and the father will shout.",
            "The beautiful girl will be hurrying to the city, and the father will be shouting.",
            "The beautiful girl will hurry to the city, and the father will shout.",
            "The beautiful girl will hasten into the city, and the father will shout.",
            "The beautiful girl is going to hurry into the city, and the father is going to shout.",
            "The lovely girl will hurry into the city, and the father will shout.",
            "The pretty girl will hurry into the city, and the father will shout.",
            "The beautiful girl will rush to the city, and the father will cry out.",
            "The beautiful girl will hurry into the city, and the father will call out.",
            "The beautiful girl will be rushing into the city, and the father will be crying out.",
        ],
        "explanation": (
            "• puell{T:a} pulchra (the beautiful girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pulchra* (beautiful) is an adjective, and agrees with *puella* (girl) because they are both feminine singular {T:nominative}\n"
            "• festin{R:a}{P:bi}{B:t} (will hurry)\n"
            "  → *festino* (I hurry) is the dictionary form of this verb\n"
            "  → *festin-* (hurry) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:bi}-* shows it is future, meaning 'will'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• in urbem (into the city)\n"
            "  → *in* (into or onto) is a preposition\n"
            "  → *in* + {T:accusative} can mean 'into' or 'onto'\n"
            "  → *urb{T:em}* (city) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• clam{R:a}{P:bi}{B:t} (will shout)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:bi}-* shows it is future, meaning 'will'\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "dea me amabat, sed pater tum non orabat.",
        "english": [
            "The goddess was loving me, but the father was not then begging.",
            "The goddess used to love me, but the father was not begging then.",
            "The goddess was loving me, but my father was not begging then.",
            "The goddess was loving me, but the father was not begging then.",
            "The goddess used to like me, but the father was not begging then.",
            "The goddess kept loving me, but the father was not pleading then.",
            "The goddess was loving me, but the father then was not begging.",
            "The goddess was loving me, but the father was not pleading then.",
            "The goddess was loving me, but the father was not praying then.",
        ],
        "explanation": (
            "• de{T:a} (the goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• am{R:a}{P:ba}{B:t} (was loving)\n"
            "  → *amo* (I love) is the dictionary form of this verb\n"
            "  → *am-* (love) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• me (me)\n"
            "  → *me* (me) is a pronoun — it is the {N:object}\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• tum (then)\n"
            "  → *tum* (then) is an adverb\n"
            "• non or{R:a}{P:ba}{B:t} (was not begging)\n"
            "  → *non* (not) negates the verb\n"
            "  → *oro* (I beg) is the dictionary form of this verb\n"
            "  → *or-* (beg) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "dea patrem liberabit, et pater deae tum imperabit.",
        "english": [
            "The goddess will free the father, and the father will then order the goddess.",
            "The goddess will set free the father, and then the father will order the goddess.",
            "The goddess will free her father, and the father will then order the goddess.",
            "The goddess will liberate the father, and the father will then order the goddess.",
            "The goddess will release the father, and the father will then order the goddess.",
            "The goddess will free the father, and then the father will command the goddess.",
            "The goddess will free the father, and the father will then command the goddess.",
            "The goddess is going to free the father, and the father is going to order the goddess then.",
            "The goddess will set the father free, and the father will then order the goddess.",
            "The goddess will free the father, and the father will order the goddess then.",
            "The goddess will free the father, and the father of the goddess will then order.",
            "The goddess will free the father, and the goddess's father will then order.",
        ],
        "explanation": (
            "• de{T:a} (the goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• liber{R:a}{P:bi}{B:t} (will free)\n"
            "  → *libero* (I free) is the dictionary form of this verb\n"
            "  → *liber-* (free) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:bi}-* shows it is future, meaning 'will'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• patr{T:em} (the father)\n"
            "  → *patr{T:em}* (father) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• tum (then)\n"
            "  → *tum* (then) is an adverb — flexible position in the sentence\n"
            "• imper{R:a}{P:bi}{B:t} (will order)\n"
            "  → *impero* (I order) is the dictionary form of this verb\n"
            "  → *imper-* (order) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:bi}-* shows it is future, meaning 'will'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• de{T:ae} (the goddess / of the goddess)\n"
            "  → *de{T:ae}* is 1st declension feminine singular — this ending is shared by {T:dative} and {T:genitive}\n"
            "  → in context here, {T:dative} fits best (*impero* takes the dative): 'ordered the goddess'\n"
            "  → but {T:genitive} ('of the goddess') is also grammatically valid: 'the father of the goddess will order'\n"
            "  → both readings are accepted"
        ),
    },
    {
        "latin": "regina tristis deum laetum putabat, sed dea non orabat.",
        "english": [
            "The sad queen was thinking the god happy, but the goddess was not begging.",
            "The sad queen was thinking that the god was happy, but the goddess was not begging.",
            "The sad queen was thinking the god was happy, but the goddess was not begging.",
            "A sad queen was thinking the god happy, but the goddess was not begging.",
            "The sad queen thought the god happy, but the goddess was not begging.",
            "The sad queen thought the god was happy, but the goddess was not begging.",
            "The sad queen thought that the god was happy, but the goddess was not begging.",
            "The sad queen used to think the god happy, but the goddess did not beg.",
            "The sad queen used to think that the god was happy, but the goddess did not beg.",
            "The unhappy queen was thinking the god happy, but the goddess was not begging.",
            "The sad queen considered the god happy, but the goddess was not praying to (him).",
            "The sad queen considered the god to be happy, but the goddess was not praying.",
            "The sad queen believed the god happy, but the goddess was not begging.",
            "The sad queen believed that the god was happy, but the goddess was not begging.",
            "The sad queen supposed the god happy, but the goddess was not begging.",
            "The sad queen kept thinking the god happy, but the goddess was not begging.",
            "The sad queen was thinking the god joyful, but the goddess was not begging.",
            "The sad queen was thinking the god glad, but the goddess was not begging.",
            "The sorrowful queen was thinking the god happy, but the goddess was not begging.",
        ],
        "explanation": (
            "• regin{T:a} tristis (the sad queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *tristis* (sad) is an adjective, and agrees with *regina* (queen) because they are both feminine singular {T:nominative}\n"
            "• put{R:a}{P:ba}{B:t} (was thinking)\n"
            "  → *puto* (I think) is the dictionary form of this verb\n"
            "  → *put-* (think) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• de{T:um} laetum (the god happy)\n"
            "  → *puto* takes two {T:accusative}s: 'I think X to be Y'\n"
            "  → *de{T:um}* (god) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → *laetum* (happy) is an adjective, and agrees with *deum* (god) because they are both masculine singular {T:accusative}\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• de{T:a} (the goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• non or{R:a}{P:ba}{B:t} (was not begging)\n"
            "  → *non* (not) negates the verb\n"
            "  → *oro* (I beg) is the dictionary form of this verb\n"
            "  → *or-* (beg) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "ingens navis per terram navigabat, et puella pulchra clamabat.",
        "english": [
            "A huge ship was sailing through the land, and the beautiful girl was shouting.",
            "An enormous ship was sailing through the land, and the beautiful girl was shouting.",
            "A huge ship used to sail through the land, and the beautiful girl kept shouting.",
            "A huge ship was sailing through the country, and the beautiful girl was shouting.",
            "The huge ship was sailing through the land, and the beautiful girl was shouting.",
            "A massive ship was sailing through the land, and the beautiful girl was shouting.",
            "A vast ship was sailing through the land, and the beautiful girl was shouting.",
            "A huge ship was voyaging through the land, and the beautiful girl was shouting.",
            "A huge ship used to sail through the land, and the beautiful girl used to shout.",
            "A huge ship kept sailing through the land, and the beautiful girl kept shouting.",
            "An enormous ship was sailing through the country, and the lovely girl was shouting.",
            "A huge ship was sailing through the land, and the beautiful girl was crying out.",
            "A huge ship was sailing through the land, and the pretty girl was shouting.",
        ],
        "explanation": (
            "• ingens nav{T:is} (a huge ship)\n"
            "  → *nav{T:is}* (ship) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *ingens* (huge) is an adjective, and agrees with *navis* (ship) because they are both feminine singular {T:nominative}\n"
            "• navig{R:a}{P:ba}{B:t} (was sailing)\n"
            "  → *navigo* (I sail) is the dictionary form of this verb\n"
            "  → *navig-* (sail) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• per terram (through the land)\n"
            "  → *per* (through) is a preposition\n"
            "  → *per* + {T:accusative} means 'through'\n"
            "  → *terr{T:am}* (land) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• puell{T:a} pulchra (the beautiful girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pulchra* (beautiful) is an adjective, and agrees with *puella* (girl) because they are both feminine singular {T:nominative}\n"
            "• clam{R:a}{P:ba}{B:t} (was shouting)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
]

SENTENCES_ACTIVE = [
    {
        "latin": "puella clamavit.",
        "english": [
            "The girl shouted.",
            "The girl has shouted.",
            "The girl did shout.",
            "The girl cried out.",
            "The girl has cried out.",
            "The girl called out.",
            "The girl has called out.",
            "The girl did cry out.",
            "A girl shouted.",
        ],
        "explanation": (
            "• puell{T:a} (the girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• clam{R:a}{P:v}{B:it} (shouted)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "pater feminam rogavit.",
        "english": [
            "The father asked the woman.",
            "The father has asked the woman.",
            "The father questioned the woman.",
            "The father did ask the woman.",
            "The father has questioned the woman.",
            "The father did question the woman.",
            "A father asked the woman.",
            "The father asked a woman.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• rog{R:a}{P:v}{B:it} (asked)\n"
            "  → *rogo* (I ask) is the dictionary form of this verb\n"
            "  → *rog-* (ask) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• femin{T:am} (the woman)\n"
            "  → *femin{T:am}* (woman) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "dea pulchra deum amavit, et deus clamavit.",
        "english": [
            "The beautiful goddess loved the god, and the god shouted.",
            "The beautiful goddess has loved the god, and the god has shouted.",
            "The beautiful goddess liked the god, and the god cried out.",
            "The beautiful goddess loved the god, and the god called out.",
            "The beautiful goddess did love the god, and the god did shout.",
            "The lovely goddess loved the god, and the god shouted.",
            "The pretty goddess loved the god, and the god shouted.",
            "The beautiful goddess has liked the god, and the god has shouted.",
            "The beautiful goddess loved the god, and the god has shouted.",
            "The beautiful goddess loved the god, and the god has cried out.",
            "The beautiful goddess has loved the god, and the god cried out.",
            "The beautiful goddess liked the god, and the god shouted.",
        ],
        "explanation": (
            "• de{T:a} pulchra (the beautiful goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pulchra* (beautiful) is an adjective, and agrees with *dea* (goddess) because they are both feminine singular {T:nominative}\n"
            "• am{R:a}{P:v}{B:it} (loved)\n"
            "  → *amo* (I love) is the dictionary form of this verb\n"
            "  → *am-* (love) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• de{T:um} (the god)\n"
            "  → *de{T:um}* (god) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• de{T:us} (the god)\n"
            "  → *de{T:us}* (god) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• clam{R:a}{P:v}{B:it} (shouted)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "regina filiam non liberaverat, sed pater domum festinavit.",
        "english": [
            "The queen had not freed the daughter, but the father hurried home.",
            "The queen had not set free the daughter, but the father hurried home.",
            "The queen had not freed her daughter, but the father hurried homewards.",
            "The queen had not freed the daughter, but the father has hurried home.",
            "The queen had not liberated the daughter, but the father hurried home.",
            "The queen had not released the daughter, but the father hurried home.",
            "The queen had not set the daughter free, but the father hurried home.",
            "The queen had not freed the daughter, but the father has hurried homewards.",
            "The queen had not freed the daughter, but the father did hurry home.",
            "The queen had not freed her daughter, but the father hurried home.",
            "The queen had not freed the daughter, but the father hastened home.",
            "The queen had not freed the daughter, but the father rushed home.",
            "The queen had not freed the daughter, but the father hastened homewards.",
        ],
        "explanation": (
            "• regin{T:a} (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• non liber{R:a}{P:v}{M:era}{B:t} (had not freed)\n"
            "  → *non* (not) negates the verb\n"
            "  → *libero* (I free) is the dictionary form of this verb\n"
            "  → *liber-* (free) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* is the perfect stem marker\n"
            "  → *-{M:era}-* shows it is pluperfect, meaning 'had'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• fili{T:am} (the daughter)\n"
            "  → *fili{T:am}* (daughter) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• festin{R:a}{P:v}{B:it} (hurried)\n"
            "  → *festino* (I hurry) is the dictionary form of this verb\n"
            "  → *festin-* (hurry) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• domum (home)\n"
            "  → *domum* (home) is the {T:accusative} of *domus* (house) — used without a preposition to mean 'to home'"
        ),
    },
    {
        "latin": "multi dei ad insulam navigaverunt, et puellas necaverunt.",
        "english": [
            "Many gods sailed to the island, and killed the girls.",
            "Many gods sailed towards the island, and killed the girls.",
            "Many gods have sailed to the island, and have killed the girls.",
            "Many of the gods sailed to the island, and murdered the girls.",
            "Many gods sailed to the island, and they killed the girls.",
            "Many gods sailed to the island, and slew the girls.",
            "Many gods have sailed towards the island, and have killed the girls.",
            "Many gods sailed to the island, and murdered the girls.",
            "Many gods sailed to the island, and have killed the girls.",
            "Many gods did sail to the island, and did kill the girls.",
            "Numerous gods sailed to the island, and killed the girls.",
            "Many gods voyaged to the island, and killed the girls.",
            "A lot of gods sailed to the island, and killed the girls.",
        ],
        "explanation": (
            "• multi de{T:i} (the many gods)\n"
            "  → *de{T:i}* (gods) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *multi* (many) is an adjective, and agrees with *dei* (gods) because they are both masculine plural {T:nominative}\n"
            "• navig{R:a}{P:v}{B:erunt} (sailed)\n"
            "  → *navigo* (I sail) is the dictionary form of this verb\n"
            "  → *navig-* (sail) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:erunt}* shows it is the they form\n"
            "• ad insulam (to the island)\n"
            "  → *ad* (to, towards) is a preposition\n"
            "  → *ad* + {T:accusative} means 'to' or 'towards'\n"
            "  → *insul{T:am}* (island) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• puell{T:as} (the girls)\n"
            "  → *puell{T:as}* (girls) is a noun, 1st declension feminine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• nec{R:a}{P:v}{B:erunt} (killed)\n"
            "  → *neco* (I kill) is the dictionary form of this verb\n"
            "  → *nec-* (kill) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:erunt}* shows it is the they form"
        ),
    },
    {
        "latin": "pater ingens puellam amaverat, sed puella tristis deum oraverat.",
        "english": [
            "The huge father had loved the girl, but the sad girl had begged the god.",
            "The enormous father had loved the girl, but the unhappy girl had begged the god.",
            "The huge father had liked the girl, but the sad girl had pleaded with the god.",
            "The huge father had loved the girl, but the sad girl had prayed to the god.",
            "The massive father had loved the girl, but the sad girl had begged the god.",
            "The vast father had loved the girl, but the sad girl had begged the god.",
            "The huge father had loved the girl, but the sorrowful girl had begged the god.",
            "The huge father had loved the girl, but the unhappy girl had pleaded with the god.",
            "The huge father had loved the girl, but the unhappy girl had prayed to the god.",
            "The enormous father had liked the girl, but the sad girl had pleaded with the god.",
            "The huge father had loved the girl, but the sad girl had pleaded with the god.",
        ],
        "explanation": (
            "• pater ingens (the huge father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *ingens* (huge) is an adjective, and agrees with *pater* (father) because they are both masculine singular {T:nominative}\n"
            "• am{R:a}{P:v}{M:era}{B:t} (had loved)\n"
            "  → *amo* (I love) is the dictionary form of this verb\n"
            "  → *am-* (love) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* is the perfect stem marker\n"
            "  → *-{M:era}-* shows it is pluperfect, meaning 'had'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• puell{T:am} (the girl)\n"
            "  → *puell{T:am}* (girl) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• puell{T:a} tristis (the sad girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *tristis* (sad) is an adjective, and agrees with *puella* (girl) because they are both feminine singular {T:nominative}\n"
            "• or{R:a}{P:v}{M:era}{B:t} (had begged)\n"
            "  → *oro* (I beg) is the dictionary form of this verb\n"
            "  → *or-* (beg) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* is the perfect stem marker\n"
            "  → *-{M:era}-* shows it is pluperfect, meaning 'had'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• de{T:um} (the god)\n"
            "  → *de{T:um}* (god) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "dea pulchra ad tristem feminam appropinquavit, et clamabat.",
        "english": [
            "The beautiful goddess approached the sad woman, and was shouting.",
            "The beautiful goddess approached the sad woman, and kept shouting.",
            "The beautiful goddess approached the sad woman, and used to shout.",
            "A beautiful goddess approached the sad woman, and was shouting.",
            "The beautiful goddess drew near to the sad woman, and was shouting.",
            "The beautiful goddess came near to the sad woman, and was shouting.",
            "The lovely goddess approached the sad woman, and was shouting.",
            "The pretty goddess approached the sad woman, and was shouting.",
            "The beautiful goddess approached the unhappy woman, and was shouting.",
            "The beautiful goddess approached the sorrowful woman, and was shouting.",
            "The beautiful goddess has approached the sad woman, and was shouting.",
            "The beautiful goddess approached the sad woman, and was crying out.",
            "The beautiful goddess approached the sad woman, and was calling out.",
            "The beautiful goddess did approach the sad woman, and was shouting.",
        ],
        "explanation": (
            "• de{T:a} pulchra (the beautiful goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pulchra* (beautiful) is an adjective, and agrees with *dea* (goddess) because they are both feminine singular {T:nominative}\n"
            "• appropinqu{R:a}{P:v}{B:it} (approached)\n"
            "  → *appropinquo* (I approach) is the dictionary form of this verb\n"
            "  → *appropinqu-* (approach) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• ad tristem feminam (to the sad woman)\n"
            "  → *ad* (to, towards) is a preposition\n"
            "  → *ad* + {T:accusative} means 'to' or 'towards'\n"
            "  → *femin{T:am}* (woman) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → *tristem* (sad) is an adjective, and agrees with *feminam* (woman) because they are both feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• clam{R:a}{P:ba}{B:t} (was shouting)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "regina urbem oppugnavit, et prope insulam habitavit.",
        "english": [
            "The queen attacked the city, and lived near the island.",
            "The queen has attacked the city, and has lived near the island.",
            "The queen attacked the city, and dwelt close to the island.",
            "The queen attacked the city, and lived next to the island.",
            "The queen attacked the city, and lived close to the island.",
            "The queen attacked the city, and lived nearby the island.",
            "The queen has attacked the city, and lived near the island.",
            "The queen attacked the city, and has lived near the island.",
            "The queen assaulted the city, and lived near the island.",
            "The queen besieged the city, and lived near the island.",
            "The queen attacked the city, and dwelt near the island.",
            "The queen did attack the city, and did live near the island.",
        ],
        "explanation": (
            "• regin{T:a} (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• oppugn{R:a}{P:v}{B:it} (attacked)\n"
            "  → *oppugno* (I attack) is the dictionary form of this verb\n"
            "  → *oppugn-* (attack) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• urb{T:em} (the city)\n"
            "  → *urb{T:em}* (city) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• habit{R:a}{P:v}{B:it} (lived)\n"
            "  → *habito* (I live) is the dictionary form of this verb\n"
            "  → *habit-* (live) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• prope insulam (near the island)\n"
            "  → *prope* (near) is a preposition\n"
            "  → *prope* + {T:accusative} means 'near'\n"
            "  → *insul{T:am}* (island) is a noun, 1st declension feminine singular {T:accusative}"
        ),
    },
    {
        "latin": "ego deos rogaveram, sed etiam tum non clamaverant.",
        "english": [
            "I had asked the gods, but even then they had not shouted.",
            "I myself had asked the gods, but still then they had not shouted.",
            "I had asked the gods, but also then they had not shouted.",
            "I had asked the gods, but even at that moment they had not shouted.",
            "I had questioned the gods, but even then they had not shouted.",
            "I had asked the gods, but even then they had not cried out.",
            "I had asked the gods, but even then they had not called out.",
            "I myself had asked the gods, but even then they had not shouted.",
            "I had asked the gods, but still at that time they had not shouted.",
            "I had asked the gods, but they had not even then shouted.",
            "I had asked the gods, but they had still not shouted then.",
        ],
        "explanation": (
            "• ego (I)\n"
            "  → *ego* (I) is a pronoun — the {N:subject} of this verb\n"
            "  → *ego* is emphatic — it stresses that it was specifically I who did this\n"
            "• rog{R:a}{P:v}{M:era}{B:m} (had asked)\n"
            "  → *rogo* (I ask) is the dictionary form of this verb\n"
            "  → *rog-* (ask) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* is the perfect stem marker\n"
            "  → *-{M:era}-* shows it is pluperfect, meaning 'had'\n"
            "  → *-{B:m}* shows it is the I form\n"
            "• de{T:os} (the gods)\n"
            "  → *de{T:os}* (gods) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• etiam (even)\n"
            "  → *etiam* (even / also / still) is an adverb\n"
            "• tum (then)\n"
            "  → *tum* (then) is an adverb\n"
            "• non clam{R:a}{P:v}{M:era}{B:nt} (had not shouted)\n"
            "  → *non* (not) negates the verb\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* is the perfect stem marker\n"
            "  → *-{M:era}-* shows it is pluperfect, meaning 'had'\n"
            "  → *-{B:nt}* shows it is the they form"
        ),
    },
    {
        "latin": "pater mihi imperavit, et dea feminam pulchram putaverat.",
        "english": [
            "The father ordered me, and the goddess had thought the woman beautiful.",
            "The father ordered me, and the goddess had thought the woman was beautiful.",
            "The father ordered me, and the goddess had thought that the woman was beautiful.",
            "The father ordered me, and the goddess had considered the woman beautiful.",
            "The father ordered me, and the goddess had considered the woman to be beautiful.",
            "The father has ordered me, and the goddess had thought the woman (to be) beautiful.",
            "The father ordered me, and the goddess had thought (that) the woman (was) beautiful.",
            "The father commanded me, and the goddess had thought the woman beautiful.",
            "The father commanded me, and the goddess had thought the woman was beautiful.",
            "The father ordered me, and the goddess had believed the woman beautiful.",
            "The father ordered me, and the goddess had believed the woman to be beautiful.",
            "The father ordered me, and the goddess had believed that the woman was beautiful.",
            "The father ordered me, and the goddess had supposed the woman beautiful.",
            "The father ordered me, and the goddess had supposed that the woman was beautiful.",
            "The father ordered me, and the goddess had thought the woman lovely.",
            "The father ordered me, and the goddess had thought the woman pretty.",
            "The father commanded me, and the goddess had considered the woman beautiful.",
            "The father did order me, and the goddess had thought the woman beautiful.",
            "The father has commanded me, and the goddess had thought the woman beautiful.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• imper{R:a}{P:v}{B:it} (ordered)\n"
            "  → *impero* (I order) is the dictionary form of this verb\n"
            "  → *imper-* (order) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• mihi (me)\n"
            "  → *mihi* (me) is a pronoun in the {T:dative} — *impero* takes {T:dative}, not {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• de{T:a} (the goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• put{R:a}{P:v}{M:era}{B:t} (had thought)\n"
            "  → *puto* (I think) is the dictionary form of this verb\n"
            "  → *put-* (think) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* is the perfect stem marker\n"
            "  → *-{M:era}-* shows it is pluperfect, meaning 'had'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• femin{T:am} pulchram (the beautiful woman)\n"
            "  → *puto* takes two {T:accusative}s: 'I think X to be Y'\n"
            "  → *femin{T:am}* (woman) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → *pulchram* (beautiful) is an adjective, and agrees with *feminam* (woman) because they are both feminine singular {T:accusative}"
        ),
    },
]

SENTENCES_PPP = [
    {
        "latin": "puella liberata clamavit.",
        "english": [
            "The girl, having been freed, shouted.",
            "The freed girl shouted.",
            "The girl who had been freed shouted.",
            "Once freed, the girl shouted.",
            "After being freed, the girl shouted.",
            "The girl, once freed, shouted.",
            "The girl, having been freed, has shouted.",
            "The girl, having been freed, did shout.",
            "The girl, having been freed, cried out.",
            "The girl, having been freed, called out.",
            "The liberated girl shouted.",
            "The girl, having been liberated, shouted.",
            "The girl, having been set free, shouted.",
            "The released girl shouted.",
            "The freed girl has shouted.",
        ],
        "explanation": (
            "• puell{T:a} liberat{T:a} (the freed girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *liberat{T:a}* (having been freed) is a PPP, and agrees with *puella* (girl) because they are both feminine singular {T:nominative}\n"
            "• clam{R:a}{P:v}{B:it} (shouted)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "femina necata est.",
        "english": [
            "The woman was killed.",
            "The woman has been killed.",
            "The woman was murdered.",
            "The woman has been murdered.",
            "The woman was slain.",
            "The woman has been slain.",
            "A woman was killed.",
            "A woman has been killed.",
        ],
        "explanation": (
            "• femin{T:a} (the woman)\n"
            "  → *femin{T:a}* (woman) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• necat{T:a} est (was killed)\n"
            "  → *necata* is a PPP (perfect passive participle) — it means *having been killed*\n"
            "  → it is feminine singular {T:nominative}, so it agrees with *femina* (the woman)\n"
            "  → *est* on its own means *is* — but placed after a PPP, it creates the perfect passive\n"
            "  → *necata est* = literally 'is having-been-killed' → translate as 'was killed' or 'has been killed'\n"
            "  → the pattern: **PPP + *est*** = 'was ___ed'; **PPP + *sunt*** = 'were ___ed'"
        ),
    },
    {
        "latin": "dea oppugnata ad insulam navigabat.",
        "english": [
            "The goddess, having been attacked, was sailing to the island.",
            "The goddess, having been attacked, was sailing towards the island.",
            "The attacked goddess was sailing to the island.",
            "The goddess who had been attacked was sailing towards the island.",
            "The goddess, once attacked, was sailing to the island.",
            "After being attacked, the goddess was sailing to the island.",
            "The goddess who had been attacked was sailing to the island.",
            "The attacked goddess was sailing towards the island.",
            "The goddess, having been attacked, used to sail to the island.",
            "The goddess, having been attacked, kept sailing to the island.",
            "The goddess, having been assaulted, was sailing to the island.",
            "The goddess, having been besieged, was sailing to the island.",
            "The goddess, having been attacked, was voyaging to the island.",
        ],
        "explanation": (
            "• de{T:a} oppugnat{T:a} (the attacked goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *oppugnat{T:a}* (having been attacked) is a PPP, and agrees with *dea* (goddess) because they are both feminine singular {T:nominative}\n"
            "• navig{R:a}{P:ba}{B:t} (was sailing)\n"
            "  → *navigo* (I sail) is the dictionary form of this verb\n"
            "  → *navig-* (sail) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• ad insulam (to the island)\n"
            "  → *ad* (to, towards) is a preposition\n"
            "  → *ad* + {T:accusative} means 'to' or 'towards'\n"
            "  → *insul{T:am}* (island) is a noun, 1st declension feminine singular {T:accusative}"
        ),
    },
    {
        "latin": "pater filiam amatam rogavit.",
        "english": [
            "The father asked the loved daughter.",
            "The father asked the beloved daughter.",
            "The father asked the daughter, having been loved.",
            "The father asked the daughter who had been loved.",
            "The father questioned the daughter, having been loved.",
            "The father questioned the daughter who had been loved.",
            "The father asked the daughter who had been liked.",
            "The father has asked the daughter who had been loved.",
            "The father asked the having-been-loved daughter.",
            "The father asked his loved daughter.",
            "The father asked his beloved daughter.",
            "The father asked his having-been-loved daughter.",
            "The father questioned the loved daughter.",
            "The father questioned the beloved daughter.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• rog{R:a}{P:v}{B:it} (asked)\n"
            "  → *rogo* (I ask) is the dictionary form of this verb\n"
            "  → *rog-* (ask) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is {P:perfect}, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• fili{T:am} amat{T:am} (the loved daughter)\n"
            "  → *fili{T:am}* (daughter) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "  → *amat{T:am}* (loved / having been loved) is a PPP agreeing with *filiam* (daughter) — both feminine singular {T:accusative}"
        ),
    },
    {
        "latin": "regina liberata puellam tristem amavit.",
        "english": [
            "The queen, having been freed, loved the sad girl.",
            "The freed queen loved the sad girl.",
            "The queen, once freed, loved the unhappy girl.",
            "The queen who had been freed liked the sad girl.",
            "The queen, having been freed, has loved the sad girl.",
            "The queen, having been freed, did love the sad girl.",
            "The queen who had been freed loved the sad girl.",
            "After being freed, the queen loved the sad girl.",
            "The freed queen liked the sad girl.",
            "The freed queen loved the unhappy girl.",
            "The queen, having been liberated, loved the sad girl.",
            "The queen, having been set free, loved the sad girl.",
            "The released queen loved the sad girl.",
            "The queen, having been freed, loved the sorrowful girl.",
        ],
        "explanation": (
            "• regin{T:a} liberat{T:a} (the freed queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *liberat{T:a}* (having been freed) is a PPP, and agrees with *regina* (queen) because they are both feminine singular {T:nominative}\n"
            "• am{R:a}{P:v}{B:it} (loved)\n"
            "  → *amo* (I love) is the dictionary form of this verb\n"
            "  → *am-* (love) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• puell{T:am} tristem (the sad girl)\n"
            "  → *puell{T:am}* (girl) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "  → *tristem* (sad) is an adjective, and agrees with *puellam* (girl) because they are both feminine singular {T:accusative}"
        ),
    },
    {
        "latin": "deus necatus est, et dea clamabat.",
        "english": [
            "The god was killed, and the goddess was shouting.",
            "The god has been killed, and the goddess was shouting.",
            "The god was murdered, and the goddess was shouting.",
            "The god has been murdered, and the goddess was shouting.",
            "The god was slain, and the goddess was shouting.",
            "The god has been slain, and the goddess was shouting.",
            "The god was killed, and the goddess kept shouting.",
            "The god has been killed, and the goddess kept shouting.",
            "The god was killed, and the goddess used to shout.",
            "The god has been killed, and the goddess used to shout.",
        ],
        "explanation": (
            "• de{T:us} (the god)\n"
            "  → *de{T:us}* (god) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• necat{T:us} est (was killed)\n"
            "  → *necat{T:us}* (having been killed) is a PPP, masculine singular {T:nominative} agreeing with *deus*\n"
            "  → *est* (is/was) is the auxiliary verb — together they form the perfect passive\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• de{T:a} (the goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• clam{R:a}{P:ba}{B:t} (was shouting)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "multae feminae oratae sunt, sed reginae laetae non festinaverunt.",
        "english": [
            "Many women were begged, but the happy queens did not hurry.",
            "Many women have been begged, but the happy queens did not hurry.",
            "Many of the women were begged, but the happy queens did not hurry.",
            "Many of the women have been begged, but the happy queens did not hurry.",
            "Many women were begged, but the happy queens have not hurried.",
            "Many women have been begged, but the happy queens have not hurried.",
        ],
        "explanation": (
            "• multae femin{T:ae} (the many women)\n"
            "  → *femin{T:ae}* (women) is a noun, 1st declension feminine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *multae* (many) is an adjective, and agrees with *feminae* (women) because they are both feminine plural {T:nominative}\n"
            "• orat{T:ae} sunt (were begged)\n"
            "  → *orat{T:ae}* (having been begged) is a PPP, feminine plural {T:nominative} agreeing with *feminae*\n"
            "  → *sunt* (are/were) is the auxiliary verb — together they form the perfect passive\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• regin{T:ae} laetae (the happy queens)\n"
            "  → *regin{T:ae}* (queens) is a noun, 1st declension feminine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *laetae* (happy) is an adjective, and agrees with *reginae* (queens) because they are both feminine plural {T:nominative}\n"
            "• non festin{R:a}{P:v}{B:erunt} (did not hurry)\n"
            "  → *non* (not) negates the verb\n"
            "  → *festino* (I hurry) is the dictionary form of this verb\n"
            "  → *festin-* (hurry) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:erunt}* shows it is the they form"
        ),
    },
    {
        "latin": "puella oppugnata patrem oravit, et pater feminas liberavit.",
        "english": [
            "The girl, having been attacked, begged the father, and the father freed the women.",
            "The attacked girl begged her father, and the father set free the women.",
            "The girl who had been attacked pleaded with the father, and the father freed the women.",
            "Once attacked, the girl begged the father, and the father freed the women.",
            "After being attacked, the girl begged the father, and the father freed the women.",
            "The girl, having been attacked, pleaded with the father, and the father freed the women.",
            "The girl, having been attacked, prayed to the father, and the father freed the women.",
            "The attacked girl begged the father, and the father freed the women.",
            "The girl who had been attacked begged the father, and the father liberated the women.",
            "The girl, having been attacked, has begged the father, and the father has freed the women.",
            "The girl, having been attacked, begged her father, and her father freed the women.",
            "The girl, having been assaulted, begged the father, and the father freed the women.",
            "The girl, having been attacked, begged the father, and the father set free the women.",
            "The girl, having been attacked, begged the father, and the father set the women free.",
        ],
        "explanation": (
            "• puell{T:a} oppugnat{T:a} (the attacked girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *oppugnat{T:a}* (having been attacked) is a PPP, and agrees with *puella* (girl) because they are both feminine singular {T:nominative}\n"
            "• or{R:a}{P:v}{B:it} (begged)\n"
            "  → *oro* (I beg) is the dictionary form of this verb\n"
            "  → *or-* (beg) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• patr{T:em} (the father)\n"
            "  → *patr{T:em}* (father) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• liber{R:a}{P:v}{B:it} (freed)\n"
            "  → *libero* (I free) is the dictionary form of this verb\n"
            "  → *liber-* (free) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• femin{T:as} (the women)\n"
            "  → *femin{T:as}* (women) is a noun, 1st declension feminine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "dea tristis deum necatum amaverat, sed deus imperatus est.",
        "english": [
            "The sad goddess had loved the god, having been killed, but the god was ordered.",
            "The sad goddess had loved the god, having been killed, but the god has been ordered.",
            "The sad goddess had loved the god who had been killed, but the god was ordered.",
            "The sad goddess had loved the god who had been killed, but the god has been ordered.",
            "The unhappy goddess had loved the god, having been killed, but the god was ordered.",
        ],
        "explanation": (
            "• de{T:a} tristis (the sad goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *tristis* (sad) is an adjective, and agrees with *dea* (goddess) because they are both feminine singular {T:nominative}\n"
            "• am{R:a}{P:v}{M:era}{B:t} (had loved)\n"
            "  → *amo* (I love) is the dictionary form of this verb\n"
            "  → *am-* (love) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* is the perfect stem marker\n"
            "  → *-{M:era}-* shows it is pluperfect, meaning 'had'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• de{T:um} necat{T:um} (the killed god)\n"
            "  → *de{T:um}* (god) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "  → *necat{T:um}* (having been killed) is a PPP, and agrees with *deum* (god) because they are both masculine singular {T:accusative}\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• de{T:us} (the god)\n"
            "  → *de{T:us}* (god) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• imperat{T:us} est (was ordered)\n"
            "  → *imperat{T:us}* (having been ordered) is a PPP, masculine singular {T:nominative} agreeing with *deus*\n"
            "  → *est* (is/was) is the auxiliary verb — together they form the perfect passive"
        ),
    },
    {
        "latin": "ingens navis oppugnata ad terram navigabat, et multi dei clamaverunt.",
        "english": [
            "The huge ship, having been attacked, was sailing to the land, and many gods shouted.",
            "The enormous ship, having been attacked, was sailing towards the land, and many gods shouted.",
            "The huge attacked ship was sailing to the land, and many gods shouted.",
            "The vast ship, once attacked, was sailing to the land, and many gods shouted.",
            "The huge ship, having been attacked, was sailing to the country, and many gods shouted.",
            "The massive ship, having been attacked, was sailing to the land, and many gods shouted.",
            "The huge ship that had been attacked was sailing to the land, and many gods shouted.",
            "The huge ship which had been attacked was sailing to the land, and many gods shouted.",
            "After being attacked, the huge ship was sailing to the land, and many gods shouted.",
            "The huge attacked ship was sailing towards the land, and many gods cried out.",
            "The huge ship, having been assaulted, was sailing to the land, and many gods shouted.",
            "The huge ship, having been besieged, was sailing to the land, and many gods shouted.",
            "The huge ship, having been attacked, was sailing to the land, and many gods have shouted.",
            "The huge ship, having been attacked, was sailing to the land, and many gods did shout.",
            "The huge ship, having been attacked, was voyaging to the land, and many gods shouted.",
        ],
        "explanation": (
            "• ingens nav{T:is} oppugnat{T:a} (the huge attacked ship)\n"
            "  → *nav{T:is}* (ship) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *ingens* (huge) is an adjective, and agrees with *navis* (ship) because they are both feminine singular {T:nominative}\n"
            "  → *oppugnat{T:a}* (having been attacked) is a PPP, and agrees with *navis* (ship) because they are both feminine singular {T:nominative}\n"
            "• navig{R:a}{P:ba}{B:t} (was sailing)\n"
            "  → *navigo* (I sail) is the dictionary form of this verb\n"
            "  → *navig-* (sail) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is imperfect, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• ad terram (to the land)\n"
            "  → *ad* (to, towards) is a preposition\n"
            "  → *ad* + {T:accusative} means 'to' or 'towards'\n"
            "  → *terr{T:am}* (land) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• multi de{T:i} (the many gods)\n"
            "  → *de{T:i}* (gods) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *multi* (many) is an adjective, and agrees with *dei* (gods) because they are both masculine plural {T:nominative}\n"
            "• clam{R:a}{P:v}{B:erunt} (shouted)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is perfect, meaning 'did' or 'has done'\n"
            "  → *-{B:erunt}* shows it is the they form"
        ),
    },
]

VERB_IDENTIFY = [
    {"form": "The ancient Romans built wide roads.", "correct": "built", "options": ["ancient", "Romans", "built", "roads"]},
    {"form": "Gladiators fight in the arena.", "correct": "fight", "options": ["Gladiators", "fight", "in", "arena"]},
    {"form": "We are learning about the Roman Empire.", "correct": "are learning", "options": ["We", "are learning", "Roman", "Empire"]},
    {"form": "The emperor sits tightly on his throne.", "correct": "sits", "options": ["emperor", "sits", "tightly", "throne"]},
    {"form": "Mount Vesuvius aggressively destroyed Pompeii.", "correct": "destroyed", "options": ["Mount Vesuvius", "aggressively", "destroyed", "Pompeii"]}
]








SENTENCES_REVIEW = [
    {
        "latin": "puella pulchra reginam tristem oraverat, et dea puellam liberavit.",
        "english": [
            "The beautiful girl had begged the sad queen, and the goddess freed the girl.",
            "A beautiful girl had begged the sad queen, and the goddess freed the girl.",
            "The beautiful girl had begged the unhappy queen, and the goddess freed the girl.",
            "The beautiful girl had begged the sorrowful queen, and the goddess freed the girl.",
            "The beautiful girl had begged the sad queen, and the goddess set free the girl.",
            "The beautiful girl had begged the sad queen, and the goddess set the girl free.",
            "The beautiful girl had begged the sad queen, and the goddess liberated the girl.",
            "The beautiful girl had begged the sad queen, and the goddess released the girl.",
            "The beautiful girl had begged the sad queen, and the goddess has freed the girl.",
            "The lovely girl had begged the sad queen, and the goddess freed the girl.",
            "The pretty girl had begged the sad queen, and the goddess freed the girl.",
            "The beautiful girl had pleaded with the sad queen, and the goddess freed the girl.",
            "The beautiful girl had prayed to the sad queen, and the goddess freed the girl.",
            "The beautiful girl had begged the sad queen, and the goddess did free the girl.",
        ],
        "explanation": (
            "• puella pulchra (the beautiful girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pulchra* (beautiful) is an adjective agreeing with *puella*, both feminine singular {T:nominative}\n"
            "• or{R:a}{P:v}{M:era}{B:t} (had begged)\n"
            "  → *oro* (I beg) is the dictionary form of this verb\n"
            "  → *or-* (beg) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is built on the perfect stem\n"
            "  → *-{M:era}-* shows it is {M:pluperfect}, meaning 'had ___'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• reginam tristem (the sad queen)\n"
            "  → *regin{T:am}* (queen) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "  → *tristem* (sad) is an adjective agreeing with *reginam*, both feminine singular {T:accusative}\n"
            "• *et* (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• dea (the goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• liber{R:a}{P:v}{B:it} (freed)\n"
            "  → *libero* (I free) is the dictionary form of this verb\n"
            "  → *liber-* (free) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is {P:perfect}, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• puellam (the girl)\n"
            "  → *puell{T:am}* (girl) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "multi dei ad ingentem urbem navigaverunt feminasque necaverunt.",
        "english": [
            "Many gods sailed to the huge city and killed the women.",
            "Many gods sailed towards the enormous city, and killed the women.",
            "Many of the gods sailed to the huge city and murdered the women.",
            "Many gods sailed to the huge city, and they killed the women.",
            "Many gods sailed to the massive city and killed the women.",
            "Many gods sailed to the vast city and killed the women.",
            "Many gods sailed to the huge city and slew the women.",
            "Many gods sailed to the huge city and murdered the women.",
            "Many gods have sailed to the huge city and have killed the women.",
            "Many gods sailed towards the huge city and killed the women.",
            "Numerous gods sailed to the huge city and killed the women.",
            "A lot of gods sailed to the huge city and killed the women.",
            "Many gods voyaged to the huge city and killed the women.",
            "Many gods sailed to the huge city, and killed the women.",
        ],
        "explanation": (
            "• multi dei (the many gods)\n"
            "  → *de{T:i}* (gods) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *multi* (many) is an adjective agreeing with *dei*, both masculine plural {T:nominative}\n"
            "• navig{R:a}{P:v}{B:erunt} (sailed)\n"
            "  → *navigo* (I sail) is the dictionary form of this verb\n"
            "  → *navig-* (sail) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is {P:perfect}, meaning 'did' or 'has done'\n"
            "  → *-{B:erunt}* shows it is the they form\n"
            "• ad ingentem urbem (to the huge city)\n"
            "  → *ad* is a preposition that takes the {T:accusative}: *ad + acc* = 'to' / 'towards'\n"
            "  → *urb{T:em}* (city) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "  → *ingentem* (huge) is an adjective agreeing with *urbem*, both feminine singular {T:accusative}\n"
            "• feminas (the women)\n"
            "  → *femin{T:as}* (women) is a noun, 1st declension feminine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• -que (and)\n"
            "  → *-que* means 'and' — it clips onto the end of a word, but you translate 'and' BEFORE that word. So *necaveruntque* = '... and killed'\n"
            "• nec{R:a}{P:v}{B:erunt} (killed)\n"
            "  → *neco* (I kill) is the dictionary form of this verb\n"
            "  → *nec-* (kill) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is {P:perfect}, meaning 'did' or 'has done'\n"
            "  → *-{B:erunt}* shows it is the they form"
        ),
    },
    {
        "latin": "pater tristis filiam amatam liberaverat, sed dea puellam oppugnavit.",
        "english": [
            "The sad father had freed the beloved daughter, but the goddess attacked the girl.",
            "The sad father had freed the loved daughter, but the goddess attacked the girl.",
            "The sad father had freed the daughter, having been loved, but the goddess attacked the girl.",
            "The sad father had freed the daughter who had been loved, but the goddess attacked the girl.",
            "The unhappy father had freed the daughter, having been loved, but the goddess attacked the girl.",
            "The sad father had set free the daughter, having been loved, but the goddess attacked the girl.",
            "The sad father had freed the daughter, having been loved, but the goddess assaulted the girl.",
            "The sad father had freed the daughter who had been loved, but the goddess assaulted the girl.",
            "The sad father had freed the daughter, having been loved, but the goddess has attacked the girl.",
            "The sad father had freed the having-been-loved daughter, but the goddess attacked the girl.",
            "The unhappy father had freed the loved daughter, but the goddess attacked the girl.",
            "The unhappy father had freed the beloved daughter, but the goddess attacked the girl.",
            "The sad father had freed the loved daughter, but the goddess assaulted the girl.",
            "The sad father had freed the beloved daughter, but the goddess assaulted the girl.",
            "The sorrowful father had freed the daughter, having been loved, but the goddess attacked the girl.",
            "The sad father had liberated the daughter, having been loved, but the goddess attacked the girl.",
            "The sad father had liberated the beloved daughter, but the goddess attacked the girl.",
            "The sad father had liberated the loved daughter, but the goddess attacked the girl.",
        ],
        "explanation": (
            "• pater tristis (the sad father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *tristis* (sad) is an adjective agreeing with *pater*, both masculine singular {T:nominative}\n"
            "• liber{R:a}{P:v}{M:era}{B:t} (had freed)\n"
            "  → *libero* (I free) is the dictionary form of this verb\n"
            "  → *liber-* (free) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is built on the perfect stem\n"
            "  → *-{M:era}-* shows it is {M:pluperfect}, meaning 'had ___'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• filiam amatam (the daughter, having been loved)\n"
            "  → *fili{T:am}* (daughter) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "  → *amat{T:am}* (having been loved) is a PPP agreeing with *filiam*, both feminine singular {T:accusative}\n"
            "• *sed* (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• dea (the goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• oppugn{R:a}{P:v}{B:it} (attacked)\n"
            "  → *oppugno* (I attack) is the dictionary form of this verb\n"
            "  → *oppugn-* (attack) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is {P:perfect}, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• puellam (the girl)\n"
            "  → *puell{T:am}* (girl) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "regina laeta tum in insula habitabat, nam dei patrem necaverant.",
        "english": [
            "The happy queen was then living on the island, for the gods had killed the father.",
            "The happy queen was living on the island then, for the gods had killed the father.",
            "The happy queen was living then on the island, for the gods had killed the father.",
            "The happy queen was living then on an island, for the gods had killed the father.",
            "The happy queen was living on the island then, for the gods had killed her father.",
            "The happy queen was living then on the island, for the gods had killed her father.",
            "The happy queen was living then on an island, for the gods had killed her father.",
            "The happy queen was then living on the island, for the gods had killed her father.",
            "A happy queen was living on the island then, for the gods had killed the father.",
            "The happy queen used to live on the island then, for the gods had killed the father.",
            "The happy queen used to live on the island then, for the gods had killed her father.",
            "The happy queen then was living on the island, for the gods had killed the father.",
            "The happy queen used to dwell on the island then, for the gods had killed the father.",
            "The happy queen was inhabiting the island then, for the gods had killed the father.",
            "The happy queen was living in the island then, for the gods had killed the father.",
            "The happy queen was living on the island then, because the gods had killed the father.",
            "The happy queen was living on the island then, because the gods had killed her father.",
            "The happy queen lived on the island then, for the gods had killed the father.",
            "The happy queen kept living on the island then, for the gods had killed the father.",
            "The joyful queen was living on the island then, for the gods had killed the father.",
            "The glad queen was living on the island then, for the gods had killed the father.",
            "The happy queen was living on the island then, for the gods had murdered the father.",
            "The happy queen was living on the island then, for the gods had slain the father.",
        ],
        "explanation": (
            "• regina laeta (the happy queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *laeta* (happy) is an adjective agreeing with *regina*, both feminine singular {T:nominative}\n"
            "• *tum* (then)\n"
            "  → *tum* (then) is an adverb — flexible position in the sentence\n"
            "• in insula (on the island)\n"
            "  → *in* is a preposition; with the {T:ablative} it means 'in' / 'on' (location)\n"
            "  → *insul{T:a}* (island) is a noun, 1st declension feminine singular {T:ablative}\n"
            "• habit{R:a}{P:ba}{B:t} (was living)\n"
            "  → *habito* (I live) is the dictionary form of this verb\n"
            "  → *habit-* (live) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is {P:imperfect}, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• *nam* (for)\n"
            "  → *nam* (for) is a conjunction introducing a reason\n"
            "• dei (the gods)\n"
            "  → *de{T:i}* (gods) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• nec{R:a}{P:v}{M:era}{B:nt} (had killed)\n"
            "  → *neco* (I kill) is the dictionary form of this verb\n"
            "  → *nec-* (kill) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is built on the perfect stem\n"
            "  → *-{M:era}-* shows it is {M:pluperfect}, meaning 'had ___'\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• patrem (the father)\n"
            "  → *patr{T:em}* (father) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "femina pulchra deum rogavit, sed deus feminam pulchram non putavit.",
        "english": [
            "The beautiful woman asked the god, but the god did not think the woman beautiful.",
            "The beautiful woman questioned the god, but the god did not think the woman beautiful.",
            "The beautiful woman asked the god, but the god did not consider the woman beautiful.",
            "The beautiful woman asked the god, but the god did not think the woman pretty.",
            "The beautiful woman has asked the god, but the god did not think the woman beautiful.",
            "The lovely woman asked the god, but the god did not think the woman beautiful.",
            "The beautiful woman did ask the god, but the god did not consider the woman beautiful.",
        ],
        "explanation": (
            "• femina pulchra (the beautiful woman)\n"
            "  → *femin{T:a}* (woman) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pulchra* (beautiful) is an adjective agreeing with *femina*, both feminine singular {T:nominative}\n"
            "• rog{R:a}{P:v}{B:it} (asked)\n"
            "  → *rogo* (I ask) is the dictionary form of this verb\n"
            "  → *rog-* (ask) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is {P:perfect}, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• deum (the god)\n"
            "  → *de{T:um}* (god) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• *sed* (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• deus (the god)\n"
            "  → *de{T:us}* (god) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• feminam pulchram (the woman beautiful)\n"
            "  → *femin{T:am}* (woman) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → *pulchr{T:am}* (beautiful) is an adjective agreeing with *feminam*, both feminine singular {T:accusative}\n"
            "  → *puto* takes a **double accusative**: 'I think X (to be) Y' — *feminam* is the first object, *pulchram* the second\n"
            "• non put{R:a}{P:v}{B:it} (did not think)\n"
            "  → *non* (not) negates the verb\n"
            "  → *puto* (I think) is the dictionary form of this verb\n"
            "  → *put-* (think) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is {P:perfect}, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "dea ad terram ingentem navigabat, et puellae oppugnatae clamabant.",
        "english": [
            "The goddess was sailing to the huge land, and the girls, having been attacked, were shouting.",
            "The goddess was sailing towards the enormous land, and the girls, having been attacked, were shouting.",
            "The goddess used to sail to the vast land, and the girls who had been attacked were shouting.",
            "The goddess was sailing to the huge country, and the attacked girls kept shouting.",
            "The goddess was sailing to the huge land, and the attacked girls were shouting.",
            "The goddess was sailing to the massive land, and the attacked girls were shouting.",
            "The goddess was sailing to the huge land, and the girls who had been attacked were shouting.",
            "The goddess was sailing to the huge land, and the girls, having been assaulted, were shouting.",
            "The goddess kept sailing to the huge land, and the girls, having been attacked, kept shouting.",
            "The goddess used to sail to the huge land, and the girls, having been attacked, used to shout.",
            "The goddess was voyaging to the huge land, and the girls, having been attacked, were crying out.",
        ],
        "explanation": (
            "• dea (the goddess)\n"
            "  → *de{T:a}* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• ad terram ingentem (to the huge land)\n"
            "  → *ad* is a preposition that takes the {T:accusative}: *ad + acc* = 'to' / 'towards'\n"
            "  → *terr{T:am}* (land) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → *ingentem* (huge) is an adjective agreeing with *terram*, both feminine singular {T:accusative}\n"
            "• navig{R:a}{P:ba}{B:t} (was sailing)\n"
            "  → *navigo* (I sail) is the dictionary form of this verb\n"
            "  → *navig-* (sail) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is {P:imperfect}, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• *et* (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• puellae oppugnatae (the girls, having been attacked)\n"
            "  → *puell{T:ae}* (girls) is a noun, 1st declension feminine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *oppugnat{T:ae}* (having been attacked) is a PPP agreeing with *puellae*, both feminine plural {T:nominative}\n"
            "• clam{R:a}{P:ba}{B:nt} (were shouting)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is {P:imperfect}, meaning 'was' or 'were'\n"
            "  → *-{B:nt}* shows it is the they form"
        ),
    },
    {
        "latin": "pater ad insulam appropinquavit, et filiam oppugnatam liberavit.",
        "english": [
            "The father approached the island, and freed the daughter, having been attacked.",
            "The father approached the island, and freed the daughter who had been attacked.",
            "The father drew near to the island, and freed the daughter, having been attacked.",
            "The father came near to the island, and set free the daughter who had been attacked.",
            "The father approached the island, and freed the daughter, having been assaulted.",
            "The father approached the island, and freed the daughter, having been attacked.",
            "The father approached the island, and set free the daughter, having been attacked.",
            "The father drew near to the island, and set free the daughter who had been attacked.",
            "The father approached the island, and liberated the daughter, having been attacked.",
            "The father approached the island, and released the daughter, having been attacked.",
            "The father has approached the island, and freed the daughter, having been attacked.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• ad insulam (to the island)\n"
            "  → *ad* is a preposition that takes the {T:accusative}: *ad + acc* = 'to' / 'towards'\n"
            "  → *insul{T:am}* (island) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• appropinqu{R:a}{P:v}{B:it} (approached)\n"
            "  → *appropinquo* (I approach) is the dictionary form of this verb\n"
            "  → *appropinqu-* (approach) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is {P:perfect}, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• *et* (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• liber{R:a}{P:v}{B:it} (freed)\n"
            "  → *libero* (I free) is the dictionary form of this verb\n"
            "  → *liber-* (free) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is {P:perfect}, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• filiam oppugnatam (the daughter, having been attacked)\n"
            "  → *fili{T:am}* (daughter) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "  → *oppugnat{T:am}* (having been attacked) is a PPP agreeing with *filiam*, both feminine singular {T:accusative}"
        ),
    },
    {
        "latin": "multi dei reginam tristem oraverant, sed regina deis non imperavit.",
        "english": [
            "Many gods had begged the sad queen, but the queen did not order the gods.",
            "Many gods had pleaded with the unhappy queen, but the queen did not order the gods.",
            "Many of the gods had prayed to the sad queen, but the queen did not command the gods.",
            "Many gods had begged the sad queen, but the queen has not ordered the gods.",
            "Many gods had begged the sad queen, but the queen did not command the gods.",
            "Many gods had pleaded with the sad queen, but the queen did not order the gods.",
            "Many gods had prayed to the sad queen, but the queen did not order the gods.",
            "Many gods had begged the unhappy queen, but the queen did not order the gods.",
            "Many gods had begged the sorrowful queen, but the queen did not order the gods.",
            "Numerous gods had begged the sad queen, but the queen did not order the gods.",
            "A lot of gods had begged the sad queen, but the queen did not order the gods.",
            "Many gods had begged the sad queen, but the queen has not commanded the gods.",
        ],
        "explanation": (
            "• multi dei (the many gods)\n"
            "  → *de{T:i}* (gods) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *multi* (many) is an adjective agreeing with *dei*, both masculine plural {T:nominative}\n"
            "• reginam tristem (the sad queen)\n"
            "  → *regin{T:am}* (queen) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "  → *tristem* (sad) is an adjective agreeing with *reginam*, both feminine singular {T:accusative}\n"
            "• or{R:a}{P:v}{M:era}{B:nt} (had begged)\n"
            "  → *oro* (I beg) is the dictionary form of this verb\n"
            "  → *or-* (beg) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is built on the perfect stem\n"
            "  → *-{M:era}-* shows it is {M:pluperfect}, meaning 'had ___'\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• *sed* (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• regina (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• deis (the gods)\n"
            "  → *de{T:is}* (gods) is a noun, 2nd declension masculine plural {T:dative}\n"
            "  → *impero* takes the {T:dative}: literally 'I give orders to' — translate as 'order' (no 'to')\n"
            "• non imper{R:a}{P:v}{B:it} (did not order)\n"
            "  → *non* (not) negates the verb\n"
            "  → *impero* (I order) is the dictionary form of this verb\n"
            "  → *imper-* (order) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is {P:perfect}, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "puella liberata in urbem festinabat, et pater deam tum oravit.",
        "english": [
            "The girl, having been freed, was hurrying into the city, and the father then begged the goddess.",
            "The freed girl was hurrying into the city, and then the father begged the goddess.",
            "The girl who had been freed was rushing to the city, and the father pleaded with the goddess then.",
            "Once freed, the girl was hurrying into the city, and the father prayed to the goddess then.",
            "The girl, having been freed, was hurrying into the city, and the father begged the goddess then.",
            "The girl, having been freed, was rushing into the city, and the father then begged the goddess.",
            "The girl, having been freed, was hastening into the city, and the father then begged the goddess.",
            "The freed girl was hurrying into the city, and the father then begged the goddess.",
            "The liberated girl was hurrying into the city, and the father then begged the goddess.",
            "The girl who had been freed was hurrying into the city, and the father then begged the goddess.",
            "After being freed, the girl was hurrying into the city, and the father then begged the goddess.",
            "The girl, having been freed, used to hurry into the city, and the father then begged the goddess.",
            "The girl, having been freed, kept hurrying into the city, and the father then begged the goddess.",
            "The girl, having been set free, was hurrying into the city, and the father then begged the goddess.",
            "The girl, having been freed, was hurrying to the city, and the father then prayed to the goddess.",
        ],
        "explanation": (
            "• puella liberata (the girl, having been freed)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *liberat{T:a}* (having been freed) is a PPP agreeing with *puella*, both feminine singular {T:nominative}\n"
            "• in urbem (into the city)\n"
            "  → *in* is a preposition; with the {T:accusative} it means 'into' (motion)\n"
            "  → *urb{T:em}* (city) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "• festin{R:a}{P:ba}{B:t} (was hurrying)\n"
            "  → *festino* (I hurry) is the dictionary form of this verb\n"
            "  → *festin-* (hurry) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:ba}-* shows it is {P:imperfect}, meaning 'was' or 'were'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• *et* (and)\n"
            "  → *et* (and) is a conjunction\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• deam (the goddess)\n"
            "  → *de{T:am}* (goddess) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• *tum* (then)\n"
            "  → *tum* (then) is an adverb — flexible position in the sentence\n"
            "• or{R:a}{P:v}{B:it} (begged)\n"
            "  → *oro* (I beg) is the dictionary form of this verb\n"
            "  → *or-* (beg) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is {P:perfect}, meaning 'did' or 'has done'\n"
            "  → *-{B:it}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "deus pulcher pulchras feminas oppugnatas amaverat, sed reginae tristes clamaverant.",
        "english": [
            "The beautiful god had loved the beautiful women, having been attacked, but the sad queens had shouted.",
            "The beautiful god had loved the beautiful women who had been attacked, but the sad queens had shouted.",
            "The beautiful god had liked the beautiful women, having been attacked, but the sad queens had shouted.",
            "The beautiful god had loved the lovely women, having been attacked, but the sad queens had shouted.",
            "The beautiful god had loved the beautiful women who had been attacked, but the unhappy queens had shouted.",
            "The beautiful god had loved the beautiful women, having been attacked, but the sorrowful queens had shouted.",
        ],
        "explanation": (
            "• deus pulcher (the beautiful god)\n"
            "  → *de{T:us}* (god) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pulcher* (beautiful) is an adjective agreeing with *deus*, both masculine singular {T:nominative}\n"
            "• am{R:a}{P:v}{M:era}{B:t} (had loved)\n"
            "  → *amo* (I love) is the dictionary form of this verb\n"
            "  → *am-* (love) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is built on the perfect stem\n"
            "  → *-{M:era}-* shows it is {M:pluperfect}, meaning 'had ___'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• pulchras feminas oppugnatas (the beautiful women, having been attacked)\n"
            "  → *femin{T:as}* (women) is a noun, 1st declension feminine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → *pulchras* (beautiful) is an adjective agreeing with *feminas*, both feminine plural {T:accusative}\n"
            "  → *oppugnat{T:as}* (having been attacked) is a PPP agreeing with *feminas*, both feminine plural {T:accusative}\n"
            "• *sed* (but)\n"
            "  → *sed* (but) is a conjunction\n"
            "• reginae tristes (the sad queens)\n"
            "  → *regin{T:ae}* (queens) is a noun, 1st declension feminine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *tristes* (sad) is an adjective agreeing with *reginae*, both feminine plural {T:nominative}\n"
            "• clam{R:a}{P:v}{M:era}{B:nt} (had shouted)\n"
            "  → *clamo* (I shout) is the dictionary form of this verb\n"
            "  → *clam-* (shout) is the stem\n"
            "  → *-{R:a}-* shows it belongs to the 1st conjugation\n"
            "  → *-{P:v}-* shows it is built on the perfect stem\n"
            "  → *-{M:era}-* shows it is {M:pluperfect}, meaning 'had ___'\n"
            "  → *-{B:nt}* shows it is the they form"
        ),
    },
]

PARSE_TRANSLATE_QUESTIONS = [
    {"form":"navigas",       "tense":"present",    "person":"2nd","number":"singular","translation":"you (sg) sail"},
    {"form":"clamant",       "tense":"present",    "person":"3rd","number":"plural",  "translation":"they shout"},
    {"form":"oppugnamus",    "tense":"present",    "person":"1st","number":"plural",  "translation":"we attack"},
    {"form":"rogabat",       "tense":"imperfect",  "person":"3rd","number":"singular","translation":"he/she was asking"},
    {"form":"liberabant",    "tense":"imperfect",  "person":"3rd","number":"plural",  "translation":"they were freeing"},
    {"form":"necabam",       "tense":"imperfect",  "person":"1st","number":"singular","translation":"I was killing"},
    {"form":"amabis",        "tense":"future",     "person":"2nd","number":"singular","translation":"you (sg) will love"},
    {"form":"festinabit",    "tense":"future",     "person":"3rd","number":"singular","translation":"he/she will hurry"},
    {"form":"habitabunt",    "tense":"future",     "person":"3rd","number":"plural",  "translation":"they will live"},
    {"form":"clamavit",      "tense":"perfect",    "person":"3rd","number":"singular","translation":"he/she shouted"},
    {"form":"navigaverunt",  "tense":"perfect",    "person":"3rd","number":"plural",  "translation":"they sailed"},
    {"form":"rogavisti",     "tense":"perfect",    "person":"2nd","number":"singular","translation":"you (sg) asked"},
    {"form":"amaverat",      "tense":"pluperfect", "person":"3rd","number":"singular","translation":"he/she had loved"},
    {"form":"necaveramus",   "tense":"pluperfect", "person":"1st","number":"plural",  "translation":"we had killed"},
    {"form":"liberaverant",  "tense":"pluperfect", "person":"3rd","number":"plural",  "translation":"they had freed"},
]

VERB_IDENTIFY = [
    {"form": "The ancient Romans built wide roads.", "correct": "built", "options": ["ancient", "Romans", "built", "roads"]},
    {"form": "Gladiators fight in the arena.", "correct": "fight", "options": ["Gladiators", "fight", "in", "arena"]},
    {"form": "We are learning about the Roman Empire.", "correct": "are learning", "options": ["We", "are learning", "Roman", "Empire"]},
    {"form": "The emperor sits tightly on his throne.", "correct": "sits", "options": ["emperor", "sits", "tightly", "throne"]},
    {"form": "Mount Vesuvius aggressively destroyed Pompeii.", "correct": "destroyed", "options": ["Mount Vesuvius", "aggressively", "destroyed", "Pompeii"]}
]


























































# ── Sentence-vocab tile content for Node 1 (filtered to lemmas that actually
# appear in Node 1 sentences, plus BE_FORMS) ────────────────────────────────
from sentence_vocab_scanner import build_tile_vocab as _build_tile_vocab
NODE1_TILE_VOCAB = _build_tile_vocab(
    SENTENCES_PRESENT_TEST + SENTENCES_PRESENT_SYSTEM
    + SENTENCES_ACTIVE + SENTENCES_PPP + SENTENCES_REVIEW
)


SETS = [
    # -- Node 0: Introduction --------------------------------------------------
    {
        "id":1, "node":0, "node_title":"Introduction",
        "title":"What is a verb?",
        "type":"reference", "optional":True,
        "sell":"A verb is a **doing, being, or having word**.\n\nIn Latin, a verb typically appears at the end of the sentence:\n\n*miles regem necat* (the soldier kills the king)\n\nNotice how *necat* ('kills') appears at the end of the sentence.",
    },
    {
        "id":2, "node":0, "node_title":"Introduction",
        "title":"What is a conjugation?",
        "type":"reference", "optional":True,
        "sell":"A conjugation is a **family of verbs** that follow the same pattern of endings.\n\nLatin has **four conjugations**. The exercises below introduce you to them one by one.",
    },
    {
        "id":3, "node":0, "node_title":"Introduction",
        "title":"What is parsing?",
        "type":"reference", "optional":True,
        "sell":"To parse a verb means to identify when and who is doing the action.",
        "screens":[{
            "heading":"What is parsing?",
            "body":"To parse a verb means to identify when and who is doing the action.\n\nWhen asked to parse a verb, you must describe:\n\n• Its **person** and **number** (I / you (sg) / he, she, it / we / you (pl) / they)\n\n• Its **tense** (present / future / imperfect / perfect / pluperfect)",
            "body_align":"left",
        }],
    },
    {
        "id":4, "node":0, "node_title":"Introduction",
        "title":"What are principal parts?",
        "type":"reference", "optional":True,
        "sell":"Every verb in Latin has four principal parts. Learning them allows you to recognise any form of the verb.",
        "screens":[{
            "heading":"What are principal parts?",
            "body":"Every verb in Latin has four principal parts. Learning them allows you to recognise any form of the verb.\n\nHere are the four principal parts of *specto*:",
            "table_note":"Memorising your principal parts will improve your ability to identify verb forms quickly in the exam. It also helps you recognise derivatives in English. For example the word 'spectate' comes from the fourth principal part, *spectatus*.",
            "principal_parts_table":[
                {"part":"1st","name":"Present tense 'I' form","latin":"specto","english":"I watch"},
                {"part":"2nd","name":"Infinitive","latin":"spectare","english":"to watch"},
                {"part":"3rd","name":"Perfect tense 'I' form","latin":"spectavi","english":"I watched"},
                {"part":"4th","name":"Perfect Passive Participle","latin":"spectatus","english":"having been watched"},
            ],
        }],
    },

    # -- Node 1: 1st Conjugation -----------------------------------------------
    {
        "id":5, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Sentence Vocabulary",
        "type":"vocab", "optional":True,
        "sell":"This set teaches you the nouns, adjectives, and prepositions that appear in sentences throughout this node. The set is optional.",
        "pass_mark":80,
        "content":{"vocab":NODE1_TILE_VOCAB, "mode":"meanings"},
    },
    {
        "id":6, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Present: 'I' Form",
        "badge":"Principal Part",
        "type":"verbs",
        "sell":"There are 13 first conjugation verbs commonly used at GCSE. This set teaches you the **first principal part** — the present tense 'I' form.",
        "pass_mark":80,
        "screens":[
            {
                "heading":"The 1st Principal Part",
                "body":"The **1st principal part** is the 'I' form of the verb. Notice how they all end in *-o*:\n\n\u2022 *amo* = I love\n\u2022 *clamo* = I shout\n\u2022 *rogo* = I ask",
            }
        ],
        "content":{"verbs":VERBS_1ST_TOP150, "mode":"meanings"},
    },
    {
        "id":7, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Present Tense Endings",
        "type":"translate_form",
        "sell":"The ending of a Latin verb tells you who is doing the action. This set teaches you all six present tense endings for 1st conjugation verbs.",
        "pass_mark":80,
        "screens":[
            {
                "heading":"1st Conjugation: Present Tense Endings",
                "body":"1st conjugation verbs all have *-a-* as their stem vowel. Different endings tell you who is doing the action:",
                "table":[
                    {"conjugation":"I",             "infinitive_ending":"-o",   "example":"amo",    "ep":[["am",""],["o","blue"]]},
                    {"conjugation":"you (sg)",       "infinitive_ending":"-s",   "example":"amas",   "ep":[["am",""],["a","coral"],["s","blue"]]},
                    {"conjugation":"he / she / it",  "infinitive_ending":"-t",   "example":"amat",   "ep":[["am",""],["a","coral"],["t","blue"]]},
                    {"conjugation":"we",             "infinitive_ending":"-mus", "example":"amamus", "ep":[["am",""],["a","coral"],["mus","blue"]]},
                    {"conjugation":"you (pl)",       "infinitive_ending":"-tis", "example":"amatis", "ep":[["am",""],["a","coral"],["tis","blue"]]},
                    {"conjugation":"they",           "infinitive_ending":"-nt",  "example":"amant",  "ep":[["am",""],["a","coral"],["nt","blue"]]},
                ],
                "table_note":"The *-a-* stem vowel is the signature of the 1st conjugation. All 1st conjugation verbs have it — except in their **'I' form** (notice it's *am{B:o}*, not *am{R:a}{B:o}*).\n\nColour key:\n**red** = stem vowel\n**blue** = person ending",
                "infinitive_ending_header":"Ending",
            }
        ],
        "content":{"questions":QUESTIONS_PRESENT}
    },
    {
        "id":8, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"The Present Tense",
        "type":"sentences",
        "sell":"This set practises translating sentences using the first conjugation present tense verbs that are most common at GCSE.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PRESENT_TEST},
    },
    {
        "id":9, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Infinitive",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **second principal part** — the infinitive, or 'to…' form of the verb.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_1ST_TOP150,
            "mode":"infinitives",
            "show_parts_so_far":1,
            "pattern_screen":{
                "title":"1st Conjugation: The Infinitive",
                "subtitle":"The infinitive is formed by adding *-re* to the present stem:",
                "examples":[
                    {"present":"amo",         "full":"amare",         "ending":"re","english":"to love"},
                    {"present":"clamo",       "full":"clamare",       "ending":"re","english":"to shout"},
                    {"present":"festino",     "full":"festinare",     "ending":"re","english":"to hurry"},
                    {"present":"habito",      "full":"habitare",      "ending":"re","english":"to live"},
                    {"present":"impero",      "full":"imperare",      "ending":"re","english":"to order"},
                    {"present":"libero",      "full":"liberare",      "ending":"re","english":"to free"},
                    {"present":"neco",        "full":"necare",        "ending":"re","english":"to kill"},
                    {"present":"navigo",      "full":"navigare",      "ending":"re","english":"to sail"},
                    {"present":"oppugno",     "full":"oppugnare",     "ending":"re","english":"to attack"},
                    {"present":"oro",         "full":"orare",         "ending":"re","english":"to beg"},
                    {"present":"puto",        "full":"putare",        "ending":"re","english":"to think"},
                    {"present":"rogo",        "full":"rogare",        "ending":"re","english":"to ask"},
                    {"present":"appropinquo","full":"appropinquare","ending":"re","english":"to approach"},
                ],
                "footnote":"The stem of 1st conjugation verbs ends in *-a*. The infinitive is always stem + *-re*."
            }
        },
    },
    {
        "id":10, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"The Imperfect Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **imperfect tense** — used for continuous or repeated action in the past.",
        "pass_mark":80,
        "screens":[
            {
                "heading":"The Imperfect Tense",
                "body":"The imperfect tense refers to repeated or ongoing action in the past. In Latin it is formed by inserting the tense marker *-ba-* between the present stem and the person ending.\n\nNote: the I form ends in *-bam* (not *-bao*).",
                "table":[
                    {"conjugation":"I",             "infinitive_ending":"-bam",  "example":"amabam",  "tr":"I was loving",    "ep":[["am",""],["a","coral"],["ba","purple"],["m","blue"]]},
                    {"conjugation":"you (sg)",       "infinitive_ending":"-bas",  "example":"amabas",  "tr":"you were loving", "ep":[["am",""],["a","coral"],["ba","purple"],["s","blue"]]},
                    {"conjugation":"he / she / it",  "infinitive_ending":"-bat",  "example":"amabat",  "tr":"he/she was loving","ep":[["am",""],["a","coral"],["ba","purple"],["t","blue"]]},
                    {"conjugation":"we",             "infinitive_ending":"-bamus","example":"amabamus","tr":"we were loving",   "ep":[["am",""],["a","coral"],["ba","purple"],["mus","blue"]]},
                    {"conjugation":"you (pl)",       "infinitive_ending":"-batis","example":"amabatis","tr":"you were loving",  "ep":[["am",""],["a","coral"],["ba","purple"],["tis","blue"]]},
                    {"conjugation":"they",           "infinitive_ending":"-bant", "example":"amabant", "tr":"they were loving", "ep":[["am",""],["a","coral"],["ba","purple"],["nt","blue"]]},
                ],
                "table_note":"The tense marker *-ba-* appears in every imperfect form. Be careful not to confuse it with the future tense markers *-bo-*, *-bi-*, *-bu-*.\n\nColour key:\n**red** = stem vowel\n**purple** = tense marker (*-ba-*)\n**blue** = person ending",
                "infinitive_ending_header":"Ending"
            }
        ],
        "content":{"questions":QUESTIONS_IMPERFECT}
    },
    {
        "id":11, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"The Future Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **future tense** — used for actions that 'will' happen.",
        "pass_mark":80,
        "screens":[
            {
                "heading":"The Future Tense",
                "body":"Where in English we add **'will'** to express the future tense, in Latin the future tense is formed by inserting *-bo-*, *-bi-*, or *-bu-* between the present stem and the person ending.",
                "table":[
                    {"conjugation":"I",             "infinitive_ending":"-bo",   "example":"amabo",   "tr":"I will love",       "ep":[["am",""],["a","coral"],["bo","purple"]]},
                    {"conjugation":"you (sg)",       "infinitive_ending":"-bis",  "example":"amabis",  "tr":"you will love",     "ep":[["am",""],["a","coral"],["bi","purple"],["s","blue"]]},
                    {"conjugation":"he / she / it",  "infinitive_ending":"-bit",  "example":"amabit",  "tr":"he/she will love",  "ep":[["am",""],["a","coral"],["bi","purple"],["t","blue"]]},
                    {"conjugation":"we",             "infinitive_ending":"-bimus","example":"amabimus","tr":"we will love",       "ep":[["am",""],["a","coral"],["bi","purple"],["mus","blue"]]},
                    {"conjugation":"you (pl)",       "infinitive_ending":"-bitis","example":"amabitis","tr":"you will love",      "ep":[["am",""],["a","coral"],["bi","purple"],["tis","blue"]]},
                    {"conjugation":"they",           "infinitive_ending":"-bunt", "example":"amabunt", "tr":"they will love",    "ep":[["am",""],["a","coral"],["bu","purple"],["nt","blue"]]},
                ],
                "table_note":"Colour key:\n**red** = stem vowel\n**purple** = tense marker (*-bo-*/*-bi-*/*-bu-*)\n**blue** = person ending",
                "infinitive_ending_header":"Ending"
            }
        ],
        "content":{"questions":QUESTIONS_FUTURE}
    },
    {
        "id":12, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"The Present System",
        "type":"sentences",
        "sell":"This set tests your ability to translate sentences that use the present, future, and imperfect tenses.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PRESENT_SYSTEM},
    },
    {
        "id":13, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Perfect: 'I' Form",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **third principal part** — the perfect 'I' form.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_1ST_TOP150,
            "mode":"perfects",
            "show_parts_so_far":2,
            "pattern_screen":{
                "title":"1st Conjugation: The Perfect",
                "subtitle":"Take the infinitive, remove the -re, add -vi:",
                "examples":[
                    {"full":"amavi","ending":"vi","inf":"amare","english":"I loved","present":"amo"},
                    {"full":"rogavi","ending":"vi","inf":"rogare","english":"I asked","present":"rogo"},
                    {"full":"necavi","ending":"vi","inf":"necare","english":"I killed","present":"neco"},
                    {"full":"navigavi","ending":"vi","inf":"navigare","english":"I sailed","present":"navigo"},
                    {"full":"festinavi","ending":"vi","inf":"festinare","english":"I hurried","present":"festino"},
                ],
                "footnote":"The *-v-* is the past marker. Look for it to spot any perfect tense form."
            }
        },
    },
    {
        "id":14, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Perfect Tense: All Endings",
        "type":"translate_form",
        "sell":"The ending of a Latin verb tells you who is doing the action. This set teaches you all six forms of the **perfect tense**.",
        "pass_mark":80,
        "screens":[
            {
                "heading":"The Perfect Tense",
                "body":"The perfect tense is used for completed actions in the past. In English, perfect verbs often end in -ed. In Latin, the perfect is often formed by inserting one of the tense markers *-v-*, *-u-*, *-x-*, or *-s-* between the present stem and the unique perfect person endings.\n\nFor the 1st conjugation, the *-v-* after the stem is the clearest sign of the perfect. Look for it in every form.",
                "table":[
                    {"conjugation":"I",             "infinitive_ending":"-i",     "example":"amavi",    "tr":"I loved",       "ep":[["am",""],["a","coral"],["v","purple"],["i","blue"]]},
                    {"conjugation":"you (sg)",       "infinitive_ending":"-isti",  "example":"amavisti", "tr":"you loved",     "ep":[["am",""],["a","coral"],["v","purple"],["isti","blue"]]},
                    {"conjugation":"he / she / it",  "infinitive_ending":"-it",    "example":"amavit",   "tr":"he/she loved",  "ep":[["am",""],["a","coral"],["v","purple"],["it","blue"]]},
                    {"conjugation":"we",             "infinitive_ending":"-imus",  "example":"amavimus", "tr":"we loved",      "ep":[["am",""],["a","coral"],["v","purple"],["imus","blue"]]},
                    {"conjugation":"you (pl)",       "infinitive_ending":"-istis", "example":"amavistis","tr":"you loved",     "ep":[["am",""],["a","coral"],["v","purple"],["istis","blue"]]},
                    {"conjugation":"they",           "infinitive_ending":"-erunt", "example":"amaverunt","tr":"they loved",    "ep":[["am",""],["a","coral"],["v","purple"],["erunt","blue"]]},
                ],
                "table_note":"The *-v-* after the stem is the clearest sign of any 1st conjugation perfect. Look for it in every form.\n\nColour key:\n**red** = stem vowel\n**purple** = tense marker (*-v-*)\n**blue** = person ending",
                "infinitive_ending_header":"Ending"
            }
        ],
        "content":{"questions":QUESTIONS_PERFECT}
    },
    {
        "id":15, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"The Pluperfect Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **pluperfect tense** — used for actions completed before another past event ('had loved', 'had killed').",
        "pass_mark":80,
        "screens":[
            {
                "heading":"The Pluperfect Tense",
                "body":"The pluperfect tense is used for actions completed before another past event ('had loved', 'had killed').\n\nWhere in English we add **'had'** to express the pluperfect, in Latin the pluperfect is built on the perfect stem by inserting the tense marker *-era-* between the perfect stem and the person ending.",
                "table":[
                    {"conjugation":"I",             "infinitive_ending":"-eram",  "example":"amaveram",  "tr":"I had loved",       "ep":[["am",""],["a","coral"],["v","purple"],["era","pink"],["m","blue"]]},
                    {"conjugation":"you (sg)",       "infinitive_ending":"-eras",  "example":"amaveras",  "tr":"you had loved",     "ep":[["am",""],["a","coral"],["v","purple"],["era","pink"],["s","blue"]]},
                    {"conjugation":"he / she / it",  "infinitive_ending":"-erat",  "example":"amaverat",  "tr":"he/she had loved",  "ep":[["am",""],["a","coral"],["v","purple"],["era","pink"],["t","blue"]]},
                    {"conjugation":"we",             "infinitive_ending":"-eramus","example":"amaveramus","tr":"we had loved",       "ep":[["am",""],["a","coral"],["v","purple"],["era","pink"],["mus","blue"]]},
                    {"conjugation":"you (pl)",       "infinitive_ending":"-eratis","example":"amaveratis","tr":"you had loved",      "ep":[["am",""],["a","coral"],["v","purple"],["era","pink"],["tis","blue"]]},
                    {"conjugation":"they",           "infinitive_ending":"-erant", "example":"amaverant", "tr":"they had loved",    "ep":[["am",""],["a","coral"],["v","purple"],["era","pink"],["nt","blue"]]},
                ],
                "table_note":"The pluperfect can always be recognised by its *-era-* tense marker. Be careful not to confuse the perfect *-erunt* with the pluperfect *-erant* — whenever you see *-era-*, it must be pluperfect.\n\nColour key:\n**red** = stem vowel\n**purple** = perfect-stem marker (*-v-*)\n**pink** = pluperfect marker (*-era-*)\n**blue** = person ending",
                "infinitive_ending_header":"Ending"
            }
        ],
        "content":{"questions":QUESTIONS_PLUPERFECT}
    },
    {
        "id":16, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Perfect & Pluperfect",
        "type":"sentences",
        "sell":"This set practises translating sentences using the perfect and pluperfect tenses.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_ACTIVE},
    },
    {
        "id":17, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Perfect Passive Participle (PPP)",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **fourth principal part** — the **Perfect Passive Participle (PPP)**.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_1ST_TOP150,
            "mode":"ppps",
            "show_parts_so_far":3,
            "pattern_screen":{
                "title":"1st Conjugation: The PPP",
                "subtitle":"Take the present stem and add *-tus*:",
                "examples":[
                    {"present":"amo",  "infinitive":"amare",  "perfect":"amavi",  "full":"amatus",  "ending":"tus","english":"having been loved"},
                    {"present":"rogo", "infinitive":"rogare", "perfect":"rogavi", "full":"rogatus", "ending":"tus","english":"having been asked"},
                    {"present":"neco", "infinitive":"necare", "perfect":"necavi", "full":"necatus", "ending":"tus","english":"having been killed"},
                ],
                "footnote":"You can always translate a PPP as **'having been'** + the verb's meaning — e.g. *amatus* = 'having been loved'. It acts like an adjective in the sentence, agreeing with the noun it describes in gender, number, and case.\n\n**PPP + est / sunt = perfect passive**: *necatus est* = 'he was killed'; *necati sunt* = 'they were killed'.\n\nNote: *festino*, *navigo*, and *appropinquo* have no PPP."
            }
        },
    },
    {
        "id":18, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Perfect Passive Participles",
        "type":"sentences",
        "sell":"This set practises translating sentences that contain the **Perfect Passive Participle**. You can always translate a PPP with **'having been'**.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PPP},
    },
    {
        "id":19, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Build the Principal Parts",
        "type":"building_parts",
        "sell":"This set provides you with the present 'I' form of the verbs you have studied and tests you on their other principal parts: the **infinitive**, the **perfect**, and the **PPP**.",
        "pass_mark":80,
        "content":{"verbs":VERBS_1ST_TOP150, "mode":"all_four", "show_parts_so_far":4, "gap_positions":[1, 2, 3]},
    },
    {
        "id":20, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Review",
        "type":"review",
        "badge":"test",
        "sell":"This set reviews everything in the node: parse and translate individual verb forms, then translate sentences covering all tenses and PPPs.",
        "pass_mark":80,
        "content":{
            "sentences": SENTENCES_REVIEW,
            "parse_translate": PARSE_TRANSLATE_QUESTIONS,
        },
    },
]



# ── Nodes 2-5 wired in for live testing ─────────────────────────────────────
from data_node2 import SETS_N2  # 16 tiles, ids 21-36, mirroring Node 1 exactly
from data_node3 import SETS_N3  # 16 tiles, ids 37-52, mirroring Node 1
from data_node4 import SETS_N4  # 16 tiles, ids 53-68, mirroring Node 1
from data_node5 import SETS_N5  # 5 tiles, ids 69-73, verb principal parts consolidation
# Node 6 (irregular verbs) — backed up at _backup/data_node6_irregulars_BACKUP.py

SETS += SETS_N2 + SETS_N3 + SETS_N4 + SETS_N5

# Tile order: Nodes 1-5
_order = [1,4,2,3, 6,7,5,8, 9,11,10,12, 13,14,15,16, 17,18,19,20,
          21,22,23,24, 25,26,27,28, 29,30,31,32, 33,34,35,36,
          37,38,39,40, 41,42,43,44, 45,46,47,48, 49,50,51,52,
          53,54,55,56, 57,58,59,60, 61,62,63,64, 65,66,67,68,
          69, 70, 71, 72, 73]
SETS = [next(s for s in SETS if s["id"]==i) for i in _order]

SETS_BY_ID = {s["id"]: s for s in SETS}
