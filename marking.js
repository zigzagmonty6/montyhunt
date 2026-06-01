/* ============================================================
   marking.js — faithful JS port of marking.py
   Provides: checkSentence, checkLatinTyped, checkAllFourParts,
             checkVocab, checkParsing, normEng, normLat
   All attached to window so platform-compiled.js can call them.
   ============================================================ */
(function(){
'use strict';

// ── Levenshtein ───────────────────────────────────────────────────────────────
function levenshtein(s1, s2){
  if(s1.length < s2.length) return levenshtein(s2, s1);
  if(s2.length === 0) return s1.length;
  var prev = [];
  for(var i=0;i<=s2.length;i++) prev[i]=i;
  for(var i=0;i<s1.length;i++){
    var curr=[i+1];
    for(var j=0;j<s2.length;j++)
      curr.push(Math.min(prev[j+1]+1, curr[j]+1, prev[j]+(s1[i]!==s2[j]?1:0)));
    prev=curr;
  }
  return prev[s2.length];
}

var COMMON_WORDS = new Set(["the","a","an","is","am","are","was","were","be","been","have","has","had",
  "do","does","did","he","she","it","they","we","you","not","no","yes","and",
  "or","but","if","so","as","at","in","on","to","for","of","with","by","from",
  "up","out","bad","bat","bed","big","bit","bug","bus","buy","car","cat","eat",
  "fat","fit","fly","fun","got","hat","hit","hot","let","lit","man","men","met",
  "new","now","old","our","own","put","ran","run","sat","say","see","set","sit",
  "ten","top","two","use","war","bear","beer","bird","bold","bone","born","call",
  "came","care","food","good","hold","fear","hear","kill","king","love","walk","look","at"]);

// ── norm (English) ────────────────────────────────────────────────────────────
function norm(text){
  var t = (text||'').toLowerCase().trim();
  t = t.replace(/\s*\/\s*/g, '/');
  t = t.replace(/-/g, ' ');
  t = t.replace(/[^a-z0-9/ ]/g, '');
  t = t.replace(/\s+/g, ' ').trim();
  t = t.replace(/\byou p\b/g, 'you pl');
  t = t.replace(/\byou s\b/g, 'you sg');
  t = t.replace(/\bplural\b/g, 'pl');
  t = t.replace(/\bsingular\b/g, 'sg');
  t = t.replace(/\bhe\s+she\s+it\b/g, 'he/she/it');
  t = t.replace(/\bhe\s+she\b/g, 'he/she');
  t = t.replace(/\bhe\s+it\b/g, 'he/it');
  t = t.replace(/\bshe\s+it\b/g, 'she/it');
  return t;
}

function normLat(text){
  var t = (text||'').toLowerCase().trim();
  t = t.replace(/-/g, '');
  t = t.replace(/[^a-z ]/g, '');
  t = t.replace(/\s+/g, ' ').trim();
  return t;
}

function splitParts(text){
  return (text||'').trim().split(/[\s,/]+/).filter(function(p){return p.length>0;});
}

// ── _T150_SYNONYMS ────────────────────────────────────────────────────────────
var _T150 = [
  [/\bto (the|a|an)\b/g,      'towards $1'],
  [/\btowards (the|a|an)\b/g, 'to $1'],
  [/\bto (the|a|an)\b/g,      'at $1'],
  [/\bat (the|a|an)\b/g,      'to $1'],
  [/\bin (the|a|an)\b/g,      'on $1'],
  [/\bon (the|a|an)\b/g,      'in $1'],
  [/\binto (the|a|an)\b/g,    'onto $1'],
  [/\bonto (the|a|an)\b/g,    'into $1'],
  [/\bfrom (the|a|an)\b/g,    'away from $1'],
  [/\baway from (the|a|an)\b/g,'from $1'],
  [/\bbig\b/g,                'great'],
  [/\bgreat\b/g,              'big'],
  [/\bhuge\b/g,               'enormous'],
  [/\benormous\b/g,           'huge'],
  [/\bhuge\b/g,               'vast'],
  [/\bvast\b/g,               'huge'],
  [/\bbrave\b/g,              'strong'],
  [/\bstrong\b/g,             'brave'],
  [/\bbraver\b/g,             'stronger'],
  [/\bstronger\b/g,           'braver'],
  [/\bbravest\b/g,            'strongest'],
  [/\bstrongest\b/g,          'bravest'],
  [/\broad\b/g,               'street'],
  [/\bstreet\b/g,             'road'],
  [/\bmuch\b/g,               'many'],
  [/\bmany\b/g,               'much'],
  [/\ball\b/g,                'every'],
  [/\bevery\b/g,              'all'],
  [/\balone\b/g,              'lonely'],
  [/\blonely\b/g,             'alone'],
  [/\bhand\b/g,               'group'],
  [/\bgroup\b/g,              'hand'],
  [/\bface\b/g,               'expression'],
  [/\bexpression\b/g,         'face'],
  [/\bisland\b/g,             'block of flats'],
  [/\bblock of flats\b/g,     'island'],
  [/\bland\b/g,               'earth'],
  [/\bearth\b/g,              'ground'],
  [/\bground\b/g,             'land'],
  [/\balready\b/g,            'now'],
  [/\bhardly\b/g,             'scarcely'],
  [/\bscarcely\b/g,           'hardly'],
  [/\bat once\b/g,            'immediately'],
  [/\bimmediately\b/g,        'at once'],
  [/\bfinally\b/g,            'at last'],
  [/\bat last\b/g,            'finally'],
  [/\beven\b/g,               'also'],
  [/\bso great\b/g,           'such a great'],
  [/\bsuch a great\b/g,       'so great'],
  [/\banother\b/g,            'other'],
  [/\balthough\b/g,           'even though'],
  [/\beven though\b/g,        'although'],
  [/\bwhen\b/g,               'since'],
  [/\bwhere\b/g,              'when'],
  [/\bso that\b/g,            'in order to'],
  [/\bin order to\b/g,        'so that'],
  [/\bbecause\b/g,            'which'],
  [/\bhis own\b/g,            'her own'],
  [/\bher own\b/g,            'his own'],
  [/\bhis own\b/g,            'their own'],
  [/\btheir own\b/g,          'his own'],
  [/\bits own\b/g,            'his own'],
  [/\bhis own\b/g,            'its own'],
  [/\bhis own\b/g,            'his'],
  [/\bher own\b/g,            'her'],
  [/\btheir own\b/g,          'their'],
  [/\bits own\b/g,            'its'],
  [/\bhuman\b/g,              'man'],
];

function expandTop150(target){
  var results = new Set([target]);
  _T150.forEach(function(pair){
    var pat = pair[0], rep = pair[1];
    results.forEach(function(existing){
      var alt = existing.replace(pat, rep);
      if(alt !== existing) results.add(alt);
    });
  });
  return results;
}

// ── _GLOSS_ALIASES ────────────────────────────────────────────────────────────
var _GLOSS_ALIASES = {
  "alone":["lone"],"lonely":["lone"],
  "force":["compel","make"],"forced":["compelled","made"],"forces":["compels","makes"],"forcing":["compelling","making"],
  "leave":["depart","withdraw"],"leaves":["departs","withdraws"],"leaving":["departing","withdrawing"],"left":["departed","withdrew"],
  "then":["at that time"],
  "see":["look","look at","watch"],"sees":["looks","looks at","watches"],"seeing":["looking","looking at","watching"],"saw":["looked","looked at","watched"],"seen":["looked","looked at","watched"],
  "at once":["immediately","straight away"],"immediately":["at once","straight away"],
  "hardly":["scarcely","barely"],"scarcely":["hardly","barely"],
  "however":["nevertheless","yet","but"],"but":["however","nevertheless","yet"],
  "therefore":["so","and so"],
  "for":["because"],
  "finally":["at last","in the end"],"at last":["finally","in the end"],
  "find out":["recognise","realise"],"found out":["recognised","realised"],"finds out":["recognises","realises"],
  "recognise":["find out"],"recognises":["finds out"],"recognised":["found out"],"recognising":["finding out"],
  "realise":["find out"],"realises":["finds out"],"realised":["found out"],"realising":["finding out"],
  "notice":["catch sight of","spot"],"noticed":["caught sight of","spotted"],"notices":["catches sight of","spots"],"noticing":["catching sight of","spotting"],
  "spot":["notice","catch sight of"],"spots":["notices","catches sight of"],"spotted":["noticed","caught sight of"],"spotting":["noticing","catching sight of"],
  "catch sight of":["notice","spot"],"catches sight of":["notices","spots"],"caught sight of":["noticed","spotted"],"catching sight of":["noticing","spotting"],
  "searching for":["searching","seeking"],"searched for":["searched","sought"],"search for":["search","seek"],"searches for":["searches","seeks"],
  "seek":["search for"],"seeks":["searches for"],"sought":["searched for"],"seeking":["searching for"],
  "approached the":["approached into the","approached to the"],"approaches the":["approaches into the","approaches to the"],"approaching the":["approaching into the","approaching to the"],
  "appear":["come into view"],"appears":["comes into view"],"appearing":["coming into view"],"appeared":["came into view"],
  "order":["tell","instruct"],"orders":["tells","instructs"],"ordered":["told","instructed"],"ordering":["telling","instructing"],
  "command":["tell","instruct"],"commands":["tells","instructs"],"commanded":["told","instructed"],"commanding":["telling","instructing"],
  "persuade":["convince"],"persuades":["convinces"],"persuaded":["convinced"],"persuading":["convincing"],
  "announce":["report"],"announces":["reports"],"announced":["reported"],"announcing":["reporting"],
  "try":["attempt"],"tries":["attempts"],"tried":["attempted"],"trying":["attempting"],
  "attempt":["try"],"attempts":["tries"],"attempted":["tried"],"attempting":["trying"],
  "hear":["listen to"],"hears":["listens to"],"heard":["listened to"],"hearing":["listening to"],
  "listen to":["hear"],"listens to":["hears"],"listened to":["heard"],"listening to":["hearing"],
  "arrive":["come"],"arrives":["comes"],"arrived":["came"],"arriving":["coming"],
  "look for":["search for","seek"],"looks for":["searches for","seeks"],"looked for":["searched for","sought"],"looking for":["searching for","seeking"],
  "thus":["therefore","and so"],
};

var _GLOSS_PATTERNS = Object.keys(_GLOSS_ALIASES).map(function(canon){
  return {re: new RegExp('\\b'+canon.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\b','g'), canon:canon, alts:_GLOSS_ALIASES[canon]};
});

function expandGlossAliases(text){
  var results = new Set([text]);
  _GLOSS_PATTERNS.forEach(function(entry){
    var arr = Array.from(results);
    arr.forEach(function(existing){
      if(!entry.re.test(existing)){entry.re.lastIndex=0;return;}
      entry.re.lastIndex=0;
      entry.alts.forEach(function(alt){
        results.add(existing.replace(entry.re, alt));
        entry.re.lastIndex=0;
      });
    });
  });
  return results;
}

// ── _expand_progressive ───────────────────────────────────────────────────────
function makeThirdPerson(base){
  if(/(?:ch|sh|x|ss|zz)$/.test(base)) return base+'es';
  if(/[^aeiou]y$/.test(base)) return base.slice(0,-1)+'ies';
  return base+'s';
}
function toGerund(base){
  if(!base||base.length<2) return null;
  var v="aeiou";
  if(base.length>=3&&!v.includes(base.slice(-1))&&v.includes(base.slice(-2,-1))&&!v.includes(base.slice(-3,-2))&&!'wxy'.includes(base.slice(-1)))
    return base+base.slice(-1)+'ing';
  if(base.endsWith('e')&&base.length>2&&!v.includes(base.slice(-2,-1)))
    return base.slice(0,-1)+'ing';
  return base+'ing';
}
function expandProgressive(sn){
  var results = new Set([sn]);
  var prog = /\b(is|are|am|was|were)\s+(\w+ing)\b/;
  var m = sn.match(prog);
  if(m){
    var be=m[1], gerund=m[2];
    if(gerund.endsWith('ing')){
      var stem=gerund.slice(0,-3);
      if(stem.length>=2&&stem.slice(-1)===stem.slice(-2,-1)) stem=stem.slice(0,-1);
      [stem, stem+'e'].forEach(function(base){
        var third=makeThirdPerson(base);
        results.add(sn.replace(be+' '+gerund, third));
        if(be==='was'||be==='were'){
          results.add(sn.replace(be+' '+gerund, 'used to '+base));
          results.add(sn.replace(be+' '+gerund, 'kept '+gerund));
        }
      });
    }
    return Array.from(results);
  }
  var words = sn.split(' ');
  words.forEach(function(word, i){
    if(word.length<=2||COMMON_WORDS.has(word)) return;
    if(word.endsWith('s')&&!word.endsWith('ss')&&!word.endsWith('us')&&!word.endsWith('is')){
      var candidates=[word.slice(0,-1)];
      if(word.endsWith('es')&&word.length>4) candidates.push(word.slice(0,-2));
      if(word.endsWith('ies')&&word.length>4) candidates.push(word.slice(0,-3)+'y');
      candidates.forEach(function(base){
        var gerund=toGerund(base);
        if(gerund&&gerund.length>=5){
          var w2=words.slice(); w2.splice(i,1,'is',gerund);
          results.add(w2.join(' '));
        }
      });
    }
  });
  return Array.from(results);
}

// ── Motion verb expansion ─────────────────────────────────────────────────────
var MOTION_VERBS = ["approached","approaches","approach","approaching","came","come","comes","coming",
  "went","go","goes","going","arrived","arrives","arrive","arriving","hurried","hurries","hurry","hurrying",
  "rushed","rushes","rush","rushing","sailed","sails","sail","sailing","ran","runs","run","running",
  "returned","returns","return","returning"];

function expandMotionAbsorption(sn){
  var results=new Set([sn]);
  MOTION_VERBS.forEach(function(verb){
    var patIn=new RegExp('\\b'+verb+'\\b (the|a|an|his|her|its|their|my|your) ','g');
    var pm; patIn.lastIndex=0;
    while((pm=patIn.exec(sn))!==null){
      var before=sn.slice(0,pm.index)+verb+' ';
      var after=sn.slice(pm.index+verb.length+1);
      results.add(before+'to '+after);
      results.add(before+'towards '+after);
      patIn.lastIndex=0; break;
    }
    var patStrip=new RegExp('\\b'+verb+'\\s+(to|towards)\\s+','g');
    var stripped=sn.replace(patStrip,verb+' ');
    if(stripped!==sn) results.add(stripped);
  });
  return results;
}

// ── PPP placement expansion ───────────────────────────────────────────────────
function expandParticiplePlacement(sn){
  var results=new Set([sn]);
  var pat=/\b(the|a|an|his|her|its|their|my|your)\s+having[- ]been[- ](\w+(?:ed|d|t|en))\s+(\w+)/g;
  var m;
  while((m=pat.exec(sn))!==null){
    var art=m[1],ppp=m[2],noun=m[3],span=m[0];
    [art+' '+noun+' having been '+ppp, art+' '+noun+' having-been-'+ppp,
     art+' '+ppp+' '+noun, art+' '+noun+' who had been '+ppp,
     art+' '+noun+' which had been '+ppp].forEach(function(alt){
      results.add(sn.replace(span,alt));
    });
  }
  var pat2=/\b(the|a|an|his|her|its|their|my|your)\s+(\w+ed|\w+en)\s+(\w+)/g;
  while((m=pat2.exec(sn))!==null){
    var art=m[1],ppp=m[2],noun=m[3],span=m[0];
    [art+' '+noun+' having been '+ppp, art+' '+noun+' who had been '+ppp,
     art+' having been '+ppp+' '+noun].forEach(function(alt){
      results.add(sn.replace(span,alt));
    });
  }
  return results;
}

// ── Genitive preprocessor ────────────────────────────────────────────────────
function preprocessGenitive(raw){
  return raw.replace(/\b(?:the\s+)?(\w+)'s\s+(\w+)\b/gi, 'the $2 of the $1');
}

// ── Article / possessive strip ────────────────────────────────────────────────
function stripArticles(s){
  return s.replace(/\b(the|a|an|this|that|these|those)\b/g,' ').replace(/\s+/g,' ').trim();
}
function stripPossessives(s){
  return s.replace(/\b(my|your|his|her|its|our|their)\s+/g,'').replace(/\s+/g,' ').trim();
}

// ── Flexible adverbs ──────────────────────────────────────────────────────────
var FLEX_ADVS = new Set(["again","now","always","then","suddenly","quickly","slowly",
  "immediately","scarcely","hardly","barely","soon","already","finally","next",
  "therefore","so","however","nevertheless","still","also","even","there"]);
var MULTI_ADVS = ["at once","at last","straight away","in the end","right away","up to now"];

function stripAdvsArts(s){
  var found=new Set();
  var s2=s.replace(/\b(the|a|an|this|that|these|those)\b/g,' ');
  MULTI_ADVS.slice().sort(function(a,b){return b.length-a.length;}).forEach(function(ph){
    var re=new RegExp('\\b'+ph.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\b','g');
    if(re.test(s2)){found.add(ph); s2=s2.replace(re,' ');}
  });
  var words=s2.replace(/\s+/g,' ').trim().split(' ');
  var remaining=[];
  words.forEach(function(w){if(FLEX_ADVS.has(w)){found.add(w);}else{remaining.push(w);}});
  return {str:remaining.join(' '), advs:found};
}
function setsEqual(a,b){if(a.size!==b.size) return false; a.forEach(function(v){if(!b.has(v)) return false;}); return true;}
function adverbMatch(nAns, target){
  var a=stripAdvsArts(nAns), t=stripAdvsArts(target);
  // compare adverb sets
  var advEq = a.advs.size===t.advs.size;
  if(advEq){a.advs.forEach(function(v){if(!t.advs.has(v))advEq=false;});}
  return advEq && a.str===t.str;
}

// ── Build all targets ─────────────────────────────────────────────────────────
function buildAllTargets(sentence){
  var allTargets=new Set();
  (sentence.english||[]).forEach(function(eng){
    var base=norm(eng).replace(/\.$/,'');
    allTargets.add(base);
    expandProgressive(base).forEach(function(v){allTargets.add(v);});
    if(base.includes('he/she')){
      allTargets.add(base.replace(/he\/she/g,'he'));
      allTargets.add(base.replace(/he\/she/g,'she'));
    }
  });
  // second pass progressive
  Array.from(allTargets).forEach(function(t){
    expandProgressive(t).forEach(function(v){allTargets.add(v);});
  });
  // strip optional trailing pronoun
  Array.from(allTargets).forEach(function(t){
    var words=t.split(' ');
    if(words.length&&['her','him','it','them'].includes(words[words.length-1]))
      allTargets.add(words.slice(0,-1).join(' '));
  });
  // Top 150 synonyms
  Array.from(allTargets).forEach(function(t){
    expandTop150(t).forEach(function(v){allTargets.add(v);});
  });
  // Gloss aliases
  Array.from(allTargets).forEach(function(t){
    expandGlossAliases(t).forEach(function(v){allTargets.add(v);});
  });
  // Motion absorption
  Array.from(allTargets).forEach(function(t){
    expandMotionAbsorption(t).forEach(function(v){allTargets.add(v);});
  });
  // PPP placement
  Array.from(allTargets).forEach(function(t){
    expandParticiplePlacement(t).forEach(function(v){allTargets.add(v);});
  });
  return allTargets;
}

// ── Helper: is number error ───────────────────────────────────────────────────
var IRREG_PLURAL = {man:'men',woman:'women',mouse:'mice',tooth:'teeth',foot:'feet',person:'people',child:'children'};
function isNumberError(a,b){
  if(IRREG_PLURAL[a]===b||IRREG_PLURAL[b]===a) return true;
  return b===a+'s'||b===a+'es'||a===b+'s'||a===b+'es';
}
function isPersonError(a,b){
  var subj=new Set(['i','we','you','he','she','it','they']);
  if(a===b||!subj.has(a)||!subj.has(b)) return false;
  if((a==='i'&&b==='we')||(a==='we'&&b==='i')) return false;
  var third3=new Set(['he','she','it']);
  if((third3.has(a)&&b==='they')||(third3.has(b)&&a==='they')) return false;
  return true;
}
function isTenseSwap(a,b){
  if(a===b||a.length<4||b.length<4) return false;
  var common=0; for(var i=0;i<Math.min(a.length,b.length);i++){if(a[i]===b[i])common++;else break;}
  if(common<3) return false;
  var ps=a.slice(common), ts=b.slice(common);
  var past=new Set(['d','ed','ied']), pres=new Set(['s','es','ies']);
  return (past.has(ps)&&pres.has(ts))||(pres.has(ps)&&past.has(ts));
}
function isEndingOnly(a,b){
  if(a.length<4||b.length<4) return false;
  var common=0; for(var i=0;i<Math.min(a.length,b.length);i++){if(a[i]===b[i])common++;else break;}
  if(common<Math.max(3,Math.floor(Math.min(a.length,b.length)*0.6))) return false;
  return a.slice(common).length<=3&&b.slice(common).length<=3;
}

var WRONG_MESSAGES = ["Unlucky! Take another look at this one.","Whoops! Something's gone wrong here.",
  "Wrong! Give it another go.","Incorrect! You must be exact.","Oh no! Something needs fixing."];
var _wrongIdx=0;
function pickWrong(){return WRONG_MESSAGES[(_wrongIdx++)%WRONG_MESSAGES.length];}

function stripClausePronouns(text){
  return text.replace(/\b(and|but|then|so),?\s+(he|she|it|they|we|i)\s+/gi,'$1 ');
}

// ── checkSentence ─────────────────────────────────────────────────────────────
function checkSentence(pupilAnswer, sentence){
  var raw=(pupilAnswer||'').trim();
  var best=sentence.english[0];
  if(!raw) return {result:'wrong',message:"You didn't type anything.",correct_answer:best,counts_as_correct:false};

  var allTargets=buildAllTargets(sentence);
  var nFull=norm(raw).replace(/\.$/,'');
  var nFullNoQual=nFull.replace(/\byou\s*(sg|pl)\b/g,'you');
  if(nFullNoQual===nFull) nFullNoQual=null;
  var nFullNoPron=norm(stripClausePronouns(raw)).replace(/\.$/,'');
  if(nFullNoPron===nFull) nFullNoPron=null;
  var rawGen=preprocessGenitive(raw);
  var nFullGen=(rawGen!==raw)?norm(rawGen).replace(/\.$/, ''):null;

  function correct(){ return {result:'correct',message:'Correct!',correct_answer:best,counts_as_correct:true}; }

  // Full match passes
  var candidates=[nFull];
  if(nFullNoQual) candidates.push(nFullNoQual);
  if(nFullNoPron) candidates.push(nFullNoPron);
  if(nFullGen)    candidates.push(nFullGen);

  for(var ci=0;ci<candidates.length;ci++){
    var cand=candidates[ci];
    var targArr=Array.from(allTargets);
    for(var ti=0;ti<targArr.length;ti++){
      var target=targArr[ti];
      if(cand===target) return correct();
      if(stripArticles(cand)===stripArticles(target)) return correct();
      if(stripPossessives(stripArticles(cand))===stripPossessives(stripArticles(target))) return correct();
    }
    if(targArr.some(function(t){return adverbMatch(cand,t);})) return correct();
  }

  // Comma-split legacy path
  var parts=raw.split(',').map(function(p){return p.trim();});
  for(var pi=0;pi<parts.length;pi++){
    var nPart=norm(parts[pi]).replace(/\.$/,'');
    var tArr=Array.from(allTargets);
    for(var ti=0;ti<tArr.length;ti++){
      var target=tArr[ti];
      if(nPart===target) return correct();
      if(stripArticles(nPart)===stripArticles(target)) return correct();
      if(stripPossessives(nPart)===stripPossessives(target)) return correct();
    }
    if(tArr.some(function(t){return adverbMatch(nPart,t);})) return correct();
  }

  // Typo path
  var nClean=norm(raw).replace(/\.$/,'');
  var tArr=Array.from(allTargets);
  var REAL_WORD_PAIRS=new Set(["man,woman","woman,man","boy,girl","girl,boy","son,sun","sun,son",
    "god,good","good,god","ship,sheep","sheep,ship","king,queen","queen,king",
    "father,mother","mother,father","kill,kiss"]);
  for(var ti=0;ti<tArr.length;ti++){
    var target=tArr[ti];
    var nw=nClean.split(' '), tw=target.split(' ');
    if(nw.length!==tw.length) continue;
    var diffs=[];
    for(var di=0;di<nw.length;di++) if(nw[di]!==tw[di]) diffs.push([nw[di],tw[di]]);
    if(diffs.length===0) continue;
    if(diffs.length===1){
      var pa=diffs[0][0], pb=diffs[0][1];
      var maxLev=pb.length>=8?2:1;
      var lev=levenshtein(pa,pb);
      if(lev>0&&lev<=maxLev&&pb.length>=5){
        if(REAL_WORD_PAIRS.has(pa+','+pb)||REAL_WORD_PAIRS.has(pb+','+pa)) continue;
        if((pa.match(/(?:ed|ied)$/)&&pb.match(/(?:es|ies|s)$/))||(pb.match(/(?:ed|ied)$/)&&pa.match(/(?:es|ies|s)$/))) continue;
        if((pa+'s')===pb||(pb+'s')===pa) continue;
        var _NUMBER_PAIRS=new Set(["woman,women","man,men","son,sons","daughter,daughters",
          "ship,ships","god,gods","goddess,goddesses","girl,girls","boy,boys",
          "father,fathers","mother,mothers","queen,queens","king,kings","friend,friends",
          "sword,swords","city,cities","island,islands","land,lands"]);
        if(_NUMBER_PAIRS.has(pa+','+pb)||_NUMBER_PAIRS.has(pb+','+pa)) continue;
        return {result:'typo',message:"Almost! Watch your spelling.",correct_answer:best,counts_as_correct:true,is_typo:true};
      }
    }
  }

  // Original targets for specific hints
  var origTargets=(sentence.english||[]).map(function(e){return norm(e).replace(/\.$/,'');});
  var nAns=norm(parts[0]).replace(/\.$/,'');

  // Tense swap check
  for(var oi=0;oi<origTargets.length;oi++){
    var oNw=nAns.split(' '), oTw=origTargets[oi].split(' ');
    if(oNw.length===oTw.length){
      var diffs=[];
      for(var di=0;di<oNw.length;di++) if(oNw[di]!==oTw[di]) diffs.push([oNw[di],oTw[di]]);
      if(diffs.length>0&&diffs.every(function(d){return isTenseSwap(d[0],d[1]);})){
        var pIsPast=diffs.some(function(d){return /(?:ed|d|ied)$/.test(d[0]);});
        return {result:'wrong',
          message:'Close! You misidentified the tense of the verb. (Should be **'+(pIsPast?'present':'past')+'**, not '+(pIsPast?'past':'present')+')',
          correct_answer:best,counts_as_correct:false};
      }
    }
  }

  // you without sg/pl
  if(/\byou\b/.test(nAns)&&!/\byou\s*(sg|pl|\(sg\)|\(pl\))/.test(nAns)){
    for(var ti=0;ti<tArr.length;ti++){
      var stripped=tArr[ti].replace(/\byou\s*(sg|pl|\(sg\)|\(pl\))\s*/g,'you ').replace(/\s+/g,' ').trim();
      if(nAns===stripped) return {result:'wrong',message:"You need to specify whether it's singular or plural. Be precise!",correct_answer:best,counts_as_correct:false};
    }
  }

  // Number / person errors
  for(var oi=0;oi<origTargets.length;oi++){
    var oNw=nAns.split(' '), oTw=origTargets[oi].split(' ');
    if(oNw.length===oTw.length){
      var diffs=[];
      for(var di=0;di<oNw.length;di++) if(oNw[di]!==oTw[di]) diffs.push([oNw[di],oTw[di]]);
      if(diffs.length===1&&isNumberError(diffs[0][0],diffs[0][1]))
        return {result:'wrong',message:"Nearly! You need to make sure what's singular versus plural.",correct_answer:best,counts_as_correct:false};
      if(diffs.length===1&&isPersonError(diffs[0][0],diffs[0][1]))
        return {result:'wrong',message:"Nearly! Check who's doing the action.",correct_answer:best,counts_as_correct:false};
    }
    if(isEndingOnly(nAns,origTargets[oi])&&levenshtein(nAns,origTargets[oi])<=3)
      return {result:'wrong',message:"Check your ending carefully.",correct_answer:best,counts_as_correct:false};
    if(levenshtein(nAns,origTargets[oi])<=2){
      var oNw2=nAns.split(' '), oTw2=origTargets[oi].split(' ');
      if(oNw2.length===oTw2.length){
        var diffs2=[];
        for(var di=0;di<oNw2.length;di++) if(oNw2[di]!==oTw2[di]) diffs2.push([oNw2[di],oTw2[di]]);
        if(diffs2.some(function(d){return (d[0]==='in'&&d[1]==='into')||(d[0]==='into'&&d[1]==='in');}))
          return {result:'wrong',message:"*in* + accusative = 'into' (motion); *in* + ablative = 'in' (position).",correct_answer:best,counts_as_correct:false};
        if(diffs2.some(function(d){return isTenseSwap(d[0],d[1]);})){
          var anyImpf=origTargets.some(function(t){return /\b(was|were)\s+\w+ing\b|\bused\s+to\s+\w+|\bkept\s+\w+ing\b/.test(t);});
          var pIsPast=diffs2.some(function(d){return /(?:ed|d|ied)$/.test(d[0]);});
          if(anyImpf&&pIsPast) return {result:'wrong',message:"Close! This verb is **imperfect** — use *'was ...ing'*, *'used to ...'*, or *'kept ...ing'* — not simple past.",correct_answer:best,counts_as_correct:false};
          return {result:'wrong',message:'Close! You misidentified the tense.',correct_answer:best,counts_as_correct:false};
        }
        if(diffs2.some(function(d){return isNumberError(d[0],d[1]);}))
          return {result:'wrong',message:"Nearly! You need to make sure what's singular versus plural.",correct_answer:best,counts_as_correct:false};
        if(diffs2.length===1&&levenshtein(diffs2[0][0],diffs2[0][1])>=2)
          return {result:'wrong',message:pickWrong(),correct_answer:best,counts_as_correct:false};
        if(diffs2.length>=2)
          return {result:'wrong',message:pickWrong(),correct_answer:best,counts_as_correct:false};
      }
      return {result:'typo',message:"Almost! Watch your spelling.",correct_answer:best,counts_as_correct:true,is_typo:true};
    }
  }

  // Imperfect hint
  var anyImpf=origTargets.some(function(t){return /\b(was|were)\s+\w+ing\b|\bused\s+to\s+\w+|\bkept\s+\w+ing\b/.test(t);});
  if(anyImpf&&!/\b(was|were|had)\b/.test(nAns)&&/\b\w+(?:ed|ied)\b/.test(nAns))
    return {result:'wrong',message:"Close! This verb is **imperfect** — use *'was ...ing'*, *'used to ...'*, or *'kept ...ing'* — not simple past.",correct_answer:best,counts_as_correct:false};

  return {result:'wrong',message:pickWrong(),correct_answer:best,counts_as_correct:false};
}

// ── checkLatinTyped ───────────────────────────────────────────────────────────
function checkLatinTyped(pupilAnswer, correctLatin){
  var raw=(pupilAnswer||'').trim();
  if(!raw) return {result:'wrong',message:"You didn't type anything.",correct_answer:correctLatin,counts_as_correct:false};
  if(normLat(raw)===normLat(correctLatin)) return {result:'correct',message:'Correct!',correct_answer:correctLatin,counts_as_correct:true};
  return {result:'wrong',message:pickWrong(),correct_answer:correctLatin,counts_as_correct:false};
}

// ── checkAllFourParts ─────────────────────────────────────────────────────────
function checkAllFourParts(pupilAnswer, correctInf, correctPerf, correctPpp){
  var raw=(pupilAnswer||'').trim();
  var hasPpp=correctPpp!=null&&correctPpp!=='null'&&correctPpp!=='';
  var correctAnswer=hasPpp?correctInf+' '+correctPerf+' '+correctPpp:correctInf+' '+correctPerf;
  var expectedCount=hasPpp?3:2;
  if(!raw) return {result:'wrong',message:'You didn\'t type anything. The answer is: *'+correctAnswer+'*',correct_answer:correctAnswer,counts_as_correct:false};
  var parts=splitParts(raw);
  if(parts.length!==expectedCount){
    if(!hasPpp&&parts.length===3) return {result:'wrong',message:'This verb has no PPP. Type only the infinitive and perfect: *'+correctAnswer+'*',correct_answer:correctAnswer,counts_as_correct:false};
    return {result:'wrong',message:'Type '+expectedCount+' parts separated by spaces. The answer is: *'+correctAnswer+'*',correct_answer:correctAnswer,counts_as_correct:false};
  }
  var okInf=normLat(parts[0])===normLat(correctInf);
  var okPerf=normLat(parts[1])===normLat(correctPerf);
  var okPpp=!hasPpp||(normLat(parts[2])===normLat(correctPpp));
  if(okInf&&okPerf&&okPpp) return {result:'correct',message:'Correct!',correct_answer:correctAnswer,counts_as_correct:true};
  var errors=[];
  if(!okInf) errors.push('infinitive: *'+correctInf+'*');
  if(!okPerf) errors.push('perfect: *'+correctPerf+'*');
  if(hasPpp&&!okPpp) errors.push('PPP: *'+correctPpp+'*');
  return {result:'wrong',message:'Check: '+errors.join('; ')+'.',correct_answer:correctAnswer,counts_as_correct:false};
}

// ── checkParsing ──────────────────────────────────────────────────────────────
var _PERSON_NUM_MAP = {
  "i":["1st","singular"],"1st singular":["1st","singular"],
  "you (sg)":["2nd","singular"],"you sg":["2nd","singular"],"2nd singular":["2nd","singular"],
  "he/she/it":["3rd","singular"],"he/she":["3rd","singular"],"3rd singular":["3rd","singular"],
  "we":["1st","plural"],"1st plural":["1st","plural"],
  "you (pl)":["2nd","plural"],"you pl":["2nd","plural"],"2nd plural":["2nd","plural"],
  "they":["3rd","plural"],"3rd plural":["3rd","plural"],
};
function checkParsing(pupilTense,pupilPerson,pupilNumber,correctTense,correctPerson,correctNumber){
  var lookup=(pupilPerson||'').toLowerCase().trim();
  var pn=_PERSON_NUM_MAP[lookup]||[pupilPerson,pupilNumber];
  var pt=(pupilTense||'').toLowerCase().trim(), ct=(correctTense||'').toLowerCase().trim();
  var pp=pn[0].toLowerCase().trim(), cp=(correctPerson||'').toLowerCase().trim();
  var pn2=pn[1].toLowerCase().trim(), cn=(correctNumber||'').toLowerCase().trim();
  var ok=(pt===ct&&pp===cp&&pn2===cn);
  if(ok) return {result:'correct',message:'Correct!',counts_as_correct:true};
  var errors=[];
  if(pt!==ct) errors.push('tense: **'+correctTense+'**');
  if(pp!==cp) errors.push('person: **'+correctPerson+'**');
  if(pn2!==cn) errors.push('number: **'+correctNumber+'**');
  return {result:'wrong',message:'Not quite. '+errors.join('; ')+'.',counts_as_correct:false};
}

// ── Vocab (simple) ────────────────────────────────────────────────────────────
function checkVocabSimple(pupilAnswer, correctAnswer){
  var raw=(pupilAnswer||'').trim();
  if(!raw) return {result:'wrong',message:"You didn't type anything.",correct_answer:correctAnswer,counts_as_correct:false};
  var pa=norm(raw), ca=norm(correctAnswer);
  if(pa===ca) return {result:'correct',message:'Correct!',correct_answer:correctAnswer,counts_as_correct:true};
  // Check comma-separated parts
  var parts=correctAnswer.split(/,\s*/);
  if(parts.some(function(p){return norm(p)===pa;})) return {result:'correct',message:'Correct!',correct_answer:correctAnswer,counts_as_correct:true};
  return {result:'wrong',message:pickWrong(),correct_answer:correctAnswer,counts_as_correct:false};
}

// ── Expose globally ───────────────────────────────────────────────────────────
window._marking = {
  checkSentence: checkSentence,
  checkLatinTyped: checkLatinTyped,
  checkAllFourParts: checkAllFourParts,
  checkParsing: checkParsing,
  checkVocabSimple: checkVocabSimple,
  normLat: normLat,
  norm: norm,
  PLATFORM_DATA: null, // set by platform-compiled.js
};

})();
