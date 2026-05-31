"""
Latin GCSE Mastery Platform - Content Data, Node 4 (4th Conjugation).
Mirrors the architecture of data_node3.py for Node 4.

Focus: 4th conjugation verbs (audio, dormio, aperio, advenio).
       Plus introduces:
         - new nouns: uxor, maritus, equus, porta, cibus, donum, vultus, annus
         - demonstratives: hic/haec/hoc, ille/illa/illud, eius, eum/eam/eos/eas
         - new conjunctions/adverbs: quamquam, postquam, simulac, ubi, cur,
           quod (because), igitur, mox, iterum, deinde, nunc
         - acc of duration: 'multos annos'
         - cum + abl, a/ab + abl (agent/separation)

Per Eduqas scope (carried forward from Node 3):
  - Perfect-passive only in this node (PPP + est/sunt); pluperfect-passive removed.
  - Ideal English uses "the/a/an" (no "his/her/their") for the canonical entry.
  - Ideal imperfect: "was Xing" (no bare past in english list).
  - Ideal perfect-passive: "was Xed" / "has been Xed" (both fine).
"""

from OFFICIAL_GLOSSES import g as _g
from data import NODE1_VOCAB as _N1_VOCAB
from data_node2 import NODE2_VOCAB as _N2_VOCAB
from data_node3 import NODE3_VOCAB as _N3_VOCAB
from sentence_vocab_scanner import build_tile_vocab as _build_tile_vocab


# ── 4th Conjugation verbs - Top 150 (4 verbs) ────────────────────────────────
# Tuple: (present, infinitive, perfect, ppp_or_None,
#         eng_present, eng_infinitive, eng_perfect, eng_ppp_or_None)
# dormio and advenio have NO PPP at GCSE.
VERBS_4TH_TOP150 = [
    ("audio",   "audire",   "audivi",   "auditus",   "I hear",   "to hear",   "I heard",   "having been heard"),
    ("dormio",  "dormire",  "dormivi",  None,        "I sleep",  "to sleep",  "I slept",   None),
    ("aperio",  "aperire",  "aperui",   "apertus",   "I open",   "to open",   "I opened",  "having been opened"),
    ("advenio", "advenire", "adveni",   None,        "I arrive", "to arrive", "I arrived", None),
]


# ── Node 4 Sentence Vocabulary - new lemmas introduced in this node ──────────
NODE4_VOCAB = [
    # New nouns (3rd & 2nd & 4th declension)
    {"id":"uxor",    "latin":"uxor",    "english":["wife"],    "pos":"noun",
     "derivatives":[
         {"word":"uxorial",   "meaning":"relating to a wife or wifely behaviour"},
         {"word":"uxorious",  "meaning":"excessively fond of or submissive to one's wife"},
     ]},
    {"id":"maritus", "latin":"maritus", "english":["husband"], "pos":"noun",
     "derivatives":[
         {"word":"marital",  "meaning":"relating to marriage"},
         {"word":"marry",    "meaning":"to take as a husband or wife"},
         {"word":"marriage", "meaning":"the legal union of two people"},
     ]},
    {"id":"equus",   "latin":"equus",   "english":["horse"],   "pos":"noun",
     "derivatives":[
         {"word":"equine",      "meaning":"relating to horses"},
         {"word":"equestrian",  "meaning":"a horse rider, or relating to horse riding"},
     ]},
    {"id":"porta",   "latin":"porta",   "english":["gate"],    "pos":"noun",
     "derivatives":[
         {"word":"portal",   "meaning":"a doorway, gate, or entrance — especially a grand one"},
         {"word":"port",     "meaning":"a harbour where ships dock — originally a gateway in/out"},
         {"word":"porter",   "meaning":"a doorkeeper or someone who carries luggage through entrances"},
     ]},
    {"id":"cibus",   "latin":"cibus",   "english":["food"],    "pos":"noun",
     "derivatives":[
         {"word":"cibarious", "meaning":"relating to food (rare/literary)"},
     ]},
    {"id":"donum",   "latin":"donum",   "english":["gift"],    "pos":"noun",
     "derivatives":[
         {"word":"donate",    "meaning":"to give as a gift, especially to charity"},
         {"word":"donation",  "meaning":"a gift, often of money, given to a cause"},
         {"word":"donor",     "meaning":"a person who gives or donates something"},
     ]},
    {"id":"vultus",  "latin":"vultus",  "english":["face","expression"], "pos":"noun",
     "derivatives":[]},
    {"id":"annus",   "latin":"annus",   "english":["year"],    "pos":"noun",
     "derivatives":[
         {"word":"annual",    "meaning":"happening once a year"},
         {"word":"anniversary","meaning":"the date marking a year (or years) since an event"},
         {"word":"annals",    "meaning":"a yearly historical record"},
     ]},

    # Demonstrative pronouns/adjectives — the big new pronoun families for Node 4
    {"id":"hic",     "latin":"hic, haec, hoc", "english":["this"],   "pos":"pronoun",
     "display_label":"hic / haec / hoc",
     "derivatives":[]},
    {"id":"ille",    "latin":"ille, illa, illud", "english":["that"], "pos":"pronoun",
     "display_label":"ille / illa / illud",
     "derivatives":[]},
    {"id":"is",      "latin":"is, ea, id", "english":["he","she","it","they"], "pos":"pronoun",
     "display_label":"is / ea / id",
     "note":"Forms used in Node 4 sentences: eius (his/her), eum/eam (him/her), eos/eas (them).",
     "derivatives":[]},

    # Adjectives
    {"id":"unus",    "latin":"unus",    "english":["one","a single"], "pos":"adjective",
     "derivatives":[
         {"word":"unite",    "meaning":"to bring together as one"},
         {"word":"union",    "meaning":"the act of joining together as one"},
         {"word":"unique",   "meaning":"being the only one of its kind"},
     ]},
    {"id":"pauci",   "latin":"pauci",   "english":["few","a few"], "pos":"adjective",
     "derivatives":[
         {"word":"paucity",  "meaning":"a small amount; scarcity"},
     ]},
    {"id":"ceteri",  "latin":"ceteri",  "english":["the rest","the other","the remaining"], "pos":"adjective",
     "derivatives":[
         {"word":"et cetera (etc.)", "meaning":"'and the rest' — used to indicate further items"},
     ]},
    {"id":"omnis",   "latin":"omnis",   "english":["all","every"], "pos":"adjective",
     "derivatives":[
         {"word":"omnipotent",  "meaning":"all-powerful"},
         {"word":"omnipresent", "meaning":"present everywhere at once"},
         {"word":"omniscient",  "meaning":"all-knowing"},
     ]},
    {"id":"perterritus", "latin":"perterritus", "english":["terrified","very frightened"], "pos":"adjective",
     "derivatives":[
         {"word":"terror",    "meaning":"extreme fear"},
         {"word":"terrify",   "meaning":"to fill with great fear"},
     ]},

    # Adverbs
    {"id":"iam",      "latin":"iam",      "english":["now","already"],     "pos":"adverb", "derivatives":[]},
    {"id":"mox",      "latin":"mox",      "english":["soon"],              "pos":"adverb", "derivatives":[]},
    {"id":"iterum",   "latin":"iterum",   "english":["again"],             "pos":"adverb",
     "derivatives":[{"word":"iterate", "meaning":"to do something again, or repeat a process"}]},
    {"id":"nunc",     "latin":"nunc",     "english":["now"],               "pos":"adverb", "derivatives":[]},
    {"id":"deinde",   "latin":"deinde",   "english":["then","next"],       "pos":"adverb", "derivatives":[]},
    {"id":"statim",   "latin":"statim",   "english":["immediately","at once","straight away"], "pos":"adverb",
     "derivatives":[{"word":"static", "meaning":"not moving — staying in one place"}]},
    {"id":"prope",    "latin":"prope",    "english":["near","close to"],   "pos":"preposition",
     "note":"prope + accusative",
     "derivatives":[
         {"word":"approach",   "meaning":"to come near"},
         {"word":"propinquity","meaning":"the state of being near in time, space or relationship"},
     ]},

    # Conjunctions
    {"id":"quamquam", "latin":"quamquam", "english":["although"],          "pos":"conjunction", "derivatives":[]},
    {"id":"postquam", "latin":"postquam", "english":["after"],             "pos":"conjunction",
     "note":"postquam + perfect tense in Latin = 'after X-ed' in English.",
     "derivatives":[]},
    {"id":"simulac",  "latin":"simulac",  "english":["as soon as"],        "pos":"conjunction", "derivatives":[]},
    {"id":"ubi_when", "latin":"ubi",      "english":["when","where"],      "pos":"conjunction",
     "derivatives":[]},
    {"id":"cur",      "latin":"cur",      "english":["why"],               "pos":"adverb",
     "derivatives":[]},
    {"id":"quod_because","latin":"quod",  "english":["because"],           "pos":"conjunction",
     "derivatives":[]},
    {"id":"igitur",   "latin":"igitur",   "english":["therefore","and so"], "pos":"conjunction",
     "note":"postpositive — usually 2nd word in its clause.",
     "derivatives":[]},
]


# ── Conjugation generators for 4th-conjugation verbs ──────────────────────────
# 4th conj forms: stem (audi-) + endings:
#   present:    -o, -s, -t, -mus, -tis, -unt        (NB 1pl/2pl/3pl spell as audi+mus, audi+tis, audi+unt)
#   imperfect:  -ebam, -ebas, -ebat, -ebamus, -ebatis, -ebant   (added to stem incl. final -i, so 'audiebam')
#   future:     -am, -es, -et, -emus, -etis, -ent             (gives 'audiam, audies, audiet')
# (essentially the same surface forms as the 3rd-io subset.)

def _make_3sg_part(phrase):
    """Apply English 3rd-sg rule to a verb phrase, preserving any trailing text."""
    import re as _re
    m = _re.match(r'^(\S+)(.*)', phrase.strip())
    if not m:
        return phrase + "s"
    verb, tail = m.group(1), m.group(2)
    irreg = {"have":"has", "do":"does", "go":"goes", "be":"is", "say":"says"}
    if verb in irreg:
        return irreg[verb] + tail
    elif verb.endswith(("s","x","ch","sh","z","o")):
        return verb + "es" + tail
    elif verb.endswith("y") and len(verb) >= 2 and verb[-2] not in "aeiou":
        return verb[:-1] + "ies" + tail
    else:
        return verb + "s" + tail

def _opts_present(eng_present):
    base = eng_present[2:]  # strip "I "
    third = _make_3sg_part(base)
    return [f"I {base}", f"you (sg) {base}", f"he/she {third}",
            f"we {base}", f"you (pl) {base}", f"they {base}"]

def _make_gerund(verb_word):
    """Cheap progressive gerund: 'sleep' -> 'sleeping', 'open' -> 'opening', 'arrive' -> 'arriving'."""
    if verb_word.endswith("e") and not verb_word.endswith("ee"):
        stem = verb_word[:-1]
    elif (len(verb_word) >= 3 and verb_word[-1] not in "aeiouwxy"
          and verb_word[-2] in "aeiou" and verb_word[-3] not in "aeiou"):
        stem = verb_word + verb_word[-1]
    else:
        stem = verb_word
    return stem + "ing"

def _opts_imperf(eng_present):
    base = eng_present[2:]
    parts = [p.strip() for p in base.split(",")][:2]
    ger = " / ".join(_make_gerund(p) for p in parts)
    return [f"I was {ger}", f"you (sg) were {ger}", f"he/she was {ger}",
            f"we were {ger}", f"you (pl) were {ger}", f"they were {ger}"]

def _opts_future(eng_present):
    base = eng_present[2:]
    return [f"I will {base}", f"you (sg) will {base}", f"he/she will {base}",
            f"we will {base}", f"you (pl) will {base}", f"they will {base}"]

def _opts_perfect(eng_perfect):
    base = eng_perfect[2:]
    return [f"I {base}", f"you (sg) {base}", f"he/she {base}",
            f"we {base}", f"you (pl) {base}", f"they {base}"]

def _opts_pluperf(eng_perfect):
    PAST_PARTICIPLE = {
        "heard":"heard", "slept":"slept", "opened":"opened", "arrived":"arrived",
    }
    base = eng_perfect[2:]
    pp = PAST_PARTICIPLE.get(base, base)
    return [f"I had {pp}", f"you (sg) had {pp}", f"he/she had {pp}",
            f"we had {pp}", f"you (pl) had {pp}", f"they had {pp}"]


def _stem4(verb):
    """Strip final -o from the 1sg present to get the 4th-conj stem (audi-, dormi-, ...)."""
    return verb[0][:-1]  # 'audio' -> 'audi'


def _gen_present(verb):
    s = _stem4(verb); eng = verb[4]
    forms = [s+"o", s+"s", s+"t", s+"mus", s+"tis", s+"unt"]
    eng_set = _opts_present(eng)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]

def _gen_imperfect(verb):
    s = _stem4(verb); eng = verb[4]
    # Stem already ends in -i; append -ebam etc.
    forms = [s+"ebam", s+"ebas", s+"ebat", s+"ebamus", s+"ebatis", s+"ebant"]
    eng_set = _opts_imperf(eng)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]

def _gen_future(verb):
    s = _stem4(verb); eng = verb[4]
    # 4th-conj future = stem + -am/-es/-et/-emus/-etis/-ent
    forms = [s+"am", s+"es", s+"et", s+"emus", s+"etis", s+"ent"]
    eng_set = _opts_future(eng)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]

def _gen_perfect(verb):
    perf = verb[2]; eng_perf = verb[6]
    p = perf[:-1]  # drop final -i
    forms = [perf, p+"isti", p+"it", p+"imus", p+"istis", p+"erunt"]
    eng_set = _opts_perfect(eng_perf)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]

def _gen_pluperf(verb):
    perf = verb[2]; eng_perf = verb[6]
    p = perf[:-1]
    forms = [p+"eram", p+"eras", p+"erat", p+"eramus", p+"eratis", p+"erant"]
    eng_set = _opts_pluperf(eng_perf)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]


QUESTIONS_PRESENT_N4    = [q for v in VERBS_4TH_TOP150 for q in _gen_present(v)]
QUESTIONS_IMPERFECT_N4  = [q for v in VERBS_4TH_TOP150 for q in _gen_imperfect(v)]
QUESTIONS_FUTURE_N4     = [q for v in VERBS_4TH_TOP150 for q in _gen_future(v)]
QUESTIONS_PERFECT_N4    = [q for v in VERBS_4TH_TOP150 for q in _gen_perfect(v)]
QUESTIONS_PLUPERFECT_N4 = [q for v in VERBS_4TH_TOP150 for q in _gen_pluperf(v)]


# ── Conjugation tables (translate_form intro screens) ─────────────────────────
# Lead with 'audio' (most regular 4th-conj exemplar).

TABLE_PRESENT_4TH = [
    {"conjugation":"I",            "infinitive_ending":"-o",  "example":"audio",     "ep":[["aud",""],["i","coral"],["o","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-s",  "example":"audis",     "ep":[["aud",""],["i","coral"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-t",  "example":"audit",     "ep":[["aud",""],["i","coral"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-mus","example":"audimus",   "ep":[["aud",""],["i","coral"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-tis","example":"auditis",   "ep":[["aud",""],["i","coral"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-unt","example":"audiunt",   "ep":[["aud",""],["i","coral"],["unt","blue"]]},
]

TABLE_IMPERFECT_4TH = [
    {"conjugation":"I",            "infinitive_ending":"-ebam",  "example":"audiebam",  "tr":"I was hearing",      "ep":[["aud",""],["i","coral"],["eba","purple"],["m","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-ebas",  "example":"audiebas",  "tr":"you were hearing",   "ep":[["aud",""],["i","coral"],["eba","purple"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-ebat",  "example":"audiebat",  "tr":"he/she was hearing", "ep":[["aud",""],["i","coral"],["eba","purple"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-ebamus","example":"audiebamus","tr":"we were hearing",    "ep":[["aud",""],["i","coral"],["eba","purple"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-ebatis","example":"audiebatis","tr":"you were hearing",   "ep":[["aud",""],["i","coral"],["eba","purple"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-ebant", "example":"audiebant", "tr":"they were hearing",  "ep":[["aud",""],["i","coral"],["eba","purple"],["nt","blue"]]},
]

# 4th-conj future: stem + -am/-es/-et/-emus/-etis/-ent (NOT -bo/-bi/-bu — same as 3rd)
TABLE_FUTURE_4TH = [
    {"conjugation":"I",            "infinitive_ending":"-am",   "example":"audiam",    "tr":"I will hear",      "ep":[["aud",""],["i","coral"],["a","purple"],["m","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-es",   "example":"audies",    "tr":"you will hear",    "ep":[["aud",""],["i","coral"],["e","purple"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-et",   "example":"audiet",    "tr":"he/she will hear", "ep":[["aud",""],["i","coral"],["e","purple"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-emus", "example":"audiemus",  "tr":"we will hear",     "ep":[["aud",""],["i","coral"],["e","purple"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-etis", "example":"audietis",  "tr":"you will hear",    "ep":[["aud",""],["i","coral"],["e","purple"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-ent",  "example":"audient",   "tr":"they will hear",   "ep":[["aud",""],["i","coral"],["e","purple"],["nt","blue"]]},
]

# Perfect: lead with audivi (-v- marker).
TABLE_PERFECT_4TH = [
    {"conjugation":"I",            "infinitive_ending":"-i",     "example":"audivi",     "tr":"I heard",         "ep":[["audi",""],["v","purple"],["i","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-isti",  "example":"audivisti",  "tr":"you heard",       "ep":[["audi",""],["v","purple"],["isti","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-it",    "example":"audivit",    "tr":"he/she heard",    "ep":[["audi",""],["v","purple"],["it","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-imus",  "example":"audivimus",  "tr":"we heard",        "ep":[["audi",""],["v","purple"],["imus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-istis", "example":"audivistis", "tr":"you heard",       "ep":[["audi",""],["v","purple"],["istis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-erunt", "example":"audiverunt", "tr":"they heard",      "ep":[["audi",""],["v","purple"],["erunt","blue"]]},
]

TABLE_PLUPERFECT_4TH = [
    {"conjugation":"I",            "infinitive_ending":"-eram",  "example":"audiveram",  "tr":"I had heard",      "ep":[["audi",""],["v","purple"],["era","pink"],["m","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-eras",  "example":"audiveras",  "tr":"you had heard",    "ep":[["audi",""],["v","purple"],["era","pink"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-erat",  "example":"audiverat",  "tr":"he/she had heard", "ep":[["audi",""],["v","purple"],["era","pink"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-eramus","example":"audiveramus","tr":"we had heard",     "ep":[["audi",""],["v","purple"],["era","pink"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-eratis","example":"audiveratis","tr":"you had heard",    "ep":[["audi",""],["v","purple"],["era","pink"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-erant", "example":"audiverant", "tr":"they had heard",   "ep":[["audi",""],["v","purple"],["era","pink"],["nt","blue"]]},
]


# ── Parse-and-translate questions for the Review set ─────────────────────────
PARSE_TRANSLATE_QUESTIONS_N4 = [
    {"form":"audis",       "tense":"present",    "person":"2nd","number":"singular","translation":"you (sg) hear"},
    {"form":"dormiunt",    "tense":"present",    "person":"3rd","number":"plural",  "translation":"they sleep"},
    {"form":"aperit",      "tense":"present",    "person":"3rd","number":"singular","translation":"he/she opens"},
    {"form":"adveniebat",  "tense":"imperfect",  "person":"3rd","number":"singular","translation":"he/she was arriving"},
    {"form":"audiebant",   "tense":"imperfect",  "person":"3rd","number":"plural",  "translation":"they were hearing"},
    {"form":"dormiebam",   "tense":"imperfect",  "person":"1st","number":"singular","translation":"I was sleeping"},
    {"form":"audient",     "tense":"future",     "person":"3rd","number":"plural",  "translation":"they will hear"},
    {"form":"aperiet",     "tense":"future",     "person":"3rd","number":"singular","translation":"he/she will open"},
    {"form":"dormies",     "tense":"future",     "person":"2nd","number":"singular","translation":"you (sg) will sleep"},
    {"form":"audivit",     "tense":"perfect",    "person":"3rd","number":"singular","translation":"he/she heard"},
    {"form":"adveni",      "tense":"perfect",    "person":"1st","number":"singular","translation":"I arrived"},
    {"form":"aperuerunt",  "tense":"perfect",    "person":"3rd","number":"plural",  "translation":"they opened"},
    {"form":"audiverat",   "tense":"pluperfect", "person":"3rd","number":"singular","translation":"he/she had heard"},
    {"form":"dormiveramus","tense":"pluperfect", "person":"1st","number":"plural",  "translation":"we had slept"},
    {"form":"adveneras",   "tense":"pluperfect", "person":"2nd","number":"singular","translation":"you (sg) had arrived"},
]


# Sentence sets — populated from contextstuff/trans_node4.json.
# Each sentence: canonical translation + 4-8 acceptable variants + explanation
# in the new full-breakdown format (matches Node 1 Set 20 style).

SENTENCES_PRESENT_TEST_N4 = [
    {
        "latin": "uxor in urbe dormit.",
        "english": [
            "The wife is sleeping in the city.",
            "The wife sleeps in the city.",
            "A wife is sleeping in the city.",
            "The wife is asleep in the city.",
            "The wife sleeps inside the city.",
        ],
        "explanation": (
            "• uxor (the wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• dorm{R:i}{B:t} (is sleeping / sleeps)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* (sleep) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• in urbe (in the city)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *urb{T:e}* (city) is a noun, 3rd declension feminine singular {T:ablative}"
        ),
    },
    {
        "latin": "maritus portam aperit.",
        "english": [
            "The husband opens the gate.",
            "The husband is opening the gate.",
            "A husband opens the gate.",
            "The husband opens the door.",
            "The husband is opening the door.",
        ],
        "explanation": (
            "• maritus (the husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• aper{R:i}{B:t} (opens)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aper-* (open) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "unus equus prope portam dormit.",
        "english": [
            "One horse is sleeping near the gate.",
            "One horse sleeps near the gate.",
            "A single horse is sleeping near the gate.",
            "One lone horse sleeps close to the gate.",
            "A single horse sleeps near the gate.",
            "One horse is asleep near the gate.",
        ],
        "explanation": (
            "• unus equus (one horse)\n"
            "  → *equus* (horse) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *unus* (one / a single) is an adjective agreeing with *equus* as both are masculine singular {T:nominative}\n"
            "• dorm{R:i}{B:t} (is sleeping / sleeps)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* (sleep) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• prope portam (near the gate)\n"
            "  → *prope + accusative* = 'near' / 'close to'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}"
        ),
    },
    {
        "latin": "regina ad portam advenit, et vultus suus laetus est.",
        "english": [
            "The queen arrives at the gate, and her face is happy.",
            "The queen comes to the gate, and her face is happy.",
            "The queen arrives at the gate, and her expression is happy.",
            "A queen arrives at the gate, and her face is glad.",
            "The queen arrives at the gate, and her face is joyful.",
            "The queen reaches the gate, and her face is happy.",
            "The queen arrives at the gate, and her own face is happy.",
            "The queen comes to the gate, and her own expression is happy.",
        ],
        "explanation": (
            "• regina (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• adven{R:i}{B:t} (arrives)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven-* (arrive) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• ad portam (to the gate)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• vultus suus (her face)\n"
            "  → *vultus* (face / expression) is a noun, 4th declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *suus* (his/her own) is the reflexive possessive adjective, masculine singular {T:nominative} agreeing with *vultus* — it refers back to the subject (*regina*)\n"
            "• laetus est (is happy)\n"
            "  → *laetus* (happy) is an adjective, masculine singular {T:nominative} agreeing with *vultus*\n"
            "  → *est* (is) is the present 3sg of *sum* (to be) — links subject to predicate adjective"
        ),
    },
    {
        "latin": "tristis puella portam aperit, et patrem audit.",
        "english": [
            "The sad girl opens the gate, and hears her father.",
            "The unhappy girl opens the gate, and hears her father.",
            "The sad girl opens the gate, and hears the father.",
            "The sorrowful girl opens the gate, and hears her father.",
            "The sad girl opens the gate, and can hear her father.",
            "The sad girl is opening the gate, and is hearing her father.",
        ],
        "explanation": (
            "• tristis puella (the sad girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *tristis* (sad) is an adjective agreeing with *puella* as both are feminine singular {T:nominative}\n"
            "• aper{R:i}{B:t} (opens)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aper-* (open) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• aud{R:i}{B:t} (hears)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aud-* (hear) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• patrem (her father)\n"
            "  → *patr{T:em}* (father) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "hic iuvenis verba regis audit, et portam statim aperit.",
        "english": [
            "This young man hears the words of the king, and immediately opens the gate.",
            "This young man hears the king's words, and opens the gate immediately.",
            "This young man hears the words of the king, and at once opens the gate.",
            "This young man listens to the words of the king, and immediately opens the gate.",
            "This young man hears the king's words, and straight away opens the gate.",
        ],
        "explanation": (
            "• hic iuvenis (this young man)\n"
            "  → *iuvenis* (young man) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *hic* (this) is a demonstrative agreeing with *iuvenis* as both are masculine singular {T:nominative}\n"
            "• aud{R:i}{B:t} (hears)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aud-* (hear) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• verba regis (the words of the king)\n"
            "  → *verb{T:a}* (words) is a noun, 2nd declension neuter plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → *reg{T:is}* (of the king) is a noun, 3rd declension masculine singular {T:genitive} — 'of...' / 'the king's'\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• aper{R:i}{B:t} (opens)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aper-* (open) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position"
        ),
    },
    {
        "latin": "ceteri milites adveniunt, sed pauci mariti portam aperiunt.",
        "english": [
            "The rest of the soldiers arrive, but few husbands open the gate.",
            "The other soldiers arrive, but few husbands open the gate.",
            "The remaining soldiers arrive, but a few husbands open the gate.",
            "The rest of the soldiers are arriving, but few husbands are opening the gate.",
            "The other soldiers arrive, but few of the husbands open the gate.",
        ],
        "explanation": (
            "• ceteri milites (the rest of the soldiers)\n"
            "  → *milit{T:es}* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *ceteri* (the rest / the other) is an adjective agreeing with *milites* as both are masculine plural {T:nominative}\n"
            "• adven{R:i}{B:unt} (arrive)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven-* (arrive) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:unt}* shows it is the they form\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• pauci mariti (few husbands)\n"
            "  → *marit{T:i}* (husbands) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pauci* (few / a few) is an adjective agreeing with *mariti* as both are masculine plural {T:nominative}\n"
            "• aper{R:i}{B:unt} (open)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aper-* (open) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:unt}* shows it is the they form\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "multi equi ad portam adveniunt; regina eos iam audit.",
        "english": [
            "Many horses arrive at the gate; the queen now hears them.",
            "Many horses arrive at the gate; the queen already hears them.",
            "Many horses come to the gate; the queen now hears them.",
            "Many horses are arriving at the gate; the queen now hears them.",
            "Many horses reach the gate; the queen already hears them.",
            "Many horses arrive at the gate; the queen hears them now.",
        ],
        "explanation": (
            "• multi equi (many horses)\n"
            "  → *equ{T:i}* (horses) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *multi* (many) is an adjective agreeing with *equi* as both are masculine plural {T:nominative}\n"
            "• adven{R:i}{B:unt} (arrive)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven-* (arrive) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:unt}* shows it is the they form\n"
            "• ad portam (to the gate)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• regina (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• iam (now)\n"
            "  → *iam* (now / already) is an adverb — flexible position\n"
            "• aud{R:i}{B:t} (hears)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aud-* (hear) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• eos (them)\n"
            "  → *eos* is the masculine plural {T:accusative} of *is/ea/id* — 'them' (referring back to *equi*)\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "haec uxor iam dormit, sed hic maritus portam aperit.",
        "english": [
            "This wife is now sleeping, but this husband opens the gate.",
            "This wife now sleeps, but this husband opens the gate.",
            "This wife is already sleeping, but this husband is opening the gate.",
            "This wife is now asleep, but this husband opens the gate.",
            "This wife is sleeping now, but this husband opens the gate.",
            "This wife is already sleeping, but this husband is opening the gate.",
        ],
        "explanation": (
            "• haec uxor (this wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *haec* (this) is a demonstrative agreeing with *uxor* as both are feminine singular {T:nominative}\n"
            "• iam (now)\n"
            "  → *iam* (now / already) is an adverb — flexible position\n"
            "• dorm{R:i}{B:t} (is sleeping)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* (sleep) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• hic maritus (this husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *hic* (this) is a demonstrative agreeing with *maritus* as both are masculine singular {T:nominative}\n"
            "• aper{R:i}{B:t} (opens)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aper-* (open) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "quamquam uxor tristis est, maritus advenit.",
        "english": [
            "Although the wife is sad, the husband arrives.",
            "Although the wife is unhappy, the husband arrives.",
            "Even though the wife is sad, the husband arrives.",
            "Although the wife is sorrowful, the husband arrives.",
            "Although a wife is sad, the husband arrives.",
            "Although the wife is sad, the husband is arriving.",
        ],
        "explanation": (
            "• quamquam (although)\n"
            "  → *quamquam* (although) is a conjunction — introduces a concessive clause\n"
            "• uxor (the wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• tristis est (is sad)\n"
            "  → *tristis* (sad) is an adjective agreeing with *uxor* as both are feminine singular {T:nominative}\n"
            "  → *est* (is) is the present 3sg of *sum* — links subject to the predicate adjective\n"
            "• maritus (the husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• adven{R:i}{B:t} (arrives)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven-* (arrive) is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
]

SENTENCES_PRESENT_SYSTEM_N4 = [
    {
        "latin": "uxor in urbe dormiebat.",
        "english": [
            "The wife was sleeping in the city.",
            "The wife used to sleep in the city.",
            "The wife kept sleeping in the city.",
            "A wife was sleeping in the city.",
            "The wife was asleep in the city.",
        ],
        "explanation": (
            "• uxor (the wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• dorm{R:i}{P:eba}{B:t} (was sleeping)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was sleeping' or 'used to sleep'\n"
            "• in urbe (in the city)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *urb{T:e}* (city) is a noun, 3rd declension feminine singular {T:ablative}"
        ),
    },
    {
        "latin": "hic maritus ad portam iterum adveniet.",
        "english": [
            "This husband will arrive at the gate again.",
            "This husband will come to the gate again.",
            "This husband will arrive at the gate once more.",
            "Again, this husband will arrive at the gate.",
            "This husband will reach the gate again.",
        ],
        "explanation": (
            "• hic maritus (this husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *hic* (this) is a demonstrative agreeing with *maritus* as both are masculine singular {T:nominative}\n"
            "• adven{R:i}{P:e}{B:t} (will arrive)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:e}-* marks the future — 4th conjugation uses *-iam/-ies/-iet* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• ad portam (to the gate)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• iterum (again)\n"
            "  → *iterum* (again) is an adverb — flexible position"
        ),
    },
    {
        "latin": "unus equus prope portam audiebat, et statim advenit.",
        "english": [
            "One horse was listening near the gate, and immediately arrived.",
            "One horse was hearing near the gate, and immediately arrived.",
            "A single horse was listening near the gate, and at once arrived.",
            "One horse was listening near the gate, and straight away arrived.",
            "One lone horse kept listening near the gate, and immediately arrived.",
            "One horse was listening near the gate, and immediately arrives.",
            "One horse was hearing near the gate, and immediately arrives.",
            "One horse was listening near the gate, and at once arrives.",
            "One horse used to listen near the gate, and immediately arrived.",
            "One horse used to listen near the gate, and immediately arrives.",
        ],
        "explanation": (
            "• unus equus (one horse)\n"
            "  → *equus* (horse) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *unus* (one / a single) is an adjective agreeing with *equus* as both are masculine singular {T:nominative}\n"
            "• aud{R:i}{P:eba}{B:t} (was listening)\n"
            "  → *audio* (I hear / listen) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aud-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was listening' or 'used to listen'\n"
            "• prope portam (near the gate)\n"
            "  → *prope + accusative* = 'near' / 'close to'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• adven{R:i}{B:t} (arrives / arrived)\n"
            "  → *advenio* is the dictionary form, 4th conjugation — *adven{R:i}{B:t}* (present) and *adven{B:it}* (perfect) are identical forms\n"
        ),
    },
    {
        "latin": "regina ad portam adveniet; maritus eam mox audiet.",
        "english": [
            "The queen will arrive at the gate; the husband will soon hear her.",
            "The queen will come to the gate; the husband will soon hear her.",
            "The queen will arrive at the gate; the husband will soon listen to her.",
            "A queen will arrive at the gate; the husband will soon hear her.",
            "The queen will arrive at the gate; her husband will soon hear her.",
        ],
        "explanation": (
            "• regina (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• adven{R:i}{P:e}{B:t} (will arrive)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:e}-* marks the future — 4th conjugation uses *-iam/-ies/-iet* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• ad portam (to the gate)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• maritus (the husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• mox (soon)\n"
            "  → *mox* (soon) is an adverb — flexible position\n"
            "• aud{R:i}{P:e}{B:t} (will hear)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aud-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:e}-* marks the future — 4th conjugation uses *-iam/-ies/-iet* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• eam (her)\n"
            "  → *eam* is the feminine singular {T:accusative} of *is/ea/id* — 'her'\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "tristis puella portam aperiebat, et tum patrem audiebat.",
        "english": [
            "The sad girl was opening the gate, and then was hearing her father.",
            "The sad girl was opening the gate, and then she was hearing her father.",
            "The unhappy girl was opening the gate, and then could hear her father.",
            "The sad girl used to open the gate, and then used to hear her father.",
            "The sad girl kept opening the gate, and then kept hearing her father.",
            "The sad girl was opening the gate, and then heard her father.",
            "The sad girl was opening the gate, and then kept hearing her father.",
            "The sad girl was opening the gate, and she then heard her father.",
        ],
        "explanation": (
            "• tristis puella (the sad girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *tristis* (sad) is an adjective agreeing with *puella* as both are feminine singular {T:nominative}\n"
            "• aper{R:i}{P:eba}{B:t} (was opening)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aper-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was opening' or 'used to open'\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• tum (then)\n"
            "  → *tum* (then / at that time) is an adverb — flexible position\n"
            "• aud{R:i}{P:eba}{B:t} (was hearing)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aud-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was hearing' or 'used to hear'\n"
            "• patrem (her father)\n"
            "  → *patr{T:em}* (father) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "haec puella verba regis audit, et portam mox aperiet.",
        "english": [
            "This girl hears the words of the king, and will soon open the gate.",
            "This girl hears the king's words, and will soon open the gate.",
            "This girl hears the words of the king, and soon will open the gate.",
            "This girl listens to the words of the king, and will soon open the gate.",
            "This girl hears the king's words, and will open the gate soon.",
        ],
        "explanation": (
            "• haec puella (this girl)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *haec* (this) is a demonstrative agreeing with *puella* as both are feminine singular {T:nominative}\n"
            "• aud{R:i}{B:t} (hears)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aud-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• verba regis (the words of the king)\n"
            "  → *verb{T:a}* (words) is a noun, 2nd declension neuter plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → *reg{T:is}* (of the king) is a noun, 3rd declension masculine singular {T:genitive} — 'of...' / 'the king's'\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• mox (soon)\n"
            "  → *mox* (soon) is an adverb — flexible position\n"
            "• aper{R:i}{P:e}{B:t} (will open)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aper-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:e}-* marks the future — 4th conjugation uses *-iam/-ies/-iet* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "ceteri milites ad portam advenient, sed pauci mariti iam dormient.",
        "english": [
            "The rest of the soldiers will arrive at the gate, but few husbands will be sleeping.",
            "The other soldiers will arrive at the gate, but few husbands will already be sleeping.",
            "The remaining soldiers will come to the gate, but a few husbands will be asleep.",
            "The other soldiers will arrive at the gate, but few husbands will still be sleeping.",
            "The rest of the soldiers will reach the gate, but few of the husbands will be sleeping.",
        ],
        "explanation": (
            "• ceteri milites (the rest of the soldiers)\n"
            "  → *milit{T:es}* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *ceteri* (the rest / the other) is an adjective agreeing with *milites* as both are masculine plural {T:nominative}\n"
            "• adven{R:i}{P:e}{B:nt} (will arrive)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:e}-* marks the future — 4th conjugation uses *-iam/-ies/-iet* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• ad portam (to the gate)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• pauci mariti (few husbands)\n"
            "  → *marit{T:i}* (husbands) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pauci* (few / a few) is an adjective agreeing with *mariti* as both are masculine plural {T:nominative}\n"
            "• iam (already / now)\n"
            "  → *iam* (now / already) is an adverb — flexible position\n"
            "• dorm{R:i}{P:e}{B:nt} (will be sleeping)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:e}-* marks the future — 4th conjugation uses *-iam/-ies/-iet* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:nt}* shows it is the they form"
        ),
    },
    {
        "latin": "multos annos rex in urbe dormiebat.",
        "english": [
            "For many years the king was sleeping in the city.",
            "The king was sleeping in the city for many years.",
            "For many years the king used to sleep in the city.",
            "The king kept sleeping in the city for many years.",
            "For many years a king was sleeping in the city.",
            "For many years the king was asleep in the city.",
        ],
        "explanation": (
            "• multos annos (for many years)\n"
            "  → *ann{T:os}* (years) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → this is the **accusative of duration**: 'for X years' (no preposition needed)\n"
            "  → *multos* (many) is an adjective agreeing with *annos* as both are masculine plural {T:accusative}\n"
            "• rex (the king)\n"
            "  → *rex* (king) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• dorm{R:i}{P:eba}{B:t} (was sleeping)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was sleeping' or 'used to sleep'\n"
            "• in urbe (in the city)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *urb{T:e}* (city) is a noun, 3rd declension feminine singular {T:ablative}"
        ),
    },
    {
        "latin": "quamquam uxor tristis erat, maritus mox adveniet et eam audiet.",
        "english": [
            "Although the wife was sad, the husband will soon arrive and will hear her.",
            "Although the wife was unhappy, the husband will soon arrive and hear her.",
            "Even though the wife was sad, the husband will soon come and hear her.",
            "Although the wife was sad, the husband will soon arrive and listen to her.",
            "Although the wife was sorrowful, the husband will soon arrive and will hear her.",
        ],
        "explanation": (
            "• quamquam (although)\n"
            "  → *quamquam* (although) is a conjunction — introduces a concessive clause\n"
            "• uxor (the wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• tristis erat (was sad)\n"
            "  → *tristis* (sad) is an adjective agreeing with *uxor* as both are feminine singular {T:nominative}\n"
            "  → *erat* (was) is the imperfect 3sg of *sum*\n"
            "• maritus (the husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• mox (soon)\n"
            "  → *mox* (soon) is an adverb — flexible position\n"
            "• adven{R:i}{P:e}{B:t} (will arrive)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:e}-* marks the future — 4th conjugation uses *-iam/-ies/-iet* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• aud{R:i}{P:e}{B:t} (will hear)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aud-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:e}-* marks the future — 4th conjugation uses *-iam/-ies/-iet* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• eam (her)\n"
            "  → *eam* is the feminine singular {T:accusative} of *is/ea/id* — 'her'\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "cur hic filius dormiebat? quod pater ad portam iam adveniebat.",
        "english": [
            "Why was this son sleeping? Because the father was already arriving at the gate.",
            "Why was this son sleeping? Because the father was now arriving at the gate.",
            "Why used this son to sleep? Because the father was already coming to the gate.",
            "Why was this son sleeping? Because the father was already approaching the gate.",
            "Why was this son asleep? Because the father was already arriving at the gate.",
            "Why was this son sleeping? Because the father used to come to the gate.",
            "Why was this son sleeping? Because the father used to arrive at the gate.",
        ],
        "explanation": (
            "• cur (why)\n"
            "  → *cur* (why) is an adverb — introduces a question\n"
            "• hic filius (this son)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *hic* (this) is a demonstrative agreeing with *filius* as both are masculine singular {T:nominative}\n"
            "• dorm{R:i}{P:eba}{B:t} (was sleeping)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was sleeping' or 'used to sleep'\n"
            "• quod (because)\n"
            "  → *quod* (because) is a conjunction — gives a reason (NOT a relative pronoun here)\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• adven{R:i}{P:eba}{B:t} (was arriving)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was arriving' or 'used to arrive'\n"
            "• ad portam (to the gate)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• iam (already / now)\n"
            "  → *iam* (now / already) is an adverb — flexible position"
        ),
    },
]


SENTENCES_ACTIVE_N4 = [
    {
        "latin": "uxor tandem dormivit.",
        "english": [
            "The wife finally slept.",
            "The wife at last slept.",
            "The wife eventually slept.",
            "The wife finally went to sleep.",
            "A wife finally slept.",
            "The wife has finally slept.",
        ],
        "explanation": (
            "• uxor (the wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• tandem (finally / at last)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• dormiv{B:it} (slept)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dormiv-* is the perfect stem (from *dormivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'slept'"
        ),
    },
    {
        "latin": "maritus portam aperuerat, et ad reginam advenit.",
        "english": [
            "The husband had opened the gate, and arrived at the queen.",
            "The husband had opened the gate, and came to the queen.",
            "A husband had opened the gate, and arrived at the queen.",
            "The husband had opened the gate, and made his way to the queen.",
            "The husband had opened the gate, and reached the queen.",
            "The husband had opened the gate, and arrives at the queen.",
            "The husband had opened the gate, and comes to the queen.",
        ],
        "explanation": (
            "• maritus (the husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• aperu{M:era}{B:t} (had opened)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aperu-* is the perfect stem (from *aperui*)\n"
            "  → *-{M:era}-* is the pluperfect marker\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the pluperfect describes an action completed before another past event: 'had opened'\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• adven{R:i}{B:t} (arrives / arrived)\n"
            "  → *advenio* is the dictionary form, 4th conjugation — *adven{R:i}{B:t}* (present) and *adven{B:it}* (perfect) are identical forms\n"
            "• ad reginam (to the queen)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *regin{T:am}* (queen) is a noun, 1st declension feminine singular {T:accusative}"
        ),
    },
    {
        "latin": "hic rex eos iam audiverat, et cum paucis militibus advenit.",
        "english": [
            "This king had already heard them, and arrived with a few soldiers.",
            "This king had already listened to them, and came with a few soldiers.",
            "This king had now heard them, and arrived with a few soldiers.",
            "This king had already heard them, and came with a few soldiers.",
            "This king had already heard them, and arrived with few soldiers.",
            "This king had already heard them, and arrives with a few soldiers.",
            "This king had already heard them, and comes with a few soldiers.",
        ],
        "explanation": (
            "• hic rex (this king)\n"
            "  → *rex* (king) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *hic* (this) is a demonstrative agreeing with *rex* as both are masculine singular {T:nominative}\n"
            "• iam (already)\n"
            "  → *iam* (now / already) is an adverb — flexible position\n"
            "• audiv{M:era}{B:t} (had heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{M:era}-* is the pluperfect marker\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the pluperfect describes an action completed before another past event: 'had heard'\n"
            "• eos (them)\n"
            "  → *eos* is the masculine plural {T:accusative} of *is/ea/id* — 'them'\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• adven{R:i}{B:t} (arrives / arrived)\n"
            "  → *advenio* is the dictionary form, 4th conjugation — *adven{R:i}{B:t}* (present) and *adven{B:it}* (perfect) are identical forms\n"
            "• cum paucis militibus (with a few soldiers)\n"
            "  → *cum + ablative* = 'with'\n"
            "  → *milit{T:ibus}* (soldiers) is a noun, 3rd declension masculine plural {T:ablative}\n"
            "  → *paucis* (few) is an adjective agreeing with *militibus* as both are masculine plural {T:ablative}"
        ),
    },
    {
        "latin": "unus equus ad portam advenit, et tristem reginam audivit.",
        "english": [
            "One horse arrived at the gate, and heard the sad queen.",
            "One horse arrived at the gate, and listened to the sad queen.",
            "A single horse arrived at the gate, and heard the sad queen.",
            "One horse arrived at the gate, and heard the unhappy queen.",
            "One lone horse arrived at the gate, and heard the sad queen.",
            "One horse arrives at the gate, and heard the sad queen.",
            "One horse comes to the gate, and heard the sad queen.",
        ],
        "explanation": (
            "• unus equus (one horse)\n"
            "  → *equus* (horse) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *unus* (one / a single) is an adjective agreeing with *equus* as both are masculine singular {T:nominative}\n"
            "• adven{R:i}{B:t} (arrives / arrived)\n"
            "  → *advenio* is the dictionary form, 4th conjugation — *adven{R:i}{B:t}* (present) and *adven{B:it}* (perfect) are identical forms\n"
            "• ad portam (to the gate)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• audiv{B:it} (heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'heard'\n"
            "• tristem reginam (the sad queen)\n"
            "  → *regin{T:am}* (queen) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → *tristem* (sad) is an adjective agreeing with *reginam* as both are feminine singular {T:accusative}"
        ),
    },
    {
        "latin": "multos annos uxor sua sola in silva dormiverat.",
        "english": [
            "For many years his wife had slept alone in the wood.",
            "For many years his own wife had slept alone in the forest.",
            "His wife had slept alone in the wood for many years.",
            "For many years his wife had been sleeping alone in the wood.",
            "For many years his wife had been asleep alone in the wood.",
            "His own wife had slept alone in the forest for many years.",
        ],
        "explanation": (
            "• multos annos (for many years)\n"
            "  → *ann{T:os}* (years) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → this is the **accusative of duration**: 'for X years' (no preposition needed)\n"
            "  → *multos* (many) is an adjective agreeing with *annos* as both are masculine plural {T:accusative}\n"
            "• uxor sua sola (his wife alone)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *sua* (his/her own) is a possessive adjective agreeing with *uxor*\n"
            "  → *sola* (alone) is an adjective agreeing with *uxor*\n"
            "• dormiv{M:era}{B:t} (had slept)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dormiv-* is the perfect stem (from *dormivi*)\n"
            "  → *-{M:era}-* is the pluperfect marker\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the pluperfect describes an action completed before another past event: 'had slept'\n"
            "• in silva (in the wood)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *silv{T:a}* (wood) is a noun, 1st declension feminine singular {T:ablative}"
        ),
    },
    {
        "latin": "regina ad portam tandem advenit, et laeta erat.",
        "english": [
            "The queen finally arrived at the gate, and was happy.",
            "The queen at last arrived at the gate, and was happy.",
            "The queen finally came to the gate, and was glad.",
            "The queen finally reached the gate, and was happy.",
            "The queen finally arrived at the gate, and was joyful.",
            "The queen finally arrives at the gate, and was happy.",
            "The queen at last arrives at the gate, and was happy.",
        ],
        "explanation": (
            "• regina (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• tandem (finally)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• adven{R:i}{B:t} (arrives / arrived)\n"
            "  → *advenio* is the dictionary form, 4th conjugation — *adven{R:i}{B:t}* (present) and *adven{B:it}* (perfect) are identical forms\n"
            "• ad portam (to the gate)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• laeta erat (was happy)\n"
            "  → *laeta* (happy) is an adjective, feminine singular {T:nominative} agreeing with *regina*\n"
            "  → *erat* (was) is the imperfect 3sg of *sum*"
        ),
    },
    {
        "latin": "\"cur,\" inquit maritus, \"in urbe dormiebas?\" uxor nihil audivit.",
        "english": [
            "\"Why,\" said the husband, \"were you sleeping in the city?\" The wife heard nothing.",
            "\"Why,\" said the husband, \"used you to sleep in the city?\" The wife heard nothing.",
            "\"Why,\" said the husband, \"were you sleeping in the city?\" The wife did not hear anything.",
            "\"Why,\" said the husband, \"were you asleep in the city?\" The wife heard nothing.",
            "\"Why,\" said the husband, \"were you sleeping inside the city?\" The wife heard nothing.",
        ],
        "explanation": (
            "• cur (why)\n"
            "  → *cur* (why) is an adverb — introduces a question\n"
            "• inquit (said)\n"
            "  → *inquit* (said) is a defective verb — always splits direct speech, placed after the first word(s)\n"
            "• maritus (the husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• dorm{R:i}{P:eba}{B:s} (were you sleeping)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:s}* shows it is the you (singular) form\n"
            "  → the imperfect describes a continuing or repeated past action: 'were sleeping' or 'used to sleep'\n"
            "• in urbe (in the city)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *urb{T:e}* (city) is a noun, 3rd declension feminine singular {T:ablative}\n"
            "• uxor (the wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• audiv{B:it} (heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'heard'\n"
            "• nihil (nothing)\n"
            "  → *nihil* (nothing) is indeclinable — the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "pauci milites portam aperuerunt, et ceteri advenerunt.",
        "english": [
            "A few soldiers opened the gate, and the rest arrived.",
            "Few soldiers opened the gate, and the others arrived.",
            "A few soldiers opened the gate, and the remaining ones arrived.",
            "A few soldiers opened the gate, and the rest came.",
            "A few soldiers opened the gate, and the others came through.",
        ],
        "explanation": (
            "• pauci milites (a few soldiers)\n"
            "  → *milit{T:es}* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pauci* (few / a few) is an adjective agreeing with *milites* as both are masculine plural {T:nominative}\n"
            "• aperu{B:erunt} (opened)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aperu-* is the perfect stem (from *aperui*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'opened'\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• ceteri (the rest)\n"
            "  → *ceteri* (the rest / the others) is an adjective used substantivally, masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• adven{B:erunt} (arrived)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven{B:erunt}* is the perfect they form\n"
            "  → the perfect tense describes a completed, single past action: 'arrived'"
        ),
    },
    {
        "latin": "maritus uxorem suam audiverat, sed quamquam adveniebat, portam non aperuit.",
        "english": [
            "The husband had heard his own wife, but although he was arriving, he did not open the gate.",
            "The husband had heard his wife, but although he was coming, he did not open the gate.",
            "The husband had listened to his wife, but although he was arriving, he did not open the gate.",
            "The husband had heard his wife, but although he kept arriving, he did not open the gate.",
            "The husband had heard his wife, but although he was approaching, he did not open the gate.",
        ],
        "explanation": (
            "• maritus (the husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• audiv{M:era}{B:t} (had heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{M:era}-* is the pluperfect marker\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the pluperfect describes an action completed before another past event: 'had heard'\n"
            "• uxorem suam (his own wife)\n"
            "  → *uxor{T:em}* (wife) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → *suam* (his/her own) is a possessive adjective agreeing with *uxorem*\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• quamquam (although)\n"
            "  → *quamquam* (although) is a conjunction — introduces a concessive clause\n"
            "• adven{R:i}{P:eba}{B:t} (was arriving)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was arriving' or 'used to arrive'\n"
            "• non aperu{B:it} (did not open)\n"
            "  → *non* (not) negates the verb\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aperu-* is the perfect stem (from *aperui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'did not open'\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "ubi hic maritus advenit, omnes eum audiverunt.",
        "english": [
            "When this husband arrived, everyone heard him.",
            "When this husband arrived, all of them heard him.",
            "When this husband arrived, everybody listened to him.",
            "When this husband arrived, all heard him.",
            "When this husband arrived, everyone could hear him.",
            "When this husband arrives, everyone heard him.",
            "When this husband comes, everyone heard him.",
        ],
        "explanation": (
            "• ubi (when)\n"
            "  → *ubi* (when) is a temporal conjunction (with the indicative — not 'where' here)\n"
            "• hic maritus (this husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *hic* (this) is a demonstrative agreeing with *maritus* as both are masculine singular {T:nominative}\n"
            "• adven{R:i}{B:t} (arrives / arrived)\n"
            "  → *advenio* is the dictionary form, 4th conjugation — *adven{R:i}{B:t}* (present) and *adven{B:it}* (perfect) are identical forms\n"
            "• omnes (everyone)\n"
            "  → *omn{T:es}* (all / everyone) is a noun, 3rd declension masculine plural {T:nominative}, used substantivally\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• audiv{B:erunt} (heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'heard'\n"
            "• eum (him)\n"
            "  → *eum* is the masculine singular {T:accusative} of *is/ea/id* — 'him'\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
]


SENTENCES_PPP_N4 = [
    {
        "latin": "porta aperta est.",
        "english": [
            "The gate was opened.",
            "The gate has been opened.",
            "The gate was thrown open.",
            "A gate was opened.",
            "The gate is open.",
        ],
        "explanation": (
            "• porta (the gate)\n"
            "  → *port{T:a}* (gate) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• aperta est (was opened)\n"
            "  → *apert{T:a}* is the PPP of *aperio*, feminine singular {T:nominative} agreeing with *porta*\n"
            "  → *est* + PPP = **perfect passive**: 'was opened' / 'has been opened'\n"
            "  → note: the PPP can also be read as a predicate adjective — 'the gate is open'"
        ),
    },
    {
        "latin": "verbum auditum est.",
        "english": [
            "The word was heard.",
            "The word has been heard.",
            "A word was heard.",
            "The word was listened to.",
            "The word has been listened to.",
        ],
        "explanation": (
            "• verbum (the word)\n"
            "  → *verb{T:um}* (word) is a noun, 2nd declension neuter singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• auditum est (was heard)\n"
            "  → *audit{T:um}* is the PPP of *audio*, neuter singular {T:nominative} agreeing with *verbum*\n"
            "  → *est* + PPP = **perfect passive**: 'was heard' / 'has been heard'"
        ),
    },
    {
        "latin": "puella audita portam statim aperuit.",
        "english": [
            "The girl, having been heard, immediately opened the gate.",
            "The girl who had been heard immediately opened the gate.",
            "The heard girl immediately opened the gate.",
            "Having been heard, the girl immediately opened the gate.",
            "The girl, once heard, immediately opened the gate.",
        ],
        "explanation": (
            "• puella audita (the girl, having been heard)\n"
            "  → *puell{T:a}* (girl) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *audit{T:a}* is the PPP of *audio*, feminine singular {T:nominative} agreeing with *puella*\n"
            "• aperu{B:it} (opened)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aperu-* is the perfect stem (from *aperui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'opened'\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position"
        ),
    },
    {
        "latin": "donum tandem apertum est, et regina laeta erat.",
        "english": [
            "The gift was finally opened, and the queen was happy.",
            "The gift has finally been opened, and the queen was happy.",
            "The gift was at last opened, and the queen was happy.",
            "The gift was finally opened, and the queen was glad.",
            "The gift was finally opened, and the queen was joyful.",
        ],
        "explanation": (
            "• donum (the gift)\n"
            "  → *don{T:um}* (gift) is a noun, 2nd declension neuter singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• tandem (finally)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• apertum est (was opened)\n"
            "  → *apert{T:um}* is the PPP of *aperio*, neuter singular {T:nominative} agreeing with *donum*\n"
            "  → *est* + PPP = **perfect passive**: 'was opened' / 'has been opened'\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• regina (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• laeta erat (was happy)\n"
            "  → *laeta* (happy) is a predicate adjective, feminine singular {T:nominative} agreeing with *regina*\n"
            "  → *erat* (was) is the imperfect 3sg of *sum*"
        ),
    },
    {
        "latin": "omnes, verba audita, statim advenerunt.",
        "english": [
            "All, the words having been heard, immediately arrived.",
            "Everyone, once the words had been heard, arrived immediately.",
            "All of them, the words having been heard, immediately came.",
            "Once the words had been heard, everyone immediately arrived.",
            "Everyone arrived immediately, the words having been heard.",
        ],
        "explanation": (
            "• omnes (everyone)\n"
            "  → *omn{T:es}* (all / everyone) is a noun, 3rd declension masculine plural {T:nominative}, used substantivally\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• verba audita (the words having been heard)\n"
            "  → *verb{T:a}* (words) is a noun, 2nd declension neuter plural {T:nominative}\n"
            "  → *audit{T:a}* is the PPP of *audio*, neuter plural {T:nominative} agreeing with *verba*\n"
            "  → this PPP phrase sets context — in meaning it functions as an ablative absolute: 'the words having been heard'\n"
            "• adven{B:erunt} (arrived)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven{B:erunt}* is the perfect they form\n"
            "  → the perfect tense describes a completed, single past action: 'arrived'\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position"
        ),
    },
    {
        "latin": "ubi portae apertae sunt, pauci milites advenerunt.",
        "english": [
            "When the gates were opened, a few soldiers arrived.",
            "When the gates had been opened, a few soldiers arrived.",
            "When the gates have been opened, a few soldiers arrived.",
            "Once the gates were opened, a few soldiers arrived.",
            "Once the gates have been opened, a few soldiers arrived.",
            "When the gates were opened, few soldiers arrived.",
            "When the gates were opened, a few soldiers came.",
        ],
        "explanation": (
            "• ubi (when)\n"
            "  → *ubi* (when) is a temporal conjunction — with the perfect = 'when'\n"
            "• portae (the gates)\n"
            "  → *port{T:ae}* (gates) is a noun, 1st declension feminine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• apertae sunt (were opened)\n"
            "  → *apert{T:ae}* is the PPP of *aperio*, feminine plural {T:nominative} agreeing with *portae*\n"
            "  → *sunt* + PPP = **perfect passive**: 'were opened' / 'have been opened'\n"
            "• pauci milites (a few soldiers)\n"
            "  → *milit{T:es}* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pauci* (few / a few) is an adjective agreeing with *milites* as both are masculine plural {T:nominative}\n"
            "• adven{B:erunt} (arrived)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven{B:erunt}* is the perfect they form\n"
            "  → the perfect tense describes a completed, single past action: 'arrived'"
        ),
    },
    {
        "latin": "porta tandem aperta est, et maritus laetus erat.",
        "english": [
            "The gate was finally opened, and the husband was happy.",
            "The gate has finally been opened, and the husband was happy.",
            "The gate was at last opened, and the husband was happy.",
            "The gate was finally opened, and the husband was glad.",
            "The gate was finally opened, and the husband was joyful.",
        ],
        "explanation": (
            "• porta (the gate)\n"
            "  → *port{T:a}* (gate) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• tandem (finally)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• aperta est (was opened)\n"
            "  → *apert{T:a}* is the PPP of *aperio*, feminine singular {T:nominative} agreeing with *porta*\n"
            "  → *est* + PPP = **perfect passive**: 'was opened' / 'has been opened'\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• maritus (the husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• laetus erat (was happy)\n"
            "  → *laetus* (happy) is a predicate adjective, masculine singular {T:nominative} agreeing with *maritus*\n"
            "  → *erat* (was) is the imperfect 3sg of *sum*"
        ),
    },
    {
        "latin": "haec uxor audita est; tandem pater eam in silva audivit.",
        "english": [
            "This wife was heard; finally the father heard her in the wood.",
            "This wife has been heard; finally the father heard her in the wood.",
            "This wife was listened to; finally the father heard her in the forest.",
            "This wife has been listened to; finally the father heard her in the wood.",
            "This wife was heard; at last the father heard her in the wood.",
            "This wife was heard; eventually the father heard her in the wood.",
        ],
        "explanation": (
            "• haec uxor (this wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *haec* (this) is a demonstrative agreeing with *uxor* as both are feminine singular {T:nominative}\n"
            "• audita est (was heard)\n"
            "  → *audit{T:a}* is the PPP of *audio*, feminine singular {T:nominative} agreeing with *uxor*\n"
            "  → *est* + PPP = **perfect passive**: 'was heard' / 'has been heard'\n"
            "• tandem (finally)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• audiv{B:it} (heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'heard'\n"
            "• eam (her)\n"
            "  → *eam* is the feminine singular {T:accusative} of *is/ea/id* — 'her'\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• in silva (in the wood)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *silv{T:a}* (wood) is a noun, 1st declension feminine singular {T:ablative}"
        ),
    },
    {
        "latin": "illa porta aperta est a marito, sed uxor iam dormiebat.",
        "english": [
            "That gate was opened by the husband, but the wife was already sleeping.",
            "That gate has been opened by the husband, but the wife was already sleeping.",
            "That gate was opened by the husband, but the wife was now sleeping.",
            "The gate was opened by the husband, but the wife was already asleep.",
            "That gate was opened by the husband, but the wife was already fast asleep.",
            "That gate has been opened by the husband, but the wife was now sleeping.",
        ],
        "explanation": (
            "• illa porta (that gate)\n"
            "  → *port{T:a}* (gate) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *illa* (that) is a demonstrative agreeing with *porta* as both are feminine singular {T:nominative}\n"
            "• aperta est (was opened)\n"
            "  → *apert{T:a}* is the PPP of *aperio*, feminine singular {T:nominative} agreeing with *porta*\n"
            "  → *est* + PPP = **perfect passive**: 'was opened' / 'has been opened'\n"
            "• a marito (by the husband)\n"
            "  → *a/ab + ablative* = 'by' (agent of a passive verb)\n"
            "  → *marit{T:o}* (husband) is a noun, 2nd declension masculine singular {T:ablative}\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• uxor (the wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• iam (already)\n"
            "  → *iam* (now / already) is an adverb — flexible position\n"
            "• dorm{R:i}{P:eba}{B:t} (was sleeping)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was sleeping' or 'used to sleep'"
        ),
    },
    {
        "latin": "ille dux auditus est, et tristis in urbe dormiebat.",
        "english": [
            "That leader was heard, and was sleeping sadly in the city.",
            "That leader has been heard, and was sleeping sadly in the city.",
            "That leader was listened to, and was sleeping sadly in the city.",
            "That leader has been listened to, and was sleeping sadly in the city.",
            "That leader was heard, and kept sleeping sadly in the city.",
            "That leader was heard, and used to sleep sadly in the city.",
        ],
        "explanation": (
            "• ille dux (that leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *ille* (that) is a demonstrative agreeing with *dux* as both are masculine singular {T:nominative}\n"
            "• auditus est (was heard)\n"
            "  → *audit{T:us}* is the PPP of *audio*, masculine singular {T:nominative} agreeing with *dux*\n"
            "  → *est* + PPP = **perfect passive**: 'was heard' / 'has been heard'\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• tristis (sad)\n"
            "  → *tristis* (sad) is an adjective agreeing with *dux* as both are masculine singular {T:nominative}\n"
            "• dorm{R:i}{P:eba}{B:t} (was sleeping)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was sleeping' or 'used to sleep'\n"
            "• in urbe (in the city)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *urb{T:e}* (city) is a noun, 3rd declension feminine singular {T:ablative}"
        ),
    },
]


SENTENCES_REVIEW_N4 = [
    {
        "latin": "quamquam haec uxor tristis erat, maritus eius tandem advenit.",
        "english": [
            "Although this wife was sad, her husband finally arrived.",
            "Although this wife was unhappy, her husband finally arrived.",
            "Even though this wife was sad, her husband at last arrived.",
            "Although this wife was sad, her husband finally came.",
            "Although this wife was sorrowful, her husband finally arrived.",
            "Although this wife was sad, her husband finally arrives.",
            "Although this wife was sad, her husband at last arrives.",
        ],
        "explanation": (
            "• quamquam (although)\n"
            "  → *quamquam* (although) is a conjunction — introduces a concessive clause\n"
            "• haec uxor (this wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *haec* (this) is a demonstrative agreeing with *uxor* as both are feminine singular {T:nominative}\n"
            "• tristis erat (was sad)\n"
            "  → *tristis* (sad) is an adjective agreeing with *uxor* as both are feminine singular {T:nominative}\n"
            "  → *erat* (was) is the imperfect 3sg of *sum*\n"
            "• maritus eius (her husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *eius* is the genitive of *is/ea/id* — used as a possessive: 'her' / 'his'\n"
            "• tandem (finally)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• adven{R:i}{B:t} (arrives / arrived)\n"
            "  → *advenio* is the dictionary form, 4th conjugation — *adven{R:i}{B:t}* (present) and *adven{B:it}* (perfect) are identical forms\n"
        ),
    },
    {
        "latin": "ceteri milites ad portam advenerunt, et cum paucis amicis eam aperuerunt.",
        "english": [
            "The rest of the soldiers arrived at the gate, and with a few friends opened it.",
            "The other soldiers arrived at the gate, and opened it with a few friends.",
            "The remaining soldiers came to the gate, and opened it with a few friends.",
            "The rest of the soldiers reached the gate, and with a few friends opened it.",
        ],
        "explanation": (
            "• ceteri milites (the rest of the soldiers)\n"
            "  → *milit{T:es}* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *ceteri* (the rest / the other) is an adjective agreeing with *milites* as both are masculine plural {T:nominative}\n"
            "• adven{B:erunt} (arrived)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven{B:erunt}* is the perfect they form\n"
            "  → the perfect tense describes a completed, single past action: 'arrived'\n"
            "• ad portam (to the gate)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• aperu{B:erunt} (opened)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aperu-* is the perfect stem (from *aperui*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'opened'\n"
            "• eam (it)\n"
            "  → *eam* is the feminine singular {T:accusative} of *is/ea/id* — refers back to *porta*\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• cum paucis amicis (with a few friends)\n"
            "  → *cum + ablative* = 'with'\n"
            "  → *amic{T:is}* (friends) is a noun, 2nd declension masculine plural {T:ablative}\n"
            "  → *paucis* (few) is an adjective agreeing with *amicis* as both are masculine plural {T:ablative}"
        ),
    },
    {
        "latin": "ubi unus iuvenis verba regis audivit, statim portam aperuit.",
        "english": [
            "When one young man heard the words of the king, he immediately opened the gate.",
            "When one young man heard the king's words, he immediately opened the gate.",
            "When a single young man heard the words of the king, he at once opened the gate.",
            "When one young man heard the words of the king, he straight away opened the gate.",
            "When one young man listened to the words of the king, he immediately opened the gate.",
        ],
        "explanation": (
            "• ubi (when)\n"
            "  → *ubi* (when) is a temporal conjunction — here with the perfect = 'when X-ed'\n"
            "• unus iuvenis (one young man)\n"
            "  → *iuvenis* (young man) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *unus* (one / a single) is an adjective agreeing with *iuvenis* as both are masculine singular {T:nominative}\n"
            "• audiv{B:it} (heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'heard'\n"
            "• verba regis (the words of the king)\n"
            "  → *verb{T:a}* (words) is a noun, 2nd declension neuter plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → *reg{T:is}* (of the king) is a noun, 3rd declension masculine singular {T:genitive} — 'of...' / 'the king's'\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• aperu{B:it} (opened)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aperu-* is the perfect stem (from *aperui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'opened'\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "tantus erat vultus eius dei; omnes igitur milites perterriti portam aperuerunt.",
        "english": [
            "So great was the face of that god; therefore all the terrified soldiers opened the gate.",
            "So great was the expression of that god; and so all the terrified soldiers opened the gate.",
            "So great was the face of that god; therefore all the very frightened soldiers opened the gate.",
            "The face of that god was so great; and so all the terrified soldiers opened the gate.",
            "So great was the face of that god; therefore all the soldiers, terrified, opened the gate.",
            "So great was that god's face; therefore all the terrified soldiers opened the gate.",
            "That god's face was so great; and so all the terrified soldiers opened the gate.",
        ],
        "explanation": (
            "• vultus eius dei (the face of that god)\n"
            "  → *vultus* (face / expression) is a noun, 4th declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *eius* is the genitive of *is/ea/id* — used as a possessive: 'his' / 'of that one'\n"
            "  → *dei* is the masculine singular {T:genitive} of *deus* — 'of (a/the) god'\n"
            "• tantus erat (was so great)\n"
            "  → *tantus* (so great) is an adjective, masculine singular {T:nominative} agreeing with *vultus*\n"
            "  → *erat* (was) is the imperfect 3sg of *sum*\n"
            "• omnes milites perterriti (all the terrified soldiers)\n"
            "  → *milit{T:es}* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *omnes* (all) and *perterriti* (terrified) are adjectives agreeing with *milites* as all are masculine plural {T:nominative}\n"
            "• igitur (therefore)\n"
            "  → *igitur* (therefore) is a conjunction — postpositive (2nd word of its clause)\n"
            "• aperu{B:erunt} (opened)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aperu-* is the perfect stem (from *aperui*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'opened'\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "\"cur,\" inquit regina, \"in silva multos annos dormiebas?\" ille nihil audivit.",
        "english": [
            "\"Why,\" said the queen, \"were you sleeping in the wood for many years?\" He heard nothing.",
            "\"Why,\" said the queen, \"were you sleeping in the forest for many years?\" He heard nothing.",
            "\"Why,\" said the queen, \"used you to sleep in the wood for many years?\" He heard nothing.",
            "\"Why,\" said the queen, \"were you asleep in the wood for many years?\" He heard nothing.",
            "\"Why,\" said the queen, \"were you sleeping in the wood for many years?\" That man heard nothing.",
        ],
        "explanation": (
            "• cur (why)\n"
            "  → *cur* (why) is an adverb — introduces a question\n"
            "• inquit (said)\n"
            "  → *inquit* (said) is a defective verb — always splits direct speech, placed after the first word(s)\n"
            "• regina (the queen)\n"
            "  → *regin{T:a}* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• dorm{R:i}{P:eba}{B:s} (were you sleeping)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:s}* shows it is the you (singular) form\n"
            "  → the imperfect describes a continuing or repeated past action: 'were sleeping' or 'used to sleep'\n"
            "• in silva (in the wood)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *silv{T:a}* (wood) is a noun, 1st declension feminine singular {T:ablative}\n"
            "• multos annos (for many years)\n"
            "  → *ann{T:os}* (years) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → this is the **accusative of duration**: 'for X years' (no preposition needed)\n"
            "  → *multos* (many) is an adjective agreeing with *annos* as both are masculine plural {T:accusative}\n"
            "• ille (he / that man)\n"
            "  → *ille* is the masculine singular {T:nominative} of *ille/illa/illud* — 'that man' / 'he'\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• audiv{B:it} (heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'heard'\n"
            "• nihil (nothing)\n"
            "  → *nihil* (nothing) is indeclinable — the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "hic equus prope portam advenit; uxor eum statim audivit.",
        "english": [
            "This horse arrived near the gate; the wife immediately heard it.",
            "This horse arrived close to the gate; the wife immediately heard it.",
            "This horse came near the gate; the wife at once heard it.",
            "This horse arrived near the gate; the wife straight away heard it.",
            "This horse reached near the gate; the wife immediately heard it.",
            "This horse arrives near the gate; the wife immediately heard it.",
            "This horse comes near the gate; the wife immediately heard it.",
        ],
        "explanation": (
            "• hic equus (this horse)\n"
            "  → *equus* (horse) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *hic* (this) is a demonstrative agreeing with *equus* as both are masculine singular {T:nominative}\n"
            "• adven{R:i}{B:t} (arrives / arrived)\n"
            "  → *advenio* is the dictionary form, 4th conjugation — *adven{R:i}{B:t}* (present) and *adven{B:it}* (perfect) are identical forms\n"
            "• prope portam (near the gate)\n"
            "  → *prope + accusative* = 'near' / 'close to'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "• uxor (the wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• audiv{B:it} (heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'heard'\n"
            "• eum (it / him)\n"
            "  → *eum* is the masculine singular {T:accusative} of *is/ea/id* — refers to *equus*\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "quo modo ille maritus filiam audivit? per urbem advenit, et portas tantas aperuit.",
        "english": [
            "How did that husband hear his daughter? He arrived through the city, and opened such huge gates.",
            "How did that husband hear his daughter? He came through the city, and opened such huge gates.",
            "How did that husband hear his daughter? He arrived through the city, and opened such massive gates.",
            "How did that husband hear his daughter? He came through the city, and opened the huge gates.",
            "How did that husband hear his daughter? He arrived through the city, and opened gates so huge.",
            "How did that husband hear his daughter? He arrives through the city, and opened such huge gates.",
            "How did that husband hear his daughter? He comes through the city, and opened such huge gates.",
        ],
        "explanation": (
            "• quo modo (how / in what way)\n"
            "  → *quo modo* is an idiom meaning 'how' — literally 'in what manner'\n"
            "• ille maritus (that husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *ille* (that) is a demonstrative agreeing with *maritus* as both are masculine singular {T:nominative}\n"
            "• audiv{B:it} (heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'heard'\n"
            "• filiam (daughter)\n"
            "  → *fili{T:am}* (daughter) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• adven{R:i}{B:t} (arrives / arrived)\n"
            "  → *advenio* is the dictionary form, 4th conjugation — *adven{R:i}{B:t}* (present) and *adven{B:it}* (perfect) are identical forms\n"
            "• per urbem (through the city)\n"
            "  → *per + accusative* = 'through'\n"
            "  → *urb{T:em}* (city) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• aperu{B:it} (opened)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aperu-* is the perfect stem (from *aperui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'opened'\n"
            "• portas tantas (such huge gates)\n"
            "  → *port{T:as}* (gates) is a noun, 1st declension feminine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → *tantas* (so great / so huge) is an adjective agreeing with *portas* as both are feminine plural {T:accusative}"
        ),
    },
    {
        "latin": "postquam uxor dormivit, maritus suus ad portam advenit.",
        "english": [
            "After the wife slept, her own husband arrived at the gate.",
            "After the wife had slept, her own husband arrived at the gate.",
            "After the wife slept, her husband came to the gate.",
            "After the wife slept, her own husband came to the gate.",
            "After the wife had gone to sleep, her husband arrived at the gate.",
            "After the wife slept, her own husband arrives at the gate.",
            "After the wife slept, her own husband comes to the gate.",
        ],
        "explanation": (
            "• postquam (after)\n"
            "  → *postquam* (after) is a temporal conjunction — with perfect tense in Latin = 'after X-ed' in English\n"
            "• uxor (the wife)\n"
            "  → *uxor* (wife) is a noun, 3rd declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• dormiv{B:it} (slept)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dormiv-* is the perfect stem (from *dormivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'slept'\n"
            "• maritus suus (her own husband)\n"
            "  → *maritus* (husband) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *suus* (his/her own) is a possessive adjective agreeing with *maritus*\n"
            "• adven{R:i}{B:t} (arrives / arrived)\n"
            "  → *advenio* is the dictionary form, 4th conjugation — *adven{R:i}{B:t}* (present) and *adven{B:it}* (perfect) are identical forms\n"
            "• ad portam (to the gate)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}"
        ),
    },
    {
        "latin": "\"cur,\" inquit pater, \"portam iam aperis?\" filius nihil audivit; pater igitur portam ipse aperuit.",
        "english": [
            "\"Why,\" said the father, \"are you opening the gate?\" The son heard nothing; the father therefore opened the gate himself.",
            "\"Why,\" said the father, \"are you already opening the gate?\" The son heard nothing; the father therefore opened the gate himself.",
            "\"Why,\" said the father, \"are you now opening the gate?\" The son heard nothing; the father therefore opened the gate himself.",
            "\"Why,\" said the father, \"are you opening the gate?\" The son heard nothing; the father himself therefore opened the gate.",
            "\"Why,\" said the father, \"are you opening the gate now?\" The son heard nothing; and so the father opened the gate himself.",
        ],
        "explanation": (
            "• cur (why)\n"
            "  → *cur* (why) is an adverb — introduces a question\n"
            "• inquit (said)\n"
            "  → *inquit* (said) is a defective verb — always splits direct speech, placed after the first word(s)\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• iam (now / already)\n"
            "  → *iam* (now / already) is an adverb — flexible position\n"
            "• aper{R:i}{B:s} (you are opening)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aper-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{B:s}* shows it is the you (singular) form\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• filius (the son)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• audiv{B:it} (heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'heard'\n"
            "• nihil (nothing)\n"
            "  → *nihil* (nothing) is indeclinable — the {T:accusative} is the {N:object} so it receives the verb\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative} — subject of the second main clause\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• igitur (therefore)\n"
            "  → *igitur* (therefore) is a conjunction — postpositive (2nd word of its clause)\n"
            "• ipse (himself)\n"
            "  → *ipse* (himself) is an emphatic pronoun, masculine singular {T:nominative} agreeing with *pater*\n"
            "• aperu{B:it} (opened)\n"
            "  → *aperio* (I open) is the dictionary form of this verb, 4th conjugation\n"
            "  → *aperu-* is the perfect stem (from *aperui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'opened'\n"
            "• portam (the gate)\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "illae feminae tristes in silva dormiebant, sed pauci milites eas tandem audiverunt, et ad portam advenerunt.",
        "english": [
            "Those sad women were sleeping in the wood, but a few soldiers finally heard them and arrived at the gate.",
            "Those unhappy women were sleeping in the wood, but a few soldiers at last heard them and came to the gate.",
            "Those sad women used to sleep in the wood, but few soldiers finally heard them and arrived at the gate.",
            "Those sad women kept sleeping in the wood, but a few soldiers finally heard them and arrived at the gate.",
            "Those sorrowful women were sleeping in the wood, but a few soldiers finally heard them and came to the gate.",
        ],
        "explanation": (
            "• illae feminae tristes (those sad women)\n"
            "  → *femin{T:ae}* (women) is a noun, 1st declension feminine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *illae* (those) is a demonstrative agreeing with *feminae* as both are feminine plural {T:nominative}\n"
            "  → *tristes* (sad) is an adjective agreeing with *feminae* as both are feminine plural {T:nominative}\n"
            "• dorm{R:i}{P:eba}{B:nt} (were sleeping)\n"
            "  → *dormio* (I sleep) is the dictionary form of this verb, 4th conjugation\n"
            "  → *dorm-* is the stem\n"
            "  → *-{R:i}-* shows it belongs to the 4th conjugation\n"
            "  → *-{P:eba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "  → the imperfect describes a continuing or repeated past action: 'were sleeping' or 'used to sleep'\n"
            "• in silva (in the wood)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *silv{T:a}* (wood) is a noun, 1st declension feminine singular {T:ablative}\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• pauci milites (a few soldiers)\n"
            "  → *milit{T:es}* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *pauci* (few / a few) is an adjective agreeing with *milites* as both are masculine plural {T:nominative}\n"
            "• tandem (finally)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• audiv{B:erunt} (heard)\n"
            "  → *audio* (I hear) is the dictionary form of this verb, 4th conjugation\n"
            "  → *audiv-* is the perfect stem (from *audivi*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'heard'\n"
            "• eas (them)\n"
            "  → *eas* is the feminine plural {T:accusative} of *is/ea/id* — refers to *feminae*\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins clauses\n"
            "• adven{B:erunt} (arrived)\n"
            "  → *advenio* (I arrive) is the dictionary form of this verb, 4th conjugation\n"
            "  → *adven{B:erunt}* is the perfect they form\n"
            "  → the perfect tense describes a completed, single past action: 'arrived'\n"
            "• ad portam (to the gate)\n"
            "  → *ad + accusative* = 'to' / 'towards'\n"
            "  → *port{T:am}* (gate) is a noun, 1st declension feminine singular {T:accusative}"
        ),
    },
]


NODE4_TITLE = "4th Conjugation (Top 150)"


# ── 16 sets, mirroring Node 3 structure with 4th-conj content ────────────────
SETS_N4 = [
    # Row 1: foundations
    {
        "id":53, "node":4, "node_title":NODE4_TITLE,
        "title":"Present: 'I' Form",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **first principal part** of all 4th conjugation verbs in your top-150 list — the dictionary form (the 'I' form).",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_4TH_TOP150,
            "mode":"presents",
            "show_parts_so_far":1,
            "gap_positions":[0],
            "pattern_screen":{
                "title":"4th Conjugation: The 'I' Form",
                "subtitle":"All 4th-conjugation verbs end in *-io* in the dictionary form, and *-ire* in the infinitive:",
                "examples":[
                    {"full":"audio",   "ending":"io", "english":"I hear"},
                    {"full":"dormio",  "ending":"io", "english":"I sleep"},
                    {"full":"aperio",  "ending":"io", "english":"I open"},
                    {"full":"advenio", "ending":"io", "english":"I arrive"},
                ],
                "footnote":"4th conjugation verbs are recognised by their *-io* present and *-ire* infinitive — distinct from 1st (*-are*), 2nd (*-ere*), and 3rd (*-ere*)."
            }
        },
    },
    {
        "id":54, "node":4, "node_title":NODE4_TITLE,
        "title":"Present Tense Endings",
        "type":"translate_form",
        "sell":"This set teaches you all six forms of the **present tense** for 4th conjugation verbs.",
        "pass_mark":80,
        "screens":[
            {"heading":"The Present Tense — 4th conj.",
             "body":"The person endings *-o / -s / -t / -mus / -tis / -nt* are the same across all conjugations — only the stem vowel changes.\n\nThe *-i-* stem vowel is the signature of the 4th conjugation.",
             "table":TABLE_PRESENT_4TH,
             "table_note":"⚠ *-it* (he/she) and *-imus* (we) look identical to perfect endings — always check the stem vowel to tell them apart.\n\nNote: the *they* form inserts *-u-* before the ending: *audi**u**nt*.\n\nColour key:\n**red** = stem vowel (*-i-*)\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_PRESENT_N4},
    },
    {
        "id":55, "node":4, "node_title":NODE4_TITLE,
        "title":"Sentence Vocabulary",
        "type":"vocab", "optional":True,
        "sell":"Here are the words that will appear in the sentences of this node. Some of these will already be familiar to you.",
        "pass_mark":80,
        "content":{"vocab":NODE4_VOCAB},
    },
    {
        "id":56, "node":4, "node_title":NODE4_TITLE,
        "title":"The Present Tense",
        "type":"sentences",
        "sell":"This set practises translating sentences using 4th conjugation verbs in the present tense.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PRESENT_TEST_N4},
    },
    # Row 2
    {
        "id":57, "node":4, "node_title":NODE4_TITLE,
        "title":"Infinitive",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **second principal part** — the infinitive of 4th conjugation verbs (always *-ire*).",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_4TH_TOP150,
            "mode":"infinitives",
            "show_parts_so_far":1,
            "pattern_screen":{
                "title":"4th Conjugation: The Infinitive",
                "subtitle":"4th conjugation infinitives always end in *-ire*:",
                "examples":[
                    {"present":"audio",   "full":"audire",   "ending":"re", "english":"to hear"},
                    {"present":"dormio",  "full":"dormire",  "ending":"re", "english":"to sleep"},
                    {"present":"aperio",  "full":"aperire",  "ending":"re", "english":"to open"},
                    {"present":"advenio", "full":"advenire", "ending":"re", "english":"to arrive"},
                ],
                "footnote":"All 4th conjugation infinitives end in *-ire*."
            }
        },
    },
    {
        "id":58, "node":4, "node_title":NODE4_TITLE,
        "title":"The Future Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **future tense** for 4th conjugation verbs.",
        "pass_mark":80,
        "screens":[
            {"heading":"The Future Tense — 4th conj.",
             "body":"4th conjugation verbs form their future tense with the same pattern as the 3rd conjugation. The *-i-* stem vowel is preserved throughout.",
             "table":TABLE_FUTURE_4TH,
             "table_note":"Colour key:\n**red** = stem vowel (*-i-*)\n**purple** = future tense marker\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_FUTURE_N4},
    },
    {
        "id":59, "node":4, "node_title":NODE4_TITLE,
        "title":"The Imperfect Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **imperfect tense** for 4th conjugation verbs.",
        "pass_mark":80,
        "screens":[
            {"heading":"The Imperfect Tense — 4th conj.",
             "body":"The imperfect tense refers to repeated or ongoing action in the past. The endings are *-bam*, *-bas*, *-bat*, *-bamus*, *-batis*, *-bant* — the same across all conjugations. In the 4th conjugation, an extra *-e-* appears before *-ba-*, after the stem vowel *-i-*.",
             "table":TABLE_IMPERFECT_4TH,
             "table_note":"Spot *-ba-* to identify the imperfect immediately.\n\nColour key:\n**red** = stem vowel (*-i-*) + theme *-e-*\n**purple** = tense marker (*-ba-*)\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_IMPERFECT_N4},
    },
    {
        "id":60, "node":4, "node_title":NODE4_TITLE,
        "title":"The Present System",
        "type":"sentences",
        "sell":"This set tests your ability to translate sentences that use the present, future, and imperfect tenses with 4th conjugation verbs.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PRESENT_SYSTEM_N4},
    },
    # Row 3
    {
        "id":61, "node":4, "node_title":NODE4_TITLE,
        "title":"Perfect: 'I' Form",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **third principal part** — the perfect 'I' form for 4th conjugation verbs.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_4TH_TOP150,
            "mode":"perfects",
            "show_parts_so_far":2,
            "pattern_screen":{
                "title":"4th Conjugation: The Perfect",
                "subtitle":"Most 4th-conj. perfects use *-v-* or *-u-*, but some are irregular (no marker — just a vowel change):",
                "examples":[
                    {"full":"audivi",   "ending":"vi", "inf":"audire",   "english":"I heard",   "present":"audio"},
                    {"full":"dormivi",  "ending":"vi", "inf":"dormire",  "english":"I slept",   "present":"dormio"},
                    {"full":"aperui",   "ending":"ui", "inf":"aperire",  "english":"I opened",  "present":"aperio"},
                    {"full":"adveni",   "ending":"i",  "inf":"advenire", "english":"I arrived", "present":"advenio"},
                ],
                "footnote":"*audio* and *dormio* take *-v-* (the regular 4th-conj. perfect marker). *aperio* takes *-u-*. *advenio* has no marker (just a vowel shortening: *adveni*)."
            }
        },
    },
    {
        "id":62, "node":4, "node_title":NODE4_TITLE,
        "title":"Perfect Tense: All Endings",
        "type":"translate_form",
        "sell":"This set teaches you all six forms of the **perfect tense** for 4th conjugation verbs.",
        "pass_mark":80,
        "screens":[
            {"heading":"The Perfect Tense — 4th conj.",
             "body":"Built on the **perfect stem** (the 3rd principal part, minus the final *-i*).",
             "table":TABLE_PERFECT_4TH,
             "table_note":"The four perfect-stem markers are *-v-*, *-u-*, *-x-*, *-s-*. For 4th conjugation: *-v-* is the main marker (*audivi*, *dormivi*); *-u-* also appears (*aperui*); and *adveni* has no marker (vowel shortening — learn it separately).\n\nColour key:\n**purple** = stem marker\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_PERFECT_N4},
    },
    {
        "id":63, "node":4, "node_title":NODE4_TITLE,
        "title":"The Pluperfect Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **pluperfect tense** for 4th conjugation verbs — built on the perfect stem with the marker *-era-*.",
        "pass_mark":80,
        "screens":[
            {"heading":"The Pluperfect Tense — 4th conj.",
             "body":"The pluperfect tense is used for actions completed before another past event ('had heard', 'had slept').\n\nWhere in English we add **'had'** to express the pluperfect, in Latin the pluperfect is built on the perfect stem by adding the tense marker *-era-* before the person ending.",
             "table":TABLE_PLUPERFECT_4TH,
             "table_note":"The pluperfect uses the same perfect stem as the perfect (here *audi-v-*), then adds the marker *-era-* and the person ending. Be careful not to confuse the perfect *-erunt* (they heard) with the pluperfect *-erant* (they had heard) — whenever you see *-era-*, it must be pluperfect.\n\nColour key:\n**purple** = stem marker (*-v-*)\n**pink** = pluperfect marker (*-era-*)\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_PLUPERFECT_N4},
    },
    {
        "id":64, "node":4, "node_title":NODE4_TITLE,
        "title":"Perfect & Pluperfect",
        "type":"sentences",
        "sell":"This set practises translating sentences using the perfect and pluperfect tenses with 4th conjugation verbs.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_ACTIVE_N4},
    },
    # Row 4
    {
        "id":65, "node":4, "node_title":NODE4_TITLE,
        "title":"Perfect Passive Participle (PPP)",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **fourth principal part** — the **Perfect Passive Participle (PPP)** for 4th conjugation verbs.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_4TH_TOP150,
            "mode":"ppps",
            "show_parts_so_far":3,
            "pattern_screen":{
                "title":"4th Conjugation: The PPP",
                "subtitle":"4th-conj. PPPs end in *-tus*, but the stem must be memorised:",
                "examples":[
                    {"present":"audio",   "infinitive":"audire",  "perfect":"audivi", "full":"auditus", "ending":"tus", "english":"having been heard"},
                    {"present":"aperio",  "infinitive":"aperire", "perfect":"aperui", "full":"apertus", "ending":"tus", "english":"having been opened"},
                ],
                "footnote":"You can always translate a PPP as **'having been'** + the verb's meaning — e.g. *auditus* = 'having been heard'. It acts like an adjective, agreeing with the noun it describes in gender, number, and case.\n\n**PPP + est / sunt = perfect passive**: *auditus est* = 'he was heard'; *audita sunt* = 'they (n.) were heard'.\n\nNote: *dormio* and *advenio* have no PPP at GCSE."
            }
        },
    },
    {
        "id":66, "node":4, "node_title":NODE4_TITLE,
        "title":"Perfect Passive Participles",
        "type":"sentences",
        "sell":"You can always translate a PPP as **'having been ___'** — this set practises sentences with the Perfect Passive Participle (*PPP + est / sunt* = perfect passive).",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PPP_N4},
    },
    {
        "id":67, "node":4, "node_title":NODE4_TITLE,
        "title":"Build the Principal Parts",
        "type":"building_parts",
        "sell":"This set tests all four principal parts of 4th conjugation verbs in random order. You are given the present 'I' form and must supply the **infinitive**, **perfect**, or **PPP** from memory.",
        "pass_mark":80,
        "content":{"verbs":VERBS_4TH_TOP150, "mode":"all_four", "show_parts_so_far":4, "gap_positions":[1, 2, 3]},
    },
    {
        "id":68, "node":4, "node_title":NODE4_TITLE,
        "title":"Review",
        "type":"review",
        "badge":"test",
        "sell":"This set reviews everything in the node: parse and translate individual verb forms, then translate sentences covering all tenses and PPPs with 4th conjugation verbs.",
        "pass_mark":80,
        "content":{
            "sentences": SENTENCES_REVIEW_N4,
            "parse_translate": PARSE_TRANSLATE_QUESTIONS_N4,
        },
    },
]


SETS_N4_BY_ID = {s["id"]: s for s in SETS_N4}
