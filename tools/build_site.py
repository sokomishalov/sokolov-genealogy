# -*- coding: utf-8 -*-
"""Собирает публичный сайт site/ из case/tree.html и реестров дела.

Живые люди попадают на древо только именем и степенью родства:
их карточки, даты и документы не публикуются.
"""
import csv, html, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASE = os.path.join(ROOT, 'case')
SITE = os.path.join(ROOT, 'site')

LIVING = {'mikhail', 'andrey', 'olga', 'vika', 'sergeyn', 'lidiya'}
LIVING_SIB = {'nikolay', 'lidiya'}
LIVING_REL = {'mikhail': 'это ты', 'andrey': 'отец', 'olga': 'мать', 'vika': 'бабушка по отцу', 'sergeyn': 'дед по отцу', 'lidiya': 'бабушка по матери'}
PIDS = {
    'mikhail': 'P-0001', 'andrey': 'P-0002', 'olga': 'P-0003', 'nikolay': 'P-0004', 'lidiya': 'P-0005', 'yakov': 'P-0006',
    'serafim': 'P-0007', 'asya': 'P-0008', 'vika': 'P-0010', 'sergey1887': 'P-0011', 'sergey1861': 'P-0012', 'ekaterina': 'P-0013',
    'klavdiya': 'P-0014', 'sergey1911': 'P-0015', 'ivanbatsov': 'P-0016', 'sergeyn': 'P-0017', 'olgade': 'P-0018', 'ivanbed': 'P-0019',
    'annabed': 'P-0020', 'serafimwife': 'P-0021', 'pesterevy': 'P-0022;P-0023', 'nikita': 'P-0024', 'paraskeva': 'P-0025',
    'ivand': 'P-0026', 'evdokiya': 'P-0027', 'dmitriy': 'P-0028', 'apukhtina': 'P-0029', 'ivann': 'P-0030', 'glazunova': 'P-0031',
    'nikolayo': 'P-0032', 'frayery': 'P-0035;P-0036',
}
PUBLIC_IMG_DIRS = ('inputs/yandex-archive/', 'inputs/pn/', 'inputs/pamyat-naroda/', 'inputs/rgfond/', 'inputs/decrees/', 'inputs/memo-sokolov1887/')
SCRUB = [r'[^.<>]*?(ДНК|Генотек)[^.<]*\.\s*']
SERAFIM_KIDS = (r'Старшие дети: Галина \(24\.05\.1935, Шушталеп\), Тамара \(02\.04\.1937, Гурьевск\), Виктор \(13\.12\.1938, Белово\); младшая — Лидия\.',
                'Дети: Галина, Тамара, Виктор и младшая Лидия (живые — даты не публикуются).')


def scrub(s):
    for pat in SCRUB:
        s = re.sub(pat, '', s)
    return re.sub(SERAFIM_KIDS[0], SERAFIM_KIDS[1], s)


def main():
    t = open(os.path.join(CASE, 'tree.html'), encoding='utf-8').read()
    nodes = []
    for m in re.finditer(r'\{ id: "(\w+)",\s*g:\s*(\d+), x:\s*(\d+),\s*n: "([^"]*)", s: "([^"]*)", st: "(\w+)"(?:, c: "(\w+)")?', t):
        nid, g, x, n, s, st, c = m.groups()
        nodes.append(dict(id=nid, g=int(g), x=int(x), n=n, s=s, st=st, c=c))
    sib = {}
    for m in re.finditer(r'\{ of: "(\w+)", side: "\w", (?:w: \d+, )?items: (\[\[.*?\]\]) \}', t):
        items = json.loads(m.group(2))
        sib[m.group(1)] = [dict(n=i[0], d=i[1], st=i[2]) for i in items]
    cards = {}
    for m in re.finditer(r'<details class="person s-(\w+)" id="(\w+)"><summary>(.*?)</summary><div class="pbody">(.*?)</div></details>', t, re.S):
        st, cid, summ, body = m.groups()
        pname = re.search(r'<span class="pname">(.*?)</span>', summ)
        pyrs = re.search(r'<span class="pyrs">(.*?)</span>', summ)
        cards[cid] = dict(name=html.unescape(re.sub('<.*?>', '', pname.group(1))) if pname else '',
                          years=html.unescape(re.sub('<.*?>', '', pyrs.group(1))) if pyrs else '', body=scrub(body))
    gaps = re.search(r'<section class="gaps"[^>]*>(.*?)</section>', t, re.S).group(1)
    srcs = re.search(r'<section class="sources"[^>]*>(.*)</section>\s*</main>', t, re.S)
    srcs = srcs.group(1) if srcs else re.search(r'<section class="sources"[^>]*>(.*?)<script', t, re.S).group(1)
    drop = re.compile(r'<li>(?:(?!</li>).)*?(ДНК|Генотек|Telegram, личный чат|Людмила)(?:(?!</li>).)*?</li>', re.S)
    gaps, srcs = drop.sub('', gaps), drop.sub('', srcs)
    gaps = re.sub(r'<h2[^>]*>.*?</h2>', '', gaps)
    srcs = re.sub(r'<h2[^>]*>.*?</h2>', '', srcs)

    arts = list(csv.DictReader(open(os.path.join(CASE, 'artifact-register.csv'), encoding='utf-8')))
    scans_dir = os.path.join(SITE, 'scans')
    shutil.rmtree(scans_dir, ignore_errors=True)
    os.makedirs(scans_dir)
    by_id = {n['id']: n for n in nodes}
    out = []
    for n in nodes:
        living = n['id'] in LIVING
        card = cards.get(n['id'], {})
        docs = []
        if not living and n['id'] in PIDS:
            pids = PIDS[n['id']].split(';')
            for a in arts:
                if not any(p in a['person_ids'].split(';') for p in pids):
                    continue
                if a['source_type'].startswith('family'):
                    continue
                parts = [p.strip() for p in re.split(r'\s;\s|\s;|;\s', a['source_url_or_path'])]
                urls = [p for p in parts if p.startswith('http')]
                imgs = []
                for p in parts:
                    for q in [s.strip() for s in p.split(',')]:
                        q2 = q if q.startswith('inputs/') else ('inputs/yandex-archive/' + q if re.match(r'^[\w.-]+\.(png|jpe?g)$', q) else q)
                        if q2.startswith(PUBLIC_IMG_DIRS) and re.search(r'\.(png|jpe?g)$', q2, re.I):
                            src = os.path.join(CASE, q2)
                            if os.path.isfile(src):
                                dst = os.path.basename(q2)
                                shutil.copy(src, os.path.join(scans_dir, dst))
                                imgs.append('scans/' + dst)
                docs.append(dict(id=a['artifact_id'], t=a['source_title'], ref=a['archival_reference'] or a['repository_or_archive'],
                                 d=a['record_date'], url=urls[0] if urls else '', imgs=imgs))
        sibs = [dict(n=re.sub(r'\s*·.*$', '', i['n']) if n['id'] in LIVING_SIB else i['n'],
                     d='' if n['id'] in LIVING_SIB else i['d'], st='living' if n['id'] in LIVING_SIB else i['st'])
                for i in sib.get(n['id'], [])]
        out.append(dict(id=n['id'], g=n['g'], x=n['x'], n=n['n'], s=LIVING_REL[n['id']] if living else n['s'],
                        st='living' if living else n['st'], c=n['c'],
                        name=card.get('name') or n['n'], years='' if living else card.get('years', ''),
                        body='' if living else card.get('body', ''), docs=docs, sibs=sibs))
    data = dict(nodes=out, gaps=gaps, sources=srcs)
    tpl = open(os.path.join(ROOT, 'tools', 'site_template.html'), encoding='utf-8').read()
    page = tpl.replace('/*__DATA__*/null', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
    open(os.path.join(SITE, 'index.html'), 'w', encoding='utf-8').write(page)
    open(os.path.join(SITE, '.nojekyll'), 'w').close()
    leaks = [w for w in ('24.05.1935', 'ДНК', 'Генотек', '02.04.1937') if w in page]
    print('nodes', len(out), 'docs', sum(len(o['docs']) for o in out), 'scans', len(os.listdir(scans_dir)), 'leaks', leaks)
    if leaks:
        sys.exit(1)


if __name__ == '__main__':
    main()
