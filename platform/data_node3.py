"""
Latin GCSE Mastery Platform - Content Data, Node 3 (3rd Conjugation).
Mirrors the architecture of data.py (Node 1) and data_node2.py (Node 2) but for Node 3.

Focus: 3rd conjugation verbs (duco, dico, pono, peto, quaero, relinquo,
       discedo, constituo, cogo) and the -io subset (cupio, facio, effugio);
       '*iter facere*' idiom; 3rd-decl nouns (rex, dux, comes, miles, etc.).

DRAFT - pending teacher review before integration with data.py.

Per Eduqas scope (carried forward from Node 2):
  - No demonstratives (ille / hic / is ...) reach Node 3 sentences (Node 4 territory).
  - No 'tam' in sentences (Node 5).
  - No pluperfect-passive forms - passives capped at perfect passive (*PPP + est*/sunt).
  - Ideal perfect-passive translation: 'was Xed' (not 'has been Xed').
  - Ideal imperfect translation: 'was Xing' (no bare past in english list - marker
    flags bare past as a tense error).
  - Ideal pluperfect-active translation: MUST include 'had Xed'.
  - Ideal PPP standalone: 'having been Xed'.
  - Ideal English (the FIRST entry of `english`) NEVER uses 'his', 'her', 'their',
    'my', 'your' - use 'the' or 'a/an' instead. Possessives may appear in variants.
"""

from OFFICIAL_GLOSSES import g as _g
from data import NODE1_VOCAB as _N1_VOCAB
from data_node2 import NODE2_VOCAB as _N2_VOCAB
from sentence_vocab_scanner import build_tile_vocab as _build_tile_vocab


# ── 3rd Conjugation verbs - Top 150 (12 verbs incl. -io subset) ──────────────
# Tuple: (present, infinitive, perfect, ppp_or_None,
#         eng_present, eng_infinitive, eng_perfect, eng_ppp_or_None)
# discedo and effugio have NO PPP.
VERBS_3RD_TOP150 = [
    # plain 3rd conjugation
    ("duco",       "ducere",       "duxi",       "ductus",      "I lead",        "to lead",        "I led",        "having been led"),
    ("dico",       "dicere",       "dixi",       "dictus",      "I say",         "to say",         "I said",       "having been said"),
    ("pono",       "ponere",       "posui",      "positus",     "I put, place",  "to put, place",  "I put, placed","having been put, placed"),
    ("peto",       "petere",       "petivi",     "petitus",     "I seek, beg, ask, attack", "to seek, beg, ask, attack", "I sought, begged, asked, attacked", "having been sought, begged, asked, attacked"),
    ("quaero",     "quaerere",     "quaesivi",   "quaesitus",   "I search, ask (for)", "to search, ask (for)", "I searched, asked (for)", "having been searched, asked for"),
    ("relinquo",   "relinquere",   "reliqui",    "relictus",    "I leave behind","to leave behind","I left behind","having been left behind"),
    ("discedo",    "discedere",    "discessi",   None,          "I leave",       "to leave",       "I left",       None),
    ("constituo",  "constituere",  "constitui",  "constitutus", "I decide",      "to decide",      "I decided",    "having been decided"),
    ("cogo",       "cogere",       "coegi",      "coactus",     "I force",       "to force",       "I forced",     "having been forced"),
    ("occido",     "occidere",     "occidi",     "occisus",     "I kill",        "to kill",        "I killed",     "having been killed"),
    # -io subset
    ("cupio",      "cupere",       "cupivi",     "cupitus",     "I want",        "to want",        "I wanted",     "having been wanted"),
    ("facio",      "facere",       "feci",       "factus",      "I make, do",    "to make, do",    "I made, did",  "having been made, done"),
    ("effugio",    "effugere",     "effugi",     None,          "I escape",      "to escape",      "I escaped",    None),
]


# ── Node 3 Sentence Vocabulary - non-verb lemmas across all 50 sentences ─────
NODE3_VOCAB = [
    # Nouns (3rd-declension focus)
    {"id":"homo",    "latin":"homo",    "english":[_g("homo")],    "pos":"noun",
     "derivatives":[
         {"word":"homicide",  "meaning":"the killing of one person by another"},
         {"word":"hominid",   "meaning":"a member of the group of primates that includes humans and their ancestors"},
         {"word":"homo sapiens", "meaning":"the scientific name for modern humans — literally 'wise person'"},
     ]},
    {"id":"iuvenis", "latin":"iuvenis", "english":[_g("iuvenis")], "pos":"noun",
     "derivatives":[
         {"word":"juvenile",   "meaning":"relating to young people, e.g. juvenile crime"},
         {"word":"rejuvenate", "meaning":"to make someone look or feel young and energetic again"},
     ]},
    {"id":"rex",     "latin":"rex",     "english":[_g("rex")],     "pos":"noun",
     "derivatives":[
         {"word":"regal",    "meaning":"fit for a king — dignified and impressive"},
         {"word":"reign",    "meaning":"the period a ruler holds power"},
         {"word":"T-Rex",    "meaning":"Tyrannosaurus Rex — literally 'king of the tyrant lizards'"},
     ]},
    {"id":"vir",     "latin":"vir",     "english":[_g("vir")],     "pos":"noun",
     "derivatives":[
         {"word":"virile",  "meaning":"having the strength and energy traditionally associated with men"},
         {"word":"virtue",  "meaning":"originally meant strength and manliness — now means moral goodness"},
         {"word":"virility","meaning":"strength and energy, especially associated with men"},
     ]},
    {"id":"miles",   "latin":"miles",   "english":[_g("miles")],   "pos":"noun",
     "derivatives":[
         {"word":"military", "meaning":"relating to soldiers and armed forces"},
         {"word":"militia",  "meaning":"a group of armed civilians who fight like soldiers"},
         {"word":"militant", "meaning":"aggressively active in pursuit of a cause"},
     ]},
    {"id":"dux",     "latin":"dux",     "english":[_g("dux")],     "pos":"noun",
     "derivatives":[
         {"word":"duke",    "meaning":"a high-ranking nobleman — from Latin dux, meaning leader"},
         {"word":"duchess", "meaning":"the wife of a duke, or a noblewoman of equal rank"},
         {"word":"duchy",   "meaning":"the territory ruled by a duke"},
     ]},
    {"id":"comes",   "latin":"comes",   "english":[_g("comes")],   "pos":"noun",
     "derivatives":[
         {"word":"count",  "meaning":"a European nobleman — from Latin comes, the companion of a ruler"},
         {"word":"county", "meaning":"an administrative region — originally the territory of a count"},
     ]},
    {"id":"mors",    "latin":"mors",    "english":[_g("mors")],    "pos":"noun",
     "derivatives":[
         {"word":"mortal",    "meaning":"able to die — all living things are mortal"},
         {"word":"immortal",  "meaning":"living forever — unable to die"},
         {"word":"mortuary",  "meaning":"a place where bodies are kept before burial or cremation"},
         {"word":"moribund",  "meaning":"near death, or at a point of no longer functioning"},
     ]},
    {"id":"iter",    "latin":"iter",    "english":[_g("iter")],    "pos":"noun",
     "derivatives":[
         {"word":"itinerary",  "meaning":"a planned route or schedule for a journey"},
         {"word":"itinerant",  "meaning":"travelling from place to place without a permanent home"},
     ]},
    {"id":"cibus",   "latin":"cibus",   "english":[_g("cibus")],   "pos":"noun"},
    {"id":"donum",   "latin":"donum",   "english":[_g("donum")],   "pos":"noun",
     "derivatives":[
         {"word":"donate",   "meaning":"to give something to a good cause without expecting payment"},
         {"word":"donation", "meaning":"something given freely, especially to a charity"},
         {"word":"donor",    "meaning":"a person who donates, e.g. a blood donor"},
     ]},
    {"id":"verbum",  "latin":"verbum",  "english":[_g("verbum")],  "pos":"noun",
     "derivatives":[
         {"word":"verbal",   "meaning":"relating to words, e.g. verbal communication"},
         {"word":"verbose",  "meaning":"using far more words than necessary"},
         {"word":"proverb",  "meaning":"a short, well-known saying that expresses a truth"},
         {"word":"adverb",   "meaning":"a word that modifies a verb, adjective, or other adverb"},
     ]},
    {"id":"manus",   "latin":"manus",   "english":[_g("manus")],   "pos":"noun",
     "derivatives":[
         {"word":"manual",      "meaning":"done by hand, or a handbook of instructions"},
         {"word":"manufacture", "meaning":"to make goods, originally by hand, now usually in factories"},
         {"word":"manuscript",  "meaning":"a document written by hand — before printing existed"},
         {"word":"manage",      "meaning":"originally meant to handle horses by hand — now means to be in charge"},
     ]},
    {"id":"caput",   "latin":"caput",   "english":[_g("caput")],   "pos":"noun",
     "derivatives":[
         {"word":"capital",     "meaning":"the head city of a country or state"},
         {"word":"captain",     "meaning":"the head or leader of a group, ship, or team"},
         {"word":"decapitate",  "meaning":"to cut off someone's head"},
         {"word":"chapter",     "meaning":"a section of a book — from caput, a heading"},
     ]},
    # Adjectives
    {"id":"fortis",  "latin":"fortis",  "english":[_g("fortis")],  "pos":"adjective",
     "derivatives":[
         {"word":"fort",     "meaning":"a strong building designed for defence"},
         {"word":"fortify",  "meaning":"to make something stronger or more secure"},
         {"word":"fortress", "meaning":"a large, heavily fortified building or town"},
         {"word":"effort",   "meaning":"the energy you use to do something — literally strength directed outward"},
     ]},
    {"id":"iratus",  "latin":"iratus",  "english":[_g("iratus")],  "pos":"adjective",
     "derivatives":[
         {"word":"irate",   "meaning":"very angry"},
         {"word":"irritate","meaning":"to annoy someone, or to cause discomfort"},
     ]},
    {"id":"facilis", "latin":"facilis", "english":[_g("facilis")], "pos":"adjective",
     "derivatives":[
         {"word":"facile",    "meaning":"too easy or simplistic — not showing real thought"},
         {"word":"facilitate","meaning":"to make something easier or help it happen"},
         {"word":"facility",  "meaning":"a place or piece of equipment that makes something easy to do"},
     ]},
    {"id":"dirus",   "latin":"dirus",   "english":[_g("dirus")],   "pos":"adjective",
     "derivatives":[
         {"word":"dire", "meaning":"extremely serious or dreadful, e.g. a dire warning"},
     ]},
    {"id":"alius",   "latin":"alius",   "english":[_g("alius")],   "pos":"adjective",
     "derivatives":[
         {"word":"alias", "meaning":"another name used by a person — an 'other' identity"},
         {"word":"alien", "meaning":"belonging to another world or country — something other"},
     ]},
    {"id":"solus",   "latin":"solus",   "english":[_g("solus")],   "pos":"adjective",
     "derivatives":[
         {"word":"solo",     "meaning":"done alone, e.g. a solo performance"},
         {"word":"solitary", "meaning":"done alone, or existing alone"},
         {"word":"solitude", "meaning":"the state of being alone, often peacefully"},
     ]},
    # Pronouns - Node 3 introduces 1st/2nd plural + reflexive
    {"id":"nos",     "latin":"nos",     "english":[_g("nos")],     "pos":"pronoun", "notes":"can be either the subject (we) or the object (us) - the case is the same"},
    {"id":"vos",     "latin":"vos",     "english":[_g("vos")],     "pos":"pronoun", "notes":"can be either the subject or the object - the case is the same"},
    {"id":"se",      "latin":"se",      "english":[_g("se")],      "pos":"pronoun", "notes":"reflexive - refers back to the subject of the sentence"},
    {"id":"suus",    "latin":"suus",    "english":[_g("suus")],    "pos":"adjective", "notes":"possessive that refers back to the subject ('his own', 'her own', 'their own')"},
    # Determiners / nouns
    {"id":"nihil",   "latin":"nihil",   "english":[_g("nihil")],   "pos":"noun",
     "derivatives":[
         {"word":"nil",        "meaning":"nothing — used especially in scores, e.g. three–nil"},
         {"word":"annihilate", "meaning":"to destroy something completely — to reduce it to nothing"},
     ]},
    # Prepositions
    {"id":"cum_abl", "latin":"cum",     "english":[_g("cum + abl")], "pos":"preposition", "display_label":"+ abl"},
    # Conjunctions
    {"id":"dum",       "latin":"dum",       "english":[_g("dum")],       "pos":"conjunction"},
    {"id":"postquam",  "latin":"postquam",  "english":[_g("postquam")],  "pos":"conjunction"},
    {"id":"simulac",   "latin":"simulac",   "english":[_g("simulac")],   "pos":"conjunction",
     "derivatives":[
         {"word":"simultaneous", "meaning":"happening at the same time — from simul, meaning 'at the same time'"},
         {"word":"simulate",     "meaning":"to imitate or recreate the appearance or conditions of something"},
     ]},
]


# ── Tense ID questions - present/imperfect/future/perfect/pluperfect of 3rd conj ─
TENSE_ID_QUESTIONS_N3 = [
    # Present
    {"form":"ducit",        "plain":"ducit",        "tense":"present",    "translation":"he/she leads"},
    {"form":"dico",         "plain":"dico",         "tense":"present",    "translation":"I say"},
    {"form":"ponunt",       "plain":"ponunt",       "tense":"present",    "translation":"they put, place"},
    {"form":"petit",        "plain":"petit",        "tense":"present",    "translation":"he/she seeks"},
    {"form":"discedimus",   "plain":"discedimus",   "tense":"present",    "translation":"we leave"},
    {"form":"cupiunt",      "plain":"cupiunt",      "tense":"present",    "translation":"they want"},
    {"form":"facit",        "plain":"facit",        "tense":"present",    "translation":"he/she makes, does"},
    # Imperfect
    {"form":"ducebat",      "plain":"ducebat",      "tense":"imperfect",  "translation":"he/she was leading"},
    {"form":"dicebant",     "plain":"dicebant",     "tense":"imperfect",  "translation":"they were saying"},
    {"form":"petebat",      "plain":"petebat",      "tense":"imperfect",  "translation":"he/she was seeking"},
    {"form":"quaerebamus",  "plain":"quaerebamus",  "tense":"imperfect",  "translation":"we were searching"},
    {"form":"cupiebat",     "plain":"cupiebat",     "tense":"imperfect",  "translation":"he/she was wanting"},
    {"form":"faciebant",    "plain":"faciebant",    "tense":"imperfect",  "translation":"they were making, doing"},
    # Future
    {"form":"ducet",        "plain":"ducet",        "tense":"future",     "translation":"he/she will lead"},
    {"form":"dicent",       "plain":"dicent",       "tense":"future",     "translation":"they will say"},
    {"form":"ponam",        "plain":"ponam",        "tense":"future",     "translation":"I will put, place"},
    {"form":"petes",        "plain":"petes",        "tense":"future",     "translation":"you (sg) will seek"},
    {"form":"faciet",       "plain":"faciet",       "tense":"future",     "translation":"he/she will make, do"},
    {"form":"effugient",    "plain":"effugient",    "tense":"future",     "translation":"they will escape"},
    # Perfect
    {"form":"duxit",        "plain":"duxit",        "tense":"perfect",    "translation":"he/she led"},
    {"form":"dixerunt",     "plain":"dixerunt",     "tense":"perfect",    "translation":"they said"},
    {"form":"posuit",       "plain":"posuit",       "tense":"perfect",    "translation":"he/she put, placed"},
    {"form":"reliqui",      "plain":"reliqui",      "tense":"perfect",    "translation":"I left behind"},
    {"form":"coegerunt",    "plain":"coegerunt",    "tense":"perfect",    "translation":"they forced"},
    {"form":"fecit",        "plain":"fecit",        "tense":"perfect",    "translation":"he/she made, did"},
    # Pluperfect
    {"form":"duxerat",      "plain":"duxerat",      "tense":"pluperfect", "translation":"he/she had led"},
    {"form":"dixerant",     "plain":"dixerant",     "tense":"pluperfect", "translation":"they had said"},
    {"form":"petiverat",    "plain":"petiverat",    "tense":"pluperfect", "translation":"he/she had sought"},
    {"form":"constituerat", "plain":"constituerat", "tense":"pluperfect", "translation":"he/she had decided"},
    {"form":"fecerat",      "plain":"fecerat",      "tense":"pluperfect", "translation":"he/she had made, done"},
]


# ════════════════════════════════════════════════════════════════════════════
# SENTENCE SETS
# ════════════════════════════════════════════════════════════════════════════
#
# Pre-adaptation log (against _curr.txt 1150-1546):
#    9: 'eius comes' -> 'comes ducis' (3rd-pers possessive reserved for Node 4)
#   18: 'eum' -> 'comitem' (Node 4 reservation)
#   25: 'eius regina' -> 'regis regina'
#   26: 'illa dea' -> 'dea tristis' (demonstratives reserved)
#   27: 'eum petivit' -> 'comitem petivit'
#   28: 'ei persuasit' -> 'reginae persuasit'
#   30: 'eum coegit' -> 'militem coegit'
#   31: 'iter factum erat' -> 'iter factum est' (pluperf passive -> perf passive)
#   33: 'positum erat' -> 'positum est'
#   35: 'constitutum erat' -> 'constitutum est'
#   38: 'cognitus erat' -> 'cognitus est'
#   39: 'illud verbum dirum ... dictum erat' -> 'verbum dirum ... dictum est'
#   41: 'ille dux' -> 'dux fortis'
#   43: 'eum liberare' -> 'filium liberare'
#   44: 'comes eius' -> 'comes ducis'
#   46: 'eam' -> 'reginam'
#   47: 'tam diram mortem' -> 'diram mortem' (Node 5 'tam' reservation)
#   49: 'filius eius' -> 'filius regis'
# ════════════════════════════════════════════════════════════════════════════


# ── Set 4 (id 40): Present ──────────────────────────────────────────────────
SENTENCES_PRESENT_TEST_N3 = [
    {
        "latin": "regina iter facit.",
        "english": [
            "The queen makes a journey.",
            "The queen is making a journey.",
            "The queen goes on a journey.",
            "The queen travels.",
            "A queen makes a journey.",
        ],
        "explanation": (
            "• regin{T:a} (the queen)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• fac{B:it} (makes)\n"
            "  → *facio* (I make, do) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *fac-* (make) is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• iter (a journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → neuter nouns have the same form in nominative and accusative — context tells you which\n"
            "  → *iter facere* is an idiom meaning 'to make a journey' or 'to travel'"
        ),
    },
    {
        "latin": "comes verbum dicit.",
        "english": [
            "The companion says a word.",
            "The companion says the word.",
            "A companion says a word.",
            "The companion speaks a word.",
            "The companion utters a word.",
            "The companion is saying a word.",
        ],
        "explanation": (
            "• comes (the companion)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• dic{B:it} (says)\n"
            "  → *dico* (I say) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *dic-* (say) is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• verbum (a word)\n"
            "  → *verbum* (word) is a noun, 2nd declension neuter singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "milites aliud iter petunt.",
        "english": [
            "The soldiers seek another journey.",
            "The soldiers seek a different journey.",
            "The soldiers are seeking another journey.",
            "The soldiers look for another journey.",
            "The soldiers are looking for another route.",
            "The soldiers are heading for another journey.",
        ],
        "explanation": (
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• pet{B:unt} (seek)\n"
            "  → *peto* (I seek, beg, ask, attack) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *pet-* (seek) is the stem\n"
            "  → *-{B:unt}* shows it is the they form\n"
            "• aliud iter (another journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → *aliud* (other / another) is an adjective, agreeing with *iter* as both are neuter singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → neuter adjectives have the same form for nominative and accusative — context is key"
        ),
    },
    {
        "latin": "solus homo manum ponit.",
        "english": [
            "The lonely man places a hand.",
            "The lone man places his hand.",
            "The lonely man places his hand.",
            "The lone man puts his hand.",
            "The lone man lays his hand.",
            "The lone man is placing his hand.",
            "Only the man places his hand.",
        ],
        "explanation": (
            "• solus homo (the lone man)\n"
            "  → *homo* (man / person) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → *solus* (alone / only) is an adjective, agreeing with *homo* as both are masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• pon{B:it} (places)\n"
            "  → *pono* (I put, place) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *pon-* (place) is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• man{T:um} (a hand)\n"
            "  → *manus* (hand) is a noun, 4th declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "dux nihil quaerit, et constituit discedere.",
        "english": [
            "The leader searches for nothing, and decides to leave.",
            "The leader searches for nothing, and decides to depart.",
            "The leader is searching for nothing, and decides to leave.",
            "The leader asks for nothing, and decides to leave.",
            "The leader is looking for nothing, and decides to leave.",
            "The leader searches for nothing, and is deciding to leave.",
        ],
        "explanation": (
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• quaer{B:it} (searches for)\n"
            "  → *quaero* (I search, ask for) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *quaer-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• nihil (nothing)\n"
            "  → *nihil* (nothing) is an indeclinable noun used as {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — nothing is being searched for\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• constitu{B:it} (decides)\n"
            "  → *constituo* (I decide) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *constitu-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "  → *constituo* + infinitive = 'decides to Y'\n"
            "• discedere (to leave)\n"
            "  → *discedere* is the infinitive of *discedo* (I leave), 3rd conjugation\n"
            "  → the infinitive completes *constituit*: 'decides TO leave'"
        ),
    },
    {
        "latin": "dux milites cogit, et milites cum comitibus statim discedunt.",
        "english": [
            "The leader forces the soldiers, and the soldiers immediately leave with the companions.",
            "The leader forces the soldiers, and the soldiers immediately leave with their companions.",
            "The leader forces the soldiers, and the soldiers leave with their companions immediately.",
            "The leader is forcing the soldiers, and the soldiers immediately leave with their companions.",
            "The leader forces the soldiers, and the soldiers at once leave with their companions.",
            "The leader forces the soldiers, and the soldiers straight away leave with their companions.",
        ],
        "explanation": (
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of *cogit*\n"
            "• cog{B:it} (forces)\n"
            "  → *cogo* (I force) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *cog-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *cogit* — the soldiers are being forced\n"
            "  → in the second clause, *milites* becomes the {T:nominative} {N:subject} of *discedunt*\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• cum comitibus (with the companions)\n"
            "  → *cum + ablative* = 'with'\n"
            "  → *comitibus* (companions) is the {T:ablative} plural of *comes*\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• disced{B:unt} (leave)\n"
            "  → *discedo* (I leave) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *disced-* is the stem\n"
            "  → *-{B:unt}* shows it is the they form"
        ),
    },
    {
        "latin": "dux milites discedere cogit, et comes iter constituere cupit.",
        "english": [
            "The leader forces the soldiers to leave, and the companion wants to decide on a journey.",
            "The leader is forcing the soldiers to leave, and the companion wants to plan a journey.",
            "The leader forces the soldiers to depart, and the companion wants to decide on a journey.",
            "The leader compels the soldiers to leave, and the companion wants to decide on a journey.",
            "The leader forces the soldiers to go, and the companion wants to settle on a journey.",
        ],
        "explanation": (
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the first clause\n"
            "• cog{B:it} (forces)\n"
            "  → *cogo* (I force) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *cog-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *cogit* — the soldiers are being forced\n"
            "• discedere (to leave)\n"
            "  → *discedere* is the infinitive of *discedo* (I leave), 3rd conjugation\n"
            "  → ***cogo + acc + inf*** = force someone to do something\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• com{T:es} (the companion)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second clause\n"
            "• cup{B:it} (wants)\n"
            "  → *cupio* (I want) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *cup-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "  → ***cupio + inf*** = want to do something\n"
            "• constituere (to decide on)\n"
            "  → *constituere* is the infinitive of *constituo* (I decide), 3rd conjugation\n"
            "  → the infinitive completes *cupit*: 'wants TO decide on'\n"
            "• iter (a journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *constituere*"
        ),
    },
    {
        "latin": "iuvenis iratus ducem alium prope insulam occidit.",
        "english": [
            "The angry young man kills another leader near the island.",
            "The angry young man kills a different leader near the island.",
            "The angry young man is killing another leader near the island.",
            "The angry young man kills another leader close to the island.",
            "The angry young man kills another leader next to the island.",
            "The angry young man slays another leader near the island.",
        ],
        "explanation": (
            "• iuvenis iratus (the angry young man)\n"
            "  → *iuvenis* (young man) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → *iratus* (angry) is an adjective, agreeing with *iuvenis* as both are masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• occid{B:it} (kills)\n"
            "  → *occido* (I kill) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *occid-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• duc{T:em} ali{T:um} (another leader)\n"
            "  → *ducem* (leader) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → *alium* (another) is an adjective agreeing with *ducem* as both are masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the leader is being killed\n"
            "• prope insul{T:am} (near the island)\n"
            "  → *prope + accusative* = near / close to\n"
            "  → *insul{T:am}* (island) is the {T:accusative} singular"
        ),
    },
    {
        "latin": "comes ducis ingentem navem conspicit, et verbum dicit.",
        "english": [
            "The companion of the leader notices a huge ship, and says a word.",
            "The leader's companion catches sight of a huge ship, and says a word.",
            "The companion of the leader spots a huge ship, and says a word.",
            "The companion of the leader notices an enormous ship, and says a word.",
            "The companion of the leader catches sight of a vast ship, and says a word.",
            "The companion of the leader catches sight of a huge ship, and speaks a word.",
        ],
        "explanation": (
            "• comes ducis (the companion of the leader)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "  → *ducis* (of the leader) is the {T:genitive} singular of *dux*\n"
            "  → the {T:genitive} means 'of' — 'the companion OF the leader'\n"
            "• conspic{B:it} (notices / catches sight of)\n"
            "  → *conspicio* (I notice, catch sight of) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *conspic-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "  → *conspicio* is stronger than *video* — 'catch sight of' implies deliberate noticing\n"
            "• ingent{T:em} nav{T:em} (a huge ship)\n"
            "  → *navem* (ship) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "  → *ingentem* (huge) is an adjective agreeing with *navem* as both are feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the ship is being noticed\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• dic{B:it} (says)\n"
            "  → *dico* (I say) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *dic-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• verbum (a word)\n"
            "  → *verbum* (word) is a noun, 2nd declension neuter singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "dum dux milites ducit, regina iter per silvam facit.",
        "english": [
            "While the leader leads the soldiers, the queen makes a journey through the wood.",
            "While the leader is leading the soldiers, the queen makes a journey through the wood.",
            "While the leader leads the soldiers, the queen makes a journey through the forest.",
            "While the leader leads the soldiers, the queen travels through the wood.",
            "While the leader leads the soldiers, the queen goes on a journey through the wood.",
        ],
        "explanation": (
            "• dum (while)\n"
            "  → *dum* (while) introduces a subordinate clause — the background action\n"
            "  → *dum* + present tense = 'while' (an ongoing background action)\n"
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of *ducit*\n"
            "• duc{B:it} (leads)\n"
            "  → *duco* (I lead) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *duc-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the soldiers are being led\n"
            "• regin{T:a} (the queen)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of *facit*\n"
            "• fac{B:it} (makes)\n"
            "  → *facio* (I make, do) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *fac-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form\n"
            "• iter (a journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object}\n"
            "• per silv{T:am} (through the wood)\n"
            "  → *per + accusative* = through\n"
            "  → *silv{T:am}* (wood) is the {T:accusative} singular\n"
            "  → *iter facere* = 'to make a journey' — an idiom for 'to travel'"
        ),
    },
]


# ── Set 8 (id 42): Imperfect & Future ───────────────────────────────────────
SENTENCES_PRESENT_SYSTEM_N3 = [
    {
        "latin": "dux iter faciebat.",
        "english": [
            "The leader was making a journey.",
            "The leader was travelling.",
            "The leader used to make a journey.",
            "The leader kept making a journey.",
            "The leader was going on a journey.",
        ],
        "explanation": (
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• fac{P:ieba}{B:t} (was making)\n"
            "  → *facio* (I make, do) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *fac-* is the stem\n"
            "  → *-{P:ieba}-* is the imperfect marker — 3rd-io uses *-ieba-* not *-eba-*\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was making' or 'used to make'\n"
            "• iter (a journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object}\n"
            "  → ***iter facere*** is an idiom: 'to make a journey' / 'to travel'"
        ),
    },
    {
        "latin": "comes verba dicet.",
        "english": [
            "The companion will say the words.",
            "The companion will say words.",
            "The companion will speak the words.",
            "The companion will utter the words.",
            "A companion will say the words.",
        ],
        "explanation": (
            "• comes (the companion)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• dic{P:e}{B:t} (will say)\n"
            "  → *dico* (I say) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *dic-* is the stem\n"
            "  → *-{P:e}-* marks the future — 3rd conjugation uses *-am/-es/-et* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• verb{T:a} (the words)\n"
            "  → *verbum* (word) is a noun, 2nd declension neuter plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "milites aliud iter petebant.",
        "english": [
            "The soldiers were seeking another journey.",
            "The soldiers were seeking a different journey.",
            "The soldiers were looking for another journey.",
            "The soldiers were making for another journey.",
            "The soldiers used to seek another route.",
        ],
        "explanation": (
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• pet{P:eba}{B:nt} (were seeking)\n"
            "  → *peto* (I seek, beg, ask, attack) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *pet-* is the stem\n"
            "  → *-{P:eba}-* is the imperfect marker — shows the action was ongoing or repeated\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "  → the imperfect describes a continuing or repeated past action: 'were seeking' or 'used to seek'\n"
            "• aliud iter (another journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → *aliud* (another) is an adjective, neuter singular {T:accusative}, agreeing with *iter*\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "iuvenis gladium manu ponet.",
        "english": [
            "The young man will place the sword with a hand.",
            "The young man will place the sword with his hand.",
            "The young man will put the sword with his hand.",
            "The young man will place the sword by hand.",
            "A young man will place the sword with his hand.",
        ],
        "explanation": (
            "• iuvenis (the young man)\n"
            "  → *iuvenis* (young man) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• pon{P:e}{B:t} (will place)\n"
            "  → *pono* (I put, place) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *pon-* is the stem\n"
            "  → *-{P:e}-* marks the future — 3rd conjugation uses *-am/-es/-et* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• gladi{T:um} (the sword)\n"
            "  → *gladius* (sword) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• man{T:u} (with a hand)\n"
            "  → *manus* (hand) is a noun, 4th declension feminine singular {T:ablative}\n"
            "  → **ablative of instrument**: 'with / by means of' (NO preposition needed)"
        ),
    },
    {
        "latin": "nunc rex nihil quaerebat, tandem tamen iter constituet.",
        "english": [
            "Now the king was searching for nothing, but finally he will decide on a journey.",
            "Now the king was asking for nothing, but at last he will decide on a journey.",
            "Now the king was looking for nothing, but finally he will decide on a journey.",
            "The king was now searching for nothing, but at last he will decide on a journey.",
            "Now the king was searching for nothing, but eventually he will decide on a journey.",
            "Now the king was searching for nothing, but finally he will decide a journey.",
            "Now the king was asking for nothing, but at last he will decide a journey.",
            "Now the king was looking for nothing, but finally he will decide a journey.",
            "Now the king was searching for nothing, but eventually he will decide a journey.",
            "Now the king was searching for nothing, but he will finally decide on a journey.",
            "Now the king was searching for nothing, but he will at last decide on a journey.",
        ],
        "explanation": (
            "• nunc (now)\n"
            "  → *nunc* (now) is an adverb — flexible position\n"
            "• rex (the king)\n"
            "  → *rex* (king) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• quaer{P:eba}{B:t} (was searching for)\n"
            "  → *quaero* (I search, ask for) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *quaer-* is the stem\n"
            "  → *-{P:eba}-* is the imperfect marker — shows the action was ongoing or repeated\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was searching' or 'used to search'\n"
            "• nihil (nothing)\n"
            "  → *nihil* (nothing) is an indeclinable noun used as {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — nothing is being searched for\n"
            "• tandem (finally)\n"
            "  → *tandem* (finally / at last) is an adverb — flexible position\n"
            "• tamen (however)\n"
            "  → *tamen* (however / but / yet) is a conjunction — postpositive (2nd word of its clause)\n"
            "• constitu{P:e}{B:t} (will decide on)\n"
            "  → *constituo* (I decide) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *constitu-* is the stem\n"
            "  → *-{P:e}-* marks the future — 3rd conjugation uses *-am/-es/-et* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• iter (a journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "dum dux milites cogebat, reges effugiebant.",
        "english": [
            "While the leader was forcing the soldiers, the kings were escaping.",
            "While the leader was forcing the soldiers, the kings were fleeing.",
            "While the leader was forcing the soldiers, the kings were getting away.",
            "While the leader kept forcing the soldiers, the kings were escaping.",
            "While the leader used to force the soldiers, the kings were escaping.",
            "While the leader was forcing the soldiers, the kings kept escaping.",
            "While the leader was forcing the soldiers, the kings used to escape.",
        ],
        "explanation": (
            "• dum (while)\n"
            "  → *dum* (while) is a temporal conjunction — with the imperfect = 'while' (both actions ongoing)\n"
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the *dum*-clause\n"
            "• cog{P:eba}{B:t} (was forcing)\n"
            "  → *cogo* (I force) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *cog-* is the stem\n"
            "  → *-{P:eba}-* is the imperfect marker — shows the action was ongoing or repeated\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was forcing' or 'used to force'\n"
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the soldiers are being forced\n"
            "• reg{T:es} (the kings)\n"
            "  → *rex* (king) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the main clause\n"
            "• effug{P:ieba}{B:nt} (were escaping)\n"
            "  → *effugio* (I escape) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *effug-* is the stem\n"
            "  → *-{P:ieba}-* is the imperfect marker — 3rd-io uses *-ieba-* not *-eba-*\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "  → the imperfect describes a continuing or repeated past action: 'were escaping' or 'used to escape'"
        ),
    },
    {
        "latin": "dea discedere cupiebat, et tum solum deum relinquebat.",
        "english": [
            "The goddess was wanting to leave, and was then leaving the god alone behind.",
            "The goddess wanted to leave, and was then leaving the god alone behind.",
            "The goddess was wanting to depart, and was then leaving the god alone behind.",
            "The goddess kept wanting to leave, and was then leaving the solitary god behind.",
            "The goddess was wanting to leave, and was then abandoning the solitary god.",
            "The goddess was wanting to leave, and was then leaving the lonely god behind.",
            "The goddess was wanting to leave, and was then abandoning the lonely god.",
        ],
        "explanation": (
            "• de{T:a} (the goddess)\n"
            "  → *dea* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• cup{P:ieba}{B:t} (was wanting)\n"
            "  → *cupio* (I want) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *cup-* is the stem\n"
            "  → *-{P:ieba}-* is the imperfect marker — 3rd-io uses *-ieba-* not *-eba-*\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was wanting' or 'used to want'\n"
            "• discedere (to leave)\n"
            "  → *discedere* is the infinitive of *discedo* (I leave), 3rd conjugation\n"
            "  → ***cupio + inf*** = want to do something\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• tum (then)\n"
            "  → *tum* (then / at that time) is an adverb — flexible position\n"
            "• relinqu{P:eba}{B:t} (was leaving behind)\n"
            "  → *relinquo* (I leave behind) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *relinqu-* is the stem\n"
            "  → *-{P:eba}-* is the imperfect marker — shows the action was ongoing or repeated\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was leaving behind' or 'used to leave behind'\n"
            "• solum deum (the god alone)\n"
            "  → *deus* (god) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → *solum* (alone / only / solitary) is an adjective agreeing with *deum* as both are masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "simulac dux comitem cognoscet, comitem ibi statim accipiet.",
        "english": [
            "As soon as the leader finds out the companion, the leader will immediately receive the companion there.",
            "As soon as the leader gets to know the companion, the leader will immediately receive the companion there.",
            "As soon as the leader recognises the companion, the leader will immediately receive the companion there.",
            "As soon as the leader gets to know the companion, he will immediately receive the companion there.",
            "As soon as the leader finds out about his companion, he will immediately receive his companion there.",
            "As soon as the leader recognises his companion, he will immediately welcome the companion there.",
            "As soon as the leader recognises his companion, he will at once accept the companion there.",
            "As soon as the leader notices the companion, he will immediately receive the companion there.",
            "As soon as the leader will notice the companion, he will immediately receive the companion there.",
            "As soon as the leader recognises the companion, he will immediately receive the companion there.",
            "As soon as the leader gets to know the companion, he will at once receive the companion there.",
            "As soon as the leader finds out about the companion, he will immediately accept the companion there.",
        ],
        "explanation": (
            "• simulac (as soon as)\n"
            "  → *simulac* (as soon as) is a temporal conjunction\n"
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of both verbs\n"
            "• cognosc{P:e}{B:t} (will find out)\n"
            "  → *cognosco* (I find out, recognise) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *cognosc-* is the stem\n"
            "  → *-{P:e}-* marks the future — 3rd conjugation uses *-am/-es/-et* (NOT *-bo/-bi/-bu*)\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → *cognosco* present/future = 'get to know / find out'\n"
            "• comit{T:em} (the companion)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *cognoscet*\n"
            "• ibi (there)\n"
            "  → *ibi* (there) is an adverb — flexible position\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• accip{P:ie}{B:t} (will receive)\n"
            "  → *accipio* (I receive, accept) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *accip-* is the stem\n"
            "  → *-{P:ie}-* marks the future for 3rd-io verbs — uses *-ie-* not *-e-*\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• comit{T:em} (the companion, again)\n"
            "  → same form, the {T:accusative} {N:object} of *accipiet*"
        ),
    },
    {
        "latin": "pater alia verba dicebat, et filium per silvam ducebat.",
        "english": [
            "The father was saying other words, and was leading the son through the wood.",
            "The father was saying different words, and was leading his son through the wood.",
            "The father was speaking other words, and was leading his son through the forest.",
            "The father kept saying other words, and was leading his son through the wood.",
            "The father used to say other words, and was leading his son through the wood.",
            "The father was saying other words, and kept leading the son through the wood.",
            "The father was saying other words, and used to lead the son through the wood.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• dic{P:eba}{B:t} (was saying)\n"
            "  → *dico* (I say) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *dic-* is the stem\n"
            "  → *-{P:eba}-* is the imperfect marker — shows the action was ongoing or repeated\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was saying' or 'used to say'\n"
            "• alia verba (other words)\n"
            "  → *verbum* (word) is a noun, 2nd declension neuter plural {T:accusative}\n"
            "  → *alia* (other) is an adjective, neuter plural {T:accusative}, agreeing with *verba*\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• duc{P:eba}{B:t} (was leading)\n"
            "  → *duco* (I lead) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *duc-* is the stem\n"
            "  → *-{P:eba}-* is the imperfect marker — shows the action was ongoing or repeated\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was leading' or 'used to lead'\n"
            "• fili{T:um} (the son)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• per silv{T:am} (through the wood)\n"
            "  → *per + accusative* = through\n"
            "  → *silv{T:am}* (wood) is the {T:accusative} singular"
        ),
    },
    {
        "latin": "deinde miles constituit discedere, nam dux iratus erat.",
        "english": [
            "Then the soldier decides to leave, for the leader was angry.",
            "Then the soldier decided to leave, for the leader was angry.",
            "Next the soldier decides to leave, because the leader was angry.",
            "Then the soldier decides to leave, for the leader is angry.",
            "Then the soldier is deciding to leave, for the leader was angry.",
        ],
        "explanation": (
            "• deinde (then)\n"
            "  → *deinde* (then / next) is an adverb — flexible position\n"
            "• miles (the soldier)\n"
            "  → *miles* (soldier) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• constitu{B:it} (decides / decided)\n"
            "  → *constituo* (I decide) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *constitu-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form; this form is **ambiguous** (could be present or perfect)\n"
            "  → narrative context here favours 'decided'\n"
            "  → ***constituo + inf*** = 'decide to ___'\n"
            "• discedere (to leave)\n"
            "  → *discedere* is the infinitive of *discedo* (I leave), 3rd conjugation\n"
            "  → the infinitive completes *constituit*: 'decided TO leave'\n"
            "• nam (for)\n"
            "  → *nam* (for / because) is a conjunction — gives a reason\n"
            "• dux iratus (the angry leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → *iratus* (angry) is an adjective agreeing with *dux* as both are masculine singular {T:nominative}\n"
            "• erat (was)\n"
            "  → *erat* is the imperfect 3rd person singular of *sum* (I am) — 'was'"
        ),
    },
]


# ── Set 12 (id 44): Perfect & Pluperfect (active) ───────────────────────────
SENTENCES_ACTIVE_N3 = [
    {
        "latin": "dux discessit.",
        "english": [
            "The leader left.",
            "The leader has left.",
            "The leader did leave.",
            "The leader departed.",
            "A leader left.",
        ],
        "explanation": (
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• discess{B:it} (left)\n"
            "  → *discedo* (I leave) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *discess-* is the perfect stem (from *discessi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'left'"
        ),
    },
    {
        "latin": "comes ducem suum cognovit, et laetus erat.",
        "english": [
            "The companion recognised his own leader, and was happy.",
            "The companion recognised his leader, and was happy.",
            "The companion recognised his own leader, and was glad.",
            "The companion came to know his own leader, and was happy.",
            "A companion recognised his own leader, and was happy.",
        ],
        "explanation": (
            "• comes (the companion)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• duc{T:em} suum (his own leader)\n"
            "  → *ducem* (leader) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "  → *suum* (his own) is a reflexive possessive adjective agreeing with *ducem*\n"
            "• cognov{B:it} (recognised)\n"
            "  → *cognosco* (I find out, recognise) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *cognov-* is the perfect stem (from *cognovi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'recognised'\n"
            "  → *cognosco* present/future = 'get to know'; perfect = 'know / recognise / found out'\n"
            "• laetus erat (was happy)\n"
            "  → *laetus* (happy) is an adjective, masculine singular {T:nominative}\n"
            "  → *erat* is the imperfect of *sum* (I am) — 'was'"
        ),
    },
    {
        "latin": "comes verba iam dixerat, sed milites tandem non effugerunt.",
        "english": [
            "The companion had already said the words, but the soldiers at last did not escape.",
            "The companion had already said the words, but the soldiers finally did not escape.",
            "The companion had already spoken the words, but the soldiers at last did not escape.",
            "The companion had already said the words, but the soldiers in the end did not flee.",
            "The companion had already said the words, but the soldiers eventually did not get away.",
        ],
        "explanation": (
            "• comes (the companion)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the first clause\n"
            "• iam (already)\n"
            "  → *iam* (already / now) is an adverb — flexible position; fits 'already' with the pluperfect here\n"
            "• dix{M:era}{B:t} (had said)\n"
            "  → *dico* (I say) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *dix-* is the perfect stem (from *dixi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:t}* shows it is the he/she/it form; the pluperfect means 'had done'\n"
            "• verb{T:a} (the words)\n"
            "  → *verbum* (word) is a noun, 2nd declension neuter plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second clause\n"
            "• tandem (at last)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• non effug{B:erunt} (did not escape)\n"
            "  → *non* (not) negates the verb\n"
            "  → *effugio* (I escape) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *effug-* is the perfect stem (from *effugi*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'escaped'"
        ),
    },
    {
        "latin": "solus iuvenis ducem alium sua manu occidit, et statim ex silva discessit.",
        "english": [
            "The young man alone killed another leader with his own hand, and immediately left the wood.",
            "Only the young man killed another leader with his own hand, and immediately left the wood.",
            "The young man alone slew another leader with his own hand, and immediately left the wood.",
            "The young man alone killed another leader with his own hand, and at once left the wood.",
            "Only the young man killed another leader with his own hand, and immediately departed the wood.",
            "The young man by himself killed another leader with his own hand, and immediately left the wood.",
            "The young man alone killed another leader with his hand, and immediately left the wood.",
            "Only the young man killed another leader with his hand, and at once left the wood.",
            "The lone young man killed another leader with his own hand, and immediately left the wood.",
            "The lone young man killed another leader with his hand, and immediately left the wood.",
        ],
        "explanation": (
            "• solus iuvenis (the young man alone / only the young man)\n"
            "  → *iuvenis* (young man) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → *solus* (alone / only) is an adjective agreeing with *iuvenis* as both are masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• occi{B:dit} (killed)\n"
            "  → *occido* (I kill) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *occis-* is the perfect stem (from *occidi*); note: *occidit* is identical to present 3sg — context disambiguates\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'killed'\n"
            "• ducem alium (another leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → *alium* (another) is an adjective, masculine singular {T:accusative}, agreeing with *ducem*\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• sua manu (with his own hand)\n"
            "  → *manus* (hand) is a noun, 4th declension feminine singular {T:ablative}\n"
            "  → **ablative of instrument** (NO preposition needed): 'with / by means of'\n"
            "  → *sua* (his own) is the feminine singular {T:ablative} of *suus*\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• ex silv{T:a} (out of the wood)\n"
            "  → *ex / e + ablative* = 'out of / from'\n"
            "  → *silv{T:a}* (wood) is the {T:ablative} singular\n"
            "• discess{B:it} (left)\n"
            "  → *discedo* (I leave) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *discess-* is the perfect stem (from *discessi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'left'"
        ),
    },
    {
        "latin": "regis regina suum iter facile constituerat, et comites milites coegerant.",
        "english": [
            "The king's queen had easily decided a journey, and the companions had forced the soldiers.",
            "The king's queen had easily decided her own journey, and the companions had forced the soldiers.",
            "The queen of the king had easily decided her own journey, and the companions had forced the soldiers.",
            "The king's queen had easily settled on her own journey, and the companions had forced the soldiers.",
            "The king's queen had easily decided her own journey, and the companions had compelled the soldiers.",
            "The king's queen had easily decided her journey, and the companions had forced the soldiers.",
            "The queen of the king had easily decided her journey, and the companions had compelled the soldiers.",
        ],
        "explanation": (
            "• regis regina (the king's queen)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *regis* (of the king) is the {T:genitive} singular of *rex*\n"
            "  → the {T:genitive} means 'of' — 'the queen OF the king'\n"
            "• constitu{M:era}{B:t} (had decided)\n"
            "  → *constituo* (I decide) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *constitu-* is the perfect stem (from *constitui*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:t}* shows it is the he/she/it form; the pluperfect means 'had done'\n"
            "• suum iter (her own journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → *suum* (his/her own) is an adjective, neuter singular {T:accusative}, agreeing with *iter*\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• facile (easily)\n"
            "  → *facile* is an adverb here — the neuter singular form of *facilis* used adverbially\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• comit{T:es} (the companions)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second clause\n"
            "• coeg{M:era}{B:nt} (had forced)\n"
            "  → *cogo* (I force) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *coeg-* is the perfect stem (from *coegi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:nt}* shows it is the they form; the pluperfect means 'had done'\n"
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "dea tristis iter constituerat, sed tamen non effugit.",
        "english": [
            "The sad goddess had decided on a journey, but nevertheless she did not escape.",
            "The sad goddess had decided on a route, but nevertheless she did not escape.",
            "The unhappy goddess had decided on a journey, but still she did not escape.",
            "The sad goddess had decided on a journey, but she still did not flee.",
            "The sad goddess had decided on a journey, but nevertheless she did not get away.",
        ],
        "explanation": (
            "• dea tristis (the sad goddess)\n"
            "  → *dea* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → *tristis* (sad) is an adjective agreeing with *dea* as both are feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• constitu{M:era}{B:t} (had decided)\n"
            "  → *constituo* (I decide) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *constitu-* is the perfect stem (from *constitui*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:t}* shows it is the he/she/it form; the pluperfect means 'had done'\n"
            "• iter (a journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• tamen (however)\n"
            "  → *tamen* (however / nevertheless) is a conjunction — postpositive/flexible\n"
            "• non effug{B:it} (did not escape)\n"
            "  → *non* (not) negates the verb\n"
            "  → *effugio* (I escape) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *effug-* is the perfect stem (from *effugi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense; this form is identical to present 3sg — context disambiguates\n"
            "  → the perfect tense describes a completed, single past action: 'escaped'"
        ),
    },
    {
        "latin": "simulac dux comitem conspexit, comitem petivit.",
        "english": [
            "As soon as the leader noticed the companion, the leader sought the companion.",
            "As soon as the leader caught sight of his companion, he made for the companion.",
            "As soon as the leader spotted his companion, he attacked the companion.",
            "As soon as the leader noticed his companion, he asked for the companion.",
            "As soon as the leader caught sight of his companion, he went after the companion.",
            "As soon as the leader noticed his companion, he sought the companion.",
            "As soon as the leader spotted his companion, he sought the companion.",
        ],
        "explanation": (
            "• simulac (as soon as)\n"
            "  → *simulac* (as soon as) is a temporal conjunction\n"
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of both verbs\n"
            "• conspex{B:it} (caught sight of)\n"
            "  → *conspicio* (I catch sight of) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *conspex-* is the perfect stem (from *conspexi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'caught sight of'\n"
            "• comit{T:em} (the companion)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *conspexit*\n"
            "• petiv{B:it} (sought / went after)\n"
            "  → *peto* (I seek, beg, ask, attack) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *petiv-* is the perfect stem (from *petivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'sought'\n"
            "  → *peto* = 'seek / beg / ask / attack' — context here favours 'sought' / 'made for' / 'went after'\n"
            "• comit{T:em} (the companion, again)\n"
            "  → same form, the {T:accusative} {N:object} of *petivit*"
        ),
    },
    {
        "latin": "\"ego,\" inquit regina, \"iam tandem discedere cupio; dei me cogunt!\" deinde solus comes reginam coegit.",
        "english": [
            "\"I,\" said the queen, \"now at last want to leave; the gods are forcing me!\" Then the lone companion forced the queen.",
            "\"I,\" said the queen, \"now finally want to leave; the gods are forcing me!\" Then only the companion forced the queen.",
            "\"I myself,\" said the queen, \"now at last want to leave; the gods are compelling me!\" Then only the companion forced the queen.",
            "\"I,\" said the queen, \"now at last want to leave; the gods force me!\" Then only the companion forced the queen.",
            "\"I,\" said the queen, \"now eventually want to leave; the gods are forcing me!\" Then the lone companion compelled the queen.",
        ],
        "explanation": (
            "• ego (I)\n"
            "  → *ego* (I) is an emphatic pronoun, 1st person — the verb ending already gives the {N:subject}\n"
            "• inquit (said)\n"
            "  → *inquit* (said) is a defective verb — splits direct speech, placed after the first word(s) of the quotation\n"
            "• regin{T:a} (the queen)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of *inquit*\n"
            "• iam (now)\n"
            "  → *iam* (now / already) is an adverb — flexible position\n"
            "• tandem (at last)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• cup{B:io} (I want)\n"
            "  → *cupio* (I want) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *cup-* is the stem\n"
            "  → *-{B:io}* shows it is the I form\n"
            "  → ***cupio + inf*** = 'want to ___'\n"
            "• discedere (to leave)\n"
            "  → *discedere* is the infinitive of *discedo* (I leave), 3rd conjugation\n"
            "  → the infinitive completes *cupio*: 'want TO leave'\n"
            "• de{T:i} (the gods)\n"
            "  → *deus* (god) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of *cogunt*\n"
            "• cog{B:unt} (are forcing)\n"
            "  → *cogo* (I force) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *cog-* is the stem\n"
            "  → *-{B:unt}* shows it is the they form\n"
            "• me (me)\n"
            "  → *me* is the {T:accusative} of *ego* — {N:object} of *cogunt*\n"
            "• deinde (then)\n"
            "  → *deinde* (then / next) is an adverb — flexible position\n"
            "• solus comes (the lone companion)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → *solus* (alone / only) is an adjective agreeing with *comes* as both are masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the final clause\n"
            "• coeg{B:it} (forced)\n"
            "  → *cogo* (I force) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *coeg-* is the perfect stem (from *coegi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'forced'\n"
            "• regin{T:am} (the queen)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "rex nihil acceperat, et deinde urbem petivit.",
        "english": [
            "The king had received nothing, and then made for the city.",
            "The king had accepted nothing, and then made for the city.",
            "The king had received nothing, and then sought the city.",
            "The king had received nothing, and then headed for the city.",
            "The king had received nothing, and afterwards made for the city.",
        ],
        "explanation": (
            "• rex (the king)\n"
            "  → *rex* (king) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• accep{M:era}{B:t} (had received)\n"
            "  → *accipio* (I receive, accept) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *accep-* is the perfect stem (from *accepi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:t}* shows it is the he/she/it form; the pluperfect means 'had done'\n"
            "• nihil (nothing)\n"
            "  → *nihil* (nothing) is an indeclinable noun used as {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — nothing had been received\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• deinde (then)\n"
            "  → *deinde* (then / next / afterwards) is an adverb — flexible position\n"
            "• petiv{B:it} (made for / sought)\n"
            "  → *peto* (I seek, beg, ask, attack) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *petiv-* is the perfect stem (from *petivi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'sought'\n"
            "  → *peto + acc* here = 'make for / head to' rather than 'ask for'\n"
            "• urb{T:em} (the city)\n"
            "  → *urbs* (city) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "tum miles effugere constituit, sed dux militem coegit.",
        "english": [
            "Then the soldier decided to escape, but the leader forced the soldier.",
            "Then the soldier decided to flee, but the leader forced the soldier.",
            "Then the soldier decided to get away, but the leader forced the soldier.",
            "At that time the soldier decided to escape, but the leader forced the soldier.",
            "Then the soldier decided to escape, but the leader compelled the soldier.",
        ],
        "explanation": (
            "• tum (then)\n"
            "  → *tum* (then / at that time) is an adverb — flexible position\n"
            "• miles (the soldier)\n"
            "  → *miles* (soldier) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the first clause\n"
            "• constitu{B:it} (decided)\n"
            "  → *constituo* (I decide) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *constitu-* is the perfect stem (from *constitui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'decided'\n"
            "  → ***constituo + inf*** = 'decide to ___'\n"
            "• effugere (to escape)\n"
            "  → *effugere* is the infinitive of *effugio* (I escape), 3rd conjugation (-io)\n"
            "  → the infinitive completes *constituit*: 'decided TO escape'\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second clause\n"
            "• coeg{B:it} (forced)\n"
            "  → *cogo* (I force) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *coeg-* is the perfect stem (from *coegi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'forced'\n"
            "• milit{T:em} (the soldier)\n"
            "  → *miles* (soldier) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
]


# ── Set 14 (id 46): PPP / Passive review ────────────────────────────────────
# Pluperfect passive removed throughout (out of Eduqas scope) - perfect
# passive (*PPP + est*/sunt) used instead. Ideal: 'was Xed', not 'has been Xed'.
SENTENCES_PPP_N3 = [
    {
        "latin": "iter factum est, et milites tandem discesserunt.",
        "english": [
            "The journey was made, and the soldiers finally left.",
            "The journey was made, and the soldiers at last left.",
            "The journey has been made, and the soldiers eventually left.",
            "A journey was made, and the soldiers finally left.",
            "The journey was made, and the soldiers in the end left.",
        ],
        "explanation": (
            "• iter factum est (the journey was made)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} — the thing being acted upon\n"
            "  → *factum* is the PPP of *facio*, neuter singular {T:nominative} agreeing with *iter*\n"
            "  → *est* + PPP = **perfect passive**: 'was made' / 'has been made'\n"
            "  → idiom: ***iter facere*** = 'to make a journey'; passive: 'a journey was made'\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second clause\n"
            "• tandem (at last)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• discess{B:erunt} (left)\n"
            "  → *discedo* (I leave) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *discess-* is the perfect stem (from *discessi*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'left'"
        ),
    },
    {
        "latin": "miles coactus statim discessit.",
        "english": [
            "The soldier, having been forced, immediately left.",
            "The soldier, having been forced, immediately departed.",
            "The soldier who had been forced left immediately.",
            "Once forced, the soldier immediately left.",
            "The soldier, having been forced, at once left.",
            "The soldier, having been forced, straight away left.",
            "The forced soldier immediately left.",
            "The compelled soldier immediately left.",
            "The forced soldier immediately departed.",
        ],
        "explanation": (
            "• miles coactus (the soldier, having been forced)\n"
            "  → *miles* (soldier) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → *coactus* is the PPP of *cogo*, masculine singular {T:nominative} agreeing with *miles*: 'having been forced'\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• discess{B:it} (left)\n"
            "  → *discedo* (I leave) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *discess-* is the perfect stem (from *discessi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'left'"
        ),
    },
    {
        "latin": "gladius solus positus est in silva.",
        "english": [
            "The sword alone was placed in the wood.",
            "Only the sword was placed in the wood.",
            "The sword alone has been placed in the wood.",
            "The sword alone was put in the wood.",
            "The sword alone was placed in the forest.",
        ],
        "explanation": (
            "• gladius solus (the sword alone)\n"
            "  → *gladius* (sword) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → *solus* (alone / only) is an adjective agreeing with *gladius* as both are masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} — the thing being acted upon\n"
            "• positus est (was placed)\n"
            "  → *positus* is the PPP of *pono*, masculine singular {T:nominative} agreeing with *gladius*\n"
            "  → *est* + PPP = **perfect passive**: 'was placed' / 'was put'\n"
            "• in silv{T:a} (in the wood)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *silv{T:a}* (wood) is the {T:ablative} singular"
        ),
    },
    {
        "latin": "ducem occisum pater conspexit.",
        "english": [
            "The father noticed the leader, having been killed.",
            "The father caught sight of the leader, having been killed.",
            "The father spotted the leader, having been killed.",
            "The father noticed the leader who had been killed.",
            "The father caught sight of the leader who had been slain.",
            "The father noticed the killed leader.",
            "The father noticed the slain leader.",
            "The father caught sight of the killed leader.",
            "The father spotted the slain leader.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• conspex{B:it} (caught sight of)\n"
            "  → *conspicio* (I catch sight of) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *conspex-* is the perfect stem (from *conspexi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'caught sight of'\n"
            "• ducem occisum (the leader, having been killed)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → *occisum* is the PPP of *occido*, masculine singular {T:accusative} agreeing with *ducem*: 'having been killed'\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb"
        ),
    },
    {
        "latin": "iter facile constitutum est, sed milites non discesserunt.",
        "english": [
            "The easy journey was decided, but the soldiers did not leave.",
            "An easy journey was decided, but the soldiers did not leave.",
            "The easy journey was settled, but the soldiers did not leave.",
            "The easy journey has been decided, but the soldiers did not leave.",
            "The easy journey was decided, but the soldiers did not depart.",
        ],
        "explanation": (
            "• iter facile (the easy journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:nominative}\n"
            "  → *facile* is the neuter singular nominative of the adjective *facilis* (NOT the adverb here), agreeing with *iter*\n"
            "  → the {T:nominative} is the {N:subject} — the thing being acted upon\n"
            "• constitutum est (was decided)\n"
            "  → *constitutum* is the PPP of *constituo*, neuter singular {T:nominative} agreeing with *iter*\n"
            "  → *est* + PPP = **perfect passive**: 'was decided'\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second clause\n"
            "• non discess{B:erunt} (did not leave)\n"
            "  → *non* (not) negates the verb\n"
            "  → *discedo* (I leave) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *discess-* is the perfect stem (from *discessi*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'left'"
        ),
    },
    {
        "latin": "regina relicta in insula discedere cupiebat; nihil enim acceperat.",
        "english": [
            "The queen, having been left behind on the island, was wanting to leave; for she had received nothing.",
            "The queen, having been left behind on the island, was wanting to depart; for she had received nothing.",
            "The queen, having been abandoned on the island, wanted to leave; for she had received nothing.",
            "The queen who had been left behind on the island was wanting to leave; for she had received nothing.",
            "The queen, having been left behind on the island, was wishing to leave; because she had received nothing.",
            "The abandoned queen on the island was wanting to leave; for she had received nothing.",
            "The left-behind queen on the island was wanting to leave; for she had received nothing.",
            "The queen left behind on the island was wanting to leave; for she had received nothing.",
            "The queen, having been abandoned on the island, was wanting to depart; for she had received nothing.",
            "The abandoned queen on the island wanted to leave; because she had received nothing.",
        ],
        "explanation": (
            "• regina relicta (the queen, having been left behind)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → *relicta* is the PPP of *relinquo*, feminine singular {T:nominative} agreeing with *regina*: 'having been left behind'\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• in insul{T:a} (on the island)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *insul{T:a}* (island) is the {T:ablative} singular\n"
            "• cup{P:ieba}{B:t} (was wanting)\n"
            "  → *cupio* (I want) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *cup-* is the stem\n"
            "  → *-{P:ieba}-* is the imperfect marker — 3rd-io uses *-ieba-* not *-eba-*\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was wanting' or 'used to want'\n"
            "  → ***cupio + inf*** = 'want to ___'\n"
            "• discedere (to leave)\n"
            "  → *discedere* is the infinitive of *discedo* (I leave), 3rd conjugation\n"
            "  → the infinitive completes *cupiebat*: 'was wanting TO leave'\n"
            "• enim (for)\n"
            "  → *enim* (for / because) is a conjunction — postpositive (2nd word of its clause)\n"
            "• accep{M:era}{B:t} (had received)\n"
            "  → *accipio* (I receive, accept) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *accep-* is the perfect stem (from *accepi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:t}* shows it is the he/she/it form; the pluperfect means 'had done'\n"
            "• nihil (nothing)\n"
            "  → *nihil* (nothing) is an indeclinable noun used as {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — nothing had been received"
        ),
    },
    {
        "latin": "comes conspectus statim effugit.",
        "english": [
            "The companion, having been noticed, immediately escaped.",
            "The companion, having been noticed, immediately escaped.",
            "The companion who had been spotted escaped immediately.",
            "Once spotted, the companion immediately escaped.",
            "The companion, having been spotted, immediately fled.",
            "The companion, having been spotted, immediately got away.",
        ],
        "explanation": (
            "• comes conspectus (the companion, having been spotted)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → *conspectus* is the PPP of *conspicio*, masculine singular {T:nominative} agreeing with *comes*: 'having been spotted'\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• effug{B:it} (escaped)\n"
            "  → *effugio* (I escape) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *effug-* is the perfect stem (from *effugi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense; this form is identical to present 3sg — context disambiguates\n"
            "  → the perfect tense describes a completed, single past action: 'escaped'"
        ),
    },
    {
        "latin": "filius quaesitus a patre tandem cognitus est.",
        "english": [
            "The son, having been searched for by the father, was at last found out.",
            "The son, having been sought by the father, was finally recognised.",
            "The son, having been searched for by the father, was at last recognised.",
            "The son who had been searched for by the father was finally recognised.",
            "The son, searched for by the father, was finally found out.",
            "The son, having been searched for by the father, has finally been recognised.",
        ],
        "explanation": (
            "• filius quaesitus (the son, having been searched for)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → *quaesitus* is the PPP of *quaero*, masculine singular {T:nominative} agreeing with *filius*: 'having been searched for / sought'\n"
            "  → the {T:nominative} is the {N:subject} — the thing being acted upon\n"
            "• a patre (by the father)\n"
            "  → *a/ab + ablative* with persons = 'by' (**agent of a passive verb**)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:ablative}\n"
            "• tandem (at last)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• cognitus est (was recognised / found out)\n"
            "  → *cognitus* is the PPP of *cognosco*, masculine singular {T:nominative} agreeing with *filius*\n"
            "  → *est* + PPP = **perfect passive**: 'was recognised' / 'was found out'"
        ),
    },
    {
        "latin": "verbum dirum a deo dictum est, et dux statim cognovit.",
        "english": [
            "A dreadful word was said by a god, and the leader immediately found out.",
            "A dreadful word was said by a god, and the leader immediately found out.",
            "A terrible word was spoken by a god, and the leader immediately recognised it.",
            "A dire word was said by a god, and the leader immediately got to know.",
            "An awful word was spoken by a god, and the leader at once found out.",
            "A dreadful word has been spoken by a god, and the leader immediately found out.",
        ],
        "explanation": (
            "• verbum dirum (a dreadful word)\n"
            "  → *verbum* (word) is a noun, 2nd declension neuter singular {T:nominative}\n"
            "  → *dirum* (dreadful) is an adjective agreeing with *verbum* as both are neuter singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} — the thing being acted upon\n"
            "• a deo (by a god)\n"
            "  → *a/ab + ablative* with persons = 'by' (agent of a passive verb)\n"
            "  → *deus* (god) is a noun, 2nd declension masculine singular {T:ablative}\n"
            "• dictum est (was said)\n"
            "  → *dictum* is the PPP of *dico*, neuter singular {T:nominative} agreeing with *verbum*\n"
            "  → *est* + PPP = **perfect passive**: 'was said' / 'was spoken'\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second clause\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• cognov{B:it} (found out)\n"
            "  → *cognosco* (I find out, recognise) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *cognov-* is the perfect stem (from *cognovi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'found out'"
        ),
    },
    {
        "latin": "iuvenis petitus effugere constituit, et cum comitibus discessit.",
        "english": [
            "The young man, having been sought, decided to escape, and left with the companions.",
            "The young man, having been sought, decided to escape, and left with his companions.",
            "The young man, having been attacked, decided to escape, and left with his companions.",
            "The young man who had been sought decided to escape, and left with his companions.",
            "The young man, having been sought, decided to flee, and left with his companions.",
            "The young man, having been sought, decided to get away, and departed with his companions.",
        ],
        "explanation": (
            "• iuvenis petitus (the young man, having been sought)\n"
            "  → *iuvenis* (young man) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → *petitus* is the PPP of *peto*, masculine singular {T:nominative} agreeing with *iuvenis*: 'having been sought / attacked'\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• constitu{B:it} (decided)\n"
            "  → *constituo* (I decide) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *constitu-* is the perfect stem (from *constitui*); this form is ambiguous (could be present or perfect) — narrative context = 'decided'\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → ***constituo + inf*** = 'decide to ___'\n"
            "• effugere (to escape)\n"
            "  → *effugere* is the infinitive of *effugio* (I escape), 3rd conjugation (-io)\n"
            "  → the infinitive completes *constituit*: 'decided TO escape'\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• cum comitibus (with the companions)\n"
            "  → *cum + ablative* = 'with'\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine plural {T:ablative}\n"
            "• discess{B:it} (left)\n"
            "  → *discedo* (I leave) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *discess-* is the perfect stem (from *discessi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'left'"
        ),
    },
]


# ── Set 16 (id 48): Exam-level mixed review ─────────────────────────────────
SENTENCES_REVIEW_N3 = [
    {
        "latin": "dux fortis, postquam milites coegerat, cum suis comitibus ad urbem iter facile fecit.",
        "english": [
            "The brave leader, after he had forced the soldiers, easily made a journey to the city with his own companions.",
            "The strong leader, after he had forced the soldiers, easily made a journey to the city with his own companions.",
            "The brave leader, after he had forced the soldiers, easily travelled to the city with his own companions.",
            "The brave leader, after he had forced the soldiers, easily made a journey towards the city with his own companions.",
            "The brave leader, after he had forced the soldiers, easily made a journey to the city with his companions.",
            "The brave leader, after he had forced the soldiers, easily went on a journey to the city with his own companions.",
        ],
        "explanation": (
            "• dux fortis (the brave leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → *fortis* (brave / strong) is an adjective agreeing with *dux* as both are masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• postquam (after)\n"
            "  → *postquam* (after) is a temporal conjunction — *postquam + pluperfect* = 'after he had ___ed'\n"
            "• coeg{M:era}{B:t} (had forced)\n"
            "  → *cogo* (I force) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *coeg-* is the perfect stem (from *coegi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:t}* shows it is the he/she/it form; the pluperfect means 'had done'\n"
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *coegerat*\n"
            "• fec{B:it} (made)\n"
            "  → *facio* (I make, do) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *fec-* is the perfect stem (from *feci*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'made'\n"
            "• iter (a journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *fecit*\n"
            "• facile (easily)\n"
            "  → *facile* is an adverb here — flexible position\n"
            "  → ***iter facere*** idiom = 'to make a journey' / 'to travel'\n"
            "• cum suis comitibus (with his own companions)\n"
            "  → *cum + ablative* = 'with'\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine plural {T:ablative}\n"
            "  → *suis* (his own) is an adjective agreeing with *comitibus*\n"
            "• ad urbem (to the city)\n"
            "  → *ad + accusative* = 'to' (direction)\n"
            "  → *urb{T:em}* (city) is the {T:accusative} singular"
        ),
    },
    {
        "latin": "solus miles alia verba dixerat, sed dux nihil acceperat.",
        "english": [
            "The lonely soldier had said other words, but the leader had received nothing.",
            "The lone soldier had said other words, but the leader had received nothing.",
            "Only the soldier had spoken other words, but the leader had received nothing.",
            "The lonely soldier had said different words, but the leader had received nothing.",
            "Only the soldier had said other words, but the leader had accepted nothing.",
        ],
        "explanation": (
            "• solus miles (the lonely soldier / only the soldier)\n"
            "  → *miles* (soldier) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → *solus* (alone / only / lonely) is an adjective agreeing with *miles* as both are masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the first clause\n"
            "• dix{M:era}{B:t} (had said)\n"
            "  → *dico* (I say) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *dix-* is the perfect stem (from *dixi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:t}* shows it is the he/she/it form; the pluperfect means 'had done'\n"
            "• alia verba (other words)\n"
            "  → *verbum* (word) is a noun, 2nd declension neuter plural {T:accusative}\n"
            "  → *alia* (other) is an adjective, neuter plural {T:accusative}, agreeing with *verba*\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second clause\n"
            "• accep{M:era}{B:t} (had received)\n"
            "  → *accipio* (I receive, accept) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *accep-* is the perfect stem (from *accepi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:t}* shows it is the he/she/it form; the pluperfect means 'had done'\n"
            "• nihil (nothing)\n"
            "  → *nihil* (nothing) is an indeclinable noun used as {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — nothing had been received"
        ),
    },
    {
        "latin": "regina filium ductum a milite iam conspexit, et statim filium petere cupiebat.",
        "english": [
            "The queen now noticed the son, having been led by a soldier, and immediately wanted to seek the son.",
            "The queen now caught sight of her son, having been led by a soldier, and immediately wanted to seek her son.",
            "The queen now spotted her son, having been led by a soldier, and immediately wanted to go to her son.",
            "The queen already caught sight of her son, having been led by a soldier, and immediately wanted to make for her son.",
            "The queen now noticed her son, having been led by a soldier, and immediately wanted to head for her son.",
        ],
        "explanation": (
            "• regin{T:a} (the queen)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• iam (now)\n"
            "  → *iam* (now / already) is an adverb — flexible position\n"
            "• conspex{B:it} (caught sight of)\n"
            "  → *conspicio* (I catch sight of) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *conspex-* is the perfect stem (from *conspexi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'caught sight of'\n"
            "• filium ductum (the son, having been led)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → *ductum* is the PPP of *duco*, masculine singular {T:accusative} agreeing with *filium*: 'having been led'\n"
            "  → the {T:accusative} is the {N:object} of *conspexit*\n"
            "• a milite (by a soldier)\n"
            "  → *a/ab + ablative* with persons = 'by' (**agent of a passive**) — here used with the PPP *ductum*\n"
            "  → *miles* (soldier) is a noun, 3rd declension masculine singular {T:ablative}\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• cup{P:ieba}{B:t} (was wanting)\n"
            "  → *cupio* (I want) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *cup-* is the stem\n"
            "  → *-{P:ieba}-* is the imperfect marker — 3rd-io uses *-ieba-* not *-eba-*\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was wanting' or 'used to want'\n"
            "  → ***cupio + inf*** = 'want to ___'\n"
            "• petere (to seek / to make for)\n"
            "  → *petere* is the infinitive of *peto* (I seek, beg, ask, attack), 3rd conjugation\n"
            "  → the infinitive completes *cupiebat*: 'was wanting TO seek'\n"
            "• fili{T:um} (the son, again)\n"
            "  → same form, the {T:accusative} {N:object} of *petere*"
        ),
    },
    {
        "latin": "simulac comes ducis ingentem navem conspexit, \"ad insulam,\" inquit, \"iter facimus!\"",
        "english": [
            "As soon as the companion of the leader noticed the huge ship, \"We are making a journey to the island,\" he said.",
            "As soon as the leader's companion caught sight of the huge ship, \"We are making a journey to the island,\" he said.",
            "As soon as the companion of the leader spotted the enormous ship, \"We are making a journey to the island,\" he said.",
            "As soon as the companion of the leader noticed the vast ship, \"We are making a journey towards the island,\" he said.",
            "As soon as the companion of the leader caught sight of the huge ship, \"We are travelling to the island,\" he said.",
        ],
        "explanation": (
            "• simulac (as soon as)\n"
            "  → *simulac* (as soon as) is a temporal conjunction\n"
            "• comes ducis (the companion of the leader)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *ducis* (of the leader) is the {T:genitive} singular of *dux*\n"
            "  → the {T:genitive} means 'of' — 'the companion OF the leader'\n"
            "• conspex{B:it} (caught sight of)\n"
            "  → *conspicio* (I catch sight of) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *conspex-* is the perfect stem (from *conspexi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'caught sight of'\n"
            "• ingent{T:em} nav{T:em} (the huge ship)\n"
            "  → *navis* (ship) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "  → *ingentem* (huge) is an adjective agreeing with *navem* as both are feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• inquit (he said)\n"
            "  → *inquit* (said) is a defective verb — splits direct speech, placed after the first word(s)\n"
            "• fac{B:imus} (we are making)\n"
            "  → *facio* (I make, do) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *fac-* is the stem\n"
            "  → *-{B:imus}* shows it is the we form\n"
            "• iter (a journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object}\n"
            "  → ***iter facere*** idiom = 'to make a journey' / 'to travel'\n"
            "• ad insulam (to the island)\n"
            "  → *ad + accusative* = 'to' (direction)\n"
            "  → *insul{T:am}* (island) is the {T:accusative} singular"
        ),
    },
    {
        "latin": "pater cum filio discedere cupiebat, sed filius in silva nunc dixit: \"pater me relinquit!\"",
        "english": [
            "The father wanted to leave with the son, but the son now said in the wood: \"The father is leaving me behind!\"",
            "The father wanted to leave with his son, but the son now said in the wood: \"The father is leaving me behind!\"",
            "The father wanted to depart with his son, but the son now said in the wood: \"The father is abandoning me!\"",
            "The father wanted to leave with his son, but the son now said in the forest: \"The father leaves me behind!\"",
            "The father was wanting to leave with his son, but the son now said in the wood: \"The father is leaving me behind!\"",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the main clause\n"
            "• cup{P:ieba}{B:t} (was wanting)\n"
            "  → *cupio* (I want) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *cup-* is the stem\n"
            "  → *-{P:ieba}-* is the imperfect marker — 3rd-io uses *-ieba-* not *-eba-*\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was wanting' or 'used to want'\n"
            "  → ***cupio + inf*** = 'want to ___'\n"
            "• discedere (to leave)\n"
            "  → *discedere* is the infinitive of *discedo* (I leave), 3rd conjugation\n"
            "  → the infinitive completes *cupiebat*: 'was wanting TO leave'\n"
            "• cum filio (with the son)\n"
            "  → *cum + ablative* = 'with'\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:ablative}\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• filius (the son)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second clause\n"
            "• in silv{T:a} (in the wood)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *silv{T:a}* (wood) is the {T:ablative} singular\n"
            "• nunc (now)\n"
            "  → *nunc* (now) is an adverb — flexible position\n"
            "• dix{B:it} (said)\n"
            "  → *dico* (I say) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *dix-* is the perfect stem (from *dixi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'said'\n"
            "• relinqu{B:it} (is leaving behind)\n"
            "  → *relinquo* (I leave behind) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *relinqu-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form — present tense, within the direct speech\n"
            "• me (me)\n"
            "  → *me* is the accusative singular of *ego* — {N:object} of *relinquit*"
        ),
    },
    {
        "latin": "deinde omnes milites reginam petiverunt, et reginam in navem posuerunt.",
        "english": [
            "Then all the soldiers sought the queen, and placed the queen into the ship.",
            "Then all the soldiers made for the queen, and placed the queen onto the ship.",
            "Next all the soldiers went after the queen, and put the queen into the ship.",
            "Then all of the soldiers attacked the queen, and placed the queen into the ship.",
            "Then all the soldiers sought the queen, and put her into the ship.",
        ],
        "explanation": (
            "• deinde (then)\n"
            "  → *deinde* (then / next) is an adverb — flexible position\n"
            "• omnes milit{T:es} (all the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → *omnes* (all) is an adjective agreeing with *milites* as both are masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• petiv{B:erunt} (sought)\n"
            "  → *peto* (I seek, beg, ask, attack) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *petiv-* is the perfect stem (from *petivi*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'sought'\n"
            "  → *peto* = 'seek / beg / ask / attack' — here 'sought' / 'made for'\n"
            "• regin{T:am} (the queen)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *petiverunt*\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• posu{B:erunt} (placed)\n"
            "  → *pono* (I put, place) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *posu-* is the perfect stem (from *posui*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'placed'\n"
            "• regin{T:am} (the queen, again)\n"
            "  → same form, the {T:accusative} {N:object} of *posuerunt*\n"
            "• in navem (into the ship)\n"
            "  → *in + accusative* = 'into' (motion towards)\n"
            "  → *nav{T:em}* (ship) is the {T:accusative} singular"
        ),
    },
    {
        "latin": "dea diram mortem cupiverat; tandem suum filium reliquit et discessit.",
        "english": [
            "The goddess had wanted a dreadful death; finally she left behind her own son and left.",
            "The goddess had desired a dreadful death; finally she left her own son behind and departed.",
            "The goddess had wanted a terrible death; at last she left behind her own son and left.",
            "The goddess had wanted a dire death; eventually she left her own son behind and left.",
            "The goddess had wanted an awful death; finally she abandoned her own son and left.",
            "The goddess had wanted a dreadful death; in the end she left her own son behind and went away.",
        ],
        "explanation": (
            "• de{T:a} (the goddess)\n"
            "  → *dea* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does all three verbs\n"
            "• cupiv{M:era}{B:t} (had wanted)\n"
            "  → *cupio* (I want) is the dictionary form of this verb, 3rd conjugation (-io)\n"
            "  → *cupiv-* is the perfect stem (from *cupivi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:t}* shows it is the he/she/it form; the pluperfect means 'had done'\n"
            "• diram mortem (a dreadful death)\n"
            "  → *mors* (death) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "  → *diram* (dreadful) is an adjective agreeing with *mortem* as both are feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *cupiverat*\n"
            "• tandem (finally)\n"
            "  → *tandem* (finally / at last) is an adverb — flexible position\n"
            "• reliqu{B:it} (left behind)\n"
            "  → *relinquo* (I leave behind) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *reliqu-* is the perfect stem (from *reliqui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'left behind'\n"
            "• suum filium (her own son)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → *suum* (his/her own) is an adjective, masculine singular {T:accusative}, agreeing with *filium*\n"
            "  → the {T:accusative} is the {N:object} of *reliquit*\n"
            "• et (and)\n"
            "  → *et* (and) is a conjunction — joins the two clauses\n"
            "• discess{B:it} (left)\n"
            "  → *discedo* (I leave) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *discess-* is the perfect stem (from *discessi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'left'"
        ),
    },
    {
        "latin": "dux iam milites cogit; deinde \"nunc,\" inquit, \"discedere constituo.\"",
        "english": [
            "The leader is now forcing the soldiers; then \"now,\" he said, \"I decide to leave.\"",
            "The leader now forces the soldiers; then \"now,\" he said, \"I decide to leave.\"",
            "The leader is already forcing the soldiers; next \"now,\" he said, \"I decide to leave.\"",
            "The leader is now forcing the soldiers; then \"now,\" he says, \"I decide to leave.\"",
            "The leader is now forcing the soldiers; then \"now,\" he said, \"I am deciding to leave.\"",
        ],
        "explanation": (
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• iam (now)\n"
            "  → *iam* (now / already) is an adverb — flexible position\n"
            "• cog{B:it} (is forcing / forces)\n"
            "  → *cogo* (I force) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *cog-* is the stem\n"
            "  → *-{B:it}* shows it is the he/she/it form — historic present (Latin narrative often uses present where English uses past)\n"
            "• milit{T:es} (the soldiers)\n"
            "  → *milites* (soldiers) is a noun, 3rd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "• deinde (then)\n"
            "  → *deinde* (then / next) is an adverb — flexible position\n"
            "• nunc (now)\n"
            "  → *nunc* (now) is an adverb — flexible position (within the direct speech)\n"
            "• inquit (he said)\n"
            "  → *inquit* (said) is a defective verb — splits direct speech, placed after the first word(s)\n"
            "• constitu{B:o} (I decide)\n"
            "  → *constituo* (I decide) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *constitu-* is the stem\n"
            "  → *-{B:o}* shows it is the I form\n"
            "  → ***constituo + inf*** = 'decide to ___'\n"
            "• discedere (to leave)\n"
            "  → *discedere* is the infinitive of *discedo* (I leave), 3rd conjugation\n"
            "  → the infinitive completes *constituo*: 'decide TO leave'"
        ),
    },
    {
        "latin": "filius regis patrem quaesiverat, sed tandem per silvam solus discessit.",
        "english": [
            "The son of the king had searched for the father, but finally he left through the wood alone.",
            "The king's son had searched for his father, but finally he left through the wood alone.",
            "The son of the king had asked for his father, but at last he left through the forest alone.",
            "The son of the king had looked for his father, but eventually he departed through the wood alone.",
            "The son of the king had searched for his father, but finally he left alone through the wood.",
        ],
        "explanation": (
            "• filius regis (the son of the king)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "  → *regis* (of the king) is the {T:genitive} singular of *rex*\n"
            "  → the {T:genitive} means 'of' — 'the son OF the king'\n"
            "• quaesiv{M:era}{B:t} (had searched for)\n"
            "  → *quaero* (I search, ask for) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *quaesiv-* is the perfect stem (from *quaesivi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:t}* shows it is the he/she/it form; the pluperfect means 'had done'\n"
            "• patr{T:em} (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *quaesiverat*\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• tandem (at last)\n"
            "  → *tandem* (at last / finally) is an adverb — flexible position\n"
            "• per silv{T:am} (through the wood)\n"
            "  → *per + accusative* = through\n"
            "  → *silv{T:am}* (wood) is the {T:accusative} singular\n"
            "• solus (alone)\n"
            "  → *solus* (alone / only) is an adjective, masculine singular {T:nominative} agreeing with the implicit {N:subject} ('he')\n"
            "• discess{B:it} (left)\n"
            "  → *discedo* (I leave) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *discess-* is the perfect stem (from *discessi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'left'"
        ),
    },
    {
        "latin": "omnes comites tum dixerant: \"dux iter facile constituit!\" sed dirum erat iter.",
        "english": [
            "All the companions had then said: \"The leader has decided an easy journey!\" but the journey was dreadful.",
            "All of the companions had then said: \"The leader has decided an easy journey!\" but the journey was dreadful.",
            "All the companions had at that time said: \"The leader has decided an easy journey!\" but the journey was terrible.",
            "All the companions had then spoken: \"The leader has decided an easy journey!\" but the journey was dire.",
            "All the companions had then said: \"The leader has settled on an easy journey!\" but the journey was dreadful.",
        ],
        "explanation": (
            "• omnes comit{T:es} (all the companions)\n"
            "  → *comes* (companion) is a noun, 3rd declension masculine plural {T:nominative}\n"
            "  → *omnes* (all) is an adjective agreeing with *comites* as both are masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• tum (then)\n"
            "  → *tum* (then / at that time) is an adverb — flexible position\n"
            "• dix{M:era}{B:nt} (had said)\n"
            "  → *dico* (I say) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *dix-* is the perfect stem (from *dixi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:nt}* shows it is the they form; the pluperfect means 'had done'\n"
            "• dux (the leader)\n"
            "  → *dux* (leader) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the quoted clause (within the direct speech)\n"
            "• constitu{B:it} (has decided)\n"
            "  → *constituo* (I decide) is the dictionary form of this verb, 3rd conjugation\n"
            "  → *constitu-* is the perfect stem (from *constitui*); this form is ambiguous — perfect from context\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "• iter facile (an easy journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:accusative}\n"
            "  → *facile* is the neuter singular accusative of the adjective *facilis* (NOT the adverb here), agreeing with *iter*\n"
            "  → the {T:accusative} is the {N:object} of *constituit*\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast\n"
            "• erat (was)\n"
            "  → *erat* is the imperfect 3rd person singular of *sum* (I am) — 'was'\n"
            "• dirum iter (the dreadful journey)\n"
            "  → *iter* (journey) is a noun, 3rd declension neuter singular {T:nominative}\n"
            "  → *dirum* (dreadful) is an adjective agreeing with *iter* as both are neuter singular {T:nominative}\n"
            "  → the {T:nominative} is the predicate subject of the second clause"
        ),
    },
]


# ════════════════════════════════════════════════════════════════════════════
# SETS_N3 — exactly 16 tile entries for Node 3, mirroring Node 2 exactly.
# Set ids continue from Node 2's last id (36). Node 3 ids: 37-52.
# ════════════════════════════════════════════════════════════════════════════

# Table note for the 3rd conjugation present tense tile.
PRESENT_TABLE_NOTE_3RD = (
    "Colour key: **red** = stem vowel  |  **blue** = person ending\n\n"
    "Note: the *I* form has no stem vowel (*duco*, not *duci*; *cupio*, not *cupuo*)."
)


# ── translate_form question generators ──────────────────────────────────────
# Each verb -> 6 forms x 1 ending pattern. Mirrors Node 2's generators but
# adapted to 3rd-conjugation patterns (incl. the -io subset).

def _make_3sg_part(phrase):
    """Apply English 3rd-sg rule to ONE verb phrase, preserving any trailing
    particle or parenthetical.  e.g. 'ask (for)' -> 'asks (for)',
    'leave behind' -> 'leaves behind', 'search' -> 'searches'."""
    # Split verb from any trailing text (parenthetical or particle words)
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

def _verbset_eng(eng_present):
    """Given 'I search, ask (for)' -> six person/number translations with
    correct 3sg form: 'he/she searches, asks (for)'."""
    base = eng_present[2:]  # strip "I "
    # Irregular whole-phrase shortcuts (multi-meaning special cases)
    irreg_whole = {"make, do": "makes, does"}
    if base in irreg_whole:
        third = irreg_whole[base]
    elif "," in base:
        # Comma-separated multi-meaning: apply 3sg rule to each part
        parts = [p.strip() for p in base.split(",")]
        third = ", ".join(_make_3sg_part(p) for p in parts)
    else:
        third = _make_3sg_part(base)
    return [f"I {base}", f"you (sg) {base}", f"he/she {third}",
            f"we {base}", f"you (pl) {base}", f"they {base}"]

def _opts_present(eng_present):  return _verbset_eng(eng_present)

def _make_gerund(phrase):
    """Return the gerund of the first word of a phrase, preserving any tail.
    e.g. 'leave behind' -> 'leaving behind', 'put' -> 'putting', 'make' -> 'making'."""
    words = phrase.strip().split()
    first, tail = words[0], " ".join(words[1:])
    VOWELS = "aeiou"
    if first.endswith("ie"):
        stem = first[:-2] + "ying"
    elif first.endswith("e") and len(first) > 2 and first[-2] not in VOWELS:
        stem = first[:-1] + "ing"
    elif (len(first) >= 3
          and first[-1] not in VOWELS + "wxy"
          and first[-2] in VOWELS
          and first[-3] not in VOWELS):
        # CVC pattern with single-syllable word → double final consonant
        stem = first + first[-1] + "ing"
    else:
        stem = first + "ing"
    return (stem + " " + tail).strip() if tail else stem

def _opts_imperf(eng_present):
    base = eng_present[2:]  # strip "I "
    # For compound glosses like "put, place" → gerund each part, join with " / "; cap at 2
    parts = [p.strip() for p in base.split(",")][:2]
    ger_parts = [_make_gerund(p) for p in parts]
    ger = " / ".join(ger_parts)
    return [f"I was {ger}", f"you (sg) were {ger}", f"he/she was {ger}",
            f"we were {ger}", f"you (pl) were {ger}", f"they were {ger}"]

def _opts_future(eng_present):
    base = eng_present[2:]
    return [f"I will {base}", f"you (sg) will {base}", f"he/she will {base}",
            f"we will {base}", f"you (pl) will {base}", f"they will {base}"]

def _opts_perfect(eng_perfect):
    base = eng_perfect[2:]  # strip "I "
    return [f"I {base}", f"you (sg) {base}", f"he/she {base}",
            f"we {base}", f"you (pl) {base}", f"they {base}"]

def _opts_pluperf(eng_perfect):
    # pluperfect -> "had X-ed". Use a small map for 3rd-conj past participles.
    PAST_PARTICIPLE = {
        "led":"led", "said":"said", "put, placed":"put, placed",
        "sought, begged, asked, attacked":"sought, begged, asked, attacked",
        "searched, asked (for)":"searched, asked for",
        "left behind":"left behind", "left":"left",
        "decided":"decided", "forced":"forced",
        "wanted":"wanted", "made, did":"made, done", "escaped":"escaped",
    }
    base = eng_perfect[2:]
    pp = PAST_PARTICIPLE.get(base, base)
    return [f"I had {pp}", f"you (sg) had {pp}", f"he/she had {pp}",
            f"we had {pp}", f"you (pl) had {pp}", f"they had {pp}"]


# Stem extraction: drop final 'o' for plain 3rd; drop 'io' for -io subset.
def _is_io(verb):
    pres = verb[0]
    return pres.endswith("io")

def _present_stem(verb):
    pres = verb[0]
    return pres[:-2] if _is_io(verb) else pres[:-1]


def _gen_present(verb):
    pres = verb[0]; eng = verb[4]
    s = _present_stem(verb)
    if _is_io(verb):
        # capio, capis, capit, capimus, capitis, capiunt
        forms = [s+"io", s+"is", s+"it", s+"imus", s+"itis", s+"iunt"]
    else:
        # duco, ducis, ducit, ducimus, ducitis, ducunt
        forms = [s+"o", s+"is", s+"it", s+"imus", s+"itis", s+"unt"]
    eng_set = _opts_present(eng)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]

def _gen_imperfect(verb):
    eng = verb[4]
    s = _present_stem(verb)
    if _is_io(verb):
        # capiebam, capiebas, capiebat, capiebamus, capiebatis, capiebant
        forms = [s+"iebam", s+"iebas", s+"iebat", s+"iebamus", s+"iebatis", s+"iebant"]
    else:
        forms = [s+"ebam", s+"ebas", s+"ebat", s+"ebamus", s+"ebatis", s+"ebant"]
    eng_set = _opts_imperf(eng)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]

def _gen_future(verb):
    eng = verb[4]
    s = _present_stem(verb)
    if _is_io(verb):
        # capiam, capies, capiet, capiemus, capietis, capient
        forms = [s+"iam", s+"ies", s+"iet", s+"iemus", s+"ietis", s+"ient"]
    else:
        # ducam, duces, ducet, ducemus, ducetis, ducent
        forms = [s+"am", s+"es", s+"et", s+"emus", s+"etis", s+"ent"]
    eng_set = _opts_future(eng)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]

def _gen_perfect(verb):
    perf = verb[2]; eng_perf = verb[6]
    p = perf[:-1]  # drop final i
    forms = [perf, p+"isti", p+"it", p+"imus", p+"istis", p+"erunt"]
    eng_set = _opts_perfect(eng_perf)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]

def _gen_pluperf(verb):
    perf = verb[2]; eng_perf = verb[6]
    p = perf[:-1]
    forms = [p+"eram", p+"eras", p+"erat", p+"eramus", p+"eratis", p+"erant"]
    eng_set = _opts_pluperf(eng_perf)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]

QUESTIONS_PRESENT_N3    = [q for v in VERBS_3RD_TOP150 for q in _gen_present(v)]
QUESTIONS_IMPERFECT_N3  = [q for v in VERBS_3RD_TOP150 for q in _gen_imperfect(v)]
QUESTIONS_FUTURE_N3     = [q for v in VERBS_3RD_TOP150 for q in _gen_future(v)]
QUESTIONS_PERFECT_N3    = [q for v in VERBS_3RD_TOP150 for q in _gen_perfect(v)]
QUESTIONS_PLUPERFECT_N3 = [q for v in VERBS_3RD_TOP150 for q in _gen_pluperf(v)]


# ── Conjugation tables (translate_form intro screens) ─────────────────────────
# Lead with 'duco' (most regular 3rd-conj exemplar).

TABLE_PRESENT_3RD = [
    {"conjugation":"I",            "infinitive_ending":"-o",  "example":"duco",     "ep":[["duc",""],["o","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-s",  "example":"ducis",    "ep":[["duc",""],["i","coral"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-t",  "example":"ducit",    "ep":[["duc",""],["i","coral"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-mus","example":"ducimus",  "ep":[["duc",""],["i","coral"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-tis","example":"ducitis",  "ep":[["duc",""],["i","coral"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-nt", "example":"ducunt",   "ep":[["duc",""],["u","coral"],["nt","blue"]]},
]

TABLE_PRESENT_3RD_IO = [
    {"conjugation":"I",            "infinitive_ending":"-io",  "example":"cupio",    "ep":[["cup",""],["io","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-is",  "example":"cupis",    "ep":[["cup",""],["i","coral"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-it",  "example":"cupit",    "ep":[["cup",""],["i","coral"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-imus","example":"cupimus",  "ep":[["cup",""],["i","coral"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-itis","example":"cupitis",  "ep":[["cup",""],["i","coral"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-iunt","example":"cupiunt",  "ep":[["cup",""],["i","coral"],["unt","blue"]]},
]

TABLE_IMPERFECT_3RD = [
    {"conjugation":"I",            "infinitive_ending":"-ebam",  "example":"ducebam",  "tr":"I was leading",      "ep":[["duc",""],["e","coral"],["ba","purple"],["m","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-ebas",  "example":"ducebas",  "tr":"you were leading",   "ep":[["duc",""],["e","coral"],["ba","purple"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-ebat",  "example":"ducebat",  "tr":"he/she was leading", "ep":[["duc",""],["e","coral"],["ba","purple"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-ebamus","example":"ducebamus","tr":"we were leading",    "ep":[["duc",""],["e","coral"],["ba","purple"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-ebatis","example":"ducebatis","tr":"you were leading",   "ep":[["duc",""],["e","coral"],["ba","purple"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-ebant", "example":"ducebant", "tr":"they were leading",  "ep":[["duc",""],["e","coral"],["ba","purple"],["nt","blue"]]},
]

# Future: 3rd conj uses a DIFFERENT pattern from 1st/2nd (NOT -bo/-bi/-bu).
# Pattern: stem + -am / -es / -et / -emus / -etis / -ent.
TABLE_FUTURE_3RD = [
    {"conjugation":"I",            "infinitive_ending":"-am",   "example":"ducam",    "tr":"I will lead",      "ep":[["duc",""],["a","coral"],["m","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-es",   "example":"duces",    "tr":"you will lead",    "ep":[["duc",""],["e","coral"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-et",   "example":"ducet",    "tr":"he/she will lead", "ep":[["duc",""],["e","coral"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-emus", "example":"ducemus",  "tr":"we will lead",     "ep":[["duc",""],["e","coral"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-etis", "example":"ducetis",  "tr":"you will lead",    "ep":[["duc",""],["e","coral"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-ent",  "example":"ducent",   "tr":"they will lead",   "ep":[["duc",""],["e","coral"],["nt","blue"]]},
]

# Perfect: lead with duxi (-x- marker — most common in 3rd conj).
TABLE_PERFECT_3RD = [
    {"conjugation":"I",            "infinitive_ending":"-i",     "example":"duxi",       "tr":"I led",        "ep":[["du",""],["x","purple"],["i","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-isti",  "example":"duxisti",    "tr":"you led",      "ep":[["du",""],["x","purple"],["isti","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-it",    "example":"duxit",      "tr":"he/she led",   "ep":[["du",""],["x","purple"],["it","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-imus",  "example":"duximus",    "tr":"we led",       "ep":[["du",""],["x","purple"],["imus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-istis", "example":"duxistis",   "tr":"you led",      "ep":[["du",""],["x","purple"],["istis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-erunt", "example":"duxerunt",   "tr":"they led",     "ep":[["du",""],["x","purple"],["erunt","blue"]]},
]

# Pluperfect: same perfect stem (du + x) + -era- + person ending.
TABLE_PLUPERFECT_3RD = [
    {"conjugation":"I",            "infinitive_ending":"-eram",  "example":"duxeram",    "tr":"I had led",        "ep":[["du",""],["x","purple"],["era","pink"],["m","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-eras",  "example":"duxeras",    "tr":"you had led",      "ep":[["du",""],["x","purple"],["era","pink"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-erat",  "example":"duxerat",    "tr":"he/she had led",   "ep":[["du",""],["x","purple"],["era","pink"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-eramus","example":"duxeramus",  "tr":"we had led",       "ep":[["du",""],["x","purple"],["era","pink"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-eratis","example":"duxeratis",  "tr":"you had led",      "ep":[["du",""],["x","purple"],["era","pink"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-erant", "example":"duxerant",   "tr":"they had led",     "ep":[["du",""],["x","purple"],["era","pink"],["nt","blue"]]},
]


# ── Parse-and-translate questions for the Review set ────────────────────────
PARSE_TRANSLATE_QUESTIONS_N3 = [
    {"form":"ducis",      "tense":"present",    "person":"2nd","number":"singular","translation":"you (sg) lead"},
    {"form":"dicunt",     "tense":"present",    "person":"3rd","number":"plural",  "translation":"they say"},
    {"form":"ponimus",    "tense":"present",    "person":"1st","number":"plural",  "translation":"we put, place"},
    {"form":"cupit",      "tense":"present",    "person":"3rd","number":"singular","translation":"he/she wants"},
    {"form":"ducebat",    "tense":"imperfect",  "person":"3rd","number":"singular","translation":"he/she was leading"},
    {"form":"petebant",   "tense":"imperfect",  "person":"3rd","number":"plural",  "translation":"they were seeking"},
    {"form":"faciebam",   "tense":"imperfect",  "person":"1st","number":"singular","translation":"I was making, doing"},
    {"form":"duces",      "tense":"future",     "person":"2nd","number":"singular","translation":"you (sg) will lead"},
    {"form":"dicet",      "tense":"future",     "person":"3rd","number":"singular","translation":"he/she will say"},
    {"form":"effugient",  "tense":"future",     "person":"3rd","number":"plural",  "translation":"they will escape"},
    {"form":"duxit",      "tense":"perfect",    "person":"3rd","number":"singular","translation":"he/she led"},
    {"form":"dixerunt",   "tense":"perfect",    "person":"3rd","number":"plural",  "translation":"they said"},
    {"form":"posuisti",   "tense":"perfect",    "person":"2nd","number":"singular","translation":"you (sg) put, placed"},
    {"form":"duxerat",    "tense":"pluperfect", "person":"3rd","number":"singular","translation":"he/she had led"},
    {"form":"coegeramus", "tense":"pluperfect", "person":"1st","number":"plural",  "translation":"we had forced"},
    {"form":"fecerant",   "tense":"pluperfect", "person":"3rd","number":"plural",  "translation":"they had made, done"},
]


# ── Sentence-vocab tile content (filtered to lemmas that actually appear in
# Node 3 sentences, plus BE_FORMS) ──────────────────────────────────────────
_TILE_VOCAB_N3 = _build_tile_vocab(
    SENTENCES_PRESENT_TEST_N3 + SENTENCES_PRESENT_SYSTEM_N3
    + SENTENCES_ACTIVE_N3 + SENTENCES_PPP_N3 + SENTENCES_REVIEW_N3
)


# ── 16-tile Node 3 set list, mirroring Node 2 exactly ───────────────────────
NODE3_TITLE = "3rd Conjugation (Top 150)"

SETS_N3 = [
    # ── Row 1 ────────────────────────────────────────────────────────────────
    {
        "id":37, "node":3, "node_title":NODE3_TITLE,
        "title":"Present: 'I' Form",
        "badge":"Principal Part",
        "type":"verbs",
        "sell":"There are 12 third conjugation verbs in the GCSE Top 150. This set teaches you the **first principal part** — the present tense 'I' form.",
        "pass_mark":80,
        "screens":[
            {"heading":"The 1st Principal Part — 3rd conj.",
             "body":"The **1st principal part** of a 3rd conjugation verb ends in *-o*:\n\n    *duco* = I lead\n    *dico* = I say\n    *pono* = I put, place\n    *peto* = I seek, beg, ask, attack\n    *quaero* = I search, ask (for)\n    *relinquo* = I leave behind\n    *discedo* = I leave\n    *constituo* = I decide\n    *cogo* = I force\n    *occido* = I kill\n\nSome 3rd conjugation verbs end in *-io*. They behave slightly differently in certain forms:\n\n    *cupio* = I want\n    *facio* = I make, do\n    *effugio* = I escape"}
        ],
        "content":{"verbs":VERBS_3RD_TOP150, "mode":"meanings"},
    },
    {
        "id":38, "node":3, "node_title":NODE3_TITLE,
        "title":"Present Tense Endings",
        "type":"translate_form",
        "sell":"This set teaches you all six present tense endings for 3rd conjugation verbs.",
        "pass_mark":80,
        "screens":[
            {"heading":"3rd Conjugation: Present Tense",
             "body":"The person endings are the same as every conjugation: *-o / -s / -t / -mus / -tis / -nt*. What changes is the **stem vowel**. In the 3rd conjugation the stem vowel is *-i-* in most forms — but *-u-* in the **they** form (*ducunt*), and absent in the **I** form (*duco*).",
             "table":TABLE_PRESENT_3RD,
             "table2_heading":"The *-io* subset (*cupio*, *facio*, *effugio* ...)",
             "table2_body":"A small group of 3rd-conjugation verbs keeps *-i-* throughout — the *I* form ends in *-io* and the *they* form ends in *-iunt*. All other forms are identical to *duco*. In some ways this is easier: the *-i-* never changes.",
             "table2":TABLE_PRESENT_3RD_IO,
             "table_note":PRESENT_TABLE_NOTE_3RD,
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_PRESENT_N3},
    },
    {
        "id":39, "node":3, "node_title":NODE3_TITLE,
        "title":"Sentence Vocabulary",
        "type":"vocab", "optional":True,
        "sell":"Here are the words that will appear in the sentences of this node. Some of these will already be familiar to you.",
        "pass_mark":80,
        "content":{"vocab":_TILE_VOCAB_N3, "mode":"meanings"},
    },
    {
        "id":40, "node":3, "node_title":NODE3_TITLE,
        "title":"The Present Tense",
        "type":"sentences",
        "sell":"This set practises translating sentences using 3rd conjugation present tense verbs.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PRESENT_TEST_N3},
    },
    # ── Row 2 ────────────────────────────────────────────────────────────────
    {
        "id":41, "node":3, "node_title":NODE3_TITLE,
        "title":"Infinitive",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **second principal part** — the infinitive, or 'to…' form of the verb.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_3RD_TOP150,
            "mode":"infinitives",
            "show_parts_so_far":1,
            "pattern_screen":{
                "title":"3rd Conjugation: The Infinitive",
                "subtitle":"Add *-ere* to the verb stem:",
                "examples":[
                    {"present":"duco",  "full":"ducere",  "ending":"ere","english":"to lead"},
                    {"present":"dico",  "full":"dicere",  "ending":"ere","english":"to say"},
                    {"present":"pono",  "full":"ponere",  "ending":"ere","english":"to put, place"},
                    {"present":"cupio", "full":"cupere",  "ending":"ere","english":"to want"},
                    {"present":"facio", "full":"facere",  "ending":"ere","english":"to make, do"},
                ],
                "footnote":"3rd conjugation infinitives end in *-ere*, so they look the same as 2nd conjugation infinitives."
            }
        },
    },
    {
        "id":42, "node":3, "node_title":NODE3_TITLE,
        "title":"The Future Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **future tense** for 3rd conjugation verbs ('will lead', 'will say', 'will place').",
        "pass_mark":80,
        "screens":[
            {"heading":"The Future Tense — 3rd conj.",
             "body":"The 3rd conjugation future uses a different pattern from the 1st and 2nd conjugations — there is no *-b-*.",
             "table":TABLE_FUTURE_3RD,
             "table_note":"Colour key:\n**red** = theme vowel (*-a-* in I form; *-e-* elsewhere)\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_FUTURE_N3},
    },
    {
        "id":43, "node":3, "node_title":NODE3_TITLE,
        "title":"The Imperfect Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **imperfect tense** — used for continuous or repeated action in the past ('was leading', 'used to lead').",
        "pass_mark":80,
        "screens":[
            {"heading":"The Imperfect Tense — 3rd conj.",
             "body":"The imperfect tense refers to repeated or ongoing action in the past. The endings are *-bam*, *-bas*, *-bat*, *-bamus*, *-batis*, *-bant* — the same across all conjugations. In the 3rd conjugation, an extra *-e-* appears before *-ba-*.",
             "table":TABLE_IMPERFECT_3RD,
             "table_note":"Spot *-ba-* to identify the imperfect immediately.\n\nColour key:\n**red** = theme vowel (*-e-*)\n**purple** = tense marker (*-ba-*)\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_IMPERFECT_N3},
    },
    {
        "id":44, "node":3, "node_title":NODE3_TITLE,
        "title":"The Present System",
        "type":"sentences",
        "sell":"This set tests your ability to translate sentences using the present, imperfect, and future tenses with 3rd conjugation verbs.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PRESENT_SYSTEM_N3},
    },
    # ── Row 3 ────────────────────────────────────────────────────────────────
    {
        "id":45, "node":3, "node_title":NODE3_TITLE,
        "title":"Perfect: 'I' Form",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **third principal part** — the perfect 'I' form.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_3RD_TOP150,
            "mode":"perfects",
            "show_parts_so_far":2,
            "pattern_screen":{
                "title":"3rd Conjugation: The Perfect",
                "subtitle":"The 3rd conjugation uses four markers: *-v-*, *-u-*, *-x-*, *-s-*. A further group shows a complete stem change and must be learnt separately.",
                "examples":[
                    # -v- marker
                    {"full":"petivi",    "ending":"vi", "inf":"petere",      "english":"I sought, begged, asked, attacked",         "present":"peto"},
                    {"full":"quaesivi",  "ending":"vi", "inf":"quaerere",    "english":"I searched, asked (for)",                   "present":"quaero"},
                    {"full":"cupivi",    "ending":"vi", "inf":"cupere",      "english":"I wanted",                                  "present":"cupio"},
                    # -u- marker
                    {"full":"posui",     "ending":"ui", "inf":"ponere",      "english":"I put, placed",                             "present":"pono"},
                    # -x- marker
                    {"full":"duxi",      "ending":"xi", "inf":"ducere",      "english":"I led",                                     "present":"duco"},
                    {"full":"dixi",      "ending":"xi", "inf":"dicere",      "english":"I said",                                    "present":"dico"},
                    # -s- marker
                    {"full":"discessi",  "ending":"si", "inf":"discedere",   "english":"I left",                                    "present":"discedo"},
                    # complete stem changes (no marker — the whole stem shifts)
                    {"full":"reliqui",   "ending":"i",  "inf":"relinquere",  "english":"I left behind",                             "present":"relinquo"},
                    {"full":"constitui", "ending":"i",  "inf":"constituere", "english":"I decided",                                 "present":"constituo"},
                    {"full":"coegi",     "ending":"i",  "inf":"cogere",      "english":"I forced",                                  "present":"cogo"},
                    {"full":"occidi",    "ending":"i",  "inf":"occidere",    "english":"I killed",                                  "present":"occido"},
                    {"full":"feci",      "ending":"i",  "inf":"facere",      "english":"I made, did",                               "present":"facio"},
                    {"full":"effugi",    "ending":"i",  "inf":"effugere",    "english":"I escaped",                                 "present":"effugio"},
                ],
                "footnote":"The four perfect-stem markers (*-v-*, *-u-*, *-x-*, *-s-*) apply in the 3rd conjugation as follows:\n\n*-v-*: *petivi*, *quaesivi*, *cupivi*\n*-u-*: *posui*\n*-x-*: *duxi*, *dixi*\n*-s-*: *discessi*\n\nThe final group (*reliqui*, *constitui*, *coegi*, *feci*, *occidi*, *effugi*) are **complete stem changes** — the whole stem shifts. These are a new type: not 'no marker', but a different stem entirely. Learn them individually."
            }
        },
    },
    {
        "id":46, "node":3, "node_title":NODE3_TITLE,
        "title":"Perfect Tense: All Endings",
        "type":"translate_form",
        "sell":"This set teaches you all six forms of the **perfect tense** — used for completed actions in the past ('led', 'said', 'placed').",
        "pass_mark":80,
        "screens":[
            {"heading":"The Perfect Tense — 3rd conj.",
             "body":"Built on the **perfect stem** (the 3rd principal part, minus the final *-i*).",
             "table":TABLE_PERFECT_3RD,
             "table_note":"The four perfect-stem markers are *-v-*, *-u-*, *-x-*, *-s-*. In this table, the marker is *-x-*. Other 3rd-conj. perfects use *-v-* (*petivi*), *-u-* (*posui*), or *-s-* (*discessi*). Verbs like *reliqui*, *feci* are complete stem changes — learn them separately.\n\nColour key:\n**purple** = stem marker\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_PERFECT_N3},
    },
    {
        "id":47, "node":3, "node_title":NODE3_TITLE,
        "title":"The Pluperfect Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **pluperfect tense** — used for actions completed before another past event ('had led', 'had said').",
        "pass_mark":80,
        "screens":[
            {"heading":"The Pluperfect Tense — 3rd conj.",
             "body":"In English, we express the pluperfect with **'had'** — for example, 'he had led', 'they had placed'.\n\nIn Latin, build on the perfect stem and add the tense marker *-era-* before the person ending.",
             "table":TABLE_PLUPERFECT_3RD,
             "table_note":"The pluperfect uses the same perfect stem as the perfect (here *du-x-*), then adds the marker *-era-* and the person ending. Be careful not to confuse the perfect *-erunt* (they led) with the pluperfect *-erant* (they had led) — whenever you see *-era-*, it must be pluperfect.\n\nColour key:\n**purple** = stem marker\n**pink** = pluperfect marker (*-era-*)\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_PLUPERFECT_N3},
    },
    {
        "id":48, "node":3, "node_title":NODE3_TITLE,
        "title":"Perfect & Pluperfect",
        "type":"sentences",
        "sell":"This set practises translating sentences using the perfect and pluperfect tenses with 3rd conjugation verbs.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_ACTIVE_N3},
    },
    # ── Row 4 ────────────────────────────────────────────────────────────────
    {
        "id":49, "node":3, "node_title":NODE3_TITLE,
        "title":"Perfect Passive Participle (PPP)",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **fourth principal part** — the **Perfect Passive Participle (PPP)** for 3rd conjugation verbs.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_3RD_TOP150,
            "mode":"ppps",
            "show_parts_so_far":3,
            "pattern_screen":{
                "title":"3rd Conjugation: The PPP",
                "subtitle":"3rd conj. PPPs end in *-tus* or *-sus*, but the stem must be memorised:",
                "examples":[
                    {"present":"duco",      "infinitive":"ducere",     "perfect":"duxi",     "full":"ductus",      "ending":"tus","english":"having been led"},
                    {"present":"dico",      "infinitive":"dicere",     "perfect":"dixi",     "full":"dictus",      "ending":"tus","english":"having been said"},
                    {"present":"pono",      "infinitive":"ponere",     "perfect":"posui",    "full":"positus",     "ending":"tus","english":"having been put, placed"},
                    {"present":"peto",      "infinitive":"petere",     "perfect":"petivi",   "full":"petitus",     "ending":"tus","english":"having been sought, begged, asked, attacked"},
                    {"present":"relinquo",  "infinitive":"relinquere", "perfect":"reliqui",  "full":"relictus",    "ending":"tus","english":"having been left behind"},
                    {"present":"cogo",      "infinitive":"cogere",     "perfect":"coegi",    "full":"coactus",     "ending":"tus","english":"having been forced"},
                    {"present":"occido",    "infinitive":"occidere",   "perfect":"occidi",   "full":"occisus",     "ending":"sus","english":"having been killed"},
                    {"present":"facio",     "infinitive":"facere",     "perfect":"feci",     "full":"factus",      "ending":"tus","english":"having been made, done"},
                ],
                "footnote":"You can always translate a PPP as **'having been'** + the verb's meaning — e.g. *ductus* = 'having been led'. It acts like an adjective in the sentence, agreeing with the noun it describes in gender, number, and case.\n\n**PPP + est / sunt = perfect passive**: *ductus est* = 'he was led'; *ducti sunt* = 'they were led'.\n\nNote: *discedo* and *effugio* have no PPP."
            }
        },
    },
    {
        "id":50, "node":3, "node_title":NODE3_TITLE,
        "title":"Perfect Passive Participles",
        "type":"sentences",
        "sell":"You can always translate a PPP as **'having been ___'** — this set practises sentences that contain the Perfect Passive Participle.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PPP_N3},
    },
    {
        "id":51, "node":3, "node_title":NODE3_TITLE,
        "title":"Build the Principal Parts",
        "type":"building_parts",
        "sell":"This set tests all four principal parts of 3rd conjugation verbs in random order. You are given the present 'I' form and must supply the **infinitive**, **perfect**, or **PPP** from memory.",
        "pass_mark":80,
        "content":{"verbs":VERBS_3RD_TOP150, "mode":"all_four", "show_parts_so_far":4, "gap_positions":[1, 2, 3]},
    },
    {
        "id":52, "node":3, "node_title":NODE3_TITLE,
        "title":"Review",
        "type":"review",
        "badge":"test",
        "sell":"This set reviews everything in the node: parse and translate individual verb forms, then translate sentences covering all tenses and PPPs.",
        "pass_mark":80,
        "content":{
            "sentences": SENTENCES_REVIEW_N3,
            "parse_translate": PARSE_TRANSLATE_QUESTIONS_N3,
        },
    },
]


SETS_N3_BY_ID = {s["id"]: s for s in SETS_N3}
