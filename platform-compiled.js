"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function ownKeys(e, r) { var t = Object.keys(e); if (Object.getOwnPropertySymbols) { var o = Object.getOwnPropertySymbols(e); r && (o = o.filter(function (r) { return Object.getOwnPropertyDescriptor(e, r).enumerable; })), t.push.apply(t, o); } return t; }
function _objectSpread(e) { for (var r = 1; r < arguments.length; r++) { var t = null != arguments[r] ? arguments[r] : {}; r % 2 ? ownKeys(Object(t), !0).forEach(function (r) { _defineProperty(e, r, t[r]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(t)) : ownKeys(Object(t)).forEach(function (r) { Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(t, r)); }); } return e; }
function _defineProperty(e, r, t) { return (r = _toPropertyKey(r)) in e ? Object.defineProperty(e, r, { value: t, enumerable: !0, configurable: !0, writable: !0 }) : e[r] = t, e; }
function _toPropertyKey(t) { var i = _toPrimitive(t, "string"); return "symbol" == _typeof(i) ? i : i + ""; }
function _toPrimitive(t, r) { if ("object" != _typeof(t) || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || "default"); if ("object" != _typeof(i)) return i; throw new TypeError("@@toPrimitive must return a primitive value."); } return ("string" === r ? String : Number)(t); }
function _regenerator() { /*! regenerator-runtime -- Copyright (c) 2014-present, Facebook, Inc. -- license (MIT): https://github.com/babel/babel/blob/main/packages/babel-helpers/LICENSE */ var e, t, r = "function" == typeof Symbol ? Symbol : {}, n = r.iterator || "@@iterator", o = r.toStringTag || "@@toStringTag"; function i(r, n, o, i) { var c = n && n.prototype instanceof Generator ? n : Generator, u = Object.create(c.prototype); return _regeneratorDefine2(u, "_invoke", function (r, n, o) { var i, c, u, f = 0, p = o || [], y = !1, G = { p: 0, n: 0, v: e, a: d, f: d.bind(e, 4), d: function d(t, r) { return i = t, c = 0, u = e, G.n = r, a; } }; function d(r, n) { for (c = r, u = n, t = 0; !y && f && !o && t < p.length; t++) { var o, i = p[t], d = G.p, l = i[2]; r > 3 ? (o = l === n) && (u = i[(c = i[4]) ? 5 : (c = 3, 3)], i[4] = i[5] = e) : i[0] <= d && ((o = r < 2 && d < i[1]) ? (c = 0, G.v = n, G.n = i[1]) : d < l && (o = r < 3 || i[0] > n || n > l) && (i[4] = r, i[5] = n, G.n = l, c = 0)); } if (o || r > 1) return a; throw y = !0, n; } return function (o, p, l) { if (f > 1) throw TypeError("Generator is already running"); for (y && 1 === p && d(p, l), c = p, u = l; (t = c < 2 ? e : u) || !y;) { i || (c ? c < 3 ? (c > 1 && (G.n = -1), d(c, u)) : G.n = u : G.v = u); try { if (f = 2, i) { if (c || (o = "next"), t = i[o]) { if (!(t = t.call(i, u))) throw TypeError("iterator result is not an object"); if (!t.done) return t; u = t.value, c < 2 && (c = 0); } else 1 === c && (t = i.return) && t.call(i), c < 2 && (u = TypeError("The iterator does not provide a '" + o + "' method"), c = 1); i = e; } else if ((t = (y = G.n < 0) ? u : r.call(n, G)) !== a) break; } catch (t) { i = e, c = 1, u = t; } finally { f = 1; } } return { value: t, done: y }; }; }(r, o, i), !0), u; } var a = {}; function Generator() {} function GeneratorFunction() {} function GeneratorFunctionPrototype() {} t = Object.getPrototypeOf; var c = [][n] ? t(t([][n]())) : (_regeneratorDefine2(t = {}, n, function () { return this; }), t), u = GeneratorFunctionPrototype.prototype = Generator.prototype = Object.create(c); function f(e) { return Object.setPrototypeOf ? Object.setPrototypeOf(e, GeneratorFunctionPrototype) : (e.__proto__ = GeneratorFunctionPrototype, _regeneratorDefine2(e, o, "GeneratorFunction")), e.prototype = Object.create(u), e; } return GeneratorFunction.prototype = GeneratorFunctionPrototype, _regeneratorDefine2(u, "constructor", GeneratorFunctionPrototype), _regeneratorDefine2(GeneratorFunctionPrototype, "constructor", GeneratorFunction), GeneratorFunction.displayName = "GeneratorFunction", _regeneratorDefine2(GeneratorFunctionPrototype, o, "GeneratorFunction"), _regeneratorDefine2(u), _regeneratorDefine2(u, o, "Generator"), _regeneratorDefine2(u, n, function () { return this; }), _regeneratorDefine2(u, "toString", function () { return "[object Generator]"; }), (_regenerator = function _regenerator() { return { w: i, m: f }; })(); }
function _regeneratorDefine2(e, r, n, t) { var i = Object.defineProperty; try { i({}, "", {}); } catch (e) { i = 0; } _regeneratorDefine2 = function _regeneratorDefine(e, r, n, t) { function o(r, n) { _regeneratorDefine2(e, r, function (e) { return this._invoke(r, n, e); }); } r ? i ? i(e, r, { value: n, enumerable: !t, configurable: !t, writable: !t }) : e[r] = n : (o("next", 0), o("throw", 1), o("return", 2)); }, _regeneratorDefine2(e, r, n, t); }
function asyncGeneratorStep(n, t, e, r, o, a, c) { try { var i = n[a](c), u = i.value; } catch (n) { return void e(n); } i.done ? t(u) : Promise.resolve(u).then(r, o); }
function _asyncToGenerator(n) { return function () { var t = this, e = arguments; return new Promise(function (r, o) { var a = n.apply(t, e); function _next(n) { asyncGeneratorStep(a, r, o, _next, _throw, "next", n); } function _throw(n) { asyncGeneratorStep(a, r, o, _next, _throw, "throw", n); } _next(void 0); }); }; }
function _createForOfIteratorHelper(r, e) { var t = "undefined" != typeof Symbol && r[Symbol.iterator] || r["@@iterator"]; if (!t) { if (Array.isArray(r) || (t = _unsupportedIterableToArray(r)) || e && r && "number" == typeof r.length) { t && (r = t); var _n = 0, F = function F() {}; return { s: F, n: function n() { return _n >= r.length ? { done: !0 } : { done: !1, value: r[_n++] }; }, e: function e(r) { throw r; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var o, a = !0, u = !1; return { s: function s() { t = t.call(r); }, n: function n() { var r = t.next(); return a = r.done, r; }, e: function e(r) { u = !0, o = r; }, f: function f() { try { a || null == t.return || t.return(); } finally { if (u) throw o; } } }; }
function _slicedToArray(r, e) { return _arrayWithHoles(r) || _iterableToArrayLimit(r, e) || _unsupportedIterableToArray(r, e) || _nonIterableRest(); }
function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }
function _iterableToArrayLimit(r, l) { var t = null == r ? null : "undefined" != typeof Symbol && r[Symbol.iterator] || r["@@iterator"]; if (null != t) { var e, n, i, u, a = [], f = !0, o = !1; try { if (i = (t = t.call(r)).next, 0 === l) { if (Object(t) !== t) return; f = !1; } else for (; !(f = (e = i.call(t)).done) && (a.push(e.value), a.length !== l); f = !0); } catch (r) { o = !0, n = r; } finally { try { if (!f && null != t.return && (u = t.return(), Object(u) !== u)) return; } finally { if (o) throw n; } } return a; } }
function _arrayWithHoles(r) { if (Array.isArray(r)) return r; }
function _toConsumableArray(r) { return _arrayWithoutHoles(r) || _iterableToArray(r) || _unsupportedIterableToArray(r) || _nonIterableSpread(); }
function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }
function _unsupportedIterableToArray(r, a) { if (r) { if ("string" == typeof r) return _arrayLikeToArray(r, a); var t = {}.toString.call(r).slice(8, -1); return "Object" === t && r.constructor && (t = r.constructor.name), "Map" === t || "Set" === t ? Array.from(r) : "Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t) ? _arrayLikeToArray(r, a) : void 0; } }
function _iterableToArray(r) { if ("undefined" != typeof Symbol && null != r[Symbol.iterator] || null != r["@@iterator"]) return Array.from(r); }
function _arrayWithoutHoles(r) { if (Array.isArray(r)) return _arrayLikeToArray(r); }
function _arrayLikeToArray(r, a) { (null == a || a > r.length) && (a = r.length); for (var e = 0, n = Array(a); e < a; e++) n[e] = r[e]; return n; }
var _React = React,
  useState = _React.useState,
  useEffect = _React.useEffect,
  useRef = _React.useRef;
var api = function api(p) {
  var opts = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};
  if (p === '/api/sets') return Promise.resolve(PLATFORM_DATA.sets_list);
  var sm = p.match(/^\/api\/sets\/(\d+)$/);
  if (sm) return Promise.resolve(PLATFORM_DATA.sets_by_id[sm[1]] || null);
  return Promise.resolve([]);
};
var _nl = function _nl(s) {
  return (s || '').toLowerCase().replace(/[^a-z ]/g, '').replace(/\s+/g, ' ').trim();
};
var _ne = function _ne(s) {
  return (s || '').toLowerCase().replace(/[^a-z0-9 ]/g, ' ').replace(/\s+/g, ' ').trim();
};
var post = function post(p, b) {
  if (p !== '/api/check') return Promise.resolve({
    session_id: 0
  });
  var qt = b && b.question_type || '';
  var pa = b && b.pupil_answer || '';
  var ca = b && b.correct_answer || '';
  var ok = false;
  if (qt === 'flashcard_rating') {
    ok = pa === 'got_it';
  } else if (['mc', 'parsing_mcq', 'translate_form', 'tense_id'].includes(qt)) {
    ok = pa === ca;
  } else if (qt === 'latin_typed' || qt === 'all_four_typed') {
    ok = _nl(pa) === _nl(ca);
  } else {
    var setD = PLATFORM_DATA.sets_by_id[String(b && b.set_id)];
    var sents = setD && setD.sentences || [];
    var qt2 = b && b.question_text || '';
    var sent = sents.find(function (s) {
      return _ne(s.latin) === _ne(qt2);
    });
    if (sent && sent.english) {
      ok = sent.english.some(function (e) {
        return _ne(e) === _ne(pa);
      });
    } else {
      ok = _ne(pa) === _ne(ca) && pa.length > 0;
    }
  }
  return Promise.resolve({
    counts_as_correct: ok,
    correct_answer: ca,
    result: ok ? 'correct' : 'wrong',
    message: ok ? 'Correct!' : 'Not quite — ' + ca
  });
};
// Shuffle once and lock - do NOT re-shuffle on state update
var shuffleOnce = function shuffleOnce(arr) {
  var a = _toConsumableArray(arr);
  for (var i = a.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var _ref = [a[j], a[i]];
    a[i] = _ref[0];
    a[j] = _ref[1];
  }
  return a;
};
// Always scroll .activity-body back to top (window.scrollTo doesn't reach it)
var resetScroll = function resetScroll() {
  var _document$querySelect;
  (_document$querySelect = document.querySelector('.activity-body')) === null || _document$querySelect === void 0 || _document$querySelect.scrollTo({
    top: 0,
    behavior: 'instant'
  });
};

// Streak context — lets ProgressBar read the streak without prop drilling
var StreakCtx = React.createContext(0);
var streakTier = function streakTier(s) {
  return s >= 60 ? 't9' : s >= 45 ? 't8' : s >= 35 ? 't7' : s >= 25 ? 't6' : s >= 20 ? 't5' : s >= 15 ? 't4' : s >= 10 ? 't3' : s >= 6 ? 't2' : 't1';
};
function ProgressBar(_ref2) {
  var pct = _ref2.pct;
  var streak = React.useContext(StreakCtx);
  var tier = streakTier(streak);
  var prevTierRef = useRef(null);
  var _useState = useState(false),
    _useState2 = _slicedToArray(_useState, 2),
    bumping = _useState2[0],
    setBumping = _useState2[1];
  useEffect(function () {
    if (streak >= 3 && prevTierRef.current !== null && prevTierRef.current !== tier) {
      setBumping(true);
      var t = setTimeout(function () {
        return setBumping(false);
      }, 450);
      return function () {
        return clearTimeout(t);
      };
    }
    prevTierRef.current = tier;
  }, [tier, streak]);
  return /*#__PURE__*/React.createElement("div", {
    className: "progress-track",
    style: {
      overflow: 'visible',
      position: 'relative'
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "progress-fill",
    style: {
      width: "".concat(pct, "%")
    }
  }), streak >= 3 && /*#__PURE__*/React.createElement("span", {
    className: "streak-chip ".concat(tier).concat(bumping ? ' bumping' : ''),
    style: {
      left: "".concat(Math.max(2, Math.min(98, pct)), "%")
    }
  }, streak));
}
var StreakChip = function StreakChip(_ref3) {
  var streak = _ref3.streak;
  var tier = streakTier(streak);
  return /*#__PURE__*/React.createElement("span", {
    className: "streak-chip ".concat(tier),
    style: {
      position: 'static',
      transform: 'none'
    },
    title: "Correct in a row"
  }, /*#__PURE__*/React.createElement("strong", null, streak));
};
function PopText(_ref4) {
  var text = _ref4.text,
    active = _ref4.active;
  var chars = React.useMemo(function () {
    return _toConsumableArray(text).map(function (c, i) {
      return {
        c: c,
        rot: ((i % 2 === 0 ? -1 : 1) * (6 + i * 3.7 % 6)).toFixed(1),
        delay: (i * 0.055).toFixed(3)
      };
    });
  }, [text]);
  if (!active) return /*#__PURE__*/React.createElement("span", null, text);
  return /*#__PURE__*/React.createElement("span", null, chars.map(function (ch, i) {
    return ch.c === ' ' ? /*#__PURE__*/React.createElement("span", {
      key: i,
      style: {
        display: 'inline-block',
        width: '.32em'
      }
    }, "\xA0") : /*#__PURE__*/React.createElement("span", {
      key: i,
      className: "poptext-ch",
      style: {
        '--r': ch.rot + 'deg',
        '--d': ch.delay + 's'
      }
    }, ch.c);
  }));
}
function CardPile(_ref5) {
  var count = _ref5.count,
    hardCount = _ref5.hardCount,
    side = _ref5.side;
  var isRight = side === 'right';
  var shown = Math.min(count, 3);
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 5,
      width: 96,
      flexShrink: 0,
      paddingLeft: isRight ? 8 : 0,
      paddingRight: isRight ? 0 : 8,
      boxSizing: 'border-box',
      overflow: 'visible'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'relative',
      width: 76,
      height: 52
    }
  }, count === 0 && /*#__PURE__*/React.createElement("div", {
    style: {
      width: 76,
      height: 52,
      border: '1px dashed var(--lgrey)',
      borderRadius: 8,
      opacity: 0.25,
      boxSizing: 'border-box'
    }
  }), _toConsumableArray(Array(shown)).map(function (_, i) {
    var rot = side === 'left' ? -(shown - i) * 1.8 : (shown - i) * 1.8;
    return /*#__PURE__*/React.createElement("div", {
      key: i,
      style: {
        position: 'absolute',
        inset: 0,
        background: 'var(--white)',
        border: '1px solid #dde3ea',
        borderRadius: 8,
        transform: "rotate(".concat(rot, "deg)"),
        boxShadow: '0 1px 3px rgba(0,0,0,0.06)',
        zIndex: i
      }
    });
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 3,
      overflow: 'visible'
    }
  }, count > 0 && /*#__PURE__*/React.createElement("span", {
    style: {
      background: isRight ? '#16a34a' : '#64748b',
      color: 'white',
      borderRadius: 5,
      padding: '2px 10px',
      fontSize: '0.72rem',
      fontWeight: 800,
      lineHeight: 1.4,
      letterSpacing: '0.02em',
      whiteSpace: 'nowrap'
    }
  }, count), !isRight && (hardCount || 0) > 0 && /*#__PURE__*/React.createElement("span", {
    style: {
      background: '#f59e0b',
      color: 'white',
      borderRadius: 5,
      padding: '2px 7px',
      fontSize: '0.7rem',
      fontWeight: 800,
      lineHeight: 1.4,
      whiteSpace: 'nowrap'
    }
  }, "+", hardCount)));
}

// Render ordinal suffixes as superscript: 1st → 1<sup>st</sup>
var renderOrdinals = function renderOrdinals(text) {
  if (!text) return text;
  return text.replace(/(\d+)(st|nd|rd|th)\b/g, function (m, n, s) {
    return "".concat(n, "<sup>").concat(s, "</sup>");
  });
};

// Verbs that take the dative — show a note on their flashcard
var DATIVE_VERBS = new Set(['impero', 'imperare', 'imperavi', 'imperatus', 'persuadeo', 'persuadere', 'persuasi', 'persuasus']);
var renderScaffolded = function renderScaffolded(text) {
  if (!text || !text.includes('-')) return /*#__PURE__*/React.createElement("span", {
    className: "latin"
  }, text);
  return /*#__PURE__*/React.createElement("span", {
    className: "latin"
  }, text.split('').map(function (c, i) {
    return c === '-' ? /*#__PURE__*/React.createElement("span", {
      key: i,
      style: {
        color: '#bbb',
        fontWeight: 400
      }
    }, "-") : /*#__PURE__*/React.createElement("span", {
      key: i
    }, c);
  }));
};
var renderVocabLatin = function renderVocabLatin(v) {
  if (v.display_label && v.pos !== 'pronoun') {
    return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
      className: "latin"
    }, v.latin), /*#__PURE__*/React.createElement("span", {
      style: {
        fontSize: '0.6em',
        color: 'var(--white)',
        fontWeight: 800,
        fontStyle: 'normal',
        marginLeft: 6,
        padding: '3px 8px',
        background: '#0D9488',
        borderRadius: 6,
        textTransform: 'uppercase',
        verticalAlign: 'middle'
      }
    }, v.display_label.toUpperCase()));
  }
  if (v.dative_note) {
    return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
      className: "latin"
    }, v.latin), /*#__PURE__*/React.createElement("span", {
      style: {
        fontSize: '0.6em',
        color: 'var(--white)',
        fontWeight: 800,
        fontStyle: 'normal',
        marginLeft: 6,
        padding: '3px 8px',
        background: '#0D9488',
        borderRadius: 6,
        textTransform: 'uppercase',
        verticalAlign: 'middle'
      }
    }, "+DAT"));
  }
  return /*#__PURE__*/React.createElement("span", {
    className: "latin"
  }, v.latin);
};
var COLOR_WORDS = {
  'coral': 'var(--coral)',
  'red': 'var(--coral)',
  'blue': 'var(--blue)',
  'purple': '#7C3AED',
  'gold': 'var(--gold)',
  'yellow': 'var(--gold)',
  'magenta': '#DB2777',
  'pink': '#DB2777',
  'teal': '#0D9488',
  'navy': '#1F3864'
};
// Colour-tag syntax used in explanation strings to colour-code Latin form
// segments and matching grammar terms. Convention:
//   {R:am}  red       — stem vowel
//   {B:t}   blue      — person ending (verb)
//   {P:ba}  purple    — tense marker  (-ba-, -bo/-bi/-bu, -v-, -u-, -s-)
//   {M:era} magenta   — pluperfect marker (-era-)
//   {T:a}   teal      — noun case ending  (also case-name terms)
//   {N:subject} navy  — semantic role     (subject, object, …)
var TAG_COLORS = {
  R: 'var(--coral)',
  B: 'var(--blue)',
  P: '#7C3AED',
  M: '#DB2777',
  T: '#0D9488',
  N: '#1F3864'
};
var renderTextWithKey = function renderTextWithKey(text) {
  if (!text) return null;
  // Accept "Colour key:" either mid-string (preceded by \n) OR at the very
  // start of the string (the Future table_note has no body, just the key).
  var ckIdx = text.indexOf('\nColour key:');
  var mainPart, ckRaw;
  if (ckIdx === -1) {
    if (text.startsWith('Colour key:')) {
      mainPart = '';
      ckRaw = text;
    } else return renderText(text);
  } else {
    mainPart = text.slice(0, ckIdx);
    ckRaw = text.slice(ckIdx + 1);
  }
  // Parse colour key lines: each "**colour** = label"
  var ckLines = ckRaw.replace(/^Colour key:\n?/, '').split('\n').filter(function (l) {
    return l.trim();
  });
  var chips = ckLines.map(function (line) {
    var m = line.match(/\*+([a-zA-Z]+)\*+\s*=\s*(.+)/i);
    if (!m) return null;
    var col = COLOR_WORDS[m[1].toLowerCase()] || m[1];
    return {
      color: col,
      label: m[2].trim(),
      name: m[1]
    };
  }).filter(Boolean);
  return /*#__PURE__*/React.createElement(React.Fragment, null, mainPart && /*#__PURE__*/React.createElement("span", {
    style: {
      display: 'block',
      marginBottom: 8
    }
  }, renderText(mainPart)), chips.length > 0 && /*#__PURE__*/React.createElement("div", {
    className: "colour-key"
  }, chips.map(function (c, i) {
    return /*#__PURE__*/React.createElement("span", {
      key: i,
      className: "colour-key-item"
    }, /*#__PURE__*/React.createElement("span", {
      className: "colour-chip",
      style: {
        background: c.color,
        border: '1px solid rgba(0,0,0,0.12)'
      }
    }), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--navy)'
      }
    }, c.name), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--grey)',
        fontWeight: 500,
        fontStyle: 'normal'
      }
    }, "= ", renderText(c.label)));
  })));
};
var renderText = function renderText(text) {
  if (!text) return null;
  return text.split('\n').map(function (line, l) {
    return /*#__PURE__*/React.createElement(React.Fragment, {
      key: l
    }, line.split(/(\*\*.*?\*\*|\*[^*]+\*|\{[RBPMTN]:[^}]+\})/g).map(function (part, i) {
      // {R:am} {B:t} {P:ba} {M:era} {T:a} {N:subject} colour-tag spans
      var tag = part.match(/^\{([RBPMTN]):(.+)\}$/);
      if (tag) {
        var col = TAG_COLORS[tag[1]];
        return /*#__PURE__*/React.createElement("strong", {
          key: i,
          style: {
            color: col,
            fontWeight: 900
          }
        }, tag[2]);
      }
      if (part.startsWith('**') && part.endsWith('**')) {
        var inner = part.slice(2, -2);
        var _col = COLOR_WORDS[inner.toLowerCase()];
        if (_col) return /*#__PURE__*/React.createElement("strong", {
          key: i,
          style: {
            fontWeight: 900,
            color: _col
          }
        }, inner);
        return /*#__PURE__*/React.createElement("strong", {
          key: i,
          style: {
            fontWeight: 900,
            color: 'var(--navy)'
          },
          dangerouslySetInnerHTML: {
            __html: renderOrdinals(inner)
          }
        });
      }
      if (part.startsWith('*') && part.endsWith('*')) {
        var _inner = part.slice(1, -1);
        return /*#__PURE__*/React.createElement("em", {
          key: i,
          className: "latin"
        }, _inner.split(/(\{[RBPMTN]:[^}]+\})/g).map(function (p, j) {
          var t = p.match(/^\{([RBPMTN]):(.+)\}$/);
          if (t) return /*#__PURE__*/React.createElement("strong", {
            key: j,
            style: {
              color: TAG_COLORS[t[1]],
              fontWeight: 900,
              fontStyle: 'italic'
            }
          }, t[2]);
          return p || null;
        }));
      }
      return /*#__PURE__*/React.createElement("span", {
        key: i,
        dangerouslySetInnerHTML: {
          __html: renderOrdinals(part)
        }
      });
    }), l < text.split('\n').length - 1 && /*#__PURE__*/React.createElement("br", null));
  });
};

// renderExplanation: parses bullet + sub-rule lines into a structured
// explanation. Bullet format: "• latin (gloss) — info"
// Sub-rule format: "  → set phrase" (indented arrow on its own line)
var renderExplanation = function renderExplanation(text) {
  if (!text) return null;
  var lines = text.split('\n').filter(function (p) {
    return p.trim();
  });
  var BULLET_RE = /^\s*•\s*([^()]+?)\s*\(([^)]*)\)\s*(?:[:—-]\s*(.*))?$/;
  var BULLET_NO_PAREN = /^\s*•\s*([^:—\-(]+?)\s*[:—-]\s*(.*)$/;
  var SUBRULE_RE = /^\s*→\s*(.+)$/;
  var bullets = [];
  var orphans = [];
  var lastBullet = null;
  var _iterator = _createForOfIteratorHelper(lines),
    _step;
  try {
    for (_iterator.s(); !(_step = _iterator.n()).done;) {
      var part = _step.value;
      var raw = part.trimEnd().replace(/\.$/, '');
      var sr = raw.match(SUBRULE_RE);
      if (sr) {
        if (lastBullet) {
          lastBullet.subrules = lastBullet.subrules || [];
          lastBullet.subrules.push(sr[1]);
        } else orphans.push(sr[1]);
        continue;
      }
      var m = raw.match(BULLET_RE);
      var latin = void 0,
        gloss = void 0,
        info = void 0;
      if (m) {
        var _m = _slicedToArray(m, 4);
        latin = _m[1];
        gloss = _m[2];
        info = _m[3];
        info = info || '';
      } else {
        var m2 = raw.match(BULLET_NO_PAREN);
        if (!m2) {
          orphans.push(raw.replace(/^\s*•\s*/, ''));
          continue;
        }
        var _m2 = _slicedToArray(m2, 3);
        latin = _m2[1];
        info = _m2[2];
        gloss = "";
      }
      var lo = info.toLowerCase();
      var role = "other";
      if (lo.includes("nominative")) role = "nom";else if (lo.includes("accusative")) role = "acc";else if (lo.includes("dative")) role = "dat";else if (lo.includes("ablative")) role = "abl";else if (lo.includes("genitive")) role = "gen";else if (lo.includes("verb") || lo.includes("tense") || lo.includes(" form")) role = "verb";else if (lo.includes("preposition") || lo.includes("prep")) role = "prep";else if (lo.includes("conjunction")) role = "conj";else if (lo.includes("adverb")) role = "adv";else if (lo.includes("adjective")) role = "adj";else if (lo.includes("ppp")) role = "ppp";
      var isAdj = role === "adj";
      var agreesWith = isAdj ? (info.match(/agrees?\s+with\s+(\w+)/i) || [])[1] : null;
      var isSg = lo.includes("singular");
      var isPl = lo.includes("plural");
      var plainLatin = latin.trim().replace(/\{[A-Z]:[^}]+\}/g, '');
      var endsM = plainLatin.endsWith("m");
      var endsA = plainLatin.endsWith("a");
      var isNeuter = lo.includes("neuter");
      // Auto-mnemonic fallback for old explanations without explicit sub-rules
      var autoMnemonic = null;
      if (role === "acc" && isSg && endsM) autoMnemonic = "If it ends in *-m* it's happening to them!";else if ((role === "nom" || role === "acc") && isPl && isNeuter && endsA) autoMnemonic = "Please remember every day, neuter plurals end in *-a*!";
      var b = {
        latin: latin.trim(),
        gloss: gloss,
        info: info,
        role: role,
        agreesWith: agreesWith,
        autoMnemonic: autoMnemonic,
        isAdj: isAdj,
        subrules: []
      };
      bullets.push(b);
      lastBullet = b;
    }

    // Group adjectives onto their noun
  } catch (err) {
    _iterator.e(err);
  } finally {
    _iterator.f();
  }
  var byLatin = {};
  bullets.forEach(function (b) {
    if (!b.isAdj) byLatin[b.latin] = b;
  });
  var merged = [];
  bullets.forEach(function (b) {
    if (b.isAdj && b.agreesWith && byLatin[b.agreesWith]) {
      var host = byLatin[b.agreesWith];
      host.adjs = host.adjs || [];
      host.adjs.push(b);
    } else if (!b.isAdj) {
      merged.push(b);
    } else {
      merged.push(b);
    }
  });

  // Preserve data order — explanations are written in English-clarity order already

  var renderCaseLine = function renderCaseLine(b) {
    var cn = b.role === "nom" ? "nominative" : b.role === "acc" ? "accusative" : b.role === "dat" ? "dative" : b.role === "abl" ? "ablative" : b.role === "gen" ? "genitive" : null;
    if (!cn) return renderText(b.info);
    var num = b.info.toLowerCase().includes("singular") ? " singular" : b.info.toLowerCase().includes("plural") ? " plural" : "";
    var t = b.role === "nom" ? "{T:".concat(cn, "}").concat(num, " \u2014 the {N:subject} (does the verb)") : b.role === "acc" ? "{T:".concat(cn, "}").concat(num, " \u2014 the {N:object} (receives the verb)") : b.role === "dat" ? "{T:".concat(cn, "}").concat(num, " \u2014 to / for") : b.role === "abl" ? "{T:".concat(cn, "}").concat(num, " \u2014 by / with / from") : "{T:".concat(cn, "}").concat(num, " \u2014 of");
    return renderText(t);
  };

  // Render a Latin form that may contain inline colour tags, keeping Latin font
  var renderLatinForm = function renderLatinForm(form) {
    return form.split(/(\{[RBPMTN]:[^}]+\})/g).map(function (part, i) {
      var tag = part.match(/^\{([RBPMTN]):(.+)\}$/);
      if (tag) return /*#__PURE__*/React.createElement("strong", {
        key: i,
        style: {
          color: TAG_COLORS[tag[1]],
          fontWeight: 900,
          fontStyle: 'italic',
          fontFamily: "'Crimson Text',Georgia,serif"
        }
      }, tag[2]);
      return part ? /*#__PURE__*/React.createElement("span", {
        key: i,
        className: "latin"
      }, part) : null;
    });
  };
  var srStyle = {
    marginLeft: 28,
    marginTop: 3,
    display: 'flex',
    gap: 5,
    alignItems: 'baseline',
    lineHeight: 1.55
  };
  var arrowCol = {
    color: '#7C3AED',
    fontWeight: 700,
    flexShrink: 0,
    fontSize: '0.87em',
    opacity: 0.85
  };
  return /*#__PURE__*/React.createElement("div", {
    style: {
      lineHeight: 1.85
    }
  }, merged.map(function (b, i) {
    var adjForms = (b.adjs || []).map(function (a) {
      return a.latin;
    }).join(" ");
    var adjGlosses = (b.adjs || []).map(function (a) {
      return a.gloss;
    }).join(", ");
    var allSubs = [].concat(_toConsumableArray(b.subrules || []), _toConsumableArray((b.adjs || []).flatMap(function (a) {
      return a.subrules || [];
    })), [b.autoMnemonic && !(b.subrules || []).length ? b.autoMnemonic : null]).filter(Boolean);
    return /*#__PURE__*/React.createElement("div", {
      key: i,
      style: {
        marginBottom: 14
      }
    }, /*#__PURE__*/React.createElement("div", {
      style: {
        display: 'flex',
        gap: 7,
        alignItems: 'baseline'
      }
    }, /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--navy)',
        fontWeight: 800,
        minWidth: 20,
        flexShrink: 0
      }
    }, i + 1, "."), /*#__PURE__*/React.createElement("div", null, adjForms && /*#__PURE__*/React.createElement(React.Fragment, null, renderLatinForm(adjForms), /*#__PURE__*/React.createElement("span", {
      className: "latin"
    }, " ")), renderLatinForm(b.latin), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--dark)',
        fontWeight: 500
      }
    }, " (", adjGlosses ? adjGlosses + (b.gloss ? " " : "") : "", b.gloss, ")"), b.info && /*#__PURE__*/React.createElement("span", {
      style: {
        fontSize: '0.87em',
        color: '#6B7280'
      }
    }, " \u2014 ", renderText(b.info)))), allSubs.map(function (rule, j) {
      return /*#__PURE__*/React.createElement("div", {
        key: j,
        style: srStyle
      }, /*#__PURE__*/React.createElement("span", {
        style: arrowCol
      }, "\u2192"), /*#__PURE__*/React.createElement("span", {
        style: {
          fontSize: '0.87em',
          color: '#6B7280'
        }
      }, renderText(rule)));
    }));
  }), orphans.length > 0 && /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 10,
      fontSize: '0.95em',
      color: 'var(--grey)'
    }
  }, orphans.map(function (o, i) {
    return /*#__PURE__*/React.createElement("div", {
      key: i
    }, renderText(o));
  })));
};
var grade = function grade(s) {
  return s === 100 ? 'TRAILBLAZER!' : s >= 95 ? 'PHENOMENAL!' : s >= 90 ? 'SUPERB!' : s >= 85 ? 'GREAT!' : s >= 80 ? 'PASSED!' : 'KEEP PRACTISING!';
};
var TIMEOUT_BADGES = ["Time's up!", "Too slow!", "You only have 10 seconds!", "Keep an eye on the clock!"];
var timeoutBadge = function timeoutBadge() {
  return TIMEOUT_BADGES[Math.floor(Math.random() * TIMEOUT_BADGES.length)];
};
var tagColor = function tagColor(t) {
  return {
    intro: '#4A90D9',
    vocab: '#F5A623',
    building_parts: '#002147',
    tense_id: '#7C3AED',
    translate_form: '#4A90D9',
    parsing: '#002147',
    parsing_mcq: '#B91C1C',
    sentences: '#EA580C',
    reference: '#7C3AED',
    concept: '#7C3AED',
    verbs: '#F5A623',
    review: '#EA580C'
  }[t] || '#7B8794';
};
var tagColorWithBadge = function tagColorWithBadge(t, badge) {
  if (badge === 'Principal Part') return '#002147';
  if (badge === 'test') return '#111827';
  return tagColor(t);
};
var tagLabel = function tagLabel(t) {
  if (t === 'building_parts') return 'principal parts';
  if (t === 'translate_form') return 'tense endings';
  if (t === 'reference' || t === 'concept') return 'grammar';
  if (t === 'vocab' || t === 'verbs') return 'vocabulary';
  if (t === 'tense_id') return 'grammar';
  if (t === 'parsing_mcq') return 'translation';
  if (t === 'sentences' || t === 'review') return 'sentences';
  return t.replace('_', ' ');
};
var tagLabelWithBadge = function tagLabelWithBadge(t, badge) {
  if (badge === 'Principal Part') return 'principal part';
  if (badge === 'test') return 'assessment';
  return tagLabel(t);
};

// ── App ──────────────────────────────────────────────────────────────────────

function FeedbackWidget(_ref6) {
  var pupilId = _ref6.pupilId,
    setId = _ref6.setId;
  var _useState3 = useState(false),
    _useState4 = _slicedToArray(_useState3, 2),
    open = _useState4[0],
    setOpen = _useState4[1];
  var _useState5 = useState(''),
    _useState6 = _slicedToArray(_useState5, 2),
    note = _useState6[0],
    setNote = _useState6[1];
  var _useState7 = useState(false),
    _useState8 = _slicedToArray(_useState7, 2),
    sent = _useState8[0],
    setSent = _useState8[1];
  var _useState9 = useState(false),
    _useState0 = _slicedToArray(_useState9, 2),
    busy = _useState0[0],
    setBusy = _useState0[1];
  var taRef = useRef();
  useEffect(function () {
    if (open && taRef.current) taRef.current.focus();
  }, [open]);
  var submit = /*#__PURE__*/function () {
    var _ref7 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee() {
      return _regenerator().w(function (_context) {
        while (1) switch (_context.n) {
          case 0:
            if (!(!note.trim() || busy)) {
              _context.n = 1;
              break;
            }
            return _context.a(2);
          case 1:
            setBusy(true);
            _context.n = 2;
            return post('/api/feedback', {
              pupil_id: pupilId || 0,
              set_id: setId || 0,
              note: note,
              url: window.location.href
            });
          case 2:
            setSent(true);
            setBusy(false);
            setTimeout(function () {
              setOpen(false);
              setNote('');
              setSent(false);
            }, 1400);
          case 3:
            return _context.a(2);
        }
      }, _callee);
    }));
    return function submit() {
      return _ref7.apply(this, arguments);
    };
  }();
  return /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'fixed',
      bottom: 24,
      right: 24,
      zIndex: 9999,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'flex-end',
      gap: 8
    }
  }, open && /*#__PURE__*/React.createElement("div", {
    style: {
      background: 'white',
      border: '2px solid var(--lgrey)',
      borderRadius: 16,
      padding: 18,
      boxShadow: '0 8px 32px rgba(0,0,0,0.15)',
      width: 280
    }
  }, sent ? /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 700,
      color: 'var(--navy)',
      textAlign: 'center',
      margin: 0
    }
  }, "Thanks! Note saved.") : /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 700,
      color: 'var(--navy)',
      marginBottom: 8,
      fontSize: '0.9rem'
    }
  }, "Message Mr Hunt"), /*#__PURE__*/React.createElement("textarea", {
    ref: taRef,
    value: note,
    onChange: function onChange(e) {
      return setNote(e.target.value);
    },
    rows: 4,
    style: {
      width: '100%',
      borderRadius: 8,
      border: '2px solid var(--lgrey)',
      padding: '8px 10px',
      fontSize: '0.9rem',
      resize: 'vertical',
      boxSizing: 'border-box',
      minHeight: 90
    },
    placeholder: "Let Mr Hunt know about anything \u2014 a bug, question, or comment about a set\u2026"
  }), /*#__PURE__*/React.createElement("button", {
    onClick: submit,
    disabled: busy || !note.trim(),
    style: {
      marginTop: 8,
      width: '100%',
      background: 'var(--navy)',
      color: 'white',
      border: 'none',
      borderRadius: 8,
      padding: '8px',
      fontWeight: 700,
      cursor: 'pointer',
      fontSize: '0.9rem'
    }
  }, "Send"))), /*#__PURE__*/React.createElement("button", {
    onClick: function onClick() {
      setOpen(function (o) {
        return !o;
      });
      setSent(false);
    },
    style: {
      width: 44,
      height: 44,
      borderRadius: 50,
      background: 'var(--navy)',
      color: 'white',
      border: 'none',
      fontSize: '1.3rem',
      cursor: 'pointer',
      boxShadow: '0 4px 12px rgba(0,0,0,0.2)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    },
    title: "Leave a note"
  }, "\u270E"));
}
function App() {
  var _useState1 = useState('teacher_dash'),
    _useState10 = _slicedToArray(_useState1, 2),
    screen = _useState10[0],
    setScreen = _useState10[1];
  var _useState11 = useState({
      id: 0,
      first_name: 'Preview'
    }),
    _useState12 = _slicedToArray(_useState11, 2),
    pupil = _useState12[0],
    setPupil = _useState12[1];
  var _useState13 = useState(null),
    _useState14 = _slicedToArray(_useState13, 2),
    currentSet = _useState14[0],
    setCurrentSet = _useState14[1];
  var _useState15 = useState(null),
    _useState16 = _slicedToArray(_useState15, 2),
    sessionId = _useState16[0],
    setSessionId = _useState16[1];
  var _useState17 = useState(true),
    _useState18 = _slicedToArray(_useState17, 2),
    isPreview = _useState18[0],
    setIsPreview = _useState18[1];
  var login = function login(p) {
    setPupil(p);
    setIsPreview(false);
    setScreen('dashboard');
  };
  var startPreview = function startPreview() {
    setPupil({
      id: 0,
      first_name: 'Teacher Mode'
    });
    setIsPreview(true);
    setScreen('teacher_dash');
  };
  var setStartRef = useRef(0);
  var startSet = /*#__PURE__*/function () {
    var _ref8 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee2(s) {
      var r;
      return _regenerator().w(function (_context2) {
        while (1) switch (_context2.n) {
          case 0:
            setStartRef.current = Date.now();
            setCurrentSet(s);
            if (isPreview) {
              _context2.n = 2;
              break;
            }
            _context2.n = 1;
            return post('/api/session/start', {
              pupil_id: pupil.id,
              set_id: s.id
            });
          case 1:
            r = _context2.v;
            setSessionId(r.session_id);
          case 2:
            setScreen('front');
          case 3:
            return _context2.a(2);
        }
      }, _callee2);
    }));
    return function startSet(_x) {
      return _ref8.apply(this, arguments);
    };
  }();
  var _useState19 = useState(0),
    _useState20 = _slicedToArray(_useState19, 2),
    dashKey = _useState20[0],
    setDashKey = _useState20[1];
  var saveProgress = /*#__PURE__*/function () {
    var _ref9 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee3(score, timeSecs) {
      var t;
      return _regenerator().w(function (_context3) {
        while (1) switch (_context3.n) {
          case 0:
            if (isPreview) {
              _context3.n = 2;
              break;
            }
            if (!sessionId) {
              _context3.n = 1;
              break;
            }
            _context3.n = 1;
            return post("/api/session/end?session_id=".concat(sessionId), {});
          case 1:
            t = timeSecs !== undefined ? timeSecs : Math.round((Date.now() - setStartRef.current) / 1000);
            _context3.n = 2;
            return post('/api/complete', {
              pupil_id: pupil.id,
              set_id: currentSet.id,
              score: score,
              time_seconds: t
            });
          case 2:
            return _context3.a(2);
        }
      }, _callee3);
    }));
    return function saveProgress(_x2, _x3) {
      return _ref9.apply(this, arguments);
    };
  }();
  var finishSet = /*#__PURE__*/function () {
    var _ref0 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee4(score) {
      return _regenerator().w(function (_context4) {
        while (1) switch (_context4.n) {
          case 0:
            _context4.n = 1;
            return saveProgress(score);
          case 1:
            setDashKey(function (k) {
              return k + 1;
            });
            setScreen(isPreview ? 'teacher_dash' : 'dashboard');
          case 2:
            return _context4.a(2);
        }
      }, _callee4);
    }));
    return function finishSet(_x4) {
      return _ref0.apply(this, arguments);
    };
  }();
  var saveAndNext = /*#__PURE__*/function () {
    var _ref1 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee5(score, targetSet) {
      var full;
      return _regenerator().w(function (_context5) {
        while (1) switch (_context5.n) {
          case 0:
            _context5.n = 1;
            return saveProgress(score);
          case 1:
            _context5.n = 2;
            return api("/api/sets/".concat(targetSet.id));
          case 2:
            full = _context5.v;
            startSet(full);
          case 3:
            return _context5.a(2);
        }
      }, _callee5);
    }));
    return function saveAndNext(_x5, _x6) {
      return _ref1.apply(this, arguments);
    };
  }();
  var backToDash = function backToDash() {
    setDashKey(function (k) {
      return k + 1;
    });
    setScreen(isPreview ? 'teacher_dash' : 'dashboard');
  };
  var fw = /*#__PURE__*/React.createElement(FeedbackWidget, {
    pupilId: (pupil === null || pupil === void 0 ? void 0 : pupil.id) || 0,
    setId: (currentSet === null || currentSet === void 0 ? void 0 : currentSet.id) || 0
  });
  if (screen === 'login') return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(Login, {
    onLogin: login,
    onPreview: startPreview
  }), fw);
  if (screen === 'dashboard') return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(Dashboard, {
    key: dashKey,
    pupil: pupil,
    onLogout: function onLogout() {
      return setScreen('login');
    },
    onStart: startSet
  }), fw);
  if (screen === 'teacher_dash') return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(TeacherDashboard, {
    onLogout: function onLogout() {
      return setScreen('login');
    },
    onStart: startSet
  }), fw);
  if (screen === 'front') {
    var isRefOverlay = currentSet.type === 'reference' || currentSet.type === 'concept';
    var frontOverlay = /*#__PURE__*/React.createElement(Front, {
      set: currentSet,
      onGo: function onGo() {
        setScreen('play');
      },
      onBack: backToDash,
      onComplete: function onComplete() {
        return finishSet(100);
      }
    });
    if (isRefOverlay) {
      if (isPreview) return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(TeacherDashboard, {
        onLogout: function onLogout() {
          return setScreen('login');
        },
        onStart: startSet
      }, frontOverlay), fw);
      return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(Dashboard, {
        key: dashKey,
        pupil: pupil,
        onLogout: function onLogout() {
          return setScreen('login');
        },
        onStart: startSet
      }, frontOverlay), fw);
    }
    return /*#__PURE__*/React.createElement(React.Fragment, null, frontOverlay, fw);
  }
  if (screen === 'play') return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement(Play, {
    pupil: pupil,
    set: currentSet,
    isPreview: isPreview,
    onFinish: finishSet,
    onSaveAndNext: saveAndNext,
    onBack: backToDash
  }), fw);
  return null;
}
function Login(_ref10) {
  var onLogin = _ref10.onLogin,
    onPreview = _ref10.onPreview;
  var _useState21 = useState('10'),
    _useState22 = _slicedToArray(_useState21, 2),
    year = _useState22[0],
    setYear = _useState22[1];
  var _useState23 = useState([]),
    _useState24 = _slicedToArray(_useState23, 2),
    pupils = _useState24[0],
    setPupils = _useState24[1];
  var _useState25 = useState(false),
    _useState26 = _slicedToArray(_useState25, 2),
    showT = _useState26[0],
    setShowT = _useState26[1];
  var _useState27 = useState(''),
    _useState28 = _slicedToArray(_useState27, 2),
    pwd = _useState28[0],
    setPwd = _useState28[1];
  useEffect(function () {
    if (year) api("/api/pupils?year=".concat(year)).then(setPupils);
  }, [year]);
  useEffect(function () {
    var _document$querySelect2;
    (_document$querySelect2 = document.querySelector('.login-body')) === null || _document$querySelect2 === void 0 || _document$querySelect2.scrollTo({
      top: 0,
      behavior: 'instant'
    });
  }, [year]);
  var doT = function doT() {
    if (pwd === 'latinmagistra') onPreview();else alert('Wrong password');
  };
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen login-page"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "login-body anim-fade"
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: '3.5rem',
      marginBottom: 20,
      color: 'var(--navy)'
    }
  }, "Select your name"), /*#__PURE__*/React.createElement("div", {
    className: "pupil-grid"
  }, pupils.map(function (p) {
    return /*#__PURE__*/React.createElement("button", {
      key: p.id,
      className: "pupil-btn",
      onClick: function onClick() {
        return onLogin(p);
      }
    }, p.first_name);
  }))), /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'fixed',
      bottom: 30,
      right: 40,
      fontSize: '1.2rem',
      color: 'var(--grey)',
      cursor: 'pointer',
      fontWeight: 800
    },
    onClick: function onClick() {
      return setShowT(!showT);
    }
  }, "Teacher Mode"), showT && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      position: 'fixed',
      bottom: 80,
      right: 40,
      background: 'var(--white)',
      padding: 30,
      borderRadius: 20,
      boxShadow: '0 12px 40px rgba(0,0,0,.15)'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      marginBottom: 16,
      fontWeight: 800,
      fontSize: '1.2rem',
      color: 'var(--navy)'
    }
  }, "Enter Teacher Password:"), /*#__PURE__*/React.createElement("input", {
    type: "password",
    value: pwd,
    onChange: function onChange(e) {
      return setPwd(e.target.value);
    },
    onKeyDown: function onKeyDown(e) {
      return e.key === 'Enter' && doT();
    },
    autoFocus: true,
    style: {
      padding: 16,
      border: '3px solid var(--lgrey)',
      borderRadius: 12,
      fontSize: '1.2rem',
      marginRight: 12
    }
  }), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    onClick: doT
  }, "Enter")));
}

// ── Leaderboard row — shared by Dashboard modal, Play modal, Teacher tab ──────
var LB_GRAD = {
  1: 'linear-gradient(130deg,#FFFDE7 0%,#FFF8C4 48%,#FFFDE7 100%)',
  2: 'linear-gradient(130deg,#F8FAFA 0%,#E6E6E6 48%,#F8FAFA 100%)',
  3: 'linear-gradient(130deg,#FFF4E6 0%,#FFE0AD 48%,#FFF4E6 100%)'
};
var LB_SHADOW = {
  1: '0 3px 14px rgba(245,166,35,.22)',
  2: '0 3px 14px rgba(140,140,140,.18)',
  3: '0 3px 14px rgba(205,127,50,.22)'
};
var LB_DOT = {
  1: '#F5A623',
  2: '#9CA3AF',
  3: '#CD7F32'
};
function LBRow(_ref11) {
  var p = _ref11.p,
    isMe = _ref11.isMe,
    onClick = _ref11.onClick,
    extra = _ref11.extra;
  var t3 = p.rank <= 3,
    t10 = p.rank <= 10;
  var rs = isMe ? {
    background: '#EEF6FC',
    border: '2px solid var(--blue)',
    borderRadius: 12,
    marginBottom: 5,
    padding: '12px 16px',
    boxShadow: '0 2px 8px rgba(74,144,217,.14)'
  } : t3 ? {
    background: LB_GRAD[p.rank],
    borderRadius: 13,
    marginBottom: 7,
    padding: '15px 18px',
    boxShadow: LB_SHADOW[p.rank]
  } : t10 ? {
    background: '#F3F7FF',
    borderRadius: 9,
    marginBottom: 3,
    padding: '11px 14px'
  } : {
    borderBottom: '1px solid #EFEFEF',
    padding: '9px 14px'
  };
  return /*#__PURE__*/React.createElement(React.Fragment, null, p.rank === 11 && /*#__PURE__*/React.createElement("div", {
    style: {
      height: 1,
      background: 'var(--lgrey)',
      margin: '8px 0',
      opacity: .35
    }
  }), /*#__PURE__*/React.createElement("div", {
    onClick: onClick,
    style: _objectSpread(_objectSpread({
      display: 'flex',
      alignItems: 'center',
      gap: 14
    }, rs), {}, {
      cursor: onClick ? 'pointer' : 'default'
    })
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      width: t3 ? 40 : 28,
      height: t3 ? 40 : 28,
      minWidth: t3 ? 40 : 28,
      borderRadius: '50%',
      background: isMe ? 'var(--blue)' : t3 ? LB_DOT[p.rank] : t10 ? '#D8E4F5' : 'var(--lgrey)',
      color: t3 || isMe ? '#fff' : t10 ? 'var(--navy)' : 'var(--grey)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontWeight: 900,
      fontSize: t3 ? '1.05rem' : '0.8rem',
      flexShrink: 0,
      boxShadow: t3 ? LB_SHADOW[p.rank] : undefined
    }
  }, p.rank), /*#__PURE__*/React.createElement("span", {
    style: {
      flex: 1,
      fontWeight: t3 || isMe ? 800 : t10 ? 600 : 400,
      fontSize: t3 ? '1.12rem' : t10 || isMe ? '1rem' : '0.95rem',
      color: onClick ? 'var(--blue)' : 'var(--navy)'
    }
  }, p.name, isMe ? ' (you)' : ''), /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 800,
      color: 'var(--navy)',
      fontSize: t3 ? '1.15rem' : '1rem'
    }
  }, p.xp, /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 400,
      fontSize: '0.78em',
      color: 'var(--grey)',
      marginLeft: 3
    }
  }, "XP")), extra));
}
function Dashboard(_ref12) {
  var pupil = _ref12.pupil,
    onLogout = _ref12.onLogout,
    onStart = _ref12.onStart,
    children = _ref12.children;
  var _useState29 = useState([]),
    _useState30 = _slicedToArray(_useState29, 2),
    sets = _useState30[0],
    setSets = _useState30[1];
  var _useState31 = useState([]),
    _useState32 = _slicedToArray(_useState31, 2),
    progress = _useState32[0],
    setProgress = _useState32[1];
  var firstRef = useRef(null);
  var _useState33 = useState(false),
    _useState34 = _slicedToArray(_useState33, 2),
    showLB = _useState34[0],
    setShowLB = _useState34[1];
  var _useState35 = useState([]),
    _useState36 = _slicedToArray(_useState35, 2),
    lbData = _useState36[0],
    setLbData = _useState36[1];
  var openLB = function openLB() {
    api('/api/leaderboard').then(setLbData);
    setShowLB(true);
  };
  useEffect(function () {
    var h = function h(e) {
      if (e.key === 'Escape') setShowLB(false);
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  }, [showLB]);
  useEffect(function () {
    api('/api/sets').then(function (s) {
      setSets(s);
      api("/api/pupil/".concat(pupil.id, "/progress")).then(setProgress);
    });
  }, [pupil.id]);
  useEffect(function () {
    if (sets.length > 0 && progress.length >= 0 && !children) {
      var t = setTimeout(function () {
        if (firstRef.current) {
          var body = document.querySelector('.dash-body');
          var el = firstRef.current;
          if (body) {
            var elTop = el.getBoundingClientRect().top - body.getBoundingClientRect().top + body.scrollTop - 120;
            body.scrollTo({
              top: Math.max(0, elTop),
              behavior: 'smooth'
            });
          } else {
            el.scrollIntoView({
              behavior: 'smooth',
              block: 'start'
            });
          }
        }
      }, 600);
      return function () {
        return clearTimeout(t);
      };
    }
  }, [sets.length, progress, children]);
  var pm = {};
  progress.forEach(function (p) {
    return pm[p.set_id] = p;
  });
  // Group by node number (not string title) to avoid any label mismatch creating duplicate sections
  var nodeMap = {};
  var nodeOrder = [];
  sets.forEach(function (s) {
    if (!(s.node in nodeMap)) {
      nodeMap[s.node] = {
        label: s.node_title,
        sets: []
      };
      nodeOrder.push(s.node);
    }
    nodeMap[s.node].sets.push(s);
  });
  var nodes = nodeOrder.map(function (n) {
    return nodeMap[n];
  });
  var foundFirst = false;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 16,
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: '1.2rem',
      fontWeight: 700
    }
  }, pupil.first_name), /*#__PURE__*/React.createElement("button", {
    onClick: openLB,
    style: {
      background: 'rgba(255,255,255,.2)',
      color: '#fff',
      padding: '10px 20px',
      fontSize: '1rem',
      border: 'none',
      borderRadius: 10,
      fontWeight: 700,
      cursor: 'pointer'
    }
  }, "Leaderboard"), /*#__PURE__*/React.createElement("a", {
    href: "index.html",
    style: {
      fontSize: "0.78rem",
      letterSpacing: ".14em",
      textTransform: "uppercase",
      fontWeight: 700,
      color: "#fff",
      textDecoration: "none",
      padding: "8px 16px",
      border: "1.5px solid rgba(255,255,255,.45)",
      borderRadius: "8px",
      background: "rgba(255,255,255,.1)"
    }
  }, "Home"))), /*#__PURE__*/React.createElement("div", {
    className: "dash-body anim-fade"
  }, nodes.map(function (node) {
    return /*#__PURE__*/React.createElement("div", {
      key: node.label
    }, /*#__PURE__*/React.createElement("div", {
      className: "section-label"
    }, node.label), /*#__PURE__*/React.createElement("div", {
      className: "set-grid"
    }, node.sets.map(function (s) {
      var p = pm[s.id] || {
        status: 'locked'
      };
      var effectiveStatus = p.status;
      var isFirst = !foundFirst && (p.status === 'available' || p.status === 'in_progress');
      if (isFirst) foundFirst = true;
      return /*#__PURE__*/React.createElement("div", {
        key: s.id,
        ref: isFirst ? firstRef : null,
        className: "set-card ".concat(effectiveStatus).concat(s.optional ? ' optional-card' : ''),
        onClick: function onClick() {
          if (effectiveStatus !== 'locked') api("/api/sets/".concat(s.id)).then(onStart);
        }
      }, /*#__PURE__*/React.createElement("div", {
        className: "tag-badge",
        style: {
          background: tagColorWithBadge(s.type, s.badge)
        }
      }, tagLabelWithBadge(s.type, s.badge)), /*#__PURE__*/React.createElement("h3", {
        dangerouslySetInnerHTML: {
          __html: renderOrdinals(s.title)
        }
      }), p.status === 'passed' && /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--green-bright)',
          position: 'absolute',
          bottom: 24,
          right: 24,
          fontSize: '1.1rem',
          fontWeight: 900
        }
      }, Math.round(p.best_score), "%"));
    })));
  })), showLB && /*#__PURE__*/React.createElement("div", {
    className: "modal-overlay",
    onClick: function onClick(e) {
      return e.target === e.currentTarget && setShowLB(false);
    },
    style: {
      zIndex: 200
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "modal-content",
    style: {
      maxWidth: 600,
      padding: '40px 40px 32px'
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: '2rem',
      color: 'var(--navy)',
      marginBottom: 4
    }
  }, "Leaderboard"), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 24,
      fontSize: '0.9rem'
    }
  }, "XP = sum of best scores across all completed sets."), /*#__PURE__*/React.createElement("div", {
    style: {
      maxHeight: '60vh',
      overflowY: 'auto',
      paddingRight: 2
    }
  }, lbData.map(function (p) {
    return /*#__PURE__*/React.createElement(LBRow, {
      key: p.pupil_id,
      p: p,
      isMe: pupil && p.pupil_id === pupil.id
    });
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 24,
      textAlign: 'center'
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    onClick: function onClick() {
      return setShowLB(false);
    }
  }, "Close", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Esc"))))), children);
}
function TeacherDashboard(_ref13) {
  var onLogout = _ref13.onLogout,
    onStart = _ref13.onStart,
    children = _ref13.children;
  var _useState37 = useState('preview'),
    _useState38 = _slicedToArray(_useState37, 2),
    tab = _useState38[0],
    setTab = _useState38[1];
  var _useState39 = useState([]),
    _useState40 = _slicedToArray(_useState39, 2),
    sets = _useState40[0],
    setSets = _useState40[1];
  var _useState41 = useState([]),
    _useState42 = _slicedToArray(_useState41, 2),
    overview = _useState42[0],
    setOverview = _useState42[1];
  var _useState43 = useState([]),
    _useState44 = _slicedToArray(_useState43, 2),
    weak = _useState44[0],
    setWeak = _useState44[1];
  var _useState45 = useState([]),
    _useState46 = _slicedToArray(_useState45, 2),
    misc = _useState46[0],
    setMisc = _useState46[1];
  var _useState47 = useState(null),
    _useState48 = _slicedToArray(_useState47, 2),
    selPupil = _useState48[0],
    setSelPupil = _useState48[1];
  var _useState49 = useState([]),
    _useState50 = _slicedToArray(_useState49, 2),
    detail = _useState50[0],
    setDetail = _useState50[1];
  var _useState51 = useState(null),
    _useState52 = _slicedToArray(_useState51, 2),
    homework = _useState52[0],
    setHomework = _useState52[1];
  var _useState53 = useState(null),
    _useState54 = _slicedToArray(_useState53, 2),
    hwProgress = _useState54[0],
    setHwProgress = _useState54[1];
  var _useState55 = useState([]),
    _useState56 = _slicedToArray(_useState55, 2),
    feedbackMsgs = _useState56[0],
    setFeedbackMsgs = _useState56[1];
  var _useState57 = useState([]),
    _useState58 = _slicedToArray(_useState57, 2),
    leaderboard = _useState58[0],
    setLeaderboard = _useState58[1];
  var _useState59 = useState(null),
    _useState60 = _slicedToArray(_useState59, 2),
    viewNode = _useState60[0],
    setViewNode = _useState60[1];
  var _useState61 = useState([]),
    _useState62 = _slicedToArray(_useState61, 2),
    timing = _useState62[0],
    setTiming = _useState62[1];
  var _useState63 = useState(false),
    _useState64 = _slicedToArray(_useState63, 2),
    timingFlagged = _useState64[0],
    setTimingFlagged = _useState64[1];
  var _useState65 = useState('newest'),
    _useState66 = _slicedToArray(_useState65, 2),
    feedbackSort = _useState66[0],
    setFeedbackSort = _useState66[1];
  var _useState67 = useState(''),
    _useState68 = _slicedToArray(_useState67, 2),
    newName = _useState68[0],
    setNewName = _useState68[1];
  var _useState69 = useState(false),
    _useState70 = _slicedToArray(_useState69, 2),
    adding = _useState70[0],
    setAdding = _useState70[1];
  var doAddPupil = /*#__PURE__*/function () {
    var _ref14 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee6() {
      var n, p, _t;
      return _regenerator().w(function (_context6) {
        while (1) switch (_context6.p = _context6.n) {
          case 0:
            n = newName.trim();
            if (n) {
              _context6.n = 1;
              break;
            }
            return _context6.a(2);
          case 1:
            setAdding(true);
            _context6.p = 2;
            _context6.n = 3;
            return api('/api/teacher/add-pupil', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                name: n
              })
            });
          case 3:
            p = _context6.v;
            setLeaderboard(function (lb) {
              return [].concat(_toConsumableArray(lb), [_objectSpread(_objectSpread({}, p), {}, {
                xp: 0,
                rank: lb.length + 1
              })]);
            });
            setNewName('');
            _context6.n = 5;
            break;
          case 4:
            _context6.p = 4;
            _t = _context6.v;
            alert(_t.message || 'Could not add pupil');
          case 5:
            _context6.p = 5;
            setAdding(false);
            return _context6.f(5);
          case 6:
            return _context6.a(2);
        }
      }, _callee6, null, [[2, 4, 5, 6]]);
    }));
    return function doAddPupil() {
      return _ref14.apply(this, arguments);
    };
  }();
  var loadData = function loadData() {
    api('/api/sets').then(setSets);
    api('/api/teacher/overview').then(setOverview);
    api('/api/teacher/weak-verbs').then(setWeak);
    api('/api/teacher/misconceptions').then(setMisc);
    api('/api/teacher/homework').then(setHomework);
    api('/api/teacher/homework-progress').then(setHwProgress);
    api('/api/teacher/feedback').then(setFeedbackMsgs);
    api('/api/leaderboard').then(setLeaderboard);
    api('/api/teacher/timing').then(setTiming);
  };
  useEffect(function () {
    loadData();
  }, []);
  var setHomeworkTarget = function setHomeworkTarget(type, value) {
    api('/api/teacher/homework', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        target_type: type,
        target_value: value
      })
    }).then(function () {
      api('/api/teacher/homework').then(setHomework);
      api('/api/teacher/homework-progress').then(setHwProgress);
    });
  };
  var viewNodeProgress = /*#__PURE__*/function () {
    var _ref15 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee7(nodeNum) {
      var data;
      return _regenerator().w(function (_context7) {
        while (1) switch (_context7.n) {
          case 0:
            setViewNode(nodeNum);
            _context7.n = 1;
            return api("/api/teacher/homework-progress?node=".concat(nodeNum));
          case 1:
            data = _context7.v;
            setHwProgress(data);
          case 2:
            return _context7.a(2);
        }
      }, _callee7);
    }));
    return function viewNodeProgress(_x7) {
      return _ref15.apply(this, arguments);
    };
  }();
  var markRead = function markRead(id) {
    api("/api/teacher/feedback/".concat(id, "/read"), {
      method: 'POST'
    }).then(function () {
      return setFeedbackMsgs(function (m) {
        return m.map(function (x) {
          return x.id === id ? _objectSpread(_objectSpread({}, x), {}, {
            read: true
          }) : x;
        });
      });
    });
  };
  var loadPupil = /*#__PURE__*/function () {
    var _ref16 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee8(p) {
      var d;
      return _regenerator().w(function (_context8) {
        while (1) switch (_context8.n) {
          case 0:
            _context8.n = 1;
            return api("/api/teacher/pupil/".concat(p.pupil_id));
          case 1:
            d = _context8.v;
            setSelPupil(p);
            setDetail(d);
            setTab('pupil');
          case 2:
            return _context8.a(2);
        }
      }, _callee8);
    }));
    return function loadPupil(_x8) {
      return _ref16.apply(this, arguments);
    };
  }();
  var nodeMap2 = {};
  var nodeOrder2 = [];
  sets.forEach(function (s) {
    if (!(s.node in nodeMap2)) {
      nodeMap2[s.node] = {
        label: s.node_title,
        sets: []
      };
      nodeOrder2.push(s.node);
    }
    nodeMap2[s.node].sets.push(s);
  });
  var nodes = nodeOrder2.map(function (n) {
    return nodeMap2[n];
  });
  var unreadCount = feedbackMsgs.filter(function (m) {
    return !m.read;
  }).length;
  var tabs = [{
    key: 'preview',
    label: 'Curriculum'
  }];
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.3rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 24,
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("a", {
    href: "index.html",
    style: {
      fontSize: "0.78rem",
      letterSpacing: ".14em",
      textTransform: "uppercase",
      fontWeight: 700,
      color: "#fff",
      textDecoration: "none",
      padding: "8px 16px",
      border: "1.5px solid rgba(255,255,255,.45)",
      borderRadius: "8px",
      background: "rgba(255,255,255,.1)"
    }
  }, "Home"))), /*#__PURE__*/React.createElement("div", {
    className: "t-dash anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "t-content"
  }, tab === 'homework' && /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 960
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: '1.8rem',
      marginBottom: 8
    }
  }, "Progress Tracker"), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 20
    }
  }, "Click a node to view pupil progress. Use \"Set as Homework\" to assign a target."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 12,
      flexWrap: 'wrap',
      marginBottom: 20
    }
  }, nodes.filter(function (n) {
    return n.label !== 'Introduction';
  }).map(function (node) {
    var nodeNum = nodeOrder2[nodes.indexOf(node)];
    var isActive = viewNode === nodeNum;
    return /*#__PURE__*/React.createElement("button", {
      key: nodeNum,
      onClick: function onClick() {
        return viewNodeProgress(nodeNum);
      },
      style: {
        padding: '10px 18px',
        background: isActive ? 'var(--navy)' : '#fff',
        color: isActive ? '#fff' : 'var(--navy)',
        border: '2px solid ' + (isActive ? 'var(--navy)' : 'var(--lgrey)'),
        borderRadius: 10,
        fontWeight: 700,
        cursor: 'pointer',
        fontSize: '0.95rem'
      }
    }, node.label);
  })), viewNode !== null && /*#__PURE__*/React.createElement("button", {
    onClick: function onClick() {
      return setHomeworkTarget('node', viewNode);
    },
    style: {
      marginBottom: 24,
      padding: '9px 18px',
      background: (homework === null || homework === void 0 ? void 0 : homework.target_value) === viewNode ? 'var(--green-bright)' : 'var(--gold)',
      color: '#fff',
      border: 'none',
      borderRadius: 10,
      fontWeight: 700,
      cursor: 'pointer',
      fontSize: '0.9rem'
    }
  }, (homework === null || homework === void 0 ? void 0 : homework.target_value) === viewNode ? 'Set as homework (active)' : 'Set as homework for class'), hwProgress && viewNode !== null && /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 8,
      marginBottom: 16,
      flexWrap: 'wrap'
    }
  }, [{
    s: 'done',
    c: 'var(--green-bright)',
    l: 'Done'
  }, {
    s: 'partial',
    c: 'var(--gold)',
    l: 'Partial'
  }, {
    s: 'not_started',
    c: 'var(--red-bright)',
    l: 'Not started'
  }].map(function (_ref17) {
    var s = _ref17.s,
      c = _ref17.c,
      l = _ref17.l;
    var n = hwProgress.pupils.filter(function (p) {
      return p.status === s;
    }).length;
    return /*#__PURE__*/React.createElement("div", {
      key: s,
      style: {
        background: '#f8fafc',
        border: '2px solid var(--lgrey)',
        borderRadius: 10,
        padding: '8px 16px',
        fontWeight: 700,
        fontSize: '0.9rem',
        display: 'flex',
        gap: 8,
        alignItems: 'center'
      }
    }, /*#__PURE__*/React.createElement("span", {
      style: {
        width: 10,
        height: 10,
        borderRadius: '50%',
        background: c,
        display: 'inline-block'
      }
    }), l, ": ", n);
  })), /*#__PURE__*/React.createElement("table", {
    className: "t-table"
  }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Pupil"), /*#__PURE__*/React.createElement("th", null, "Status"), /*#__PURE__*/React.createElement("th", null, "Progress"))), /*#__PURE__*/React.createElement("tbody", null, hwProgress.pupils.sort(function (a, b) {
    var o = {
      done: 0,
      partial: 1,
      not_started: 2
    };
    return o[a.status] - o[b.status] || a.name.localeCompare(b.name);
  }).map(function (p, i) {
    var colour = p.status === 'done' ? 'var(--green-bright)' : p.status === 'partial' ? 'var(--gold)' : 'var(--red-bright)';
    var label = p.status === 'done' ? 'DONE' : p.status === 'partial' ? 'PARTIAL' : 'NOT STARTED';
    return /*#__PURE__*/React.createElement("tr", {
      key: i
    }, /*#__PURE__*/React.createElement("td", {
      style: {
        fontWeight: 700
      }
    }, p.name), /*#__PURE__*/React.createElement("td", null, /*#__PURE__*/React.createElement("span", {
      style: {
        background: p.status === 'done' ? '#d4f7e0' : p.status === 'partial' ? '#fef3c7' : '#ffeaec',
        color: colour,
        fontWeight: 800,
        fontSize: '0.8rem',
        padding: '4px 10px',
        borderRadius: 6,
        textTransform: 'uppercase'
      }
    }, label)), /*#__PURE__*/React.createElement("td", {
      style: {
        color: 'var(--grey)'
      }
    }, p.done, " / ", p.total, " sets"));
  })))), viewNode === null && /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      fontStyle: 'italic',
      marginTop: 8
    }
  }, "\u2190 Select a node above to view progress")), tab === 'leaderboard' && /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 800
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: '1.8rem',
      marginBottom: 6
    }
  }, "Leaderboard"), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 20,
      fontSize: '0.95rem'
    }
  }, "XP = sum of best scores across all passed sets. Click a pupil to view their set-by-set detail."), leaderboard.map(function (p) {
    var ov = overview.find(function (o) {
      return o.pupil_id === p.pupil_id || o.id === p.pupil_id;
    });
    return /*#__PURE__*/React.createElement(LBRow, {
      key: p.pupil_id,
      p: p,
      isMe: false,
      onClick: function onClick() {
        return loadPupil(_objectSpread(_objectSpread({}, p), {}, {
          first_name: p.name
        }));
      },
      extra: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--grey)',
          fontSize: '0.85rem',
          whiteSpace: 'nowrap'
        }
      }, p.sets_passed, " sets"), (ov === null || ov === void 0 ? void 0 : ov.last_active) && ov.last_active !== 'Never' && /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--lgrey)',
          fontSize: '0.8rem',
          minWidth: 72,
          textAlign: 'right',
          whiteSpace: 'nowrap'
        }
      }, ov.last_active))
    });
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 24,
      display: 'flex',
      gap: 12,
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("input", {
    value: newName,
    onChange: function onChange(e) {
      return setNewName(e.target.value);
    },
    onKeyDown: function onKeyDown(e) {
      return e.key === 'Enter' && doAddPupil();
    },
    placeholder: "Add pupil \u2014 e.g. Jana H",
    style: {
      padding: '12px 16px',
      border: '2px solid var(--lgrey)',
      borderRadius: 10,
      fontSize: '1rem',
      flex: 1,
      maxWidth: 300
    }
  }), /*#__PURE__*/React.createElement("button", {
    onClick: doAddPupil,
    disabled: adding || !newName.trim(),
    className: "btn btn-primary",
    style: {
      padding: '12px 24px',
      fontSize: '1rem',
      minWidth: 'auto'
    }
  }, adding ? 'Adding…' : 'Add Pupil'))), tab === 'weak' && /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 900
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: '1.8rem',
      marginBottom: 20
    }
  }, "Most Missed Forms"), /*#__PURE__*/React.createElement("table", {
    className: "t-table"
  }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Form asked"), /*#__PURE__*/React.createElement("th", null, "Attempts"), /*#__PURE__*/React.createElement("th", null, "Error rate"))), /*#__PURE__*/React.createElement("tbody", null, weak.slice(0, 20).map(function (r, i) {
    return /*#__PURE__*/React.createElement("tr", {
      key: i
    }, /*#__PURE__*/React.createElement("td", {
      className: "latin",
      style: {
        fontSize: '1.4rem'
      }
    }, r.form), /*#__PURE__*/React.createElement("td", null, r.attempts), /*#__PURE__*/React.createElement("td", null, /*#__PURE__*/React.createElement("strong", {
      style: {
        color: 'var(--red-bright)'
      }
    }, r.error_rate, "%")));
  })))), tab === 'feedback' && /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 800
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'center',
      gap: 16,
      marginBottom: 20,
      flexWrap: 'wrap'
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: '1.8rem',
      margin: 0
    }
  }, "Pupil Feedback"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 6,
      marginLeft: 'auto'
    }
  }, [['newest', 'Most recent'], ['oldest', 'Furthest ago'], ['set', 'By set']].map(function (_ref18) {
    var _ref19 = _slicedToArray(_ref18, 2),
      val = _ref19[0],
      lbl = _ref19[1];
    return /*#__PURE__*/React.createElement("button", {
      key: val,
      onClick: function onClick() {
        return setFeedbackSort(val);
      },
      style: {
        padding: '6px 14px',
        background: feedbackSort === val ? 'var(--navy)' : '#fff',
        color: feedbackSort === val ? '#fff' : 'var(--navy)',
        border: '2px solid ' + (feedbackSort === val ? 'var(--navy)' : 'var(--lgrey)'),
        borderRadius: 8,
        fontWeight: 700,
        cursor: 'pointer',
        fontSize: '0.85rem'
      }
    }, lbl);
  }))), feedbackMsgs.length === 0 && /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)'
    }
  }, "No feedback yet."), _toConsumableArray(feedbackMsgs).sort(function (a, b) {
    if (feedbackSort === 'oldest') return new Date(a.created_at) - new Date(b.created_at);
    if (feedbackSort === 'set') return (a.set_id || 0) - (b.set_id || 0) || new Date(b.created_at) - new Date(a.created_at);
    return new Date(b.created_at) - new Date(a.created_at); // newest
  }).map(function (m) {
    var _m$created_at;
    return /*#__PURE__*/React.createElement("div", {
      key: m.id,
      onClick: function onClick() {
        return !m.read && markRead(m.id);
      },
      style: {
        background: m.read ? '#f8fafc' : '#fff',
        border: '2px solid ' + (m.read ? 'var(--lgrey)' : 'var(--navy)'),
        borderRadius: 14,
        padding: '16px 20px',
        marginBottom: 12,
        cursor: m.read ? 'default' : 'pointer'
      }
    }, /*#__PURE__*/React.createElement("div", {
      style: {
        display: 'flex',
        gap: 12,
        alignItems: 'center',
        marginBottom: 6
      }
    }, /*#__PURE__*/React.createElement("span", {
      style: {
        fontWeight: 800,
        color: 'var(--navy)'
      }
    }, m.pupil_name || 'Anonymous'), m.set_title && /*#__PURE__*/React.createElement("span", {
      style: {
        background: 'var(--lgrey)',
        borderRadius: 6,
        padding: '2px 8px',
        fontSize: '0.8rem',
        fontWeight: 700,
        color: 'var(--grey)'
      }
    }, m.set_title), /*#__PURE__*/React.createElement("span", {
      style: {
        marginLeft: 'auto',
        fontSize: '0.8rem',
        color: 'var(--grey)'
      }
    }, (_m$created_at = m.created_at) === null || _m$created_at === void 0 ? void 0 : _m$created_at.substring(0, 16).replace('T', ' ')), !m.read && /*#__PURE__*/React.createElement("span", {
      style: {
        background: 'var(--navy)',
        color: '#fff',
        borderRadius: 6,
        padding: '2px 8px',
        fontSize: '0.75rem',
        fontWeight: 700
      }
    }, "NEW")), /*#__PURE__*/React.createElement("p", {
      style: {
        margin: 0,
        color: 'var(--dark)',
        fontSize: '1.05rem'
      }
    }, m.note));
  })), tab === 'timing' && /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 960
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: '1.8rem',
      marginBottom: 6
    }
  }, "Timing & Integrity"), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 16,
      fontSize: '0.95rem'
    }
  }, "Set completion times. ", /*#__PURE__*/React.createElement("span", {
    style: {
      color: 'var(--red-bright)',
      fontWeight: 700
    }
  }, "Red"), " = very fast (<30s with passing score), ", /*#__PURE__*/React.createElement("span", {
    style: {
      color: '#92400e',
      fontWeight: 700
    }
  }, "amber"), " = below expected minimum for set type."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 12,
      marginBottom: 20,
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("label", {
    style: {
      display: 'flex',
      gap: 8,
      alignItems: 'center',
      cursor: 'pointer',
      fontWeight: 600,
      fontSize: '0.9rem'
    }
  }, /*#__PURE__*/React.createElement("input", {
    type: "checkbox",
    checked: timingFlagged,
    onChange: function onChange(e) {
      return setTimingFlagged(e.target.checked);
    },
    style: {
      width: 16,
      height: 16
    }
  }), "Show flagged only (", timing.filter(function (t) {
    return t.flag > 0;
  }).length, " entries)")), timing.length === 0 && /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      fontStyle: 'italic'
    }
  }, "No timing data yet \u2014 data is collected as pupils complete sets."), timing.length > 0 && /*#__PURE__*/React.createElement("table", {
    className: "t-table"
  }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Pupil"), /*#__PURE__*/React.createElement("th", null, "Set"), /*#__PURE__*/React.createElement("th", null, "Score"), /*#__PURE__*/React.createElement("th", null, "Time"), /*#__PURE__*/React.createElement("th", null, "Flag"))), /*#__PURE__*/React.createElement("tbody", null, timing.filter(function (t) {
    return !timingFlagged || t.flag > 0;
  }).map(function (t, i) {
    var flagEl = t.flag === 2 ? /*#__PURE__*/React.createElement("span", {
      style: {
        background: '#ffeaec',
        color: 'var(--red-bright)',
        fontWeight: 800,
        fontSize: '0.78rem',
        padding: '3px 8px',
        borderRadius: 5
      }
    }, "VERY FAST") : t.flag === 1 ? /*#__PURE__*/React.createElement("span", {
      style: {
        background: '#fef3c7',
        color: '#92400e',
        fontWeight: 800,
        fontSize: '0.78rem',
        padding: '3px 8px',
        borderRadius: 5
      }
    }, "FAST") : /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--lgrey)',
        fontSize: '0.85rem'
      }
    }, "\u2014");
    var mins = Math.floor(t.time_seconds / 60);
    var secs = t.time_seconds % 60;
    var timeStr = mins > 0 ? "".concat(mins, "m ").concat(secs, "s") : "".concat(secs, "s");
    return /*#__PURE__*/React.createElement("tr", {
      key: i,
      style: {
        background: t.flag === 2 ? '#fff5f5' : t.flag === 1 ? '#fffbeb' : 'inherit'
      }
    }, /*#__PURE__*/React.createElement("td", {
      style: {
        fontWeight: 700
      }
    }, t.pupil_name), /*#__PURE__*/React.createElement("td", {
      style: {
        fontSize: '0.9rem'
      }
    }, t.set_title), /*#__PURE__*/React.createElement("td", null, /*#__PURE__*/React.createElement("strong", {
      style: {
        color: t.score >= 80 ? 'var(--green-bright)' : 'var(--gold)'
      }
    }, t.score, "%")), /*#__PURE__*/React.createElement("td", {
      style: {
        fontFamily: 'monospace',
        fontWeight: 600
      }
    }, timeStr), /*#__PURE__*/React.createElement("td", null, flagEl));
  })))), tab === 'misconceptions' && /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 900
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: '1.8rem',
      marginBottom: 20
    }
  }, "Common Wrong Answers"), /*#__PURE__*/React.createElement("table", {
    className: "t-table"
  }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Question"), /*#__PURE__*/React.createElement("th", null, "Wrote"), /*#__PURE__*/React.createElement("th", null, "Correct"), /*#__PURE__*/React.createElement("th", null, "Times"))), /*#__PURE__*/React.createElement("tbody", null, misc.slice(0, 20).map(function (r, i) {
    return /*#__PURE__*/React.createElement("tr", {
      key: i
    }, /*#__PURE__*/React.createElement("td", null, r.question_text || r.question), /*#__PURE__*/React.createElement("td", {
      className: "latin",
      style: {
        color: 'var(--red-bright)'
      }
    }, r.pupil_answer || r.wrong_answer), /*#__PURE__*/React.createElement("td", {
      className: "latin",
      style: {
        color: 'var(--green-bright)'
      }
    }, r.correct_answer || r.correct), /*#__PURE__*/React.createElement("td", null, r.occurrences || r.count || r.n));
  })))), tab === 'preview' && /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.2rem',
      color: 'var(--grey)',
      marginBottom: 20
    }
  }, "Click any set to preview. Progress will not be saved."), nodes.map(function (node) {
    return /*#__PURE__*/React.createElement("div", {
      key: node.label
    }, /*#__PURE__*/React.createElement("div", {
      className: "section-label"
    }, node.label), /*#__PURE__*/React.createElement("div", {
      className: "set-grid"
    }, node.sets.map(function (s) {
      return /*#__PURE__*/React.createElement("div", {
        key: s.id,
        className: "set-card passed",
        onClick: function onClick() {
          return api("/api/sets/".concat(s.id)).then(onStart);
        }
      }, /*#__PURE__*/React.createElement("div", {
        className: "tag-badge",
        style: {
          background: tagColorWithBadge(s.type, s.badge)
        }
      }, tagLabelWithBadge(s.type, s.badge)), /*#__PURE__*/React.createElement("h3", {
        dangerouslySetInnerHTML: {
          __html: renderOrdinals(s.title)
        }
      }));
    })));
  })), tab === 'pupil' && selPupil && /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 900
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: '1.8rem',
      marginBottom: 20
    }
  }, selPupil.first_name || selPupil.name), /*#__PURE__*/React.createElement("table", {
    className: "t-table"
  }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Set"), /*#__PURE__*/React.createElement("th", null, "Status"), /*#__PURE__*/React.createElement("th", null, "Best Score"), /*#__PURE__*/React.createElement("th", null, "Attempts"))), /*#__PURE__*/React.createElement("tbody", null, detail.map(function (d, i) {
    var s = sets.find(function (s) {
      return s.id === d.set_id;
    });
    return /*#__PURE__*/React.createElement("tr", {
      key: i
    }, /*#__PURE__*/React.createElement("td", null, s ? s.title : "Set ".concat(d.set_id)), /*#__PURE__*/React.createElement("td", null, d.status), /*#__PURE__*/React.createElement("td", null, d.best_score ? Math.round(d.best_score) + '%' : '-'), /*#__PURE__*/React.createElement("td", null, d.attempts));
  })))))), children);
}

// ── Front Overlay ─────────────────────────────────────────────────────────────
function Front(_ref20) {
  var set = _ref20.set,
    onGo = _ref20.onGo,
    onBack = _ref20.onBack,
    onComplete = _ref20.onComplete;
  var isOverlay = set.type === 'reference' || set.type === 'concept';
  var complete = onComplete || onBack;
  useEffect(function () {
    var h = function h(e) {
      if (e.key === 'Escape') onBack();
      if (e.key === 'Enter') {
        isOverlay ? complete() : onGo();
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  }, [onBack, onGo, isOverlay, complete]);

  // Check if the set content is screens-based (e.g. concept)
  var screens = set.screens || [];
  var _useState71 = useState(0),
    _useState72 = _slicedToArray(_useState71, 2),
    screenIdx = _useState72[0],
    setScreenIdx = _useState72[1];
  useEffect(function () {
    var _document$querySelect3;
    (_document$querySelect3 = document.querySelector('.modal-content')) === null || _document$querySelect3 === void 0 || _document$querySelect3.scrollTo({
      top: 0,
      behavior: 'instant'
    });
  }, [screenIdx]);

  // If it's a concept, we act as an intro modal scrolling through screens. If standard reference or standard set, we just show the title/sell
  if (isOverlay && screens.length > 0) {
    var s = screens[screenIdx];
    return /*#__PURE__*/React.createElement("div", {
      className: "modal-overlay anim-fade"
    }, /*#__PURE__*/React.createElement("div", {
      className: "modal-content",
      style: {
        textAlign: 'left'
      }
    }, /*#__PURE__*/React.createElement("h2", {
      style: {
        fontSize: '2.5rem',
        color: 'var(--navy)',
        marginBottom: 24
      },
      dangerouslySetInnerHTML: {
        __html: renderOrdinals(s.heading)
      }
    }), s.warning && /*#__PURE__*/React.createElement("div", {
      style: {
        background: '#ffeaec',
        border: '3px solid var(--red-bright)',
        borderRadius: 12,
        padding: '16px 20px',
        marginBottom: 16,
        fontWeight: 700,
        color: '#991b1b'
      }
    }, renderText(s.warning)), s.body && /*#__PURE__*/React.createElement("p", {
      style: {
        fontSize: '1.3rem',
        color: 'var(--grey)',
        lineHeight: 1.5,
        marginBottom: 20,
        textAlign: s.body_align || 'left'
      }
    }, renderTextWithKey(s.body)), s.principal_parts_table && /*#__PURE__*/React.createElement("table", {
      className: "pp-table",
      style: {
        marginBottom: 16
      }
    }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Principal Part"), /*#__PURE__*/React.createElement("th", null, "Name"), /*#__PURE__*/React.createElement("th", null, "Latin form"), /*#__PURE__*/React.createElement("th", null, "English meaning"))), /*#__PURE__*/React.createElement("tbody", null, s.principal_parts_table.map(function (r, i) {
      return /*#__PURE__*/React.createElement("tr", {
        key: i
      }, /*#__PURE__*/React.createElement("td", {
        style: {
          fontWeight: 800
        }
      }, r.part), /*#__PURE__*/React.createElement("td", null, r.name), /*#__PURE__*/React.createElement("td", {
        className: "lat-cell"
      }, r.latin), /*#__PURE__*/React.createElement("td", {
        style: {
          color: 'var(--grey)'
        }
      }, r.english));
    }))), s.table && /*#__PURE__*/React.createElement("table", {
      className: "conj-table"
    }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Person & Number"), /*#__PURE__*/React.createElement("th", null, "Ending"), /*#__PURE__*/React.createElement("th", null, "Example"))), /*#__PURE__*/React.createElement("tbody", null, s.table.map(function (r, i) {
      return /*#__PURE__*/React.createElement("tr", {
        key: i
      }, /*#__PURE__*/React.createElement("td", {
        style: {
          fontWeight: 800
        }
      }, r.conjugation), /*#__PURE__*/React.createElement("td", null, /*#__PURE__*/React.createElement("span", {
        className: "latin"
      }, r.infinitive_ending)), /*#__PURE__*/React.createElement("td", null, r.ep ? r.ep.map(function (p, pi) {
        return /*#__PURE__*/React.createElement("span", {
          key: pi,
          className: "latin",
          style: {
            color: p[1] === 'blue' ? 'var(--blue)' : p[1] === 'coral' || p[1] === 'red' ? 'var(--coral)' : p[1] === 'purple' ? '#7C3AED' : p[1] === 'pink' ? '#DB2777' : p[1] === 'gold' || p[1] === 'yellow' ? 'var(--gold)' : p[1] === 'green' ? '#16a34a' : 'var(--dark)'
          }
        }, p[0]);
      }) : /*#__PURE__*/React.createElement("span", {
        className: "latin"
      }, r.example), r.tr && /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--grey)',
          fontStyle: 'italic',
          fontSize: '0.9em',
          marginLeft: 6
        }
      }, "(", r.tr, ")")));
    }))), s.table_note && /*#__PURE__*/React.createElement("p", {
      style: {
        marginTop: 10,
        fontSize: '0.9rem',
        color: 'var(--grey)',
        fontStyle: 'italic'
      }
    }, renderTextWithKey(s.table_note)), /*#__PURE__*/React.createElement("div", {
      style: {
        marginTop: 20,
        display: 'flex',
        gap: 24,
        justifyContent: 'center'
      }
    }, screenIdx > 0 && /*#__PURE__*/React.createElement("button", {
      className: "btn btn-outline",
      onClick: function onClick() {
        return setScreenIdx(function (i) {
          return i - 1;
        });
      }
    }, "Back"), screenIdx < screens.length - 1 ? /*#__PURE__*/React.createElement("button", {
      className: "btn btn-primary",
      autoFocus: true,
      onClick: function onClick() {
        return setScreenIdx(function (i) {
          return i + 1;
        });
      }
    }, "Next", /*#__PURE__*/React.createElement("span", {
      className: "keyhint",
      style: {
        color: 'white'
      }
    }, "Enter")) : /*#__PURE__*/React.createElement("button", {
      className: "btn btn-primary",
      autoFocus: true,
      onClick: complete
    }, "Got it", /*#__PURE__*/React.createElement("span", {
      className: "keyhint",
      style: {
        color: 'white'
      }
    }, "Esc")))));
  }
  return /*#__PURE__*/React.createElement("div", {
    className: isOverlay ? "modal-overlay anim-fade" : "fullscreen"
  }, !isOverlay && /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: isOverlay ? "modal-content" : "front-page anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: isOverlay ? "" : "front-box"
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: isOverlay ? '3.5rem' : '3.5rem',
      marginBottom: 24,
      color: 'var(--navy)'
    },
    dangerouslySetInnerHTML: {
      __html: renderOrdinals(set.title)
    }
  }), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.5rem',
      color: 'var(--grey)',
      lineHeight: 1.5,
      whiteSpace: 'pre-line',
      marginBottom: 40,
      textAlign: 'center'
    }
  }, renderText(set.sell)), set.footnote && /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--lgrey)',
      fontSize: '0.9rem',
      marginTop: 8,
      marginBottom: 8,
      fontStyle: 'italic'
    }
  }, renderTextWithKey(set.footnote)), set.pass_mark ? /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      color: 'var(--navy)',
      fontSize: '1.4rem'
    }
  }, "Pass mark: ", set.pass_mark, "%") : null, /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 60,
      display: 'flex',
      gap: 24,
      justifyContent: 'center'
    }
  }, isOverlay ? /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    autoFocus: true,
    onClick: complete
  }, "Got it", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Esc")) : /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-outline",
    onClick: onBack
  }, "Back", /*#__PURE__*/React.createElement("span", {
    className: "keyhint"
  }, "Esc")), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    autoFocus: true,
    onClick: onGo
  }, "Begin", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")))))));
}

// ── Play router ───────────────────────────────────────────────────────────────
function Play(_ref21) {
  var pupil = _ref21.pupil,
    set = _ref21.set,
    isPreview = _ref21.isPreview,
    onFinish = _ref21.onFinish,
    onSaveAndNext = _ref21.onSaveAndNext,
    onBack = _ref21.onBack;
  var _useState73 = useState('init'),
    _useState74 = _slicedToArray(_useState73, 2),
    phase = _useState74[0],
    setPhase = _useState74[1];
  var _useState75 = useState(null),
    _useState76 = _slicedToArray(_useState75, 2),
    targetPhase = _useState76[0],
    setTargetPhase = _useState76[1];
  var _useState77 = useState(false),
    _useState78 = _slicedToArray(_useState77, 2),
    confirmQuit = _useState78[0],
    setConfirmQuit = _useState78[1];
  var _useState79 = useState({
      correct: 0,
      wrong: []
    }),
    _useState80 = _slicedToArray(_useState79, 2),
    res = _useState80[0],
    setRes = _useState80[1];
  var totalRef = useRef(0);
  var originalTargetRef = useRef(null);
  useEffect(function () {
    var _document$querySelect4;
    (_document$querySelect4 = document.querySelector('.activity-body')) === null || _document$querySelect4 === void 0 || _document$querySelect4.scrollTo({
      top: 0,
      behavior: 'instant'
    });
    var target = set.type;
    if (set.type === 'vocab' || set.type === 'verbs') {
      var n = set.verbs ? (set.verbs || []).length : (set.vocab || []).length;
      totalRef.current = n * 2;
      target = 'vocab_overview';
    } else if (set.type === 'building_parts') {
      var verbs = set.verbs || [];
      var mode = set.mode;
      var countVerbs = mode === 'ppps' ? verbs.filter(function (v) {
        return v.ppp !== null;
      }).length : verbs.length;
      if (mode === 'all_four_from_present') totalRef.current = verbs.length;else if (mode === 'all_four') {
        // MC phase: one question per verb; typed phase: one per gap per verb
        var gapPos = set.gap_positions || [2, 3];
        var typedCount = verbs.reduce(function (acc, v) {
          var parts = [v.present, v.infinitive, v.perfect, v.ppp];
          return acc + gapPos.filter(function (g) {
            return parts[g] != null;
          }).length;
        }, 0);
        totalRef.current = verbs.length + typedCount;
      } else if (mode === 'all_four_progressive') {
        // phase1: all verbs (gap=perfect), phase2: PPP-having verbs (gap=PPP), phase3: all verbs (all_four_from_present)
        var pppCount = verbs.filter(function (v) {
          return v.ppp !== null;
        }).length;
        totalRef.current = verbs.length + pppCount + verbs.length;
      } else totalRef.current = countVerbs * 2; // MC phase + typed phase each count
      target = mode === 'all_four_from_present' || mode === 'all_four_progressive' ? 'bp_typed' : 'bp_pattern';
    } else if (set.type === 'tense_id') {
      totalRef.current = (set.questions || []).length;
      target = 'tense_id';
    } else if (set.type === 'parsing') {
      totalRef.current = (set.questions || []).length;
      target = 'parsing';
    } else if (set.type === 'parsing_mcq') {
      totalRef.current = (set.questions || []).length;
      target = 'parsing_mcq';
    } else if (set.type === 'translate_form') {
      totalRef.current = (set.questions || []).length * 2;
      target = 'translate_form';
    } else if (set.type === 'sentences') {
      totalRef.current = (set.sentences || []).length;
      target = 'sentences';
    } else if (set.type === 'review') {
      var sCount = (set.sentences || []).length;
      var ptCount = (set.parse_translate || []).length;
      totalRef.current = sCount + ptCount;
      target = 'parse_translate';
    } else if (set.type === 'verb_conjugation') {
      // FC (no marks) → MC (1 per verb) → Typed (part + meaning = 2 per verb)
      totalRef.current = (set.verbs || []).length * 3;
      target = 'verb_conj_fc';
    } else if (set.type === 'intro' || set.type === 'reference' || set.type === 'concept') {
      totalRef.current = 1;
      target = 'intro';
    }
    originalTargetRef.current = target;
    if (set.screens && set.screens.length > 0 && target !== 'intro') {
      setTargetPhase(target);
      setPhase('intro');
    } else {
      setPhase(target);
    }
  }, []);
  useEffect(function () {
    if (phase === 'results') return;
    var h = function h(e) {
      if (e.key === 'Escape') {
        if (showPlayLB) {
          setShowPlayLB(false);
        } else {
          setConfirmQuit(function (q) {
            return !q;
          });
        }
      }
      if (e.ctrlKey && e.altKey && e.code === "KeyS") {
        totalRef.current = 1;
        setRes({
          correct: 1,
          wrong: []
        });
        setPhase('results');
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  }, [phase]);
  var _useState81 = useState(0),
    _useState82 = _slicedToArray(_useState81, 2),
    streak = _useState82[0],
    setStreak = _useState82[1];
  var addC = function addC() {
    setRes(function (p) {
      return _objectSpread(_objectSpread({}, p), {}, {
        correct: p.correct + 1
      });
    });
    setStreak(function (s) {
      return s + 1;
    });
  };
  var addW = function addW(w) {
    setRes(function (p) {
      return _objectSpread(_objectSpread({}, p), {}, {
        wrong: [].concat(_toConsumableArray(p.wrong), [w])
      });
    });
    setStreak(0);
  };
  var wrongCount = res.wrong.length;
  var HELP_TIPS = {
    vocab_fc: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Flashcard practice."), " No marks, just exposure. Press ", /*#__PURE__*/React.createElement("strong", null, "SPACE"), " to flip the card. Press ", /*#__PURE__*/React.createElement("strong", null, "1"), " if you found it hard, ", /*#__PURE__*/React.createElement("strong", null, "2"), " if you got it. Hard cards come back more often before the set ends."),
    vocab_mc: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Multiple choice."), " Pick the right English meaning from four options using keys ", /*#__PURE__*/React.createElement("strong", null, "1\u20134"), ", then press ", /*#__PURE__*/React.createElement("strong", null, "Enter"), " to confirm. There is a 10-second timer per question; if it runs out the question is marked wrong."),
    vocab_typed: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Type the English translation"), " of the Latin word and press ", /*#__PURE__*/React.createElement("strong", null, "Enter"), ". If you get it wrong, you'll see an explanation and have to type the correct answer once before you can continue."),
    bp_fc: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Principal-parts flashcard."), " Press ", /*#__PURE__*/React.createElement("strong", null, "SPACE"), " to reveal all four parts. Press ", /*#__PURE__*/React.createElement("strong", null, "1"), " for hard, ", /*#__PURE__*/React.createElement("strong", null, "2"), " if you knew it."),
    bp_mc: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Multiple choice."), " Pick the correct principal part from the four options. Use keys ", /*#__PURE__*/React.createElement("strong", null, "1\u20134"), " to select, then press ", /*#__PURE__*/React.createElement("strong", null, "Enter"), " to continue."),
    bp_typed: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Type the missing principal part"), " for each verb and press ", /*#__PURE__*/React.createElement("strong", null, "Enter"), ". Wrong answers will be re-shown with the correct form before you continue."),
    tense_id: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Identify the tense"), " of the Latin verb form shown. Use the keys ", /*#__PURE__*/React.createElement("strong", null, "1\u20134"), " or click. Wrong answers explain which tense marker gives the form away."),
    parsing: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Full parse:"), " identify person/number, then tense \u2014 each step marked individually."),
    parsing_mcq: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Pick the correct parse"), " of the Latin verb from the multiple-choice options."),
    translate_form: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Latin verb form \u2192 English."), " You'll be shown a single Latin verb form (e.g. ", /*#__PURE__*/React.createElement("em", null, "amabamus"), ") and asked to choose its person, then tense, then English translation in three steps. Used in tense-practice sets."),
    tf_typed: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Type the English"), " for the Latin verb form shown, then press ", /*#__PURE__*/React.createElement("strong", null, "Enter"), ". Wrong answers must be retyped correctly before you can continue."),
    sentences: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Translate the whole sentence."), " Press ", /*#__PURE__*/React.createElement("strong", null, "Enter"), " to check your answer. If you get it wrong, you'll see an explanation of the grammar and have to type the correct answer before continuing."),
    parse_translate: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Parse one verb, then translate the sentence."), " Two steps per question; each is marked separately."),
    bp_pattern: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Pattern-match principal parts."), " Match each Latin form to the principal-part position it belongs in."),
    vocab_overview: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Set overview."), " Have a quick look at every word in the set, then press ", /*#__PURE__*/React.createElement("strong", null, "Enter"), " to begin."),
    verb_conj_fc: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Flashcard \u2014 principal parts."), " Press ", /*#__PURE__*/React.createElement("strong", null, "SPACE"), " to reveal all four principal parts. Press ", /*#__PURE__*/React.createElement("strong", null, "1"), " if you found it hard, ", /*#__PURE__*/React.createElement("strong", null, "2"), " if you knew it. Hard cards come back before the set ends."),
    verb_conj_mc: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Multiple choice \u2014 meanings."), " All four principal parts are shown. Pick the correct English meaning from the four options using keys ", /*#__PURE__*/React.createElement("strong", null, "1\u20134"), ", then press ", /*#__PURE__*/React.createElement("strong", null, "Enter"), "."),
    verb_conj: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Principal parts drill."), " Each question shows a verb with one part blanked. Type the missing principal part in the left box, and the English meaning in the right box. Press ", /*#__PURE__*/React.createElement("strong", null, "Tab"), " to switch between boxes, ", /*#__PURE__*/React.createElement("strong", null, "Enter"), " to check."),
    intro: /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("strong", null, "Rule explanation."), " Read the grammar carefully. You'll be tested on it next. Press ", /*#__PURE__*/React.createElement("strong", null, "Enter"), " to advance.")
  };
  var tip = HELP_TIPS[phase];
  var _useState83 = useState(false),
    _useState84 = _slicedToArray(_useState83, 2),
    showRule = _useState84[0],
    setShowRule = _useState84[1];
  var _useState85 = useState(false),
    _useState86 = _slicedToArray(_useState85, 2),
    showPlayLB = _useState86[0],
    setShowPlayLB = _useState86[1];
  var _useState87 = useState([]),
    _useState88 = _slicedToArray(_useState87, 2),
    playLBData = _useState88[0],
    setPlayLBData = _useState88[1];
  var openPlayLB = function openPlayLB() {
    api('/api/leaderboard').then(setPlayLBData);
    setShowPlayLB(true);
  };
  // Hint-chip flash: pulse the ? button on the first two sets of any node
  // so first-time pupils notice it. Stops once the pupil hovers/clicks it.
  var _useState89 = useState(function () {
      return !!localStorage.getItem('hintSeen');
    }),
    _useState90 = _slicedToArray(_useState89, 2),
    hintSeen = _useState90[0],
    setHintSeen = _useState90[1];
  var flashHint = !hintSeen && set && (set.id <= 2 || set.id === 21 || set.id === 37);
  var _useState91 = useState(false),
    _useState92 = _slicedToArray(_useState91, 2),
    autoTip = _useState92[0],
    setAutoTip = _useState92[1];
  useEffect(function () {
    if (flashHint) {
      setAutoTip(true);
      var t = setTimeout(function () {
        return setAutoTip(false);
      }, 4000);
      return function () {
        clearTimeout(t);
        setAutoTip(false);
      };
    }
  }, [flashHint]);
  var ruleCard = set.rule_card;
  var pct = totalRef.current > 0 ? Math.min(100, res.correct / totalRef.current * 100) : 0;
  var done = function done() {
    return setPhase('results');
  };

  // Stable shuffled arrays - only computed once
  var vocabItems = useRef(shuffleOnce(set.vocab ? (set.vocab || []).map(function (v) {
    return _objectSpread(_objectSpread({}, v), {}, {
      dative_note: v.dative_note || DATIVE_VERBS.has(v.latin)
    });
  }) : (set.verbs || []).map(function (v) {
    return _objectSpread({
      latin: v.present,
      english: [v.eng_present],
      pos: 'verb',
      id: v.present,
      dative_note: DATIVE_VERBS.has(v.present)
    }, v.derivatives ? {
      derivatives: v.derivatives
    } : {});
  })));
  var vocabItemsTyped = useRef(shuffleOnce(set.vocab ? (set.vocab || []).map(function (v) {
    return _objectSpread(_objectSpread({}, v), {}, {
      dative_note: v.dative_note || DATIVE_VERBS.has(v.latin)
    });
  }) : (set.verbs || []).map(function (v) {
    return _objectSpread({
      latin: v.present,
      english: [v.eng_present],
      pos: 'verb',
      id: v.present,
      dative_note: DATIVE_VERBS.has(v.present)
    }, v.derivatives ? {
      derivatives: v.derivatives
    } : {});
  })));
  var bpVerbs = useRef(shuffleOnce(_toConsumableArray(set.verbs || [])));
  var vcVerbs = useRef(shuffleOnce(_toConsumableArray(set.verbs || [])));
  var tenseQs = useRef(_toConsumableArray(set.questions || [])); // server shuffles already
  var parsingQs = useRef(_toConsumableArray(set.questions || []));
  var sentences = useRef(_toConsumableArray(set.sentences || []));
  var tfTypedQs = useRef(shuffleOnce(_toConsumableArray(set.questions || [])));
  var parseTrQs = useRef(_toConsumableArray(set.parse_translate || []));
  var content = null;
  if (phase === 'intro') content = /*#__PURE__*/React.createElement(Intro, {
    set: set,
    screens: set.screens || [],
    isPreview: isPreview,
    pupil: pupil,
    onDone: function onDone() {
      return targetPhase ? setPhase(targetPhase) : done();
    },
    pct: pct
  });else if (phase === 'vocab_overview') content = /*#__PURE__*/React.createElement(VocabOverview, {
    set: set,
    items: set.vocab || set.verbs || [],
    onDone: function onDone() {
      return setPhase('vocab_fc');
    }
  });else if (phase === 'vocab_fc') content = /*#__PURE__*/React.createElement(VocabFC, {
    pupil: pupil,
    set: set,
    items: vocabItems.current,
    isPreview: isPreview,
    onDone: function onDone() {
      return setPhase('vocab_mc');
    },
    pct: pct
  });else if (phase === 'vocab_mc') content = /*#__PURE__*/React.createElement(VocabMC, {
    pupil: pupil,
    set: set,
    items: vocabItems.current,
    isPreview: isPreview,
    onDone: function onDone() {
      return setPhase('vocab_typed');
    },
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'vocab_typed') content = /*#__PURE__*/React.createElement(VocabTyped, {
    pupil: pupil,
    set: set,
    items: vocabItemsTyped.current,
    isPreview: isPreview,
    onDone: done,
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'bp_pattern') content = /*#__PURE__*/React.createElement(BPPattern, {
    set: set,
    onDone: function onDone() {
      return setPhase('bp_fc');
    }
  });else if (phase === 'bp_fc') content = /*#__PURE__*/React.createElement(BPFC, {
    pupil: pupil,
    set: set,
    verbs: bpVerbs.current,
    isPreview: isPreview,
    onDone: function onDone() {
      return setPhase('bp_mc');
    },
    pct: pct
  });else if (phase === 'bp_mc') content = /*#__PURE__*/React.createElement(BPMC, {
    pupil: pupil,
    set: set,
    verbs: bpVerbs.current,
    isPreview: isPreview,
    onDone: function onDone() {
      return setPhase('bp_typed');
    },
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'bp_typed') content = /*#__PURE__*/React.createElement(BPTyped, {
    pupil: pupil,
    set: set,
    verbs: bpVerbs.current,
    isPreview: isPreview,
    onDone: done,
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'tense_id') content = /*#__PURE__*/React.createElement(TenseId, {
    pupil: pupil,
    set: set,
    qs: tenseQs.current,
    isPreview: isPreview,
    onDone: done,
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'parsing') content = /*#__PURE__*/React.createElement(FullParsing, {
    pupil: pupil,
    set: set,
    qs: parsingQs.current,
    isPreview: isPreview,
    onDone: done,
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'parsing_mcq') content = /*#__PURE__*/React.createElement(Parsing, {
    pupil: pupil,
    set: set,
    qs: set.questions || [],
    isPreview: isPreview,
    onDone: done,
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'translate_form') content = /*#__PURE__*/React.createElement(TranslateForm, {
    pupil: pupil,
    set: set,
    qs: set.questions || [],
    isPreview: isPreview,
    onDone: function onDone() {
      return setPhase('tf_typed');
    },
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'tf_typed') content = /*#__PURE__*/React.createElement(TFTyped, {
    pupil: pupil,
    set: set,
    qs: tfTypedQs.current,
    isPreview: isPreview,
    onDone: done,
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'sentences') content = /*#__PURE__*/React.createElement(Sentences, {
    pupil: pupil,
    set: set,
    qs: sentences.current,
    isPreview: isPreview,
    onDone: done,
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'parse_translate') content = /*#__PURE__*/React.createElement(ParseAndTranslate, {
    pupil: pupil,
    set: set,
    qs: parseTrQs.current,
    isPreview: isPreview,
    onDone: set.type === 'review' ? function () {
      return setPhase('sentences');
    } : done,
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'verb_conj_fc') content = /*#__PURE__*/React.createElement(VerbConjFC, {
    pupil: pupil,
    set: set,
    verbs: vcVerbs.current,
    isPreview: isPreview,
    onDone: function onDone() {
      return setPhase('verb_conj_mc');
    },
    pct: pct
  });else if (phase === 'verb_conj_mc') content = /*#__PURE__*/React.createElement(VerbConjMC, {
    pupil: pupil,
    set: set,
    verbs: vcVerbs.current,
    isPreview: isPreview,
    onDone: function onDone() {
      return setPhase('verb_conj');
    },
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'verb_conj') content = /*#__PURE__*/React.createElement(VerbConj, {
    pupil: pupil,
    set: set,
    verbs: vcVerbs.current,
    isPreview: isPreview,
    onDone: done,
    addC: addC,
    addW: addW,
    pct: pct
  });
  // Quick Review: filter the original vocab items to those the pupil missed,
  // then re-run the full FC → MC → Typed cycle on just that subset, then
  // show a done screen with options to move on or redo the whole set.
  var wrongLatinSet = useRef(new Set());
  var qrItems = useRef([]);
  var preQrPassed = useRef(false);
  var preQrScore = useRef(0);
  var startQuickReview = function startQuickReview() {
    // Capture pass state before we reset res.
    var s = totalRef.current > 0 ? Math.min(100, Math.round(res.correct / totalRef.current * 100)) : 100;
    preQrScore.current = s;
    preQrPassed.current = s >= (set.pass_mark || 80);
    // Build the wrong-item set from res.wrong, dedup'd.
    var lats = new Set(res.wrong.map(function (w) {
      return w.latin;
    }).filter(Boolean));
    wrongLatinSet.current = lats;
    // Filter from original vocabItems so we keep full item shape (english array, dative_note, etc.)
    var pool = vocabItems.current;
    qrItems.current = pool.filter(function (v) {
      return lats.has(v.latin);
    });
    if (qrItems.current.length === 0) {
      setRes({
        correct: 0,
        wrong: []
      });
      setStreak(0);
      setPhase(originalTargetRef.current || set.type);
      return;
    }
    saveProgress(s); // save before wiping res so score is always persisted
    setRes({
      correct: 0,
      wrong: []
    });
    setStreak(0);
    setPhase('qr_typed');
  };
  if (phase === 'qr_typed') content = /*#__PURE__*/React.createElement(VocabTyped, {
    pupil: pupil,
    set: set,
    items: qrItems.current,
    isPreview: isPreview,
    onDone: function onDone() {
      return setPhase('qr_done');
    },
    addC: addC,
    addW: addW,
    pct: pct
  });else if (phase === 'qr_done') content = /*#__PURE__*/React.createElement(QuickReviewDone, {
    count: qrItems.current.length,
    passed: preQrPassed.current,
    score: preQrScore.current,
    set: set,
    onRetry: function onRetry() {
      setRes({
        correct: 0,
        wrong: []
      });
      setStreak(0);
      setPhase(originalTargetRef.current || set.type);
    },
    onMenu: function onMenu() {
      return onFinish(preQrScore.current);
    },
    onSaveAndNext: onSaveAndNext
  });else if (phase === 'wrongs_practice') content = /*#__PURE__*/React.createElement(WrongsPractice, {
    wrongs: res.wrong,
    onDone: function onDone() {
      return onFinish(preQrScore.current);
    },
    set: set,
    pupil: pupil
  });else if (phase === 'results') content = /*#__PURE__*/React.createElement(Results, {
    res: res,
    set: set,
    total: totalRef.current,
    onFinish: onFinish,
    onSaveAndNext: onSaveAndNext,
    onPracticeWrongs: set.type === 'vocab' || set.type === 'verbs' ? startQuickReview : function () {
      var s = totalRef.current > 0 ? Math.min(100, Math.round(res.correct / totalRef.current * 100)) : 100;
      preQrScore.current = s;
      preQrPassed.current = s >= (set.pass_mark || 80);
      saveProgress(s);
      setPhase('wrongs_practice');
    }
  });
  var showStreak = ['sentences', 'review'].includes(set.type) ? 0 : streak;
  return /*#__PURE__*/React.createElement(StreakCtx.Provider, {
    value: showStreak
  }, content, phase !== 'results' && phase !== 'wrongs_practice' && phase !== 'qr_done' && /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'fixed',
      top: 24,
      right: 40,
      zIndex: 50,
      display: 'flex',
      gap: 10,
      alignItems: 'center'
    }
  }, wrongCount > 0 && /*#__PURE__*/React.createElement("span", {
    className: "play-chip queue",
    title: "Items you've missed in this set so far"
  }, /*#__PURE__*/React.createElement("strong", null, wrongCount), " to review"), ruleCard && /*#__PURE__*/React.createElement("button", {
    className: "play-chip",
    onClick: function onClick() {
      return setShowRule(true);
    },
    style: {
      cursor: 'pointer'
    }
  }, "Show the rule"), tip && /*#__PURE__*/React.createElement("span", {
    className: "help-wrap",
    onMouseEnter: function onMouseEnter() {
      if (!hintSeen) {
        localStorage.setItem('hintSeen', '1');
        setHintSeen(true);
      }
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "help-chip".concat(flashHint ? ' flash' : ''),
    "aria-label": "Help"
  }, "?"), /*#__PURE__*/React.createElement("div", {
    className: "help-tip".concat(autoTip ? ' open' : '')
  }, tip)), !isPreview && /*#__PURE__*/React.createElement("button", {
    onClick: openPlayLB,
    className: "play-chip",
    style: {
      cursor: 'pointer'
    }
  }, "Leaderboard"), /*#__PURE__*/React.createElement("button", {
    onClick: function onClick() {
      return setConfirmQuit(true);
    },
    className: "play-chip",
    style: {
      cursor: 'pointer'
    }
  }, "Menu")), showRule && ruleCard && /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'fixed',
      inset: 0,
      background: 'rgba(0,0,0,0.55)',
      zIndex: 200,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    },
    onClick: function onClick() {
      return setShowRule(false);
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    onClick: function onClick(e) {
      return e.stopPropagation();
    },
    style: {
      background: 'white',
      borderRadius: 20,
      padding: '40px 50px',
      maxWidth: 680,
      width: '92%',
      boxShadow: '0 20px 60px rgba(0,0,0,0.3)'
    }
  }, /*#__PURE__*/React.createElement("h3", {
    style: {
      color: 'var(--navy)',
      marginBottom: 16,
      fontSize: '1.5rem'
    }
  }, ruleCard.title || 'The rule'), /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: '1.1rem',
      lineHeight: 1.55,
      color: 'var(--dark)'
    }
  }, renderText(ruleCard.body || '')), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 24,
      textAlign: 'right'
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    onClick: function onClick() {
      return setShowRule(false);
    }
  }, "Got it", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Esc"))))), confirmQuit && /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'fixed',
      inset: 0,
      background: 'rgba(0,0,0,0.55)',
      zIndex: 200,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: 'white',
      borderRadius: 20,
      padding: '60px 80px',
      maxWidth: 520,
      width: '90%',
      textAlign: 'center',
      boxShadow: '0 20px 60px rgba(0,0,0,0.3)'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.3rem',
      fontWeight: 800,
      color: 'var(--navy)',
      marginBottom: 10
    }
  }, "Leave this set?"), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 40
    }
  }, "Your progress won't be saved."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 32,
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-outline",
    onClick: function onClick() {
      return setConfirmQuit(false);
    }
  }, "Keep going", /*#__PURE__*/React.createElement("span", {
    className: "keyhint"
  }, "Esc")), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    onClick: onBack
  }, "Leave", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "\u2192 Menu"))))), showPlayLB && /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'fixed',
      inset: 0,
      background: 'rgba(0,0,0,0.55)',
      zIndex: 200,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    },
    onClick: function onClick(e) {
      return e.target === e.currentTarget && setShowPlayLB(false);
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: 'white',
      borderRadius: 20,
      padding: '40px 40px 32px',
      maxWidth: 560,
      width: '92%',
      boxShadow: '0 20px 60px rgba(0,0,0,0.3)'
    }
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontSize: '2rem',
      color: 'var(--navy)',
      marginBottom: 4
    }
  }, "Leaderboard"), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 20,
      fontSize: '0.9rem'
    }
  }, "XP = sum of best scores across all completed sets."), /*#__PURE__*/React.createElement("div", {
    style: {
      maxHeight: '55vh',
      overflowY: 'auto',
      paddingRight: 2
    }
  }, playLBData.map(function (p) {
    return /*#__PURE__*/React.createElement(LBRow, {
      key: p.pupil_id,
      p: p,
      isMe: pupil && p.pupil_id === pupil.id
    });
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 24,
      textAlign: 'center'
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    onClick: function onClick() {
      return setShowPlayLB(false);
    }
  }, "Close", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Esc"))))));
}

// ── Intro ─────────────────────────────────────────────────────────────────────
function Intro(_ref22) {
  var set = _ref22.set,
    screens = _ref22.screens,
    isPreview = _ref22.isPreview,
    pupil = _ref22.pupil,
    onDone = _ref22.onDone,
    pct = _ref22.pct;
  var _useState93 = useState(0),
    _useState94 = _slicedToArray(_useState93, 2),
    idx = _useState94[0],
    setIdx = _useState94[1];
  var s = screens[idx];
  var total = screens.length;
  var cardRef = useRef(null);
  var finish = /*#__PURE__*/function () {
    var _ref23 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee9() {
      return _regenerator().w(function (_context9) {
        while (1) switch (_context9.n) {
          case 0:
            if (!(!isPreview && (set.type === 'intro' || set.type === 'reference' || set.type === 'concept'))) {
              _context9.n = 1;
              break;
            }
            _context9.n = 1;
            return post('/api/complete', {
              pupil_id: pupil.id,
              set_id: set.id,
              score: 100
            });
          case 1:
            onDone();
          case 2:
            return _context9.a(2);
        }
      }, _callee9);
    }));
    return function finish() {
      return _ref23.apply(this, arguments);
    };
  }();
  useEffect(function () {
    resetScroll();
  }, [idx]);
  useEffect(function () {
    var h = function h(e) {
      if (e.key === 'Enter') {
        if (idx < total - 1) setIdx(function (i) {
          return i + 1;
        });else finish();
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  }, [idx, total]);
  // Stagger fade-in: each child fades in paced to reading age ~14 (300ms/word)
  useEffect(function () {
    var card = cardRef.current;
    if (!card) return;
    card.classList.remove('si-run');
    var kids = Array.from(card.children);
    var t = 0;
    kids.forEach(function (el, i) {
      var isLast = i === kids.length - 1;
      var delay = isLast ? t + 400 : t;
      el.style.setProperty('--d', delay + 'ms');
      // For conj-table / pp-table: stagger each tbody row from the table's own delay
      if (el.tagName === 'TABLE' && (el.classList.contains('conj-table') || el.classList.contains('pp-table'))) {
        Array.from(el.querySelectorAll('tbody tr')).forEach(function (tr, ri) {
          tr.style.setProperty('--dr', delay + ri * 90 + 'ms');
        });
      }
      if (!isLast) {
        var wc = (el.textContent || '').trim().split(/\s+/).filter(Boolean).length || 1;
        t += Math.max(300, Math.min(2500, Math.round(wc * 396 * 0.8)));
      }
    });
    var id = setTimeout(function () {
      if (cardRef.current) cardRef.current.classList.add('si-run');
    }, 16);
    return function () {
      return clearTimeout(id);
    };
  }, [idx]);
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: (idx + 1) / total * 100
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 700,
      color: 'var(--grey)'
    }
  }, idx + 1, " / ", total)), /*#__PURE__*/React.createElement("div", {
    className: "intro-body"
  }, /*#__PURE__*/React.createElement("div", {
    className: "intro-card stagger-intro",
    ref: cardRef
  }, /*#__PURE__*/React.createElement("h2", {
    dangerouslySetInnerHTML: {
      __html: renderOrdinals(s.heading)
    }
  }), s.body && /*#__PURE__*/React.createElement("p", {
    style: {
      textAlign: s.body_align || 'left'
    }
  }, renderText(s.body)), s.example_latin && /*#__PURE__*/React.createElement("div", {
    className: "intro-example"
  }, /*#__PURE__*/React.createElement("div", {
    className: "lat-sent"
  }, s.example_latin), /*#__PURE__*/React.createElement("div", {
    className: "eng-sent"
  }, s.example_english), s.note && /*#__PURE__*/React.createElement("p", {
    style: {
      marginTop: 12,
      fontSize: '1.1rem',
      color: 'var(--gold)',
      fontWeight: 700
    }
  }, renderText(s.note))), s.principal_parts_table && /*#__PURE__*/React.createElement("table", {
    className: "pp-table"
  }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Principal Part"), /*#__PURE__*/React.createElement("th", null, "Name"), /*#__PURE__*/React.createElement("th", null, "Latin form"), /*#__PURE__*/React.createElement("th", null, "English meaning"))), /*#__PURE__*/React.createElement("tbody", null, s.principal_parts_table.map(function (r, i) {
    return /*#__PURE__*/React.createElement("tr", {
      key: i
    }, /*#__PURE__*/React.createElement("td", {
      style: {
        fontWeight: 800
      }
    }, r.part), /*#__PURE__*/React.createElement("td", null, r.name), /*#__PURE__*/React.createElement("td", {
      className: "lat-cell"
    }, r.latin), /*#__PURE__*/React.createElement("td", {
      style: {
        color: 'var(--grey)'
      }
    }, r.english));
  }))), s.table && /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("table", {
    className: "conj-table"
  }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Person & Number"), /*#__PURE__*/React.createElement("th", null, s.infinitive_ending_header || 'Ending'), /*#__PURE__*/React.createElement("th", null, "Example"))), /*#__PURE__*/React.createElement("tbody", null, s.table.map(function (r, i) {
    return /*#__PURE__*/React.createElement("tr", {
      key: i
    }, /*#__PURE__*/React.createElement("td", {
      style: {
        fontWeight: 800
      }
    }, r.conjugation), /*#__PURE__*/React.createElement("td", null, /*#__PURE__*/React.createElement("span", {
      className: "latin"
    }, r.infinitive_ending)), /*#__PURE__*/React.createElement("td", null, r.ep ? r.ep.map(function (p, pi) {
      return /*#__PURE__*/React.createElement("span", {
        key: pi,
        className: "latin",
        style: {
          color: p[1] === 'blue' ? 'var(--blue)' : p[1] === 'coral' || p[1] === 'red' ? 'var(--coral)' : p[1] === 'purple' ? '#7C3AED' : p[1] === 'pink' ? '#DB2777' : p[1] === 'gold' || p[1] === 'yellow' ? 'var(--gold)' : p[1] === 'green' ? '#16a34a' : 'var(--dark)'
        }
      }, p[0]);
    }) : /*#__PURE__*/React.createElement("span", {
      className: "latin"
    }, r.example), r.tr && /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--grey)',
        fontStyle: 'italic',
        fontSize: '0.9em',
        marginLeft: 6
      }
    }, "(", r.tr, ")")));
  }))), s.table2 && /*#__PURE__*/React.createElement(React.Fragment, null, s.table2_heading && /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      fontSize: '1rem',
      color: 'var(--navy)',
      marginTop: 24,
      marginBottom: 8,
      textAlign: 'left'
    }
  }, renderText(s.table2_heading)), s.table2_body && /*#__PURE__*/React.createElement("p", {
    style: {
      textAlign: 'left',
      marginBottom: 8,
      fontSize: '0.95rem'
    }
  }, renderText(s.table2_body)), /*#__PURE__*/React.createElement("table", {
    className: "conj-table"
  }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", null, "Person & Number"), /*#__PURE__*/React.createElement("th", null, s.infinitive_ending_header || 'Ending'), /*#__PURE__*/React.createElement("th", null, "Example"))), /*#__PURE__*/React.createElement("tbody", null, s.table2.map(function (r, i) {
    return /*#__PURE__*/React.createElement("tr", {
      key: i
    }, /*#__PURE__*/React.createElement("td", {
      style: {
        fontWeight: 800
      }
    }, r.conjugation), /*#__PURE__*/React.createElement("td", null, /*#__PURE__*/React.createElement("span", {
      className: "latin"
    }, r.infinitive_ending)), /*#__PURE__*/React.createElement("td", null, r.ep ? r.ep.map(function (p, pi) {
      return /*#__PURE__*/React.createElement("span", {
        key: pi,
        className: "latin",
        style: {
          color: p[1] === 'blue' ? 'var(--blue)' : p[1] === 'coral' || p[1] === 'red' ? 'var(--coral)' : p[1] === 'purple' ? '#7C3AED' : p[1] === 'pink' ? '#DB2777' : p[1] === 'gold' || p[1] === 'yellow' ? 'var(--gold)' : p[1] === 'green' ? '#16a34a' : 'var(--dark)'
        }
      }, p[0]);
    }) : /*#__PURE__*/React.createElement("span", {
      className: "latin"
    }, r.example), r.tr && /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--grey)',
        fontStyle: 'italic',
        fontSize: '0.9em',
        marginLeft: 6
      }
    }, "(", r.tr, ")")));
  })))), s.table_note && /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 12,
      fontSize: '1rem',
      color: 'var(--grey)',
      fontStyle: 'italic'
    }
  }, renderTextWithKey(s.table_note))), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 40,
      display: 'flex',
      gap: 24,
      justifyContent: 'center'
    }
  }, idx > 0 && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-outline",
    onClick: function onClick() {
      return setIdx(function (i) {
        return i - 1;
      });
    }
  }, "Back"), idx < total - 1 ? /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    autoFocus: true,
    onClick: function onClick() {
      return setIdx(function (i) {
        return i + 1;
      });
    }
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")) : /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    autoFocus: true,
    onClick: finish
  }, "Done", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")))))));
}

// ── Vocab Overview ─────────────────────────────────────────────────────────────
function VocabOverview(_ref24) {
  var set = _ref24.set,
    items = _ref24.items,
    onDone = _ref24.onDone;
  useEffect(function () {
    resetScroll();
  }, []);
  useEffect(function () {
    var h = function h(e) {
      if (e.key === 'Enter') onDone();
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  }, [onDone]);
  var POS_ORDER = ['noun', 'pronoun', 'adjective', 'verb', 'adverb', 'conjunction', 'preposition'];
  var POS_LABEL = {
    noun: 'Nouns',
    pronoun: 'Pronouns',
    adjective: 'Adjectives',
    verb: 'Verbs',
    adverb: 'Adverbs',
    conjunction: 'Conjunctions',
    preposition: 'Prepositions'
  };
  var hasPos = items.some(function (v) {
    return v.pos && POS_LABEL[v.pos];
  });
  var grouped = {};
  var ungrouped = [];
  if (hasPos) {
    items.forEach(function (v) {
      var p = v.pos || '_other';
      if (!grouped[p]) grouped[p] = [];
      grouped[p].push(v);
    });
  } else {
    ungrouped.push.apply(ungrouped, _toConsumableArray(items));
  }
  var sections = hasPos ? POS_ORDER.filter(function (p) {
    return grouped[p];
  }) : ['_other'];
  var renderChips = function renderChips(arr) {
    return arr.map(function (v, i) {
      return /*#__PURE__*/React.createElement("div", {
        key: i,
        className: "vocab-chip"
      }, /*#__PURE__*/React.createElement("div", {
        className: "lat",
        style: {
          fontSize: '1.3rem'
        }
      }, renderVocabLatin(_objectSpread(_objectSpread({}, v), {}, {
        latin: v.latin || v.present
      }))), v.pos === 'pronoun' && v.display_label && /*#__PURE__*/React.createElement("div", {
        style: {
          fontSize: '0.75rem',
          color: '#B5179E',
          fontStyle: 'italic',
          fontWeight: 600,
          marginTop: 2
        }
      }, "(", v.display_label, ")"), /*#__PURE__*/React.createElement("div", {
        className: "eng",
        style: {
          color: 'var(--grey)',
          fontSize: '0.9rem',
          marginTop: 4
        }
      }, (v.english || [v.eng_present || '']).join(', ')));
    });
  };
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: 1
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.5rem',
      fontWeight: 800,
      color: 'var(--navy)',
      marginBottom: 8
    }
  }, "Here's an overview of the ", items.length, " words in this set"), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 24,
      fontSize: '1.1rem'
    }
  }, "You do not need to memorise them before beginning the set."), hasPos ? sections.map(function (pos) {
    return /*#__PURE__*/React.createElement("div", {
      key: pos,
      style: {
        width: '100%',
        maxWidth: 900,
        marginBottom: 24
      }
    }, /*#__PURE__*/React.createElement("h3", {
      style: {
        fontSize: '1rem',
        fontWeight: 800,
        color: 'var(--navy)',
        textTransform: 'uppercase',
        letterSpacing: '0.05em',
        marginBottom: 10,
        borderBottom: '2px solid var(--lgrey)',
        paddingBottom: 6
      }
    }, POS_LABEL[pos]), /*#__PURE__*/React.createElement("div", {
      className: "vocab-overview",
      style: {
        marginTop: 0,
        marginBottom: 0
      }
    }, renderChips(grouped[pos] || [])));
  }) : /*#__PURE__*/React.createElement("div", {
    className: "vocab-overview"
  }, renderChips(ungrouped)), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    autoFocus: true,
    onClick: onDone,
    style: {
      marginTop: 10
    }
  }, "Begin", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")))));
}

// ── Vocab FC (flashcard - Press 1 Hard, Press 2 Got it) ───────────────────────
function VocabFC(_ref25) {
  var pupil = _ref25.pupil,
    set = _ref25.set,
    items = _ref25.items,
    isPreview = _ref25.isPreview,
    onDone = _ref25.onDone,
    pct = _ref25.pct;
  var _useState95 = useState(function () {
      return _toConsumableArray(items);
    }),
    _useState96 = _slicedToArray(_useState95, 2),
    queue = _useState96[0],
    setQueue = _useState96[1];
  var _useState97 = useState(0),
    _useState98 = _slicedToArray(_useState97, 2),
    idx = _useState98[0],
    setIdx = _useState98[1];
  var _useState99 = useState(false),
    _useState100 = _slicedToArray(_useState99, 2),
    rev = _useState100[0],
    setRev = _useState100[1];
  var _useState101 = useState(false),
    _useState102 = _slicedToArray(_useState101, 2),
    busy = _useState102[0],
    setBusy = _useState102[1];
  var _useState103 = useState(0),
    _useState104 = _slicedToArray(_useState103, 2),
    doneCount = _useState104[0],
    setDoneCount = _useState104[1];
  var _useState105 = useState(false),
    _useState106 = _slicedToArray(_useState105, 2),
    showDerivatives = _useState106[0],
    setShowDerivatives = _useState106[1];
  var _useState107 = useState(''),
    _useState108 = _slicedToArray(_useState107, 2),
    exitCls = _useState108[0],
    setExitCls = _useState108[1];
  var _useState109 = useState(false),
    _useState110 = _slicedToArray(_useState109, 2),
    entering = _useState110[0],
    setEntering = _useState110[1];
  var cardTimesRef = useRef([]);
  var cardStartRef = useRef(Date.now());
  var _useState111 = useState(true),
    _useState112 = _slicedToArray(_useState111, 2),
    autoplay = _useState112[0],
    setAutoplay = _useState112[1];
  var synthRef = useRef(window.speechSynthesis || null);
  // preprocess text: "/" → " or ", clean up for natural TTS reading
  // ttsClean: convert slashes and commas-between-meanings to "or" for natural speech
  var ttsClean = function ttsClean(t) {
    if (!t) return '';
    return t.replace(/\s*\/\s*/g, ' or ').replace(/,\s+/g, ' or ').replace(/\s+/g, ' ').trim();
  };
  var speak = function speak(text, isLatin) {
    var synth = synthRef.current;
    if (!synth) return;
    synth.cancel();
    var utt = new SpeechSynthesisUtterance('');
    var voices = synth.getVoices();
    if (isLatin) {
      // Classical Latin: hard-g fix — Spanish voice reads 'ge'/'gi' as soft-g (wrong for Latin).
      // Replace ge→gue, gi→gui so Spanish TTS produces the correct hard-g sound.
      var latText = ttsClean(text).replace(/g([ei])/gi, function (m, v2) {
        return 'gu' + v2;
      });
      utt.text = latText;
      var v = voices.find(function (v) {
        return v.lang.startsWith('la');
      }) || voices.find(function (v) {
        return v.lang.startsWith('es');
      }) || voices.find(function (v) {
        return v.lang.startsWith('it');
      }) || null;
      if (v) utt.voice = v;
      utt.lang = v ? v.lang : 'es-ES';
      utt.rate = 0.75;
    } else {
      utt.text = ttsClean(text);
      // Prefer natural UK human voices (Daniel/Serena/Oliver on macOS; Microsoft Hazel on Windows)
      var _v = voices.find(function (v) {
        return v.name === 'Daniel';
      }) || voices.find(function (v) {
        return v.name === 'Serena';
      }) || voices.find(function (v) {
        return v.name === 'Oliver';
      }) || voices.find(function (v) {
        return /hazel/i.test(v.name) && v.lang.startsWith('en-GB');
      }) || voices.find(function (v) {
        return v.lang === 'en-GB';
      }) || voices.find(function (v) {
        return v.lang.startsWith('en-GB');
      }) || voices.find(function (v) {
        return v.lang.startsWith('en');
      }) || null;
      if (_v) utt.voice = _v;
      utt.lang = 'en-GB';
      utt.rate = 0.82;
      utt.pitch = 1.05;
    }
    synth.speak(utt);
  };
  useEffect(function () {
    cardStartRef.current = Date.now();
  }, [idx]);
  // Autoplay Latin when card changes; hide derivatives panel
  useEffect(function () {
    setShowDerivatives(false);
    if (autoplay && queue[idx]) speak(queue[idx].latin, true);
  }, [idx, autoplay]);
  // Autoplay English when flipped
  useEffect(function () {
    if (autoplay && rev && queue[idx]) {
      var t = setTimeout(function () {
        return speak(queue[idx].english.join(', '), false);
      }, 250);
      return function () {
        return clearTimeout(t);
      };
    }
  }, [rev]);
  // Stop speech on unmount
  useEffect(function () {
    return function () {
      synthRef.current && synthRef.current.cancel();
    };
  }, []);
  var rate = /*#__PURE__*/function () {
    var _ref26 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee0(r) {
      var currentQ, newQueue;
      return _regenerator().w(function (_context0) {
        while (1) switch (_context0.n) {
          case 0:
            if (!busy) {
              _context0.n = 1;
              break;
            }
            return _context0.a(2);
          case 1:
            setBusy(true);
            currentQ = queue[idx];
            cardTimesRef.current.push(Date.now() - cardStartRef.current);
            if (isPreview) {
              _context0.n = 2;
              break;
            }
            _context0.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'flashcard_rating',
              question_text: currentQ.latin,
              pupil_answer: r
            });
          case 2:
            setExitCls(r === 'got_it' ? 'fc-exit-right' : 'fc-exit-left');
            if (r === 'again') {
              newQueue = [].concat(_toConsumableArray(queue), [_objectSpread(_objectSpread({}, currentQ), {}, {
                revisit: true
              })]);
              setQueue(newQueue);
              setTimeout(function () {
                setExitCls('');
                setRev(false);
                setBusy(false);
                if (idx + 1 >= newQueue.length) onDone();else {
                  setIdx(function (i) {
                    return i + 1;
                  });
                  setEntering(true);
                  setTimeout(function () {
                    return setEntering(false);
                  }, 230);
                }
              }, 270);
            } else {
              setDoneCount(function (d) {
                return d + 1;
              });
              setTimeout(function () {
                setExitCls('');
                setRev(false);
                setBusy(false);
                if (idx + 1 >= queue.length) onDone();else {
                  setIdx(function (i) {
                    return i + 1;
                  });
                  setEntering(true);
                  setTimeout(function () {
                    return setEntering(false);
                  }, 230);
                }
              }, 270);
            }
          case 3:
            return _context0.a(2);
        }
      }, _callee0);
    }));
    return function rate(_x9) {
      return _ref26.apply(this, arguments);
    };
  }();
  var q = queue[idx];
  var goBack = function goBack() {
    if (idx > 0) {
      setIdx(function (i) {
        return i - 1;
      });
      setRev(false);
    }
  };
  useEffect(function () {
    var h = function h(e) {
      if (e.code === 'Space') {
        e.preventDefault();
        if (!rev) setRev(true);else rate('got_it');
        return;
      }
      if (rev && e.key === '1') rate('again');
      if (rev && e.key === '2') rate('got_it');
      if ((e.ctrlKey || e.metaKey) && e.key === 'z' && idx > 0) {
        e.preventDefault();
        goBack();
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  var remaining = queue.slice(idx + 1);
  var freshInQueue = queue.slice(idx).filter(function (c) {
    return !c.revisit;
  }).length;
  var hardInQueue = remaining.filter(function (c) {
    return c.revisit;
  }).length;
  var n = cardTimesRef.current.length;
  var avgMs = n >= 5 ? cardTimesRef.current.reduce(function (a, b) {
    return a + b;
  }, 0) / n : 0;
  var estMs = avgMs > 0 ? remaining.length * avgMs : 0;
  var estLabel = avgMs > 0 ? estMs >= 60000 ? "~".concat(Math.round(estMs / 60000), " min left") : "~".concat(Math.round(estMs / 1000), "s left") : null;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'center',
      gap: 20,
      width: '100%',
      maxWidth: 1140,
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement(CardPile, {
    count: freshInQueue,
    hardCount: hardInQueue,
    side: "left"
  }), /*#__PURE__*/React.createElement("div", {
    className: "flashcard".concat(exitCls ? ' ' + exitCls : '').concat(entering ? ' fc-enter' : ''),
    style: {
      flex: 1,
      minWidth: 0,
      width: 'auto',
      maxWidth: 'none',
      position: 'relative',
      overflow: 'hidden'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'absolute',
      top: 18,
      right: 20,
      display: 'flex',
      gap: 8,
      alignItems: 'center',
      zIndex: 5
    }
  }, rev && /*#__PURE__*/React.createElement("button", {
    title: "Image (coming soon)",
    style: {
      background: 'none',
      border: 'none',
      cursor: 'default',
      padding: 4,
      borderRadius: 6,
      color: '#d1d5db',
      lineHeight: 1,
      display: 'flex',
      alignItems: 'center',
      animation: 'card-btn-appear 0.4s ease-out'
    }
  }, /*#__PURE__*/React.createElement("svg", {
    width: "16",
    height: "16",
    viewBox: "0 0 15 15",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: "1.5",
    strokeLinecap: "round"
  }, /*#__PURE__*/React.createElement("rect", {
    x: "1",
    y: "1.5",
    width: "13",
    height: "12",
    rx: "2"
  }), /*#__PURE__*/React.createElement("circle", {
    cx: "5.5",
    cy: "5.5",
    r: "1.3"
  }), /*#__PURE__*/React.createElement("path", {
    d: "M1 10.5l4-4 3 3 2-2 4 3.5"
  }))), rev && q.derivatives && q.derivatives.length > 0 && /*#__PURE__*/React.createElement("button", {
    onClick: function onClick(e) {
      e.stopPropagation();
      setShowDerivatives(function (d) {
        return !d;
      });
    },
    title: "English derivatives",
    style: {
      background: showDerivatives ? '#FFF3C4' : 'none',
      border: showDerivatives ? '1.5px solid #F59E0B' : '1.5px solid transparent',
      cursor: 'pointer',
      padding: 4,
      borderRadius: 6,
      color: showDerivatives ? '#92400E' : '#b45309',
      lineHeight: 1,
      display: 'flex',
      alignItems: 'center',
      transition: 'all .15s',
      animation: 'card-btn-appear 0.4s ease-out'
    }
  }, /*#__PURE__*/React.createElement("svg", {
    width: "16",
    height: "16",
    viewBox: "0 0 15 15",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: "1.5",
    strokeLinecap: "round"
  }, /*#__PURE__*/React.createElement("rect", {
    x: "1.5",
    y: "1",
    width: "12",
    height: "13",
    rx: "2"
  }), /*#__PURE__*/React.createElement("line", {
    x1: "4.5",
    y1: "4.5",
    x2: "10.5",
    y2: "4.5"
  }), /*#__PURE__*/React.createElement("line", {
    x1: "4.5",
    y1: "7.5",
    x2: "10.5",
    y2: "7.5"
  }), /*#__PURE__*/React.createElement("line", {
    x1: "4.5",
    y1: "10.5",
    x2: "8",
    y2: "10.5"
  }))), /*#__PURE__*/React.createElement("button", {
    onClick: function onClick(e) {
      e.stopPropagation();
      setAutoplay(function (a) {
        var n = !a;
        if (!n && synthRef.current) synthRef.current.cancel();
        if (n && queue[idx]) speak(rev ? queue[idx].english.join(', ') : queue[idx].latin, !rev);
        return n;
      });
    },
    title: autoplay ? 'Mute audio' : 'Unmute audio',
    style: {
      background: 'none',
      border: 'none',
      cursor: 'pointer',
      padding: 4,
      borderRadius: 6,
      color: autoplay ? '#94a3b8' : '#d1d5db',
      lineHeight: 1,
      display: 'flex',
      alignItems: 'center'
    }
  }, autoplay ? /*#__PURE__*/React.createElement("svg", {
    width: "18",
    height: "16",
    viewBox: "0 0 17 15",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: "1.6",
    strokeLinecap: "round"
  }, /*#__PURE__*/React.createElement("path", {
    d: "M1 5.5h2.5L7 2v11l-3.5-3.5H1V5.5z"
  }), /*#__PURE__*/React.createElement("path", {
    d: "M10.5 4a4.5 4.5 0 010 7M12.5 1.5a7 7 0 010 12"
  })) : /*#__PURE__*/React.createElement("svg", {
    width: "18",
    height: "16",
    viewBox: "0 0 17 15",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: "1.6",
    strokeLinecap: "round"
  }, /*#__PURE__*/React.createElement("path", {
    d: "M1 5.5h2.5L7 2v11l-3.5-3.5H1V5.5z"
  }), /*#__PURE__*/React.createElement("line", {
    x1: "11",
    y1: "4",
    x2: "16",
    y2: "11"
  }), /*#__PURE__*/React.createElement("line", {
    x1: "16",
    y1: "4",
    x2: "11",
    y2: "11"
  })))), showDerivatives && q.derivatives && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      position: 'absolute',
      inset: 0,
      background: '#FFFBEB',
      borderRadius: 32,
      padding: '40px 36px',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 10,
      boxShadow: 'inset 0 0 0 3px #F59E0B'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '0.7rem',
      fontWeight: 800,
      color: '#92400E',
      textTransform: 'uppercase',
      letterSpacing: '0.1em',
      marginBottom: 18
    }
  }, "English derivatives of ", /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'Crimson Text,serif',
      fontStyle: 'italic',
      fontSize: '1.1em'
    }
  }, q.latin)), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 12,
      width: '100%',
      maxWidth: 460
    }
  }, q.derivatives.map(function (d, i) {
    return /*#__PURE__*/React.createElement("div", {
      key: i,
      style: {
        background: 'white',
        border: '2px solid #FCD34D',
        borderRadius: 12,
        padding: '10px 16px',
        textAlign: 'left'
      }
    }, /*#__PURE__*/React.createElement("span", {
      style: {
        fontWeight: 900,
        fontSize: '1.1rem',
        color: '#92400E'
      }
    }, d.word), /*#__PURE__*/React.createElement("span", {
      style: {
        color: '#78350F',
        fontSize: '0.92rem',
        marginLeft: 8
      }
    }, "\u2014 ", d.meaning));
  })), /*#__PURE__*/React.createElement("button", {
    onClick: function onClick() {
      return setShowDerivatives(false);
    },
    style: {
      marginTop: 20,
      background: '#F59E0B',
      color: 'white',
      border: 'none',
      borderRadius: 8,
      padding: '8px 20px',
      fontWeight: 800,
      fontSize: '0.85rem',
      cursor: 'pointer',
      letterSpacing: '0.04em'
    }
  }, "Close")), /*#__PURE__*/React.createElement("h1", {
    className: "latin"
  }, q.latin), q.display_label && (q.pos === 'pronoun' ? /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: '0.7rem',
      color: '#0D9488',
      fontWeight: 800,
      fontStyle: 'normal',
      marginTop: 6,
      display: 'block',
      letterSpacing: '0.06em',
      textTransform: 'uppercase'
    }
  }, "(", q.display_label.toUpperCase(), ")") : /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: '0.8rem',
      color: 'var(--white)',
      fontWeight: 800,
      fontStyle: 'normal',
      marginTop: 8,
      padding: '4px 12px',
      background: '#0D9488',
      borderRadius: 6,
      textTransform: 'uppercase',
      letterSpacing: '0.05em',
      display: 'inline-block'
    }
  }, q.display_label.toUpperCase())), rev && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 30,
      textAlign: 'center'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '2.5rem',
      fontWeight: 800,
      color: '#1a73e8'
    }
  }, q.english.join(', ')), q.dative_note && /*#__PURE__*/React.createElement("p", {
    style: {
      marginTop: 12,
      fontSize: '0.8rem',
      fontWeight: 800,
      color: '#fff',
      background: '#0D9488',
      borderRadius: 6,
      padding: '4px 12px',
      display: 'inline-block',
      textTransform: 'uppercase',
      letterSpacing: '0.05em'
    }
  }, "+ DATIVE"))), /*#__PURE__*/React.createElement(CardPile, {
    count: doneCount,
    side: "right"
  })), rev && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 50,
      display: 'flex',
      gap: 32
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-grey",
    disabled: busy,
    onClick: function onClick() {
      return rate('again');
    }
  }, "Hard", /*#__PURE__*/React.createElement("span", {
    className: "keyhint"
  }, "Press 1")), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: function onClick() {
      return rate('got_it');
    }
  }, "Easy", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Press 2"))), !rev && /*#__PURE__*/React.createElement("p", {
    style: {
      marginTop: 60,
      color: 'var(--grey)',
      fontSize: '1.4rem',
      fontWeight: 700
    }
  }, "Press SPACE to reveal"), idx > 0 && /*#__PURE__*/React.createElement("button", {
    onClick: goBack,
    style: {
      marginTop: 8,
      background: 'transparent',
      border: 'none',
      color: 'var(--lgrey)',
      fontSize: '0.8rem',
      cursor: 'pointer',
      opacity: 0.5
    }
  }, "\u2190", /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: '0.7rem',
      marginLeft: 6,
      opacity: 0.6
    }
  }, "Ctrl+Z")), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 16,
      display: 'flex',
      gap: 16,
      alignItems: 'center',
      flexWrap: 'wrap',
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: '0.9rem',
      fontWeight: 700,
      color: 'var(--lgrey)'
    }
  }, "Card ", idx + 1, " of ", queue.length, estLabel && /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 600
    }
  }, " \xB7 ", estLabel)), /*#__PURE__*/React.createElement("div", {
    style: {
      width: 200,
      height: 6,
      background: 'var(--lgrey)',
      borderRadius: 3,
      overflow: 'hidden'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      width: "".concat((idx + 1) / Math.max(queue.length, 1) * 100, "%"),
      height: '100%',
      background: 'var(--blue)',
      borderRadius: 3,
      transition: 'width .3s'
    }
  }))))));
}
function VocabMC(_ref27) {
  var pupil = _ref27.pupil,
    set = _ref27.set,
    items = _ref27.items,
    isPreview = _ref27.isPreview,
    onDone = _ref27.onDone,
    addC = _ref27.addC,
    addW = _ref27.addW,
    pct = _ref27.pct,
    distractorPool = _ref27.distractorPool;
  var _useState113 = useState(function () {
      return _toConsumableArray(items);
    }),
    _useState114 = _slicedToArray(_useState113, 2),
    queue = _useState114[0],
    setQueue = _useState114[1];
  var _useState115 = useState(0),
    _useState116 = _slicedToArray(_useState115, 2),
    qIdx = _useState116[0],
    setQIdx = _useState116[1];
  var _useState117 = useState(null),
    _useState118 = _slicedToArray(_useState117, 2),
    sel = _useState118[0],
    setSel = _useState118[1];
  var _useState119 = useState(null),
    _useState120 = _slicedToArray(_useState119, 2),
    fb = _useState120[0],
    setFb = _useState120[1];
  var _useState121 = useState(false),
    _useState122 = _slicedToArray(_useState121, 2),
    busy = _useState122[0],
    setBusy = _useState122[1];
  var _useState123 = useState(10),
    _useState124 = _slicedToArray(_useState123, 2),
    timeLeft = _useState124[0],
    setTimeLeft = _useState124[1];
  var q = queue[qIdx];
  var ansText = (q === null || q === void 0 ? void 0 : q.english.join(', ')) || '';
  // Distractor pool defaults to the items being quizzed; for Quick review we pass
  // the FULL vocab list so MCQ options always have 4 plausible choices.
  var pool = distractorPool && distractorPool.length >= 4 ? distractorPool : items;
  // Compute options once per question, locked in ref
  var optsRef = useRef(null);
  if (optsRef.current === null || optsRef.current.qIdx !== qIdx) {
    var otherItems = shuffleOnce(pool.filter(function (it) {
      return it !== q && (it.english || []).join(', ') !== ansText;
    }));
    var uniqueOthers = [];
    var _iterator2 = _createForOfIteratorHelper(otherItems),
      _step2;
    try {
      for (_iterator2.s(); !(_step2 = _iterator2.n()).done;) {
        var it = _step2.value;
        var txt = it.english.join(', ');
        if (txt !== ansText && !uniqueOthers.includes(txt) && uniqueOthers.length < 3) uniqueOthers.push(txt);
      }
    } catch (err) {
      _iterator2.e(err);
    } finally {
      _iterator2.f();
    }
    optsRef.current = {
      qIdx: qIdx,
      opts: shuffleOnce([ansText].concat(uniqueOthers))
    };
  }
  var opts = optsRef.current.opts;
  useEffect(function () {
    if (fb || busy) return;
    if (timeLeft <= 0) {
      var handleTimeout = /*#__PURE__*/function () {
        var _ref28 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee1() {
          var chkRes, res, _t2;
          return _regenerator().w(function (_context1) {
            while (1) switch (_context1.n) {
              case 0:
                setBusy(true);
                setSel('timeout');
                if (isPreview) {
                  _context1.n = 2;
                  break;
                }
                _context1.n = 1;
                return post('/api/check', {
                  pupil_id: pupil.id,
                  set_id: set.id,
                  question_type: 'mc',
                  question_text: q.id || q.latin,
                  pupil_answer: 'TIMEOUT',
                  correct_answer: ansText
                });
              case 1:
                _t2 = _context1.v;
                _context1.n = 3;
                break;
              case 2:
                _t2 = null;
              case 3:
                chkRes = _t2;
                res = {
                  counts_as_correct: false,
                  timeout: true,
                  message: "".concat(timeoutBadge(), " The correct answer is: **").concat((chkRes === null || chkRes === void 0 ? void 0 : chkRes.correct_answer) || ansText, "**")
                };
                setFb(res);
                if (!q.failed) {
                  addW({
                    latin: q.latin,
                    correct: (chkRes === null || chkRes === void 0 ? void 0 : chkRes.correct_answer) || ansText
                  });
                  setQueue(function (prev) {
                    return [].concat(_toConsumableArray(prev), [_objectSpread(_objectSpread({}, q), {}, {
                      failed: true
                    })]);
                  });
                }
                setBusy(false);
              case 4:
                return _context1.a(2);
            }
          }, _callee1);
        }));
        return function handleTimeout() {
          return _ref28.apply(this, arguments);
        };
      }();
      handleTimeout();
      return;
    }
    var t = setInterval(function () {
      return setTimeLeft(function (x) {
        return x - 1;
      });
    }, 1000);
    return function () {
      return clearInterval(t);
    };
  }, [timeLeft, fb, busy]);
  var pick = /*#__PURE__*/function () {
    var _ref29 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee10(o) {
      var res;
      return _regenerator().w(function (_context10) {
        while (1) switch (_context10.n) {
          case 0:
            if (!(fb || busy)) {
              _context10.n = 1;
              break;
            }
            return _context10.a(2);
          case 1:
            setBusy(true);
            setSel(o);
            _context10.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'mc',
              question_text: q.id || q.latin,
              pupil_answer: o,
              correct_answer: ansText
            });
          case 2:
            res = _context10.v;
            setFb(res);
            if (res.counts_as_correct) {
              if (!q.failed) addC();
            } else {
              if (!q.failed) {
                addW({
                  latin: q.latin,
                  correct: res.correct_answer || ansText
                });
                setQueue(function (prev) {
                  return [].concat(_toConsumableArray(prev), [_objectSpread(_objectSpread({}, q), {}, {
                    failed: true
                  })]);
                });
              }
            }
            setBusy(false);
          case 3:
            return _context10.a(2);
        }
      }, _callee10);
    }));
    return function pick(_x0) {
      return _ref29.apply(this, arguments);
    };
  }();
  var nx = function nx() {
    resetScroll();
    optsRef.current = null;
    setFb(null);
    setSel(null);
    setTimeLeft(10);
    if (qIdx + 1 >= queue.length) onDone();else setQIdx(function (i) {
      return i + 1;
    });
  };
  useEffect(function () {
    var h = function h(e) {
      if (e.ctrlKey && e.altKey && e.code === "KeyK") {
        e.preventDefault();
        e.stopPropagation();
        if (!(q !== null && q !== void 0 && q.failed)) addC();
        nx();
        return;
      }
      if (e.ctrlKey && e.altKey && e.code === "KeyJ") {
        e.preventDefault();
        e.stopPropagation();
        nx();
        return;
      }
      if (fb && (e.key === 'Enter' || e.code === 'Space' && e.target.tagName !== 'INPUT')) {
        e.preventDefault();
        nx();
      }
      if (!fb) {
        var n = parseInt(e.key);
        if (n >= 1 && n <= 4 && opts[n - 1]) pick(opts[n - 1]);
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  if (!q) return null;
  var isRetry = q.failed;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '12px 40px 4px',
      width: '100%',
      maxWidth: 1000,
      alignSelf: 'center',
      boxSizing: 'border-box'
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "timer-bar",
    style: {
      margin: 0
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "timer-fill",
    style: {
      width: "".concat(timeLeft / 10 * 100, "%"),
      background: fb ? fb.counts_as_correct ? 'var(--green-bright)' : 'var(--red-bright)' : timeLeft <= 3 ? 'var(--red-bright)' : 'var(--blue)',
      transition: fb ? 'none' : 'width 1s linear, background .3s'
    }
  }))), /*#__PURE__*/React.createElement("div", {
    className: "activity-body",
    style: {
      overflowY: 'hidden',
      justifyContent: 'center',
      paddingTop: 36
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 40,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: 8
    }
  }, isRetry && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: '#f97316',
      border: '2px solid #ea580c',
      borderRadius: 10,
      padding: '6px 16px',
      fontWeight: 800,
      color: 'white',
      fontSize: '0.9rem',
      display: 'inline-block'
    }
  }, "Try this again \u2014 you got it wrong before."), (fb === null || fb === void 0 ? void 0 : fb.timeout) && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: 'var(--red-bright)',
      border: '2px solid #b91c1c',
      borderRadius: 10,
      padding: '6px 16px',
      fontWeight: 800,
      color: 'white',
      fontSize: '0.9rem',
      display: 'inline-block'
    }
  }, timeoutBadge())), /*#__PURE__*/React.createElement("div", {
    className: "mc-prompt"
  }, /*#__PURE__*/React.createElement("h2", {
    style: {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      gap: 12
    }
  }, "What does ", renderVocabLatin(q), " mean?")), /*#__PURE__*/React.createElement("div", {
    className: "mc-options"
  }, opts.map(function (o, i) {
    return /*#__PURE__*/React.createElement("button", {
      key: i,
      className: "mc-opt ".concat(fb ? o === ansText ? 'correct' : o === sel ? 'wrong' : '' : ''),
      disabled: busy && !fb,
      onClick: function onClick() {
        return pick(o);
      }
    }, /*#__PURE__*/React.createElement("span", {
      className: "keyhint",
      style: {
        display: 'block',
        marginBottom: 12
      }
    }, "Press ", i + 1), o);
  })), fb && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      minHeight: 80,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: nx,
    style: {
      marginTop: 16
    }
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter / Space"))), !fb && /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 80
    }
  }))));
}

// ── Typed base (reused for vocab and building_parts typed) ────────────────────
function TypedBase(_ref30) {
  var pupil = _ref30.pupil,
    set = _ref30.set,
    items = _ref30.items,
    getPromptTop = _ref30.getPromptTop,
    getKey = _ref30.getKey,
    getPromptSub = _ref30.getPromptSub,
    getSubStyle = _ref30.getSubStyle,
    getCorrect = _ref30.getCorrect,
    isLatin = _ref30.isLatin,
    isPreview = _ref30.isPreview,
    onDone = _ref30.onDone,
    addC = _ref30.addC,
    addW = _ref30.addW,
    pct = _ref30.pct;
  var _useState125 = useState(function () {
      return _toConsumableArray(items);
    }),
    _useState126 = _slicedToArray(_useState125, 2),
    queue = _useState126[0],
    setQueue = _useState126[1];
  var _useState127 = useState(0),
    _useState128 = _slicedToArray(_useState127, 2),
    qIdx = _useState128[0],
    setQIdx = _useState128[1];
  var _useState129 = useState(''),
    _useState130 = _slicedToArray(_useState129, 2),
    ans = _useState130[0],
    setAns = _useState130[1];
  var _useState131 = useState(null),
    _useState132 = _slicedToArray(_useState131, 2),
    fb = _useState132[0],
    setFb = _useState132[1];
  var _useState133 = useState(false),
    _useState134 = _slicedToArray(_useState133, 2),
    retype = _useState134[0],
    setRetype = _useState134[1];
  var _useState135 = useState(''),
    _useState136 = _slicedToArray(_useState135, 2),
    rtAns = _useState136[0],
    setRtAns = _useState136[1];
  var _useState137 = useState(null),
    _useState138 = _slicedToArray(_useState137, 2),
    rtFb = _useState138[0],
    setRtFb = _useState138[1];
  var _useState139 = useState(false),
    _useState140 = _slicedToArray(_useState139, 2),
    busy = _useState140[0],
    setBusy = _useState140[1];
  var inRef = useRef();
  var rtRef = useRef();
  var q = queue[qIdx];
  var correct = q ? getCorrect(q) : '';
  useEffect(function () {
    var _inRef$current, _rtRef$current;
    if (!fb) (_inRef$current = inRef.current) === null || _inRef$current === void 0 || _inRef$current.focus();
    if (retype) (_rtRef$current = rtRef.current) === null || _rtRef$current === void 0 || _rtRef$current.focus();
  }, [qIdx, fb, retype]);
  var qtype = isLatin ? 'latin_typed' : 'vocab';
  var getKeyFn = getKey || getPromptTop;
  var submit = /*#__PURE__*/function () {
    var _ref31 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee11() {
      var res;
      return _regenerator().w(function (_context11) {
        while (1) switch (_context11.n) {
          case 0:
            if (!(busy || !q)) {
              _context11.n = 1;
              break;
            }
            return _context11.a(2);
          case 1:
            setBusy(true);
            _context11.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: qtype,
              question_text: getKeyFn(q),
              pupil_answer: ans,
              correct_answer: correct
            });
          case 2:
            res = _context11.v;
            setFb(res);
            if (res.counts_as_correct) {
              if (!q.failed) addC();
            } else {
              if (!q.failed) addW({
                latin: getPromptTop(q),
                correct: res.correct_answer || correct
              });
              setQueue(function (prev) {
                return [].concat(_toConsumableArray(prev), [_objectSpread(_objectSpread({}, q), {}, {
                  failed: true
                })]);
              });
              setRetype(true);
            }
            setBusy(false);
          case 3:
            return _context11.a(2);
        }
      }, _callee11);
    }));
    return function submit() {
      return _ref31.apply(this, arguments);
    };
  }();
  var rtSubmit = /*#__PURE__*/function () {
    var _ref32 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee12() {
      var res;
      return _regenerator().w(function (_context12) {
        while (1) switch (_context12.n) {
          case 0:
            if (!busy) {
              _context12.n = 1;
              break;
            }
            return _context12.a(2);
          case 1:
            if (rtAns.trim()) {
              _context12.n = 2;
              break;
            }
            setRtFb('Type your answer first.');
            return _context12.a(2);
          case 2:
            setBusy(true);
            _context12.n = 3;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: qtype,
              question_text: getKeyFn(q),
              pupil_answer: rtAns,
              correct_answer: correct
            });
          case 3:
            res = _context12.v;
            if (res.counts_as_correct) nx();else setRtFb('Not quite. Try again.');
            setBusy(false);
          case 4:
            return _context12.a(2);
        }
      }, _callee12);
    }));
    return function rtSubmit() {
      return _ref32.apply(this, arguments);
    };
  }();
  var nx = function nx() {
    resetScroll();
    setAns('');
    setFb(null);
    setRetype(false);
    setRtAns('');
    setRtFb(null);
    if (qIdx + 1 >= queue.length) onDone();else setQIdx(function (i) {
      return i + 1;
    });
  };
  useEffect(function () {
    var h = function h(e) {
      if (e.ctrlKey && e.altKey && e.code === "KeyK") {
        e.preventDefault();
        e.stopPropagation();
        if (!(q !== null && q !== void 0 && q.failed)) addC();
        nx();
        return;
      }
      if (e.ctrlKey && e.altKey && e.code === "KeyJ") {
        e.preventDefault();
        e.stopPropagation();
        nx();
        return;
      }
      if (e.key === 'Enter') {
        if (retype) rtSubmit();else if (fb && !retype) nx();else if (!fb) submit();
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  var inputStyle = isLatin ? {
    fontFamily: 'Crimson Text, serif',
    fontStyle: 'italic',
    fontSize: '2.2rem'
  } : {};
  var isRetry = q === null || q === void 0 ? void 0 : q.failed;
  if (!q) return null;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 40,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: 8
    }
  }, isRetry && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: '#f97316',
      border: '2px solid #ea580c',
      borderRadius: 10,
      padding: '6px 16px',
      fontWeight: 800,
      color: 'white',
      fontSize: '0.9rem',
      display: 'inline-block'
    }
  }, "Try this again \u2014 you got it wrong before.")), isLatin ? /*#__PURE__*/React.createElement("h1", {
    className: "latin dynamic-latin",
    style: {
      fontSize: String(getPromptTop(q)).length > 15 ? '3rem' : '4.5rem'
    }
  }, getPromptTop(q)) : /*#__PURE__*/React.createElement("div", {
    style: {
      marginBottom: 8,
      textAlign: 'center',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: String(q.latin || '').length > 12 ? '3rem' : '4.5rem',
      fontFamily: 'Crimson Text,serif',
      fontStyle: 'italic',
      fontWeight: 700,
      color: 'var(--dark)'
    }
  }, q.latin), q.display_label && (q.pos === 'pronoun' ? /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: '0.75rem',
      color: '#0D9488',
      fontWeight: 800,
      fontStyle: 'normal',
      marginTop: 6,
      letterSpacing: '0.06em',
      textTransform: 'uppercase'
    }
  }, "(", q.display_label.toUpperCase(), ")") : /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: '0.7em',
      color: 'white',
      fontWeight: 800,
      fontStyle: 'normal',
      marginTop: 6,
      padding: '4px 10px',
      background: '#0D9488',
      borderRadius: 6,
      textTransform: 'uppercase'
    }
  }, q.display_label.toUpperCase()))), getPromptSub && /*#__PURE__*/React.createElement("p", {
    style: getSubStyle || {
      color: 'var(--grey)',
      marginBottom: 8,
      fontWeight: 600,
      fontSize: '1.2rem'
    }
  }, getPromptSub(q)), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 40,
      fontWeight: 700,
      fontSize: '1.3rem',
      marginTop: getPromptSub ? 16 : 0
    }
  }, isLatin ? /*#__PURE__*/React.createElement(React.Fragment, null, "Type the ", /*#__PURE__*/React.createElement("strong", {
    style: {
      color: 'var(--navy)',
      fontSize: '1.4rem'
    }
  }, set.mode === 'infinitives' ? 'infinitive' : set.mode === 'perfects' ? 'perfect' : set.mode === 'ppps' ? 'PPP' : set.mode === 'all_four' ? 'missing part' : 'answer')) : 'Type the English translation'), /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 320,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      width: '100%'
    }
  }, !fb ? /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("input", {
    ref: inRef,
    className: "typed-input",
    style: inputStyle,
    disabled: busy,
    value: ans,
    onChange: function onChange(e) {
      return setAns(e.target.value);
    },
    placeholder: "..."
  }), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: submit,
    style: {
      marginTop: 30
    }
  }, "Check", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter"))) : /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("input", {
    className: "typed-input ".concat(fb.counts_as_correct ? 'ok' : 'bad'),
    style: inputStyle,
    value: ans,
    disabled: true
  }), !retype && /*#__PURE__*/React.createElement("div", {
    className: "feedback anim-fade ".concat(fb.counts_as_correct ? fb.is_typo ? 'warn' : 'ok' : 'bad'),
    style: {
      maxWidth: 800,
      width: '100%',
      boxSizing: 'border-box'
    }
  }, renderText(fb.message)), fb.counts_as_correct && !retype && fb.correct_answer && ans.trim().toLowerCase().replace(/[^a-z0-9 /]/g, '').replace(/\s+/g, ' ').trim() !== fb.correct_answer.trim().toLowerCase().replace(/[^a-z0-9 /]/g, '').replace(/\s+/g, ' ').trim() && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 16,
      padding: '12px 16px',
      background: '#f0fdf4',
      border: '2px solid #16a34a',
      borderRadius: 12,
      textAlign: 'left',
      maxWidth: 800,
      width: '100%'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 700,
      fontSize: '0.8rem',
      color: '#16a34a',
      textTransform: 'uppercase',
      letterSpacing: '0.05em',
      marginBottom: 4
    }
  }, "Ideal answer"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.2rem',
      fontWeight: 800,
      color: 'var(--dark)'
    }
  }, fb.correct_answer)), retype && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 16,
      width: '100%',
      maxWidth: 800,
      padding: '24px',
      background: 'var(--white)',
      border: '2px solid var(--lgrey)',
      borderRadius: 20
    }
  }, (fb === null || fb === void 0 ? void 0 : fb.message) && /*#__PURE__*/React.createElement("div", {
    style: {
      background: 'var(--coral)',
      color: 'white',
      padding: '10px 18px',
      borderRadius: 10,
      fontWeight: 700,
      marginBottom: 20,
      display: 'inline-block',
      fontSize: '1rem'
    }
  }, renderText(fb.message)), /*#__PURE__*/React.createElement("div", {
    style: {
      marginBottom: 24,
      padding: '20px',
      background: '#f0fdf4',
      border: '2px solid #16a34a',
      borderRadius: 16,
      textAlign: 'left',
      userSelect: 'none',
      WebkitUserSelect: 'none'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      fontSize: '0.9rem',
      color: '#16a34a',
      marginBottom: 8,
      textTransform: 'uppercase',
      letterSpacing: '0.05em'
    }
  }, "The correct answer is"), /*#__PURE__*/React.createElement("p", {
    className: isLatin ? 'latin' : '',
    style: {
      fontSize: '1.8rem',
      fontWeight: 800,
      color: 'var(--dark)'
    }
  }, (fb === null || fb === void 0 ? void 0 : fb.correct_answer) || correct)), /*#__PURE__*/React.createElement("input", {
    ref: rtRef,
    className: "typed-input",
    style: _objectSpread(_objectSpread({}, inputStyle), {}, {
      borderColor: rtFb ? 'var(--red-bright)' : ''
    }),
    value: rtAns,
    onChange: function onChange(e) {
      setRtAns(e.target.value);
      setRtFb(null);
    },
    onPaste: function onPaste(e) {
      return e.preventDefault();
    },
    placeholder: "..."
  }), rtFb && /*#__PURE__*/React.createElement("div", {
    style: {
      color: 'var(--red-bright)',
      marginTop: 12,
      fontWeight: 700
    }
  }, rtFb), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-outline",
    disabled: busy,
    onClick: rtSubmit,
    style: {
      marginTop: 20
    }
  }, "Continue", /*#__PURE__*/React.createElement("span", {
    className: "keyhint"
  }, "Enter"))), !retype && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary anim-fade",
    disabled: busy,
    onClick: nx,
    style: {
      marginTop: 30
    }
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")))))));
}
function VocabTyped(_ref33) {
  var pupil = _ref33.pupil,
    set = _ref33.set,
    items = _ref33.items,
    isPreview = _ref33.isPreview,
    onDone = _ref33.onDone,
    addC = _ref33.addC,
    addW = _ref33.addW,
    pct = _ref33.pct;
  return /*#__PURE__*/React.createElement(TypedBase, {
    pupil: pupil,
    set: set,
    items: items,
    isPreview: isPreview,
    onDone: onDone,
    addC: addC,
    addW: addW,
    pct: pct,
    isLatin: false,
    getPromptTop: function getPromptTop(q) {
      return q.latin;
    },
    getKey: function getKey(q) {
      return q.id || q.latin;
    },
    getPromptSub: null,
    getCorrect: function getCorrect(q) {
      return q.english[0];
    }
  });
}

// ── Helper: render a principal part with coloured ending ─────────────────────
// partIdx: 0=present, 1=infinitive, 2=perfect, 3=PPP
var renderPartWithColor = function renderPartWithColor(form, partIdx) {
  if (!form) return form;
  if (partIdx === 0) {
    // present — colour the final -o blue
    return /*#__PURE__*/React.createElement(React.Fragment, null, form.slice(0, -1), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--blue)',
        fontWeight: 700
      }
    }, form.slice(-1)));
  }
  if (partIdx === 1) {
    // infinitive — colour the final -re coral (consistent across all conjugations)
    return /*#__PURE__*/React.createElement(React.Fragment, null, form.slice(0, -2), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--coral)',
        fontWeight: 700
      }
    }, "re"));
  }
  if (partIdx === 2) {
    // perfect — colour [marker]+i
    var pm = form.match(/^(.*?)([vsux])(i)$/);
    if (pm) return /*#__PURE__*/React.createElement(React.Fragment, null, pm[1], /*#__PURE__*/React.createElement("span", {
      style: {
        color: '#7C3AED',
        fontWeight: 700
      }
    }, pm[2]), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--blue)',
        fontWeight: 700
      }
    }, "i"));
    if (form.endsWith('i')) return /*#__PURE__*/React.createElement(React.Fragment, null, form.slice(0, -1), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--blue)',
        fontWeight: 700
      }
    }, "i"));
    return form;
  }
  if (partIdx === 3) {
    // PPP — colour -tus/-sus gold
    var _pm = form.match(/^(.*?)(tus|sus)$/);
    if (_pm) return /*#__PURE__*/React.createElement(React.Fragment, null, _pm[1], /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--gold)',
        fontWeight: 700
      }
    }, _pm[2]));
    return form;
  }
  return form;
};

// ── Building Parts Pattern Screen ─────────────────────────────────────────────
function BPPattern(_ref34) {
  var set = _ref34.set,
    onDone = _ref34.onDone;
  var ps = set.pattern_screen;
  useEffect(function () {
    resetScroll();
  }, []);
  useEffect(function () {
    var h = function h(e) {
      if (e.key === 'Enter') onDone();
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  }, [onDone]);
  if (!ps) {
    onDone();
    return null;
  }

  // ── All-verbs grouped display ─────────────────────────────────────────────
  var mode = set.mode;
  var allVerbs = set.verbs || [];

  // Classify a verb into its pattern group
  var grpKey = function grpKey(v) {
    if (mode === 'perfects') {
      var pf = v.perfect;
      if (!pf) return 'none';
      if (/[aeiou]vi$/.test(pf)) return 'v';
      if (/ui$/.test(pf)) return 'u';
      if (/xi$/.test(pf)) return 'x';
      if (/[^x]si$/.test(pf) || /ssi$/.test(pf)) return 's';
      return 'str';
    }
    if (mode === 'ppps') {
      // Simplified: all -tus variants (atus/itus/etus/consonant-tus) → 'tus'; -sus/-xus → 'sus'; no PPP → 'none'
      var p = v.ppp;
      if (!p) return 'none';
      if (p.endsWith('sus') || p.endsWith('xus')) return 'sus';
      if (p.endsWith('tus')) return 'tus'; // atus, itus, etus, or consonant-stem tus — all the same marker
      return 'tus'; // fallback: any other form still shows under tus group
    }
    return 'all'; // infinitives: flat list
  };
  var GRP = {
    v: {
      label: 'perfect marker: -v-',
      color: 'var(--blue)'
    },
    u: {
      label: 'perfect marker: -u-',
      color: 'var(--gold)'
    },
    x: {
      label: 'perfect marker: -x-',
      color: 'var(--coral)'
    },
    s: {
      label: 'perfect marker: -s-',
      color: 'var(--green-bright)'
    },
    str: {
      label: 'strong / vowel-change',
      color: 'var(--navy)'
    },
    none: {
      label: 'no perfect / no PPP',
      color: 'var(--lgrey)'
    },
    tus: {
      label: 'PPP marker: -tus-',
      color: 'var(--blue)'
    },
    sus: {
      label: 'PPP marker: -sus-',
      color: 'var(--gold)'
    },
    other: {
      label: 'other',
      color: 'var(--grey)'
    },
    all: {
      label: '',
      color: 'var(--blue)'
    }
  };
  var ORDER = {
    perfects: ['v', 'u', 'x', 's', 'str', 'none'],
    ppps: ['tus', 'sus', 'none']
  };
  var grpMap = {};
  allVerbs.forEach(function (v) {
    var k = grpKey(v);
    if (!grpMap[k]) grpMap[k] = [];
    grpMap[k].push(v);
  });
  var grpOrder = ORDER[mode] || ['all'];
  var groups = grpOrder.filter(function (k) {
    return grpMap[k];
  }).map(function (k) {
    return {
      key: k,
      meta: GRP[k] || GRP.other,
      verbs: grpMap[k]
    };
  });

  // Render the colored part for a verb in the compact list
  var renderCompact = function renderCompact(v) {
    if (mode === 'infinitives') {
      var stem = v.infinitive.slice(0, -2);
      return /*#__PURE__*/React.createElement("span", {
        style: {
          fontFamily: 'Crimson Text,serif',
          fontStyle: 'italic',
          fontWeight: 700
        }
      }, stem, /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--coral)'
        }
      }, "re"));
    }
    if (mode === 'perfects') {
      var pf = v.perfect;
      if (!pf) return /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--grey)',
          fontFamily: 'sans-serif',
          fontStyle: 'normal',
          fontSize: '0.85rem'
        }
      }, "\u2014");
      var st = {
        fontFamily: 'Crimson Text,serif',
        fontStyle: 'italic',
        fontWeight: 700
      };
      // -u- perfect: ends in 'ui' — stem + u(marker) + i(person)
      if (pf.endsWith('ui')) return /*#__PURE__*/React.createElement("span", {
        style: st
      }, pf.slice(0, -2), /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--coral)'
        }
      }, "u"), /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--blue)'
        }
      }, "i"));
      // -v-, -x-, -s-: find marker after a vowel
      var m = pf.match(/^(.*[aeiou])([vsux])(.+)$/);
      if (m) return /*#__PURE__*/React.createElement("span", {
        style: st
      }, m[1], /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--coral)'
        }
      }, m[2]), /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--blue)'
        }
      }, m[3]));
      return /*#__PURE__*/React.createElement("span", {
        style: st
      }, pf);
    }
    if (mode === 'ppps') {
      var ppp = v.ppp;
      if (!ppp) return /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--grey)',
          fontFamily: 'sans-serif',
          fontStyle: 'normal',
          fontSize: '0.85rem'
        }
      }, "no PPP");
      var _m3 = ppp.match(/^(.+?)(atus|itus|etus|sus|xus|tus)$/);
      if (_m3) return /*#__PURE__*/React.createElement("span", {
        style: {
          fontFamily: 'Crimson Text,serif',
          fontStyle: 'italic',
          fontWeight: 700
        }
      }, _m3[1], /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--gold)'
        }
      }, _m3[2]));
      return /*#__PURE__*/React.createElement("span", {
        style: {
          fontFamily: 'Crimson Text,serif',
          fontStyle: 'italic',
          fontWeight: 700
        }
      }, ppp);
    }
    return null;
  };
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: 5
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("div", {
    className: "pattern-box",
    style: {
      maxWidth: 1000
    }
  }, /*#__PURE__*/React.createElement("h3", {
    style: {
      fontSize: '1.6rem',
      marginBottom: 12
    },
    dangerouslySetInnerHTML: {
      __html: renderOrdinals(ps.title || ps.heading)
    }
  }), /*#__PURE__*/React.createElement("p", {
    className: "pattern-rule",
    style: {
      marginBottom: 28
    }
  }, renderText(ps.subtitle || ps.rule)), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 10,
      marginBottom: 20
    }
  }, ps.examples.map(function (e, i) {
    return /*#__PURE__*/React.createElement("div", {
      key: i,
      style: {
        display: 'flex',
        alignItems: 'center',
        gap: 12,
        padding: '10px 0',
        borderBottom: i < ps.examples.length - 1 ? '1px solid var(--lgrey)' : 'none',
        flexWrap: 'wrap'
      }
    }, e.present || e.stem ? /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
      className: "latin",
      style: {
        fontSize: '1.3rem',
        color: 'var(--dark)',
        whiteSpace: 'nowrap'
      }
    }, function () {
      var pr = e.present || e.stem + 'o';
      return /*#__PURE__*/React.createElement(React.Fragment, null, pr.slice(0, -1), /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--blue)'
        }
      }, pr.slice(-1)));
    }()), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--lgrey)',
        fontSize: '1.2rem'
      }
    }, "\u2192")) : null, (e.infinitive || e.inf) && /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
      className: "latin",
      style: {
        fontSize: '1.3rem',
        color: 'var(--dark)',
        whiteSpace: 'nowrap'
      }
    }, (e.infinitive || e.inf).slice(0, -2), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--coral)'
      }
    }, "re")), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--lgrey)',
        fontSize: '1.2rem'
      }
    }, "\u2192")), e.perfect && /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
      className: "latin",
      style: {
        fontSize: '1.3rem',
        color: 'var(--dark)',
        fontWeight: 700,
        whiteSpace: 'nowrap'
      }
    }, function () {
      // Highlight the perfect-tense marker: -v- for 1st conj,
      // -s- for 3rd, -u- for 2nd. We find the last v/s/u before
      // the final -i and colour-highlight it in purple.
      var pf = e.perfect;
      var m = pf.match(/^(.*?)([vsux])(i|isti|it|imus|istis|erunt)$/);
      if (!m) return pf;
      return /*#__PURE__*/React.createElement(React.Fragment, null, m[1], /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--coral)'
        }
      }, m[2]), /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--blue)'
        }
      }, m[3]));
    }()), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--lgrey)',
        fontSize: '1.2rem'
      }
    }, "\u2192")), /*#__PURE__*/React.createElement("span", {
      className: "latin",
      style: {
        fontSize: '1.3rem',
        fontWeight: 700,
        whiteSpace: 'nowrap'
      }
    }, function () {
      var stem = e.full.slice(0, e.full.length - e.ending.length);
      var decl = e.declension && /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--grey)',
          fontWeight: 400,
          fontSize: '1rem'
        }
      }, " ", e.declension);
      if (e.ending === 'tus' || e.ending === 'sus') return /*#__PURE__*/React.createElement(React.Fragment, null, stem, /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--gold)',
          fontWeight: 700
        }
      }, e.ending), decl);
      if (e.ending === 're' || e.ending === 'ere') return /*#__PURE__*/React.createElement(React.Fragment, null, stem, /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--coral)',
          fontWeight: 700
        }
      }, e.ending), decl);
      // Perfect endings: split marker + person-ending -i
      var pm = e.ending.match(/^([^i])(i)$/);
      if (pm) return /*#__PURE__*/React.createElement(React.Fragment, null, stem, /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--coral)',
          fontWeight: 700
        }
      }, pm[1]), /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--blue)',
          fontWeight: 700
        }
      }, "i"), decl);
      if (e.ending === 'i') return /*#__PURE__*/React.createElement(React.Fragment, null, stem, /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--blue)',
          fontWeight: 700
        }
      }, "i"), decl);
      // Fallback (multi-char endings like vi handled above; anything else coral)
      return /*#__PURE__*/React.createElement(React.Fragment, null, stem, /*#__PURE__*/React.createElement("span", {
        style: {
          color: 'var(--coral)',
          fontWeight: 700
        }
      }, e.ending), decl);
    }()), /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--grey)',
        fontSize: '0.95rem',
        fontStyle: 'italic',
        marginLeft: 4
      }
    }, "- ", e.english));
  })), (ps.footnote || ps.note) && /*#__PURE__*/React.createElement("p", {
    className: "pattern-note"
  }, renderTextWithKey(ps.footnote || ps.note)), allVerbs.length > 0 && (mode === 'perfects' || mode === 'ppps') && /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 32,
      width: '100%'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 900,
      fontSize: '0.88rem',
      color: 'var(--navy)',
      textTransform: 'uppercase',
      letterSpacing: '0.06em',
      marginBottom: 18,
      borderBottom: '2px solid var(--lgrey)',
      paddingBottom: 8
    }
  }, "All ", allVerbs.length, " verbs in this set"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexWrap: 'wrap',
      gap: 32,
      alignItems: 'flex-start'
    }
  }, groups.map(function (g) {
    return /*#__PURE__*/React.createElement("div", {
      key: g.key,
      style: {
        display: 'inline-grid',
        gridTemplateColumns: 'auto 22px auto',
        alignItems: 'stretch',
        gap: '0 16px'
      }
    }, /*#__PURE__*/React.createElement("div", {
      style: {
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        padding: '8px 0',
        textAlign: 'right',
        gap: 6
      }
    }, g.verbs.map(function (v, vi) {
      return /*#__PURE__*/React.createElement("span", {
        key: vi,
        style: {
          display: 'inline-flex',
          alignItems: 'baseline',
          justifyContent: 'flex-end',
          gap: 8,
          fontFamily: 'Crimson Text,serif',
          fontStyle: 'italic',
          fontWeight: 700,
          color: 'var(--dark)',
          fontSize: '1.2rem',
          lineHeight: 1.35
        }
      }, v.present, /*#__PURE__*/React.createElement("span", {
        style: {
          fontFamily: 'var(--font-sans)',
          fontStyle: 'normal',
          fontWeight: 600,
          color: 'var(--grey)',
          fontSize: '0.82rem'
        }
      }, mode === 'perfects' ? v.perfect : mode === 'ppps' ? v.ppp : v.infinitive));
    })), /*#__PURE__*/React.createElement("svg", {
      viewBox: "0 0 22 100",
      preserveAspectRatio: "none",
      "aria-hidden": "true",
      style: {
        height: 'auto',
        width: 22,
        color: 'var(--dark)',
        alignSelf: 'stretch'
      }
    }, /*#__PURE__*/React.createElement("path", {
      d: "M 4 2 C 14 2, 14 2, 14 12 L 14 44 C 14 50, 16 50, 21 50 C 16 50, 14 50, 14 56 L 14 88 C 14 98, 14 98, 4 98",
      fill: "none",
      stroke: "currentColor",
      strokeWidth: "2.4",
      strokeLinecap: "round",
      strokeLinejoin: "round",
      vectorEffect: "non-scaling-stroke"
    })), /*#__PURE__*/React.createElement("div", {
      style: {
        alignSelf: 'center'
      }
    }, g.key !== 'all' && /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("p", {
      style: {
        font: '800 .75rem/1 var(--font-sans)',
        color: 'var(--grey)',
        textTransform: 'uppercase',
        letterSpacing: '.08em',
        margin: '0 0 4px'
      }
    }, "marker"), /*#__PURE__*/React.createElement("p", {
      style: {
        fontFamily: 'Crimson Text,serif',
        fontStyle: 'italic',
        fontWeight: 700,
        color: g.meta.color,
        fontSize: '2rem',
        lineHeight: 1,
        margin: 0
      }
    }, g.key === 'str' || g.key === 'other' || g.key === 'none' ? /*#__PURE__*/React.createElement("span", {
      style: {
        fontFamily: 'var(--font-sans)',
        fontStyle: 'normal',
        fontSize: '0.95rem',
        fontWeight: 800,
        color: g.meta.color,
        lineHeight: 1.3,
        display: 'block',
        maxWidth: 130
      }
    }, g.meta.label) : /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
      style: {
        opacity: .55
      }
    }, "-"), g.key, /*#__PURE__*/React.createElement("span", {
      style: {
        opacity: .55
      }
    }, "-"))))));
  })))), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    autoFocus: true,
    onClick: onDone,
    style: {
      marginTop: 28
    }
  }, "I'm ready", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")))));
}

// ── Building Parts FC (flashcard phase) ───────────────────────────────────────
// For mode=infinitives: shows present / [blank] using the gap-fill visual
// For mode=perfects: shows present / infinitive / [blank]
// For mode=ppps: shows present / infinitive / perfect / [blank]
// FC here just shows the answer - no rating, just flip and move on
function BPFC(_ref35) {
  var pupil = _ref35.pupil,
    set = _ref35.set,
    verbs = _ref35.verbs,
    isPreview = _ref35.isPreview,
    onDone = _ref35.onDone,
    pct = _ref35.pct;
  var _useState141 = useState(function () {
      return _toConsumableArray(verbs);
    }),
    _useState142 = _slicedToArray(_useState141, 2),
    queue = _useState142[0],
    setQueue = _useState142[1];
  var _useState143 = useState(0),
    _useState144 = _slicedToArray(_useState143, 2),
    qIdx = _useState144[0],
    setQIdx = _useState144[1];
  var _useState145 = useState(false),
    _useState146 = _slicedToArray(_useState145, 2),
    rev = _useState146[0],
    setRev = _useState146[1];
  var _useState147 = useState(false),
    _useState148 = _slicedToArray(_useState147, 2),
    busy = _useState148[0],
    setBusy = _useState148[1];
  var _useState149 = useState(''),
    _useState150 = _slicedToArray(_useState149, 2),
    exitCls = _useState150[0],
    setExitCls = _useState150[1];
  var _useState151 = useState(false),
    _useState152 = _slicedToArray(_useState151, 2),
    entering = _useState152[0],
    setEntering = _useState152[1];
  var _useState153 = useState(0),
    _useState154 = _slicedToArray(_useState153, 2),
    doneCount = _useState154[0],
    setDoneCount = _useState154[1];
  var v = queue[qIdx];
  if (!v) {
    onDone();
    return null;
  }
  var mode = set.mode;
  var isAllFour = mode === 'all_four';
  var known = set.show_parts_so_far || 1;
  var labels = ['present', 'infinitive', 'perfect', 'PPP'];
  var shownParts = [];
  if (isAllFour) {
    shownParts.push(v.present); // front shows only present
  } else {
    for (var i = 0; i < known; i++) {
      var vals = [v.present, v.infinitive, v.perfect, v.ppp];
      if (vals[i] !== null && vals[i] !== undefined) shownParts.push(vals[i]);
    }
  }
  var back = mode === 'infinitives' ? v.infinitive : mode === 'perfects' ? v.perfect : v.ppp;
  var backEng = mode === 'infinitives' ? v.eng_infinitive : mode === 'perfects' ? v.eng_perfect : v.eng_ppp;
  var noPPP = mode === 'ppps' && v.ppp === null;
  // all_four reveal parts: the 3 parts beyond the present
  var allFourReveal = isAllFour ? [{
    part: v.infinitive,
    eng: v.eng_infinitive,
    idx: 1
  }, {
    part: v.perfect,
    eng: v.eng_perfect,
    idx: 2
  }, {
    part: v.ppp,
    eng: v.eng_ppp,
    idx: 3
  }] : [];
  var rate = /*#__PURE__*/function () {
    var _ref36 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee13(r) {
      var newQLen;
      return _regenerator().w(function (_context13) {
        while (1) switch (_context13.n) {
          case 0:
            if (!busy) {
              _context13.n = 1;
              break;
            }
            return _context13.a(2);
          case 1:
            setBusy(true);
            if (isPreview) {
              _context13.n = 2;
              break;
            }
            _context13.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'flashcard_rating',
              question_text: v.present,
              pupil_answer: r
            });
          case 2:
            setExitCls(r === 'got_it' ? 'fc-exit-right' : 'fc-exit-left');
            newQLen = queue.length + (r === 'again' ? 1 : 0);
            if (r === 'again') setQueue(function (q) {
              var next = _toConsumableArray(q);
              next.push(_objectSpread(_objectSpread({}, v), {}, {
                revisit: true
              }));
              return next;
            });else setDoneCount(function (d) {
              return d + 1;
            });
            setTimeout(function () {
              setExitCls('');
              setRev(false);
              setBusy(false);
              if (qIdx + 1 >= newQLen) onDone();else {
                setQIdx(function (i) {
                  return i + 1;
                });
                setEntering(true);
                setTimeout(function () {
                  return setEntering(false);
                }, 230);
              }
            }, 270);
          case 3:
            return _context13.a(2);
        }
      }, _callee13);
    }));
    return function rate(_x1) {
      return _ref36.apply(this, arguments);
    };
  }();
  useEffect(function () {
    var h = function h(e) {
      if (e.code === 'Space') {
        e.preventDefault();
        if (!rev) setRev(true);else rate('got_it');
        return;
      }
      if (rev && e.key === '1') rate('again');
      if (rev && e.key === '2') rate('got_it');
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  var bpFreshInQueue = queue.slice(qIdx).filter(function (c) {
    return !c.revisit;
  }).length;
  var bpHardInQueue = queue.slice(qIdx + 1).filter(function (c) {
    return c.revisit;
  }).length;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 16,
      fontWeight: 700,
      fontSize: '1.2rem',
      textAlign: 'center',
      width: '100%'
    }
  }, isAllFour ? /*#__PURE__*/React.createElement(React.Fragment, null, "What are all the ", /*#__PURE__*/React.createElement("strong", {
    style: {
      color: 'var(--navy)'
    }
  }, "principal parts"), " of this verb?") : /*#__PURE__*/React.createElement(React.Fragment, null, "What is the ", /*#__PURE__*/React.createElement("strong", {
    style: {
      color: 'var(--navy)'
    }
  }, labels[known]), " of this verb?")), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'flex-start',
      gap: 20,
      width: '100%',
      maxWidth: 1000,
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement(CardPile, {
    count: bpFreshInQueue,
    hardCount: bpHardInQueue,
    side: "left"
  }), /*#__PURE__*/React.createElement("div", {
    className: "".concat(exitCls).concat(entering ? ' fc-enter' : ''),
    style: {
      flex: 1,
      minWidth: 0,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'center',
      gap: 16,
      marginBottom: 20,
      flexWrap: 'wrap',
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: 'center'
    }
  }, /*#__PURE__*/React.createElement("span", {
    className: "part-chip"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      whiteSpace: 'nowrap'
    }
  }, renderPartWithColor(shownParts[0], 0))), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      fontSize: '0.85rem',
      marginTop: 4,
      fontStyle: 'italic'
    }
  }, v.eng_present)), isAllFour ? /* all_four mode: show 3 blanks on front, reveal all 3 on flip */
  allFourReveal.map(function (r, ri) {
    return /*#__PURE__*/React.createElement(React.Fragment, {
      key: ri
    }, /*#__PURE__*/React.createElement("span", {
      className: "part-sep"
    }, "/"), /*#__PURE__*/React.createElement("div", {
      style: {
        textAlign: 'center'
      }
    }, r.part === null ? /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
      className: "part-chip",
      style: {
        borderColor: 'var(--grey)',
        color: 'var(--grey)',
        fontStyle: 'normal',
        fontSize: '1rem'
      }
    }, rev ? 'no PPP' : '?'), rev && /*#__PURE__*/React.createElement("p", {
      className: "anim-fade",
      style: {
        color: 'var(--grey)',
        fontSize: '0.85rem',
        marginTop: 4,
        fontStyle: 'italic'
      }
    }, "This verb has no PPP")) : /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
      className: "part-chip",
      style: {
        borderColor: 'var(--blue)',
        color: rev ? '#1a73e8' : 'var(--blue)'
      }
    }, rev ? /*#__PURE__*/React.createElement("span", {
      style: {
        whiteSpace: 'nowrap'
      }
    }, renderPartWithColor(r.part, r.idx)) : '?'), rev && /*#__PURE__*/React.createElement("p", {
      className: "anim-fade",
      style: {
        color: 'var(--grey)',
        fontSize: '0.85rem',
        marginTop: 4,
        fontStyle: 'italic'
      }
    }, r.eng))));
  }) :
  /*#__PURE__*/
  /* single-part modes: show already-known parts then one blank */
  React.createElement(React.Fragment, null, shownParts.slice(1).map(function (p, i) {
    return /*#__PURE__*/React.createElement(React.Fragment, {
      key: i
    }, /*#__PURE__*/React.createElement("span", {
      className: "part-sep"
    }, "/"), /*#__PURE__*/React.createElement("div", {
      style: {
        textAlign: 'center'
      }
    }, /*#__PURE__*/React.createElement("span", {
      className: "part-chip"
    }, /*#__PURE__*/React.createElement("span", {
      style: {
        whiteSpace: 'nowrap'
      }
    }, renderPartWithColor(p, i + 1))), /*#__PURE__*/React.createElement("p", {
      style: {
        color: 'var(--grey)',
        fontSize: '0.85rem',
        marginTop: 4,
        fontStyle: 'italic'
      }
    }, i === 0 ? v.eng_infinitive : i === 1 ? v.eng_perfect : v.eng_ppp)));
  }), /*#__PURE__*/React.createElement("span", {
    className: "part-sep"
  }, "/"), /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: 'center'
    }
  }, noPPP ? /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
    className: "part-chip",
    style: {
      borderColor: 'var(--grey)',
      color: 'var(--grey)',
      fontStyle: 'normal',
      fontSize: '1rem'
    }
  }, rev ? 'no PPP' : '?'), rev && /*#__PURE__*/React.createElement("p", {
    className: "anim-fade",
    style: {
      color: 'var(--grey)',
      fontSize: '0.85rem',
      marginTop: 4,
      fontStyle: 'italic'
    }
  }, "This verb has no PPP")) : /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
    className: "part-chip",
    style: {
      borderColor: 'var(--blue)',
      color: rev ? '#1a73e8' : 'var(--blue)'
    }
  }, rev ? /*#__PURE__*/React.createElement("span", {
    style: {
      whiteSpace: 'nowrap'
    }
  }, renderPartWithColor(back, known)) : '?'), rev && /*#__PURE__*/React.createElement("p", {
    className: "anim-fade",
    style: {
      color: 'var(--grey)',
      fontSize: '0.85rem',
      marginTop: 4,
      fontStyle: 'italic'
    }
  }, backEng)))))), /*#__PURE__*/React.createElement(CardPile, {
    count: doneCount,
    side: "right"
  })), rev ? /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      display: 'flex',
      gap: 32,
      marginTop: 24
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-grey",
    disabled: busy,
    onClick: function onClick() {
      return rate('again');
    }
  }, "Hard", /*#__PURE__*/React.createElement("span", {
    className: "keyhint"
  }, "Press 1")), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: function onClick() {
      return rate('got_it');
    }
  }, "Easy", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Press 2"))) : /*#__PURE__*/React.createElement("p", {
    style: {
      marginTop: 24,
      color: 'var(--grey)',
      fontSize: '1.3rem',
      fontWeight: 700
    }
  }, "Press SPACE to reveal"), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 16,
      display: 'flex',
      gap: 12,
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: '0.85rem',
      fontWeight: 700,
      color: 'var(--lgrey)'
    }
  }, "Card ", qIdx + 1, " of ", queue.length), /*#__PURE__*/React.createElement("div", {
    style: {
      width: 160,
      height: 5,
      background: 'var(--lgrey)',
      borderRadius: 3,
      overflow: 'hidden'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      width: "".concat((qIdx + 1) / Math.max(queue.length, 1) * 100, "%"),
      height: '100%',
      background: 'var(--blue)',
      borderRadius: 3,
      transition: 'width .3s'
    }
  }))))));
}

// ── Building Parts MC (MCQ phase between FC and Typed) ───────────────────────
// Shows known parts + blank chip, then 4 Latin MC options (correct + 3 distractors).
// No timer; marks correct/wrong like VocabMC.
function BPMC(_ref37) {
  var pupil = _ref37.pupil,
    set = _ref37.set,
    verbs = _ref37.verbs,
    isPreview = _ref37.isPreview,
    onDone = _ref37.onDone,
    addC = _ref37.addC,
    addW = _ref37.addW,
    pct = _ref37.pct;
  var _useState155 = useState(function () {
      return _toConsumableArray(verbs);
    }),
    _useState156 = _slicedToArray(_useState155, 2),
    queue = _useState156[0],
    setQueue = _useState156[1];
  var _useState157 = useState(0),
    _useState158 = _slicedToArray(_useState157, 2),
    qIdx = _useState158[0],
    setQIdx = _useState158[1];
  var _useState159 = useState(null),
    _useState160 = _slicedToArray(_useState159, 2),
    sel = _useState160[0],
    setSel = _useState160[1];
  var _useState161 = useState(null),
    _useState162 = _slicedToArray(_useState161, 2),
    fb = _useState162[0],
    setFb = _useState162[1];
  var _useState163 = useState(false),
    _useState164 = _slicedToArray(_useState163, 2),
    busy = _useState164[0],
    setBusy = _useState164[1];
  var v = queue[qIdx];
  if (!v) {
    onDone();
    return null;
  }
  var mode = set.mode;
  var known = set.show_parts_so_far || 1;
  var isAllFour = mode === 'all_four';
  var labels = ['present', 'infinitive', 'perfect', 'PPP'];
  // For all_four: randomly assign one gap position per verb (stable per qIdx)
  var gapPos = set.gap_positions || [1, 2, 3];
  var assignedPosRef = useRef({});
  if (!(qIdx in assignedPosRef.current)) {
    // pick a random available gap position for this verb
    var vals = [v.present, v.infinitive, v.perfect, v.ppp];
    var available = gapPos.filter(function (g) {
      return vals[g] != null;
    });
    assignedPosRef.current[qIdx] = available[Math.floor(Math.random() * available.length)] || gapPos[0];
  }
  var allFourPos = assignedPosRef.current[qIdx] || 2; // which part to quiz
  var shownParts = [];
  if (isAllFour) {
    // Show present and all parts up to (but not including) the quizzed one
    for (var i = 0; i < allFourPos; i++) {
      var _vals = [v.present, v.infinitive, v.perfect, v.ppp];
      if (_vals[i] != null) shownParts.push(_vals[i]);
    }
  } else {
    for (var _i = 0; _i < known; _i++) {
      var _vals2 = [v.present, v.infinitive, v.perfect, v.ppp];
      if (_vals2[_i] != null) shownParts.push(_vals2[_i]);
    }
  }
  var getPartByPos = function getPartByPos(u, pos) {
    return [u.present, u.infinitive, u.perfect, u.ppp][pos];
  };
  var back = isAllFour ? getPartByPos(v, allFourPos) : mode === 'infinitives' ? v.infinitive : mode === 'perfects' ? v.perfect : v.ppp;
  var backLabel = isAllFour ? labels[allFourPos] : labels[known];
  var noPPP = !isAllFour && mode === 'ppps' && v.ppp === null;
  // Generate options once per question
  var optsRef = useRef(null);
  if (optsRef.current === null || optsRef.current.qIdx !== qIdx) {
    var correct = back;
    var pos = isAllFour ? allFourPos : known;
    var others = shuffleOnce(verbs.filter(function (u) {
      return u !== v && getPartByPos(u, pos) !== correct;
    }));
    var ds = [];
    var _iterator3 = _createForOfIteratorHelper(others),
      _step3;
    try {
      for (_iterator3.s(); !(_step3 = _iterator3.n()).done;) {
        var u = _step3.value;
        var d = getPartByPos(u, pos);
        if (d && d !== correct && !ds.includes(d) && ds.length < 3) ds.push(d);
      }
    } catch (err) {
      _iterator3.e(err);
    } finally {
      _iterator3.f();
    }
    optsRef.current = {
      qIdx: qIdx,
      opts: shuffleOnce([correct].concat(ds)),
      pos: pos
    };
  }
  var opts = optsRef.current.opts;
  var quizPos = optsRef.current.pos || known;
  var pick = /*#__PURE__*/function () {
    var _ref38 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee14(o) {
      var res;
      return _regenerator().w(function (_context14) {
        while (1) switch (_context14.n) {
          case 0:
            if (!(fb || busy || noPPP)) {
              _context14.n = 1;
              break;
            }
            return _context14.a(2);
          case 1:
            setBusy(true);
            setSel(o);
            _context14.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'mc',
              question_text: "".concat(backLabel, " of ").concat(v.present),
              pupil_answer: o,
              correct_answer: back
            });
          case 2:
            res = _context14.v;
            setFb(res);
            if (res.counts_as_correct) {
              if (!v.failed) addC();
            } else {
              if (!v.failed) addW({
                latin: v.present,
                correct: back
              });
              setQueue(function (prev) {
                return [].concat(_toConsumableArray(prev), [_objectSpread(_objectSpread({}, v), {}, {
                  failed: true
                })]);
              });
            }
            setBusy(false);
          case 3:
            return _context14.a(2);
        }
      }, _callee14);
    }));
    return function pick(_x10) {
      return _ref38.apply(this, arguments);
    };
  }();
  var nx = function nx() {
    resetScroll();
    optsRef.current = null;
    setSel(null);
    setFb(null);
    if (qIdx + 1 >= queue.length) onDone();else setQIdx(function (i) {
      return i + 1;
    });
  };
  useEffect(function () {
    // auto-advance for no-PPP verbs
    if (noPPP && !fb) {
      var t = setTimeout(function () {
        if (!v.failed) addC();
        nx();
      }, 1200);
      return function () {
        return clearTimeout(t);
      };
    }
  }, [qIdx, noPPP]);
  useEffect(function () {
    var h = function h(e) {
      if (e.ctrlKey && e.altKey && e.code === "KeyK") {
        e.preventDefault();
        e.stopPropagation();
        if (!(v !== null && v !== void 0 && v.failed)) addC();
        nx();
        return;
      }
      if (e.ctrlKey && e.altKey && e.code === "KeyJ") {
        e.preventDefault();
        e.stopPropagation();
        nx();
        return;
      }
      if (fb && (e.key === 'Enter' || e.code === 'Space' && e.target.tagName !== 'INPUT')) {
        e.preventDefault();
        nx();
      }
      if (!fb) {
        var n = parseInt(e.key);
        if (n >= 1 && n <= 4 && opts[n - 1]) pick(opts[n - 1]);
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  var isRetry = v.failed;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body",
    style: {
      overflowY: 'hidden',
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 40,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: 8
    }
  }, isRetry && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: '#f97316',
      border: '2px solid #ea580c',
      borderRadius: 10,
      padding: '6px 16px',
      fontWeight: 800,
      color: 'white',
      fontSize: '0.9rem',
      display: 'inline-block'
    }
  }, "Try this again \u2014 you got it wrong before.")), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 16,
      fontWeight: 700,
      fontSize: '1.2rem',
      textAlign: 'center',
      width: '100%'
    }
  }, "What is the ", /*#__PURE__*/React.createElement("strong", {
    style: {
      color: 'var(--navy)'
    }
  }, backLabel), " of this verb?"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'center',
      gap: 16,
      marginBottom: 28,
      flexWrap: 'wrap',
      justifyContent: 'center'
    }
  }, shownParts.map(function (p, i) {
    return /*#__PURE__*/React.createElement(React.Fragment, {
      key: i
    }, i > 0 && /*#__PURE__*/React.createElement("span", {
      className: "part-sep"
    }, "/"), /*#__PURE__*/React.createElement("div", {
      style: {
        textAlign: 'center'
      }
    }, /*#__PURE__*/React.createElement("span", {
      className: "part-chip"
    }, /*#__PURE__*/React.createElement("span", {
      style: {
        whiteSpace: 'nowrap'
      }
    }, renderPartWithColor(p, i))), /*#__PURE__*/React.createElement("p", {
      style: {
        color: 'var(--grey)',
        fontSize: '0.85rem',
        marginTop: 4,
        fontStyle: 'italic'
      }
    }, i === 0 ? v.eng_present : i === 1 ? v.eng_infinitive : i === 2 ? v.eng_perfect : v.eng_ppp)));
  }), /*#__PURE__*/React.createElement("span", {
    className: "part-sep"
  }, "/"), /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: 'center'
    }
  }, noPPP ? /*#__PURE__*/React.createElement("span", {
    className: "part-chip",
    style: {
      borderColor: 'var(--grey)',
      color: 'var(--grey)',
      fontStyle: 'normal',
      fontSize: '1rem'
    }
  }, "no PPP") : /*#__PURE__*/React.createElement("span", {
    className: "part-chip",
    style: {
      borderColor: fb ? fb.counts_as_correct ? '#16a34a' : 'var(--red-bright)' : 'var(--blue)',
      color: fb ? fb.counts_as_correct ? '#16a34a' : 'var(--red-bright)' : 'var(--blue)'
    }
  }, fb ? /*#__PURE__*/React.createElement("span", {
    style: {
      whiteSpace: 'nowrap'
    }
  }, renderPartWithColor(back, quizPos)) : '?'))), !noPPP && /*#__PURE__*/React.createElement("div", {
    className: "mc-options"
  }, opts.map(function (o, i) {
    return /*#__PURE__*/React.createElement("button", {
      key: i,
      className: "mc-opt ".concat(fb ? o === back ? 'correct' : o === sel ? 'wrong' : '' : ''),
      disabled: busy && !fb,
      onClick: function onClick() {
        return pick(o);
      }
    }, /*#__PURE__*/React.createElement("span", {
      className: "keyhint",
      style: {
        display: 'block',
        marginBottom: 12
      }
    }, "Press ", i + 1), /*#__PURE__*/React.createElement("span", {
      style: {
        fontFamily: 'Crimson Text,serif',
        fontStyle: 'italic',
        fontWeight: 700,
        fontSize: '1.4rem'
      }
    }, renderPartWithColor(o, quizPos)));
  })), fb && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      minHeight: 80,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: nx,
    style: {
      marginTop: 16
    }
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter / Space"))), !fb && !noPPP && /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 80
    }
  }))));
}

// ── Building Parts Typed (gap-fill visual for all modes) ─────────────────────
function BPTyped(_ref39) {
  var _qs$idx, _qs$idx2;
  var pupil = _ref39.pupil,
    set = _ref39.set,
    verbs = _ref39.verbs,
    isPreview = _ref39.isPreview,
    onDone = _ref39.onDone,
    addC = _ref39.addC,
    addW = _ref39.addW,
    pct = _ref39.pct;
  var mode = set.mode;
  var labels = ['present', 'infinitive', 'perfect', 'PPP'];
  var known = set.show_parts_so_far || 1;
  var gapPositions = set.gap_positions || [known];

  // all_four_from_present = one question per verb: show present, type all remaining parts
  var isAllFourFromPresent = mode === 'all_four_from_present';
  // all_four = one question per gap position per verb (fill in one missing at a time)
  var isAllFour = mode === 'all_four';
  // all_four_progressive = phase1: gap at pos 2 (all verbs), phase2: gap at pos 3 (ppp verbs only), phase3: all_four_from_present
  var isProgressive = mode === 'all_four_progressive';
  var _useState165 = useState(function () {
      var getP = function getP(v) {
        return [v.present, v.infinitive, v.perfect, v.ppp];
      };
      if (isAllFourFromPresent) {
        // Single question per verb
        return shuffleOnce(verbs.map(function (v) {
          return {
            v: v,
            g: -1
          };
        })); // g=-1 = "all remaining"
      }
      if (isAllFour) {
        // One question per gap position per verb, but only gaps 2 and 3 (perf/PPP)
        return shuffleOnce(verbs.flatMap(function (v) {
          return gapPositions.filter(function (g) {
            return getP(v)[g] != null;
          }).map(function (g) {
            return {
              v: v,
              g: g
            };
          });
        }));
      }
      if (isProgressive) {
        // Phase 1: gap at position 2 (perfect) for all verbs - show present+infinitive, type perfect
        var phase1 = shuffleOnce(verbs.map(function (v) {
          return {
            v: v,
            g: 2,
            phase: 1
          };
        }));
        // Phase 2: gap at position 3 (PPP) for verbs that have a PPP - show present+infinitive+perfect, type PPP
        var phase2 = shuffleOnce(verbs.filter(function (v) {
          return v.ppp !== null;
        }).map(function (v) {
          return {
            v: v,
            g: 3,
            phase: 2
          };
        }));
        // Phase 3: all_four_from_present for all verbs
        var phase3 = shuffleOnce(verbs.map(function (v) {
          return {
            v: v,
            g: -1,
            phase: 3
          };
        }));
        return [].concat(_toConsumableArray(phase1), _toConsumableArray(phase2), _toConsumableArray(phase3));
      }
      return shuffleOnce(verbs.filter(function (v) {
        return mode !== 'ppps' || v.ppp !== null;
      }).map(function (v) {
        return {
          v: v,
          g: known
        };
      }));
    }),
    _useState166 = _slicedToArray(_useState165, 1),
    qs = _useState166[0];
  var _useState167 = useState(0),
    _useState168 = _slicedToArray(_useState167, 2),
    idx = _useState168[0],
    setIdx = _useState168[1];
  var _useState169 = useState(''),
    _useState170 = _slicedToArray(_useState169, 2),
    ans = _useState170[0],
    setAns = _useState170[1];
  var _useState171 = useState(null),
    _useState172 = _slicedToArray(_useState171, 2),
    fb = _useState172[0],
    setFb = _useState172[1];
  var _useState173 = useState(false),
    _useState174 = _slicedToArray(_useState173, 2),
    showReveal = _useState174[0],
    setShowReveal = _useState174[1];
  var _useState175 = useState(false),
    _useState176 = _slicedToArray(_useState175, 2),
    retype = _useState176[0],
    setRetype = _useState176[1];
  var _useState177 = useState(''),
    _useState178 = _slicedToArray(_useState177, 2),
    rtAns = _useState178[0],
    setRtAns = _useState178[1];
  var _useState179 = useState(null),
    _useState180 = _slicedToArray(_useState179, 2),
    rtFb = _useState180[0],
    setRtFb = _useState180[1];
  var _useState181 = useState(false),
    _useState182 = _slicedToArray(_useState181, 2),
    busy = _useState182[0],
    setBusy = _useState182[1];
  var inRef = useRef();
  var rtRef = useRef();
  if (!qs || qs.length === 0) {
    onDone();
    return null;
  }
  var _ref40 = qs[idx] || qs[0],
    v = _ref40.v,
    g = _ref40.g;
  var parts = [v.present, v.infinitive, v.perfect, v.ppp];

  // correct answer string
  var correct;
  if (g === -1) {
    // all_four_from_present or progressive phase 3
    correct = v.ppp ? "".concat(v.infinitive, " ").concat(v.perfect, " ").concat(v.ppp) : "".concat(v.infinitive, " ").concat(v.perfect);
  } else {
    correct = parts[g];
  }

  // For all_four (individual gap) show only up to and including the gap position
  // For all_four_from_present show all 4 (the input handles "remaining" parts)
  var shownCount = isAllFourFromPresent ? 4 : isAllFour ? g + 1 : 4;
  useEffect(function () {
    var _inRef$current2, _rtRef$current2;
    if (!fb) (_inRef$current2 = inRef.current) === null || _inRef$current2 === void 0 || _inRef$current2.focus();
    if (retype) (_rtRef$current2 = rtRef.current) === null || _rtRef$current2 === void 0 || _rtRef$current2.focus();
  }, [idx, fb, retype]);
  var submit = /*#__PURE__*/function () {
    var _ref41 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee15() {
      var res;
      return _regenerator().w(function (_context15) {
        while (1) switch (_context15.n) {
          case 0:
            if (!busy) {
              _context15.n = 1;
              break;
            }
            return _context15.a(2);
          case 1:
            setBusy(true);
            if (!isAllFourMode) {
              _context15.n = 3;
              break;
            }
            _context15.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'all_four_typed',
              question_text: v.present,
              pupil_answer: ans,
              correct_answer: correct
            });
          case 2:
            res = _context15.v;
            _context15.n = 5;
            break;
          case 3:
            _context15.n = 4;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'latin_typed',
              question_text: "".concat(labels[g], " of ").concat(v.present),
              pupil_answer: ans,
              correct_answer: correct
            });
          case 4:
            res = _context15.v;
          case 5:
            setFb(res);
            if (res.counts_as_correct) {
              if (!qs[idx].failed) addC();
            } else {
              if (!qs[idx].failed) addW({
                latin: v.present,
                correct: res.correct_answer
              });
              if (!qs.find(function (q) {
                return q.v === v && q.failed;
              })) {
                qs.push({
                  v: v,
                  g: g,
                  failed: true
                });
              }
              setShowReveal(true);
              setRetype(true);
            }
            setBusy(false);
          case 6:
            return _context15.a(2);
        }
      }, _callee15);
    }));
    return function submit() {
      return _ref41.apply(this, arguments);
    };
  }();
  var rtSubmit = /*#__PURE__*/function () {
    var _ref42 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee16() {
      var qt2, qt2text, res;
      return _regenerator().w(function (_context16) {
        while (1) switch (_context16.n) {
          case 0:
            if (!busy) {
              _context16.n = 1;
              break;
            }
            return _context16.a(2);
          case 1:
            if (rtAns.trim()) {
              _context16.n = 2;
              break;
            }
            setRtFb('Type your answer first.');
            return _context16.a(2);
          case 2:
            setBusy(true);
            qt2 = isAllFourMode ? 'all_four_typed' : 'latin_typed';
            qt2text = isAllFourMode ? v.present : "".concat(labels[g], " of ").concat(v.present);
            _context16.n = 3;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: qt2,
              question_text: qt2text,
              pupil_answer: rtAns,
              correct_answer: correct
            });
          case 3:
            res = _context16.v;
            if (res.counts_as_correct) {
              nx();
            } else setRtFb('Not quite. Check the spelling.');
            setBusy(false);
          case 4:
            return _context16.a(2);
        }
      }, _callee16);
    }));
    return function rtSubmit() {
      return _ref42.apply(this, arguments);
    };
  }();
  var nx = function nx() {
    resetScroll();
    setAns('');
    setFb(null);
    setShowReveal(false);
    setRetype(false);
    setRtAns('');
    setRtFb(null);
    if (idx + 1 >= qs.length) onDone();else setIdx(function (i) {
      return i + 1;
    });
  };
  useEffect(function () {
    var h = function h(e) {
      if (e.key === 'Enter') {
        if (retype) rtSubmit();else if (fb && !retype) nx();else if (!fb) submit();
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  var inputStyle = {
    fontFamily: 'Crimson Text, serif',
    fontStyle: 'italic',
    fontSize: '2.2rem',
    fontWeight: 700
  };
  // all_four_typed (multi-part answer) only for all_four_from_present and progressive phase 3
  // isAllFour mode fills ONE gap at a time using latin_typed, not all_four_typed
  var isAllFourMode = isAllFourFromPresent || isProgressive && g === -1;
  var isProgressiveSingleGap = isProgressive && g >= 0;

  // For progressive phase display: determine show_parts_so_far based on gap position
  var progressiveShownCount = isProgressiveSingleGap ? g === 2 ? 3 : 4 : 4;
  var effectiveShownCount = isAllFour ? 4 : isProgressiveSingleGap ? progressiveShownCount : shownCount;

  // Phase label for progressive mode
  var currentPhase = (_qs$idx = qs[idx]) === null || _qs$idx === void 0 ? void 0 : _qs$idx.phase;
  var phaseLabel = isProgressive ? currentPhase === 1 ? 'Phase 1: Type the perfect' : currentPhase === 2 ? 'Phase 2: Type the PPP' : 'Phase 3: All principal parts' : null;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 40,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: 8
    }
  }, ((_qs$idx2 = qs[idx]) === null || _qs$idx2 === void 0 ? void 0 : _qs$idx2.failed) && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: '#f97316',
      border: '2px solid #ea580c',
      borderRadius: 10,
      padding: '6px 16px',
      fontWeight: 800,
      color: 'white',
      fontSize: '0.9rem',
      display: 'inline-block'
    }
  }, "Try this again \u2014 you got it wrong before.")), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 8,
      fontWeight: 700,
      fontSize: '1.3rem'
    }
  }, isAllFourMode ? /*#__PURE__*/React.createElement(React.Fragment, null, "Type the ", /*#__PURE__*/React.createElement("strong", {
    style: {
      color: 'var(--navy)',
      fontSize: '1.4rem'
    }
  }, "remaining principal parts"), ", in order, separated by spaces:") : /*#__PURE__*/React.createElement(React.Fragment, null, "Type the ", /*#__PURE__*/React.createElement("strong", {
    style: {
      color: 'var(--navy)',
      fontSize: '1.4rem'
    }
  }, labels[g]), ":")), isAllFourMode ? /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 16,
      width: '100%',
      maxWidth: 900
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "parts-row"
  }, /*#__PURE__*/React.createElement("span", {
    className: "part-chip"
  }, /*#__PURE__*/React.createElement("span", null, renderPartWithColor(v.present, 0)), /*#__PURE__*/React.createElement("span", {
    className: "chip-eng"
  }, v.eng_present)), /*#__PURE__*/React.createElement("span", {
    className: "part-sep"
  }, "/"), /*#__PURE__*/React.createElement("span", {
    style: {
      color: 'var(--blue)',
      fontFamily: 'Crimson Text,serif',
      fontStyle: 'italic',
      fontSize: '1.5rem',
      fontWeight: 700
    }
  }, v.ppp ? 'infinitive / perfect / PPP' : 'infinitive / perfect')), /*#__PURE__*/React.createElement("input", {
    ref: inRef,
    className: "gap-input ".concat(fb ? fb.counts_as_correct ? 'ok' : 'bad' : ''),
    value: ans,
    onChange: function onChange(e) {
      return setAns(e.target.value);
    },
    disabled: !!fb,
    placeholder: "...",
    style: _objectSpread(_objectSpread({}, inputStyle), {}, {
      minWidth: 380,
      textAlign: 'left',
      paddingLeft: 24
    })
  }), !v.ppp && !fb && /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '0.9rem',
      color: 'var(--grey)',
      fontStyle: 'italic',
      marginTop: 4
    }
  }, "Note: this verb has no PPP. Type only infinitive and perfect.")) : /*#__PURE__*/React.createElement("div", {
    className: "parts-row"
  }, Array.from({
    length: effectiveShownCount
  }, function (_, i) {
    var engLabels = [v.eng_present, v.eng_infinitive, v.eng_perfect, v.eng_ppp];
    if (i === g) return /*#__PURE__*/React.createElement(React.Fragment, {
      key: i
    }, i > 0 && /*#__PURE__*/React.createElement("span", {
      className: "part-sep"
    }, "/"), /*#__PURE__*/React.createElement("input", {
      ref: inRef,
      className: "gap-input ".concat(fb ? fb.counts_as_correct ? 'ok' : 'bad' : ''),
      value: ans,
      onChange: function onChange(e) {
        return setAns(e.target.value);
      },
      disabled: !!fb,
      placeholder: "...",
      style: inputStyle
    }));
    if (parts[i] === null || parts[i] === undefined) return null;
    return /*#__PURE__*/React.createElement(React.Fragment, {
      key: i
    }, i > 0 && /*#__PURE__*/React.createElement("span", {
      className: "part-sep"
    }, "/"), /*#__PURE__*/React.createElement("span", {
      className: "part-chip"
    }, /*#__PURE__*/React.createElement("span", null, renderPartWithColor(parts[i], i)), /*#__PURE__*/React.createElement("span", {
      className: "chip-eng"
    }, engLabels[i])));
  })), showReveal && /*#__PURE__*/React.createElement("div", {
    className: "full-reveal anim-fade"
  }, (g === -1 ? parts : parts.slice(0, g + 1)).filter(function (p) {
    return p != null;
  }).map(function (p, i) {
    return /*#__PURE__*/React.createElement(React.Fragment, {
      key: i
    }, i > 0 && /*#__PURE__*/React.createElement("span", {
      className: "sep"
    }, "/"), /*#__PURE__*/React.createElement("span", {
      className: "rv"
    }, p));
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 320,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      width: '100%'
    }
  }, !fb ? /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: submit,
    style: {
      marginTop: 20
    }
  }, "Check", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")) : /*#__PURE__*/React.createElement(React.Fragment, null, !retype && /*#__PURE__*/React.createElement("div", {
    className: "feedback anim-fade ".concat(fb.counts_as_correct ? 'ok' : 'bad')
  }, renderText(fb.message)), retype && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 16,
      width: '100%',
      maxWidth: 800,
      padding: '24px',
      background: 'var(--white)',
      border: '2px solid var(--lgrey)',
      borderRadius: 20
    }
  }, (fb === null || fb === void 0 ? void 0 : fb.message) && /*#__PURE__*/React.createElement("div", {
    style: {
      background: 'var(--coral)',
      color: 'white',
      padding: '10px 18px',
      borderRadius: 10,
      fontWeight: 700,
      marginBottom: 20,
      display: 'inline-block',
      fontSize: '1rem'
    }
  }, renderText(fb.message)), /*#__PURE__*/React.createElement("div", {
    style: {
      marginBottom: 24,
      padding: '20px',
      background: '#f0fdf4',
      border: '2px solid #16a34a',
      borderRadius: 16,
      textAlign: 'left',
      userSelect: 'none',
      WebkitUserSelect: 'none'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      fontSize: '0.9rem',
      color: '#16a34a',
      marginBottom: 8,
      textTransform: 'uppercase',
      letterSpacing: '0.05em'
    }
  }, "The correct answer is"), /*#__PURE__*/React.createElement("p", {
    className: "latin",
    style: {
      fontSize: '1.8rem',
      fontWeight: 800,
      color: 'var(--dark)'
    }
  }, correct)), /*#__PURE__*/React.createElement("input", {
    ref: rtRef,
    className: "typed-input",
    style: _objectSpread(_objectSpread({}, inputStyle), {}, {
      borderColor: rtFb ? 'var(--red-bright)' : ''
    }),
    value: rtAns,
    onChange: function onChange(e) {
      setRtAns(e.target.value);
      setRtFb(null);
    },
    onPaste: function onPaste(e) {
      return e.preventDefault();
    },
    placeholder: "..."
  }), rtFb && /*#__PURE__*/React.createElement("div", {
    style: {
      color: 'var(--red-bright)',
      marginTop: 12,
      fontWeight: 700
    }
  }, rtFb), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-outline",
    disabled: busy,
    onClick: rtSubmit,
    style: {
      marginTop: 20
    }
  }, "Continue", /*#__PURE__*/React.createElement("span", {
    className: "keyhint"
  }, "Enter"))), !retype && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary anim-fade",
    disabled: busy,
    onClick: nx,
    style: {
      marginTop: 30
    }
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")))))));
}

// ── Verb Conjugation — principal parts + meaning drill ───────────────────────
// Format: show all parts of a verb with one randomly blanked; also blank meaning.
// Two boxes side by side. Tab switches between them. Both checked on Enter.
// Wrong answers: retype the incorrect box(es) before continuing.

// Generate "having been X" form for PPP meaning acceptance.
// Covers regular English patterns + common irregulars found in the GCSE verb list.
function toPPPMeaning(m) {
  m = m.trim().toLowerCase().replace(/^to /, '');
  var irregs = {
    'give': 'given',
    'write': 'written',
    'find': 'found',
    'take': 'taken',
    'make': 'made',
    'come': 'come',
    'go': 'gone',
    'see': 'seen',
    'put': 'put',
    'set': 'set',
    'let': 'let',
    'cut': 'cut',
    'get': 'got',
    'hold': 'held',
    'tell': 'told',
    'say': 'said',
    'bring': 'brought',
    'lead': 'led',
    'read': 'read',
    'build': 'built',
    'send': 'sent',
    'think': 'thought',
    'stand': 'stood',
    'sit': 'sat',
    'run': 'run',
    'fight': 'fought',
    'catch': 'caught',
    'hear': 'heard',
    'know': 'known',
    'show': 'shown',
    'break': 'broken',
    'choose': 'chosen',
    'fall': 'fallen',
    'speak': 'spoken',
    'steal': 'stolen',
    'wear': 'worn',
    'drive': 'driven',
    'eat': 'eaten',
    'begin': 'begun',
    'sing': 'sung',
    'throw': 'thrown',
    'grow': 'grown',
    'rise': 'risen',
    'win': 'won',
    'hang': 'hung',
    'pay': 'paid',
    'lay': 'laid',
    'leave': 'left',
    'lose': 'lost',
    'keep': 'kept',
    'feel': 'felt',
    'meet': 'met',
    'sell': 'sold',
    'sleep': 'slept',
    'spend': 'spent',
    'teach': 'taught',
    'buy': 'bought',
    'seek': 'sought',
    'flee': 'fled',
    'weep': 'wept',
    'hide': 'hidden',
    'overcome': 'overcome',
    'carry out': 'carried out',
    'set free': 'set free',
    'look after': 'looked after',
    'care for': 'cared for',
    'approach': 'approached',
    'surround': 'surrounded',
    'attack': 'attacked',
    'praise': 'praised',
    'enter': 'entered',
    'free': 'freed',
    'order': 'ordered',
    'command': 'commanded',
    'warn': 'warned',
    'advise': 'advised',
    'carry': 'carried',
    'save': 'saved',
    'sail': 'sailed',
    'live': 'lived',
    'march': 'marched',
    'hurry': 'hurried',
    'walk': 'walked',
    'consider': 'considered',
    'watch': 'watched',
    'supervise': 'supervised',
    'demand': 'demanded',
    'announce': 'announced',
    'greet': 'greeted',
    'prepare': 'prepared',
    'ask': 'asked',
    'beg': 'begged',
    'promise': 'promised',
    'reply': 'replied',
    'remain': 'remained',
    'report': 'reported',
    'shout': 'shouted'
  };
  if (irregs[m]) return "having been ".concat(irregs[m]);
  if (m.endsWith('e')) return "having been ".concat(m, "d");
  if (m.endsWith('y') && m.length > 1 && !'aeiou'.includes(m[m.length - 2])) return "having been ".concat(m.slice(0, -1), "ied");
  return "having been ".concat(m, "ed");
}
function VerbConj(_ref43) {
  var _qs$idx3;
  var pupil = _ref43.pupil,
    set = _ref43.set,
    verbs = _ref43.verbs,
    isPreview = _ref43.isPreview,
    onDone = _ref43.onDone,
    addC = _ref43.addC,
    addW = _ref43.addW,
    pct = _ref43.pct;
  var partLabels = ['present', 'infinitive', 'perfect', 'PPP'];
  var _useState183 = useState(function () {
      return shuffleOnce(verbs.map(function (v) {
        var parts = [v.present, v.infinitive, v.perfect, v.ppp];
        var valid = [1, 2, 3].filter(function (i) {
          return parts[i] != null;
        });
        var g = valid[Math.floor(Math.random() * valid.length)];
        return {
          v: v,
          g: g
        };
      }));
    }),
    _useState184 = _slicedToArray(_useState183, 1),
    qs = _useState184[0];
  var _useState185 = useState(0),
    _useState186 = _slicedToArray(_useState185, 2),
    idx = _useState186[0],
    setIdx = _useState186[1];
  var _useState187 = useState(''),
    _useState188 = _slicedToArray(_useState187, 2),
    partAns = _useState188[0],
    setPartAns = _useState188[1];
  var _useState189 = useState(''),
    _useState190 = _slicedToArray(_useState189, 2),
    meaningAns = _useState190[0],
    setMeaningAns = _useState190[1];
  var _useState191 = useState(null),
    _useState192 = _slicedToArray(_useState191, 2),
    fb = _useState192[0],
    setFb = _useState192[1];
  var _useState193 = useState(false),
    _useState194 = _slicedToArray(_useState193, 2),
    wrongPart = _useState194[0],
    setWrongPart = _useState194[1];
  var _useState195 = useState(false),
    _useState196 = _slicedToArray(_useState195, 2),
    wrongMeaning = _useState196[0],
    setWrongMeaning = _useState196[1];
  var _useState197 = useState(''),
    _useState198 = _slicedToArray(_useState197, 2),
    rtPartAns = _useState198[0],
    setRtPartAns = _useState198[1];
  var _useState199 = useState(''),
    _useState200 = _slicedToArray(_useState199, 2),
    rtMeaningAns = _useState200[0],
    setRtMeaningAns = _useState200[1];
  var _useState201 = useState(null),
    _useState202 = _slicedToArray(_useState201, 2),
    rtFb = _useState202[0],
    setRtFb = _useState202[1];
  var _useState203 = useState(false),
    _useState204 = _slicedToArray(_useState203, 2),
    busy = _useState204[0],
    setBusy = _useState204[1];
  var partRef = useRef();
  var meaningRef = useRef();
  var rtPartRef = useRef();
  var rtMeaningRef = useRef();
  if (!qs || qs.length === 0) {
    onDone();
    return null;
  }
  var _ref44 = qs[idx] || qs[0],
    v = _ref44.v,
    g = _ref44.g;
  var parts = [v.present, v.infinitive, v.perfect, v.ppp];
  var correctPart = parts[g];
  useEffect(function () {
    if (!fb) {
      var _partRef$current;
      (_partRef$current = partRef.current) === null || _partRef$current === void 0 || _partRef$current.focus();
    } else if (wrongPart) {
      var _rtPartRef$current;
      (_rtPartRef$current = rtPartRef.current) === null || _rtPartRef$current === void 0 || _rtPartRef$current.focus();
    } else if (wrongMeaning) {
      var _rtMeaningRef$current;
      (_rtMeaningRef$current = rtMeaningRef.current) === null || _rtMeaningRef$current === void 0 || _rtMeaningRef$current.focus();
    }
  }, [idx, fb, wrongPart, wrongMeaning]);
  var submit = /*#__PURE__*/function () {
    var _ref45 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee17() {
      var _yield$Promise$all, _yield$Promise$all2, partRes, meaningRes, wp, wm;
      return _regenerator().w(function (_context17) {
        while (1) switch (_context17.n) {
          case 0:
            if (!busy) {
              _context17.n = 1;
              break;
            }
            return _context17.a(2);
          case 1:
            setBusy(true);
            _context17.n = 2;
            return Promise.all([post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'latin_typed',
              question_text: "".concat(partLabels[g], " of ").concat(v.present),
              pupil_answer: partAns,
              correct_answer: correctPart
            }), post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'typed',
              question_text: v.present,
              pupil_answer: meaningAns,
              correct_answer: _toConsumableArray(new Set(g === 3 ? [].concat(_toConsumableArray(v.meanings), _toConsumableArray(v.meanings.map(toPPPMeaning))) : v.meanings)).join(', ')
            })]);
          case 2:
            _yield$Promise$all = _context17.v;
            _yield$Promise$all2 = _slicedToArray(_yield$Promise$all, 2);
            partRes = _yield$Promise$all2[0];
            meaningRes = _yield$Promise$all2[1];
            if (!qs[idx].failed) {
              if (partRes.counts_as_correct) addC();else addW({
                latin: v.present,
                correct: correctPart
              });
              if (meaningRes.counts_as_correct) addC();else addW({
                latin: v.present + ' (meaning)',
                correct: v.meanings[0]
              });
            }
            wp = !partRes.counts_as_correct;
            wm = !meaningRes.counts_as_correct;
            if ((wp || wm) && !qs.find(function (q) {
              return q.v === v && q.failed;
            })) qs.push({
              v: v,
              g: g,
              failed: true
            });
            setFb({
              part: partRes,
              meaning: meaningRes
            });
            setWrongPart(wp);
            setWrongMeaning(wm);
            setBusy(false);
          case 3:
            return _context17.a(2);
        }
      }, _callee17);
    }));
    return function submit() {
      return _ref45.apply(this, arguments);
    };
  }();
  var rtSubmit = /*#__PURE__*/function () {
    var _ref46 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee18() {
      var checks, results;
      return _regenerator().w(function (_context18) {
        while (1) switch (_context18.n) {
          case 0:
            if (!busy) {
              _context18.n = 1;
              break;
            }
            return _context18.a(2);
          case 1:
            if (!(wrongPart && !rtPartAns.trim())) {
              _context18.n = 2;
              break;
            }
            setRtFb('Type the missing principal part.');
            return _context18.a(2);
          case 2:
            if (!(wrongMeaning && !rtMeaningAns.trim())) {
              _context18.n = 3;
              break;
            }
            setRtFb('Type the meaning.');
            return _context18.a(2);
          case 3:
            setBusy(true);
            checks = [];
            if (wrongPart) checks.push(post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'latin_typed',
              question_text: "retype ".concat(v.present),
              pupil_answer: rtPartAns,
              correct_answer: correctPart
            }));
            if (wrongMeaning) checks.push(post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'typed',
              question_text: v.present,
              pupil_answer: rtMeaningAns,
              correct_answer: _toConsumableArray(new Set(g === 3 ? [].concat(_toConsumableArray(v.meanings), _toConsumableArray(v.meanings.map(toPPPMeaning))) : v.meanings)).join(', ')
            }));
            _context18.n = 4;
            return Promise.all(checks);
          case 4:
            results = _context18.v;
            if (results.every(function (r) {
              return r.counts_as_correct;
            })) {
              nx();
            } else {
              setRtFb('Not quite — check spelling and try again.');
            }
            setBusy(false);
          case 5:
            return _context18.a(2);
        }
      }, _callee18);
    }));
    return function rtSubmit() {
      return _ref46.apply(this, arguments);
    };
  }();
  var nx = function nx() {
    resetScroll();
    setPartAns('');
    setMeaningAns('');
    setFb(null);
    setWrongPart(false);
    setWrongMeaning(false);
    setRtPartAns('');
    setRtMeaningAns('');
    setRtFb(null);
    if (idx + 1 >= qs.length) onDone();else setIdx(function (i) {
      return i + 1;
    });
  };
  useEffect(function () {
    var h = function h(e) {
      if (e.key === 'Tab' && !fb) {
        var _meaningRef$current, _partRef$current2;
        e.preventDefault();
        if (document.activeElement === partRef.current) (_meaningRef$current = meaningRef.current) === null || _meaningRef$current === void 0 || _meaningRef$current.focus();else (_partRef$current2 = partRef.current) === null || _partRef$current2 === void 0 || _partRef$current2.focus();
      }
      if (e.key === 'Enter') {
        if (fb && (wrongPart || wrongMeaning)) rtSubmit();else if (fb && !wrongPart && !wrongMeaning) nx();else if (!fb) submit();
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  var latinStyle = {
    fontFamily: 'Crimson Text, serif',
    fontStyle: 'italic',
    fontSize: '1.9rem',
    fontWeight: 700
  };
  var engStyle = {
    fontFamily: 'Inter, sans-serif',
    fontStyle: 'normal',
    fontSize: '1.4rem',
    fontWeight: 600
  };
  var cardStyle = {
    display: 'flex',
    alignItems: 'center',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: '4px 0',
    background: 'white',
    borderRadius: 16,
    padding: '22px 28px',
    boxShadow: '0 2px 12px rgba(0,33,71,0.08)',
    border: '2px solid var(--lgrey)',
    width: '100%',
    maxWidth: 960
  };
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 32,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: 6
    }
  }, ((_qs$idx3 = qs[idx]) === null || _qs$idx3 === void 0 ? void 0 : _qs$idx3.failed) && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: '#f97316',
      border: '2px solid #ea580c',
      borderRadius: 10,
      padding: '5px 14px',
      fontWeight: 800,
      color: 'white',
      fontSize: '0.85rem',
      display: 'inline-block'
    }
  }, "Try again \u2014 wrong before.")), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      fontWeight: 700,
      fontSize: '1.05rem',
      marginBottom: 16
    }
  }, "Type the missing ", /*#__PURE__*/React.createElement("strong", {
    style: {
      color: 'var(--navy)'
    }
  }, "principal part"), " and the ", /*#__PURE__*/React.createElement("strong", {
    style: {
      color: 'var(--navy)'
    }
  }, "meaning"), ":"), !fb ? /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 14,
      width: '100%',
      maxWidth: 960
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: cardStyle
  }, parts.map(function (p, i) {
    if (p == null) return null;
    if (i === g) return /*#__PURE__*/React.createElement(React.Fragment, {
      key: i
    }, i > 0 && /*#__PURE__*/React.createElement("span", {
      className: "part-sep"
    }, "/"), /*#__PURE__*/React.createElement("input", {
      ref: partRef,
      className: "gap-input",
      value: partAns,
      onChange: function onChange(e) {
        return setPartAns(e.target.value);
      },
      disabled: !!fb,
      placeholder: "...",
      style: latinStyle
    }));
    return /*#__PURE__*/React.createElement(React.Fragment, {
      key: i
    }, i > 0 && /*#__PURE__*/React.createElement("span", {
      className: "part-sep"
    }, "/"), /*#__PURE__*/React.createElement("span", {
      className: "part-chip"
    }, /*#__PURE__*/React.createElement("span", null, renderPartWithColor(p, i))));
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      margin: '0 14px',
      color: 'var(--lgrey)',
      fontSize: '1.6rem',
      fontWeight: 200,
      lineHeight: 1
    }
  }, "|"), /*#__PURE__*/React.createElement("input", {
    ref: meaningRef,
    className: "gap-input",
    value: meaningAns,
    onChange: function onChange(e) {
      return setMeaningAns(e.target.value);
    },
    disabled: !!fb,
    placeholder: "meaning...",
    style: engStyle
  })), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '0.8rem',
      color: 'var(--grey)',
      fontStyle: 'italic',
      marginTop: 2
    }
  }, "Tab to switch boxes"), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: submit,
    style: {
      marginTop: 6
    }
  }, "Check", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter"))) : /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 14,
      width: '100%',
      maxWidth: 960
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: cardStyle
  }, parts.map(function (p, i) {
    if (p == null) return null;
    var isBlank = i === g;
    var col = isBlank ? fb.part.counts_as_correct ? '#16a34a' : 'var(--coral)' : 'inherit';
    return /*#__PURE__*/React.createElement(React.Fragment, {
      key: i
    }, i > 0 && /*#__PURE__*/React.createElement("span", {
      className: "part-sep"
    }, "/"), /*#__PURE__*/React.createElement("span", {
      className: "part-chip"
    }, /*#__PURE__*/React.createElement("span", {
      style: {
        color: col,
        fontWeight: isBlank ? 800 : 700
      }
    }, renderPartWithColor(p, i))));
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      margin: '0 14px',
      color: 'var(--lgrey)',
      fontSize: '1.6rem',
      fontWeight: 200,
      lineHeight: 1
    }
  }, "|"), /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 700,
      fontSize: '1.3rem',
      color: fb.meaning.counts_as_correct ? '#16a34a' : 'var(--coral)'
    }
  }, (v.meanings || []).join(', '))), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 10,
      flexWrap: 'wrap',
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "feedback ".concat(fb.part.counts_as_correct ? 'ok' : 'bad'),
    style: {
      fontSize: '0.95rem',
      padding: '8px 16px'
    }
  }, fb.part.counts_as_correct ? "\u2713 ".concat(partLabels[g]) : "\u2717 ".concat(partLabels[g], ": ").concat(correctPart)), /*#__PURE__*/React.createElement("div", {
    className: "feedback ".concat(fb.meaning.counts_as_correct ? 'ok' : 'bad'),
    style: {
      fontSize: '0.95rem',
      padding: '8px 16px'
    }
  }, fb.meaning.counts_as_correct ? '✓ meaning' : "\u2717 meaning: ".concat((v.meanings || []).join(', ')))), (wrongPart || wrongMeaning) && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: 'var(--white)',
      border: '2px solid var(--lgrey)',
      borderRadius: 20,
      padding: '22px 28px',
      width: '100%',
      maxWidth: 800
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 700,
      fontSize: '0.95rem',
      color: 'var(--navy)',
      marginBottom: 14
    }
  }, "Type the correct answer", wrongPart && wrongMeaning ? 's' : '', " to continue:"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 14
    }
  }, wrongPart && /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    style: {
      background: '#f0fdf4',
      border: '2px solid #16a34a',
      borderRadius: 10,
      padding: '10px 14px',
      marginBottom: 8
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      fontSize: '0.75rem',
      color: '#16a34a',
      textTransform: 'uppercase',
      letterSpacing: '0.05em',
      marginBottom: 3
    }
  }, partLabels[g]), /*#__PURE__*/React.createElement("p", {
    className: "latin",
    style: {
      fontSize: '1.6rem',
      fontWeight: 800,
      color: 'var(--dark)'
    }
  }, correctPart)), /*#__PURE__*/React.createElement("input", {
    ref: rtPartRef,
    className: "typed-input",
    style: latinStyle,
    value: rtPartAns,
    onChange: function onChange(e) {
      setRtPartAns(e.target.value);
      setRtFb(null);
    },
    onPaste: function onPaste(e) {
      return e.preventDefault();
    },
    placeholder: "..."
  })), wrongMeaning && /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    style: {
      background: '#f0fdf4',
      border: '2px solid #16a34a',
      borderRadius: 10,
      padding: '10px 14px',
      marginBottom: 8
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      fontSize: '0.75rem',
      color: '#16a34a',
      textTransform: 'uppercase',
      letterSpacing: '0.05em',
      marginBottom: 3
    }
  }, "Meaning"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.6rem',
      fontWeight: 800,
      color: 'var(--dark)'
    }
  }, (v.meanings || []).join(', '))), /*#__PURE__*/React.createElement("input", {
    ref: rtMeaningRef,
    className: "typed-input",
    style: engStyle,
    value: rtMeaningAns,
    onChange: function onChange(e) {
      setRtMeaningAns(e.target.value);
      setRtFb(null);
    },
    onPaste: function onPaste(e) {
      return e.preventDefault();
    },
    placeholder: "..."
  }))), rtFb && /*#__PURE__*/React.createElement("div", {
    style: {
      color: 'var(--red-bright)',
      marginTop: 10,
      fontWeight: 700,
      fontSize: '0.95rem'
    }
  }, rtFb), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-outline",
    disabled: busy,
    onClick: rtSubmit,
    style: {
      marginTop: 18
    }
  }, "Continue", /*#__PURE__*/React.createElement("span", {
    className: "keyhint"
  }, "Enter"))), !wrongPart && !wrongMeaning && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary anim-fade",
    disabled: busy,
    onClick: nx
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter"))))));
}

// ── Verb Conj FC (flashcard phase) ────────────────────────────────────────────
// Shows all 4 principal parts as a flip-card. Front: present + 3 blanks.
// Back: reveals infinitive / perfect / PPP. Hard/Easy rating (no marks).
function VerbConjFC(_ref47) {
  var pupil = _ref47.pupil,
    set = _ref47.set,
    verbs = _ref47.verbs,
    isPreview = _ref47.isPreview,
    onDone = _ref47.onDone,
    pct = _ref47.pct;
  var _useState205 = useState(function () {
      return _toConsumableArray(verbs);
    }),
    _useState206 = _slicedToArray(_useState205, 2),
    queue = _useState206[0],
    setQueue = _useState206[1];
  var _useState207 = useState(0),
    _useState208 = _slicedToArray(_useState207, 2),
    qIdx = _useState208[0],
    setQIdx = _useState208[1];
  var _useState209 = useState(false),
    _useState210 = _slicedToArray(_useState209, 2),
    rev = _useState210[0],
    setRev = _useState210[1];
  var _useState211 = useState(false),
    _useState212 = _slicedToArray(_useState211, 2),
    busy = _useState212[0],
    setBusy = _useState212[1];
  var _useState213 = useState(''),
    _useState214 = _slicedToArray(_useState213, 2),
    exitCls = _useState214[0],
    setExitCls = _useState214[1];
  var _useState215 = useState(false),
    _useState216 = _slicedToArray(_useState215, 2),
    entering = _useState216[0],
    setEntering = _useState216[1];
  var _useState217 = useState(0),
    _useState218 = _slicedToArray(_useState217, 2),
    doneCount = _useState218[0],
    setDoneCount = _useState218[1];
  var v = queue[qIdx];
  if (!v) {
    onDone();
    return null;
  }
  var rate = /*#__PURE__*/function () {
    var _ref48 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee19(r) {
      var newQLen;
      return _regenerator().w(function (_context19) {
        while (1) switch (_context19.n) {
          case 0:
            if (!busy) {
              _context19.n = 1;
              break;
            }
            return _context19.a(2);
          case 1:
            setBusy(true);
            if (isPreview) {
              _context19.n = 2;
              break;
            }
            _context19.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'flashcard_rating',
              question_text: v.present,
              pupil_answer: r
            });
          case 2:
            setExitCls(r === 'got_it' ? 'fc-exit-right' : 'fc-exit-left');
            newQLen = queue.length + (r === 'again' ? 1 : 0);
            if (r === 'again') setQueue(function (q) {
              var next = _toConsumableArray(q);
              next.push(_objectSpread(_objectSpread({}, v), {}, {
                revisit: true
              }));
              return next;
            });else setDoneCount(function (d) {
              return d + 1;
            });
            setTimeout(function () {
              setExitCls('');
              setRev(false);
              setBusy(false);
              if (qIdx + 1 >= newQLen) onDone();else {
                setQIdx(function (i) {
                  return i + 1;
                });
                setEntering(true);
                setTimeout(function () {
                  return setEntering(false);
                }, 230);
              }
            }, 270);
          case 3:
            return _context19.a(2);
        }
      }, _callee19);
    }));
    return function rate(_x11) {
      return _ref48.apply(this, arguments);
    };
  }();
  useEffect(function () {
    var h = function h(e) {
      if (e.code === 'Space') {
        e.preventDefault();
        if (!rev) setRev(true);else rate('got_it');
        return;
      }
      if (rev && e.key === '1') rate('again');
      if (rev && e.key === '2') rate('got_it');
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  var freshInQueue = queue.slice(qIdx).filter(function (c) {
    return !c.revisit;
  }).length;
  var hardInQueue = queue.slice(qIdx + 1).filter(function (c) {
    return c.revisit;
  }).length;
  var chipStyle = function chipStyle(revealed) {
    return {
      borderColor: revealed ? 'var(--blue)' : 'var(--blue)',
      color: revealed ? '#1a73e8' : 'var(--blue)'
    };
  };
  var parts = [{
    val: v.present,
    label: 'present',
    idx: 0,
    always: true
  }, {
    val: v.infinitive,
    label: 'infinitive',
    idx: 1,
    always: false
  }, {
    val: v.perfect,
    label: 'perfect',
    idx: 2,
    always: false
  }, {
    val: v.ppp,
    label: 'PPP',
    idx: 3,
    always: false,
    noPPP: v.ppp === null
  }];
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 16,
      fontWeight: 700,
      fontSize: '1.2rem',
      textAlign: 'center',
      width: '100%'
    }
  }, "What are all the ", /*#__PURE__*/React.createElement("strong", {
    style: {
      color: 'var(--navy)'
    }
  }, "principal parts"), " of this verb?"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'flex-start',
      gap: 20,
      width: '100%',
      maxWidth: 1000,
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement(CardPile, {
    count: freshInQueue,
    hardCount: hardInQueue,
    side: "left"
  }), /*#__PURE__*/React.createElement("div", {
    className: "".concat(exitCls).concat(entering ? ' fc-enter' : ''),
    style: {
      flex: 1,
      minWidth: 0,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      alignItems: 'center',
      gap: 16,
      marginBottom: 8,
      flexWrap: 'wrap',
      justifyContent: 'center'
    }
  }, parts.map(function (p, i) {
    return /*#__PURE__*/React.createElement(React.Fragment, {
      key: i
    }, i > 0 && /*#__PURE__*/React.createElement("span", {
      className: "part-sep"
    }, "/"), /*#__PURE__*/React.createElement("div", {
      style: {
        textAlign: 'center'
      }
    }, p.always ? /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
      className: "part-chip"
    }, /*#__PURE__*/React.createElement("span", {
      style: {
        whiteSpace: 'nowrap'
      }
    }, renderPartWithColor(p.val, p.idx))), /*#__PURE__*/React.createElement("p", {
      style: {
        color: 'var(--grey)',
        fontSize: '0.82rem',
        marginTop: 4,
        fontStyle: 'italic'
      }
    }, p.label)) : p.noPPP ? /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
      className: "part-chip",
      style: {
        borderColor: 'var(--grey)',
        color: 'var(--grey)',
        fontStyle: 'normal',
        fontSize: '0.95rem'
      }
    }, rev ? 'no PPP' : '?'), /*#__PURE__*/React.createElement("p", {
      style: {
        color: 'var(--grey)',
        fontSize: '0.82rem',
        marginTop: 4,
        fontStyle: 'italic'
      }
    }, p.label)) : /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("span", {
      className: "part-chip",
      style: chipStyle(rev)
    }, rev ? /*#__PURE__*/React.createElement("span", {
      style: {
        whiteSpace: 'nowrap'
      }
    }, renderPartWithColor(p.val, p.idx)) : '?'), /*#__PURE__*/React.createElement("p", {
      style: {
        color: 'var(--grey)',
        fontSize: '0.82rem',
        marginTop: 4,
        fontStyle: 'italic'
      }
    }, p.label))));
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      margin: '0 14px',
      color: 'var(--lgrey)',
      fontSize: '1.4rem',
      fontWeight: 200
    }
  }, "|"), /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: 'center'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 700,
      fontSize: '1.2rem',
      color: rev ? 'var(--navy)' : 'var(--blue)'
    }
  }, rev ? (v.meanings || []).join(', ') : '?'), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      fontSize: '0.82rem',
      marginTop: 4,
      fontStyle: 'italic'
    }
  }, "meaning")))), /*#__PURE__*/React.createElement(CardPile, {
    count: doneCount,
    side: "right"
  })), rev ? /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      display: 'flex',
      gap: 32,
      marginTop: 24
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-grey",
    disabled: busy,
    onClick: function onClick() {
      return rate('again');
    }
  }, "Hard", /*#__PURE__*/React.createElement("span", {
    className: "keyhint"
  }, "Press 1")), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: function onClick() {
      return rate('got_it');
    }
  }, "Easy", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Press 2"))) : /*#__PURE__*/React.createElement("p", {
    style: {
      marginTop: 24,
      color: 'var(--grey)',
      fontSize: '1.3rem',
      fontWeight: 700
    }
  }, "Press SPACE to reveal"), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: 16,
      display: 'flex',
      gap: 12,
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: '0.85rem',
      fontWeight: 700,
      color: 'var(--lgrey)'
    }
  }, "Card ", qIdx + 1, " of ", queue.length), /*#__PURE__*/React.createElement("div", {
    style: {
      width: 160,
      height: 5,
      background: 'var(--lgrey)',
      borderRadius: 3,
      overflow: 'hidden'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      width: "".concat((qIdx + 1) / Math.max(queue.length, 1) * 100, "%"),
      height: '100%',
      background: 'var(--blue)',
      borderRadius: 3,
      transition: 'width .3s'
    }
  }))))));
}

// ── Verb Conj MC (MCQ phase) ───────────────────────────────────────────────────
// Shows ALL four principal parts; asks for the English meaning (4 MC options).
function VerbConjMC(_ref49) {
  var pupil = _ref49.pupil,
    set = _ref49.set,
    verbs = _ref49.verbs,
    isPreview = _ref49.isPreview,
    onDone = _ref49.onDone,
    addC = _ref49.addC,
    addW = _ref49.addW,
    pct = _ref49.pct;
  var _useState219 = useState(function () {
      return _toConsumableArray(verbs.map(function (v) {
        return {
          v: v
        };
      }));
    }),
    _useState220 = _slicedToArray(_useState219, 2),
    queue = _useState220[0],
    setQueue = _useState220[1];
  var _useState221 = useState(0),
    _useState222 = _slicedToArray(_useState221, 2),
    qIdx = _useState222[0],
    setQIdx = _useState222[1];
  var _useState223 = useState(null),
    _useState224 = _slicedToArray(_useState223, 2),
    sel = _useState224[0],
    setSel = _useState224[1];
  var _useState225 = useState(null),
    _useState226 = _slicedToArray(_useState225, 2),
    fb = _useState226[0],
    setFb = _useState226[1];
  var _useState227 = useState(false),
    _useState228 = _slicedToArray(_useState227, 2),
    busy = _useState228[0],
    setBusy = _useState228[1];
  var q = queue[qIdx];
  if (!q) {
    onDone();
    return null;
  }
  var v = q.v;
  var parts = [v.present, v.infinitive, v.perfect, v.ppp];
  var correct = v.meanings[0];
  var correctDisplay = (v.meanings || []).join(', ');
  var isRetry = q.failed;
  // Generate options once per question
  var optsRef = useRef(null);
  if (optsRef.current === null || optsRef.current.qIdx !== qIdx) {
    var others = shuffleOnce(verbs.filter(function (u) {
      return u !== v;
    }));
    var ds = [];
    var _iterator4 = _createForOfIteratorHelper(others),
      _step4;
    try {
      for (_iterator4.s(); !(_step4 = _iterator4.n()).done;) {
        var u = _step4.value;
        var d = u.meanings[0];
        if (d && d !== correct && !ds.includes(d) && ds.length < 3) ds.push(d);
      }
    } catch (err) {
      _iterator4.e(err);
    } finally {
      _iterator4.f();
    }
    optsRef.current = {
      qIdx: qIdx,
      opts: shuffleOnce([correct].concat(ds))
    };
  }
  var opts = optsRef.current.opts;
  var pick = /*#__PURE__*/function () {
    var _ref50 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee20(o) {
      var res;
      return _regenerator().w(function (_context20) {
        while (1) switch (_context20.n) {
          case 0:
            if (!(fb || busy)) {
              _context20.n = 1;
              break;
            }
            return _context20.a(2);
          case 1:
            setBusy(true);
            setSel(o);
            _context20.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'mc',
              question_text: "meaning of ".concat(v.present),
              pupil_answer: o,
              correct_answer: correct
            });
          case 2:
            res = _context20.v;
            setFb(res);
            if (res.counts_as_correct) {
              if (!q.failed) addC();
            } else {
              if (!q.failed) addW({
                latin: v.present,
                correct: correct
              });
              setQueue(function (prev) {
                return [].concat(_toConsumableArray(prev), [{
                  v: v,
                  failed: true
                }]);
              });
            }
            setBusy(false);
          case 3:
            return _context20.a(2);
        }
      }, _callee20);
    }));
    return function pick(_x12) {
      return _ref50.apply(this, arguments);
    };
  }();
  var nx = function nx() {
    resetScroll();
    optsRef.current = null;
    setSel(null);
    setFb(null);
    if (qIdx + 1 >= queue.length) onDone();else setQIdx(function (i) {
      return i + 1;
    });
  };
  useEffect(function () {
    var h = function h(e) {
      if (e.ctrlKey && e.altKey && e.code === "KeyK") {
        e.preventDefault();
        e.stopPropagation();
        if (!(q !== null && q !== void 0 && q.failed)) addC();
        nx();
        return;
      }
      if (e.ctrlKey && e.altKey && e.code === "KeyJ") {
        e.preventDefault();
        e.stopPropagation();
        nx();
        return;
      }
      if (fb && (e.key === 'Enter' || e.code === 'Space' && e.target.tagName !== 'INPUT')) {
        e.preventDefault();
        nx();
      }
      if (!fb) {
        var n = parseInt(e.key);
        if (n >= 1 && n <= 4 && opts[n - 1]) pick(opts[n - 1]);
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  var cardStyle = {
    display: 'flex',
    alignItems: 'center',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: '4px 0',
    background: 'white',
    borderRadius: 16,
    padding: '22px 28px',
    boxShadow: '0 2px 12px rgba(0,33,71,0.08)',
    border: '2px solid var(--lgrey)',
    width: '100%',
    maxWidth: 960,
    marginBottom: 20
  };
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body",
    style: {
      overflowY: 'hidden',
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 40,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: 8
    }
  }, isRetry && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: '#f97316',
      border: '2px solid #ea580c',
      borderRadius: 10,
      padding: '6px 16px',
      fontWeight: 800,
      color: 'white',
      fontSize: '0.9rem',
      display: 'inline-block'
    }
  }, "Try this again \u2014 you got it wrong before.")), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 16,
      fontWeight: 700,
      fontSize: '1.2rem',
      textAlign: 'center',
      width: '100%'
    }
  }, "What does this verb ", /*#__PURE__*/React.createElement("strong", {
    style: {
      color: 'var(--navy)'
    }
  }, "mean"), "?"), /*#__PURE__*/React.createElement("div", {
    style: cardStyle
  }, parts.map(function (p, i) {
    if (p == null) return null;
    return /*#__PURE__*/React.createElement(React.Fragment, {
      key: i
    }, i > 0 && /*#__PURE__*/React.createElement("span", {
      className: "part-sep"
    }, "/"), /*#__PURE__*/React.createElement("span", {
      className: "part-chip"
    }, /*#__PURE__*/React.createElement("span", {
      style: {
        whiteSpace: 'nowrap'
      }
    }, renderPartWithColor(p, i))));
  })), /*#__PURE__*/React.createElement("div", {
    className: "mc-options"
  }, opts.map(function (o, i) {
    return /*#__PURE__*/React.createElement("button", {
      key: i,
      className: "mc-opt ".concat(fb ? o === correct ? 'correct' : o === sel ? 'wrong' : '' : ''),
      disabled: busy && !fb,
      onClick: function onClick() {
        return pick(o);
      }
    }, /*#__PURE__*/React.createElement("span", {
      className: "keyhint",
      style: {
        display: 'block',
        marginBottom: 12
      }
    }, "Press ", i + 1), /*#__PURE__*/React.createElement("span", {
      style: {
        fontWeight: 700,
        fontSize: '1.5rem'
      }
    }, o === correct ? correctDisplay : o));
  })), fb && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      minHeight: 80,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: nx,
    style: {
      marginTop: 16
    }
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter / Space"))), !fb && /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 80
    }
  }))));
}

// ── Tense ID - fixed-order buttons, no timer, scaffolded forms ────────────────
function TenseId(_ref51) {
  var pupil = _ref51.pupil,
    set = _ref51.set,
    qs = _ref51.qs,
    isPreview = _ref51.isPreview,
    onDone = _ref51.onDone,
    addC = _ref51.addC,
    addW = _ref51.addW,
    pct = _ref51.pct;
  var _useState229 = useState(0),
    _useState230 = _slicedToArray(_useState229, 2),
    idx = _useState230[0],
    setIdx = _useState230[1];
  var _useState231 = useState(null),
    _useState232 = _slicedToArray(_useState231, 2),
    sel = _useState232[0],
    setSel = _useState232[1];
  var _useState233 = useState(null),
    _useState234 = _slicedToArray(_useState233, 2),
    fb = _useState234[0],
    setFb = _useState234[1];
  var _useState235 = useState(false),
    _useState236 = _slicedToArray(_useState235, 2),
    busy = _useState236[0],
    setBusy = _useState236[1];
  var q = qs[idx];
  var tenseOpts = set.tense_options || ['present', 'future', 'imperfect', 'perfect', 'pluperfect'];
  var pick = /*#__PURE__*/function () {
    var _ref52 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee21(o) {
      var res;
      return _regenerator().w(function (_context21) {
        while (1) switch (_context21.n) {
          case 0:
            if (!(fb || busy)) {
              _context21.n = 1;
              break;
            }
            return _context21.a(2);
          case 1:
            setBusy(true);
            setSel(o);
            _context21.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'parsing_mcq',
              question_text: q.plain_form || q.form,
              pupil_answer: o,
              correct_answer: q.tense
            });
          case 2:
            res = _context21.v;
            setFb(res);
            if (res.counts_as_correct) {
              if (!q.failed) addC();
            } else {
              if (!q.failed) addW({
                latin: q.form,
                correct: q.tense
              });
            }
            ;
            setBusy(false);
          case 3:
            return _context21.a(2);
        }
      }, _callee21);
    }));
    return function pick(_x13) {
      return _ref52.apply(this, arguments);
    };
  }();
  var nx = function nx() {
    resetScroll();
    setFb(null);
    setSel(null);
    if (idx + 1 >= qs.length) onDone();else setIdx(function (i) {
      return i + 1;
    });
  };
  useEffect(function () {
    var h = function h(e) {
      if (e.ctrlKey && e.altKey && e.code === "KeyK") {
        e.preventDefault();
        e.stopPropagation();
        if (!(q !== null && q !== void 0 && q.failed)) addC();
        nx();
        return;
      }
      if (e.ctrlKey && e.altKey && e.code === "KeyJ") {
        e.preventDefault();
        e.stopPropagation();
        nx();
        return;
      }
      if (fb && (e.key === 'Enter' || e.code === 'Space' && e.target.tagName !== 'INPUT')) {
        e.preventDefault();
        nx();
      }
      if (!fb) {
        var n = parseInt(e.key);
        if (n >= 1 && n <= tenseOpts.length) pick(tenseOpts[n - 1]);
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body",
    style: {
      overflowY: 'hidden',
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "mc-prompt"
  }, /*#__PURE__*/React.createElement("h2", null, "What tense is ", renderScaffolded(q.form), "?")), /*#__PURE__*/React.createElement("div", {
    className: "mc-options",
    style: {
      gridTemplateColumns: '1fr 1fr 1fr',
      maxWidth: 1100
    }
  }, tenseOpts.map(function (o, i) {
    return /*#__PURE__*/React.createElement("button", {
      key: i,
      className: "mc-opt ".concat(fb ? o === q.tense ? 'correct' : o === sel ? 'wrong' : '' : ''),
      disabled: busy && !fb,
      onClick: function onClick() {
        return pick(o);
      },
      style: {
        padding: '28px 16px',
        fontSize: '1.5rem'
      }
    }, /*#__PURE__*/React.createElement("span", {
      className: "keyhint",
      style: {
        display: 'block',
        marginBottom: 10
      }
    }, "Press ", i + 1), o);
  })), fb && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      minHeight: 80,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    }
  }, fb.counts_as_correct && /*#__PURE__*/React.createElement("p", {
    style: {
      marginTop: 8,
      fontSize: '1.2rem',
      color: 'var(--grey)'
    }
  }, /*#__PURE__*/React.createElement("span", {
    className: "latin"
  }, q.plain_form), " = ", /*#__PURE__*/React.createElement("em", null, q.translation)), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: nx,
    style: {
      marginTop: 16
    }
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter / Space"))), !fb && /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 80
    }
  }))));
}

// ── Parsing MCQ - fixed option order, 10s timer ───────────────────────────────
// ── Translate the Form ───────────────────────────────────────────────────────
function TranslateForm(_ref53) {
  var pupil = _ref53.pupil,
    set = _ref53.set,
    qs = _ref53.qs,
    isPreview = _ref53.isPreview,
    onDone = _ref53.onDone,
    addC = _ref53.addC,
    addW = _ref53.addW,
    pct = _ref53.pct;
  var _useState237 = useState(function () {
      return _toConsumableArray(qs);
    }),
    _useState238 = _slicedToArray(_useState237, 2),
    queue = _useState238[0],
    setQueue = _useState238[1];
  var _useState239 = useState(0),
    _useState240 = _slicedToArray(_useState239, 2),
    qIdx = _useState240[0],
    setQIdx = _useState240[1];
  var _useState241 = useState(null),
    _useState242 = _slicedToArray(_useState241, 2),
    sel = _useState242[0],
    setSel = _useState242[1];
  var _useState243 = useState(null),
    _useState244 = _slicedToArray(_useState243, 2),
    fb = _useState244[0],
    setFb = _useState244[1];
  var _useState245 = useState(false),
    _useState246 = _slicedToArray(_useState245, 2),
    busy = _useState246[0],
    setBusy = _useState246[1];
  var _useState247 = useState(10),
    _useState248 = _slicedToArray(_useState247, 2),
    timeLeft = _useState248[0],
    setTimeLeft = _useState248[1];
  var q = queue[qIdx];
  useEffect(function () {
    if (fb || busy || !q || q.failed) return; // no timer on retries
    if (timeLeft <= 0) {
      var handleTimeout = /*#__PURE__*/function () {
        var _ref54 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee22() {
          var res;
          return _regenerator().w(function (_context22) {
            while (1) switch (_context22.n) {
              case 0:
                setBusy(true);
                setSel('timeout');
                res = {
                  counts_as_correct: false,
                  timeout: true,
                  message: "".concat(timeoutBadge(), " The correct answer is: **").concat(q.correct, "**")
                };
                if (isPreview) {
                  _context22.n = 1;
                  break;
                }
                _context22.n = 1;
                return post('/api/check', {
                  pupil_id: pupil.id,
                  set_id: set.id,
                  question_type: 'translate_form',
                  question_text: q.form,
                  pupil_answer: 'TIMEOUT',
                  correct_answer: q.correct
                });
              case 1:
                setFb(res);
                if (!q.failed) addW({
                  latin: q.form,
                  correct: q.correct
                });
                setQueue(function (prev) {
                  return [].concat(_toConsumableArray(prev), [_objectSpread(_objectSpread({}, q), {}, {
                    failed: true
                  })]);
                });
                setBusy(false);
              case 2:
                return _context22.a(2);
            }
          }, _callee22);
        }));
        return function handleTimeout() {
          return _ref54.apply(this, arguments);
        };
      }();
      handleTimeout();
      return;
    }
    var t = setInterval(function () {
      return setTimeLeft(function (x) {
        return x - 1;
      });
    }, 1000);
    return function () {
      return clearInterval(t);
    };
  }, [timeLeft, fb, busy, q, isPreview, pupil.id, set.id, addW]);
  var nx = function nx() {
    resetScroll();
    setSel(null);
    setFb(null);
    setTimeLeft(10);
    if (qIdx + 1 >= queue.length) onDone();else setQIdx(function (i) {
      return i + 1;
    });
  };
  var pick = /*#__PURE__*/function () {
    var _ref55 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee23(o) {
      var res;
      return _regenerator().w(function (_context23) {
        while (1) switch (_context23.n) {
          case 0:
            if (!(fb || busy || !q)) {
              _context23.n = 1;
              break;
            }
            return _context23.a(2);
          case 1:
            setBusy(true);
            setSel(o);
            _context23.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'translate_form',
              question_text: q.form,
              pupil_answer: o,
              correct_answer: q.correct
            });
          case 2:
            res = _context23.v;
            setFb(res);
            if (res.counts_as_correct) {
              if (!q.failed) addC();
            } else {
              if (!q.failed) {
                addW({
                  latin: q.form,
                  correct: q.correct
                });
              }
              // Re-add to queue for retry
              setQueue(function (prev) {
                return [].concat(_toConsumableArray(prev), [_objectSpread(_objectSpread({}, q), {}, {
                  failed: true
                })]);
              });
            }
            setBusy(false);
          case 3:
            return _context23.a(2);
        }
      }, _callee23);
    }));
    return function pick(_x14) {
      return _ref55.apply(this, arguments);
    };
  }();
  useEffect(function () {
    var h = function h(e) {
      if (fb && (e.key === 'Enter' || e.code === 'Space' && e.target.tagName !== 'INPUT')) {
        e.preventDefault();
        nx();
        return;
      }
      if (!fb && q) {
        var _q$options;
        var n = parseInt(e.key);
        if (n >= 1 && n <= (((_q$options = q.options) === null || _q$options === void 0 ? void 0 : _q$options.length) || 0)) pick(q.options[n - 1]);
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  if (!q) return null;
  var isRetry = q.failed;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), !isRetry && /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '12px 40px 4px',
      width: '100%',
      maxWidth: 1000,
      alignSelf: 'center',
      boxSizing: 'border-box'
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "timer-bar",
    style: {
      margin: 0
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "timer-fill",
    style: {
      width: "".concat(timeLeft / 10 * 100, "%"),
      background: fb ? fb.counts_as_correct ? 'var(--green-bright)' : 'var(--red-bright)' : timeLeft <= 3 ? 'var(--red-bright)' : 'var(--blue)',
      transition: fb ? 'none' : 'width 1s linear, background .3s'
    }
  }))), /*#__PURE__*/React.createElement("div", {
    className: "activity-body",
    style: {
      overflowY: 'hidden',
      justifyContent: 'center',
      paddingTop: 36
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 40,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: 8
    }
  }, isRetry && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: '#f97316',
      border: '2px solid #ea580c',
      borderRadius: 10,
      padding: '6px 16px',
      fontWeight: 800,
      color: 'white',
      fontSize: '0.9rem',
      display: 'inline-block'
    }
  }, "Try this again \u2014 you got it wrong before."), (fb === null || fb === void 0 ? void 0 : fb.timeout) && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: 'var(--red-bright)',
      border: '2px solid #b91c1c',
      borderRadius: 10,
      padding: '6px 16px',
      fontWeight: 800,
      color: 'white',
      fontSize: '0.9rem',
      display: 'inline-block'
    }
  }, timeoutBadge())), /*#__PURE__*/React.createElement("div", {
    className: "mc-prompt"
  }, /*#__PURE__*/React.createElement("h1", {
    className: "latin dynamic-latin",
    style: {
      fontSize: '3.8rem'
    }
  }, q.form)), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 24,
      fontWeight: 700
    }
  }, "What does this mean?"), /*#__PURE__*/React.createElement("div", {
    className: "mc-options",
    style: {
      gridTemplateColumns: '1fr 1fr 1fr',
      maxWidth: 1000
    }
  }, (q.options || []).map(function (o, i) {
    return /*#__PURE__*/React.createElement("button", {
      key: i,
      className: "mc-opt ".concat(fb ? o === q.correct ? 'correct' : o === sel ? 'wrong' : '' : ''),
      disabled: busy && !fb,
      onClick: function onClick() {
        return pick(o);
      }
    }, /*#__PURE__*/React.createElement("span", {
      className: "keyhint",
      style: {
        display: 'block',
        marginBottom: 8
      }
    }, "Press ", i + 1), o);
  })), fb && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      marginTop: 16
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    onClick: nx,
    style: {
      marginTop: 12
    }
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter / Space"))))));
}

// ── Full Parsing (Hoi Polloi Logoi style) ─────────────────────────────────
// Student clicks Tense + Person + Number buttons, then presses Check
function FullParsing(_ref56) {
  var _q$form;
  var pupil = _ref56.pupil,
    set = _ref56.set,
    qs = _ref56.qs,
    isPreview = _ref56.isPreview,
    onDone = _ref56.onDone,
    addC = _ref56.addC,
    addW = _ref56.addW,
    pct = _ref56.pct;
  var TENSES = ['present', 'future', 'imperfect', 'perfect', 'pluperfect'];
  var PERSON_NUMBERS = [{
    id: '1-s',
    label: 'I',
    p: '1st',
    n: 'singular'
  }, {
    id: '2-s',
    label: 'you (sg)',
    p: '2nd',
    n: 'singular'
  }, {
    id: '3-s',
    label: 'he/she/it',
    p: '3rd',
    n: 'singular'
  }, {
    id: '1-p',
    label: 'we',
    p: '1st',
    n: 'plural'
  }, {
    id: '2-p',
    label: 'you (pl.)',
    p: '2nd',
    n: 'plural'
  }, {
    id: '3-p',
    label: 'they',
    p: '3rd',
    n: 'plural'
  }];
  var _useState249 = useState(0),
    _useState250 = _slicedToArray(_useState249, 2),
    idx = _useState250[0],
    setIdx = _useState250[1];
  var _useState251 = useState(null),
    _useState252 = _slicedToArray(_useState251, 2),
    selTense = _useState252[0],
    setSelTense = _useState252[1];
  var _useState253 = useState(null),
    _useState254 = _slicedToArray(_useState253, 2),
    selPerson = _useState254[0],
    setSelPerson = _useState254[1];
  var _useState255 = useState(null),
    _useState256 = _slicedToArray(_useState255, 2),
    selNumber = _useState256[0],
    setSelNumber = _useState256[1];
  var selPN = selPerson && selNumber ? "".concat(selPerson, "-").concat(selNumber).substring(0, 3) : null;
  var _useState257 = useState(null),
    _useState258 = _slicedToArray(_useState257, 2),
    fb = _useState258[0],
    setFb = _useState258[1];
  var _useState259 = useState(false),
    _useState260 = _slicedToArray(_useState259, 2),
    busy = _useState260[0],
    setBusy = _useState260[1];
  var q = qs[idx];
  var nx = function nx() {
    resetScroll();
    setSelTense(null);
    setSelPerson(null);
    setSelNumber(null);
    setFb(null);
    if (idx + 1 >= qs.length) onDone();else setIdx(function (i) {
      return i + 1;
    });
  };
  var check = /*#__PURE__*/function () {
    var _ref57 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee24() {
      var correctKey, res;
      return _regenerator().w(function (_context24) {
        while (1) switch (_context24.n) {
          case 0:
            if (!(!selTense || !selPerson || !selNumber || busy)) {
              _context24.n = 1;
              break;
            }
            return _context24.a(2);
          case 1:
            setBusy(true);
            correctKey = "".concat(q.tense, "|").concat(q.person, "|").concat(q.number);
            _context24.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'parsing',
              question_text: q.plain || q.form,
              pupil_answer: "".concat(selTense, "|").concat(selPerson, "|").concat(selNumber),
              correct_answer: correctKey,
              tense: selTense,
              person: selPerson,
              number: selNumber
            });
          case 2:
            res = _context24.v;
            setFb(res);
            if (res.counts_as_correct) {
              if (!q.failed) addC();
            } else {
              if (!q.failed) addW({
                latin: q.form,
                correct: "".concat(q.tense, " ").concat(q.person, " ").concat(q.number)
              });
            }
            setBusy(false);
          case 3:
            return _context24.a(2);
        }
      }, _callee24);
    }));
    return function check() {
      return _ref57.apply(this, arguments);
    };
  }();
  useEffect(function () {
    var h = function h(e) {
      if (fb && e.key === 'Enter') nx();
      if (!fb && e.key === 'Enter' && selTense && selPerson && selNumber) check();
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  var BtnGroup = function BtnGroup(_ref58) {
    var options = _ref58.options,
      selected = _ref58.selected,
      onSelect = _ref58.onSelect,
      label = _ref58.label,
      correctVal = _ref58.correctVal;
    return /*#__PURE__*/React.createElement("div", {
      style: {
        marginBottom: 20
      }
    }, /*#__PURE__*/React.createElement("p", {
      style: {
        fontWeight: 800,
        color: 'var(--grey)',
        fontSize: '0.85rem',
        textTransform: 'uppercase',
        letterSpacing: '0.08em',
        marginBottom: 8
      }
    }, label), /*#__PURE__*/React.createElement("div", {
      style: {
        display: 'flex',
        gap: 10,
        flexWrap: 'wrap',
        justifyContent: 'center'
      }
    }, options.map(function (o) {
      var isSel = o === selected;
      var isRight = fb && (fb.counts_as_correct ? isSel : isSel && o === correctVal);
      var isWrong = fb && isSel && !fb.counts_as_correct && o !== correctVal;
      var bg = fb ? isRight ? 'var(--green-bright)' : isWrong ? 'var(--red-bright)' : isSel ? 'var(--navy)' : 'var(--white)' : isSel ? 'var(--navy)' : 'var(--white)';
      var bd = fb ? isRight ? 'var(--green-bright)' : isWrong ? 'var(--red-bright)' : isSel ? 'var(--navy)' : 'var(--lgrey)' : isSel ? 'var(--navy)' : 'var(--lgrey)';
      return /*#__PURE__*/React.createElement("button", {
        key: o,
        disabled: !!fb,
        onClick: function onClick() {
          return onSelect(o === selected ? null : o);
        },
        style: {
          padding: '10px 20px',
          borderRadius: 12,
          border: "2px solid ".concat(bd),
          background: bg,
          color: isSel || isRight ? 'var(--white)' : 'var(--dark)',
          fontWeight: 700,
          fontSize: '1rem',
          cursor: fb ? 'default' : 'pointer',
          transition: 'all .15s'
        }
      }, o);
    })));
  };
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("div", {
    className: "flashcard",
    style: {
      maxWidth: 800
    }
  }, /*#__PURE__*/React.createElement("h1", {
    className: "latin dynamic-latin",
    style: {
      fontSize: (q === null || q === void 0 || (_q$form = q.form) === null || _q$form === void 0 ? void 0 : _q$form.length) > 15 ? '2.8rem' : '3.6rem',
      marginBottom: 24
    }
  }, q === null || q === void 0 ? void 0 : q.form), (q === null || q === void 0 ? void 0 : q.translation) && !fb && /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      fontSize: '1rem',
      marginBottom: 20,
      fontStyle: 'italic'
    }
  }, "(", q.translation, ")"), /*#__PURE__*/React.createElement("div", {
    style: {
      marginBottom: 20
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      color: 'var(--grey)',
      fontSize: '0.85rem',
      textTransform: 'uppercase',
      letterSpacing: '0.08em',
      marginBottom: 8
    }
  }, "Person / Number"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: '1fr 1fr 1fr',
      gap: 10
    }
  }, PERSON_NUMBERS.map(function (pn) {
    var isSel = pn.id === selPN;
    var pnIsCorrect = pn.p === (q === null || q === void 0 ? void 0 : q.person) && pn.n === (q === null || q === void 0 ? void 0 : q.number);
    var isRight = fb && (fb.counts_as_correct ? isSel : isSel && pnIsCorrect);
    var isWrong = fb && isSel && !fb.counts_as_correct && !pnIsCorrect;
    var bg = fb ? isRight ? 'var(--green-bright)' : isWrong ? 'var(--red-bright)' : isSel ? 'var(--navy)' : 'var(--white)' : isSel ? 'var(--navy)' : 'var(--white)';
    var bd = fb ? isRight ? 'var(--green-bright)' : isWrong ? 'var(--red-bright)' : isSel ? 'var(--navy)' : 'var(--lgrey)' : isSel ? 'var(--navy)' : 'var(--lgrey)';
    return /*#__PURE__*/React.createElement("button", {
      key: pn.id,
      disabled: !!fb,
      onClick: function onClick() {
        if (pn.id === selPN) {
          setSelPerson(null);
          setSelNumber(null);
        } else {
          setSelPerson(pn.p);
          setSelNumber(pn.n);
        }
      },
      style: {
        padding: '14px 10px',
        borderRadius: 12,
        border: "2px solid ".concat(bd),
        background: bg,
        color: isSel || isRight ? 'var(--white)' : 'var(--dark)',
        fontWeight: 700,
        fontSize: '1.1rem',
        cursor: fb ? 'default' : 'pointer',
        transition: 'all .15s'
      }
    }, pn.label);
  }))), /*#__PURE__*/React.createElement(BtnGroup, {
    label: "Tense",
    options: TENSES,
    selected: selTense,
    onSelect: setSelTense,
    correctVal: q === null || q === void 0 ? void 0 : q.tense
  }), fb && !fb.counts_as_correct && /*#__PURE__*/React.createElement("div", {
    className: "feedback anim-fade bad",
    style: {
      marginTop: 12
    }
  }, renderText(fb.message))), !fb && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: !selTense || !selPerson || !selNumber || busy,
    onClick: check,
    style: {
      marginTop: 30,
      opacity: !selTense || !selPerson || !selNumber ? 0.4 : 1
    }
  }, "Check", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")), fb && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary anim-fade",
    onClick: nx,
    style: {
      marginTop: 30
    }
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")), /*#__PURE__*/React.createElement("p", {
    style: {
      marginTop: 16,
      color: 'var(--lgrey)',
      fontSize: '0.9rem',
      fontWeight: 700
    }
  }, "Question ", idx + 1, " of ", qs.length))));
}
function Parsing(_ref59) {
  var _q$form2;
  var pupil = _ref59.pupil,
    set = _ref59.set,
    qs = _ref59.qs,
    isPreview = _ref59.isPreview,
    onDone = _ref59.onDone,
    addC = _ref59.addC,
    addW = _ref59.addW,
    pct = _ref59.pct;
  var _useState261 = useState(0),
    _useState262 = _slicedToArray(_useState261, 2),
    idx = _useState262[0],
    setIdx = _useState262[1];
  var _useState263 = useState(null),
    _useState264 = _slicedToArray(_useState263, 2),
    sel = _useState264[0],
    setSel = _useState264[1];
  var _useState265 = useState(null),
    _useState266 = _slicedToArray(_useState265, 2),
    fb = _useState266[0],
    setFb = _useState266[1];
  var _useState267 = useState(false),
    _useState268 = _slicedToArray(_useState267, 2),
    busy = _useState268[0],
    setBusy = _useState268[1];
  var _useState269 = useState(10),
    _useState270 = _slicedToArray(_useState269, 2),
    timeLeft = _useState270[0],
    setTimeLeft = _useState270[1];
  var q = qs[idx];
  useEffect(function () {
    if (fb || busy || !q) return;
    if (timeLeft <= 0) {
      var handleTimeout = /*#__PURE__*/function () {
        var _ref60 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee25() {
          var res;
          return _regenerator().w(function (_context25) {
            while (1) switch (_context25.n) {
              case 0:
                setBusy(true);
                setSel('timeout');
                res = {
                  counts_as_correct: false,
                  timeout: true,
                  message: "".concat(timeoutBadge(), " The correct answer is: **").concat(q.correct, "**")
                };
                if (isPreview) {
                  _context25.n = 1;
                  break;
                }
                _context25.n = 1;
                return post('/api/check', {
                  pupil_id: pupil.id,
                  set_id: set.id,
                  question_type: 'parsing_mcq',
                  question_text: q.plain_form || q.form,
                  pupil_answer: 'TIMEOUT',
                  correct_answer: q.correct
                });
              case 1:
                setFb(res);
                if (!q.failed) addW({
                  latin: q.form,
                  correct: q.correct
                });
                setBusy(false);
              case 2:
                return _context25.a(2);
            }
          }, _callee25);
        }));
        return function handleTimeout() {
          return _ref60.apply(this, arguments);
        };
      }();
      handleTimeout();
      return;
    }
    var t = setInterval(function () {
      return setTimeLeft(function (x) {
        return x - 1;
      });
    }, 1000);
    return function () {
      return clearInterval(t);
    };
  }, [timeLeft, fb, busy, q]);
  var pick = /*#__PURE__*/function () {
    var _ref61 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee26(o) {
      var res;
      return _regenerator().w(function (_context26) {
        while (1) switch (_context26.n) {
          case 0:
            if (!(fb || busy || !q)) {
              _context26.n = 1;
              break;
            }
            return _context26.a(2);
          case 1:
            setBusy(true);
            setSel(o);
            _context26.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'parsing_mcq',
              question_text: q.plain_form || q.form,
              pupil_answer: o,
              correct_answer: q.correct
            });
          case 2:
            res = _context26.v;
            setFb(res);
            if (res.counts_as_correct) {
              if (!q.failed) addC();
            } else {
              if (!q.failed) addW({
                latin: q.form,
                correct: q.correct
              });
            }
            ;
            setBusy(false);
          case 3:
            return _context26.a(2);
        }
      }, _callee26);
    }));
    return function pick(_x15) {
      return _ref61.apply(this, arguments);
    };
  }();
  var nx = function nx() {
    resetScroll();
    setFb(null);
    setSel(null);
    setTimeLeft(10);
    if (idx + 1 >= qs.length) onDone();else setIdx(function (i) {
      return i + 1;
    });
  };
  useEffect(function () {
    var h = function h(e) {
      if (fb && (e.key === 'Enter' || e.code === 'Space' && e.target.tagName !== 'INPUT')) {
        e.preventDefault();
        nx();
      }
      if (!fb && q) {
        var n = parseInt(e.key);
        if (n >= 1 && n <= 4 && q.options) pick(q.options[n - 1]);
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  if (!q) return null;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '12px 40px 4px',
      width: '100%',
      maxWidth: 1000,
      alignSelf: 'center',
      boxSizing: 'border-box'
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "timer-bar",
    style: {
      margin: 0
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "timer-fill",
    style: {
      width: "".concat(timeLeft / 10 * 100, "%"),
      background: fb ? fb.counts_as_correct ? 'var(--green-bright)' : 'var(--red-bright)' : timeLeft <= 3 ? 'var(--red-bright)' : 'var(--blue)',
      transition: fb ? 'none' : 'width 1s linear, background .3s'
    }
  }))), /*#__PURE__*/React.createElement("div", {
    className: "activity-body",
    style: {
      overflowY: 'hidden',
      justifyContent: 'center',
      paddingTop: 36
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 40,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: 8
    }
  }, (fb === null || fb === void 0 ? void 0 : fb.timeout) && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: 'var(--red-bright)',
      border: '2px solid #b91c1c',
      borderRadius: 10,
      padding: '6px 16px',
      fontWeight: 800,
      color: 'white',
      fontSize: '0.9rem',
      display: 'inline-block'
    }
  }, timeoutBadge())), /*#__PURE__*/React.createElement("div", {
    className: "mc-prompt"
  }, /*#__PURE__*/React.createElement("h1", {
    className: "latin dynamic-latin",
    style: {
      fontSize: (q === null || q === void 0 || (_q$form2 = q.form) === null || _q$form2 === void 0 ? void 0 : _q$form2.length) > 20 ? '3rem' : '4rem'
    }
  }, (q === null || q === void 0 ? void 0 : q.plain_form) || (q === null || q === void 0 ? void 0 : q.form))), /*#__PURE__*/React.createElement("div", {
    className: "mc-options",
    style: {
      gridTemplateColumns: '1fr 1fr',
      maxWidth: 800
    }
  }, (q.options || []).map(function (o, i) {
    return /*#__PURE__*/React.createElement("button", {
      key: i,
      className: "mc-opt ".concat(fb ? o === q.correct ? 'correct' : o === sel ? 'wrong' : '' : ''),
      disabled: busy && !fb,
      onClick: function onClick() {
        return pick(o);
      }
    }, /*#__PURE__*/React.createElement("span", {
      className: "keyhint",
      style: {
        display: 'block',
        marginBottom: 12
      }
    }, "Press ", i + 1), o);
  })), fb && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      minHeight: 80,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: nx,
    style: {
      marginTop: 16
    }
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter / Space"))), !fb && /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 80
    }
  }))));
}

// ── Sentences ─────────────────────────────────────────────────────────────────
// ── Noun Table (two-mode: full-screen modal default + draggable widget) ──────
function NounTable(_ref62) {
  var onClose = _ref62.onClose,
    _ref62$onModeChange = _ref62.onModeChange,
    onModeChange = _ref62$onModeChange === void 0 ? function () {} : _ref62$onModeChange;
  var _React$useState = React.useState(true),
    _React$useState2 = _slicedToArray(_React$useState, 2),
    neuters = _React$useState2[0],
    setNeuters = _React$useState2[1]; // modal default: on
  var _React$useState3 = React.useState(true),
    _React$useState4 = _slicedToArray(_React$useState3, 2),
    d4 = _React$useState4[0],
    setD4 = _React$useState4[1];
  var _React$useState5 = React.useState(true),
    _React$useState6 = _slicedToArray(_React$useState5, 2),
    d5 = _React$useState6[0],
    setD5 = _React$useState6[1];
  var _React$useState7 = React.useState('modal'),
    _React$useState8 = _slicedToArray(_React$useState7, 2),
    tableMode = _React$useState8[0],
    setTableMode = _React$useState8[1]; // 'modal' | 'widget'
  var _React$useState9 = React.useState(null),
    _React$useState0 = _slicedToArray(_React$useState9, 2),
    hoverEnding = _React$useState0[0],
    setHoverEnding = _React$useState0[1];
  // Compare endings ignoring vowel length (macrons)
  var normE = function normE(s) {
    return s.replace(/[āàáâ]/g, 'a').replace(/[ēèéê]/g, 'e').replace(/[īìíî]/g, 'i').replace(/[ōòóô]/g, 'o').replace(/[ūùúû]/g, 'u').toLowerCase();
  };
  var _React$useState1 = React.useState({
      x: Math.max(0, window.innerWidth - 340),
      y: 70
    }),
    _React$useState10 = _slicedToArray(_React$useState1, 2),
    pos = _React$useState10[0],
    setPos = _React$useState10[1];
  var dragRef = React.useRef(null);
  React.useEffect(function () {
    var onMove = function onMove(e) {
      if (!dragRef.current) return;
      if (e.cancelable) e.preventDefault();
      var cx = e.touches ? e.touches[0].clientX : e.clientX;
      var cy = e.touches ? e.touches[0].clientY : e.clientY;
      var _dragRef$current = dragRef.current,
        startX = _dragRef$current.startX,
        startY = _dragRef$current.startY,
        ox = _dragRef$current.ox,
        oy = _dragRef$current.oy;
      setPos({
        x: Math.max(0, Math.min(ox + (cx - startX), window.innerWidth - 350)),
        y: Math.max(0, oy + (cy - startY))
      });
    };
    var onUp = function onUp() {
      dragRef.current = null;
    };
    window.addEventListener('mousemove', onMove);
    window.addEventListener('mouseup', onUp);
    window.addEventListener('touchmove', onMove, {
      passive: false
    });
    window.addEventListener('touchend', onUp);
    return function () {
      window.removeEventListener('mousemove', onMove);
      window.removeEventListener('mouseup', onUp);
      window.removeEventListener('touchmove', onMove);
      window.removeEventListener('touchend', onUp);
    };
  }, []);
  var startDrag = function startDrag(e) {
    var cx = e.touches ? e.touches[0].clientX : e.clientX;
    var cy = e.touches ? e.touches[0].clientY : e.clientY;
    dragRef.current = {
      startX: cx,
      startY: cy,
      ox: pos.x,
      oy: pos.y
    };
    e.preventDefault();
  };
  var sg = [{
    d1: '-a',
    d2m: '-us',
    d2n: '-um',
    d3: '—',
    d3n: '—',
    d4: '-us',
    d5: '-es'
  }, {
    d1: '-am',
    d2m: '-um',
    d2n: '-um',
    d3: '-em',
    d3n: '—',
    d4: '-um',
    d5: '-em'
  }, {
    d1: '-ae',
    d2m: '-i',
    d2n: '-i',
    d3: '-is',
    d3n: '-is',
    d4: '-us',
    d5: '-ei'
  }, {
    d1: '-ae',
    d2m: '-o',
    d2n: '-o',
    d3: '-i',
    d3n: '-i',
    d4: '-ui',
    d5: '-ei'
  }, {
    d1: '-a',
    d2m: '-o',
    d2n: '-o',
    d3: '-e',
    d3n: '-e',
    d4: '-u',
    d5: '-e'
  }];
  var pl = [{
    d1: '-ae',
    d2m: '-i',
    d2n: '-a',
    d3: '-es',
    d3n: '-a',
    d4: '-us',
    d5: '-es'
  }, {
    d1: '-as',
    d2m: '-os',
    d2n: '-a',
    d3: '-es',
    d3n: '-a',
    d4: '-us',
    d5: '-es'
  }, {
    d1: '-arum',
    d2m: '-orum',
    d2n: '-orum',
    d3: '-um',
    d3n: '-um',
    d4: '-uum',
    d5: '-erum'
  }, {
    d1: '-is',
    d2m: '-is',
    d2n: '-is',
    d3: '-ibus',
    d3n: '-ibus',
    d4: '-ibus',
    d5: '-ebus'
  }, {
    d1: '-is',
    d2m: '-is',
    d2n: '-is',
    d3: '-ibus',
    d3n: '-ibus',
    d4: '-ibus',
    d5: '-ebus'
  }];
  var cols = [{
    k: 'd1',
    hd: '1ST',
    sub: 'FEM.',
    grp: 1,
    neut: false
  }, {
    k: 'd2m',
    hd: '2ND',
    sub: 'MASC.',
    grp: 2,
    neut: false
  }].concat(_toConsumableArray(neuters ? [{
    k: 'd2n',
    hd: '2ND',
    sub: 'NEUT.',
    grp: 2,
    neut: true
  }] : []), [{
    k: 'd3',
    hd: '3RD',
    sub: 'M. / F.',
    grp: 3,
    neut: false
  }], _toConsumableArray(neuters ? [{
    k: 'd3n',
    hd: '3RD',
    sub: 'NEUT.',
    grp: 3,
    neut: true
  }] : []), _toConsumableArray(d4 ? [{
    k: 'd4',
    hd: '4TH',
    sub: 'M. / F.',
    grp: 4,
    neut: false
  }] : []), _toConsumableArray(d5 ? [{
    k: 'd5',
    hd: '5TH',
    sub: 'FEM.',
    grp: 5,
    neut: false
  }] : []));
  var getBL = function getBL(col, i) {
    if (i === 0) return 'none';
    var prev = cols[i - 1];
    if (prev.grp !== col.grp) return '2px solid #7C3AED';
    if (col.neut) return '2px dashed #C4B5FD';
    return 'none';
  };
  var isModal = tableMode === 'modal';
  var CW = isModal ? 96 : 50;
  var caseW = isModal ? 150 : 50;
  var cbSize = isModal ? '1rem' : '0.7rem';
  var cellSize = isModal ? '1.45rem' : '0.95rem';
  var caseNames = isModal ? ['NOMINATIVE', 'ACCUSATIVE', 'GENITIVE', 'DATIVE', 'ABLATIVE'] : ['NOM', 'ACC', 'GEN', 'DAT', 'ABL'];
  var cellSt = function cellSt(col, i) {
    return {
      textAlign: 'center',
      width: CW,
      minWidth: CW,
      maxWidth: CW,
      padding: '4px 0',
      fontFamily: 'Crimson Text,serif',
      fontStyle: 'italic',
      fontWeight: 700,
      fontSize: cellSize,
      color: '#111',
      borderLeft: getBL(col, i)
    };
  };
  var caseSt = {
    width: caseW,
    minWidth: caseW,
    padding: '4px 6px 4px 0',
    fontWeight: 800,
    fontSize: cbSize,
    color: '#7C3AED',
    textAlign: 'right',
    whiteSpace: 'nowrap',
    letterSpacing: '0.04em'
  };
  var hdSt = function hdSt(col, i) {
    return {
      textAlign: 'center',
      width: CW,
      minWidth: CW,
      maxWidth: CW,
      padding: '5px 0',
      borderBottom: '2px solid #7C3AED',
      color: '#7C3AED',
      fontSize: '0.62rem',
      fontWeight: 900,
      whiteSpace: 'nowrap',
      letterSpacing: '0.07em',
      borderLeft: getBL(col, i)
    };
  };
  var secSt = {
    padding: '5px 0 2px',
    fontWeight: 800,
    fontSize: '0.6rem',
    color: '#A78BFA',
    textTransform: 'uppercase',
    letterSpacing: '0.09em'
  };
  var renderRows = function renderRows(rows) {
    return rows.map(function (r, i) {
      return /*#__PURE__*/React.createElement("tr", {
        key: i,
        style: {
          background: i % 2 === 0 ? '#FAF8FF' : 'var(--white)'
        }
      }, /*#__PURE__*/React.createElement("td", {
        style: caseSt
      }, caseNames[i]), cols.map(function (c, ci) {
        var v = r[c.k];
        var hilite = hoverEnding !== null && normE(v) === normE(hoverEnding);
        return /*#__PURE__*/React.createElement("td", {
          key: c.k,
          style: _objectSpread(_objectSpread({}, cellSt(c, ci)), {}, {
            background: hilite ? '#ede9fe' : 'inherit',
            color: hilite ? '#7C3AED' : '#111',
            transition: 'background .1s,color .1s',
            cursor: 'default',
            borderRadius: hilite ? 3 : 0
          }),
          onMouseEnter: function onMouseEnter() {
            return setHoverEnding(v);
          },
          onMouseLeave: function onMouseLeave() {
            return setHoverEnding(null);
          }
        }, v);
      }));
    });
  };
  var checkboxes = /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 10,
      marginBottom: 8,
      flexWrap: 'wrap',
      alignItems: 'center'
    }
  }, [['neuters', neuters, setNeuters, 'Neuters'], ['d4', d4, setD4, '4th'], ['d5', d5, setD5, '5th']].map(function (_ref63) {
    var _ref64 = _slicedToArray(_ref63, 4),
      k = _ref64[0],
      v = _ref64[1],
      sv = _ref64[2],
      lbl = _ref64[3];
    return /*#__PURE__*/React.createElement("label", {
      key: k,
      style: {
        display: 'flex',
        alignItems: 'center',
        gap: 4,
        cursor: 'pointer',
        fontSize: isModal ? '0.8rem' : '0.72rem',
        fontWeight: 700,
        color: '#374151',
        userSelect: 'none'
      }
    }, /*#__PURE__*/React.createElement("input", {
      type: "checkbox",
      checked: v,
      onChange: function onChange(e) {
        return sv(e.target.checked);
      },
      style: {
        width: isModal ? 13 : 11,
        height: isModal ? 13 : 11,
        cursor: 'pointer',
        accentColor: '#7C3AED'
      }
    }), lbl);
  }));
  var tableEl = /*#__PURE__*/React.createElement("table", {
    style: {
      borderCollapse: 'collapse'
    }
  }, /*#__PURE__*/React.createElement("thead", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("th", {
    style: _objectSpread(_objectSpread({}, caseSt), {}, {
      borderBottom: '2px solid #7C3AED',
      textAlign: 'right'
    })
  }), cols.map(function (c, ci) {
    return /*#__PURE__*/React.createElement("th", {
      key: c.k,
      style: hdSt(c, ci)
    }, c.hd, /*#__PURE__*/React.createElement("br", null), /*#__PURE__*/React.createElement("span", {
      style: {
        fontWeight: 600,
        color: '#A78BFA',
        fontSize: '0.54rem',
        letterSpacing: '0.01em'
      }
    }, c.sub));
  }))), /*#__PURE__*/React.createElement("tbody", null, /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("td", {
    colSpan: cols.length + 1,
    style: secSt
  }, "Singular")), renderRows(sg), /*#__PURE__*/React.createElement("tr", null, /*#__PURE__*/React.createElement("td", {
    colSpan: cols.length + 1,
    style: _objectSpread(_objectSpread({}, secSt), {}, {
      paddingTop: 8
    })
  }, "Plural")), renderRows(pl)));
  if (isModal) return /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'fixed',
      inset: 0,
      background: 'rgba(0,0,0,0.55)',
      zIndex: 9200,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    },
    onClick: function onClick(e) {
      if (e.target === e.currentTarget) onClose();
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      background: 'var(--white)',
      borderRadius: 16,
      boxShadow: '0 12px 60px rgba(124,58,237,0.3)',
      border: '2px solid #7C3AED',
      width: 'min(98vw,1200px)',
      maxHeight: '95vh',
      overflowY: 'auto',
      overflowX: 'auto'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      background: '#7C3AED',
      color: 'white',
      padding: '12px 20px',
      borderRadius: '14px 14px 0 0',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      gap: 12,
      userSelect: 'none',
      position: 'sticky',
      top: 0,
      zIndex: 1
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 900,
      fontSize: '1rem',
      letterSpacing: '0.08em',
      textTransform: 'uppercase'
    }
  }, "\u283F Noun Endings"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 6,
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("button", {
    onClick: function onClick() {
      setTableMode('widget');
      setNeuters(false);
      setD4(false);
      setD5(false);
      onModeChange('widget');
    },
    style: {
      padding: '4px 12px',
      borderRadius: 4,
      border: '1.5px solid rgba(255,255,255,0.6)',
      background: 'transparent',
      color: 'white',
      fontSize: '0.75rem',
      fontWeight: 800,
      cursor: 'pointer',
      letterSpacing: '0.04em',
      textTransform: 'uppercase',
      whiteSpace: 'nowrap'
    }
  }, "Widget \u25BE"), /*#__PURE__*/React.createElement("button", {
    onClick: onClose,
    style: {
      background: 'rgba(255,255,255,0.15)',
      border: '1px solid rgba(255,255,255,0.35)',
      borderRadius: 6,
      color: 'white',
      fontSize: '1.1rem',
      lineHeight: 1,
      cursor: 'pointer',
      padding: '2px 8px',
      fontWeight: 700
    }
  }, "\xD7"))), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '16px 24px 20px'
    }
  }, checkboxes, tableEl)));
  return /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'fixed',
      left: pos.x,
      top: pos.y,
      zIndex: 9100,
      width: 'max-content',
      boxShadow: '0 8px 40px rgba(124,58,237,0.2)',
      borderRadius: 14,
      background: 'var(--white)',
      border: '2px solid #7C3AED'
    }
  }, /*#__PURE__*/React.createElement("div", {
    onMouseDown: startDrag,
    onTouchStart: startDrag,
    style: {
      background: '#7C3AED',
      color: 'white',
      padding: '7px 12px',
      borderRadius: '12px 12px 0 0',
      cursor: 'grab',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      userSelect: 'none',
      gap: 8
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 900,
      fontSize: '0.75rem',
      letterSpacing: '0.08em',
      textTransform: 'uppercase',
      flexShrink: 0
    }
  }, "\u283F Noun Endings"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 4,
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("button", {
    onMouseDown: function onMouseDown(e) {
      return e.stopPropagation();
    },
    onClick: function onClick() {
      setTableMode('modal');
      setNeuters(true);
      setD4(true);
      setD5(true);
      onModeChange('modal');
    },
    style: {
      padding: '2px 8px',
      borderRadius: 4,
      border: '1px solid rgba(255,255,255,0.5)',
      background: 'transparent',
      color: 'white',
      fontSize: '0.6rem',
      fontWeight: 800,
      cursor: 'pointer',
      letterSpacing: '0.04em',
      textTransform: 'uppercase',
      whiteSpace: 'nowrap'
    }
  }, "Full \u25B4"), /*#__PURE__*/React.createElement("button", {
    onClick: onClose,
    style: {
      background: 'rgba(255,255,255,0.15)',
      border: '1px solid rgba(255,255,255,0.35)',
      borderRadius: 6,
      color: 'white',
      fontSize: '1rem',
      lineHeight: 1,
      cursor: 'pointer',
      padding: '1px 7px',
      fontWeight: 700,
      marginLeft: 2
    }
  }, "\xD7"))), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '8px 12px 10px'
    }
  }, checkboxes, tableEl));
}
function Sentences(_ref65) {
  var _q$latin, _q$latin2;
  var pupil = _ref65.pupil,
    set = _ref65.set,
    qs = _ref65.qs,
    isPreview = _ref65.isPreview,
    onDone = _ref65.onDone,
    addC = _ref65.addC,
    addW = _ref65.addW,
    pct = _ref65.pct;
  var _useState271 = useState(false),
    _useState272 = _slicedToArray(_useState271, 2),
    showNounTable = _useState272[0],
    setShowNounTable = _useState272[1];
  var _useState273 = useState('modal'),
    _useState274 = _slicedToArray(_useState273, 2),
    ntMode = _useState274[0],
    setNtMode = _useState274[1]; // track widget vs modal for layout
  var _useState275 = useState(function () {
      return _toConsumableArray(qs);
    }),
    _useState276 = _slicedToArray(_useState275, 2),
    queue = _useState276[0],
    setQueue = _useState276[1];
  var _useState277 = useState(0),
    _useState278 = _slicedToArray(_useState277, 2),
    qIdx = _useState278[0],
    setQIdx = _useState278[1];
  var _useState279 = useState(''),
    _useState280 = _slicedToArray(_useState279, 2),
    ans = _useState280[0],
    setAns = _useState280[1];
  var _useState281 = useState(null),
    _useState282 = _slicedToArray(_useState281, 2),
    fb = _useState282[0],
    setFb = _useState282[1];
  var _useState283 = useState(false),
    _useState284 = _slicedToArray(_useState283, 2),
    retype = _useState284[0],
    setRetype = _useState284[1];
  var _useState285 = useState(''),
    _useState286 = _slicedToArray(_useState285, 2),
    rtAns = _useState286[0],
    setRtAns = _useState286[1];
  var _useState287 = useState(null),
    _useState288 = _slicedToArray(_useState287, 2),
    rtFb = _useState288[0],
    setRtFb = _useState288[1];
  var _useState289 = useState(false),
    _useState290 = _slicedToArray(_useState289, 2),
    busy = _useState290[0],
    setBusy = _useState290[1];
  var inRef = useRef();
  var rtRef = useRef();
  var bodyRef = useRef();
  var q = queue[qIdx];
  useEffect(function () {
    var _inRef$current3, _rtRef$current3;
    if (!fb) (_inRef$current3 = inRef.current) === null || _inRef$current3 === void 0 || _inRef$current3.focus();
    if (retype) (_rtRef$current3 = rtRef.current) === null || _rtRef$current3 === void 0 || _rtRef$current3.focus();
  }, [qIdx, fb, retype]);
  useEffect(function () {
    if (fb && bodyRef.current) bodyRef.current.scrollTop = 0;
  }, [fb]);
  var submit = /*#__PURE__*/function () {
    var _ref66 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee27() {
      var res;
      return _regenerator().w(function (_context27) {
        while (1) switch (_context27.n) {
          case 0:
            if (!busy) {
              _context27.n = 1;
              break;
            }
            return _context27.a(2);
          case 1:
            setBusy(true);
            _context27.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'sentence',
              question_text: q.latin,
              pupil_answer: ans,
              correct_answer: '',
              sentence_index: q.original_index
            });
          case 2:
            res = _context27.v;
            setFb(res);
            if (res.counts_as_correct) {
              if (!q.failed) addC();
            } else {
              if (!q.failed) addW({
                latin: q.latin,
                correct: res.correct_answer
              });
              setQueue(function (prev) {
                return [].concat(_toConsumableArray(prev), [_objectSpread(_objectSpread({}, q), {}, {
                  failed: true
                })]);
              });
              setRetype(true);
            }
            setBusy(false);
          case 3:
            return _context27.a(2);
        }
      }, _callee27);
    }));
    return function submit() {
      return _ref66.apply(this, arguments);
    };
  }();
  var rtSubmit = /*#__PURE__*/function () {
    var _ref67 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee28() {
      var res;
      return _regenerator().w(function (_context28) {
        while (1) switch (_context28.n) {
          case 0:
            if (!busy) {
              _context28.n = 1;
              break;
            }
            return _context28.a(2);
          case 1:
            if (rtAns.trim()) {
              _context28.n = 2;
              break;
            }
            setRtFb('Type your answer first.');
            return _context28.a(2);
          case 2:
            setBusy(true);
            _context28.n = 3;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'sentence',
              question_text: q.latin,
              pupil_answer: rtAns,
              correct_answer: '',
              sentence_index: q.original_index
            });
          case 3:
            res = _context28.v;
            if (res.counts_as_correct) {
              nx();
            } else setRtFb(res.message);
            setBusy(false);
          case 4:
            return _context28.a(2);
        }
      }, _callee28);
    }));
    return function rtSubmit() {
      return _ref67.apply(this, arguments);
    };
  }();
  // CRITICAL: nx clears ALL state before moving on
  var nx = function nx() {
    resetScroll();
    setAns('');
    setFb(null);
    setRetype(false);
    setRtAns('');
    setRtFb(null);
    if (qIdx + 1 >= queue.length) onDone();else setQIdx(function (i) {
      return i + 1;
    });
  };
  useEffect(function () {
    // Only bind Enter to nx/submit if NOT in retype mode (retype has its own button)
    var h = function h(e) {
      // Ctrl+Alt+K: mark this question CORRECT and skip ahead (teacher override)
      if (e.ctrlKey && e.altKey && e.code === "KeyK") {
        e.preventDefault();
        e.stopPropagation();
        if (!(q !== null && q !== void 0 && q.failed)) addC();
        nx();
        return;
      }
      // Ctrl+Alt+J: skip without recording (neither correct nor wrong)
      if (e.ctrlKey && e.altKey && e.code === "KeyJ") {
        e.preventDefault();
        e.stopPropagation();
        nx();
        return;
      }
      if (e.key === 'Enter' || e.code === 'Space' && e.target.tagName !== 'INPUT') {
        if (e.code === 'Space') e.preventDefault();
        if (retype) {
          rtSubmit();
          return;
        }
        if (fb && !retype) nx();else if (!fb) submit();
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  }, [qIdx, fb, retype, ans, rtAns, queue]);
  // Token-set comparison: "to, at, towards" == "to, towards, at" → no ideal answer shown
  var normTokenSet = function normTokenSet(s) {
    return new Set(s.trim().toLowerCase().replace(/[^a-z0-9, ]/g, '').split(/\s*,\s*/).map(function (p) {
      return p.replace(/\s+/g, ' ').trim();
    }).filter(Boolean));
  };
  var sameTokens = function sameTokens(a, b) {
    var sa = normTokenSet(a),
      sb = normTokenSet(b);
    if (sa.size !== sb.size) return false;
    var _iterator5 = _createForOfIteratorHelper(sa),
      _step5;
    try {
      for (_iterator5.s(); !(_step5 = _iterator5.n()).done;) {
        var x = _step5.value;
        if (!sb.has(x)) return false;
      }
    } catch (err) {
      _iterator5.e(err);
    } finally {
      _iterator5.f();
    }
    return true;
  };
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, showNounTable && /*#__PURE__*/React.createElement(NounTable, {
    onClose: function onClose() {
      setShowNounTable(false);
      setNtMode('modal');
    },
    onModeChange: setNtMode
  }), /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement("button", {
    onClick: function onClick() {
      return setShowNounTable(function (t) {
        return !t;
      });
    },
    className: "noun-table-chip".concat(showNounTable ? ' active' : ''),
    title: "Noun endings table"
  }, /*#__PURE__*/React.createElement("svg", {
    viewBox: "0 0 14 14",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: "1.8",
    width: "14",
    height: "14"
  }, /*#__PURE__*/React.createElement("rect", {
    x: "1",
    y: "2",
    width: "12",
    height: "10",
    rx: "1.5"
  }), /*#__PURE__*/React.createElement("line", {
    x1: "1",
    y1: "5.5",
    x2: "13",
    y2: "5.5"
  }), /*#__PURE__*/React.createElement("line", {
    x1: "1",
    y1: "8.5",
    x2: "13",
    y2: "8.5"
  }), /*#__PURE__*/React.createElement("line", {
    x1: "5",
    y1: "2",
    x2: "5",
    y2: "12"
  }), /*#__PURE__*/React.createElement("line", {
    x1: "9",
    y1: "2",
    x2: "9",
    y2: "12"
  })), "Noun table"), /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    ref: bodyRef,
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      paddingRight: showNounTable && ntMode === 'widget' ? 364 : 0,
      transition: 'padding-right 0.25s',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      width: '100%'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 58,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center'
    }
  }, (q === null || q === void 0 ? void 0 : q.failed) && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: '#f97316',
      border: '2px solid #ea580c',
      color: 'white',
      padding: '10px 24px',
      borderRadius: 12,
      fontWeight: 800,
      fontSize: '1.1rem'
    }
  }, "Try this again \u2014 you got it wrong before.")), !fb ? /*#__PURE__*/React.createElement("div", {
    style: {
      background: '#fff',
      border: '3px solid var(--lgrey)',
      borderRadius: 24,
      padding: '48px 56px 40px',
      boxShadow: '0 4px 16px rgba(0,33,71,.04)',
      maxWidth: 980,
      width: '100%',
      boxSizing: 'border-box',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      marginBottom: 40
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      fontWeight: 700,
      fontSize: '1.2rem',
      textAlign: 'center',
      margin: '0 0 16px'
    }
  }, "Translate into English:"), /*#__PURE__*/React.createElement("h1", {
    className: "latin dynamic-latin",
    style: {
      fontSize: (q === null || q === void 0 || (_q$latin = q.latin) === null || _q$latin === void 0 ? void 0 : _q$latin.length) > 30 ? '2.6rem' : '3.6rem',
      margin: '0 0 44px',
      textAlign: 'center',
      width: '100%'
    }
  }, q === null || q === void 0 ? void 0 : q.latin), /*#__PURE__*/React.createElement("input", {
    ref: inRef,
    className: "typed-input",
    style: {
      maxWidth: 780
    },
    disabled: busy,
    value: ans,
    onChange: function onChange(e) {
      return setAns(e.target.value);
    },
    placeholder: "..."
  }), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: submit,
    style: {
      marginTop: 28
    }
  }, "Check", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter"))) : /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      width: '100%',
      paddingBottom: 80
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      fontWeight: 700,
      fontSize: '1.2rem',
      textAlign: 'center',
      width: '100%',
      margin: '0 0 16px'
    }
  }, "Translate into English:"), /*#__PURE__*/React.createElement("h1", {
    className: "latin dynamic-latin",
    style: {
      fontSize: (q === null || q === void 0 || (_q$latin2 = q.latin) === null || _q$latin2 === void 0 ? void 0 : _q$latin2.length) > 30 ? '2.6rem' : '3.6rem',
      position: 'sticky',
      top: 0,
      zIndex: 5,
      background: 'var(--card)',
      paddingTop: 16,
      paddingBottom: 16,
      paddingLeft: 32,
      paddingRight: 32,
      marginTop: 0,
      marginBottom: 24,
      borderRadius: 14,
      boxShadow: '0 4px 12px rgba(0,33,71,.08)',
      border: 'none',
      textAlign: 'center',
      width: '100%'
    }
  }, q === null || q === void 0 ? void 0 : q.latin), retype && ans && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 6,
      marginBottom: 10,
      padding: '16px 40px',
      background: '#fef2f2',
      border: '2px solid #dc2626',
      borderRadius: 14,
      textAlign: 'left',
      maxWidth: 900,
      width: '100%',
      boxSizing: 'border-box'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      fontSize: '0.82rem',
      color: '#dc2626',
      marginBottom: 4,
      textTransform: 'uppercase',
      letterSpacing: '0.05em'
    }
  }, "Your answer"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.2rem',
      fontWeight: 700,
      color: 'var(--dark)',
      textDecoration: 'line-through',
      opacity: 0.85
    }
  }, ans)), retype && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginBottom: 10,
      padding: '16px 40px',
      background: '#f0fdf4',
      border: '2px solid #16a34a',
      borderRadius: 14,
      textAlign: 'left',
      maxWidth: 900,
      width: '100%',
      boxSizing: 'border-box',
      userSelect: 'none',
      WebkitUserSelect: 'none'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      fontSize: '0.85rem',
      color: '#16a34a',
      marginBottom: 6,
      textTransform: 'uppercase',
      letterSpacing: '0.05em'
    }
  }, "The correct answer is"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.4rem',
      fontWeight: 800,
      color: 'var(--dark)'
    }
  }, fb === null || fb === void 0 ? void 0 : fb.correct_answer)), retype && (q === null || q === void 0 ? void 0 : q.explanation) && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginBottom: 14,
      padding: '16px 40px',
      background: '#F5F3FF',
      border: '2px solid #7C3AED',
      borderRadius: 12,
      maxWidth: 900,
      width: '100%',
      boxSizing: 'border-box',
      textAlign: 'left',
      lineHeight: 1.7
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      fontSize: '0.82rem',
      color: '#7C3AED',
      textTransform: 'uppercase',
      letterSpacing: '0.06em',
      marginBottom: 8
    }
  }, "Explanation"), renderExplanation(q.explanation)), !retype && /*#__PURE__*/React.createElement("input", {
    className: "typed-input ".concat(fb.counts_as_correct ? 'ok' : 'bad'),
    style: {
      maxWidth: 900
    },
    value: ans,
    disabled: true
  }), !retype && /*#__PURE__*/React.createElement("div", {
    className: "feedback anim-fade ".concat(fb.counts_as_correct ? fb.is_typo ? 'warn' : 'ok' : 'bad'),
    style: {
      maxWidth: 900,
      width: '100%',
      boxSizing: 'border-box'
    }
  }, renderText(fb.message)), fb.counts_as_correct && !retype && fb.correct_answer && !sameTokens(ans, fb.correct_answer) && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 16,
      padding: '16px 40px',
      background: '#f0fdf4',
      border: '2px solid #16a34a',
      borderRadius: 12,
      textAlign: 'left',
      maxWidth: 900,
      width: '100%',
      boxSizing: 'border-box'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 700,
      fontSize: '0.8rem',
      color: '#16a34a',
      textTransform: 'uppercase',
      letterSpacing: '0.05em',
      marginBottom: 4
    }
  }, "Ideal answer"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.2rem',
      fontWeight: 800,
      color: 'var(--dark)'
    }
  }, fb.correct_answer)), !retype && (q === null || q === void 0 ? void 0 : q.explanation) && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 16,
      padding: '16px 40px',
      background: '#F5F3FF',
      border: '2px solid #7C3AED',
      borderRadius: 12,
      maxWidth: 900,
      width: '100%',
      boxSizing: 'border-box',
      textAlign: 'left',
      lineHeight: 1.8
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      fontSize: '0.82rem',
      color: '#7C3AED',
      textTransform: 'uppercase',
      letterSpacing: '0.06em',
      marginBottom: 10
    }
  }, "Explanation"), renderExplanation(q.explanation)), !fb.counts_as_correct && !retype && fb.correct_answer && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 16,
      padding: '16px 40px',
      background: '#f0fdf4',
      border: '2px solid #16a34a',
      borderRadius: 12,
      maxWidth: 900,
      width: '100%',
      boxSizing: 'border-box',
      textAlign: 'left'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 700,
      fontSize: '0.85rem',
      color: '#16a34a',
      marginBottom: 6,
      textTransform: 'uppercase',
      letterSpacing: '0.05em'
    }
  }, "Correct answer"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.3rem',
      fontWeight: 800,
      color: 'var(--dark)'
    }
  }, fb.correct_answer)), fb.counts_as_correct && !retype && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary anim-fade",
    onClick: nx,
    style: {
      marginTop: 24
    }
  }, "Continue", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter / Space")), retype && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 8,
      width: '100%',
      maxWidth: 900,
      padding: '20px 40px',
      background: '#FFFBEB',
      border: '2px solid #F59E0B',
      borderRadius: 18,
      boxSizing: 'border-box'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '0.85rem',
      marginBottom: 12,
      fontWeight: 800,
      color: '#92400E',
      textTransform: 'uppercase',
      letterSpacing: '0.05em'
    }
  }, "Type the correct answer"), /*#__PURE__*/React.createElement("input", {
    ref: rtRef,
    className: "typed-input",
    style: {
      maxWidth: '900px',
      borderColor: rtFb ? 'var(--red-bright)' : ''
    },
    value: rtAns,
    onChange: function onChange(e) {
      setRtAns(e.target.value);
      setRtFb(null);
    },
    onPaste: function onPaste(e) {
      return e.preventDefault();
    },
    placeholder: "..."
  }), rtFb && /*#__PURE__*/React.createElement("div", {
    style: {
      color: 'var(--red-bright)',
      marginTop: 12,
      fontWeight: 700
    }
  }, renderText(rtFb)), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-outline",
    disabled: busy,
    onClick: rtSubmit,
    style: {
      marginTop: 16
    }
  }, "Check", /*#__PURE__*/React.createElement("span", {
    className: "keyhint"
  }, "Enter"))))))));
}

// ── TF Typed (typed phase after TranslateForm MCQ) ───────────────────────────
// Shows the Latin form, asks for English translation (typed)
function TFTyped(_ref68) {
  var pupil = _ref68.pupil,
    set = _ref68.set,
    qs = _ref68.qs,
    isPreview = _ref68.isPreview,
    onDone = _ref68.onDone,
    addC = _ref68.addC,
    addW = _ref68.addW,
    pct = _ref68.pct;
  var _useState291 = useState(function () {
      return _toConsumableArray(qs);
    }),
    _useState292 = _slicedToArray(_useState291, 2),
    queue = _useState292[0],
    setQueue = _useState292[1];
  var _useState293 = useState(0),
    _useState294 = _slicedToArray(_useState293, 2),
    qIdx = _useState294[0],
    setQIdx = _useState294[1];
  var _useState295 = useState(''),
    _useState296 = _slicedToArray(_useState295, 2),
    ans = _useState296[0],
    setAns = _useState296[1];
  var _useState297 = useState(null),
    _useState298 = _slicedToArray(_useState297, 2),
    fb = _useState298[0],
    setFb = _useState298[1];
  var _useState299 = useState(false),
    _useState300 = _slicedToArray(_useState299, 2),
    retype = _useState300[0],
    setRetype = _useState300[1];
  var _useState301 = useState(''),
    _useState302 = _slicedToArray(_useState301, 2),
    rtAns = _useState302[0],
    setRtAns = _useState302[1];
  var _useState303 = useState(null),
    _useState304 = _slicedToArray(_useState303, 2),
    rtFb = _useState304[0],
    setRtFb = _useState304[1];
  var _useState305 = useState(false),
    _useState306 = _slicedToArray(_useState305, 2),
    busy = _useState306[0],
    setBusy = _useState306[1];
  var inRef = useRef();
  var rtRef = useRef();
  var q = queue[qIdx];
  useEffect(function () {
    var _inRef$current4, _rtRef$current4;
    if (!fb) (_inRef$current4 = inRef.current) === null || _inRef$current4 === void 0 || _inRef$current4.focus();
    if (retype) (_rtRef$current4 = rtRef.current) === null || _rtRef$current4 === void 0 || _rtRef$current4.focus();
  }, [qIdx, fb, retype]);
  var submit = /*#__PURE__*/function () {
    var _ref69 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee29() {
      var res;
      return _regenerator().w(function (_context29) {
        while (1) switch (_context29.n) {
          case 0:
            if (!(busy || !q)) {
              _context29.n = 1;
              break;
            }
            return _context29.a(2);
          case 1:
            setBusy(true);
            _context29.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'vocab',
              question_text: q.form,
              pupil_answer: ans,
              correct_answer: q.correct
            });
          case 2:
            res = _context29.v;
            setFb(res);
            if (res.counts_as_correct) {
              if (!q.failed) addC();
            } else {
              if (!q.failed) addW({
                latin: q.form,
                correct: q.correct
              });
              setQueue(function (prev) {
                return [].concat(_toConsumableArray(prev), [_objectSpread(_objectSpread({}, q), {}, {
                  failed: true
                })]);
              });
              setRetype(true);
            }
            setBusy(false);
          case 3:
            return _context29.a(2);
        }
      }, _callee29);
    }));
    return function submit() {
      return _ref69.apply(this, arguments);
    };
  }();
  var rtSubmit = /*#__PURE__*/function () {
    var _ref70 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee30() {
      var res;
      return _regenerator().w(function (_context30) {
        while (1) switch (_context30.n) {
          case 0:
            if (!busy) {
              _context30.n = 1;
              break;
            }
            return _context30.a(2);
          case 1:
            if (rtAns.trim()) {
              _context30.n = 2;
              break;
            }
            setRtFb('Type your answer first.');
            return _context30.a(2);
          case 2:
            setBusy(true);
            _context30.n = 3;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'vocab',
              question_text: q.form,
              pupil_answer: rtAns,
              correct_answer: q.correct
            });
          case 3:
            res = _context30.v;
            if (res.counts_as_correct) {
              nx();
            } else setRtFb('Not quite. Try again.');
            setBusy(false);
          case 4:
            return _context30.a(2);
        }
      }, _callee30);
    }));
    return function rtSubmit() {
      return _ref70.apply(this, arguments);
    };
  }();
  var nx = function nx() {
    resetScroll();
    setAns('');
    setFb(null);
    setRetype(false);
    setRtAns('');
    setRtFb(null);
    if (qIdx + 1 >= queue.length) onDone();else setQIdx(function (i) {
      return i + 1;
    });
  };
  useEffect(function () {
    var h = function h(e) {
      if (e.key === 'Enter') {
        if (retype) rtSubmit();else if (fb && !retype) nx();else if (!fb) submit();
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  if (!q) return null;
  var isRetry = q.failed;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 40,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: 8
    }
  }, isRetry && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      background: '#f97316',
      border: '2px solid #ea580c',
      borderRadius: 10,
      padding: '6px 16px',
      fontWeight: 800,
      color: 'white',
      fontSize: '0.9rem',
      display: 'inline-block'
    }
  }, "Try this again \u2014 you got it wrong before.")), /*#__PURE__*/React.createElement("h1", {
    className: "latin dynamic-latin",
    style: {
      fontSize: '4rem'
    }
  }, q.form), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 40,
      fontWeight: 700,
      fontSize: '1.3rem',
      marginTop: 8
    }
  }, "Type the English translation"), /*#__PURE__*/React.createElement("div", {
    style: {
      minHeight: 320,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      width: '100%'
    }
  }, !fb ? /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("input", {
    ref: inRef,
    className: "typed-input",
    disabled: busy,
    value: ans,
    onChange: function onChange(e) {
      return setAns(e.target.value);
    },
    placeholder: "..."
  }), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: busy,
    onClick: submit,
    style: {
      marginTop: 30
    }
  }, "Check", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter"))) : /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("input", {
    className: "typed-input ".concat(fb.counts_as_correct ? 'ok' : 'bad'),
    value: ans,
    disabled: true
  }), !retype && /*#__PURE__*/React.createElement("div", {
    className: "feedback anim-fade ".concat(fb.counts_as_correct ? fb.is_typo ? 'warn' : 'ok' : 'bad'),
    style: {
      maxWidth: 800,
      width: '100%',
      boxSizing: 'border-box'
    }
  }, renderText(fb.message)), fb.counts_as_correct && !retype && fb.correct_answer && ans.trim().toLowerCase().replace(/[^a-z0-9 /]/g, '').replace(/\s+/g, ' ').trim() !== fb.correct_answer.trim().toLowerCase().replace(/[^a-z0-9 /]/g, '').replace(/\s+/g, ' ').trim() && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 16,
      padding: '12px 16px',
      background: '#f0fdf4',
      border: '2px solid #16a34a',
      borderRadius: 12,
      textAlign: 'left',
      maxWidth: 800,
      width: '100%'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 700,
      fontSize: '0.8rem',
      color: '#16a34a',
      textTransform: 'uppercase',
      letterSpacing: '0.05em',
      marginBottom: 4
    }
  }, "Ideal answer"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.2rem',
      fontWeight: 800,
      color: 'var(--dark)'
    }
  }, fb.correct_answer)), retype && /*#__PURE__*/React.createElement("div", {
    className: "anim-fade",
    style: {
      marginTop: 16,
      width: '100%',
      maxWidth: 800,
      padding: '24px',
      background: 'var(--white)',
      border: '2px solid var(--lgrey)',
      borderRadius: 20
    }
  }, (fb === null || fb === void 0 ? void 0 : fb.message) && /*#__PURE__*/React.createElement("div", {
    style: {
      background: 'var(--coral)',
      color: 'white',
      padding: '10px 18px',
      borderRadius: 10,
      fontWeight: 700,
      marginBottom: 20,
      display: 'inline-block',
      fontSize: '1rem'
    }
  }, renderText(fb.message)), /*#__PURE__*/React.createElement("div", {
    style: {
      marginBottom: 24,
      padding: '20px',
      background: '#f0fdf4',
      border: '2px solid #16a34a',
      borderRadius: 16,
      textAlign: 'left',
      userSelect: 'none',
      WebkitUserSelect: 'none'
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      fontSize: '0.9rem',
      color: '#16a34a',
      marginBottom: 8,
      textTransform: 'uppercase',
      letterSpacing: '0.05em'
    }
  }, "The correct answer is"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.8rem',
      fontWeight: 800,
      color: 'var(--dark)'
    }
  }, q.correct)), /*#__PURE__*/React.createElement("input", {
    ref: rtRef,
    className: "typed-input",
    style: {
      borderColor: rtFb ? 'var(--red-bright)' : ''
    },
    value: rtAns,
    onChange: function onChange(e) {
      setRtAns(e.target.value);
      setRtFb(null);
    },
    onPaste: function onPaste(e) {
      return e.preventDefault();
    },
    placeholder: "..."
  }), rtFb && /*#__PURE__*/React.createElement("div", {
    style: {
      color: 'var(--red-bright)',
      marginTop: 12,
      fontWeight: 700
    }
  }, rtFb), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-outline",
    disabled: busy,
    onClick: rtSubmit,
    style: {
      marginTop: 20
    }
  }, "Continue", /*#__PURE__*/React.createElement("span", {
    className: "keyhint"
  }, "Enter"))), !retype && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary anim-fade",
    disabled: busy,
    onClick: nx,
    style: {
      marginTop: 30
    }
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")))))));
}

// ── Parse and Translate (review set) ─────────────────────────────────────────
function ParseAndTranslate(_ref71) {
  var pupil = _ref71.pupil,
    set = _ref71.set,
    qs = _ref71.qs,
    isPreview = _ref71.isPreview,
    onDone = _ref71.onDone,
    addC = _ref71.addC,
    addW = _ref71.addW,
    pct = _ref71.pct;
  var TENSES = ['present', 'future', 'imperfect', 'perfect', 'pluperfect'];
  var PERSON_NUMBERS = [{
    id: '1-s',
    label: 'I',
    p: '1st',
    n: 'singular'
  }, {
    id: '2-s',
    label: 'you (sg)',
    p: '2nd',
    n: 'singular'
  }, {
    id: '3-s',
    label: 'he/she/it',
    p: '3rd',
    n: 'singular'
  }, {
    id: '1-p',
    label: 'we',
    p: '1st',
    n: 'plural'
  }, {
    id: '2-p',
    label: 'you (pl)',
    p: '2nd',
    n: 'plural'
  }, {
    id: '3-p',
    label: 'they',
    p: '3rd',
    n: 'plural'
  }];
  var _useState307 = useState(0),
    _useState308 = _slicedToArray(_useState307, 2),
    idx = _useState308[0],
    setIdx = _useState308[1];
  var _useState309 = useState(null),
    _useState310 = _slicedToArray(_useState309, 2),
    selTense = _useState310[0],
    setSelTense = _useState310[1];
  var _useState311 = useState(null),
    _useState312 = _slicedToArray(_useState311, 2),
    selPerson = _useState312[0],
    setSelPerson = _useState312[1];
  var _useState313 = useState(null),
    _useState314 = _slicedToArray(_useState313, 2),
    selNumber = _useState314[0],
    setSelNumber = _useState314[1];
  var _useState315 = useState(''),
    _useState316 = _slicedToArray(_useState315, 2),
    transAns = _useState316[0],
    setTransAns = _useState316[1];
  var _useState317 = useState(null),
    _useState318 = _slicedToArray(_useState317, 2),
    fb = _useState318[0],
    setFb = _useState318[1];
  var _useState319 = useState(false),
    _useState320 = _slicedToArray(_useState319, 2),
    busy = _useState320[0],
    setBusy = _useState320[1];
  var inRef = useRef();
  var selPN = selPerson && selNumber ? "".concat(selPerson[0], "-").concat(selNumber[0]) : null;
  var q = qs[idx];
  useEffect(function () {
    var _inRef$current5;
    if (!fb) (_inRef$current5 = inRef.current) === null || _inRef$current5 === void 0 || _inRef$current5.focus();
  }, [idx, fb]);
  var nx = function nx() {
    resetScroll();
    setSelTense(null);
    setSelPerson(null);
    setSelNumber(null);
    setTransAns('');
    setFb(null);
    if (idx + 1 >= qs.length) onDone();else setIdx(function (i) {
      return i + 1;
    });
  };
  var check = /*#__PURE__*/function () {
    var _ref72 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee31() {
      var correctKey, res;
      return _regenerator().w(function (_context31) {
        while (1) switch (_context31.n) {
          case 0:
            if (!(!selTense || !selPerson || !selNumber || !transAns.trim() || busy)) {
              _context31.n = 1;
              break;
            }
            return _context31.a(2);
          case 1:
            setBusy(true);
            correctKey = "".concat(q.tense, "|").concat(q.person, "|").concat(q.number, "|").concat(q.translation);
            _context31.n = 2;
            return post('/api/check', {
              pupil_id: pupil.id,
              set_id: set.id,
              question_type: 'parse_translate',
              question_text: q.form,
              pupil_answer: transAns,
              correct_answer: correctKey,
              tense: selTense,
              person: selPerson,
              number: selNumber
            });
          case 2:
            res = _context31.v;
            setFb(res);
            if (res.counts_as_correct) {
              addC();
            } else {
              addW({
                latin: q.form,
                correct: "".concat(q.tense, " ").concat(q.person, " ").concat(q.number, ": ").concat(q.translation)
              });
            }
            setBusy(false);
          case 3:
            return _context31.a(2);
        }
      }, _callee31);
    }));
    return function check() {
      return _ref72.apply(this, arguments);
    };
  }();
  useEffect(function () {
    var h = function h(e) {
      if (fb && e.key === 'Enter') nx();
      if (!fb && e.key === 'Enter' && selTense && selPerson && selNumber && transAns.trim()) check();
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  });
  if (!q) return null;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  })), /*#__PURE__*/React.createElement("div", {
    className: "activity-body"
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 8,
      fontWeight: 700,
      fontSize: '1.2rem'
    }
  }, "Parse this verb and translate it into English:"), /*#__PURE__*/React.createElement("h1", {
    className: "latin dynamic-latin",
    style: {
      fontSize: '4rem',
      marginBottom: 24
    }
  }, q.form), /*#__PURE__*/React.createElement("div", {
    style: {
      background: 'var(--white)',
      borderRadius: 20,
      padding: '32px 40px',
      maxWidth: 860,
      width: '100%',
      boxShadow: '0 8px 24px rgba(0,0,0,.06)',
      marginBottom: 24
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      marginBottom: 20
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      color: 'var(--grey)',
      fontSize: '0.85rem',
      textTransform: 'uppercase',
      letterSpacing: '0.08em',
      marginBottom: 8
    }
  }, "Person / Number"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: '1fr 1fr 1fr',
      gap: 10
    }
  }, PERSON_NUMBERS.map(function (pn) {
    var isSel = pn.p === selPerson && pn.n === selNumber;
    var pnIsCorrect = pn.p === q.person && pn.n === q.number;
    var isRight = fb && (fb.counts_as_correct ? isSel : isSel && pnIsCorrect);
    var isWrong = fb && isSel && !fb.counts_as_correct && !pnIsCorrect;
    return /*#__PURE__*/React.createElement("button", {
      key: pn.id,
      disabled: !!fb,
      onClick: function onClick() {
        if (isSel) {
          setSelPerson(null);
          setSelNumber(null);
        } else {
          setSelPerson(pn.p);
          setSelNumber(pn.n);
        }
      },
      style: {
        padding: '14px 10px',
        borderRadius: 12,
        border: "2px solid ".concat(fb && isSel ? isRight ? 'var(--green-bright)' : isWrong ? 'var(--red-bright)' : 'var(--navy)' : isSel ? 'var(--navy)' : 'var(--lgrey)'),
        background: fb && isSel ? isRight ? 'var(--green-bright)' : isWrong ? 'var(--red-bright)' : 'var(--navy)' : isSel ? 'var(--navy)' : 'var(--white)',
        color: isSel ? 'var(--white)' : 'var(--dark)',
        fontWeight: 700,
        fontSize: '1rem',
        cursor: fb ? 'default' : 'pointer',
        transition: 'all .15s'
      }
    }, pn.label);
  }))), /*#__PURE__*/React.createElement("div", {
    style: {
      marginBottom: 20
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      color: 'var(--grey)',
      fontSize: '0.85rem',
      textTransform: 'uppercase',
      letterSpacing: '0.08em',
      marginBottom: 8
    }
  }, "Tense"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 10,
      flexWrap: 'wrap',
      justifyContent: 'center'
    }
  }, TENSES.map(function (t) {
    var isSel = t === selTense;
    var isRight = fb && (fb.counts_as_correct ? isSel : isSel && t === q.tense);
    var isWrong = fb && isSel && !fb.counts_as_correct && t !== q.tense;
    return /*#__PURE__*/React.createElement("button", {
      key: t,
      disabled: !!fb,
      onClick: function onClick() {
        return setSelTense(t === selTense ? null : t);
      },
      style: {
        padding: '10px 20px',
        borderRadius: 12,
        border: "2px solid ".concat(fb && isSel ? isRight ? 'var(--green-bright)' : isWrong ? 'var(--red-bright)' : 'var(--navy)' : isSel ? 'var(--navy)' : 'var(--lgrey)'),
        background: fb && isSel ? isRight ? 'var(--green-bright)' : isWrong ? 'var(--red-bright)' : 'var(--navy)' : isSel ? 'var(--navy)' : 'var(--white)',
        color: isSel ? 'var(--white)' : 'var(--dark)',
        fontWeight: 700,
        fontSize: '1rem',
        cursor: fb ? 'default' : 'pointer',
        transition: 'all .15s'
      }
    }, t);
  }))), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("p", {
    style: {
      fontWeight: 800,
      color: 'var(--grey)',
      fontSize: '0.85rem',
      textTransform: 'uppercase',
      letterSpacing: '0.08em',
      marginBottom: 8
    }
  }, "Translation"), /*#__PURE__*/React.createElement("input", {
    ref: inRef,
    className: "typed-input ".concat(fb ? fb.counts_as_correct ? 'ok' : 'bad' : ''),
    value: transAns,
    onChange: function onChange(e) {
      return setTransAns(e.target.value);
    },
    disabled: !!fb,
    placeholder: "Type the English translation...",
    style: {
      fontSize: '1.5rem',
      padding: '20px 28px'
    }
  }))), fb && !fb.counts_as_correct && /*#__PURE__*/React.createElement("div", {
    className: "feedback anim-fade bad",
    style: {
      maxWidth: 860,
      marginBottom: 16
    }
  }, renderText(fb.message)), !fb && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    disabled: !selTense || !selPerson || !selNumber || !transAns.trim() || busy,
    onClick: check,
    style: {
      opacity: !selTense || !selPerson || !selNumber || !transAns.trim() ? 0.4 : 1
    }
  }, "Check", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")), fb && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary anim-fade",
    onClick: nx
  }, "Next", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")), /*#__PURE__*/React.createElement("p", {
    style: {
      marginTop: 16,
      color: 'var(--lgrey)',
      fontSize: '0.9rem',
      fontWeight: 700
    }
  }, "Question ", idx + 1, " of ", qs.length))));
}

// ── Results ───────────────────────────────────────────────────────────────────
function Confetti() {
  // Pure CSS confetti: 80 pieces in mixed colours falling from top
  var pieces = [];
  var colours = ['#fbbf24', '#16a34a', '#2563eb', '#dc2626', '#a855f7', '#ec4899', '#14b8a6'];
  for (var i = 0; i < 80; i++) {
    pieces.push({
      left: Math.random() * 100,
      delay: Math.random() * 1.2,
      colour: colours[i % colours.length],
      rot: Math.random() * 360,
      dur: 2.8 + Math.random() * 1.6
    });
  }
  return /*#__PURE__*/React.createElement(React.Fragment, null, pieces.map(function (p, i) {
    return /*#__PURE__*/React.createElement("span", {
      key: i,
      className: "confetti-piece",
      style: {
        left: p.left + '%',
        background: p.colour,
        animationDelay: p.delay + 's',
        animationDuration: p.dur + 's',
        transform: "rotate(".concat(p.rot, "deg)")
      }
    });
  }));
}
function Results(_ref73) {
  var res = _ref73.res,
    set = _ref73.set,
    total = _ref73.total,
    onFinish = _ref73.onFinish,
    onSaveAndNext = _ref73.onSaveAndNext,
    onPracticeWrongs = _ref73.onPracticeWrongs;
  var score = total > 0 ? Math.min(100, Math.round(res.correct / total * 100)) : 100;
  var passMark = set.pass_mark || 80;
  var passed = score >= passMark;
  var _useState321 = useState(null),
    _useState322 = _slicedToArray(_useState321, 2),
    nextN = _useState322[0],
    setNextN = _useState322[1];
  useEffect(function () {
    api('/api/sets').then(function (all) {
      var idx = all.findIndex(function (x) {
        return x.id === set.id;
      });
      setNextN(idx >= 0 && idx + 1 < all.length ? all[idx + 1] : null);
    });
  }, [set.id]);
  var showQuickReviewKey = res.wrong.length > 0 && set.type !== 'sentences' && set.type !== 'review';
  useEffect(function () {
    var h = function h(e) {
      if (e.key === 'Escape') onFinish(score);
      if (e.key === ' ') e.preventDefault();
      if (e.key === 'Enter' || e.key === ' ') {
        if (e.key === ' ' && showQuickReviewKey) onPracticeWrongs();else if (passed && nextN) onSaveAndNext(score, nextN);else if (showQuickReviewKey) onPracticeWrongs();else if (!passed) onSaveAndNext(score, set);else onFinish(score);
      }
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  }, [score, passed, nextN, showQuickReviewKey]);
  // Tiered message
  var tier, heading, subtitle;
  if (score >= 100) {
    tier = 'gold';
    heading = 'TRAILBLAZER!';
    subtitle = 'A perfect score. Every single answer correct.';
  } else if (score >= 95) {
    tier = 'gold';
    heading = 'PHENOMENAL!';
    subtitle = 'Near perfect — this material is locked in.';
  } else if (score >= 90) {
    tier = 'gold';
    heading = 'SUPERB!';
    subtitle = 'Excellent work. One more push and it\'s perfect.';
  } else if (score >= 85) {
    tier = 'gold';
    heading = 'GREAT!';
    subtitle = 'Well above the pass mark. Keep that momentum going.';
  } else if (score >= 80) {
    tier = 'gold';
    heading = 'PASSED!';
    subtitle = 'You\'ve met the mark. Carry that precision into the next set.';
  } else if (score >= 60) {
    tier = 'orange';
    heading = 'KEEP PRACTISING!';
    subtitle = 'Practise the items you missed, then redo the whole set.';
  } else {
    tier = 'red';
    heading = 'KEEP PRACTISING!';
    subtitle = 'Review your wrongs carefully, then redo the set from scratch.';
  }
  // Barrel roll easter egg — fires 30s after any pass (≥80%), once per session
  var barrelFiredRef = useRef(false);
  useEffect(function () {
    if (!passed || barrelFiredRef.current) return;
    var t = setTimeout(function () {
      if (barrelFiredRef.current) return;
      barrelFiredRef.current = true;
      var body = document.body;
      body.classList.remove('barrel-rolling');
      void body.offsetWidth;
      body.classList.add('barrel-rolling');
      body.addEventListener('animationend', function () {
        return body.classList.remove('barrel-rolling');
      }, {
        once: true
      });
    }, 30000);
    return function () {
      return clearTimeout(t);
    };
  }, [passed]);
  // Quick review only meaningful where wrongs are atomic items (vocab / verbs / parsing / tense_id / translate_form / building_parts).
  // For sentences and review sets, "redoing wrongs" = redoing the same sentences = same as retry, so we hide it.
  var showQuickReview = res.wrong.length > 0 && set.type !== 'sentences' && set.type !== 'review';
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen results anim-fade"
  }, passed && /*#__PURE__*/React.createElement(Confetti, null), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontSize: '3rem',
      color: 'var(--navy)',
      marginBottom: 10
    }
  }, /*#__PURE__*/React.createElement(PopText, {
    text: heading,
    active: passed
  })), /*#__PURE__*/React.createElement("div", {
    className: "big-score ".concat(passed ? 'pass' : 'fail').concat(passed ? ' score-pop' : '')
  }, score, "%"), /*#__PURE__*/React.createElement("p", {
    className: "results-tier tier-".concat(tier).concat(passed ? ' tier-fadein' : ''),
    dangerouslySetInnerHTML: {
      __html: subtitle
    }
  }), res.wrong.length > 0 && /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: 'left',
      background: 'var(--white)',
      borderRadius: 20,
      padding: '40px',
      margin: '10px 0 30px',
      maxWidth: 900,
      width: '100%',
      border: '4px solid var(--red-bright)'
    }
  }, /*#__PURE__*/React.createElement("h3", {
    style: {
      color: 'var(--red-bright)',
      marginBottom: 20,
      fontSize: '1.5rem'
    }
  }, "Review these (", res.wrong.length, "):"), res.wrong.map(function (w, i) {
    return /*#__PURE__*/React.createElement("div", {
      key: i,
      style: {
        padding: '16px 0',
        borderBottom: '2px solid var(--lgrey)',
        fontSize: '1.3rem'
      }
    }, /*#__PURE__*/React.createElement("strong", {
      className: w.latin ? 'latin' : ''
    }, w.latin || w.question), " ", /*#__PURE__*/React.createElement("span", {
      style: {
        color: 'var(--grey)'
      }
    }, "\u2192"), " ", /*#__PURE__*/React.createElement("span", {
      style: {
        color: '#1a73e8',
        fontWeight: 700
      }
    }, w.correct));
  })), /*#__PURE__*/React.createElement("div", {
    className: passed ? 'btns-drift' : '',
    style: {
      display: 'flex',
      gap: 20,
      marginTop: 20,
      flexWrap: 'wrap',
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    style: {
      fontSize: '1.3rem'
    },
    onClick: function onClick() {
      return onFinish(score);
    }
  }, "Menu", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Esc")), showQuickReview && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-quick",
    style: {
      fontSize: '1.3rem'
    },
    onClick: onPracticeWrongs
  }, "Quick review", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Space")), !passed && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-grey",
    style: {
      fontSize: '1.3rem'
    },
    onClick: function onClick() {
      return onSaveAndNext(score, set);
    }
  }, "Retry set"), passed && nextN && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-green",
    style: {
      fontSize: '1.3rem'
    },
    onClick: function onClick() {
      return onSaveAndNext(score, nextN);
    }
  }, "Next Set", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter"))));
}
// ── Quick Review done splash ──────────────────────────────────────────────────
function QuickReviewDone(_ref74) {
  var count = _ref74.count,
    passed = _ref74.passed,
    score = _ref74.score,
    set = _ref74.set,
    onRetry = _ref74.onRetry,
    onMenu = _ref74.onMenu,
    onSaveAndNext = _ref74.onSaveAndNext;
  var _useState323 = useState(null),
    _useState324 = _slicedToArray(_useState323, 2),
    nextN = _useState324[0],
    setNextN = _useState324[1];
  useEffect(function () {
    if (passed) api('/api/sets').then(function (all) {
      var idx = all.findIndex(function (x) {
        return x.id === set.id;
      });
      setNextN(idx >= 0 && idx + 1 < all.length ? all[idx + 1] : null);
    });
  }, [set.id, passed]);
  useEffect(function () {
    var h = function h(e) {
      if (e.key === 'Enter') onRetry();
      if (e.key === 'Escape') onMenu();
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  }, [onRetry, onMenu]);
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-body",
    style: {
      textAlign: 'center',
      padding: '80px 20px'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      width: 56,
      height: 56,
      background: 'var(--green-bright)',
      borderRadius: '50%',
      margin: '0 auto 20px',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("svg", {
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "#fff",
    strokeWidth: "3",
    strokeLinecap: "round",
    strokeLinejoin: "round",
    style: {
      width: 28,
      height: 28
    }
  }, /*#__PURE__*/React.createElement("polyline", {
    points: "20 6 9 17 4 12"
  }))), /*#__PURE__*/React.createElement("h2", {
    style: {
      color: 'var(--navy)',
      fontSize: '2.5rem',
      marginBottom: 12
    }
  }, "Quick review done."), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.15rem',
      color: 'var(--grey)',
      maxWidth: 600,
      margin: '0 auto 12px',
      lineHeight: 1.6
    }
  }, "You drilled ", /*#__PURE__*/React.createElement("strong", null, count), " ", count === 1 ? 'item' : 'items', "."), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1.1rem',
      color: passed ? '#16a34a' : 'var(--grey)',
      maxWidth: 600,
      margin: '0 auto 40px',
      lineHeight: 1.6,
      fontWeight: passed ? 700 : 400
    }
  }, passed ? "You'd already passed with ".concat(score, "% \u2014 take the next set or go again for a higher score.") : 'You haven\'t passed yet — redo the whole set to earn your pass.'), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 16,
      justifyContent: 'center',
      flexWrap: 'wrap'
    }
  }, /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    onClick: onMenu,
    style: {
      fontSize: '1.2rem'
    }
  }, "Menu", /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Esc")), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-grey",
    onClick: onRetry,
    style: {
      fontSize: '1.2rem'
    }
  }, "Redo the whole set", /*#__PURE__*/React.createElement("span", {
    className: "keyhint"
  }, "Enter")), passed && nextN && /*#__PURE__*/React.createElement("button", {
    className: "btn btn-green",
    onClick: function onClick() {
      return onSaveAndNext(score, nextN);
    },
    style: {
      fontSize: '1.2rem'
    }
  }, "Next set \u2192")))));
}
// ── Wrongs-only typed drill (server-marked for sentences, lenient for others) ─
function WrongsPractice(_ref75) {
  var wrongs = _ref75.wrongs,
    onDone = _ref75.onDone,
    set = _ref75.set,
    pupil = _ref75.pupil;
  var _useState325 = useState(0),
    _useState326 = _slicedToArray(_useState325, 2),
    idx = _useState326[0],
    setIdx = _useState326[1];
  var _useState327 = useState(''),
    _useState328 = _slicedToArray(_useState327, 2),
    val = _useState328[0],
    setVal = _useState328[1];
  var _useState329 = useState(null),
    _useState330 = _slicedToArray(_useState329, 2),
    checked = _useState330[0],
    setChecked = _useState330[1]; // null | {ok,message,correctAnswer}
  var _useState331 = useState(false),
    _useState332 = _slicedToArray(_useState331, 2),
    retyping = _useState332[0],
    setRetyping = _useState332[1];
  var inputRef = useRef(null);
  var w = wrongs[idx];
  var isSent = set && (set.type === 'sentences' || set.type === 'review');
  useEffect(function () {
    setVal('');
    setChecked(null);
    setRetyping(false);
    setTimeout(function () {
      var _inputRef$current;
      return (_inputRef$current = inputRef.current) === null || _inputRef$current === void 0 ? void 0 : _inputRef$current.focus();
    }, 50);
  }, [idx]);
  var advance = function advance() {
    setVal('');
    setChecked(null);
    setRetyping(false);
    if (idx + 1 < wrongs.length) setIdx(function (i) {
      return i + 1;
    });else onDone();
  };
  var handleCheck = /*#__PURE__*/function () {
    var _ref76 = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee32() {
      var norm, res, _norm;
      return _regenerator().w(function (_context32) {
        while (1) switch (_context32.n) {
          case 0:
            if (!retyping) {
              _context32.n = 1;
              break;
            }
            norm = function norm(s) {
              return s.trim().toLowerCase().replace(/[.!?,;]+$/, '');
            };
            if (norm(val) === norm(checked.correctAnswer)) advance();
            return _context32.a(2);
          case 1:
            if (!isSent) {
              _context32.n = 3;
              break;
            }
            _context32.n = 2;
            return api('/api/check', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                pupil_id: (pupil === null || pupil === void 0 ? void 0 : pupil.id) || 0,
                set_id: (set === null || set === void 0 ? void 0 : set.id) || 0,
                question_type: 'sentence',
                question_text: w.latin || w.question,
                pupil_answer: val,
                correct_answer: w.correct
              })
            });
          case 2:
            res = _context32.v;
            if (res.counts_as_correct) {
              advance();
            } else {
              setChecked({
                ok: false,
                message: res.message || "Correct: ".concat(w.correct),
                correctAnswer: w.correct
              });
              setRetyping(true);
              setVal('');
            }
            _context32.n = 4;
            break;
          case 3:
            _norm = function _norm(s) {
              return (s || '').trim().toLowerCase();
            };
            if (_norm(val) === _norm(w.correct)) {
              advance();
            } else {
              setChecked({
                ok: false,
                message: "The answer is: ".concat(w.correct),
                correctAnswer: w.correct
              });
              setRetyping(true);
              setVal('');
            }
          case 4:
            return _context32.a(2);
        }
      }, _callee32);
    }));
    return function handleCheck() {
      return _ref76.apply(this, arguments);
    };
  }();
  useEffect(function () {
    var h = function h(e) {
      if (e.key === 'Enter' && e.target.tagName === 'INPUT') handleCheck();
    };
    window.addEventListener('keydown', h);
    return function () {
      return window.removeEventListener('keydown', h);
    };
  }, [val, retyping, checked, idx]);
  if (!w) return null;
  var pct = idx / wrongs.length * 100;
  return /*#__PURE__*/React.createElement("div", {
    className: "fullscreen"
  }, /*#__PURE__*/React.createElement("div", {
    className: "topbar"
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "'Crimson Text',serif",
      fontSize: "1.2rem",
      letterSpacing: ".1em",
      textTransform: "uppercase",
      fontWeight: 600
    }
  }, "Principal Parts Platform")), /*#__PURE__*/React.createElement("div", {
    className: "activity anim-fade"
  }, /*#__PURE__*/React.createElement("div", {
    className: "activity-bar"
  }, /*#__PURE__*/React.createElement(ProgressBar, {
    pct: pct
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 700,
      color: 'var(--grey)'
    }
  }, "Quick review \xB7 ", idx + 1, " / ", wrongs.length)), /*#__PURE__*/React.createElement("div", {
    className: "activity-body",
    style: {
      justifyContent: 'center',
      padding: '40px 20px',
      paddingTop: 36
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '1rem',
      color: 'var(--grey)',
      fontWeight: 700,
      letterSpacing: '.1em',
      textTransform: 'uppercase',
      marginBottom: 14
    }
  }, "Quick review \u2014 retype these"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: '2rem',
      color: 'var(--navy)',
      fontWeight: 800,
      marginBottom: 24
    },
    className: w.latin ? 'latin' : ''
  }, w.latin || w.question), checked && !checked.ok && /*#__PURE__*/React.createElement("div", {
    style: {
      background: '#ffeaec',
      border: '3px solid var(--red-bright)',
      borderRadius: 12,
      padding: '14px 20px',
      marginBottom: 16,
      color: '#991b1b',
      fontWeight: 700,
      fontSize: '1.1rem'
    }
  }, checked.message), retyping && /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--grey)',
      marginBottom: 8,
      fontWeight: 600
    }
  }, "Now type the correct answer to continue:"), /*#__PURE__*/React.createElement("input", {
    ref: inputRef,
    autoFocus: true,
    value: val,
    onChange: function onChange(e) {
      return setVal(e.target.value);
    },
    className: "typed-input",
    style: {
      maxWidth: 780,
      marginBottom: 20,
      borderColor: checked && !checked.ok ? 'var(--red-bright)' : undefined
    },
    placeholder: retyping ? 'Type the correct answer…' : 'Type your translation…'
  }), /*#__PURE__*/React.createElement("button", {
    className: "btn btn-primary",
    onClick: handleCheck,
    style: {
      fontSize: '1.1rem'
    }
  }, retyping ? 'Confirm' : 'Check', /*#__PURE__*/React.createElement("span", {
    className: "keyhint",
    style: {
      color: 'white'
    }
  }, "Enter")), /*#__PURE__*/React.createElement("p", {
    style: {
      marginTop: 24,
      color: 'var(--grey)',
      fontSize: '0.95rem'
    }
  }, "After this, you can redo the whole set from the start."))));
}
var root = ReactDOM.createRoot(document.getElementById('root'));
root.render(/*#__PURE__*/React.createElement(App, null));