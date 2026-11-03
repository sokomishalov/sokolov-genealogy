# -*- coding: utf-8 -*-
import re,sys
f=sys.argv[1]; t=open(f,encoding='utf-8').read()
def rep(old,new):
    global t
    assert t.count(old)==1, old[:60]
    t=t.replace(old,new)
rep('.treebox svg { display: block; width: 100%; min-width: 980px; height: auto; }',
    '.treebox svg { display: block; width: 100%; min-width: 1400px; height: auto; }')
rep('.hint { font-size: 13px; color: var(--muted); }',
    '.hint { font-size: 13px; color: var(--muted); }\n'
    '.sib { cursor: pointer; }\n'
    '.sib rect { fill: var(--paper); stroke: var(--rule); stroke-width: 1; }\n'
    '.sib .bar { stroke: none; }\n'
    '.sib text { fill: var(--ink); font-family: var(--body); font-size: 10.5px; }\n'
    '.sib.unknown rect { stroke-dasharray: 3 3; fill: transparent; }\n'
    '.sib.unknown text { fill: var(--muted); }\n'
    '.sib:hover rect, .sib:focus rect { stroke: var(--accent); stroke-width: 1.6; }\n'
    '.sib:focus { outline: none; }\n'
    '.sibline { fill: none; stroke: var(--bark-2); stroke-width: 1.4; stroke-linecap: round; }\n'
    '.chip-sw { width: 18px; height: 10px; border-radius: 3px; display: inline-block; border: 1px solid var(--bark-2); background: var(--paper); flex: none; }')
rep('<span class="s-fam"><i class="dot"></i>со слов семьи</span>',
    '<span class="s-fam"><i class="dot"></i>со слов семьи</span>\n      <span><i class="chip-sw"></i>мелкие плашки сбоку — братья и сёстры прямых предков</span>')
rep('viewBox="0 -170 1400 1350"','viewBox="0 -170 1800 1350"')
rep('<p class="hint">На узком экране древо прокручивается вбок.</p>',
    '<p class="hint">Рядом с каждым прямым предком мелкими плашками показаны его братья и сёстры: они висят на той же ветке, что и он. Нажмите на плашку, чтобы открыть справку о предке. На узком экране древо прокручивается вбок.</p>')
xs={"mikhail":900,"andrey":470,"olga":1330,"vika":330,"sergeyn":620,"nikolay":1000,"lidiya":1330,
"sergey1911":150,"asya":340,"yakov":650,"olgade":832,"serafim":1506,"serafimwife":1688,
"sergey1887":229,"klavdiya":411,"vasiliy":650,"ivanbed":1400,"annabed":1582,
"sergey1861":150,"ekaterina":332,"nikita":1110,"paraskeva":1290,"pesterevy":1602,
"ananiy":1110,"ivand":229,"evdokiya":411,"ivanbatsov":600,
"dmitriy":229,"apukhtina":411,"ivann":229,"glazunova":411,"nikolayo":229,"dragoya":600}
start=t.index('const P = ['); end=t.index('];',start)
block=t[start:end]
def fx(m):
    pid=m.group(1)
    return m.group(0) if pid not in xs else re.sub(r'x:\s*\d+', 'x: %d'%xs.pop(pid), m.group(0),1)
block=re.sub(r'\{ id: "(\w+)".*?\}', fx, block)
assert not xs, xs
t=t[:start]+block+t[end:]
rep('el("ellipse", { cx: 700, cy: 1168, rx: 520, ry: 26, class: "ground" });',
    'el("ellipse", { cx: 900, cy: 1168, rx: 700, ry: 26, class: "ground" });')
rep('[[300, 380, 230, 150], [1050, 380, 260, 160], [520, 250, 220, 120], [880, 300, 180, 110], [200, 150, 170, 90], [1150, 260, 150, 100]]',
    '[[330, 380, 300, 150], [1300, 380, 380, 160], [560, 250, 260, 120], [1050, 300, 240, 110], [230, 150, 210, 90], [1500, 260, 220, 100]]')
rep('el("path", { d: "M 650 1170 C 668 1140 676 1125 680 1103 L 720 1103 C 724 1125 732 1140 750 1170 Z", class: "trunk" });',
    'el("path", { d: "M 850 1170 C 868 1140 876 1125 880 1103 L 920 1103 C 924 1125 932 1140 950 1170 Z", class: "trunk" });')
rep('const r = el("text", { x: 1360, y: 1150,','const r = el("text", { x: 1760, y: 1150,')
rep('el("text", { x: 700, y: Y(g) - 34, class: "gen-label"','el("text", { x: 880, y: Y(g) - 34, class: "gen-label"')
sib = r'''
  const SIB = [
    { of: "nikolay", side: "R", items: [["тётя Таня", "Сестра Николая Яковлевича, родилась, когда отец был на фронте (со слов семьи)", "fam"]] },
    { of: "lidiya", side: "R", items: [["Галина · 1935", "Галина Серафимовна, род. 24.05.1935, Шушталеп (запись бабушки Лидии)", "fam"], ["Тамара · 1937", "Тамара Серафимовна, род. 02.04.1937, Гурьевск (запись бабушки Лидии)", "fam"], ["Виктор · 1938", "Виктор Серафимович, род. 13.12.1938, Белово (запись бабушки Лидии)", "fam"]] },
    { of: "serafim", side: "L", items: [["Ольга · 1897", "Ольга Ивановна, род. 1.09.1897 (метрики Урско-Бедаревского)", "one"], ["Александр †1899", "Александр, род. ок. 9.12.1898, умер трёх месяцев", "one"], ["Мария †оспа", "Мария, умерла от оспы (1900–1906)", "one"], ["Анфиса †мл.", "Анфиса, умерла младенцем (книга 1907–1911)", "one"], ["Мария", "Мария (книга 1907–1911)", "one"], ["Владимир †мл.", "Владимир, умер младенцем (книга 1911–1914)", "one"], ["Николай · 1911–14", "Николай, род. 6 декабря (книга 1911–1914)", "one"]] },
    { of: "sergey1887", side: "L", items: [["Мария · 1887–1915", "Мария Сергеевна Власова (1887–1915), сестра (по досье Вики)", "one"]] },
    { of: "ivanbed", side: "L", items: [["Андрей", "Андрей Никитин Бедарев (метрики)", "one"], ["Фива", "Фива Никитина (метрики)", "one"], ["Наталья", "Наталья Никитина (метрики)", "one"], ["Павел †6 мес.", "Павел, умер шести месяцев", "one"], ["Тихон · 1877–89", "Тихон Никитин, 1877–1889", "one"], ["Яков †1890-е", "Яков, умер от поноса в 1890-х", "one"]] },
    { of: "annabed", side: "R", items: [["Александра", "Александра Иосифова Пестерева, вышла замуж ок. 1899", "one"]] },
    { of: "ekaterina", side: "R", w: 150, items: [["Лидия Всеволожская", "Сестра Екатерины Ивановны (по досье Вики)", "one"], ["Евгения Краснянская", "Сестра; умерла в 1954 году в Ницце (по досье Вики)", "one"], ["Владимир · полковник", "Брат Владимир Иванович Бацов, полковник (по досье Вики)", "one"], ["Александр", "Брат Александр (по досье Вики)", "one"]] },
    { of: "nikita", side: "L", items: [["Алексей Ананьев", "Брат Никиты: крёстный Ивана 1874, поручитель на свадьбе Ивана 1896", "one"], ["Анна Ананьева", "Сестра Никиты: крёстная Ивана 1874, вышла замуж в 1884–85", "one"]] },
    { of: "pesterevy", side: "L", w: 120, items: [["Захар Шапошников?", "Захар Иванов Шапошников — крёстный Анны 1876, по-видимому брат Екатерины Ивановны", "hyp"]] },
    { of: "ivand", side: "L", w: 120, items: [["Пелагея †1886", "Пелагея Дмитриевна, умерла 10.11.1886 (РРФ)", "one"], ["Митрофан · 1841–97", "Митрофан Дмитриевич (1841–1897), дворянин-избиратель Карачевского у. (РРФ, ВГД)", "one"]] },
    { of: "dmitriy", side: "L", w: 120, items: [["Иван · 1795", "Иван Иванович Соколов, род. 1795 (РРФ)", "one"], ["ещё 6 детей", "Всего у Ивана Николаевича восемь детей; имена остальных не установлены", "one", 1]] },
    { of: "ivann", side: "L", w: 120, items: [["Василий Николаевич", "Брат Ивана Николаевича (РРФ)", "one"]] }
  ];
  const sibG = el("g", {});
  const sibNodes = [];
  SIB.forEach(s => {
    const a = byId[s.of], y = Y(a.g), cw = s.w || 116, ch = 24, gap = 6;
    const n = s.items.length, cols = n === 1 ? 1 : Math.ceil(n / 2);
    const span = cols * cw + (cols - 1) * gap;
    const x0 = s.side === "R" ? a.x + W / 2 + 10 : a.x - W / 2 - 10 - span;
    const barY = y - H / 2 - 9;
    const colX = c => x0 + c * (cw + gap) + cw / 2;
    const far = s.side === "R" ? colX(cols - 1) : colX(0);
    el("path", { d: `M ${a.x} ${y - H / 2} L ${a.x} ${barY} L ${far} ${barY}`, class: "sibline" }, sibG);
    s.items.forEach((it, i) => {
      const c = n === 1 ? 0 : Math.floor(i / 2), row = n === 1 ? -1 : i % 2;
      const cx = colX(c), top = row < 0 ? y - ch / 2 : row === 0 ? y - ch - 3 : y + 3;
      el("path", { d: `M ${cx} ${barY} L ${cx} ${top}`, class: "sibline" }, sibG);
      sibNodes.push({ s, it, cx, top, cw, ch });
    });
  });
  sibNodes.forEach(({ s, it, cx, top, cw, ch }) => {
    const g = el("a", { href: "#" + s.of, class: "sib" + (it[3] ? " unknown" : ""), tabindex: 0, "aria-label": it[0] + ": " + it[1] }, sibG);
    el("title", {}, g).textContent = it[1];
    el("rect", { x: cx - cw / 2, y: top, width: cw, height: ch, rx: 5 }, g);
    el("rect", { x: cx - cw / 2, y: top + 5, width: 3, height: ch - 10, rx: 1.5, class: "bar", fill: colors[it[2]] }, g);
    el("text", { x: cx + 2, y: top + ch / 2 + 3.6, "text-anchor": "middle" }, g).textContent = it[0];
    g.addEventListener("click", ev => { ev.preventDefault(); openPerson(s.of); });
    g.addEventListener("keydown", ev => { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); openPerson(s.of); } });
  });
'''
anchor='  const colors = { doc: "var(--doc)", one: "var(--one)", hyp: "var(--hyp)", fam: "var(--fam)" };\n'
rep(anchor, anchor+sib)
open(f,'w',encoding='utf-8').write(t)
print('ok')
