/* ============================================================
   MONTY HUNT · SITE SCRIPTS
   ============================================================ */

// --- NAV TOGGLE (mobile) ---
const navToggle = document.getElementById('nav-toggle');
const navLinks  = document.getElementById('nav-links');

navToggle.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});

// Close mobile nav on link click
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => navLinks.classList.remove('open'));
});

// --- ACTIVE NAV HIGHLIGHT ON SCROLL ---
const sections = document.querySelectorAll('section[id]');
const links    = document.querySelectorAll('#nav-links a');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      links.forEach(l => l.classList.remove('active'));
      const active = document.querySelector(`#nav-links a[href="#${entry.target.id}"]`);
      if (active) active.classList.add('active');
    }
  });
}, { rootMargin: '-40% 0px -55% 0px' });

sections.forEach(s => observer.observe(s));

// --- POEM TOGGLE ---
const poemToggle = document.getElementById('poem-toggle');
const poemText   = document.getElementById('poem-text');

if (poemToggle && poemText) {
  poemToggle.addEventListener('click', () => {
    const open = poemText.classList.toggle('open');
    poemToggle.textContent = open ? 'Close poem ↑' : 'Read the poem ↓';
  });
}

// --- POEM CONTENT ---
// De Bello Britannico — insert full text here when available.
// Placeholder lines shown until full text is provided.
const poemLines = [
  { n: 1,   t: 'Arma virumque cano Brittanniae litora et urbes,' },
  { n: 2,   t: 'Caesaris expeditas acies ad Tamesis undas,' },
  { n: 3,   t: 'dum procul Albanus fumat mons, dum mare frangit' },
  { n: 4,   t: 'spumas caeruleo et scopulis adsibilat aestus.' },
  { n: '',  t: '' },
  { n: '',  t: '[ Full text to be added — paste De Bello Britannico lines into script.js ]' },
];

const poemContent = document.getElementById('poem-content');
if (poemContent) {
  poemLines.forEach(l => {
    if (!l.n && !l.t) {
      poemContent.appendChild(document.createElement('br'));
      return;
    }
    const div = document.createElement('div');
    div.className = 'poem-line';
    div.innerHTML = `<span class="line-num">${l.n || ''}</span><span class="line-text">${l.t}</span>`;
    poemContent.appendChild(div);
  });
}

// --- SMOOTH REVEAL ON SCROLL ---
const revealEls = document.querySelectorAll('.wall-panel, .resource-item, .qa-item');

const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('revealed');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.08 });

revealEls.forEach(el => {
  el.classList.add('reveal-ready');
  revealObserver.observe(el);
});
