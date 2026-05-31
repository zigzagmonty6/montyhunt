"""
Latin GCSE Mastery Platform - Content Data, Node 2 (2nd Conjugation).
Mirrors the architecture of data.py (Node 1) but for Node 2.

Focus: 2nd conjugation verbs (video, habeo, teneo, persuadeo, iubeo, appareo);
       iubeo + acc + inf; persuadeo + dat; *a/ab + abl* agent.

DRAFT — pending teacher review before integration with data.py.

Per Eduqas scope:
  - No demonstratives (ille / hic / is …) reach Node 2 sentences (Node 4 territory).
  - No 'tam' in sentences (Node 5).
  - No pluperfect-passive forms — passives capped at perfect passive (*PPP + est*/sunt).
  - Ideal perfect-passive translation: 'was Xed' (not 'has been Xed').
  - Ideal imperfect translation: 'was Xing' (no bare past in english list — marker
    flags bare past as a tense error).
  - Ideal PPP standalone: 'having been Xed'.
"""

from OFFICIAL_GLOSSES import g as _g
from data import NODE1_VOCAB as _N1_VOCAB
from sentence_vocab_scanner import build_tile_vocab as _build_tile_vocab


# ── 2nd Conjugation verbs - Top 150 only (6 verbs) ───────────────────────────
# Tuple: (present, infinitive, perfect, ppp_or_None,
#         eng_present, eng_infinitive, eng_perfect, eng_ppp_or_None)
# persuadeo and appareo have NO PPP.
VERBS_2ND_TOP150 = [
    ("video",     "videre",     "vidi",      "visus",   "I see",      "to see",      "I saw",       "having been seen"),
    ("habeo",     "habere",     "habui",     "habitus", "I have",     "to have",     "I had",       "having been had"),
    ("teneo",     "tenere",     "tenui",     "tentus",  "I hold",     "to hold",     "I held",      "having been held"),
    ("persuadeo", "persuadere", "persuasi",  None,      "I persuade", "to persuade", "I persuaded", None),
    ("iubeo",     "iubere",     "iussi",     "iussus",  "I order",    "to order",    "I ordered",   "having been ordered"),
    ("appareo",   "apparere",   "apparui",   None,      "I appear",   "to appear",   "I appeared",  None),
]


# ── Node 2 Sentence Vocabulary — non-verb lemmas across all 50 sentences ─────
NODE2_VOCAB = [
    # Nouns (new in Node 2 — Node 1 nouns recur but are not re-listed here)
    {"id":"amicus", "latin":"amicus", "english":[_g("amicus")], "pos":"noun",
     "derivatives":[
         {"word":"amiable",  "meaning":"having a friendly and pleasant manner"},
         {"word":"amicable", "meaning":"done in a friendly way without arguing, e.g. an amicable agreement"},
     ]},
    {"id":"gladius","latin":"gladius","english":[_g("gladius")],"pos":"noun",
     "derivatives":[
         {"word":"gladiator", "meaning":"a sword fighter who battled others in the Roman arena for public entertainment"},
         {"word":"gladiolus",  "meaning":"a tall garden plant named for its sword-shaped leaves"},
     ]},
    {"id":"silva",  "latin":"silva",  "english":[_g("silva")],  "pos":"noun",
     "derivatives":[
         {"word":"sylvan",       "meaning":"relating to or typical of a wood or forest"},
         {"word":"Pennsylvania", "meaning":"literally 'Penn's woodland' — the -sylvania part comes from silva"},
         {"word":"Transylvania", "meaning":"'across the forest' — trans means across, sylvania from silva"},
     ]},
    {"id":"filius", "latin":"filius", "english":[_g("filius")], "pos":"noun",
     "derivatives":[
         {"word":"affiliate",   "meaning":"to officially join or connect to an organisation — from the Latin for 'to adopt as a son'"},
         {"word":"affiliation", "meaning":"membership of or connection to a group or organisation"},
     ]},
    # Adjectives
    {"id":"omnis",       "latin":"omnis",       "english":[_g("omnis")],       "pos":"adjective",
     "derivatives":[
         {"word":"omnivore",   "meaning":"an animal that eats everything — both plants and meat"},
         {"word":"omnipotent", "meaning":"all-powerful"},
         {"word":"omniscient", "meaning":"all-knowing"},
         {"word":"omnibus",    "meaning":"a vehicle for everyone — the origin of the word 'bus'"},
     ]},
    {"id":"perterritus", "latin":"perterritus", "english":[_g("perterritus")], "pos":"adjective",
     "derivatives":[
         {"word":"terrify",   "meaning":"to make someone very frightened"},
         {"word":"terrible",  "meaning":"extremely bad or frightening"},
         {"word":"terror",    "meaning":"extreme fear"},
         {"word":"deter",     "meaning":"to discourage someone from doing something by making them afraid of the consequences"},
     ]},
    # Pronouns (2nd-person; ego / me / mihi already in Node 1)
    {"id":"tu",   "latin":"tu",   "english":[_g("tu")],   "pos":"pronoun"},
    {"id":"te",   "latin":"te",   "english":[_g("te")],   "pos":"pronoun", "notes":"object form — used as the object of a verb"},
    {"id":"tibi", "latin":"tibi", "english":[_g("tibi")], "pos":"pronoun", "notes":"used after verbs that take 'to' / 'for' (e.g. persuadeo, do)"},
    # Prepositions
    {"id":"e_ex", "latin":"e, ex", "english":[_g("e, ex")], "pos":"preposition", "display_label":"+ abl",
     "derivatives":[
         {"word":"exit",          "meaning":"the way out, or the act of leaving"},
         {"word":"export",        "meaning":"to send goods out of a country"},
         {"word":"exterior",      "meaning":"the outside of something"},
         {"word":"extraordinary", "meaning":"outside the ordinary — unusually remarkable"},
     ]},
    {"id":"a_ab", "latin":"a, ab", "english":[_g("a, ab")], "pos":"preposition", "display_label":"+ abl", "notes":"used to mark who is doing the action in a passive sentence",
     "derivatives":[
         {"word":"absent",  "meaning":"away from a place — not present"},
         {"word":"abolish", "meaning":"to do away with something completely"},
         {"word":"abduct",  "meaning":"to take someone away by force"},
         {"word":"abnormal","meaning":"away from the normal — not typical"},
     ]},
    # Adverbs / conjunctions
    {"id":"tamen",  "latin":"tamen",  "english":[_g("tamen")],  "pos":"adverb"},
    {"id":"igitur", "latin":"igitur", "english":[_g("igitur")], "pos":"adverb", "notes":"postpositive — usually 2nd word"},
    {"id":"enim",   "latin":"enim",   "english":[_g("enim")],   "pos":"conjunction", "notes":"postpositive — usually 2nd word"},
    {"id":"iterum", "latin":"iterum", "english":[_g("iterum")], "pos":"adverb",
     "derivatives":[
         {"word":"iterate",   "meaning":"to repeat a process or say something again"},
         {"word":"reiterate", "meaning":"to say something again, often for emphasis"},
         {"word":"iteration", "meaning":"one cycle of a repeated process"},
     ]},
    {"id":"vix",    "latin":"vix",    "english":[_g("vix")],    "pos":"adverb"},
    {"id":"mox",    "latin":"mox",    "english":[_g("mox")],    "pos":"adverb"},
    {"id":"statim", "latin":"statim", "english":[_g("statim")], "pos":"adverb"},
]


# ── Tense ID questions — present/imperfect/future/perfect/pluperfect of 2nd conj ─
TENSE_ID_QUESTIONS_N2 = [
    # Present
    {"form":"videt",        "plain":"videt",        "tense":"present",    "translation":"he/she sees"},
    {"form":"habeo",        "plain":"habeo",        "tense":"present",    "translation":"I have"},
    {"form":"tenent",       "plain":"tenent",       "tense":"present",    "translation":"they hold"},
    {"form":"persuadet",    "plain":"persuadet",    "tense":"present",    "translation":"he/she persuades"},
    {"form":"iubet",        "plain":"iubet",        "tense":"present",    "translation":"he/she orders"},
    {"form":"apparent",     "plain":"apparent",     "tense":"present",    "translation":"they appear"},
    # Imperfect
    {"form":"videbat",      "plain":"videbat",      "tense":"imperfect",  "translation":"he/she was seeing"},
    {"form":"habebant",     "plain":"habebant",     "tense":"imperfect",  "translation":"they were having"},
    {"form":"tenebat",      "plain":"tenebat",      "tense":"imperfect",  "translation":"he/she was holding"},
    {"form":"apparebant",   "plain":"apparebant",   "tense":"imperfect",  "translation":"they were appearing"},
    {"form":"iubebat",      "plain":"iubebat",      "tense":"imperfect",  "translation":"he/she was ordering"},
    # Future
    {"form":"videbit",      "plain":"videbit",      "tense":"future",     "translation":"he/she will see"},
    {"form":"habebunt",     "plain":"habebunt",     "tense":"future",     "translation":"they will have"},
    {"form":"tenebit",      "plain":"tenebit",      "tense":"future",     "translation":"he/she will hold"},
    {"form":"persuadebit",  "plain":"persuadebit",  "tense":"future",     "translation":"he/she will persuade"},
    {"form":"apparebunt",   "plain":"apparebunt",   "tense":"future",     "translation":"they will appear"},
    # Perfect
    {"form":"vidit",        "plain":"vidit",        "tense":"perfect",    "translation":"he/she saw"},
    {"form":"habuerunt",    "plain":"habuerunt",    "tense":"perfect",    "translation":"they had"},
    {"form":"tenuit",       "plain":"tenuit",       "tense":"perfect",    "translation":"he/she held"},
    {"form":"persuasit",    "plain":"persuasit",    "tense":"perfect",    "translation":"he/she persuaded"},
    {"form":"iusserunt",    "plain":"iusserunt",    "tense":"perfect",    "translation":"they ordered"},
    {"form":"apparuit",     "plain":"apparuit",     "tense":"perfect",    "translation":"he/she appeared"},
    # Pluperfect
    {"form":"viderat",      "plain":"viderat",      "tense":"pluperfect", "translation":"he/she had seen"},
    {"form":"habuerant",    "plain":"habuerant",    "tense":"pluperfect", "translation":"they had had"},
    {"form":"persuaserat",  "plain":"persuaserat",  "tense":"pluperfect", "translation":"he/she had persuaded"},
    {"form":"iusserat",     "plain":"iusserat",     "tense":"pluperfect", "translation":"he/she had ordered"},
]


# ════════════════════════════════════════════════════════════════════════════
# SENTENCE SETS
# ════════════════════════════════════════════════════════════════════════════
#
# Each sentence dict mirrors Node 1: latin, english (ideal first then
# accepted alternatives drawn ONLY from the teacher's notes), explanation
# (bullets, like Node 1).
#
# Pre-adaptation log (against _curr.txt 805-1149):
#   15: 'eam' -> 'deam' (Node 4 reservation)
#   27: rewritten — drop 'illud' & 'tam'
#   30: rewritten — drop 'illa' & 'ei'
#   32: pluperfect passive 'tenti erant' -> perfect passive 'tenti sunt'
#   36: 'tentus erat' -> 'tentus est'
#   37: 'iussi erant' -> 'iussi sunt'
#   38: 'habitus erat' -> 'habitus est'; 'eum' -> 'gladium'
#   39: 'visae erant' -> 'visae sunt'
#   40: 'oppugnati erant' -> 'oppugnati sunt'
#   41: 'ille' -> 'pulcher'; 'eum' -> 'filium'
#   43: 'illa' -> 'pulchra'
#   46: 'eam' -> 'deam'
# ════════════════════════════════════════════════════════════════════════════


# ── Set 4 (id 24): Present ──────────────────────────────────────────────────
SENTENCES_PRESENT_TEST_N2 = [
    {
        "latin": "amicus gladium habet.",
        "english": [
            "The friend has a sword.",
            "The friend has the sword.",
            "A friend has a sword.",
            "A friend has the sword.",
            "The friend holds a sword.",
            "The friend holds the sword.",
        ],
        "explanation": (
            "• amic{T:us} (the friend)\n"
            "  → *amicus* (friend) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → the *-{T:us}* ending is the classic 2nd declension masculine {T:nominative} singular\n"
            "• hab{R:e}{B:t} (has)\n"
            "  → *habeo* (I have) is the dictionary form of this verb\n"
            "  → *hab-* (have) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• gladi{T:um} (a sword)\n"
            "  → *gladium* (sword) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "filius patrem videt.",
        "english": [
            "The son sees the father.",
            "The son sees the father.",
            "The son sees a father.",
            "The son can see his father.",
            "The son can see the father.",
            "The son is seeing his father.",
            "A son sees the father.",
        ],
        "explanation": (
            "• fili{T:us} (the son)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• vid{R:e}{B:t} (sees)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* (see) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• patr{T:em} (the father)\n"
            "  → *patrem* (father) is a noun, 3rd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "silva ingens apparet.",
        "english": [
            "A huge wood appears.",
            "The huge wood appears.",
            "A huge forest appears.",
            "A huge woods appears.",
            "A huge wood is appearing.",
            "An enormous wood appears.",
            "A vast wood appears.",
            "A massive wood appears.",
            "A huge wood comes into view.",
        ],
        "explanation": (
            "• silv{T:a} ingens (a huge wood)\n"
            "  → *silva* (wood) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *ingens* (huge) is an adjective, and agrees with *silva* (wood) because they are both feminine singular {T:nominative}\n"
            "  → *ingens* has the same form for all genders — no gender change!\n"
            "• appar{R:e}{B:t} (appears)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *appar-* (appear) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "deae filios tenent.",
        "english": [
            "The goddesses are holding the sons.",
            "The goddesses hold the sons.",
            "The goddesses are holding their sons.",
            "The goddesses hold their sons.",
        ],
        "explanation": (
            "• de{T:ae} (the goddesses)\n"
            "  → *deae* (goddesses) is a noun, 1st declension feminine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → careful: *de{T:ae}* can also mean 'of the goddess' (genitive singular) — but the plural verb *tenent* confirms it must be the plural {T:nominative} here\n"
            "• ten{R:e}{B:nt} (are holding)\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *ten-* (hold) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• fili{T:os} (the sons)\n"
            "  → *filios* (sons) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} so it receives the verb\n"
            "  → the *-{T:os}* ending marks masculine plural {T:accusative}"
        ),
    },
    {
        "latin": "tu me vides, sed ego te non video.",
        "english": [
            "You see me, but I do not see you.",
            "You yourself see me, but I myself do not see you.",
            "You can see me, but I cannot see you.",
            "You are seeing me, but I am not seeing you.",
            "You see me, but I am not seeing you.",
        ],
        "explanation": (
            "• tu (you)\n"
            "  → *tu* (you) is the {T:nominative} singular of the 2nd person pronoun\n"
            "  → the *-{B:s}* ending of *vides* already shows you (singular) is the subject — *tu* is added for emphasis\n"
            "• vid{R:e}{B:s} (see)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* (see) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:s}* shows it is the you (singular) form\n"
            "• me (me)\n"
            "  → *me* is the {T:accusative} singular of *ego* (I)\n"
            "  → the {T:accusative} is the {N:object} — I am being seen\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast with the first clause\n"
            "• ego (I)\n"
            "  → *ego* (I) is the {T:nominative} singular of the 1st person pronoun\n"
            "  → the *-{B:o}* ending of *video* already shows I am the subject — *ego* is added for emphasis\n"
            "• non vid{R:e}{B:o} (do not see)\n"
            "  → *non* (not) negates the verb\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* (see) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:o}* shows it is the I form\n"
            "• te (you)\n"
            "  → *te* is the {T:accusative} singular of *tu* (you)\n"
            "  → the {T:accusative} is the {N:object} — you are not being seen!"
        ),
    },
    {
        "latin": "pater filio persuadet, et filius apparet.",
        "english": [
            "The father persuades the son, and the son appears.",
            "The father persuades the son, and the son comes into view.",
            "The father is persuading his son, and the son appears.",
            "The father persuades his son, and the son is appearing.",
            "The father is persuading the son, and the son appears.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• fili{T:o} (the son)\n"
            "  → *filio* is the {T:dative} singular of *filius* (son)\n"
            "  → *persuadeo* takes the {T:dative}: 'persuades the son'\n"
            "• persuad{R:e}{B:t} (persuades)\n"
            "  → *persuadeo* (I persuade) is the dictionary form of this verb\n"
            "  → *persuad-* (persuade) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• fili{T:us} (the son)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second verb *apparet*\n"
            "• appar{R:e}{B:t} (appears)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *appar-* (appear) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "regina filios iubet gladios tenere.",
        "english": [
            "The queen orders the sons to hold swords.",
            "The queen commands the sons to hold swords.",
            "The queen orders the sons to keep the swords.",
            "The queen is ordering the sons to hold swords.",
            "The queen orders the sons to hold the swords.",
        ],
        "explanation": (
            "• regin{T:a} (the queen)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• iub{R:e}{B:t} (orders)\n"
            "  → *iubeo* (I order) is the dictionary form of this verb\n"
            "  → *iub-* (order) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• fili{T:os} (the sons)\n"
            "  → *filios* (sons) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → *iubeo* + accusative + infinitive: 'order X to do Y'\n"
            "  → the {T:accusative} marks who is being ordered\n"
            "• gladi{T:os} (swords)\n"
            "  → *gladios* (swords) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *tenere* — the swords are to be held\n"
            "• tenere (to hold)\n"
            "  → *tenere* is the infinitive of *teneo* (I hold), 2nd conjugation\n"
            "  → the infinitive completes the *iubeo* structure: 'she orders the sons TO hold swords'"
        ),
    },
    {
        "latin": "omnes amici gladios tenent, et deos vident.",
        "english": [
            "All the friends are holding swords, and are seeing the gods.",
            "All the friends hold swords, and see the gods.",
            "All the friends hold swords, and are seeing the gods.",
            "All of the friends are holding swords, and are seeing the gods.",
            "All friends hold swords, and see the gods.",
        ],
        "explanation": (
            "• omn{T:es} amici (all the friends)\n"
            "  → *omnes* (all) is an adjective, 3rd declension plural {T:nominative}\n"
            "  → *amici* (friends) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → *omnes* agrees with *amici* as both are masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• ten{R:e}{B:nt} (are holding)\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *ten-* (hold) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• gladi{T:os} (swords)\n"
            "  → *gladios* (swords) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the swords are being held\n"
            "• vid{R:e}{B:nt} (are seeing)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* (see) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• de{T:os} (the gods)\n"
            "  → *deos* (gods) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the gods are being seen"
        ),
    },
    {
        "latin": "dea subito apparet, et filium ibi videt.",
        "english": [
            "The goddess suddenly appears, and sees the son there.",
            "Suddenly the goddess appears, and sees her son there.",
            "Suddenly, the goddess appears, and there she sees her son.",
            "The goddess suddenly comes into view, and sees her son there.",
            "The goddess appears suddenly, and there she sees the son.",
            "The goddess appears suddenly, and sees the son there.",
            "Suddenly the goddess appears, and there she sees the son.",
            "The goddess appears suddenly, and there she sees her son.",
        ],
        "explanation": (
            "• de{T:a} (the goddess)\n"
            "  → *dea* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• subito (suddenly)\n"
            "  → *subito* (suddenly) is an adverb — it can go anywhere in the sentence for emphasis\n"
            "• appar{R:e}{B:t} (appears)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *appar-* (appear) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• fili{T:um} (the son)\n"
            "  → *filium* (son) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the son is being seen\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• ibi (there)\n"
            "  → *ibi* (there) is an adverb — flexible position in the sentence\n"
            "• vid{R:e}{B:t} (sees)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* (see) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "pater mihi etiam persuadet, et statim gladium habeo.",
        "english": [
            "The father even persuades me, and I immediately have a sword.",
            "The father also persuades me, and I immediately have a sword.",
            "The father even persuades me, and I at once have a sword.",
            "The father even persuades me, and straight away I have a sword.",
            "The father even persuades me, and immediately I hold a sword.",
            "The father even persuades me, and I have a sword at once.",
            "The father even persuades me, and at once I have a sword.",
            "The father also persuades me, and immediately I have a sword.",
            "Father even persuades me, and I have a sword at once.",
            "The father even persuades me, and I at once hold a sword.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• mihi (me / to me)\n"
            "  → *mihi* is the {T:dative} singular of *ego* (I)\n"
            "  → *persuadeo* takes the {T:dative}: 'persuades me'\n"
            "• etiam (even / also)\n"
            "  → *etiam* (even / also) is an adverb — here 'even' fits best\n"
            "• persuad{R:e}{B:t} (persuades)\n"
            "  → *persuadeo* (I persuade) is the dictionary form of this verb\n"
            "  → *persuad-* (persuade) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — it can go anywhere for emphasis\n"
            "• hab{R:e}{B:o} (I have)\n"
            "  → *habeo* (I have) is the dictionary form of this verb\n"
            "  → *hab-* (have) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{B:o}* shows it is the I form\n"
            "• gladi{T:um} (a sword)\n"
            "  → *gladium* (sword) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the sword is being had\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
]


# ── Set 8 (id 26): Imperfect & Future ───────────────────────────────────────
# Per teacher: imperfect ideal = 'was Xing'; bare past not accepted.
SENTENCES_PRESENT_SYSTEM_N2 = [
    {
        "latin": "dea filium videbat.",
        "english": [
            "The goddess was seeing the son.",
            "The goddess was seeing the son.",
            "The goddess used to see her son.",
            "The goddess kept seeing her son.",
            "The goddess was watching her son.",
            "The goddess used to see the son.",
        ],
        "explanation": (
            "• de{T:a} (the goddess)\n"
            "  → *dea* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• vid{R:e}{P:ba}{B:t} (was seeing)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* (see) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker — spot it to identify the tense immediately\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → the imperfect describes a continuing or repeated past action: 'was seeing' or 'used to see'\n"
            "• fili{T:um} (the son)\n"
            "  → *filium* (son) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the son is being seen\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "pater gladios habebit.",
        "english": [
            "The father will have swords.",
            "The father will have the swords.",
            "The father is going to have swords.",
            "The father will be holding swords.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• hab{R:e}{P:bi}{B:t} (will have)\n"
            "  → *habeo* (I have) is the dictionary form of this verb\n"
            "  → *hab-* (have) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:bi}-* is the future marker — it will happen!\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• gladi{T:os} (swords)\n"
            "  → *gladios* (swords) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the swords will be had"
        ),
    },
    {
        "latin": "amici in silva apparebant, gladiosque tenebant.",
        "english": [
            "The friends were appearing in the wood, and were holding swords.",
            "The friends were appearing in the forest, and were holding swords.",
            "The friends were appearing in the woods, and were holding swords.",
            "The friends used to appear in the wood, and were holding swords.",
            "The friends kept appearing in the wood, and were holding swords.",
            "The friends were appearing in the wood, and kept holding swords.",
            "The friends were appearing in the wood, and used to hold swords.",
            "The friends were appearing in the forest, and used to hold swords.",
            "The friends were appearing in the woods, and used to hold swords.",
        ],
        "explanation": (
            "• amici (the friends)\n"
            "  → *amici* (friends) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• in silv{T:a} (in the wood)\n"
            "  → *in + ablative* = in / on (no motion)\n"
            "  → *silv{T:a}* (wood) is the {T:ablative} singular — the preposition *in* confirms it is ablative\n"
            "• appar{R:e}{P:ba}{B:nt} (were appearing)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *appar-* (appear) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• ten{R:e}{P:ba}{B:nt} (were holding)\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *ten-* (hold) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• gladios -que (swords and)\n"
            "  → *-que* means 'and' — it clips onto the end of a word, but you translate 'and' BEFORE that word. So *gladiosque* = '... and swords'\n"
            "  → it works just like *et* (and) but is glued onto the following word"
        ),
    },
    {
        "latin": "regina filios iubebit gladios tenere.",
        "english": [
            "The queen will order the sons to hold swords.",
            "The queen will command the sons to hold swords.",
            "The queen will order the sons to keep the swords.",
            "The queen will order the sons to hold the swords.",
            "The queen will order her sons to hold swords.",
        ],
        "explanation": (
            "• regin{T:a} (the queen)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• iub{R:e}{P:bi}{B:t} (will order)\n"
            "  → *iubeo* (I order) is the dictionary form of this verb\n"
            "  → *iub-* (order) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:bi}-* is the future marker\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• fili{T:os} (the sons)\n"
            "  → *filios* (sons) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → *iubeo* + accusative + infinitive: 'order X to do Y'\n"
            "  → the {T:accusative} marks who is being ordered\n"
            "• gladi{T:os} (swords)\n"
            "  → *gladios* (swords) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *tenere* — the swords are to be held\n"
            "• tenere (to hold)\n"
            "  → *tenere* is the infinitive of *teneo* (I hold), 2nd conjugation\n"
            "  → the infinitive completes the *iubeo* structure: 'will order them TO hold swords'"
        ),
    },
    {
        "latin": "vix dea apparebat, sed filii deam videbant.",
        "english": [
            "The goddess was scarcely appearing, but the sons were seeing the goddess.",
            "The goddess was hardly appearing, but the sons were seeing the goddess.",
            "The goddess was barely appearing, but the sons were seeing the goddess.",
            "Scarcely was the goddess appearing, but the sons were seeing the goddess.",
            "The goddess was scarcely appearing, but the sons could see the goddess.",
        ],
        "explanation": (
            "• vix (scarcely)\n"
            "  → *vix* (scarcely / hardly / barely) is an adverb — flexible position\n"
            "• de{T:a} (the goddess)\n"
            "  → *dea* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• appar{R:e}{P:ba}{B:t} (was appearing)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *appar-* (appear) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast with the first clause\n"
            "• fili{T:i} (the sons)\n"
            "  → *filii* (sons) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the second verb\n"
            "• vid{R:e}{P:ba}{B:nt} (were seeing)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* (see) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• de{T:am} (the goddess)\n"
            "  → *deam* (goddess) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the goddess is being seen\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "statim igitur omnes amici gladios habebunt, et deos videbunt.",
        "english": [
            "Therefore all the friends will immediately have swords, and will see the gods.",
            "So all the friends will immediately have swords, and will see the gods.",
            "And so, immediately, all the friends will have swords, and will see the gods.",
            "Therefore, immediately, all the friends will have swords, and will see the gods.",
            "Therefore all the friends will at once have swords, and will see the gods.",
        ],
        "explanation": (
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• igitur (therefore)\n"
            "  → *igitur* (therefore / so) is a connector — postpositive, so it sits as the 2nd word in its clause\n"
            "• omn{T:es} amici (all the friends)\n"
            "  → *omnes* agrees with *amici* as both are masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• hab{R:e}{P:bu}{B:nt} (will have)\n"
            "  → *habeo* (I have) is the dictionary form of this verb\n"
            "  → *hab-* (have) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:bu}-* is the future marker for the they form\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• gladi{T:os} (swords)\n"
            "  → *gladios* (swords) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the swords will be had\n"
            "• vid{R:e}{P:bu}{B:nt} (will see)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* (see) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:bu}-* is the future marker for the they form\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• de{T:os} (the gods)\n"
            "  → *deos* (gods) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the gods will be seen"
        ),
    },
    {
        "latin": "iterum dea patri persuadebat, et pater in silva apparebat.",
        "english": [
            "The goddess was again persuading the father, and the father was appearing in the wood.",
            "Again the goddess was persuading the father, and the father was appearing in the wood.",
            "The goddess was again persuading the father, and the father was appearing in the forest.",
            "The goddess used to persuade the father again, and the father used to appear in the wood.",
            "The goddess was again persuading the father, and the father kept appearing in the wood.",
        ],
        "explanation": (
            "• iterum (again)\n"
            "  → *iterum* (again) is an adverb — flexible position\n"
            "• de{T:a} (the goddess)\n"
            "  → *dea* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• patr{T:i} (the father)\n"
            "  → *patri* is the {T:dative} singular of *pater* (father)\n"
            "  → *persuadeo* takes the {T:dative}: 'persuades the father'\n"
            "• persuad{R:e}{P:ba}{B:t} (was persuading)\n"
            "  → *persuadeo* (I persuade) is the dictionary form of this verb\n"
            "  → *persuad-* (persuade) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker — the persuading was ongoing\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• in silv{T:a} (in the wood)\n"
            "  → *in + ablative* = in / on (location, no motion)\n"
            "  → *silv{T:a}* (wood) is the {T:ablative} singular\n"
            "• appar{R:e}{P:ba}{B:t} (was appearing)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *appar-* (appear) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
    {
        "latin": "filii in silva erant, et pater non videbat.",
        "english": [
            "The sons were in the wood, and the father was not seeing them.",
            "The sons were in the forest, and the father was not seeing them.",
            "The sons were in the wood, and the father could not see them.",
            "The sons were in the wood, and the father was not seeing.",
            "The sons were in the woods, and the father was not seeing them.",
            "The sons were in the wood, and the father used not to see them.",
        ],
        "explanation": (
            "• fili{T:i} (the sons)\n"
            "  → *filii* (sons) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• in silv{T:a} (in the wood)\n"
            "  → *in + ablative* = in / on\n"
            "  → *silv{T:a}* (wood) is the {T:ablative} singular\n"
            "• er{M:a}{B:nt} (were)\n"
            "  → *sum* (I am) is the irregular verb 'to be'\n"
            "  → *er{M:a}{B:nt}* is the imperfect 3rd person plural: 'they were'\n"
            "  → *-{M:a}-* is the imperfect marker; *-{B:nt}* shows it is the they form\n"
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second verb\n"
            "• non vid{R:e}{P:ba}{B:t} (was not seeing)\n"
            "  → *non* (not) negates the verb\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* (see) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "  → Latin can leave the object implicit — 'was not seeing' (them, the sons)"
        ),
    },
    {
        "latin": "filius gladium tenebit, et amicum mox iubebit apparere.",
        "english": [
            "The son will hold a sword, and will soon order the friend to appear.",
            "The son will hold the sword, and will soon order his friend to appear.",
            "The son will hold a sword, and soon will order his friend to appear.",
            "The son will hold a sword, and will soon command his friend to appear.",
            "The son will hold a sword, and will soon order his friend to come into view.",
        ],
        "explanation": (
            "• fili{T:us} (the son)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• ten{R:e}{P:bi}{B:t} (will hold)\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *ten-* (hold) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:bi}-* is the future marker\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• gladi{T:um} (a sword)\n"
            "  → *gladium* (sword) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the sword will be held\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• iub{R:e}{P:bi}{B:t} (will order)\n"
            "  → *iubeo* (I order) is the dictionary form of this verb\n"
            "  → *iub-* (order) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:bi}-* is the future marker\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• amic{T:um} (the friend)\n"
            "  → *amicum* (friend) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → *iubeo* + accusative + infinitive: 'order X to do Y'\n"
            "  → the {T:accusative} marks who is being ordered\n"
            "• mox (soon)\n"
            "  → *mox* (soon) is an adverb — flexible position\n"
            "• apparere (to appear)\n"
            "  → *apparere* is the infinitive of *appareo* (I appear), 2nd conjugation\n"
            "  → the infinitive completes the *iubeo* structure: 'will order the friend TO appear'"
        ),
    },
    {
        "latin": "pater filium iubebat gladium tenere, sed filius tamen non apparebat.",
        "english": [
            "The father was ordering the son to hold a sword, but the son however was not appearing.",
            "The father was ordering his son to hold a sword, but the son however was not appearing.",
            "The father was ordering his son to keep a sword, but the son however was not appearing.",
            "The father was commanding his son to hold a sword, but the son however was not appearing.",
            "The father kept ordering his son to hold a sword, but the son however was not appearing.",
            "The father used to order his son to hold a sword, but the son however was not appearing.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• iub{R:e}{P:ba}{B:t} (was ordering)\n"
            "  → *iubeo* (I order) is the dictionary form of this verb\n"
            "  → *iub-* (order) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker — the ordering was ongoing\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• fili{T:um} (the son)\n"
            "  → *filium* (son) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → *iubeo* + accusative + infinitive: 'order X to do Y'\n"
            "  → the {T:accusative} marks who is being ordered\n"
            "• gladi{T:um} (a sword)\n"
            "  → *gladium* (sword) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *tenere* — the sword is to be held\n"
            "• tenere (to hold)\n"
            "  → *tenere* is the infinitive of *teneo* (I hold), 2nd conjugation\n"
            "  → the infinitive completes the *iubeo* structure: 'was ordering him TO hold a sword'\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast with the first clause\n"
            "• fili{T:us} (the son)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second verb\n"
            "• tamen (however)\n"
            "  → *tamen* (however / nevertheless) is a connector — adds contrast\n"
            "• non appar{R:e}{P:ba}{B:t} (was not appearing)\n"
            "  → *non* (not) negates the verb\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *appar-* (appear) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker\n"
            "  → *-{B:t}* shows it is the he/she/it form"
        ),
    },
]


# ── Set 12 (id 28): Perfect & Pluperfect (active) ───────────────────────────
SENTENCES_ACTIVE_N2 = [
    {
        "latin": "amicus gladium tenuit.",
        "english": [
            "The friend held the sword.",
            "The friend held a sword.",
            "The friend has held the sword.",
            "The friend did hold the sword.",
            "The friend kept hold of the sword.",
        ],
        "explanation": (
            "• amic{T:us} (the friend)\n"
            "  → *amicus* (friend) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• tenu{B:it} (held)\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *tenu-* is the perfect stem (note: the present stem is *ten-*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense describes a completed, single past action: 'held'\n"
            "• gladi{T:um} (the sword)\n"
            "  → *gladium* (sword) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the sword was held\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "pater filium vidit.",
        "english": [
            "The father saw the son.",
            "The father saw the son.",
            "The father has seen his son.",
            "The father has seen the son.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• vidi{B:t} (saw)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* is the perfect stem (from *vidi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect tense\n"
            "  → the perfect tense: a completed, single past action: 'saw'\n"
            "• fili{T:um} (the son)\n"
            "  → *filium* (son) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the son was seen\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "deae iterum apparuerunt, et filii abierunt.",
        "english": [
            "The goddesses appeared again, and the sons went away.",
            "The goddesses appeared again, and the sons left.",
            "The goddesses appeared again, and the sons departed.",
            "Again the goddesses appeared, and the sons went away.",
            "The goddesses have appeared again, and the sons have gone away.",
        ],
        "explanation": (
            "• de{T:ae} (the goddesses)\n"
            "  → *deae* (goddesses) is a noun, 1st declension feminine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• iterum (again)\n"
            "  → *iterum* (again) is an adverb — flexible position\n"
            "• apparu{B:erunt} (appeared)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect tense\n"
            "• fili{T:i} (the sons)\n"
            "  → *filii* (sons) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second verb\n"
            "• ab{B:ierunt} (went away)\n"
            "  → *abeo* (*ab* + *eo*) is the dictionary form of this verb — an irregular compound: 'go away / depart'\n"
            "  → *ab-ii-* is the perfect stem; *-{B:erunt}* shows it is the they form of the perfect"
        ),
    },
    {
        "latin": "pater filio persuaserat, sed filius etiam tum non apparuit.",
        "english": [
            "The father had persuaded the son, but the son still did not appear then.",
            "The father had persuaded the son, but even then the son did not appear.",
            "The father had persuaded his son, but the son even then did not appear.",
            "The father had persuaded his son, but the son still then did not appear.",
            "The father had persuaded his son, but the son did not appear even at that time.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• fili{T:o} (the son)\n"
            "  → *filio* is the {T:dative} singular of *filius* (son)\n"
            "  → *persuadeo* takes the {T:dative}: 'persuades the son'\n"
            "• persuas{M:era}{B:t} (had persuaded)\n"
            "  → *persuadeo* (I persuade) is the dictionary form of this verb\n"
            "  → *persuas-* is the perfect stem (from *persuasi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the action had already happened before another past event\n"
            "  → *-{B:t}* shows it is the he/she/it form; the pluperfect means 'had done'\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast with the first clause\n"
            "• fili{T:us} (the son)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second verb\n"
            "• etiam tum (even then / still then)\n"
            "  → *etiam* (even / also) + *tum* (then / at that time): 'even then' or 'still then'\n"
            "• non apparu{B:it} (did not appear)\n"
            "  → *non* (not) negates the verb\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect"
        ),
    },
    {
        "latin": "multi amici gladios habuerant, et deos viderunt.",
        "english": [
            "Many friends had had swords, and saw the gods.",
            "Many friends had owned swords, and saw the gods.",
            "Many friends had possessed swords, and saw the gods.",
            "Many friends had had swords, and have seen the gods.",
            "Many of the friends had had swords, and saw the gods.",
        ],
        "explanation": (
            "• mult{T:i} amici (many friends)\n"
            "  → *multi* (many) is an adjective, masculine plural {T:nominative}\n"
            "  → *amici* (friends) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → *multi* agrees with *amici* as both are masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• habu{M:era}{B:nt} (had had)\n"
            "  → *habeo* (I have) is the dictionary form of this verb\n"
            "  → *habu-* is the perfect stem (from *habui*)\n"
            "  → *-{M:era}-* is the pluperfect marker: 'had had'\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• gladi{T:os} (swords)\n"
            "  → *gladios* (swords) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the swords had been had\n"
            "• vide{B:runt} (saw)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* is the perfect stem (from *vidi*)\n"
            "  → *-{B:erunt}* / *-{B:runt}* shows it is the they form of the perfect\n"
            "• de{T:os} (the gods)\n"
            "  → *deos* (gods) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the gods were seen"
        ),
    },
    {
        "latin": "regina filium iusserat deam videre, et filius statim vidit.",
        "english": [
            "The queen had ordered the son to see the goddess, and the son immediately saw her.",
            "The queen had ordered the son to look at the goddess, and the son immediately saw her.",
            "The queen had commanded her son to see the goddess, and the son immediately saw her.",
            "The queen had ordered her son to see the goddess, and the son at once saw her.",
            "The queen had ordered her son to look at the goddess, and the son saw her immediately.",
        ],
        "explanation": (
            "• regin{T:a} (the queen)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• iuss{M:era}{B:t} (had ordered)\n"
            "  → *iubeo* (I order) is the dictionary form of this verb\n"
            "  → *iuss-* is the perfect stem (from *iussi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — the ordering had happened before the seeing\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• fili{T:um} (the son)\n"
            "  → *filium* (son) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → *iubeo* + accusative + infinitive: 'order X to do Y'\n"
            "  → the {T:accusative} marks who is being ordered\n"
            "• de{T:am} (the goddess)\n"
            "  → *deam* (goddess) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *videre* — the goddess is to be seen\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• videre (to see)\n"
            "  → *videre* is the infinitive of *video* (I see), 2nd conjugation\n"
            "  → the infinitive completes the *iubeo* structure: 'had ordered him TO see the goddess'\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb\n"
            "• vidi{B:t} (saw)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* is the perfect stem (from *vidi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect"
        ),
    },
    {
        "latin": "gladium in silva vidi; ingens enim erat.",
        "english": [
            "I saw the sword in the wood; for it was huge.",
            "I saw the sword in the forest; for it was huge.",
            "I saw a sword in the wood; for it was huge.",
            "I saw the sword in the wood; because it was huge.",
            "I saw the sword in the wood; for it was enormous.",
            "I saw the sword in the wood; for it was vast.",
            "I have seen the sword in the wood; for it was huge.",
        ],
        "explanation": (
            "• vidi (I saw)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* is the perfect stem (from *vidi*)\n"
            "  → the *-{B:i}* ending shows it is the I form of the perfect tense\n"
            "• gladi{T:um} (the sword)\n"
            "  → *gladium* (sword) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the sword was seen\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• in silv{T:a} (in the wood)\n"
            "  → *in + ablative* = in / on\n"
            "  → *silv{T:a}* (wood) is the {T:ablative} singular\n"
            "• ingens (huge)\n"
            "  → *ingens* (huge) is an adjective referring back to *gladium* (sword)\n"
            "  → it is used as a predicate after *erat*: 'for it was huge'\n"
            "• enim (for / because)\n"
            "  → *enim* (for / because) is a connector — postpositive, so it comes as the 2nd word in its clause\n"
            "• erat (was)\n"
            "  → *erat* is the imperfect of *esse* (to be): 'was'\n"
            "  → it describes a state: 'it was huge'"
        ),
    },
    {
        "latin": "omnes igitur amici e navi apparuerunt, et urbem viderunt.",
        "english": [
            "Therefore all the friends appeared from the ship, and saw the city.",
            "Therefore all the friends appeared out of the ship, and saw the city.",
            "So all the friends appeared from the ship, and saw the city.",
            "So all the friends appeared out of the ship, and saw the city.",
            "And so all the friends appeared from the ship, and saw the city.",
            "And so all the friends appeared out of the ship, and saw the city.",
            "Therefore all the friends came into view from the ship, and saw the city.",
            "Therefore all the friends came into view out of the ship, and saw the city.",
            "Therefore all the friends appeared from the ship, and have seen the city.",
            "Therefore all the friends appeared from the ship, and they saw the city.",
            "Therefore all the friends appeared out of the ship, and they saw the city.",
        ],
        "explanation": (
            "• omn{T:es} amici (all the friends)\n"
            "  → *omnes* (all) agrees with *amici* (friends) as both are masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• igitur (therefore)\n"
            "  → *igitur* (therefore / so) is a connector — postpositive, placed 2nd in its clause\n"
            "• e nav{T:i} (from the ship)\n"
            "  → *e* / *ex + ablative* = out of / from\n"
            "  → *nav{T:i}* (ship) is the {T:ablative} singular — 3rd declension\n"
            "• apparu{B:erunt} (appeared)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect\n"
            "• vide{B:runt} (saw)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* is the perfect stem (from *vidi*)\n"
            "  → *-{B:erunt}* / *-{B:runt}* shows it is the they form of the perfect\n"
            "• urb{T:em} (the city)\n"
            "  → *urbem* (city) is a noun, 3rd declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the city was seen\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "pater in silva erat, et filium prope insulam vidit.",
        "english": [
            "The father was in the wood, and saw the son near the island.",
            "The father was in the wood, and he saw the son near the island.",
            "The father was in the forest, and saw his son near the island.",
            "The father was in the forest, and he saw his son near the island.",
            "The father was in the wood, and saw his son close to the island.",
            "The father was in the wood, and he saw his son close to the island.",
            "The father was in the wood, and saw his son near the island.",
            "The father was in the wood, and saw the son next to the island.",
            "The father was in the wood, and he saw the son next to the island.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• in silv{T:a} (in the wood)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *silv{T:a}* (wood) is the {T:ablative} singular\n"
            "• erat (was)\n"
            "  → *erat* is the imperfect of *esse* (to be): 'was'\n"
            "  → it describes a background state while the seeing happened\n"
            "• vidi{B:t} (saw)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* is the perfect stem (from *vidi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect\n"
            "• fili{T:um} (the son)\n"
            "  → *filium* (son) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the son was seen\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• prope insul{T:am} (near the island)\n"
            "  → *prope + accusative* = near / close to\n"
            "  → *insul{T:am}* (island) is the {T:accusative} singular"
        ),
    },
    {
        "latin": "subito dea apparuit, et feminae persuasit.",
        "english": [
            "Suddenly the goddess appeared, and persuaded the woman.",
            "The goddess suddenly appeared, and persuaded the woman.",
            "Suddenly, the goddess appeared, and persuaded the woman.",
            "The goddess suddenly came into view, and persuaded the woman.",
        ],
        "explanation": (
            "• subito (suddenly)\n"
            "  → *subito* (suddenly) is an adverb — here at the start for dramatic emphasis\n"
            "• de{T:a} (the goddess)\n"
            "  → *dea* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• apparu{B:it} (appeared)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect\n"
            "• femin{T:ae} (the woman)\n"
            "  → *feminae* here is the {T:dative} singular of *femina* (woman)\n"
            "  → *persuadeo* takes the {T:dative}: 'persuaded the woman'\n"
            "  → careful: *femin{T:ae}* can also be nominative plural ('women') — but the singular subject *dea* confirms this is dative singular\n"
            "• persuas{B:it} (persuaded)\n"
            "  → *persuadeo* (I persuade) is the dictionary form of this verb\n"
            "  → *persuas-* is the perfect stem (from *persuasi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect"
        ),
    },
]


# ── Set 14 (id 30): PPP / Passive review ────────────────────────────────────
# Pluperfect passive removed throughout (out of Eduqas scope) — perfect
# passive (*PPP + est*/sunt) used instead. Ideal: 'was Xed', not 'has been Xed'.
SENTENCES_PPP_N2 = [
    {
        "latin": "filius visus apparuit.",
        "english": [
            "The son, having been seen, appeared.",
            "The son, seen, appeared.",
            "The son who had been seen appeared.",
            "Once seen, the son appeared.",
            "The son, having been seen, came into view.",
            "The son, having been spotted, appeared.",
        ],
        "explanation": (
            "• fili{T:us} vis{T:us} (the son, having been seen)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "  → *visus* is the PPP (perfect passive participle) of *video* (I see)\n"
            "  → *visus* agrees with *filius* as both are masculine singular {T:nominative}\n"
            "  → the PPP means 'having been Xed': 'having been seen'\n"
            "• apparu{B:it} (appeared)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect"
        ),
    },
    {
        "latin": "gladii tenti sunt.",
        "english": [
            "The swords were held.",
            "The swords have been held.",
        ],
        "explanation": (
            "• gladi{T:i} (the swords)\n"
            "  → *gladii* (swords) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → in a passive sentence, the thing being acted on is in the {T:nominative}\n"
            "• tent{T:i} sunt (were held)\n"
            "  → *tenti* is the PPP of *teneo* (I hold), masculine plural {T:nominative}\n"
            "  → *tenti* agrees with *gladii* as both are masculine plural {T:nominative}\n"
            "  → *PPP + sunt* = perfect passive 3rd person plural: 'were held'\n"
            "  → the ideal translation is 'were held', not 'have been held'"
        ),
    },
    {
        "latin": "amicus iussus statim gladium tenuit.",
        "english": [
            "The friend, having been ordered, immediately held a sword.",
            "The friend, having been ordered, held a sword immediately.",
            "The friend who had been ordered immediately held a sword.",
            "Once ordered, the friend immediately held a sword.",
            "The friend, having been ordered, at once held a sword.",
            "The friend, having been ordered, immediately kept hold of a sword.",
        ],
        "explanation": (
            "• amic{T:us} iuss{T:us} (the friend, having been ordered)\n"
            "  → *amicus* (friend) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → *iussus* is the PPP of *iubeo* (I order), masculine singular {T:nominative}\n"
            "  → *iussus* agrees with *amicus* as both are masculine singular {T:nominative}\n"
            "  → the PPP means 'having been ordered'\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• gladi{T:um} (a sword)\n"
            "  → *gladium* (sword) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the sword was held\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• tenu{B:it} (held)\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *tenu-* is the perfect stem (note: the present stem is *ten-*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect"
        ),
    },
    {
        "latin": "dea visa apparuit, et omnes perterriti erant.",
        "english": [
            "The goddess, having been seen, appeared, and all were terrified.",
            "The goddess, having been seen, appeared, and everyone was terrified.",
            "The goddess who had been seen appeared, and all were terrified.",
            "The goddess, having been seen, appeared, and all were frightened.",
            "The goddess, having been seen, appeared, and all of them were terrified.",
            "The seen goddess appeared, and all were terrified.",
            "The seen goddess appeared, and everyone was terrified.",
            "The goddess who was seen appeared, and all were terrified.",
            "The goddess who was seen appeared, and everyone was terrified.",
        ],
        "explanation": (
            "• de{T:a} vis{T:a} (the goddess, having been seen)\n"
            "  → *dea* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → *visa* is the PPP of *video* (I see), feminine singular {T:nominative}\n"
            "  → *visa* agrees with *dea* as both are feminine singular {T:nominative}\n"
            "  → the PPP agrees with the noun it describes in gender, number, and case\n"
            "• apparu{B:it} (appeared)\n"
            "  → *appareo* (I appear) is the dictionary form; *apparu-* is the perfect stem\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect\n"
            "• omn{T:es} perterriti (all, terrified)\n"
            "  → *omnes* (all) is the {T:nominative} plural — {N:subject} of *erant*\n"
            "  → *perterriti* (terrified) is an adjective, masculine plural {T:nominative}, agreeing with *omnes*\n"
            "• erant (were)\n"
            "  → *erant* is the imperfect plural of *esse* (to be): 'were'\n"
            "  → it describes a state: 'all were terrified'"
        ),
    },
    {
        "latin": "pater filios visos tenuit.",
        "english": [
            "The father held the sons, having been seen.",
            "The father kept the sons, having been spotted.",
            "The father held the sons who had been seen.",
            "The father kept hold of the sons who had been seen.",
            "The father held the sons that had been seen.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• fili{T:os} vis{T:os} (the sons, having been seen)\n"
            "  → *filios* (sons) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the sons are being held\n"
            "  → *visos* is the PPP of *video* (I see), masculine plural {T:accusative}\n"
            "  → *visos* agrees with *filios* as both are masculine plural {T:accusative}\n"
            "  → the PPP describes the sons: 'the sons, having been seen'\n"
            "• tenu{B:it} (held)\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *tenu-* is the perfect stem (note: the present stem is *ten-*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect"
        ),
    },
    {
        "latin": "gladius tentus est, sed amicus non apparuit.",
        "english": [
            "The sword was held, but the friend did not appear.",
            "The sword has been held, but the friend did not appear.",
            "The sword was held, but the friend did not come into view.",
        ],
        "explanation": (
            "• gladi{T:us} (the sword)\n"
            "  → *gladius* (sword) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → in a passive sentence, the thing being acted on is in the {T:nominative}\n"
            "• tent{T:us} est (was held)\n"
            "  → *tentus* is the PPP of *teneo* (I hold), masculine singular {T:nominative}\n"
            "  → *tentus* agrees with *gladius* as both are masculine singular {T:nominative}\n"
            "  → *PPP + est* = perfect passive 3rd person singular: 'was held'\n"
            "  → the ideal translation is 'was held', not 'has been held'\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast with the first clause\n"
            "• amic{T:us} (the friend)\n"
            "  → *amicus* (friend) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second verb\n"
            "• non apparu{B:it} (did not appear)\n"
            "  → *non* (not) negates the verb\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect"
        ),
    },
    {
        "latin": "filii iussi sunt gladios tenere, et statim tenuerunt.",
        "english": [
            "The sons were ordered to hold swords, and immediately held them.",
            "The sons have been ordered to hold swords, and immediately held them.",
            "The sons were commanded to hold swords, and immediately held them.",
            "The sons were ordered to hold the swords, and immediately held them.",
            "The sons were ordered to hold swords, and at once held them.",
            "The sons were ordered to hold swords, and held them immediately.",
        ],
        "explanation": (
            "• fili{T:i} (the sons)\n"
            "  → *filii* (sons) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → in a passive sentence, the thing being acted on is in the {T:nominative}\n"
            "• iuss{T:i} sunt (were ordered)\n"
            "  → *iussi* is the PPP of *iubeo* (I order), masculine plural {T:nominative}\n"
            "  → *PPP + sunt* = perfect passive 3rd person plural: 'were ordered'\n"
            "  → *iubeo* passive + infinitive: 'X were ordered to Y'\n"
            "• gladi{T:os} (swords)\n"
            "  → *gladios* (swords) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} of *tenere* — the swords are to be held\n"
            "• tenere (to hold)\n"
            "  → *tenere* is the infinitive of *teneo* (I hold), 2nd conjugation\n"
            "  → the infinitive completes the passive *iubeo* structure: 'were ordered TO hold swords'\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb\n"
            "• tenu{B:erunt} (held)\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *tenu-* is the perfect stem (note: the present stem is *ten-*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect"
        ),
    },
    {
        "latin": "ingens gladius habitus est ab amico, sed amicus gladium non tenuit.",
        "english": [
            "A huge sword was had by the friend, but the friend did not hold the sword.",
            "An enormous sword was had by the friend, but the friend did not hold the sword.",
            "A vast sword was had by the friend, but the friend did not hold the sword.",
            "A huge sword was owned by the friend, but the friend did not hold the sword.",
            "A huge sword was possessed by the friend, but the friend did not hold the sword.",
            "A huge sword has been had by the friend, but the friend did not hold the sword.",
        ],
        "explanation": (
            "• ingens gladi{T:us} (a huge sword)\n"
            "  → *ingens* (huge) is an adjective, singular {T:nominative}\n"
            "  → *gladius* (sword) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → *ingens* agrees with *gladius* as both are singular {T:nominative}\n"
            "  → in a passive sentence, the thing being acted on is in the {T:nominative}\n"
            "• habit{T:us} est (was had)\n"
            "  → *habitus* is the PPP of *habeo* (I have), masculine singular {T:nominative}\n"
            "  → *PPP + est* = perfect passive 3rd person singular: 'was had'\n"
            "  → 'was had' is awkward in English — 'was owned' or 'was possessed' sounds more natural\n"
            "• ab amic{T:o} (by the friend)\n"
            "  → *a* / *ab + ablative* = 'by' — marks the agent who performed the action in a passive sentence\n"
            "  → *amic{T:o}* (friend) is the {T:ablative} singular\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast with the first clause\n"
            "• amic{T:us} (the friend)\n"
            "  → *amicus* (friend) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second verb\n"
            "• non tenu{B:it} (did not hold)\n"
            "  → *non* (not) negates the verb\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *tenu-* is the perfect stem (note: the present stem is *ten-*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect\n"
            "• gladi{T:um} (the sword)\n"
            "  → *gladium* (sword) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the sword was not held\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "multae feminae a deis visae sunt, sed reginae tristes non apparuerunt.",
        "english": [
            "Many women were seen by the gods, but the sad queens did not appear.",
            "Many women have been seen by the gods, but the sad queens did not appear.",
            "Many women were seen by the gods, but the unhappy queens did not appear.",
            "Many of the women were seen by the gods, but the sad queens did not appear.",
        ],
        "explanation": (
            "• mult{T:ae} femin{T:ae} (many women)\n"
            "  → *multae* (many) agrees with *feminae* (women) as both are 1st declension feminine plural {T:nominative}\n"
            "  → in a passive sentence, the thing being acted on is in the {T:nominative}\n"
            "• a de{T:is} (by the gods)\n"
            "  → *a* / *ab + ablative* = 'by' — the agent in a passive sentence\n"
            "  → *de{T:is}* (gods) is the {T:ablative} plural\n"
            "• vis{T:ae} sunt (were seen)\n"
            "  → *visae* is the PPP of *video* (I see), feminine plural {T:nominative}\n"
            "  → *PPP + sunt* = perfect passive they form: 'were seen'\n"
            "  → *visae* agrees with *feminae* as both are feminine plural {T:nominative}\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast with the first clause\n"
            "• regin{T:ae} tristes (the sad queens)\n"
            "  → *reginae* (queens) is a noun, 1st declension feminine plural {T:nominative}\n"
            "  → *tristes* (sad) is an adjective, plural {T:nominative}, agreeing with *reginae*\n"
            "  → the {T:nominative} is the {N:subject} of *apparuerunt*\n"
            "• non apparu{B:erunt} (did not appear)\n"
            "  → *non* (not) negates the verb\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect"
        ),
    },
    {
        "latin": "omnes filii a deis visi sunt, et statim e navi apparuerunt.",
        "english": [
            "All the sons were seen by the gods, and immediately appeared from the ship.",
            "All the sons have been seen by the gods, and immediately appeared from the ship.",
            "All of the sons were seen by the gods, and immediately appeared from the ship.",
            "All the sons were spotted by the gods, and immediately appeared from the ship.",
            "All the sons were seen by the gods, and at once appeared from the ship.",
        ],
        "explanation": (
            "• omn{T:es} fili{T:i} (all the sons)\n"
            "  → *omnes* agrees with *filii* as both are masculine plural {T:nominative}\n"
            "  → in a passive sentence, the thing being acted on is in the {T:nominative}\n"
            "• a de{T:is} (by the gods)\n"
            "  → *a* / *ab + ablative* = 'by' — the agent in a passive sentence\n"
            "  → *de{T:is}* (gods) is the {T:ablative} plural\n"
            "• vis{T:i} sunt (were seen)\n"
            "  → *visi* is the PPP of *video* (I see), masculine plural {T:nominative}\n"
            "  → *PPP + sunt* = perfect passive they form: 'were seen'\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb — flexible position\n"
            "• e nav{T:i} (from the ship)\n"
            "  → *e* / *ex + ablative* = out of / from\n"
            "  → *nav{T:i}* (ship) is the {T:ablative} singular\n"
            "• apparu{B:erunt} (appeared)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect"
        ),
    },
]


# ── Set 16 (id 32): Exam-level mixed review ─────────────────────────────────
SENTENCES_REVIEW_N2 = [
    {
        "latin": "pulcher pater filium tentum vidit, et filium statim iussit apparere.",
        "english": [
            "The beautiful father saw the son, having been held, and immediately ordered the son to appear.",
            "The beautiful father saw the captive son, and immediately ordered the son to appear.",
            "The beautiful father saw the son who had been held, and immediately ordered the son to appear.",
            "The beautiful father saw the son, having been held, and at once ordered the son to appear.",
            "The beautiful father saw the held son, and immediately ordered him to appear.",
        ],
        "explanation": (
            "• pulcher pater (the beautiful father)\n"
            "  → *pulcher* (beautiful) is an adjective, masculine singular {T:nominative}\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → *pulcher* agrees with *pater* as both are masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• vidi{B:t} (saw)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* is the perfect stem (from *vidi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect\n"
            "• fili{T:um} tent{T:um} (the son, having been held)\n"
            "  → *filium* (son) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → *tentum* is the PPP of *teneo* (I hold), masculine singular {T:accusative}\n"
            "  → *tentum* agrees with *filium* as both are masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the held son is being seen\n"
            "• iuss{B:it} (ordered)\n"
            "  → *iubeo* (I order) is the dictionary form of this verb\n"
            "  → *iuss-* is the perfect stem (from *iussi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect\n"
            "• fili{T:um} (the son)\n"
            "  → second {T:accusative}: *iubeo* + accusative + infinitive: 'order X to Y'\n"
            "• statim (immediately)\n"
            "  → *statim* (immediately / at once) is an adverb\n"
            "• apparere (to appear)\n"
            "  → *apparere* is the infinitive of *appareo* (I appear), 2nd conjugation\n"
            "  → the infinitive completes *iubeo*: 'ordered the son TO appear'"
        ),
    },
    {
        "latin": "omnes amici in silva apparuerunt, gladiosque tenebant.",
        "english": [
            "All the friends appeared in the wood, and were holding swords.",
            "All the friends appeared in the forest, and were holding swords.",
            "All of the friends appeared in the wood, and were holding swords.",
            "All the friends came into view in the wood, and were holding swords.",
            "All the friends appeared in the wood, and were holding the swords.",
        ],
        "explanation": (
            "• omn{T:es} amici (all the friends)\n"
            "  → *omnes* (all) agrees with *amici* (friends) as both are masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• in silv{T:a} (in the wood)\n"
            "  → *in + ablative* = in / on (location)\n"
            "  → *silv{T:a}* (wood) is the {T:ablative} singular\n"
            "• apparu{B:erunt} (appeared)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect\n"
            "• ten{R:e}{P:ba}{B:nt} (were holding)\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *ten-* (hold) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker — the holding was ongoing background\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "  → tense shift: *apparuerunt* (perfect — completed action) then *tenebant* (imperfect — ongoing background)\n"
            "• gladios -que (swords and)\n"
            "  → *-que* means 'and' — it clips onto the end of a word, but you translate 'and' BEFORE that word. So *gladiosque* = '... and swords'\n"
            "  → it works just like *et* (and) but is glued onto the following word"
        ),
    },
    {
        "latin": "pulchra dea filium vix vidit, nam silva ingens erat.",
        "english": [
            "The beautiful goddess scarcely saw the son, for the wood was huge.",
            "The beautiful goddess scarcely saw the son, for the wood was huge.",
            "The beautiful goddess hardly saw her son, for the wood was huge.",
            "The beautiful goddess barely saw her son, for the wood was huge.",
            "The beautiful goddess scarcely saw her son, because the wood was huge.",
            "The beautiful goddess scarcely saw her son, for the forest was huge.",
            "The beautiful goddess scarcely saw her son, for the wood was enormous.",
            "The beautiful goddess scarcely saw her son, for the wood was vast.",
            "The lovely goddess scarcely saw her son, for the wood was huge.",
            "The pretty goddess scarcely saw her son, for the wood was huge.",
        ],
        "explanation": (
            "• pulchr{T:a} de{T:a} (the beautiful goddess)\n"
            "  → *pulchra* (beautiful) is an adjective, feminine singular {T:nominative}\n"
            "  → *dea* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → *pulchra* agrees with *dea* as both are feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• vix (scarcely)\n"
            "  → *vix* (scarcely / hardly / barely) is an adverb — flexible position\n"
            "• vidi{B:t} (saw)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* is the perfect stem (from *vidi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect\n"
            "• fili{T:um} (the son)\n"
            "  → *filium* (son) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the son was scarcely seen\n"
            "  → if it ends in *-m*, it's happening to them!\n"
            "• nam (for / because)\n"
            "  → *nam* (for / because / since) gives a reason — unlike *enim*, it can go at the start of its clause\n"
            "• silv{T:a} ingens (the huge wood)\n"
            "  → *silva* (wood) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → *ingens* (huge) is an adjective agreeing with *silva*\n"
            "• erat (was)\n"
            "  → *erat* is the imperfect of *esse* (to be): 'was'\n"
            "  → it describes a state: 'the wood was huge'"
        ),
    },
    {
        "latin": "regina filio persuaserat, sed filius tamen mox non apparuit.",
        "english": [
            "The queen had persuaded the son, but the son however did not soon appear.",
            "The queen had persuaded the son, but the son however did not soon appear.",
            "The queen had persuaded her son, but the son nevertheless did not soon appear.",
            "The queen had persuaded her son, but the son however did not appear soon.",
            "The queen had persuaded her son, but the son did not however appear soon.",
        ],
        "explanation": (
            "• regin{T:a} (the queen)\n"
            "  → *regina* (queen) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• fili{T:o} (the son)\n"
            "  → *filio* is the {T:dative} singular of *filius* (son)\n"
            "  → *persuadeo* takes the {T:dative}: 'persuaded the son'\n"
            "• persuas{M:era}{B:t} (had persuaded)\n"
            "  → *persuadeo* (I persuade) is the dictionary form of this verb\n"
            "  → *persuas-* is the perfect stem (from *persuasi*)\n"
            "  → *-{M:era}-* is the pluperfect marker — 'had persuaded' (before another past event)\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast with the first clause\n"
            "• fili{T:us} (the son)\n"
            "  → *filius* (son) is a noun, 2nd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second verb\n"
            "• tamen (however)\n"
            "  → *tamen* (however / nevertheless) is a connector — adds contrast\n"
            "• mox (soon)\n"
            "  → *mox* (soon) is an adverb — flexible position\n"
            "• non apparu{B:it} (did not appear)\n"
            "  → *non* (not) negates the verb\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect"
        ),
    },
    {
        "latin": "amici naves habuerant, et insulam viderant.",
        "english": [
            "The friends had had ships, and had seen the island.",
            "The friends had owned ships, and had seen the island.",
            "The friends had possessed ships, and had seen the island.",
            "The friends had had ships, and had spotted the island.",
            "The friends had had the ships, and had seen the island.",
        ],
        "explanation": (
            "• amici (the friends)\n"
            "  → *amici* (friends) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does both verbs\n"
            "• habu{M:era}{B:nt} (had had)\n"
            "  → *habeo* (I have) is the dictionary form of this verb\n"
            "  → *habu-* is the perfect stem (from *habui*)\n"
            "  → *-{M:era}-* is the pluperfect marker: 'had had'\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• nav{T:es} (ships)\n"
            "  → *naves* (ships) is a noun, 3rd declension feminine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the ships had been had\n"
            "• vide{M:ra}{B:nt} (had seen)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* is the perfect stem (from *vidi*); *-era-* shortens to *-ra-* before *-nt*\n"
            "  → *-{M:ra}-* is the pluperfect marker: 'had seen'\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• insul{T:am} (the island)\n"
            "  → *insulam* (island) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the island had been seen\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "dea pulchra in silva apparuerat, sed amici deam non viderant.",
        "english": [
            "The beautiful goddess had appeared in the wood, but the friends had not seen the goddess.",
            "The beautiful goddess had appeared in the forest, but the friends had not seen the goddess.",
            "The lovely goddess had appeared in the wood, but the friends had not seen the goddess.",
            "The pretty goddess had appeared in the wood, but the friends had not seen the goddess.",
        ],
        "explanation": (
            "• de{T:a} pulchr{T:a} (the beautiful goddess)\n"
            "  → *dea* (goddess) is a noun, 1st declension feminine singular {T:nominative}\n"
            "  → *pulchra* (beautiful) is an adjective, feminine singular {T:nominative}\n"
            "  → *pulchra* agrees with *dea* as both are feminine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• in silv{T:a} (in the wood)\n"
            "  → *in + ablative* = in / on\n"
            "  → *silv{T:a}* (wood) is the {T:ablative} singular\n"
            "• apparu{M:era}{B:t} (had appeared)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{M:era}-* is the pluperfect marker: 'had appeared'\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast with the first clause\n"
            "• amici (the friends)\n"
            "  → *amici* (friends) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second verb\n"
            "• non vide{M:ra}{B:nt} (had not seen)\n"
            "  → *non* (not) negates the verb\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* is the perfect stem (from *vidi*); *-era-* shortens to *-ra-* before *-nt*\n"
            "  → *-{M:ra}-* is the pluperfect marker: 'had seen'\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• de{T:am} (the goddess)\n"
            "  → *deam* (goddess) is a noun, 1st declension feminine singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the goddess had not been seen\n"
            "  → if it ends in *-m*, it's happening to them!"
        ),
    },
    {
        "latin": "tu ingentem gladium tenuisti, et omnes te viderunt.",
        "english": [
            "You held the huge sword, and everyone saw you.",
            "You yourself held the huge sword, and everyone saw you.",
            "You held the enormous sword, and everyone saw you.",
            "You held the vast sword, and everyone saw you.",
            "You held the huge sword, and all saw you.",
            "You held the huge sword, and all of them saw you.",
            "You held the huge sword, and all people saw you.",
            "You held a huge sword, and everyone saw you.",
        ],
        "explanation": (
            "• tu (you)\n"
            "  → *tu* (you) is the {T:nominative} singular of the 2nd person pronoun — added for emphasis\n"
            "  → the *-isti* ending of *tenuisti* already shows you (singular) is the subject\n"
            "• tenu{B:isti} (you held)\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *tenu-* is the perfect stem (note: the present stem is *ten-*)\n"
            "  → *-{B:isti}* shows it is the you (singular) form of the perfect tense\n"
            "• ingent{T:em} gladi{T:um} (a huge sword)\n"
            "  → *ingentem* (huge) is an adjective, singular {T:accusative}\n"
            "  → *gladium* (sword) is a noun, 2nd declension masculine singular {T:accusative}\n"
            "  → *ingentem* agrees with *gladium* as both are singular {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the sword was held\n"
            "• omn{T:es} (all / everyone)\n"
            "  → *omnes* (all) is a pronoun / adjective, plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of *viderunt*\n"
            "• vide{B:runt} (saw)\n"
            "  → *video* (I see) is the dictionary form of this verb\n"
            "  → *vid-* is the perfect stem (from *vidi*)\n"
            "  → *-{B:erunt}* / *-{B:runt}* shows it is the they form of the perfect\n"
            "• te (you)\n"
            "  → *te* is the {T:accusative} singular of *tu* (you)\n"
            "  → the {T:accusative} is the {N:object} — you are being seen"
        ),
    },
    {
        "latin": "subito multi dei apparuerunt, et omnes perterriti erant.",
        "english": [
            "Suddenly many gods appeared, and all were terrified.",
            "Suddenly many gods appeared, and everyone was terrified.",
            "Suddenly many gods appeared, and all were frightened.",
            "Many gods suddenly appeared, and all were terrified.",
            "Suddenly many gods appeared, and all of them were terrified.",
            "Suddenly many gods appeared, and everyone was very scared.",
        ],
        "explanation": (
            "• subito (suddenly)\n"
            "  → *subito* (suddenly) is an adverb — here at the start for dramatic emphasis\n"
            "• mult{T:i} de{T:i} (many gods)\n"
            "  → *multi* (many) is an adjective, masculine plural {T:nominative}\n"
            "  → *dei* (gods) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → *multi* agrees with *dei* as both are masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of *apparuerunt*\n"
            "• apparu{B:erunt} (appeared)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *apparu-* is the perfect stem (from *apparui*)\n"
            "  → *-{B:erunt}* shows it is the they form of the perfect\n"
            "• omn{T:es} perterriti (all, terrified)\n"
            "  → *omnes* (all) is the {T:nominative} plural — {N:subject} of *erant*\n"
            "  → *perterriti* (terrified) is an adjective, masculine plural {T:nominative}\n"
            "  → *perterriti* agrees with *omnes* — they are all terrified\n"
            "• erant (were)\n"
            "  → *erant* is the imperfect plural of *esse* (to be): 'were'\n"
            "  → it describes the state caused by the gods' appearance: 'all were terrified'"
        ),
    },
    {
        "latin": "pater filios iubebat e silva apparere, sed filii tamen gladios tenebant.",
        "english": [
            "The father was ordering the sons to appear from the wood, but the sons however were holding swords.",
            "The father was ordering the sons to come out of the wood, but the sons however were holding swords.",
            "The father was commanding his sons to appear from the wood, but the sons however were holding swords.",
            "The father was ordering his sons to appear from the forest, but the sons however were holding swords.",
            "The father kept ordering his sons to appear from the wood, but the sons however were holding swords.",
            "The father used to order his sons to appear from the wood, but the sons however were holding swords.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• iub{R:e}{P:ba}{B:t} (was ordering)\n"
            "  → *iubeo* (I order) is the dictionary form of this verb\n"
            "  → *iub-* (order) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker — the ordering was ongoing\n"
            "  → *-{B:t}* shows it is the he/she/it form\n"
            "• fili{T:os} (the sons)\n"
            "  → *filios* (sons) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → *iubeo* + accusative + infinitive: 'order X to do Y'\n"
            "  → the {T:accusative} marks who is being ordered\n"
            "• e silv{T:a} (from the wood)\n"
            "  → *e* / *ex + ablative* = out of / from\n"
            "  → *silv{T:a}* (wood) is the {T:ablative} singular\n"
            "• apparere (to appear)\n"
            "  → *apparere* is the infinitive of *appareo* (I appear), 2nd conjugation\n"
            "  → the infinitive completes the *iubeo* structure: 'was ordering them TO appear'\n"
            "• sed (but)\n"
            "  → *sed* (but) is a conjunction — introduces a contrast with the first clause\n"
            "• fili{T:i} (the sons)\n"
            "  → *filii* (sons) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of the second verb\n"
            "• tamen (however)\n"
            "  → *tamen* (however / nevertheless) is a connector — adds contrast\n"
            "• ten{R:e}{P:ba}{B:nt} (were holding)\n"
            "  → *teneo* (I hold) is the dictionary form of this verb\n"
            "  → *ten-* (hold) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker — the holding was ongoing\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "• gladi{T:os} (swords)\n"
            "  → *gladios* (swords) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → the {T:accusative} is the {N:object} — the swords were being held"
        ),
    },
    {
        "latin": "pater filios igitur iussit gladios tenere; apparebant enim amici.",
        "english": [
            "Therefore the father ordered the sons to hold swords; for the friends were appearing.",
            "So the father ordered his sons to hold swords; for the friends were appearing.",
            "And so the father ordered his sons to hold swords; for the friends were appearing.",
            "Therefore the father commanded his sons to hold swords; for the friends were appearing.",
            "Therefore the father ordered his sons to hold the swords; for the friends were appearing.",
            "Therefore the father ordered his sons to hold swords; because the friends were appearing.",
            "Therefore the father ordered his sons to hold swords; for the friends were coming into view.",
        ],
        "explanation": (
            "• pater (the father)\n"
            "  → *pater* (father) is a noun, 3rd declension masculine singular {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} so it does the verb\n"
            "• igitur (therefore)\n"
            "  → *igitur* (therefore / so) is a connector — postpositive, placed 2nd in its clause\n"
            "• iuss{B:it} (ordered)\n"
            "  → *iubeo* (I order) is the dictionary form of this verb\n"
            "  → *iuss-* is the perfect stem (from *iussi*)\n"
            "  → *-{B:it}* shows it is the he/she/it form of the perfect\n"
            "• fili{T:os} (the sons)\n"
            "  → *filios* (sons) is a noun, 2nd declension masculine plural {T:accusative}\n"
            "  → *iubeo* + accusative + infinitive: 'order X to do Y'\n"
            "  → the {T:accusative} marks who is being ordered\n"
            "• gladi{T:os} tenere (to hold swords)\n"
            "  → *gladios* (swords) is {T:accusative} plural — the thing to be held\n"
            "  → *tenere* is the infinitive of *teneo* (I hold) — completes the *iubeo* structure\n"
            "• appar{R:e}{P:ba}{B:nt} (were appearing)\n"
            "  → *appareo* (I appear) is the dictionary form of this verb\n"
            "  → *appar-* (appear) is the stem\n"
            "  → *-{R:e}-* shows it belongs to the 2nd conjugation\n"
            "  → *-{P:ba}-* is the imperfect marker — they were appearing (ongoing background)\n"
            "  → *-{B:nt}* shows it is the they form\n"
            "  → note: the verb *apparebant* comes before its subject *amici* — Latin is flexible with word order\n"
            "• enim (for / because)\n"
            "  → *enim* (for / because) is a connector — postpositive, placed 2nd in its clause\n"
            "• amici (the friends)\n"
            "  → *amici* (friends) is a noun, 2nd declension masculine plural {T:nominative}\n"
            "  → the {T:nominative} is the {N:subject} of *apparebant*"
        ),
    },
]


# ════════════════════════════════════════════════════════════════════════════
# SETS_N2 — exactly 5 set entries (Set 4 / 8 / 12 / 14 / 16) for Node 2.
# Set ids continue from Node 1's last id (20). Mirrors the Node 1 'sentences'
# set shape exactly: id, node, node_title, title, type, sell, pass_mark,
# content. Tile-building sets (vocab cards, verb cards, principal-parts
# trainers, tense ID/MCQ, parsing) are intentionally NOT included here —
# this draft file only carries the **5 sentence sets** the teacher needs to
# review before integration. The principal-parts / table-driven tiles
# (VERBS_2ND_TOP150, TENSE_ID_QUESTIONS_N2, table_note for the present
# tense) live in this file and will be wired into SETS_N2 after the
# sentence content is approved.
# ════════════════════════════════════════════════════════════════════════════

# Table note for the 2nd conjugation present tense tile (used when this
# data file is integrated into the main SETS list).
PRESENT_TABLE_NOTE_2ND = (
    "Colour key:\n"
    "**red** = stem vowel\n"
    "**blue** = person ending"
)


# ── translate_form question generators ──────────────────────────────────────
# Each verb -> 6 forms x 1 ending pattern. Mirror Node 1's QUESTIONS_PRESENT etc.

def _make_3sg_part(phrase):
    """Apply English 3rd-sg rule to ONE verb phrase, preserving any trailing
    particle or parenthetical.  e.g. 'ask (for)' -> 'asks (for)',
    'leave behind' -> 'leaves behind', 'see' -> 'sees'."""
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
    """Given 'I see' -> six person/number translations with correct 3sg form."""
    base = eng_present[2:]  # strip "I "
    irreg_whole = {"make, do": "makes, does"}
    if base in irreg_whole:
        third = irreg_whole[base]
    elif "," in base:
        parts = [p.strip() for p in base.split(",")]
        third = ", ".join(_make_3sg_part(p) for p in parts)
    else:
        third = _make_3sg_part(base)
    return [f"I {base}", f"you (sg) {base}", f"he/she {third}",
            f"we {base}", f"you (pl) {base}", f"they {base}"]

def _opts_present(eng_present):  return _verbset_eng(eng_present)
def _opts_imperf(eng_present):
    base = eng_present[2:]
    # imperfect -> "was X-ing"/"were X-ing"
    # use simple progressive
    if base.endswith("e") and len(base)>2 and base[-2] not in "aeiou":
        ger = base[:-1] + "ing"
    else:
        ger = base + "ing"
    return [f"I was {ger}", f"you (sg) were {ger}", f"he/she was {ger}",
            f"we were {ger}", f"you (pl) were {ger}", f"they were {ger}"]
def _opts_future(eng_present):
    base = eng_present[2:]
    return [f"I will {base}", f"you (sg) will {base}", f"he/she will {base}",
            f"we will {base}", f"you (pl) will {base}", f"they will {base}"]
def _opts_perfect(eng_perfect):
    base = eng_perfect[2:]  # strip "I "  -> e.g. "saw"
    return [f"I {base}", f"you (sg) {base}", f"he/she {base}",
            f"we {base}", f"you (pl) {base}", f"they {base}"]
def _opts_pluperf(eng_perfect):
    # pluperfect -> "had X-ed". Derive from perfect: drop "I " -> add "had X" using base form.
    # Simpler: build from present: "see" -> "had seen". But irregular pasts (saw->seen) don't follow rule.
    # Use a small map for our 6 verbs.
    PAST_PARTICIPLE = {"saw":"seen","had":"had","held":"held","persuaded":"persuaded","ordered":"ordered","appeared":"appeared"}
    base = eng_perfect[2:]
    pp = PAST_PARTICIPLE.get(base, base)
    return [f"I had {pp}", f"you (sg) had {pp}", f"he/she had {pp}",
            f"we had {pp}", f"you (pl) had {pp}", f"they had {pp}"]

# Present-stem forms (I/you-sg/he-she/we/you-pl/they) for each 2nd-conj verb
def _present_stem(pres):
    # video -> vid (drop -eo)
    return pres[:-2]

def _gen_present(verb):
    pres = verb[0]; eng = verb[4]
    s = _present_stem(pres)
    forms = [pres, s+"es", s+"et", s+"emus", s+"etis", s+"ent"]
    eng_set = _opts_present(eng)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]

def _gen_imperfect(verb):
    pres = verb[0]; eng = verb[4]
    s = _present_stem(pres)
    forms = [s+"ebam", s+"ebas", s+"ebat", s+"ebamus", s+"ebatis", s+"ebant"]
    eng_set = _opts_imperf(eng)
    return [{"form":f, "correct":eng_set[i], "options":eng_set} for i,f in enumerate(forms)]

def _gen_future(verb):
    pres = verb[0]; eng = verb[4]
    s = _present_stem(pres)
    forms = [s+"ebo", s+"ebis", s+"ebit", s+"ebimus", s+"ebitis", s+"ebunt"]
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

QUESTIONS_PRESENT_N2    = [q for v in VERBS_2ND_TOP150 for q in _gen_present(v)]
QUESTIONS_IMPERFECT_N2  = [q for v in VERBS_2ND_TOP150 for q in _gen_imperfect(v)]
QUESTIONS_FUTURE_N2     = [q for v in VERBS_2ND_TOP150 for q in _gen_future(v)]
QUESTIONS_PERFECT_N2    = [q for v in VERBS_2ND_TOP150 for q in _gen_perfect(v)]
QUESTIONS_PLUPERFECT_N2 = [q for v in VERBS_2ND_TOP150 for q in _gen_pluperf(v)]


# ── Conjugation tables (translate_form intro screens) ─────────────────────────
TABLE_PRESENT_2ND = [
    {"conjugation":"I",            "infinitive_ending":"-o",   "example":"video",    "ep":[["vid",""],["e","coral"],["o","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-s",   "example":"vides",    "ep":[["vid",""],["e","coral"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-t",   "example":"videt",    "ep":[["vid",""],["e","coral"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-mus", "example":"videmus",  "ep":[["vid",""],["e","coral"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-tis", "example":"videtis",  "ep":[["vid",""],["e","coral"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-nt",  "example":"vident",   "ep":[["vid",""],["e","coral"],["nt","blue"]]},
]

TABLE_IMPERFECT_2ND = [
    {"conjugation":"I",            "infinitive_ending":"-bam",  "example":"videbam",  "tr":"I was seeing",      "ep":[["vid",""],["e","coral"],["ba","purple"],["m","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-bas",  "example":"videbas",  "tr":"you were seeing",   "ep":[["vid",""],["e","coral"],["ba","purple"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-bat",  "example":"videbat",  "tr":"he/she was seeing", "ep":[["vid",""],["e","coral"],["ba","purple"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-bamus","example":"videbamus","tr":"we were seeing",    "ep":[["vid",""],["e","coral"],["ba","purple"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-batis","example":"videbatis","tr":"you were seeing",   "ep":[["vid",""],["e","coral"],["ba","purple"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-bant", "example":"videbant", "tr":"they were seeing",  "ep":[["vid",""],["e","coral"],["ba","purple"],["nt","blue"]]},
]

TABLE_FUTURE_2ND = [
    {"conjugation":"I",            "infinitive_ending":"-bo",   "example":"videbo",   "tr":"I will see",       "ep":[["vid",""],["e","coral"],["bo","purple"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-bis",  "example":"videbis",  "tr":"you will see",      "ep":[["vid",""],["e","coral"],["bi","purple"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-bit",  "example":"videbit",  "tr":"he/she will see",   "ep":[["vid",""],["e","coral"],["bi","purple"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-bimus","example":"videbimus","tr":"we will see",       "ep":[["vid",""],["e","coral"],["bi","purple"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-bitis","example":"videbitis","tr":"you will see",      "ep":[["vid",""],["e","coral"],["bi","purple"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-bunt", "example":"videbunt", "tr":"they will see",     "ep":[["vid",""],["e","coral"],["bu","purple"],["nt","blue"]]},
]

# Perfect: lead with habui (-u- marker — most common in 2nd conj).
# The -u- is the perfect-stem marker; the i + person ending follows.
TABLE_PERFECT_2ND = [
    {"conjugation":"I",            "infinitive_ending":"-i",     "example":"habui",      "tr":"I had",       "ep":[["hab",""],["u","purple"],["i","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-isti",  "example":"habuisti",   "tr":"you had",     "ep":[["hab",""],["u","purple"],["isti","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-it",    "example":"habuit",     "tr":"he/she had",  "ep":[["hab",""],["u","purple"],["it","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-imus",  "example":"habuimus",   "tr":"we had",      "ep":[["hab",""],["u","purple"],["imus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-istis", "example":"habuistis",  "tr":"you had",     "ep":[["hab",""],["u","purple"],["istis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-erunt", "example":"habuerunt",  "tr":"they had",    "ep":[["hab",""],["u","purple"],["erunt","blue"]]},
]

# Pluperfect: same perfect stem (hab + u) + -era- + person ending
TABLE_PLUPERFECT_2ND = [
    {"conjugation":"I",            "infinitive_ending":"-eram",  "example":"habueram",   "tr":"I had had",        "ep":[["hab",""],["u","purple"],["era","pink"],["m","blue"]]},
    {"conjugation":"you (sg)",      "infinitive_ending":"-eras",  "example":"habueras",   "tr":"you had had",      "ep":[["hab",""],["u","purple"],["era","pink"],["s","blue"]]},
    {"conjugation":"he / she / it", "infinitive_ending":"-erat",  "example":"habuerat",   "tr":"he/she had had",   "ep":[["hab",""],["u","purple"],["era","pink"],["t","blue"]]},
    {"conjugation":"we",            "infinitive_ending":"-eramus","example":"habueramus", "tr":"we had had",       "ep":[["hab",""],["u","purple"],["era","pink"],["mus","blue"]]},
    {"conjugation":"you (pl)",      "infinitive_ending":"-eratis","example":"habueratis", "tr":"you had had",      "ep":[["hab",""],["u","purple"],["era","pink"],["tis","blue"]]},
    {"conjugation":"they",          "infinitive_ending":"-erant", "example":"habuerant",  "tr":"they had had",     "ep":[["hab",""],["u","purple"],["era","pink"],["nt","blue"]]},
]


# ── Parse-and-translate questions for the Review set ────────────────────────
PARSE_TRANSLATE_QUESTIONS_N2 = [
    {"form":"vides",       "tense":"present",    "person":"2nd","number":"singular","translation":"you (sg) see"},
    {"form":"habent",      "tense":"present",    "person":"3rd","number":"plural",  "translation":"they have"},
    {"form":"tenemus",     "tense":"present",    "person":"1st","number":"plural",  "translation":"we hold"},
    {"form":"videbat",     "tense":"imperfect",  "person":"3rd","number":"singular","translation":"he/she was seeing"},
    {"form":"habebant",    "tense":"imperfect",  "person":"3rd","number":"plural",  "translation":"they were having"},
    {"form":"tenebam",     "tense":"imperfect",  "person":"1st","number":"singular","translation":"I was holding"},
    {"form":"videbis",     "tense":"future",     "person":"2nd","number":"singular","translation":"you (sg) will see"},
    {"form":"iubebit",     "tense":"future",     "person":"3rd","number":"singular","translation":"he/she will order"},
    {"form":"apparebunt",  "tense":"future",     "person":"3rd","number":"plural",  "translation":"they will appear"},
    {"form":"vidit",       "tense":"perfect",    "person":"3rd","number":"singular","translation":"he/she saw"},
    {"form":"iusserunt",   "tense":"perfect",    "person":"3rd","number":"plural",  "translation":"they ordered"},
    {"form":"persuasisti", "tense":"perfect",    "person":"2nd","number":"singular","translation":"you (sg) persuaded"},
    {"form":"viderat",     "tense":"pluperfect", "person":"3rd","number":"singular","translation":"he/she had seen"},
    {"form":"tenueramus",  "tense":"pluperfect", "person":"1st","number":"plural",  "translation":"we had held"},
    {"form":"habuerant",   "tense":"pluperfect", "person":"3rd","number":"plural",  "translation":"they had had"},
]


# ── Sentence-vocab tile content (filtered to lemmas that actually appear in
# Node 2 sentences, plus BE_FORMS) ──────────────────────────────────────────
_TILE_VOCAB_N2 = _build_tile_vocab(
    SENTENCES_PRESENT_TEST_N2 + SENTENCES_PRESENT_SYSTEM_N2
    + SENTENCES_ACTIVE_N2 + SENTENCES_PPP_N2 + SENTENCES_REVIEW_N2
)


# ── 16-tile Node 2 set list, mirroring Node 1 exactly ───────────────────────
NODE2_TITLE = "2nd Conjugation (Top 150)"

SETS_N2 = [
    # ── Row 1 ────────────────────────────────────────────────────────────────
    {
        "id":21, "node":2, "node_title":NODE2_TITLE,
        "title":"Present: 'I' Form",
        "badge":"Principal Part",
        "type":"verbs",
        "sell":"There are 6 second conjugation verbs in the GCSE Top 150. This set teaches the **first principal part** — the present tense 'I' form.",
        "pass_mark":80,
        "screens":[
            {"heading":"The 1st Principal Part — 2nd conj.",
             "body":"The **1st principal part** is the present tense 'I' form. You can spot a 2nd conjugation verb by the *-e-* stem vowel:\n\n    *video* = I see\n    *habeo* = I have\n    *teneo* = I hold"}
        ],
        "content":{"verbs":VERBS_2ND_TOP150, "mode":"meanings"},
    },
    {
        "id":22, "node":2, "node_title":NODE2_TITLE,
        "title":"Present Tense Endings",
        "type":"translate_form",
        "sell":"This set teaches you all six present tense endings for 2nd conjugation verbs.",
        "pass_mark":80,
        "screens":[
            {"heading":"2nd Conjugation: Present Tense Endings",
             "body":"The person endings are the same across all conjugations — only the stem vowel changes.\n\nThe *-e-* stem vowel is the signature of the 2nd conjugation.",
             "table":TABLE_PRESENT_2ND,
             "table_note":PRESENT_TABLE_NOTE_2ND,
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_PRESENT_N2},
    },
    {
        "id":23, "node":2, "node_title":NODE2_TITLE,
        "title":"Sentence Vocabulary",
        "type":"vocab", "optional":True,
        "sell":"Here are the words that will appear in the sentences of this node. Some of these will already be familiar to you.",
        "pass_mark":80,
        "content":{"vocab":_TILE_VOCAB_N2, "mode":"meanings"},
    },
    {
        "id":24, "node":2, "node_title":NODE2_TITLE,
        "title":"The Present Tense",
        "type":"sentences",
        "sell":"This set practises translating sentences using 2nd conjugation present tense verbs.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PRESENT_TEST_N2},
    },
    # ── Row 2 ────────────────────────────────────────────────────────────────
    {
        "id":25, "node":2, "node_title":NODE2_TITLE,
        "title":"Infinitive",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **second principal part** — the infinitive, or 'to…' form of the verb.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_2ND_TOP150,
            "mode":"infinitives",
            "show_parts_so_far":1,
            "pattern_screen":{
                "title":"2nd Conjugation: The Infinitive",
                "subtitle":"Add -re to the present stem (which ends in -e):",
                "examples":[
                    {"present":"video","full":"videre","ending":"re","english":"to see"},
                    {"present":"habeo","full":"habere","ending":"re","english":"to have"},
                    {"present":"teneo","full":"tenere","ending":"re","english":"to hold"},
                ],
                "footnote":"The present stem of 2nd conjugation verbs ends in *-e*. The infinitive is simply stem + *-re* — and so always ends in *-ere*."
            }
        },
    },
    {
        "id":26, "node":2, "node_title":NODE2_TITLE,
        "title":"The Future Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **future tense** for 2nd conjugation verbs.",
        "pass_mark":80,
        "screens":[
            {"heading":"The Future Tense — 2nd conj.",
             "body":"Where in English we say 'will see', 'will hold' — in Latin the future is formed by adding *-bo-*, *-bi-*, or *-bu-* to the present stem.",
             "table":TABLE_FUTURE_2ND,
             "table_note":"Colour key:\n**red** = stem vowel\n**purple** = tense marker (*-bo-*/*-bi-*/*-bu-*)\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_FUTURE_N2},
    },
    {
        "id":27, "node":2, "node_title":NODE2_TITLE,
        "title":"The Imperfect Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **imperfect tense** — used for continuous or repeated action in the past ('was seeing', 'used to see').",
        "pass_mark":80,
        "screens":[
            {"heading":"The Imperfect Tense — 2nd conj.",
             "body":"The imperfect tense refers to repeated or ongoing action in the past. The endings are *-bam*, *-bas*, *-bat*, *-bamus*, *-batis*, *-bant* — the same across all conjugations. The *-e-* stem vowel is preserved before *-ba-*.",
             "table":TABLE_IMPERFECT_2ND,
             "table_note":"Spot *-ba-* to identify the imperfect immediately. Do not confuse it with the future markers *-bo-*, *-bi-*, *-bu-*.\n\nColour key:\n**red** = stem vowel\n**purple** = tense marker (*-ba-*)\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_IMPERFECT_N2},
    },
    {
        "id":28, "node":2, "node_title":NODE2_TITLE,
        "title":"The Present System",
        "type":"sentences",
        "sell":"This set tests your ability to translate sentences using the present, imperfect, and future tenses with 2nd conjugation verbs.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PRESENT_SYSTEM_N2},
    },
    # ── Row 3 ────────────────────────────────────────────────────────────────
    {
        "id":29, "node":2, "node_title":NODE2_TITLE,
        "title":"Perfect: 'I' Form",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **third principal part** — the perfect 'I' form.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_2ND_TOP150,
            "mode":"perfects",
            "show_parts_so_far":2,
            "pattern_screen":{
                "title":"2nd Conjugation: The Perfect",
                "subtitle":"The perfect is identified by its stem marker. There are four across Latin: *-v-*, *-u-*, *-x-*, and *-s-*. In the 2nd conjugation, look for *-u-* or *-s-* in particular.",
                "examples":[
                    # -u- marker (most common in 2nd conj)
                    {"full":"habui",     "ending":"ui","inf":"habere",    "english":"I had",       "present":"habeo"},
                    {"full":"tenui",     "ending":"ui","inf":"tenere",    "english":"I held",      "present":"teneo"},
                    {"full":"apparui",   "ending":"ui","inf":"apparere",  "english":"I appeared",  "present":"appareo"},
                    # -s- marker
                    {"full":"persuasi",  "ending":"si","inf":"persuadere","english":"I persuaded", "present":"persuadeo"},
                    {"full":"iussi",     "ending":"si","inf":"iubere",    "english":"I ordered",   "present":"iubeo"},
                    # no marker (just vowel change)
                    {"full":"vidi",      "ending":"i", "inf":"videre",    "english":"I saw",       "present":"video"},
                ],
                "footnote":"In the 2nd conjugation:\n\n*-u-*: *habui*, *tenui*, *apparui* — the most common marker\n*-s-*: *persuasi*, *iussi* — where the stem ends in a sibilant\n\n*-v-* and *-x-* do not appear in 2nd conjugation.\n\n★ *vidi* is a special case — it is a **complete stem change**. The stem vowel *-e-* of *video* disappears entirely, giving *vid-i*. Learn it on its own."
            }
        },
    },
    {
        "id":30, "node":2, "node_title":NODE2_TITLE,
        "title":"Perfect Tense: All Endings",
        "type":"translate_form",
        "sell":"This set teaches you all six forms of the **perfect tense** — used for completed actions in the past ('saw', 'held', 'ordered').",
        "pass_mark":80,
        "screens":[
            {"heading":"The Perfect Tense — 2nd conj.",
             "body":"Built on the **perfect stem** (the 3rd principal part, minus the final *-i*).",
             "table":TABLE_PERFECT_2ND,
             "table_note":"The four perfect-stem markers are *-v-*, *-u-*, *-x-*, *-s-*. In this table, the marker is *-u-*. But remember: other 2nd-conj. perfects use *-s-* (e.g. *persuasi*, *iussi*) or have no marker at all (e.g. *vidi*).\n\nColour key:\n**purple** = stem marker\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_PERFECT_N2},
    },
    {
        "id":31, "node":2, "node_title":NODE2_TITLE,
        "title":"The Pluperfect Tense",
        "type":"translate_form",
        "sell":"This set teaches you the **pluperfect tense** — used for actions completed before another past event ('had seen', 'had held').",
        "pass_mark":80,
        "screens":[
            {"heading":"The Pluperfect Tense — 2nd conj.",
             "body":"In English, we express the pluperfect with **'had'** — for example, 'he had seen', 'they had held'.\n\nIn Latin, build on the perfect stem and add the tense marker *-era-* before the person ending.",
             "table":TABLE_PLUPERFECT_2ND,
             "table_note":"The pluperfect uses the same perfect stem as the perfect (here *habu-*), then adds the marker *-era-* and the person ending.\n\n⚠ Don't confuse the perfect ending *-erunt* (they did) with the pluperfect marker *-era-* (had). Whenever *-era-* appears, you are looking at the pluperfect.\n\nColour key:\n**purple** = stem marker\n**pink** = pluperfect marker (*-era-*)\n**blue** = person ending",
             "infinitive_ending_header":"Ending"}
        ],
        "content":{"questions":QUESTIONS_PLUPERFECT_N2},
    },
    {
        "id":32, "node":2, "node_title":NODE2_TITLE,
        "title":"Perfect & Pluperfect",
        "type":"sentences",
        "sell":"This set practises translating sentences using the perfect and pluperfect tenses with 2nd conjugation verbs.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_ACTIVE_N2},
    },
    # ── Row 4 ────────────────────────────────────────────────────────────────
    {
        "id":33, "node":2, "node_title":NODE2_TITLE,
        "title":"Perfect Passive Participle (PPP)",
        "badge":"Principal Part",
        "type":"building_parts",
        "sell":"This set teaches you the **fourth principal part** — the **Perfect Passive Participle (PPP)** for 2nd conjugation verbs.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_2ND_TOP150,
            "mode":"ppps",
            "show_parts_so_far":3,
            "pattern_screen":{
                "title":"2nd Conjugation: The PPP",
                "subtitle":"2nd conjugation PPPs end in *-tus* except where the perfect stem ends in *-s-*, which gives *-sus*:",
                "examples":[
                    {"present":"habeo",    "infinitive":"habere",    "perfect":"habui",    "full":"habitus", "ending":"tus","english":"having been had"},
                    {"present":"teneo",    "infinitive":"tenere",    "perfect":"tenui",    "full":"tentus",  "ending":"tus","english":"having been held"},
                    {"present":"video",    "infinitive":"videre",    "perfect":"vidi",     "full":"visus",   "ending":"sus","english":"having been seen"},
                    {"present":"iubeo",    "infinitive":"iubere",    "perfect":"iussi",    "full":"iussus",  "ending":"sus","english":"having been ordered"},
                ],
                "footnote":"You can always translate a PPP as **'having been'** + the verb's meaning — e.g. *visus* = 'having been seen'. It acts like an adjective in the sentence, agreeing with the noun it describes in gender, number, and case.\n\n**PPP + est / sunt = perfect passive**: *visus est* = 'he was seen'; *visi sunt* = 'they were seen'.\n\nNote: *persuadeo* and *appareo* have no PPP."
            }
        },
    },
    {
        "id":34, "node":2, "node_title":NODE2_TITLE,
        "title":"Perfect Passive Participles",
        "type":"sentences",
        "sell":"You can always translate a PPP as **'having been ___'** — this set practises sentences that contain the Perfect Passive Participle.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PPP_N2},
    },
    {
        "id":35, "node":2, "node_title":NODE2_TITLE,
        "title":"Build the Principal Parts",
        "type":"building_parts",
        "sell":"This set tests all four principal parts of 2nd conjugation verbs in random order. You are given the present 'I' form and must supply the **infinitive**, **perfect**, or **PPP** from memory.",
        "pass_mark":80,
        "content":{"verbs":VERBS_2ND_TOP150, "mode":"all_four", "show_parts_so_far":4, "gap_positions":[1, 2, 3]},
    },
    {
        "id":36, "node":2, "node_title":NODE2_TITLE,
        "title":"Review",
        "type":"review",
        "badge":"test",
        "sell":"This set reviews everything in the node: parse and translate individual verb forms, then translate sentences covering all tenses and PPPs.",
        "pass_mark":80,
        "content":{
            "sentences": SENTENCES_REVIEW_N2,
            "parse_translate": PARSE_TRANSLATE_QUESTIONS_N2,
        },
    },
]


SETS_N2_BY_ID = {s["id"]: s for s in SETS_N2}
