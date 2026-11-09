# -*- coding: utf-8 -*-
import csv
D = '2026-11-09'
U = 'https://ya.ru/archive/catalog/2af33095-b37c-4c41-8235-0979727055ae/78'
s = open('case/tree.html', encoding='utf-8').read()


def addcard(cid, html):
    global s
    i = s.find(f'id="{cid}"')
    j = s.find('</div></details>', i)
    assert i > 0 and j > 0
    s = s[:j] + html + s[j:]


addcard('pesterevy', f'<p><b>09.11.2026, сверено по скану: Дарья Ильина Пестерева родилась в августе 1859 года, а не в 1857-м.</b> Запись о рождении Дарьи у «Касминской волости деревни Пестеревой заводского крестьянина Ильи Петрова Пестерева и законной жены его Хионии Марковой» стоит на <a href="{U}">скане 78 дела ф.60 оп.1 д.555</a> (Мало-Салаирская церковь, 1858–1867), среди августовских рождений. Цифру года в заголовке съел корешок («на 185…»), но на следующем скане 79 священник заверяет: «1859 года Сентября 1 дня… в прошлом Августе месяце» родились один мальчик и четыре девочки. Прежнее «1857» — ошибка распознанного текста. Значит, в 1859 году Илья Петров и Хиония Маркова жили в деревне Пестеревой и рожали детей; Иосиф (≈1857–58) мог быть их старшим сыном, но это <b>по-прежнему только гипотеза</b>.</p>'
        '<p><b>09.11.2026, сторонний отчёт (FamilySearch, кадры не сверены нами).</b> По возрасту в браке (18 лет на 16.01.1876) Иосиф родился между 17.01.1857 и 16.01.1858 ст. ст., если возраст точен. Исследователь просмотрел без находки: Салаирская Михаило-Архангельская ц. 1858 (DGS 007469948, кадры 870–891); Петропавловская ц. Салаирского рудника 1857 (DGS 007469955, кадры 172–260) и начало 1858 (DGS 007469948, 905–913, частично); Брюхановская Троицкая ц. 1857 (DGS 007469955, 127–154). Сплошной вычитки не было, поэтому это не доказывает отсутствия записи. В Брюхановской книге 1857 года есть Пестеревы из деревни Пестеревой, например отец Герасима — Трофим Андреев Пестерев (кадр 131). Связь с Иосифом не установлена. Не просмотрены: Бачатская ц. 1857 (DGS 007469954 с кадра 841), Петропавловская 1858 с кадра 914, Брюхановская 1856 и 1858.</p>')

i = s.find('id="ekaterina"')
assert i > 0
addcard('ekaterina', '<p><b>09.11.2026, наводка (не проверена).</b> Брак Лидии Ивановны Бацовой с Петром Николаевичем Всеволожским — предположительно 4 апреля 1882 года в Поздеевке; книга, по волонтёрской описи, ГАРО ф.803 оп.2 д.407 (83 л.). Ссылки: <a href="https://forum.vgd.ru/1608/40175/20.htm">семейная схема на ВГД</a>, <a href="https://inv.velikie.org/archive/garo-rostov/803/2/">опись</a>. Запись не прочитана. Если в ней Лидия названа дочерью поручика Ивана Григорьевича, это подтвердит, что она сестра Екатерины.</p>')
open('case/tree.html', 'w', encoding='utf-8').write(s)


def load(p):
    with open(p, encoding='utf-8', newline='') as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def save(p, fn, rows):
    with open(p, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fn)
        w.writeheader()
        w.writerows(rows)


def nxt(rows, key):
    return max(int(r[key].split('-')[1]) for r in rows) + 1


fn, rows = load('case/artifact-register.csv')
n = nxt(rows, 'artifact_id')
new = [
    dict(artifact_id=f'A-{n:04d}', captured_at=D, source_title='Сторонний отчёт «Важные обновления генеалогического поиска» (09.11.2026, FamilySearch-продолжение)',
         source_url_or_path='inputs/external/важные-обновления.md', source_type='secondary research report', person_ids='P-0022;P-0034',
         summary='Отрицательные просмотры FamilySearch: Салаир Михаило-Арх. 1858 (007469948 870–891), Петропавл. 1857 (007469955 172–260), 1858 нач. (905–913), Брюханово 1857 (127–154); Трофим Андреев Пестерев (Брюханово, к.131); ГАРО 803/2/407 (брак Лидии Бацовой 1882)',
         provenance_level='derivative', directness='indirect', originality='compilation', independence_group='IG-ext-report-0911b',
         reliability_notes='Кадры нами не сверены; просмотр не сплошной', status='registered'),
    dict(artifact_id=f'A-{n+1:04d}', captured_at=D, source_title='Мало-Салаирская ц., ф.60 оп.1 д.555 ск.78–79 — год записи о рождении Дарии',
         source_url_or_path=U, source_type='image of original', repository_or_archive='ГА Кузбасса', archival_reference='ф.60 оп.1 д.555 ск.78–79',
         record_date='1859-08', place_as_written='Касминской волости деревни Пестеревой', language_script='ru (дореф.)', person_ids='P-0034',
         names_as_written='Илья Петровъ Пестеревъ; Хіонія Маркова; Дарія',
         summary='Дария — среди августовских рождений; ск.79: «1859 года Сентября 1 дня… в прошломъ Августѣ мѣсяцѣ мужеска пола 1, женска 4». Год 1859 (не 1857). Цифра года в заголовке ск.78 в корешке.',
         provenance_level='primary-digitized', directness='direct', originality='image of original', independence_group='IG-METRIC-D555',
         legibility='заверительная надпись читается; день рождения по OCR', reliability_notes='Исправляет A-0048', status='registered'),
]
for a in new:
    rows.append({k: a.get(k, '') for k in fn})
for r in rows:
    if r['artifact_id'] == 'A-0048':
        r['source_url_or_path'] = U
        r['summary'] = 'ИСПРАВЛЕНО 09.11: запись Дарии — август 1859 (не 1857). ' + r['summary']
save('case/artifact-register.csv', fn, rows)

fn, rows = load('case/claims-register.csv')
c = nxt(rows, 'claim_id')
rows.append({k: v for k, v in dict(claim_id=f'C-{c:04d}', claim_text='Илья Петров Пестерев и Хиония Маркова (д. Пестерева) — родители Дарии, р. VIII.1859 (не 1857)',
             subject_person_ids='P-0034', claim_type='event', artifact_ids=f'A-{n+1:04d};A-0048', supporting_independence_groups='IG-METRIC-D555',
             status='single-source', confidence='high', rationale='Заверительная надпись 1.09.1859 за август сразу после записи.',
             next_action='Связь с Иосифом (≈1857) — гипотеза; книги 1857: Бачаты 007469954, ГАТО 170-9-601').items() if k in fn})
save('case/claims-register.csv', fn, [{k: r.get(k, '') for k in fn} for r in rows])

fn, rows = load('case/search-log.csv')
sid = nxt(rows, 'search_id')
rows.append({k: v for k, v in dict(search_id=f'S-{sid:04d}', timestamp=D, target_person_ids='P-0022;P-0034',
             research_goal='Проверка стороннего отчёта (Пестеревы, FamilySearch)', query='ya.ru: «Пестерев Хиония» → д.555 ск.78; заголовки ск.77–100',
             language_locale='ru', source_or_domain='ya.ru/archive', result_status='corrected: Дария 1859',
             artifact_ids=f'A-{n:04d};A-{n+1:04d}', next_step='Бачаты 1857 (007469954 к.841+); Петропавл. 1858 с к.914').items() if k in fn})
save('case/search-log.csv', fn, [{k: r.get(k, '') for k in fn} for r in rows])

fn, rows = load('case/person-register.csv')
for r in rows:
    if r['person_id'] == 'P-0034':
        r['relatives_as_reported'] = r['relatives_as_reported'].replace('дочь Дарья (ок. 1857)', 'дочь Дарья (VIII.1859)')
        r['source_artifact_ids'] = (r['source_artifact_ids'] + f';A-{n+1:04d}').strip(';')
save('case/person-register.csv', fn, rows)

open('case/research-state.md', 'a', encoding='utf-8').write(f'''
## 09.11 (24) — второй сторонний отчёт (Пестеревы, FamilySearch) [A-{n:04d}, A-{n+1:04d}, C-{c:04d}]
- **Исправлено по скану:** д.555 ск.78 — Дария у Ильи Петрова Пестерева и Хионии Марковой родилась в VIII.1859 (заверка ск.79 «1859 года Сентября 1 дня… в прошлом Августе»), не 1857. Связь Ильи с Иосифом — гипотеза.
- Отчёт: отрицательные просмотры FamilySearch (Салаир 1857–58, Брюханово 1857) — не сплошные, нами не сверены. Брюханово 1857 к.131: Трофим Андреев Пестерев (д. Пестерева).
- Наводка: брак Лидии Ив. Бацовой и П.Н. Всеволожского 04.04.1882 Поздеевка — ГАРО 803-2-407.
- Дальше: Бачаты 1857 (DGS 007469954 к.841–900); Петропавловская 1858 с к.914 (FamilySearch — только если доступен без входа).
''')
print(n, c, sid)
