"""
Latin GCSE Mastery Platform - Marking Engine
"""
import re, random

# ── Wrong-answer banner bank (no em-dashes) ────────────────────────────────────
# One of these is picked at random when the pupil is simply wrong (no near-miss
# hint fires). Near-miss hints (sg/pl, tense, person, missing meaning, in vs
# into, etc.) override this bank with their specific wording.
WRONG_MESSAGES = [
    "Unlucky! Take another look at this one.",
    "Whoops! Something's gone wrong here.",
    "Wrong! Give it another go.",
    "Incorrect! You must be exact.",
    "Oh no! Something needs fixing.",
]
# Cycle through the bank in shuffled order so pupils don't see the same
# banner twice in a row. When the cycle empties we reshuffle.
_WRONG_QUEUE = []
def pick_wrong():
    global _WRONG_QUEUE
    if not _WRONG_QUEUE:
        pool = list(WRONG_MESSAGES)
        random.shuffle(pool)
        # Avoid starting the new cycle with the same message that just ended
        # the previous cycle (so no back-to-back repeats across cycles).
        if pick_wrong._last and pool[0] == pick_wrong._last and len(pool) > 1:
            pool[0], pool[1] = pool[1], pool[0]
        _WRONG_QUEUE = pool
    msg = _WRONG_QUEUE.pop(0)
    pick_wrong._last = msg
    return msg
pick_wrong._last = None

# ── Levenshtein distance ──────────────────────────────────────────────────────

def levenshtein(s1, s2):
    if len(s1) < len(s2): return levenshtein(s2, s1)
    if len(s2) == 0: return len(s1)
    prev = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        curr = [i + 1]
        for j, c2 in enumerate(s2):
            curr.append(min(prev[j+1]+1, curr[j]+1, prev[j]+(c1!=c2)))
        prev = curr
    return prev[len(s2)]

COMMON_WORDS = {
    "the","a","an","is","am","are","was","were","be","been","have","has","had",
    "do","does","did","he","she","it","they","we","you","not","no","yes","and",
    "or","but","if","so","as","at","in","on","to","for","of","with","by","from",
    "up","out","bad","bat","bed","big","bit","bug","bus","buy","car","cat","eat",
    "fat","fit","fly","fun","got","hat","hit","hot","let","lit","man","men","met",
    "new","now","old","our","own","put","ran","run","sat","say","see","set","sit",
    "ten","top","two","use","war","bear","beer","bird","bold","bone","born","call",
    "came","care","food","good","hold","fear","hear","kill","king","love","walk","look","at"
}

def norm(text):
    t = text.lower().strip()
    t = re.sub(r'\s*/\s*', '/', t)
    t = re.sub(r'-', ' ', t)
    t = re.sub(r'[^a-z0-9/ ]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    # Treat "(p)" and "(pl)" as equivalent — both normalize to "pl" after "you"
    t = re.sub(r'\byou p\b', 'you pl', t)
    # Treat "(s)" and "(sg)" as equivalent — both normalize to "sg" after "you"
    t = re.sub(r'\byou s\b', 'you sg', t)
    # Accept the words "plural" / "singular" wherever pupils type them in place
    # of (pl) / (sg) — e.g. "you plural ask" → "you pl ask".
    t = re.sub(r'\bplural\b', 'pl', t)
    t = re.sub(r'\bsingular\b', 'sg', t)
    # Accept pronoun groups written with spaces instead of slashes:
    # "he she it" / "he she" → normalise to the slash form so targets match.
    t = re.sub(r'\bhe\s+she\s+it\b', 'he/she/it', t)
    t = re.sub(r'\bhe\s+she\b', 'he/she', t)
    t = re.sub(r'\bhe\s+it\b', 'he/it', t)
    t = re.sub(r'\bshe\s+it\b', 'she/it', t)
    return t

def norm_latin(text):
    t = text.lower().strip()
    t = re.sub(r'-', '', t)   # strip scaffolding hyphens
    t = re.sub(r'[^a-z ]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def split_parts(text):
    import re as _re
    return [p.strip() for p in _re.split(r'[\s,/]+', text.strip()) if p.strip()]

def fmt(vocab):
    eng = vocab.get("english", [])
    notes = vocab.get("notes", "") or ""
    if ("Both meanings" in notes or "All three meanings" in notes) and len(eng) >= 2:
        return " / ".join(eng)
    if "Any one meaning" in notes:
        return eng[0] if eng else ""
    # For vocab with multiple meanings (e.g. prepositions with several translations),
    # show all separated by " / " so the review box displays the full set of meanings
    return " / ".join(eng) if len(eng) > 1 else eng[0] if eng else ""

def make_third_person(base):
    if base.endswith(("ch","sh","x","ss","zz")): return base + "es"
    elif base.endswith("y") and len(base) > 1 and base[-2] not in "aeiou": return base[:-1] + "ies"
    else: return base + "s"

def is_ending_only_change(pupil, target):
    if len(pupil) < 4 or len(target) < 4: return False
    min_len = min(len(pupil), len(target)); common = 0
    for i in range(min_len):
        if pupil[i] == target[i]: common += 1
        else: break
    if common >= max(3, int(min_len * 0.6)):
        if len(pupil[common:]) <= 3 and len(target[common:]) <= 3: return True
    return False

def _is_number_error(pupil_word, target_word):
    irregular_plurals = {"man":"men","woman":"women","mouse":"mice","tooth":"teeth",
                         "foot":"feet","person":"people","child":"children"}
    if irregular_plurals.get(pupil_word)==target_word or irregular_plurals.get(target_word)==pupil_word:
        return True
    return target_word in (pupil_word+"s",pupil_word+"es") or pupil_word in (target_word+"s",target_word+"es")

_SUBJECT_PRONOUNS = {"i","we","you","he","she","it","they"}
_OBJECT_PRONOUNS  = {"me","us","you","him","her","it","them"}
# Person groups — anything inside the same group is a PERSON swap
_PERSON_GROUPS = [
    {"i","we"},                 # 1st sg vs 1st pl (still "person" in the loose sense → hand off to number detector)
    {"he","she","it","they"},   # 3rd sg vs 3rd pl (handled by number detector)
    {"i","he","she","it","they"},  # 1st vs 3rd
    {"we","they"},              # 1st pl vs 3rd pl
    {"you","he","she","it","they","i","we"},  # 2nd vs others
]

def _is_person_error(pupil_word, target_word):
    """True iff the two words are both subject pronouns that differ in PERSON
    (not just number — number errors are caught separately).

    We only flag clear person mismatches:
      - I  ↔ he/she/it/they
      - we ↔ they / he / she
      - you ↔ I/we/he/she/it/they
    """
    if pupil_word == target_word:
        return False
    if pupil_word not in _SUBJECT_PRONOUNS or target_word not in _SUBJECT_PRONOUNS:
        return False
    # Exclude pure number errors (i/we and they/he-she-it) — those have their own hint
    pure_number_pairs = {frozenset({"i","we"})}
    if frozenset({pupil_word,target_word}) in pure_number_pairs:
        return False
    # 3rd-sg ↔ 3rd-pl is a number error, not person
    third_sg = {"he","she","it"}
    if (pupil_word in third_sg and target_word == "they") or \
       (target_word in third_sg and pupil_word == "they"):
        return False
    return True

def _is_tense_swap(pupil_word, target_word):
    """Detect if two words are the same verb but in different tenses (past vs present 3rd sg)."""
    if pupil_word == target_word or len(pupil_word) < 4 or len(target_word) < 4:
        return False
    # Find the longest common prefix before the words diverge
    common = 0
    for a, b in zip(pupil_word, target_word):
        if a == b: common += 1
        else: break
    if common < 3:
        return False
    p_suf = pupil_word[common:]
    t_suf = target_word[common:]
    past_suffs  = {'d', 'ed', 'ied'}
    pres_suffs  = {'s', 'es', 'ies'}
    return ((p_suf in past_suffs and t_suf in pres_suffs) or
            (p_suf in pres_suffs and t_suf in past_suffs))

# ── Top 150 board-approved multi-meaning expansion ────────────────────────────
# Each entry: (regex_pattern, replacement)
# Generates both directions so all board-approved variants are accepted.
_T150_SYNONYMS = [
    # ad = to, towards, at
    (re.compile(r'\bto (the|a|an)\b'),      r'towards \1'),
    (re.compile(r'\btowards (the|a|an)\b'),  r'to \1'),
    (re.compile(r'\bto (the|a|an)\b'),      r'at \1'),
    (re.compile(r'\bat (the|a|an)\b'),       r'to \1'),
    # in + ablative = in, on
    (re.compile(r'\bin (the|a|an)\b'),       r'on \1'),
    (re.compile(r'\bon (the|a|an)\b'),       r'in \1'),
    # in + accusative = into, onto
    (re.compile(r'\binto (the|a|an)\b'),     r'onto \1'),
    (re.compile(r'\bonto (the|a|an)\b'),     r'into \1'),
    # a/ab = from, away from
    (re.compile(r'\bfrom (the|a|an)\b'),     r'away from \1'),
    (re.compile(r'\baway from (the|a|an)\b'),r'from \1'),
    # magnus/a/um = big, great
    (re.compile(r'\bbig\b'),                 r'great'),
    (re.compile(r'\bgreat\b'),               r'big'),
    # ingens = huge, enormous (also accept "very great/big" — all inter-acceptable at GCSE)
    (re.compile(r'\bhuge\b'),                r'enormous'),
    (re.compile(r'\benormous\b'),            r'huge'),
    (re.compile(r'\bhuge\b'),                r'vast'),
    (re.compile(r'\bvast\b'),               r'huge'),
    # fortis = brave, strong (incl. comparative/superlative forms)
    (re.compile(r'\bbrave\b'),               r'strong'),
    (re.compile(r'\bstrong\b'),              r'brave'),
    (re.compile(r'\bbraver\b'),              r'stronger'),
    (re.compile(r'\bstronger\b'),            r'braver'),
    (re.compile(r'\bbravest\b'),             r'strongest'),
    (re.compile(r'\bstrongest\b'),           r'bravest'),
    # via = road, street
    (re.compile(r'\broad\b'),                r'street'),
    (re.compile(r'\bstreet\b'),              r'road'),
    # multus = much, many
    (re.compile(r'\bmuch\b'),                r'many'),
    (re.compile(r'\bmany\b'),                r'much'),
    # omnis = all, every
    (re.compile(r'\ball\b'),                 r'every'),
    (re.compile(r'\bevery\b'),               r'all'),
    # solus = alone, lonely
    (re.compile(r'\balone\b'),               r'lonely'),
    (re.compile(r'\blonely\b'),              r'alone'),
    # manus = hand, group
    (re.compile(r'\bhand\b'),                r'group'),
    (re.compile(r'\bgroup\b'),               r'hand'),
    # vultus = face, expression
    (re.compile(r'\bface\b'),                r'expression'),
    (re.compile(r'\bexpression\b'),          r'face'),
    # insula = island, block of flats
    (re.compile(r'\bisland\b'),              r'block of flats'),
    (re.compile(r'\bblock of flats\b'),      r'island'),
    # terra = land, earth, ground
    (re.compile(r'\bland\b'),                r'earth'),
    (re.compile(r'\bearth\b'),               r'ground'),
    (re.compile(r'\bground\b'),              r'land'),
    # iam = now, already
    (re.compile(r'\balready\b'),             r'now'),
    # vix = hardly, scarcely
    (re.compile(r'\bhardly\b'),              r'scarcely'),
    (re.compile(r'\bscarcely\b'),            r'hardly'),
    # statim = at once, immediately
    (re.compile(r'\bat once\b'),             r'immediately'),
    (re.compile(r'\bimmediately\b'),         r'at once'),
    # tandem = finally, at last
    (re.compile(r'\bfinally\b'),             r'at last'),
    (re.compile(r'\bat last\b'),             r'finally'),
    # etiam = even, also
    (re.compile(r'\beven\b'),                r'also'),
    # tantus = so great, such a great
    (re.compile(r'\bso great\b'),            r'such a great'),
    (re.compile(r'\bsuch a great\b'),        r'so great'),
    # alius = other, another
    (re.compile(r'\banother\b'),             r'other'),
    # quamquam = although (accept "even though", "despite the fact that")
    (re.compile(r'\balthough\b'),            r'even though'),
    (re.compile(r'\beven though\b'),         r'although'),
    # cum + subj = when, since
    (re.compile(r'\bwhen\b'),                r'since'),
    # ubi = when, where
    (re.compile(r'\bwhere\b'),               r'when'),
    # ut + subj = (so) that, (in order) to
    (re.compile(r'\bso that\b'),             r'in order to'),
    (re.compile(r'\bin order to\b'),         r'so that'),
    # quod = because, which
    (re.compile(r'\bbecause\b'),             r'which'),
    # suus/sua/suum = his own, her own, their own, its own
    (re.compile(r'\bhis own\b'),             r'her own'),
    (re.compile(r'\bher own\b'),             r'his own'),
    (re.compile(r'\bhis own\b'),             r'their own'),
    (re.compile(r'\btheir own\b'),           r'his own'),
    (re.compile(r'\bits own\b'),             r'his own'),
    (re.compile(r'\bhis own\b'),             r'its own'),
    # suus — bare possessive accepted for "own" targets, but NOT the reverse:
    # eius sentences use bare "his/her" and should NOT accept "his own/her own".
    # One-directional: "his own" → "his" (lenient for suus targets),
    # but "his" does NOT expand to "his own" (strict for eius targets).
    (re.compile(r'\bhis own\b'),             r'his'),
    (re.compile(r'\bher own\b'),             r'her'),
    (re.compile(r'\btheir own\b'),           r'their'),
    (re.compile(r'\bits own\b'),             r'its'),
    # homo = man, human
    (re.compile(r'\bhuman\b'),               r'man'),
]

def _expand_top150_synonyms(target):
    """Generate board-approved synonym variants of a target string."""
    results = {target}
    for pattern, replacement in _T150_SYNONYMS:
        for existing in list(results):
            alt = pattern.sub(replacement, existing)
            if alt != existing:
                results.add(alt)
    return results


# ── Apostrophe genitive pre-processor ────────────────────────────────────────
# norm() strips apostrophes, so "king's" → "kings".  We convert BEFORE
# normalisation so the pupil's "the king's daughter" matches the target
# "the daughter of the king" (and vice-versa).
_APOS_RE = re.compile(r"\b(?:the\s+)?(\w+)'s\s+(\w+)\b", re.IGNORECASE)
_OF_THE_RE = re.compile(r'\bthe\s+(\w+)\s+of\s+the\s+(\w+)\b', re.IGNORECASE)

def _preprocess_genitive(raw):
    """Return a version of raw with possessive apostrophes converted to 'of the'.
    'the king's daughter' → 'the daughter of the king'
    Works on the pupil's raw answer before normalisation."""
    result = _APOS_RE.sub(lambda m: f"the {m.group(2)} of the {m.group(1)}", raw)
    return result

# ── Gloss aliases ───────────────────────────────────────────────────────────
# IDEAL translation uses the official strict gloss; these alternates are also
# accepted (per teacher: "ideal = strict, but accept the others").
# Map: canonical word/phrase -> list of accepted synonyms.
_GLOSS_ALIASES = {
    # solus = "alone, lonely" (accept "lone")
    "alone":     ["lone"],
    "lonely":    ["lone"],
    # cogo = "force" (accept compel/make)
    "force":     ["compel", "make"],
    "forced":    ["compelled", "made"],
    "forces":    ["compels", "makes"],
    "forcing":   ["compelling", "making"],
    # discedo = "leave" (accept depart, withdraw)
    "leave":     ["depart", "withdraw"],
    "leaves":    ["departs", "withdraws"],
    "leaving":   ["departing", "withdrawing"],
    "left":      ["departed", "withdrew"],
    # tum = "then" (accept "at that time")
    "then":      ["at that time"],
    # video = "see" (accept "look", "look at", "watch")
    "see":       ["look", "look at", "watch"],
    "sees":      ["looks", "looks at", "watches"],
    "seeing":    ["looking", "looking at", "watching"],
    "saw":       ["looked", "looked at", "watched"],
    "seen":      ["looked", "looked at", "watched"],
    # statim = "at once, immediately" (accept either alone in sentence context)
    "at once":   ["immediately", "straight away"],
    "immediately": ["at once", "straight away"],
    # vix = "hardly, scarcely" (accept either alone)
    "hardly":    ["scarcely", "barely"],
    "scarcely":  ["hardly", "barely"],
    # tamen = "however" (accept "but" / "nevertheless" / "yet")
    "however":   ["nevertheless", "yet", "but"],
    "but":       ["however", "nevertheless", "yet"],
    # igitur = "therefore" (accept "so", "and so")
    "therefore": ["so", "and so"],
    # nam / enim = "for" (accept "because")
    "for":       ["because"],
    # tandem = "finally, at last" (accept "in the end")
    "finally":   ["at last", "in the end"],
    "at last":   ["finally", "in the end"],
    # cognosco = "find out" / "get to know" (accept "recognise") — bidirectional
    "find out":  ["recognise", "realise"],
    "found out": ["recognised", "realised"],
    "finds out": ["recognises", "realises"],
    # reverse: "recognise/realise" → "find out"
    "recognise": ["find out"],
    "recognises":["finds out"],
    "recognised":["found out"],
    "recognising":["finding out"],
    "realise":   ["find out"],
    "realises":  ["finds out"],
    "realised":  ["found out"],
    "realising": ["finding out"],
    # conspicio = "notice" (accept "catch sight of", "spot") — bidirectional
    "notice":    ["catch sight of", "spot"],
    "noticed":   ["caught sight of", "spotted"],
    "notices":   ["catches sight of", "spots"],
    "noticing":  ["catching sight of", "spotting"],
    # reverse: "spot/catch sight of" → "notice"
    "spot":      ["notice", "catch sight of"],
    "spots":     ["notices", "catches sight of"],
    "spotted":   ["noticed", "caught sight of"],
    "spotting":  ["noticing", "catching sight of"],
    "catch sight of":   ["notice", "spot"],
    "catches sight of": ["notices", "spots"],
    "caught sight of":  ["noticed", "spotted"],
    "catching sight of":["noticing", "spotting"],
    # quaero/peto = "search for, seek" — accept "search" without "for" and vice versa
    # and accept "sought" / "seek" alongside "searched for" / "search for"
    "searching for": ["searching", "seeking"],
    "searched for":  ["searched", "sought"],
    "search for":    ["search", "seek"],
    "searches for":  ["searches", "seeks"],
    # reverse: "seek/sought" → "search for/searched for"
    "seek":  ["search for"],
    "seeks": ["searches for"],
    "sought":["searched for"],
    "seeking":["searching for"],
    # appropinquare + in/ad +acc — accept "approached into X" alongside
    # "approached X" / "approached to X"
    "approached the":  ["approached into the", "approached to the"],
    "approaches the":  ["approaches into the", "approaches to the"],
    "approaching the": ["approaching into the", "approaching to the"],
    # mox = "soon" (no aliases beyond synonyms — already canonical)
    # appareo = "appear" (accept "come into view")
    "appear":    ["come into view"],
    "appears":   ["comes into view"],
    "appearing": ["coming into view"],
    "appeared":  ["came into view"],
    # iubeo = "order" (accept "tell", "instruct")
    "order":     ["tell", "instruct"],
    "orders":    ["tells", "instructs"],
    "ordered":   ["told", "instructed"],
    "ordering":  ["telling", "instructing"],
    "command":   ["tell", "instruct"],
    "commands":  ["tells", "instructs"],
    "commanded": ["told", "instructed"],
    "commanding":["telling", "instructing"],
    # persuadeo = "persuade" (accept "convince")
    "persuade":  ["convince"],
    "persuades": ["convinces"],
    "persuaded": ["convinced"],
    "persuading":["convincing"],
    # nuntio = "announce" (accept "report", "tell")
    "announce":  ["report"],
    "announces": ["reports"],
    "announced": ["reported"],
    "announcing":["reporting"],
    # conor = "try" (accept "attempt")
    "try":       ["attempt"],
    "tries":     ["attempts"],
    "tried":     ["attempted"],
    "trying":    ["attempting"],
    "attempt":   ["try"],
    "attempts":  ["tries"],
    "attempted": ["tried"],
    "attempting":["trying"],
    # audio = "hear" (accept "listen to") — bidirectional
    "hear":      ["listen to"],
    "hears":     ["listens to"],
    "heard":     ["listened to"],
    "hearing":   ["listening to"],
    "listen to": ["hear"],
    "listens to":["hears"],
    "listened to":["heard"],
    "listening to":["hearing"],
    # advenio = "arrive" (accept "come") — one-directional: targets with
    # "arrived/arrive" also accept "came/come" but NOT the reverse, to avoid
    # compounding with the "appeared → came into view" alias chain.
    "arrive":    ["come"],
    "arrives":   ["comes"],
    "arrived":   ["came"],
    "arriving":  ["coming"],
    # quaero/peto = "look for" (accept "search for", "seek") — completing the chain
    "look for":  ["search for", "seek"],
    "looks for": ["searches for", "seeks"],
    "looked for":["searched for", "sought"],
    "looking for":["searching for", "seeking"],
    # igitur = "therefore" (also accept "thus")
    "thus":      ["therefore", "and so"],
}
# Compile word-boundary patterns once
_GLOSS_ALIAS_PATTERNS = [
    (re.compile(r'\b' + re.escape(canon) + r'\b'), canon, alts)
    for canon, alts in _GLOSS_ALIASES.items()
]

def _expand_gloss_aliases(text):
    """Generate variants of `text` with each canonical word substituted by
    each accepted alias. Substitutes one canon at a time (avoids combinatorial
    blow-up for sentences with multiple matches)."""
    results = {text}
    for pat, _canon, alts in _GLOSS_ALIAS_PATTERNS:
        for existing in list(results):
            if not pat.search(existing): continue
            for alt in alts:
                results.add(pat.sub(alt, existing))
    return results


def _to_gerund(base):
    if not base or len(base) < 2: return None
    vowels = "aeiou"
    if (len(base) >= 3 and base[-1] not in vowels and base[-2] in vowels
            and base[-3] not in vowels and base[-1] not in "wxy"):
        return base + base[-1] + "ing"
    if base.endswith("e") and len(base) > 2 and base[-2] not in "aeiou":
        return base[:-1] + "ing"
    return base + "ing"

def _expand_progressive(sentence_norm):
    results = {sentence_norm}
    prog_pattern = re.compile(r'\b(is|are|am|was|were)\s+(\w+ing)\b')
    match = prog_pattern.search(sentence_norm)
    if match:
        be_verb = match.group(1); gerund = match.group(2)
        if gerund.endswith("ing"):
            stem = gerund[:-3]
            if len(stem) >= 2 and stem[-1] == stem[-2]: stem = stem[:-1]
            for base in [stem, stem + "e", stem + "y" if stem.endswith(("r","l","d","n","t","p","s")) else stem]:
                third = make_third_person(base)
                results.add(sentence_norm.replace(be_verb + " " + gerund, third))
                if be_verb in ("was","were"):
                    # Imperfect rendering: accept "used to X" / "kept Xing" only.
                    # Bare past ("Xed") is NOT accepted — it conflates imperfect
                    # with perfect, which a strict Eduqas marker rejects.
                    results.add(sentence_norm.replace(be_verb + " " + gerund, "used to " + base))
                    results.add(sentence_norm.replace(be_verb + " " + gerund, "kept " + gerund))
        return list(results)
    words = sentence_norm.split()
    for i, word in enumerate(words):
        if len(word) <= 2 or word in COMMON_WORDS: continue
        if word.endswith("s") and not word.endswith(("ss","us","is")):
            candidates = [word[:-1]]
            if word.endswith("es") and len(word) > 4:
                candidates.append(word[:-2])
            if word.endswith("ies") and len(word) > 4:
                candidates.append(word[:-3] + "y")
            for base in candidates:
                gerund = _to_gerund(base)
                if gerund and len(gerund) >= 5:
                    results.add(" ".join(words[:i] + ["is", gerund] + words[i+1:]))
                # NOTE: do NOT generate a simple-past alt here. The target is a
                # present-tense verb (ends with -s) and accepting its past form
                # as "equivalent" would silently mark tense errors correct
                # (e.g. "loved" accepted for "loves"). The tense-swap detector
                # below catches legitimate perfect-tense renderings.
    return list(results)

# ── Vocabulary (English meanings) ────────────────────────────────────────────

def _expand_paren_optional(eng):
    """For glosses like "(to) home" or "(I) go" produce both with and without
    the parenthetical portion. Returns list of candidate English strings."""
    if "(" not in eng or ")" not in eng:
        return [eng]
    # Version without the parens (keeps word inside): "(to) home" -> "to home"
    with_word = re.sub(r'\s*\(([^)]+)\)\s*', r' \1 ', eng)
    with_word = re.sub(r'\s+', ' ', with_word).strip()
    # Version with the parenthetical removed entirely: "(to) home" -> "home"
    without = re.sub(r'\s*\([^)]*\)\s*', ' ', eng)
    without = re.sub(r'\s+', ' ', without).strip()
    return [with_word, without]

def _expand_slash_alternatives(eng):
    """For glosses like "to/for me" expand into separate variants:
    ["to me", "for me", "to me / for me", "to me for me"]."""
    # Only handle if slash is between two simple tokens with an optional tail
    # e.g. "to/for me", "big/great", "in/on" — split the slashed token,
    # prefix the non-slashed tail to each variant.
    m = re.match(r'^\s*([a-zA-Z]+(?:/[a-zA-Z]+)+)\s*(.*)$', eng)
    if not m:
        return [eng]
    slashed, tail = m.group(1), m.group(2).strip()
    alts = slashed.split("/")
    tail_sp = (" " + tail) if tail else ""
    variants = [a + tail_sp for a in alts]
    # Also accept the combined form: "to me / for me" and "to me for me"
    variants.append(" / ".join(a + tail_sp for a in alts))
    variants.append(" ".join(a + tail_sp for a in alts))
    variants.append(", ".join(a + tail_sp for a in alts))
    # Preserve the original literal form (e.g. "he/she asks", "to/for me")
    # so retyping the displayed ideal exactly is always accepted.
    variants.append(eng)
    return variants

def build_acceptable(vocab):
    acc = set()
    eng_list = vocab.get("english", [])
    pos = vocab.get("pos", "")
    notes = vocab.get("notes", "") or ""
    needs_both = "Both meanings" in notes or "All three meanings" in notes

    if needs_both and len(eng_list) >= 2:
        return acc  # handled separately in check_vocab

    # Expand each gloss: paren-optional AND slash-alternatives
    expanded = []
    for eng in eng_list:
        for e1 in _expand_paren_optional(eng):
            for e2 in _expand_slash_alternatives(e1):
                expanded.append(e2)

    # Expand with gloss aliases (solus/cogo/discedo/tum etc.)
    expanded = list({v for e in expanded for v in _expand_gloss_aliases(e)})

    for eng in expanded:
        n = norm(eng)
        acc.add(n)
        if pos == "noun":
            acc.update([n, "the " + n, "a " + n, "an " + n])
        elif pos == "verb" and eng.startswith("I "):
            acc.add(norm(eng))
        else:
            acc.add(n)
            if "he/she" in eng:
                acc.add(norm(eng.replace("he/she", "he")))
                acc.add(norm(eng.replace("he/she", "she")))
                acc.add(norm(eng.replace("he/she", "it")))
                acc.add(norm(eng.replace("he/she", "he/she/it")))

    # Order-agnostic multi-meaning acceptance: if the pupil types meanings in
    # any order (e.g. "ground earth land" for terra = land/earth/ground), we
    # want to accept that too. Add the full meaning set as a single joined
    # string regardless of order — the caller will also test token-set match.
    return acc

def check_dual(n_ans, eng_list, vocab):
    """For words where both meanings must be given (e.g. in + abl = in, on)."""
    meanings = []
    for eng in eng_list:
        m = eng[2:] if eng.startswith("I ") else eng
        meanings.append(norm(m))
    found = [m for m in meanings if re.search(r'\b' + re.escape(m) + r'\b', n_ans)]
    canonical = " / ".join(eng_list)  # e.g. "into / onto" or "in / on"
    if len(found) >= len(meanings):
        return {"result":"correct","message":"Correct!","correct_answer":canonical,"counts_as_correct":True}
    missing = [eng_list[i] for i,m in enumerate(meanings) if m not in found]
    need_label = "all three meanings" if len(meanings) == 3 else "both meanings"
    return {"result":"wrong",
            "message":f"You need {need_label}. Missing: **{', '.join(missing)}**.",
            "correct_answer":canonical,"counts_as_correct":False}

def check_vocab(pupil_answer, vocab):
    raw = pupil_answer.strip()
    if not raw:
        return {"result":"wrong","message":"You didn't type anything.",
                "correct_answer":fmt(vocab),"counts_as_correct":False}

    eng_list = vocab.get("english", [])
    notes = vocab.get("notes", "") or ""
    needs_both = "Both meanings" in notes or "All three meanings" in notes
    any_one = "Any one meaning" in notes   # context-dependent: any single answer is fully correct
    n_ans = norm(raw)

    if needs_both and len(eng_list) >= 2:
        return check_dual(n_ans, eng_list, vocab)

    acceptable = build_acceptable(vocab)

    # Order-agnostic multi-meaning: if pupil types multiple meanings in any order
    # (e.g. "ground earth land" for terra = "land, earth, ground"), accept if the
    # set of pupil's content tokens equals the set of canonical tokens. Fires
    # whether the meanings are split across multiple eng_list entries OR packed
    # into a single comma-separated entry like OFFICIAL_GLOSSES uses.
    has_multi_meaning = (
        (len(eng_list) >= 2) or
        (len(eng_list) == 1 and "," in eng_list[0])
    )
    if has_multi_meaning and not needs_both and not any_one:
        def _toks(s):
            s2 = re.sub(r'[,/]', ' ', s)
            s2 = re.sub(r'\b(the|a|an|to|for|from|of|at|in|on|with|by|i)\b', '', s2.lower())
            return set(t for t in re.sub(r'\s+', ' ', s2).strip().split() if t)
        pupil_toks = _toks(raw)
        canon_toks = set()
        for e in eng_list:
            canon_toks |= _toks(e)
        if pupil_toks and pupil_toks == canon_toks:
            return {"result":"correct","message":"Correct!",
                    "correct_answer":fmt(vocab),"counts_as_correct":True}

    if n_ans in acceptable:
        # For multi-meaning words (not "Any one meaning" words), remind the student
        # if they gave only one meaning when the full answer has several
        if len(eng_list) >= 2 and not needs_both and not any_one:
            full_answer = fmt(vocab)  # e.g. "brave / strong"
            if norm(full_answer) != n_ans:
                return {"result":"correct",
                        "message":"Be precise — you need all the meanings.",
                        "correct_answer":full_answer,"counts_as_correct":True}
        return {"result":"correct","message":"Correct!",
                "correct_answer":fmt(vocab),"counts_as_correct":True}

    # Check for missing sg/pl for 'you'
    if re.search(r'\byou\b', n_ans) and not re.search(r'\byou (sg|pl)\b', n_ans):
        for a in acceptable:
            if n_ans == re.sub(r'\byou (sg|pl)\b', 'you', a):
                return {"result":"wrong",
                        "message":"You need to specify whether its singular or plural - be precise!",
                        "correct_answer":fmt(vocab),"counts_as_correct":False}

    for a in acceptable:
        dist = levenshtein(n_ans, a)
        max_d = 2 if len(a) >= 7 else 1
        if 0 < dist <= max_d and len(a) >= 5 and n_ans not in COMMON_WORDS:
            if is_ending_only_change(n_ans, a): continue
            # Don't treat dropping a leading pronoun as a typo
            a_words = a.split(); n_words = n_ans.split()
            if a_words and a_words[0] in ("i","you","he","she","it","we","they") and (not n_words or n_words[0] != a_words[0]): continue
            return {"result":"typo",
                    "message":"Close! Watch your spelling.",
                    "correct_answer":fmt(vocab),"counts_as_correct":True,"is_typo":True}

    # Check if pupil gave one of several meanings when MULTIPLE are required
    # Handles BOTH multi-entry (eng_list >= 2) AND single comma-separated entries
    # like peto = "I seek, beg, ask, attack" — vocab card needs all senses.
    if not any_one:
        # Build the canonical list of senses
        senses = []
        if len(eng_list) >= 2:
            senses = list(eng_list)
        elif len(eng_list) == 1 and "," in eng_list[0]:
            raw_gloss = eng_list[0]
            prefix = "I " if raw_gloss.startswith("I ") else ""
            body = raw_gloss[2:] if prefix else raw_gloss
            senses = [prefix + s.strip() for s in body.split(",") if s.strip()]
        if len(senses) >= 2:
            given_meanings = set()
            for s in senses:
                m = s[2:] if s.startswith("I ") else s
                if re.search(r'\b' + re.escape(norm(m)) + r'\b', n_ans):
                    given_meanings.add(s)
            if given_meanings and len(given_meanings) < len(senses):
                return {"result":"wrong",
                        "message":"Close! You need to give all the meanings.",
                        "correct_answer":fmt(vocab),"counts_as_correct":False}

    return {"result":"wrong","message":pick_wrong(),
            "correct_answer":fmt(vocab),"counts_as_correct":False}

# ── Sentence marking ──────────────────────────────────────────────────────────

FLEXIBLE_ADVERBS = {"again","now","always","then","suddenly","quickly","slowly",
                    "immediately","scarcely","hardly","barely","soon","already",
                    "finally","next","therefore","so","however","nevertheless",
                    "still","also","even","there"}

# Multi-word adverbs that must be matched and stripped as complete phrases.
# These cover tandem = "at last" / "at once" / "straight away" / "in the end".
_MULTI_ADVERBS = frozenset({"at once","at last","straight away","in the end",
                             "right away","up to now"})

# Possessives pupils may insert where any one fits the sentence context.
# Rule (per teacher): if stripping possessives from both pupil and target makes
# them match, accept — e.g. "the father" ↔ "his father", "his son" ↔ "the son".
_POSS_RE = re.compile(r'\b(my|your|his|her|its|our|their)\s+')

def _strip_possessives(s):
    return re.sub(r'\s+', ' ', _POSS_RE.sub('', s)).strip()

def _strip_articles(s):
    # Strip definite/indefinite articles AND demonstratives — so "the husband"
    # matches "this husband" (hic maritus), "that god" matches "the god", etc.
    return re.sub(r'\s+', ' ', re.sub(r'\b(the|a|an|this|that|these|those)\b', '', s)).strip()

def _adverb_match(n_ans, target):
    # Strip BOTH articles and adverbs before comparing, so that
    # "the many gods suddenly were attacking the city"
    # matches ideal "Many gods were suddenly attacking the city."
    # Handles multi-word adverb phrases (at once, at last, etc.) first,
    # then single-word adverbs.
    def strip_advs_arts(s):
        found = set()
        s2 = re.sub(r'\b(the|a|an|this|that|these|those)\b', ' ', s)
        # Remove multi-word adverb phrases (longest first to avoid partial matches)
        for phrase in sorted(_MULTI_ADVERBS, key=len, reverse=True):
            if re.search(r'\b' + re.escape(phrase) + r'\b', s2):
                found.add(phrase)
                s2 = re.sub(r'\b' + re.escape(phrase) + r'\b', ' ', s2)
        # Remove single-word flexible adverbs
        words = re.sub(r'\s+', ' ', s2).strip().split()
        remaining = []
        for w in words:
            if w in FLEXIBLE_ADVERBS:
                found.add(w)
            else:
                remaining.append(w)
        return " ".join(remaining), found
    a_str, a_advs = strip_advs_arts(n_ans)
    t_str, t_advs = strip_advs_arts(target)
    return a_advs == t_advs and a_str == t_str


# ── Flex expansion helpers ────────────────────────────────────────────────────
# Verbs of motion that already IMPLY direction — a pupil may optionally insert
# "to" or "towards" after them because Latin expresses this with ad + acc.
MOTION_VERBS = (
    "approached","approaches","approach","approaching",
    "came","come","comes","coming",
    "went","go","goes","going",
    "arrived","arrives","arrive","arriving",
    "hurried","hurries","hurry","hurrying",
    "rushed","rushes","rush","rushing",
    "sailed","sails","sail","sailing",
    "ran","runs","run","running",
    "returned","returns","return","returning",
)

def _expand_motion_absorption(sentence_norm):
    """Accept redundant "to"/"towards" after motion verbs.
    e.g. target "approached the woman" ↔ pupil "approached to the woman"
                                       ↔ pupil "approached towards the woman"
    """
    results = {sentence_norm}
    for verb in MOTION_VERBS:
        # pupil inserted redundant preposition → add target with it
        pat_in = re.compile(rf'\b{verb}\b (the|a|an|his|her|its|their|my|your) ')
        for m in pat_in.finditer(sentence_norm):
            # insert "to " or "towards " between verb and noun phrase
            before = sentence_norm[:m.start()] + verb + " "
            after = sentence_norm[m.start() + len(verb) + 1:]
            results.add(before + "to " + after)
            results.add(before + "towards " + after)
        # strip redundant preposition if already present
        pat_strip = re.compile(rf'\b{verb}\s+(to|towards)\s+')
        stripped = pat_strip.sub(verb + " ", sentence_norm)
        if stripped != sentence_norm:
            results.add(stripped)
    return results


def _expand_pluperfect_drop(sentence_norm):
    """Pluperfect MUST be rendered with "had X-ed" — Eduqas insists on the
    auxiliary. We do NOT accept the bare past as an alternative.
    Returns the input unchanged.
    """
    return {sentence_norm}


def _expand_participle_placement(sentence_norm):
    """Accept multiple placements of a PPP in English.
      target:  "the having-been-loved daughter"  (compound-adj style)
      variant: "the daughter having been loved"  (post-modifier style)
      variant: "the loved daughter"               (plain past-participle)
      variant: "the daughter who had been loved"  (relative clause)
    Works on either "having-been-X" or "having been X" forms.
    """
    results = {sentence_norm}
    # Pattern: (art) having[- ]been[- ](X-ed|X-d|X-t) NOUN
    pat = re.compile(
        r'\b(the|a|an|his|her|its|their|my|your)\s+'
        r'having[- ]been[- ](\w+(?:ed|d|t|en))\s+'
        r'(\w+)'
    )
    for m in pat.finditer(sentence_norm):
        art, ppp, noun = m.group(1), m.group(2), m.group(3)
        span = m.group(0)
        alternatives = [
            f"{art} {noun} having been {ppp}",
            f"{art} {noun} having-been-{ppp}",
            f"{art} {ppp} {noun}",
            f"{art} {noun} who had been {ppp}",
            f"{art} {noun} which had been {ppp}",
        ]
        for alt in alternatives:
            results.add(sentence_norm.replace(span, alt))
    # Reverse: if target is "X-ed NOUN" allow "NOUN having been X-ed"
    pat2 = re.compile(r'\b(the|a|an|his|her|its|their|my|your)\s+(\w+ed|\w+en)\s+(\w+)')
    for m in pat2.finditer(sentence_norm):
        art, ppp, noun = m.group(1), m.group(2), m.group(3)
        span = m.group(0)
        alternatives = [
            f"{art} {noun} having been {ppp}",
            f"{art} {noun} who had been {ppp}",
            f"{art} having been {ppp} {noun}",
        ]
        for alt in alternatives:
            results.add(sentence_norm.replace(span, alt))
    return results

def _build_all_targets(sentence):
    all_targets = set()
    for eng in sentence["english"]:
        base = norm(eng).rstrip('.')
        all_targets.add(base)
        for v in _expand_progressive(base):
            all_targets.add(v)
        if "he/she" in base:
            all_targets.add(base.replace("he/she","he"))
            all_targets.add(base.replace("he/she","she"))
    for t in list(all_targets):
        for v in _expand_progressive(t):
            all_targets.add(v)
    # Strip optional trailing pronoun
    for t in list(all_targets):
        words = t.split()
        if words and words[-1] in ("her","him","it","them"):
            all_targets.add(" ".join(words[:-1]))
    # Expand with Top 150 board-approved multi-meaning synonyms
    for t in list(all_targets):
        for variant in _expand_top150_synonyms(t):
            all_targets.add(variant)
    # Expand with gloss aliases (solus/cogo/discedo/tum: accept variant wordings)
    for t in list(all_targets):
        for variant in _expand_gloss_aliases(t):
            all_targets.add(variant)
    # Motion-verb "to/towards" absorption (ad + acc after approach/come/go …)
    for t in list(all_targets):
        for variant in _expand_motion_absorption(t):
            all_targets.add(variant)
    # "had X-ed" ↔ "X-ed" (natural simple-past rendering of pluperfect)
    for t in list(all_targets):
        for variant in _expand_pluperfect_drop(t):
            all_targets.add(variant)
    # PPP placement (compound adj ↔ post-modifier ↔ relative clause)
    for t in list(all_targets):
        for variant in _expand_participle_placement(t):
            all_targets.add(variant)
    return all_targets

def _strip_clause_pronouns(text):
    """Strip optional explicit pronoun subjects (he/she/it/they/we/I) that pupils
    sometimes add after conjunctions in multi-clause sentences. These are implied
    by the Latin verb ending so both 'sailed and killed' and 'sailed and he killed'
    should be accepted.
    """
    # After 'and', 'but', 'then', 'so' (at clause boundary) strip pronoun + optional comma
    t = re.sub(r'\b(and|but|then|so),?\s+(he|she|it|they|we|i)\s+', r'\1 ', text, flags=re.IGNORECASE)
    # Also strip a leading pronoun if it matches the established subject (e.g. repeating subject)
    return t

def check_sentence(pupil_answer, sentence):
    raw = pupil_answer.strip()
    if not raw:
        return {"result":"wrong","message":"You didn't type anything.",
                "correct_answer":sentence["english"][0],"counts_as_correct":False}

    all_targets = _build_all_targets(sentence)
    has_proper = any(
        any(w[0].isupper() for w in eng.split()[1:])
        for eng in sentence.get("english",[])
    )

    # First try the full answer as a unit (norm strips commas/punctuation, so
    # "the soldier, having been freed, shouted" matches target correctly)
    n_full = norm(raw).rstrip('.')
    # Also prepare a version where any "you sg" / "you pl" qualifier is stripped,
    # so pupils who write "you (sg)" or "you sg" for a "tu" sentence (where the
    # target just says "you") are not penalised for being over-precise.
    _n_full_no_qual = re.sub(r'\byou\s*(sg|pl)\b', 'you', n_full)
    if _n_full_no_qual == n_full: _n_full_no_qual = None  # no change — don't add extra pass
    # Version with optional clause-boundary pronouns stripped (e.g. "and he freed" → "and freed")
    _n_full_no_pron = norm(_strip_clause_pronouns(raw)).rstrip('.')
    if _n_full_no_pron == n_full: _n_full_no_pron = None

    # Apostrophe-genitive: also try "the king's daughter" as "the daughter of the king"
    _raw_gen = _preprocess_genitive(raw)
    n_full_gen = norm(_raw_gen).rstrip('.') if _raw_gen != raw else None
    for target in all_targets:
        if n_full == target:
            return {"result":"correct","message":"Correct!",
                    "correct_answer":sentence["english"][0],"counts_as_correct":True}
        # Apostrophe genitive: "the king's daughter" ↔ "the daughter of the king"
        if n_full_gen and n_full_gen == target:
            return {"result":"correct","message":"Correct!",
                    "correct_answer":sentence["english"][0],"counts_as_correct":True}
        na = _strip_articles(n_full)
        ta = _strip_articles(target)
        if na == ta:
            return {"result":"correct","message":"Correct!",
                    "correct_answer":sentence["english"][0],"counts_as_correct":True}
        # Possessive-flex: pupil may insert his/her/their etc. where plausible
        if _strip_possessives(_strip_articles(n_full)) == _strip_possessives(_strip_articles(target)):
            return {"result":"correct","message":"Correct!",
                    "correct_answer":sentence["english"][0],"counts_as_correct":True}
    if any(_adverb_match(n_full, t) for t in all_targets):
        return {"result":"correct","message":"Correct!",
                "correct_answer":sentence["english"][0],"counts_as_correct":True}
    # Accept "you sg/pl" as over-precise but correct if target just has "you"
    if _n_full_no_qual:
        for target in all_targets:
            if _n_full_no_qual == target:
                return {"result":"correct","message":"Correct!",
                        "correct_answer":sentence["english"][0],"counts_as_correct":True}
            if _strip_articles(_n_full_no_qual) == _strip_articles(target):
                return {"result":"correct","message":"Correct!",
                        "correct_answer":sentence["english"][0],"counts_as_correct":True}
        if any(_adverb_match(_n_full_no_qual, t) for t in all_targets):
            return {"result":"correct","message":"Correct!",
                    "correct_answer":sentence["english"][0],"counts_as_correct":True}
    # Accept explicit pronoun subjects after conjunctions (e.g. "and he freed" = "and freed")
    if _n_full_no_pron:
        for target in all_targets:
            if _n_full_no_pron == target:
                return {"result":"correct","message":"Correct!",
                        "correct_answer":sentence["english"][0],"counts_as_correct":True}
            if _strip_articles(_n_full_no_pron) == _strip_articles(target):
                return {"result":"correct","message":"Correct!",
                        "correct_answer":sentence["english"][0],"counts_as_correct":True}
        if any(_adverb_match(_n_full_no_pron, t) for t in all_targets):
            return {"result":"correct","message":"Correct!",
                    "correct_answer":sentence["english"][0],"counts_as_correct":True}

    # Fall back to comma-split (legacy path for comma-separated variants)
    parts = [p.strip() for p in raw.split(',')]
    for part in parts:
        n_ans = norm(part).rstrip('.')
        for target in all_targets:
            if n_ans == target:
                return {"result":"correct","message":"Correct!",
                        "correct_answer":sentence["english"][0],"counts_as_correct":True}
            # Strip articles and compare — only hint if pupil answer didn't already contain an article
            na = _strip_articles(n_ans)
            ta = _strip_articles(target)
            if na == ta:
                return {"result":"correct","message":"Correct!",
                        "correct_answer":sentence["english"][0],"counts_as_correct":True}
            if _strip_possessives(na) == _strip_possessives(ta):
                return {"result":"correct","message":"Correct!",
                        "correct_answer":sentence["english"][0],"counts_as_correct":True}
        for target in all_targets:
            if _adverb_match(n_ans, target):
                return {"result":"correct","message":"Correct!",
                        "correct_answer":sentence["english"][0],"counts_as_correct":True}

    # ── Full-sentence typo path ──────────────────────────────────────────────
    # If pupil's full answer differs from any target by 1-2 character edits AND
    # only one word differs AND that one word is itself just a small misspelling
    # (Lev ≤ 1) of the target word, accept as typo. Real-word swaps (man/woman,
    # he/she) still fail because Lev between two distinct real words is usually
    # ≥ 2.
    n_full_clean = norm(raw).rstrip('.')
    for target in all_targets:
        nw = n_full_clean.split(); tw = target.split()
        if len(nw) != len(tw): continue
        diffs = [(a,b) for a,b in zip(nw,tw) if a != b]
        if not diffs: continue
        if len(diffs) == 1:
            pa, pb = diffs[0]
            # Tolerate one-letter typos in a single word (Lev=2 for long words —
            # catches transpositions like persaudes ↔ persuades).
            max_lev = 2 if len(pb) >= 8 else 1
            if 0 < levenshtein(pa, pb) <= max_lev and len(pb) >= 5:
                # But block if the differing pupil word is itself a known real
                # English word that means something different (man vs woman,
                # son vs sun) — these are vocab errors not typos.
                _REAL_WORD_PAIRS = {
                    ("man","woman"),("woman","man"),("boy","girl"),("girl","boy"),
                    ("son","sun"),("sun","son"),("god","good"),("good","god"),
                    ("ship","sheep"),("sheep","ship"),("king","queen"),("queen","king"),
                    ("father","mother"),("mother","father"),("kill","kiss"),
                }
                if (pa, pb) in _REAL_WORD_PAIRS or (pb, pa) in _REAL_WORD_PAIRS:
                    continue
                # Tense/aspect ending mismatch is NOT a typo. -ed vs -s/-es/-ies
                # signals past vs 3rd-person-present (e.g. "shouted" vs bogus
                # "shoutes" generated by progressive expansion). Reject so
                # imperfect-vs-perfect errors fall through to the wrong path.
                _PAST = ("ed", "ied")
                _PRES_S = ("es", "ies")
                if (pa.endswith(_PAST) and (pb.endswith(_PRES_S) or pb.endswith("s"))) or \
                   (pb.endswith(_PAST) and (pa.endswith(_PRES_S) or pa.endswith("s"))):
                    continue
                # Subject-verb agreement mismatch is NOT a typo.
                # "holds" 3sg vs "hold" 3pl, "attacks" / "attackes" vs "attack",
                # "carries" / "carryies" vs "carry" — drop trailing 3sg suffix.
                def _drop_3sg(w):
                    if w.endswith("ies") and len(w) > 3: return [w[:-3]+"y", w[:-2]]
                    if w.endswith("es") and len(w) > 2:  return [w[:-2], w[:-1]]
                    if w.endswith("s")  and len(w) > 1 and not w.endswith("ss"): return [w[:-1]]
                    return []
                if pa in _drop_3sg(pb) or pb in _drop_3sg(pa):
                    continue
                # Subject-verb agreement mismatch: "holds" vs "hold", "appears"
                # vs "appear". One word ending in "s" and the other not — same
                # stem, just the trailing -s. That's a 3sg/3pl agreement error,
                # not a spelling slip.
                if (pa.endswith("s") and pa[:-1] == pb) or \
                   (pb.endswith("s") and pb[:-1] == pa):
                    continue
                # Plural/singular noun mismatch: "woman" vs "women", "son" vs
                # "sons", "ship" vs "ships" — these are vocab errors not typos.
                _NUMBER_PAIRS = {
                    ("woman","women"),("man","men"),("son","sons"),("daughter","daughters"),
                    ("ship","ships"),("god","gods"),("goddess","goddesses"),("girl","girls"),
                    ("boy","boys"),("father","fathers"),("mother","mothers"),
                    ("queen","queens"),("king","kings"),("friend","friends"),
                    ("sword","swords"),("wood","woods"),("city","cities"),
                    ("island","islands"),("land","lands"),
                }
                pair = (pa, pb)
                if pair in _NUMBER_PAIRS or (pb, pa) in _NUMBER_PAIRS:
                    continue
                return {"result":"typo",
                        "message":"Almost! Watch your spelling.",
                        "correct_answer":sentence["english"][0],"counts_as_correct":True,"is_typo":True}

    n_ans = norm(parts[0]).rstrip('.')
    original_targets = [norm(e).rstrip('.') for e in sentence["english"]]

    # ── Tense-swap check: catch past tense used for present or vice versa ────
    for target in original_targets:
        n_words = n_ans.split(); t_words = target.split()
        if len(n_words) == len(t_words):
            diffs = [(a,b) for a,b in zip(n_words,t_words) if a != b]
            if diffs and all(_is_tense_swap(a,b) for a,b in diffs):
                p_is_past = any(a.endswith(('ed','d','ied')) for a,b in diffs)
                tense_msg = "past" if p_is_past else "present"
                other_msg = "present" if p_is_past else "past"
                return {"result":"wrong",
                        "message":f"Close! You misidentified the tense of the verb. (Should be **{other_msg}**, not {tense_msg}.)",
                        "correct_answer":sentence["english"][0],"counts_as_correct":False}

    # ── 'you' without sg/pl qualifier ────────────────────────────────────────
    if re.search(r'\byou\b', n_ans) and not re.search(r'\byou\s*(sg|pl|\(sg\)|\(pl\))', n_ans):
        for target in all_targets:
            stripped = re.sub(r'\byou\s*(sg|pl|\(sg\)|\(pl\))\s*', 'you ', target).strip()
            stripped = re.sub(r'\s+', ' ', stripped)
            if n_ans == stripped:
                return {"result":"wrong",
                        "message":"You need to specify whether it's singular or plural. Be precise!",
                        "correct_answer":sentence["english"][0],"counts_as_correct":False}

    for target in original_targets:
        n_words = n_ans.split(); t_words = target.split()
        if len(n_words) == len(t_words):
            diffs = [(a,b) for a,b in zip(n_words,t_words) if a != b]
            if len(diffs) == 1 and _is_number_error(diffs[0][0], diffs[0][1]):
                return {"result":"wrong",
                        "message":"Nearly! You need to make sure what's singular versus plural.",
                        "correct_answer":sentence["english"][0],"counts_as_correct":False}
            if len(diffs) == 1 and _is_person_error(diffs[0][0], diffs[0][1]):
                return {"result":"wrong",
                        "message":"Nearly! Check who's doing the action.",
                        "correct_answer":sentence["english"][0],"counts_as_correct":False}
        if is_ending_only_change(n_ans, target) and levenshtein(n_ans, target) <= 3:
            return {"result":"wrong",
                    "message":"Check your ending carefully.",
                    "correct_answer":sentence["english"][0],"counts_as_correct":False}
        if levenshtein(n_ans, target) <= 2:
            n_words = n_ans.split(); t_words = target.split()
            # Guard: "in" vs "into" is a grammar error (in+abl vs in+acc), not a typo
            PREP_SWAPS = {("in","into"),("into","in")}
            if len(n_words) == len(t_words):
                diffs = [(a,b) for a,b in zip(n_words,t_words) if a != b]
                if any((a,b) in PREP_SWAPS for a,b in diffs):
                    return {"result":"wrong",
                            "message":"*in* + accusative = 'into' (motion); *in* + ablative = 'in' (position).",
                            "correct_answer":sentence["english"][0],"counts_as_correct":False}
                # Guard against tense swaps slipping through levenshtein
                if any(_is_tense_swap(a,b) for a,b in diffs):
                    # If the real target is IMPERFECT ("was Xing" / "used to X" /
                    # "kept Xing") and the pupil used simple past, give a specific
                    # imperfect hint rather than the misleading "use present" message.
                    _orig_impf = any(
                        re.search(
                            r'\b(was|were)\s+(not\s+)?\w+ing\b|\bused\s+to\s+\w+\b|\bkept\s+\w+ing\b',
                            t
                        )
                        for t in original_targets
                    )
                    if _orig_impf and any(a.endswith(('ed','d','ied')) for a,b in diffs):
                        return {"result":"wrong",
                                "message":"Close! This verb is **imperfect** — use *'was ...ing'*, *'used to ...'*, or *'kept ...ing'* — not simple past.",
                                "correct_answer":sentence["english"][0],"counts_as_correct":False}
                    p_is_past = any(a.endswith(('ed','d','ied')) for a,b in diffs)
                    tense_msg = "past" if p_is_past else "present"
                    other_msg = "present" if p_is_past else "past"
                    return {"result":"wrong",
                            "message":f"Close! You misidentified the tense of the verb. (Should be **{other_msg}**, not {tense_msg}.)",
                            "correct_answer":sentence["english"][0],"counts_as_correct":False}
            has_number_error = False
            if len(n_words) == len(t_words):
                diffs = [(a,b) for a,b in zip(n_words,t_words) if a != b]
                if any(_is_number_error(a,b) for a,b in diffs):
                    has_number_error = True
            if has_number_error:
                return {"result":"wrong",
                        "message":"Nearly! You need to make sure what's singular versus plural.",
                        "correct_answer":sentence["english"][0],"counts_as_correct":False}
            # Guard: if a single word differs entirely (vocab swap), reject as wrong,
            # not as a typo. A true typo is one letter inside the same word.
            if len(n_words) == len(t_words):
                diffs = [(a,b) for a,b in zip(n_words,t_words) if a != b]
                if len(diffs) == 1:
                    pa, pb = diffs[0]
                    # If the two differing words are themselves far apart
                    # (>1 edit) OR the pupil's word is the wrong Latin vocab
                    # (distance >= 2), it's a vocab error, not a typo.
                    if levenshtein(pa, pb) >= 2:
                        return {"result":"wrong",
                                "message":pick_wrong(),
                                "correct_answer":sentence["english"][0],"counts_as_correct":False}
            # Same-length word mismatch across multiple words also isn't a typo.
            if len(n_words) == len(t_words):
                diffs = [(a,b) for a,b in zip(n_words,t_words) if a != b]
                if len(diffs) >= 2:
                    return {"result":"wrong",
                            "message":pick_wrong(),
                            "correct_answer":sentence["english"][0],"counts_as_correct":False}
            return {"result":"typo",
                    "message":"Almost! Watch your spelling.",
                    "correct_answer":sentence["english"][0],"counts_as_correct":True,"is_typo":True}

    # ── Imperfect-specific hint ─────────────────────────────────────────────
    # If the sentence is imperfect ("was Xing" / "used to X" / "kept Xing") and
    # the pupil used a bare simple-past verb (no was/were/had), give a targeted
    # hint rather than a generic wrong banner.  This catches "shouted" for
    # clamabat, "walked" for ambulabat, etc. (#1)
    _any_impf = any(
        re.search(r'\b(was|were)\s+(not\s+)?\w+ing\b|\bused\s+to\s+\w+|\bkept\s+\w+ing\b', t)
        for t in original_targets
    )
    if _any_impf:
        _pupil_bare_past = (
            not re.search(r'\b(was|were|had)\b', n_ans) and
            bool(re.search(r'\b\w+(?:ed|ied)\b', n_ans))
        )
        if _pupil_bare_past:
            return {"result":"wrong",
                    "message":"Close! This verb is **imperfect** — use *'was ...ing'*, *'used to ...'*, or *'kept ...ing'* — not simple past.",
                    "correct_answer":sentence["english"][0],"counts_as_correct":False}

    # Generic wrong: pick a friendly banner at random.
    return {"result":"wrong",
            "message":pick_wrong(),
            "correct_answer":sentence["english"][0],"counts_as_correct":False}

# ── Latin typed (principal parts gap fill) ────────────────────────────────────

def check_latin_typed(pupil_answer, correct_latin):
    raw = pupil_answer.strip()
    if not raw:
        return {"result":"wrong","message":"You didn't type anything.",
                "correct_answer":correct_latin,"counts_as_correct":False}
    if norm_latin(raw) == norm_latin(correct_latin):
        return {"result":"correct","message":"Correct!",
                "correct_answer":correct_latin,"counts_as_correct":True}
    return {"result":"wrong","message":pick_wrong(),
            "correct_answer":correct_latin,"counts_as_correct":False}

def check_gap_fill(pupil_answer, correct_latin):
    return check_latin_typed(pupil_answer, correct_latin)

# ── All Four Parts (type inf perf ppp from present) ───────────────────────────

def check_all_four_parts(pupil_answer, correct_inf, correct_perf, correct_ppp):
    """
    correct_ppp may be None for verbs with no PPP (festino, navigo, appropinquo).
    In that case only 2 parts are expected.
    """
    raw = pupil_answer.strip()
    has_ppp = correct_ppp is not None

    if has_ppp:
        correct_answer = f"{correct_inf} {correct_perf} {correct_ppp}"
        expected_count = 3
    else:
        correct_answer = f"{correct_inf} {correct_perf}"
        expected_count = 2

    if not raw:
        return {"result":"wrong",
                "message":f"You didn't type anything. The answer is: *{correct_answer}*",
                "correct_answer":correct_answer,"counts_as_correct":False}

    parts = split_parts(raw)

    if len(parts) != expected_count:
        if not has_ppp and len(parts) == 3:
            # Pupil typed a PPP for a verb that has none
            return {"result":"wrong",
                    "message":f"This verb has no PPP. Type only the infinitive and perfect: *{correct_answer}*",
                    "correct_answer":correct_answer,"counts_as_correct":False}
        return {"result":"wrong",
                "message":f"Type {expected_count} parts separated by spaces. The answer is: *{correct_answer}*",
                "correct_answer":correct_answer,"counts_as_correct":False}

    ok_inf  = norm_latin(parts[0]) == norm_latin(correct_inf)
    ok_perf = norm_latin(parts[1]) == norm_latin(correct_perf)
    ok_ppp  = (not has_ppp) or norm_latin(parts[2]) == norm_latin(correct_ppp)

    if ok_inf and ok_perf and ok_ppp:
        return {"result":"correct","message":"Correct!",
                "correct_answer":correct_answer,"counts_as_correct":True}

    errors = []
    if not ok_inf:  errors.append(f"infinitive: *{correct_inf}*")
    if not ok_perf: errors.append(f"perfect: *{correct_perf}*")
    if has_ppp and not ok_ppp: errors.append(f"PPP: *{correct_ppp}*")
    return {"result":"wrong",
            "message":"Check: " + "; ".join(errors) + ".",
            "correct_answer":correct_answer,"counts_as_correct":False}

# ── Parsing (full: tense + person + number) ───────────────────────────────────

# Maps from frontend display labels → (person, number) data values
_PERSON_NUMBER_MAP = {
    "i":            ("1st", "singular"),
    "'i'":          ("1st", "singular"),
    "1st singular": ("1st", "singular"),
    "you (sg)":     ("2nd", "singular"),
    "you sg":       ("2nd", "singular"),
    "2nd singular": ("2nd", "singular"),
    "he/she/it":    ("3rd", "singular"),
    "he/she":       ("3rd", "singular"),
    "3rd singular": ("3rd", "singular"),
    "we":           ("1st", "plural"),
    "1st plural":   ("1st", "plural"),
    "you (pl)":     ("2nd", "plural"),
    "you pl":       ("2nd", "plural"),
    "2nd plural":   ("2nd", "plural"),
    "they":         ("3rd", "plural"),
    "3rd plural":   ("3rd", "plural"),
}

def _norm_person_number(person, number):
    """Normalise person/number to (person_str, number_str) matching data format."""
    # If the frontend sends a combined label (e.g. "you (sg)"), decode it
    combined = (person.strip().lower() + " " + number.strip().lower()).strip()
    lookup = person.strip().lower()
    if lookup in _PERSON_NUMBER_MAP:
        return _PERSON_NUMBER_MAP[lookup]
    if combined in _PERSON_NUMBER_MAP:
        return _PERSON_NUMBER_MAP[combined]
    # Already in correct format (e.g. "2nd", "singular")
    return (person.strip(), number.strip())

def check_parsing(pupil_tense, pupil_person, pupil_number,
                  correct_tense, correct_person, correct_number):
    norm_p, norm_n = _norm_person_number(pupil_person, pupil_number)
    # Case-insensitive, strip whitespace comparisons to avoid subtle mismatches
    pt = pupil_tense.strip().lower()
    ct = correct_tense.strip().lower()
    np_ = norm_p.strip().lower()
    cp = correct_person.strip().lower()
    nn = norm_n.strip().lower()
    cn = correct_number.strip().lower()
    correct = (pt == ct and np_ == cp and nn == cn)
    if correct:
        return {"result":"correct","message":"Correct!","counts_as_correct":True}
    errors = []
    if pt != ct:  errors.append(f"tense: **{correct_tense}**")
    if np_ != cp: errors.append(f"person: **{correct_person}**")
    if nn != cn:  errors.append(f"number: **{correct_number}**")
    return {"result":"wrong",
            "message":"Not quite. " + "; ".join(errors) + ".",
            "counts_as_correct":False}
