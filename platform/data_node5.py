"""
Latin GCSE Mastery Platform — Node 5: Verb Principal Parts Consolidation.

All 120 verbs from the Eduqas GCSE Latin vocabulary list, organised by
conjugation. Each set asks pupils to:
  • type one randomly-chosen missing principal part (infinitive, perfect, or PPP)
  • type the English meaning

Sets:
  Set 69 — 1st conjugation (37 verbs)
  Set 70 — 2nd conjugation (19 verbs)
  Set 71 — 3rd conjugation (55 verbs)
  Set 72 — 4th conjugation  (9 verbs)
  Set 73 — All 120 verbs, consolidation run
"""

NODE5_TITLE = "Verb Principal Parts"

# ── Verb data ──────────────────────────────────────────────────────────────────
# Each entry: present, infinitive, perfect, ppp (None if absent), meanings, conj
# Deponents: 'perfect' holds the form used (e.g. "conatus sum"); ppp = None.
# Note: puto putare putavi putatus is listed as conj 3 in the Eduqas vocab list
# despite its infinitive following a 1st-conjugation pattern.

VERBS_ALL = [
    # ─── 1st Conjugation (37 verbs) ───────────────────────────────────────────
    {"present":"adiuvo",      "infinitive":"adiuvare",      "perfect":"adiuvi",       "ppp":"adiutus",     "meanings":["help"],                               "conj":1},
    {"present":"ambulo",      "infinitive":"ambulare",      "perfect":"ambulavi",     "ppp":None,          "meanings":["walk"],                               "conj":1},
    {"present":"amo",         "infinitive":"amare",         "perfect":"amavi",        "ppp":"amatus",      "meanings":["love","like"],                        "conj":1},
    {"present":"appropinquo", "infinitive":"appropinquare", "perfect":"appropinquavi","ppp":None,          "meanings":["approach","come near to"],            "conj":1},
    {"present":"celo",        "infinitive":"celare",        "perfect":"celavi",       "ppp":"celatus",     "meanings":["hide"],                               "conj":1},
    {"present":"clamo",       "infinitive":"clamare",       "perfect":"clamavi",      "ppp":"clamatus",    "meanings":["shout"],                              "conj":1},
    {"present":"cogito",      "infinitive":"cogitare",      "perfect":"cogitavi",     "ppp":"cogitatus",   "meanings":["think","consider"],                   "conj":1},
    {"present":"curo",        "infinitive":"curare",        "perfect":"curavi",       "ppp":"curatus",     "meanings":["look after","care for","supervise"],  "conj":1},
    {"present":"despero",     "infinitive":"desperare",     "perfect":"desperavi",    "ppp":"desperatus",  "meanings":["despair"],                            "conj":1},
    {"present":"do",          "infinitive":"dare",          "perfect":"dedi",         "ppp":"datus",       "meanings":["give"],                               "conj":1},
    {"present":"exspecto",    "infinitive":"exspectare",    "perfect":"exspectavi",   "ppp":"exspectatus", "meanings":["wait for"],                           "conj":1},
    {"present":"festino",     "infinitive":"festinare",     "perfect":"festinavi",    "ppp":None,          "meanings":["hurry"],                              "conj":1},
    {"present":"habito",      "infinitive":"habitare",      "perfect":"habitavi",     "ppp":"habitatus",   "meanings":["live"],                               "conj":1},
    {"present":"impero",      "infinitive":"imperare",      "perfect":"imperavi",     "ppp":"imperatus",   "meanings":["order","command"],                    "conj":1},
    {"present":"intro",       "infinitive":"intrare",       "perfect":"intravi",      "ppp":"intratus",    "meanings":["enter"],                              "conj":1},
    {"present":"laboro",      "infinitive":"laborare",      "perfect":"laboravi",     "ppp":None,          "meanings":["work"],                               "conj":1},
    {"present":"lacrimo",     "infinitive":"lacrimare",     "perfect":"lacrimavi",    "ppp":None,          "meanings":["weep","cry"],                         "conj":1},
    {"present":"laudo",       "infinitive":"laudare",       "perfect":"laudavi",      "ppp":"laudatus",    "meanings":["praise"],                             "conj":1},
    {"present":"libero",      "infinitive":"liberare",      "perfect":"liberavi",     "ppp":"liberatus",   "meanings":["free","set free"],                    "conj":1},
    {"present":"narro",       "infinitive":"narrare",       "perfect":"narravi",      "ppp":"narratus",    "meanings":["tell","relate"],                      "conj":1},
    {"present":"navigo",      "infinitive":"navigare",      "perfect":"navigavi",     "ppp":None,          "meanings":["sail"],                               "conj":1},
    {"present":"neco",        "infinitive":"necare",        "perfect":"necavi",       "ppp":"necatus",     "meanings":["kill"],                               "conj":1},
    {"present":"nuntio",      "infinitive":"nuntiare",      "perfect":"nuntiavi",     "ppp":"nuntiatus",   "meanings":["announce","report"],                  "conj":1},
    {"present":"oppugno",     "infinitive":"oppugnare",     "perfect":"oppugnavi",    "ppp":"oppugnatus",  "meanings":["attack"],                             "conj":1},
    {"present":"oro",         "infinitive":"orare",         "perfect":"oravi",        "ppp":"oratus",      "meanings":["beg","beg for"],                      "conj":1},
    {"present":"paro",        "infinitive":"parare",        "perfect":"paravi",       "ppp":"paratus",     "meanings":["prepare"],                            "conj":1},
    {"present":"porto",       "infinitive":"portare",       "perfect":"portavi",      "ppp":"portatus",    "meanings":["carry"],                              "conj":1},
    {"present":"postulo",     "infinitive":"postulare",     "perfect":"postulavi",    "ppp":"postulatus",  "meanings":["demand"],                             "conj":1},
    {"present":"pugno",       "infinitive":"pugnare",       "perfect":"pugnavi",      "ppp":None,          "meanings":["fight"],                              "conj":1},
    {"present":"rogo",        "infinitive":"rogare",        "perfect":"rogavi",       "ppp":"rogatus",     "meanings":["ask","ask for"],                      "conj":1},
    {"present":"saluto",      "infinitive":"salutare",      "perfect":"salutavi",     "ppp":"salutatus",   "meanings":["greet"],                              "conj":1},
    {"present":"servo",       "infinitive":"servare",       "perfect":"servavi",      "ppp":"servatus",    "meanings":["save","look after"],                  "conj":1},
    {"present":"specto",      "infinitive":"spectare",      "perfect":"spectavi",     "ppp":"spectatus",   "meanings":["look at","watch"],                    "conj":1},
    {"present":"sto",         "infinitive":"stare",         "perfect":"steti",        "ppp":None,          "meanings":["stand"],                              "conj":1},
    {"present":"supero",      "infinitive":"superare",      "perfect":"superavi",     "ppp":"superatus",   "meanings":["overcome","overpower"],               "conj":1},
    {"present":"voco",        "infinitive":"vocare",        "perfect":"vocavi",       "ppp":"vocatus",     "meanings":["call"],                               "conj":1},

    # ─── 2nd Conjugation (19 verbs) ───────────────────────────────────────────
    {"present":"appareo",    "infinitive":"apparere",    "perfect":"apparui",   "ppp":None,         "meanings":["appear"],                         "conj":2},
    {"present":"debeo",      "infinitive":"debere",      "perfect":"debui",     "ppp":"debitus",    "meanings":["owe","ought","should","must"],     "conj":2},
    {"present":"deleo",      "infinitive":"delere",      "perfect":"delevi",    "ppp":"deletus",    "meanings":["destroy"],                        "conj":2},
    {"present":"habeo",      "infinitive":"habere",      "perfect":"habui",     "ppp":"habitus",    "meanings":["have"],                           "conj":2},
    {"present":"iaceo",      "infinitive":"iacere",      "perfect":"iacui",     "ppp":None,         "meanings":["lie"],                            "conj":2},
    {"present":"iubeo",      "infinitive":"iubere",      "perfect":"iussi",     "ppp":"iussus",     "meanings":["order"],                          "conj":2},
    {"present":"maneo",      "infinitive":"manere",      "perfect":"mansi",     "ppp":None,         "meanings":["remain","stay"],                  "conj":2},
    {"present":"pareo",      "infinitive":"parere",      "perfect":"parui",     "ppp":None,         "meanings":["obey"],                           "conj":2},
    {"present":"persuadeo",  "infinitive":"persuadere",  "perfect":"persuasi",  "ppp":None,         "meanings":["persuade"],                       "conj":2},
    {"present":"placeo",     "infinitive":"placere",     "perfect":"placui",    "ppp":None,         "meanings":["please"],                         "conj":2},
    {"present":"praebeo",    "infinitive":"praebere",    "perfect":"praebui",   "ppp":"praebitus",  "meanings":["provide"],                        "conj":2},
    {"present":"respondeo",  "infinitive":"respondere",  "perfect":"respondi",  "ppp":"responsus",  "meanings":["reply"],                          "conj":2},
    {"present":"rideo",      "infinitive":"ridere",      "perfect":"risi",      "ppp":None,         "meanings":["laugh","smile"],                  "conj":2},
    {"present":"sedeo",      "infinitive":"sedere",      "perfect":"sedi",      "ppp":None,         "meanings":["sit"],                            "conj":2},
    {"present":"taceo",      "infinitive":"tacere",      "perfect":"tacui",     "ppp":"tacitus",    "meanings":["be silent","be quiet"],           "conj":2},
    {"present":"teneo",      "infinitive":"tenere",      "perfect":"tenui",     "ppp":"tentus",     "meanings":["hold","keep","possess"],          "conj":2},
    {"present":"terreo",     "infinitive":"terrere",     "perfect":"terrui",    "ppp":"territus",   "meanings":["frighten"],                       "conj":2},
    {"present":"timeo",      "infinitive":"timere",      "perfect":"timui",     "ppp":None,         "meanings":["fear","be afraid"],               "conj":2},
    {"present":"video",      "infinitive":"videre",      "perfect":"vidi",      "ppp":"visus",      "meanings":["see"],                            "conj":2},

    # ─── 3rd Conjugation (55 verbs) ───────────────────────────────────────────
    {"present":"accido",     "infinitive":"accidere",    "perfect":"accidi",       "ppp":None,           "meanings":["happen"],                            "conj":3},
    {"present":"accipio",    "infinitive":"accipere",    "perfect":"accepi",       "ppp":"acceptus",     "meanings":["accept","receive","take in"],         "conj":3},
    {"present":"ago",        "infinitive":"agere",       "perfect":"egi",          "ppp":"actus",        "meanings":["do","act","drive"],                   "conj":3},
    {"present":"bibo",       "infinitive":"bibere",      "perfect":"bibi",         "ppp":None,           "meanings":["drink"],                             "conj":3},
    {"present":"cado",       "infinitive":"cadere",      "perfect":"cecidi",       "ppp":"casus",        "meanings":["fall"],                              "conj":3},
    {"present":"capio",      "infinitive":"capere",      "perfect":"cepi",         "ppp":"captus",       "meanings":["take","catch","capture"],             "conj":3},
    {"present":"cognosco",   "infinitive":"cognoscere",  "perfect":"cognovi",      "ppp":"cognitus",     "meanings":["get to know","find out","learn"],     "conj":3},
    {"present":"cogo",       "infinitive":"cogere",      "perfect":"coegi",        "ppp":"coactus",      "meanings":["force","compel"],                    "conj":3},
    {"present":"conficio",   "infinitive":"conficere",   "perfect":"confeci",      "ppp":"confectus",    "meanings":["finish","wear out","exhaust"],        "conj":3},
    {"present":"conspicio",  "infinitive":"conspicere",  "perfect":"conspexi",     "ppp":"conspectus",   "meanings":["catch sight of","notice"],            "conj":3},
    {"present":"constituo",  "infinitive":"constituere", "perfect":"constitui",    "ppp":"constitutus",  "meanings":["decide"],                            "conj":3},
    {"present":"consumo",    "infinitive":"consumere",   "perfect":"consumpsi",    "ppp":"consumptus",   "meanings":["eat"],                               "conj":3},
    {"present":"credo",      "infinitive":"credere",     "perfect":"credidi",      "ppp":"creditus",     "meanings":["believe","trust"],                   "conj":3},
    {"present":"cupio",      "infinitive":"cupere",      "perfect":"cupivi",       "ppp":None,           "meanings":["want","desire"],                     "conj":3},
    {"present":"curro",      "infinitive":"currere",     "perfect":"cucurri",      "ppp":"cursus",       "meanings":["run"],                               "conj":3},
    {"present":"dico",       "infinitive":"dicere",      "perfect":"dixi",         "ppp":"dictus",       "meanings":["say"],                               "conj":3},
    {"present":"discedo",    "infinitive":"discedere",   "perfect":"discessi",     "ppp":None,           "meanings":["depart","leave"],                    "conj":3},
    {"present":"duco",       "infinitive":"ducere",      "perfect":"duxi",         "ppp":"ductus",       "meanings":["lead","take"],                       "conj":3},
    {"present":"effugio",    "infinitive":"effugere",    "perfect":"effugi",       "ppp":None,           "meanings":["escape"],                            "conj":3},
    {"present":"emo",        "infinitive":"emere",       "perfect":"emi",          "ppp":"emptus",       "meanings":["buy"],                               "conj":3},
    {"present":"facio",      "infinitive":"facere",      "perfect":"feci",         "ppp":"factus",       "meanings":["make","do"],                         "conj":3},
    {"present":"frango",     "infinitive":"frangere",    "perfect":"fregi",        "ppp":"fractus",      "meanings":["break"],                             "conj":3},
    {"present":"fugio",      "infinitive":"fugere",      "perfect":"fugi",         "ppp":None,           "meanings":["run away","flee"],                   "conj":3},
    {"present":"gero",       "infinitive":"gerere",      "perfect":"gessi",        "ppp":"gestus",       "meanings":["wear","wage war"],                   "conj":3},
    {"present":"iacio",      "infinitive":"iacere",      "perfect":"ieci",         "ppp":"iactus",       "meanings":["throw"],                             "conj":3},
    {"present":"incendo",    "infinitive":"incendere",   "perfect":"incendi",      "ppp":"incensus",     "meanings":["burn","set on fire"],                "conj":3},
    {"present":"intellego",  "infinitive":"intellegere", "perfect":"intellexi",    "ppp":"intellectus",  "meanings":["understand","realise"],              "conj":3},
    {"present":"lego",       "infinitive":"legere",      "perfect":"legi",         "ppp":"lectus",       "meanings":["read","choose"],                     "conj":3},
    {"present":"mitto",      "infinitive":"mittere",     "perfect":"misi",         "ppp":"missus",       "meanings":["send"],                              "conj":3},
    {"present":"occido",     "infinitive":"occidere",    "perfect":"occidi",       "ppp":"occisus",      "meanings":["kill"],                              "conj":3},
    {"present":"ostendo",    "infinitive":"ostendere",   "perfect":"ostendi",      "ppp":"ostentus",     "meanings":["show"],                              "conj":3},
    {"present":"peto",       "infinitive":"petere",      "perfect":"petivi",       "ppp":"petitus",      "meanings":["seek","attack","beg","ask for","make for"], "conj":3},
    {"present":"pono",       "infinitive":"ponere",      "perfect":"posui",        "ppp":"positus",      "meanings":["put","place","put up"],              "conj":3},
    {"present":"procedo",    "infinitive":"procedere",   "perfect":"processi",     "ppp":None,           "meanings":["advance","proceed"],                 "conj":3},
    {"present":"promitto",   "infinitive":"promittere",  "perfect":"promisi",      "ppp":"promissus",    "meanings":["promise"],                           "conj":3},
    {"present":"puto",       "infinitive":"putare",      "perfect":"putavi",       "ppp":"putatus",      "meanings":["think"],                             "conj":3},
    {"present":"quaero",     "infinitive":"quaerere",    "perfect":"quaesivi",     "ppp":"quaesitus",    "meanings":["search for","look for","ask"],       "conj":3},
    {"present":"rapio",      "infinitive":"rapere",      "perfect":"rapui",        "ppp":"raptus",       "meanings":["seize","grab"],                      "conj":3},
    {"present":"reddo",      "infinitive":"reddere",     "perfect":"reddidi",      "ppp":"redditus",     "meanings":["give back","restore"],               "conj":3},
    {"present":"relinquo",   "infinitive":"relinquere",  "perfect":"reliqui",      "ppp":"relictus",     "meanings":["leave","leave behind"],              "conj":3},
    {"present":"resisto",    "infinitive":"resistere",   "perfect":"restiti",      "ppp":None,           "meanings":["resist"],                            "conj":3},
    {"present":"scribo",     "infinitive":"scribere",    "perfect":"scripsi",      "ppp":"scriptus",     "meanings":["write"],                             "conj":3},
    {"present":"surgo",      "infinitive":"surgere",     "perfect":"surrexi",      "ppp":None,           "meanings":["get up","stand up","rise"],           "conj":3},
    {"present":"trado",      "infinitive":"tradere",     "perfect":"tradidi",      "ppp":"traditus",     "meanings":["hand over"],                         "conj":3},
    {"present":"traho",      "infinitive":"trahere",     "perfect":"traxi",        "ppp":"tractus",      "meanings":["drag","draw","pull"],                "conj":3},
    {"present":"vendo",      "infinitive":"vendere",     "perfect":"vendidi",      "ppp":"venditus",     "meanings":["sell"],                              "conj":3},
    {"present":"vinco",      "infinitive":"vincere",     "perfect":"vici",         "ppp":"victus",       "meanings":["conquer","win"],                     "conj":3},
    {"present":"vivo",       "infinitive":"vivere",      "perfect":"vixi",         "ppp":None,           "meanings":["live","be alive"],                   "conj":3},

    # ─── 4th Conjugation (9 verbs) ────────────────────────────────────────────
    {"present":"advenio",    "infinitive":"advenire",    "perfect":"adveni",      "ppp":None,        "meanings":["arrive"],           "conj":4},
    {"present":"aperio",     "infinitive":"aperire",     "perfect":"aperui",      "ppp":"apertus",   "meanings":["open"],             "conj":4},
    {"present":"audio",      "infinitive":"audire",      "perfect":"audivi",      "ppp":"auditus",   "meanings":["hear","listen to"], "conj":4},
    {"present":"dormio",     "infinitive":"dormire",     "perfect":"dormivi",     "ppp":None,        "meanings":["sleep"],            "conj":4},
    {"present":"invenio",    "infinitive":"invenire",    "perfect":"inveni",      "ppp":"inventus",  "meanings":["find"],             "conj":4},
    {"present":"nescio",     "infinitive":"nescire",     "perfect":"nescivi",     "ppp":None,        "meanings":["not know"],         "conj":4},
    {"present":"scio",       "infinitive":"scire",       "perfect":"scivi",       "ppp":"scitus",    "meanings":["know"],             "conj":4},
    {"present":"sentio",     "infinitive":"sentire",     "perfect":"sensi",       "ppp":"sensus",    "meanings":["feel","notice"],    "conj":4},
    {"present":"venio",      "infinitive":"venire",      "perfect":"veni",        "ppp":None,        "meanings":["come"],             "conj":4},
]

VERBS_CONJ1 = [v for v in VERBS_ALL if v["conj"] == 1]  # 37
VERBS_CONJ2 = [v for v in VERBS_ALL if v["conj"] == 2]  # 19
VERBS_CONJ3 = [v for v in VERBS_ALL if v["conj"] == 3]  # 55
VERBS_CONJ4 = [v for v in VERBS_ALL if v["conj"] == 4]  #  9


# ── Sets ───────────────────────────────────────────────────────────────────────

SETS_N5 = [
    {
        "id": 69, "node": 5, "node_title": NODE5_TITLE,
        "title": "1st Conjugation — Principal Parts",
        "type": "verb_conjugation",
        "sell": "Drill all **36 first-conjugation verbs** from the Eduqas GCSE list. Each question shows all principal parts with one randomly blanked — type the missing part and the English meaning.",
        "pass_mark": 80,
        "content": {"verbs": VERBS_CONJ1},
    },
    {
        "id": 70, "node": 5, "node_title": NODE5_TITLE,
        "title": "2nd Conjugation — Principal Parts",
        "type": "verb_conjugation",
        "sell": "Drill all **19 second-conjugation verbs** from the Eduqas GCSE list. Each question shows all principal parts with one randomly blanked — type the missing part and the English meaning.",
        "pass_mark": 80,
        "content": {"verbs": VERBS_CONJ2},
    },
    {
        "id": 71, "node": 5, "node_title": NODE5_TITLE,
        "title": "3rd Conjugation — Principal Parts",
        "type": "verb_conjugation",
        "sell": "Drill all **48 third-conjugation verbs** from the Eduqas GCSE list. Each question shows all principal parts with one randomly blanked — type the missing part and the English meaning.",
        "pass_mark": 80,
        "content": {"verbs": VERBS_CONJ3},
    },
    {
        "id": 72, "node": 5, "node_title": NODE5_TITLE,
        "title": "4th Conjugation — Principal Parts",
        "type": "verb_conjugation",
        "sell": "Drill all **9 fourth-conjugation verbs** from the Eduqas GCSE list. Each question shows all principal parts with one randomly blanked — type the missing part and the English meaning.",
        "pass_mark": 80,
        "content": {"verbs": VERBS_CONJ4},
    },
    {
        "id": 73, "node": 5, "node_title": NODE5_TITLE,
        "title": "All Verbs — Consolidation",
        "type": "verb_conjugation",
        "badge": "test",
        "sell": "All **112 GCSE verbs** in random order — every conjugation mixed together. For each verb one principal part is randomly blanked. Type it and the English meaning. The ultimate consolidation run.",
        "pass_mark": 80,
        "content": {"verbs": VERBS_ALL},
    },
]

SETS_N5_BY_ID = {s["id"]: s for s in SETS_N5}
