/* ============================================================
   THE HOUSE "” Monty Hunt, as a hand-inked Roman villa plan that
   plots itself onto a blueprint mat. Classical & hand-drawn on
   the paper; the tech lives on the mat and in the motion. Hover
   a room: vivid fresco pigment pools toward the cursor and bleeds
   softly past the walls, the drawings recolour, decoration wakes.
   No Latin. Vanilla SVG.
   ============================================================ */
(function () {
  const VB_W = 1600, VB_H = 1040;
  const INK = '#23221B', INK_SOFT = '#6C6D60', PAPER = '#F3EFE3', DIM = '#8C7F63';

  // vivid Pompeian pigments "” hot (wash/lines) + dark (legible labels)
  const PAL = {
    red:   { hot: '#D11F2B', dk: '#8E1620' },   // cinnabar
    blue:  { hot: '#1E7FD0', dk: '#11538C' },   // Egyptian blue
    ochre: { hot: '#E0A019', dk: '#8A5E0C' },   // yellow ochre
    green: { hot: '#3FA45A', dk: '#246B36' },   // green earth
  };

  // ---- geometry ----
  const XL = 250, XR = 1350, YT = 210, YB = 895, MY = 560;
  const ATL = 690, ATR = 910;          // atrium left/right (top centre column)
  const GDL = 620, GDR = 980;          // garden left/right (wider bottom column)
  const AXX = 800;
  const PORCH = { x: 740, w: 120, top: 150 };

  const ROOMS = [
    { id: 'cv',      label: 'CV',             ac: 'blue',  rect: [XL, YT, ATL - XL, MY - YT], apse: { cx: XL, cy: 385, r: 74, side: 'L' },
      lp: [XL + 30, YT + 64], cn: [470, 380], note: 'Cambridge Classics · PGCE\n· OCR GCSE examiner.' },
    { id: 'edtech',  label: 'EDTECH',         ac: 'blue',  rect: [XL, MY, GDL - XL, YB - MY],
      lp: [XL + 30, MY + 64], cn: [435, 730], note: 'the platform "” a Latin platform,\nlive in two London schools.' },
    { id: 'about',   label: 'ABOUT',          ac: 'red',   rect: [ATL, YT, ATR - ATL, MY - YT],
      lp: [ATL + 26, YT + 60], cn: [AXX, 385], note: 'Latin reaches 3% of state schools.\nThe problem is the pedagogy.' },
    { id: 'garden',  label: 'DIGITAL GARDEN', ac: 'green', rect: [GDL, MY, GDR - GDL, YB - MY], apse: { cx: AXX, cy: YB, r: 80, side: 'D' }, court: true,
      lp: [GDL + 30, MY + 60], cn: [AXX, 720], note: 'Notes & half-formed ideas,\ntended irregularly.' },
    { id: 'gallery', label: 'GALLERY',        ac: 'ochre', rect: [ATR, YT, XR - ATR, MY - YT], apse: { cx: XR, cy: 385, r: 74, side: 'R' },
      lp: [ATR + 30, YT + 64], cn: [1130, 380], note: 'Photography · RA Young Artists\n· the Interamna coin hoard.' },
    { id: 'output',  label: 'OUTPUT',         ac: 'ochre', rect: [GDR, MY, XR - GDR, YB - MY],
      lp: [GDR + 30, MY + 64], cn: [1165, 730], note: 'VR Troy · Montagu Butler Prize\n"” what I am building now.' },
  ];
  const byId = Object.fromEntries(ROOMS.map((r) => [r.id, r]));

  // ---- seeded RNG ----
  let _s = 0x51ed3c9b;
  const rnd = () => { _s = (Math.imul(_s, 1664525) + 1013904223) >>> 0; return _s / 4294967296; };
  const jit = (a) => (rnd() * 2 - 1) * a;

  // ---- hand stroke ----
  function stroke(x1, y1, x2, y2, w, o = {}) {
    const { over = 4, wav = 1.3, color = INK, dash = null, op = 1, draw = false } = o;
    const dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy) || 1;
    const ux = dx / len, uy = dy / len, nx = -uy, ny = ux;
    const sx = x1 - ux * over, sy = y1 - uy * over, ex = x2 + ux * over, ey = y2 + uy * over;
    const n = Math.max(2, Math.round(len / 64));
    let d = `M ${(sx + jit(0.6)).toFixed(1)} ${(sy + jit(0.6)).toFixed(1)}`;
    for (let i = 1; i <= n; i++) {
      const t = i / n;
      d += ` L ${(sx + (ex - sx) * t + nx * jit(wav)).toFixed(1)} ${(sy + (ey - sy) * t + ny * jit(wav)).toFixed(1)}`;
    }
    const cls = (draw && !dash) ? ' class="ds" pathLength="1"' : '';
    return `<path${cls} d="${d}" fill="none" stroke="${color}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"${dash ? ` stroke-dasharray="${dash}"` : ''} opacity="${op}"/>`;
  }
  function arc(cx, cy, r, a0, a1, w, o = {}) {
    const { color = INK, op = 1, draw = false, sweep = 1 } = o;
    const p = (a) => [cx + r * Math.cos(a), cy + r * Math.sin(a)];
    const [x0, y0] = p(a0), [x1, y1] = p(a1);
    const large = Math.abs(a1 - a0) > Math.PI ? 1 : 0;
    const cls = draw ? ' class="ds" pathLength="1"' : '';
    return `<path${cls} d="M ${x0.toFixed(1)} ${y0.toFixed(1)} A ${r} ${r} 0 ${large} ${sweep} ${x1.toFixed(1)} ${y1.toFixed(1)}" fill="none" stroke="${color}" stroke-width="${w}" stroke-linecap="round" opacity="${op}"/>`;
  }
  function wseg(x1, y1, x2, y2, th, w, capA, capB, o = {}) {
    const dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy) || 1;
    const nx = -dy / len * th / 2, ny = dx / len * th / 2;
    let s = stroke(x1 + nx, y1 + ny, x2 + nx, y2 + ny, w, { over: 3, wav: 0.8, ...o })
          + stroke(x1 - nx, y1 - ny, x2 - nx, y2 - ny, w, { over: 3, wav: 0.8, ...o });
    if (capA) s += stroke(x1 + nx, y1 + ny, x1 - nx, y1 - ny, w, { over: 0.4, wav: 0.3, ...o });
    if (capB) s += stroke(x2 + nx, y2 + ny, x2 - nx, y2 - ny, w, { over: 0.4, wav: 0.3, ...o });
    return s;
  }
  function wall(vert, fixed, from, to, th, w, gaps, o) {
    let cuts = [from]; (gaps || []).forEach((g) => cuts.push(g[0], g[1])); cuts.push(to);
    let s = '';
    for (let i = 0; i < cuts.length; i += 2) {
      const a = cuts[i], b = cuts[i + 1], capA = i !== 0, capB = i + 2 < cuts.length;
      s += vert ? wseg(fixed, a, fixed, b, th, w, capA, capB, o) : wseg(a, fixed, b, fixed, th, w, capA, capB, o);
    }
    return s;
  }
  function hrect(x, y, w, h, sw, o = {}) {
    return stroke(x, y, x + w, y, sw, o) + stroke(x + w, y, x + w, y + h, sw, o)
         + stroke(x + w, y + h, x, y + h, sw, o) + stroke(x, y + h, x, y, sw, o);
  }
  const circ = (x, y, r, c, w, op = 1) => `<circle cx="${x}" cy="${y}" r="${r}" fill="none" stroke="${c}" stroke-width="${w}" opacity="${op}"/>`;
  const disc = (x, y, r, c, op = 1) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${c}" opacity="${op}"/>`;

  // ---- structure ----
  const apseGeom = (a) => {
    if (a.side === 'L') return [Math.PI * 0.5, Math.PI * 1.5, 1];
    if (a.side === 'R') return [Math.PI * 1.5, Math.PI * 0.5, 1];
    return [0, Math.PI, 0]; // D (down)
  };
  function shell() {
    const EX = 24, ew = 4.6, dr = { draw: true };
    let s = `<g>`;
    s += wall(false, YT, XL, XR, EX, ew, [[PORCH.x, PORCH.x + PORCH.w]], dr);
    s += wall(false, YB, XL, XR, EX, ew, [[AXX - 80, AXX + 80]], dr);
    s += wall(true, XL, YT, YB, EX, ew, [[311, 459]], dr);
    s += wall(true, XR, YT, YB, EX, ew, [[311, 459]], dr);
    // porch
    s += wseg(PORCH.x, PORCH.top, PORCH.x, YT, 16, 3.6, false, false, dr);
    s += wseg(PORCH.x + PORCH.w, PORCH.top, PORCH.x + PORCH.w, YT, 16, 3.6, false, false, dr);
    s += wseg(PORCH.x, PORCH.top, PORCH.x + PORCH.w, PORCH.top, 16, 3.6, true, true, dr);
    // apses (double arc)
    ROOMS.forEach((r) => {
      if (!r.apse) return;
      const [a0, a1, sw] = apseGeom(r.apse);
      s += arc(r.apse.cx, r.apse.cy, r.apse.r, a0, a1, ew, { draw: true, sweep: sw });
      s += arc(r.apse.cx, r.apse.cy, r.apse.r - 12, a0, a1, 2.6, { draw: true, sweep: sw, op: 0.85 });
    });
    s += `</g>`;
    return s;
  }
  function partitions() {
    const IN = 15, iw = 3.4, dr = { draw: true };
    let s = `<g>`;
    s += wall(true, ATL, YT, MY, IN, iw, [[330, 410]], dr);
    s += wall(true, ATR, YT, MY, IN, iw, [[330, 410]], dr);
    s += wall(true, GDL, MY, YB, IN, iw, [[690, 760]], dr);
    s += wall(true, GDR, MY, YB, IN, iw, [[690, 760]], dr);
    s += wall(false, MY, XL, XR, IN, iw, [[360, 430], [740, 860], [1150, 1220]], dr);
    // thin sub-chambers (density) "” drawn lighter
    const th = { draw: true, op: 0.7 };
    s += wseg(500, YT, 500, 322, 9, 2.4, false, true, th) + wseg(XL, 322, 500, 322, 9, 2.4, false, true, th);   // CV cubiculum
    s += wseg(1100, YT, 1100, 322, 9, 2.4, false, true, th) + wseg(1100, 322, XR, 322, 9, 2.4, true, false, th); // GALLERY cubiculum
    s += wseg(450, 778, 450, YB, 9, 2.4, true, false, th);                                                       // EDTECH annex
    s += wseg(1150, 778, 1150, YB, 9, 2.4, true, false, th);                                                      // OUTPUT annex
    s += `</g>`;
    return s;
  }
  function entranceSteps() {
    let s = `<g>`;
    for (let i = 0; i < 4; i++) {
      const yy = PORCH.top + 18 + i * 24;
      s += stroke(PORCH.x + 12 + i * 5, yy, PORCH.x + PORCH.w - 12 - i * 5, yy, 2.4, { over: 1, wav: 0.4, op: 0.85, draw: true });
    }
    s += stroke(PORCH.x + 8, YT + 2, PORCH.x + PORCH.w - 8, YT + 2, 2.4, { over: 1, dash: '2 10', op: 0.6 });
    s += `</g>`;
    return s;
  }
  function doors() {
    const a = (cx, cy, r, ex, ey, sw) => `<path d="M ${cx} ${cy} A ${r} ${r} 0 0 ${sw} ${ex} ${ey}" fill="none" stroke="${INK}" stroke-width="2" opacity="0.32"/>`;
    let s = `<g>`;
    s += a(ATL, 330, 80, ATL, 410, 1) + a(ATR, 330, 80, ATR, 410, 0);
    s += a(GDL, 690, 70, GDL, 760, 1) + a(GDR, 690, 70, GDR, 760, 0);
    s += `</g>`;
    return s;
  }

  // ---- furniture (param: colour/weight/opacity) ----
  function furniture(r, o) {
    const c = o.color, w = o.w, op = o.op;
    const L = (x1, y1, x2, y2, e = {}) => stroke(x1, y1, x2, y2, w, { color: c, op, ...e });
    const R = (x, y, ww, hh, e = {}) => hrect(x, y, ww, hh, w, { color: c, op, ...e });
    const [rx, ry, rw, rh] = r.rect; const cx = rx + rw / 2, cy = ry + rh / 2;
    let s = '';
    if (r.id === 'about') {
      s += R(cx - 80, cy - 30, 160, 150);                          // impluvium
      s += R(cx - 58, cy - 10, 116, 110, { op: op * 0.7 });
      [[cx - 80, cy - 30], [cx + 80, cy - 30], [cx - 80, cy + 120], [cx + 80, cy + 120]].forEach(([x, y]) => s += disc(x, y, 9, c, op));
      s += L(cx - 52, ry + 250, cx + 52, ry + 250, { dash: '3 9', op: op * 0.5 }) + L(cx, ry + 236, cx, ry + 264, { dash: '3 9', op: op * 0.5 });
      s += R(cx - 30, cy + 156, 60, 26);                           // cartibulum
    } else if (r.id === 'cv') {
      s += R(rx + 150, ry + 150, 150, 52);                         // desk
      s += circ(rx + 225, ry + 232, 16, c, w, op);                // chair
      s += R(rx + rw - 62, ry + 100, 26, 170);                    // bookcase (right wall)
      for (let i = 1; i < 6; i++) s += L(rx + rw - 62, ry + 100 + i * 28, rx + rw - 36, ry + 100 + i * 28, { over: 0, wav: 0.3, op: op * 0.7 });
      // apse exedra bench
      s += arc(r.apse.cx + 20, r.apse.cy, r.apse.r - 26, Math.PI * 0.62, Math.PI * 1.38, w, { color: c, op: op * 0.8, sweep: 1 });
    } else if (r.id === 'gallery') {
      [[rx + 90, ry + 150], [rx + 180, ry + 132], [rx + 270, ry + 160]].forEach(([x, y]) => s += R(x, y, 40, 40)); // plinths
      s += R(rx + 110, ry + 260, 150, 24);                        // viewing bench
      [[rx + rw - 60, ry + 120], [rx + rw - 60, ry + 190]].forEach(([x, y]) => s += R(x, y, 34, 46, { op: op * 0.85 })); // framed works (right wall)
      // apse statue niche
      s += arc(r.apse.cx - 20, r.apse.cy, r.apse.r - 26, Math.PI * 0.62, Math.PI * 1.38, w, { color: c, op: op * 0.8, sweep: 0 });
      s += disc(r.apse.cx - 36, r.apse.cy, 8, c, op);
    } else if (r.id === 'edtech') {
      s += R(rx + 40, ry + rh - 90, rw - 130, 40);                 // bench
      s += R(rx + rw - 96, ry + 70, 60, 150);                      // server rack
      for (let i = 1; i < 6; i++) s += L(rx + rw - 96, ry + 70 + i * 25, rx + rw - 36, ry + 70 + i * 25, { over: 0, wav: 0.3, op: op * 0.7 });
      [0, 1, 2].forEach((i) => s += R(rx + 50 + i * 56, ry + 90, 40, 28, { op: op * 0.85 }));  // monitors
    } else if (r.id === 'output') {
      s += R(rx + 40, ry + 110, 170, 60);                          // worktable
      [0, 1, 2].forEach((i) => s += R(rx + 54 + i * 52, ry + 122, 36, 36, { op: op * 0.85 }));
      s += circ(rx + 235, ry + 96, 15, c, w, op);                  // stool
      s += R(rx + 60, ry + rh - 96, 120, 56, { op: op * 0.85 });   // kiln
    } else if (r.id === 'garden') {
      const m = 60, x0 = rx + m, x1 = rx + rw - m, y0 = ry + m + 30, y1 = ry + rh - m - 26;
      const N = 6;
      for (let i = 0; i <= N; i++) { const t = i / N; s += disc(x0 + t * (x1 - x0), y0, 8, c, op); }       // top colonnade
      for (let j = 1; j <= 2; j++) { const yy = y0 + j / 3 * (y1 - y0); s += disc(x0, yy, 8, c, op) + disc(x1, yy, 8, c, op); }  // side columns (court opens to the exedra)
      s += R(x0 + 26, y0 + 22, (x1 - x0) - 52, (y1 - y0) - 40, { op: op * 0.5 });
      const gcx = rx + rw / 2, gcy = y0 + (y1 - y0) * 0.44;
      s += L(x0 + 26, gcy, x1 - 26, gcy, { dash: '4 11', op: op * 0.4 }) + L(gcx, y0 + 22, gcx, y1 - 16, { dash: '4 11', op: op * 0.4 });
      s += circ(gcx, gcy, 30, c, w, op) + circ(gcx, gcy, 13, c, w, op * 0.7);
    }
    return s;
  }

  // ---- fresco decoration (reveal only) "” kept restrained for legibility ----
  function fresco(r, c) {
    const [rx, ry, rw, rh] = r.rect; const cx = rx + rw / 2;
    const pad = 30, w = 2.6, o = { color: c, op: 0.85, wav: 0.6 };
    let s = hrect(rx + pad, ry + pad, rw - 2 * pad, rh - 2 * pad, w, o);
    if (!r.court) {
      // a single Greek-key (meander) frieze just inside the top edge "” away from the note
      const by = ry + pad + 26, bx0 = rx + pad + 14, bx1 = rx + rw - pad - 14, step = 26;
      let mk = `M ${bx0} ${by}`, up = true;
      for (let x = bx0; x < bx1 - step; x += step) { mk += ` h ${step * 0.5} v ${up ? -12 : 12} h ${step * 0.5} v ${up ? 12 : -12}`; up = !up; }
      s += `<path d="${mk}" fill="none" stroke="${c}" stroke-width="1.9" opacity="0.5"/>`;
    } else {
      // garden in bloom "” a few flowers wake among the beds
      const m = 60, x0 = rx + m, y0 = ry + m + 24, x1 = rx + rw - m, y1 = ry + rh - m + 10;
      [[rx + 130, y0 + 56], [rx + rw - 150, y0 + 56], [rx + 130, y1 - 46], [rx + rw - 150, y1 - 46]].forEach(([fx, fy]) => {
        for (let k = 0; k < 6; k++) { const a = k / 6 * Math.PI * 2; s += disc(fx + Math.cos(a) * 11, fy + Math.sin(a) * 11, 4, c, 0.7); }
        s += disc(fx, fy, 5, c, 0.85);
      });
    }
    return s;
  }

  // ---- room clip / hit / wash shapes ----
  function roomShapes(r) {
    const [rx, ry, rw, rh] = r.rect;
    let shapes = `<rect x="${rx}" y="${ry}" width="${rw}" height="${rh}"/>`;
    if (r.apse) shapes += `<circle cx="${r.apse.cx}" cy="${r.apse.cy}" r="${r.apse.r}"/>`;
    return shapes;
  }

  // ---- labels (bold, centred both axes, no underline) ----
  function labels() {
    return ROOMS.map((r) => {
      const p = PAL[r.ac];
      const lcx = r.rect[0] + r.rect[2] / 2;
      const lcy = r.rect[1] + r.rect[3] / 2;
      return `<g class="lab" data-id="${r.id}">
        <text x="${lcx}" y="${lcy}" text-anchor="middle" dominant-baseline="central" class="lname" style="fill:${p.dk}">${r.label}</text>
      </g>`;
    }).join('');
  }

  // ---- trees & bushes (varied; easter egg: rustle + falling leaves) ----
  const FLORA = [
    { x: 168, y: 360, type: 'tree' }, { x: 196, y: 726, type: 'bush' },
    { x: 1434, y: 348, type: 'tree' }, { x: 1410, y: 720, type: 'bush' },
    { x: 548, y: 968, type: 'bush' }, { x: 1058, y: 962, type: 'tree' },
  ];
  function flora() {
    return FLORA.map((t, i) => {
      const G = ['#4E6B3C', '#5C6E45', '#6A7A4A', '#566A3E'][i % 4];
      const lean = jit(0.12);
      let s = '';
      if (t.type === 'tree') {
        const th = 30 + Math.round(rnd() * 16);            // trunk height
        const cr = 24 + Math.round(rnd() * 12);            // canopy radius
        s += stroke(t.x, t.y + th, t.x + lean * 30, t.y, 3.2, { color: G, op: 0.72, over: 0, wav: 0.7 });
        // 2"“3 overlapping canopy lobes, varied
        const lobes = 2 + Math.round(rnd());
        s += circ(t.x, t.y - cr * 0.4, cr, G, 2.4, 0.72);
        for (let k = 0; k < lobes; k++) { const a = Math.PI + k * (Math.PI / (lobes + 1)); s += circ(t.x + Math.cos(a) * cr * 0.7, t.y - cr * 0.1 + Math.sin(a) * 6, cr * 0.62, G, 2.2, 0.6); }
        const nb = 8 + Math.round(rnd() * 6);
        for (let k = 0; k < nb; k++) s += disc(t.x + jit(cr * 0.85), t.y - cr * 0.3 + jit(cr * 0.7), 1.8 + rnd() * 1.2, G, 0.4);
      } else {
        const br = 16 + Math.round(rnd() * 10);            // bush radius
        s += circ(t.x, t.y + 8, br, G, 2.4, 0.7);
        const lobes = 2 + Math.round(rnd() * 2);
        for (let k = 0; k < lobes; k++) { const a = Math.PI + k * (Math.PI / (lobes + 0.5)); s += circ(t.x + Math.cos(a) * br * 0.8, t.y + 14 + Math.sin(a) * 4, br * 0.6, G, 2.2, 0.6); }
        const nb = 6 + Math.round(rnd() * 5);
        for (let k = 0; k < nb; k++) s += disc(t.x + jit(br * 0.85), t.y + 8 + jit(br * 0.6), 1.7 + rnd(), G, 0.4);
      }
      return `<g class="flora" data-i="${i}" data-cx="${t.x}" data-cy="${t.y - 4}" style="cursor:pointer"><g class="crown">${s}</g></g>`;
    }).join('');
  }

  // ---- CAD dimension line (arrows only, no numbers) ----
  function dims() {
    const dl = `stroke="${DIM}" stroke-width="1.3" opacity="0.55"`;
    const ext = `stroke="${DIM}" stroke-width="1" opacity="0.38"`;
    const y = YB + 56;
    let s = `<g>`;
    s += `<line x1="${XL}" y1="${YB + 18}" x2="${XL}" y2="${y + 8}" ${ext}/><line x1="${XR}" y1="${YB + 18}" x2="${XR}" y2="${y + 8}" ${ext}/>`;
    s += `<line x1="${XL}" y1="${y}" x2="${XR}" y2="${y}" ${dl}/>`;
    s += `<path d="M ${XL + 15} ${y - 6} L ${XL} ${y} L ${XL + 15} ${y + 6}" fill="none" ${dl}/>`;
    s += `<path d="M ${XR - 15} ${y - 6} L ${XR} ${y} L ${XR - 15} ${y + 6}" fill="none" ${dl}/>`;
    s += `</g>`;
    return s;
  }

  // ---- footsteps ----
  function sample(pts, d) {
    const out = []; let acc = 0;
    for (let i = 0; i < pts.length - 1; i++) {
      const [x1, y1] = pts[i], [x2, y2] = pts[i + 1];
      const dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy), a = Math.atan2(dy, dx);
      let t = acc; while (t < len) { const f = t / len; out.push({ x: x1 + dx * f, y: y1 + dy * f, a }); t += d; } acc = t - len;
    }
    return out;
  }
  function footSVG(s, i) {
    const side = i % 2 === 0 ? 1 : -1, px = -Math.sin(s.a), py = Math.cos(s.a);
    const ox = (s.x + px * side * 8).toFixed(1), oy = (s.y + py * side * 8).toFixed(1);
    const deg = (s.a * 180 / Math.PI + 90).toFixed(1);
    return `<g class="foot" transform="translate(${ox} ${oy}) rotate(${deg})">
      <path d="M0,-10 C5,-10 7,-3 5,3 C4,8 2,10 0,10 C-2,10 -4,8 -5,3 C-7,-3 -5,-10 0,-10 Z"/>
      <ellipse cx="0" cy="12" rx="3.3" ry="4.2"/></g>`;
  }
  const ENTRY = [AXX, PORCH.top + 26];
  const ROUTES = [
    [ENTRY, [AXX, 400], [AXX, MY], [AXX, 720]],
    [ENTRY, [AXX, 370], [ATL, 370], [470, 370]],
    [ENTRY, [AXX, 370], [ATR, 370], [1130, 370]],
    [ENTRY, [AXX, MY], [AXX, 640], [GDL, 725], [440, 725]],
    [ENTRY, [AXX, MY], [AXX, 640], [GDR, 725], [1160, 725]],
  ];

  // ---- assemble svg ----
  const clips = ROOMS.map((r) => `<clipPath id="clip-${r.id}">${roomShapes(r)}</clipPath>`).join('');
  const fresGroups = ROOMS.map((r) => {
    const p = PAL[r.ac];
    return `<g class="fres" data-id="${r.id}" style="opacity:0">
      <g>${furniture(r, { color: p.dk, w: 3, op: 0.95 })}</g>
      <g>${fresco(r, p.dk)}</g></g>`;
  }).join('');

  const svg = `
  <svg id="plan-svg" viewBox="0 0 ${VB_W} ${VB_H}" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <filter id="paperink" x="-2%" y="-2%" width="104%" height="104%">
        <feTurbulence type="fractalNoise" baseFrequency="0.011 0.013" numOctaves="2" seed="7" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="2.2"/>
      </filter>
      <filter id="plaster"><feTurbulence type="fractalNoise" baseFrequency="0.02 0.028" numOctaves="4" seed="11"/><feColorMatrix type="saturate" values="0"/></filter>
      <radialGradient id="glowGrad" gradientUnits="userSpaceOnUse" cx="800" cy="500" r="260">
        <stop id="bg0" offset="0%" stop-color="#D11F2B" stop-opacity="0.55"/>
        <stop id="bg1" offset="46%" stop-color="#D11F2B" stop-opacity="0.30"/>
        <stop id="bg2" offset="100%" stop-color="#D11F2B" stop-opacity="0"/>
      </radialGradient>
      <radialGradient id="focusGrad" gradientUnits="userSpaceOnUse" cx="800" cy="500" r="430">
        <stop id="fg0" offset="0%" stop-color="#000"/>
        <stop id="fg1" offset="54%" stop-color="#000"/>
        <stop id="fg2" offset="100%" stop-color="#fff"/>
      </radialGradient>
      <mask id="focusMask"><rect x="0" y="0" width="${VB_W}" height="${VB_H}" fill="url(#focusGrad)"/></mask>
      ${clips}
    </defs>

    <g filter="url(#paperink)">
      <g class="phase" id="ph-details" style="opacity:0">${ROOMS.map((r) => furniture(r, { color: INK, w: 2, op: 0.3 })).join('')}</g>
      <g id="washLayer">
        <circle id="glow" cx="800" cy="500" r="0" fill="url(#glowGrad)" opacity="0"/>
      </g>
      <g class="phase" id="ph-shell" style="opacity:0">${shell()}${entranceSteps()}</g>
      <g class="phase" id="ph-rooms" style="opacity:0">${partitions()}${doors()}</g>
      <g id="fresLayer">${fresGroups}</g>
      <g class="phase" id="ph-extra" style="opacity:0">${flora()}${dims()}</g>
      <rect id="dimOverlay" x="0" y="0" width="${VB_W}" height="${VB_H}" fill="${PAPER}" mask="url(#focusMask)" opacity="0" style="transition:opacity .4s ease;pointer-events:none"/>
      <g id="steps" fill="${INK}"></g>
      <g class="phase" id="ph-names" style="opacity:0">
        <text x="${AXX}" y="70" text-anchor="middle" class="title">MONTY HUNT</text>
        ${labels()}
      </g>
    </g>

    <text id="enterMsg" x="${AXX}" y="${PORCH.top - 36}" text-anchor="middle" class="enter">Enter</text>

    <g id="hits">
      ${ROOMS.map((r) => `<g class="hit" data-id="${r.id}"><rect x="${r.rect[0]}" y="${r.rect[1]}" width="${r.rect[2]}" height="${r.rect[3]}" fill="transparent"/>${r.apse ? `<circle cx="${r.apse.cx}" cy="${r.apse.cy}" r="${r.apse.r}" fill="transparent"/>` : ''}</g>`).join('')}
    </g>
  </svg>`;

  const css = `
    #plan-svg{font-family:'Oswald',sans-serif;}
    .title{font-family:'Cinzel',serif;font-weight:800;font-size:46px;letter-spacing:.22em;fill:${INK};paint-order:stroke;stroke:${PAPER};stroke-width:9px;stroke-linejoin:round;}
    .subtitle{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.34em;fill:${INK_SOFT};paint-order:stroke;stroke:${PAPER};stroke-width:5px;stroke-linejoin:round;}
    .lname{font-family:'Oswald',sans-serif;font-weight:700;font-size:35px;letter-spacing:.07em;text-transform:uppercase;paint-order:stroke;stroke:${PAPER};stroke-width:8px;stroke-linejoin:round;transform-box:fill-box;transform-origin:center;transition:transform .25s cubic-bezier(.2,.7,.2,1);}
    .lab.on .lname{transform:scale(1.1);}
    .note{font-family:'EB Garamond',serif;font-style:italic;font-weight:600;font-size:25px;fill:${INK};paint-order:stroke;stroke:${PAPER};stroke-width:6px;stroke-linejoin:round;}
    .enter{font-family:'EB Garamond',serif;font-style:italic;font-size:25px;fill:${INK_SOFT};opacity:0;transition:opacity .6s ease;paint-order:stroke;stroke:${PAPER};stroke-width:5px;stroke-linejoin:round;}
    .phase{transition:opacity .5s ease;}
    .ds{stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset .85s ease;}
    .go .ds{stroke-dashoffset:0;}
    .wash,.fres{pointer-events:none;transition:opacity .4s ease;}
    #bloom{transition:opacity .4s ease;}
    .hit{cursor:pointer;}
    .foot{opacity:0;transition:opacity .55s ease;}
    .crown{transform-box:fill-box;transform-origin:center bottom;}
    .flora.rustle .crown{animation:rustle 1.1s ease;}
    @keyframes rustle{0%,100%{transform:rotate(0)}22%{transform:rotate(3.5deg)}48%{transform:rotate(-2.5deg)}72%{transform:rotate(1.5deg)}}
    .leaf{animation:fall var(--d,2.4s) ease-in forwards;}
    @keyframes fall{0%{opacity:.85;transform:translate(0,0) rotate(0)}100%{opacity:0;transform:translate(var(--dx,12px),64px) rotate(200deg)}}
    @media (prefers-reduced-motion: reduce){.ds{transition:none;stroke-dashoffset:0;}.foot,.enter{transition:none;}.flora.rustle .crown,.leaf{animation:none;}}
  `;

  const mount = document.getElementById('plan');
  const styleEl = document.createElement('style'); styleEl.textContent = css; document.head.appendChild(styleEl);
  mount.innerHTML = svg;

  const svgEl = mount.querySelector('svg');
  const NS = 'http://www.w3.org/2000/svg';
  const fresEls = Object.fromEntries([...svgEl.querySelectorAll('.fres')].map((e) => [e.dataset.id, e]));
  const labEls = Object.fromEntries([...svgEl.querySelectorAll('.lab')].map((e) => [e.dataset.id, e]));
  const glow = svgEl.querySelector('#glow');
  const gStops = ['bg0', 'bg1', 'bg2'].map((id) => svgEl.querySelector('#' + id));
  const focusGrad = svgEl.querySelector('#focusGrad');
  const dimOverlay = svgEl.querySelector('#dimOverlay');
  const cmdEl = document.getElementById('cmd');
  const clampPt = (r, x, y) => [Math.max(r.rect[0] + 24, Math.min(r.rect[0] + r.rect[2] - 24, x)), Math.max(r.rect[1] + 24, Math.min(r.rect[1] + r.rect[3] - 24, y))];
  let locked = null, ready = false;

  function open(id, x, y) {
    const sg = svgEl.querySelector('#steps'); if (sg) { sg.style.transition = 'opacity .3s ease'; sg.style.opacity = id ? '0' : '1'; }
    Object.values(fresEls).forEach((e) => e.style.opacity = '0');
    Object.values(labEls).forEach((e) => e.classList.remove('on'));
    if (id) {
      const r = byId[id], p = PAL[r.ac];
      const [rx, ry, rw, rh] = r.rect, ccx = rx + rw / 2, ccy = ry + rh / 2;
      fresEls[id].style.opacity = '1';
      if (labEls[id]) labEls[id].classList.add('on');
      gStops.forEach((s) => s.setAttribute('stop-color', p.hot));
      const [bx, by] = (x != null) ? clampPt(r, x, y) : r.cn;
      glow.setAttribute('cx', bx); glow.setAttribute('cy', by);
      glow.setAttribute('r', Math.min(rw, rh) * 0.78 + 50);
      glow.setAttribute('opacity', '1');
      // lantern: fade the rest of the plan back to paper, leave this room bright
      focusGrad.setAttribute('cx', ccx); focusGrad.setAttribute('cy', ccy);
      focusGrad.setAttribute('r', Math.hypot(rw, rh) / 2 + 120);
      dimOverlay.setAttribute('opacity', '0.62');
      if (cmdEl) cmdEl.textContent = 'cd ./' + id;
    } else {
      glow.setAttribute('opacity', '0');
      dimOverlay.setAttribute('opacity', '0');
      if (cmdEl) cmdEl.textContent = 'ls';
    }
  }

  const toSvg = (e) => { const m = svgEl.getScreenCTM(); if (!m) return null; const pt = svgEl.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY; return pt.matrixTransform(m.inverse()); };
  const ACTION = {
    cv:      { type: 'download', href: 'files/Monty-Hunt-CV.pdf', name: 'Monty Hunt "” CV.pdf' },
    edtech:  { type: 'newtab',   href: 'edtech.html' },
    about:   { type: 'go',       href: 'about.html' },
    garden:  { type: 'go',       href: 'garden.html' },
    output:  { type: 'go',       href: 'output.html' },
    gallery: { type: 'go',       href: 'gallery.html' },
  };
  function enter(id) {
    const a = ACTION[id]; if (!a) return;
    if (a.type === 'download') { const l = document.createElement('a'); l.href = a.href; l.download = a.name; document.body.appendChild(l); l.click(); l.remove(); return; }
    if (a.type === 'newtab') { window.open(a.href, '_blank'); return; }
    const ov = document.getElementById('enter-fade');
    if (ov) { ov.style.background = PAL[byId[id].ac].hot; ov.style.opacity = '1'; setTimeout(() => { location.href = a.href; }, 480); }
    else location.href = a.href;
  }
  [...svgEl.querySelectorAll('.hit')].forEach((hit) => {
    const id = hit.dataset.id;
    hit.addEventListener('pointerenter', (e) => { if (!ready || locked) return; const p = toSvg(e); open(id, p && p.x, p && p.y); });
    hit.addEventListener('pointermove', (e) => { if (!ready || locked) return; const p = toSvg(e); if (!p) return; const [bx, by] = clampPt(byId[id], p.x, p.y); glow.setAttribute('cx', bx); glow.setAttribute('cy', by); });
    hit.addEventListener('pointerleave', () => { if (!ready || locked) return; open(null); });
    hit.addEventListener('click', () => { if (!ready) return; enter(id); });
  });

  // flora easter egg
  [...svgEl.querySelectorAll('.flora')].forEach((fl) => {
    fl.addEventListener('pointerenter', () => {
      fl.classList.remove('rustle'); void fl.getBBox(); fl.classList.add('rustle');
      const cx = +fl.dataset.cx, cy = +fl.dataset.cy;
      for (let k = 0; k < 5; k++) {
        const leaf = document.createElementNS(NS, 'ellipse');
        leaf.setAttribute('cx', cx + (Math.random() * 36 - 18)); leaf.setAttribute('cy', cy + Math.random() * 10);
        leaf.setAttribute('rx', 3.2); leaf.setAttribute('ry', 1.9); leaf.setAttribute('fill', '#6E7E4F'); leaf.setAttribute('class', 'leaf');
        leaf.style.setProperty('--d', (1.8 + Math.random() * 1.5) + 's'); leaf.style.setProperty('--dx', (Math.random() * 30 - 15) + 'px');
        leaf.style.transformBox = 'fill-box'; fl.appendChild(leaf);
        leaf.addEventListener('animationend', () => leaf.remove());
      }
    });
  });

  // ---- build timeline (paper already landing via CSS) ----
  const paper = document.getElementById('paper');
  const phase = (id) => { const g = svgEl.querySelector('#' + id); if (g) { g.style.opacity = '1'; g.classList.add('go'); } };
  setTimeout(() => paper.classList.add('taped'), 760);
  setTimeout(() => phase('ph-shell'), 1000);
  setTimeout(() => phase('ph-rooms'), 1560);
  setTimeout(() => phase('ph-details'), 2080);
  setTimeout(() => phase('ph-extra'), 2560);
  setTimeout(() => { phase('ph-names'); document.querySelectorAll('.smudge').forEach((s) => s.style.opacity = '1'); }, 3000);
  setTimeout(() => { ready = true; }, 3450);
  // safety: ensure everything visible by ~4.4s
  setTimeout(() => { ready = true; ['ph-details', 'ph-shell', 'ph-rooms', 'ph-extra', 'ph-names'].forEach((id) => { const g = svgEl.querySelector('#' + id); if (g) { g.style.opacity = '1'; g.classList.add('go'); } }); }, 4400);

  // ---- footsteps + cycling prompt ----
  const stepsG = svgEl.querySelector('#steps');
  const enterMsg = document.getElementById('enterMsg');
  const PROMPTS = ['Enter', 'Explore', 'Come on!'];
  const order = [0, 1, 4, 2, 3]; let oi = 0;
  function walk() {
    enterMsg.textContent = PROMPTS[oi % PROMPTS.length]; enterMsg.style.opacity = '0.9';
    const pts = ROUTES[order[oi % order.length]]; oi++;
    const pp = sample(pts, 36);
    stepsG.innerHTML = pp.map((s, i) => footSVG(s, i)).join('');
    const feet = [...stepsG.children];
    feet.forEach((f, i) => setTimeout(() => { f.style.opacity = '0.6'; }, 260 + i * 220));
    const inEnd = 260 + feet.length * 220;
    setTimeout(() => { enterMsg.style.opacity = '0'; }, inEnd + 500);
    setTimeout(() => feet.forEach((f, i) => setTimeout(() => { f.style.opacity = '0'; }, i * 80)), inEnd + 2200);
    setTimeout(walk, inEnd + 2200 + feet.length * 80 + 5200);
  }
  setTimeout(walk, 3800);
})();

