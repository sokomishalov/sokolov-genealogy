# -*- coding: utf-8 -*-
import csv

D = '2026-11-09'


def load(p):
    with open(p, encoding='utf-8', newline='') as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def save(p, fn, rows):
    with open(p, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fn)
        w.writeheader()
        w.writerows(rows)


def nxt(rows, key, pfx):
    return max(int(r[key].split('-')[1]) for r in rows if r[key].startswith(pfx)) + 1


fn, rows = load('case/artifact-register.csv')
n = nxt(rows, 'artifact_id', 'A-')
ext = f'A-{n:04d}'
new = [
    dict(artifact_id=ext, captured_at=D, source_title='Сторонний отчёт «Полный отчет о генеалогическом поиске» (альтернативный агент, 09.11.2026)',
         source_url_or_path='inputs/external/Полный отчет о генеалогическом поиске.docx', source_type='secondary research report',
         person_ids='P-0014;P-0021;P-0013;P-0016', summary='Чтение «Мо-/това»; Челухоево д.3 = книга 1915; наводки РГВА 37976-1-180, ГАТО 170-9-601, ГАБО 247-1 д.113/117, АВПРИ 1853 д.164, ЦГАМО 43-1-141 л.131 (Мотова Евдокия)',
         provenance_level='derivative', directness='indirect', originality='compilation', independence_group='IG-ext-report-0911',
         reliability_notes='Наводки; чтения сверены отдельно (см. следующие артефакты)', status='registered'),
    dict(artifact_id=f'A-{n+1:04d}', captured_at=D, source_title='Брак С.С. Соколова и Клавдии Алексеевой Мотовой, №122 — визуальная сверка фамилии',
         source_url_or_path='https://ya.ru/archive/catalog/5ccd31f0-8538-4d53-9359-33a52721dec0/291', source_type='image of original',
         repository_or_archive='ЦГА Москвы', archival_reference='ф.203 оп.782 д.179 ск.291 №122', record_date='1910-09',
         place_as_written='Московской г. Бронницкаго у. Михалевской в. и села', language_script='ru (дореф.)', person_ids='P-0011;P-0014',
         names_as_written='клавдія Алексѣева Мо-/това, 20', summary='Перенос «Мо-/това»: первая буква 2-й строки = «т» писаря (ср. «Почетн.»), не «х» (ср. «Михалевской»). OCR «Мохова» ошибочен. Невесте 20 лет.',
         provenance_level='primary-digitized', directness='direct', originality='image of original', independence_group='IG-CGAM-1910',
         legibility='хорошая; одна буква сравнена с почерком', reliability_notes='Та же запись, что A-0107; два независимых чтения (Claude + сторонний отчёт)', status='registered'),
    dict(artifact_id=f'A-{n+2:04d}', captured_at=D, source_title='Челухоевская ц., ф.60 оп.6 д.3 ск.203 — год книги',
         source_url_or_path='https://ya.ru/archive/catalog/07781ef5-6d70-40be-aa09-326d0a439a05/203', source_type='image of original',
         repository_or_archive='ГА Кузбасса', archival_reference='ф.60 оп.6 д.3 ск.203', record_date='1914-12..1915',
         place_as_written='Телеутской волости', language_script='ru (дореф.)', person_ids='P-0021',
         summary='Записи №1–3: рождены 24/17/25 декабря «1914 г.», крещены в январе → книга 1915 г. A-0118 датирован ошибочно (XII.1913–X.1914 → XII.1914–X.1915).',
         provenance_level='primary-digitized', directness='direct', originality='image of original', independence_group='IG-METRIC-BACHATY',
         reliability_notes='Исправляет A-0118', status='registered'),
]
for a in new:
    rows.append({k: a.get(k, '') for k in fn})
for r in rows:
    if r['artifact_id'] == 'A-0118':
        r['source_title'] = r['source_title'].replace('XII.1913–X.1914', 'XII.1914–X.1915 (исправлено 09.11)')
        r['record_date'] = '1914-12..1915-10'
        r['summary'] = 'ИСПРАВЛЕНО 09.11: это книга 1915 г. (декабрьские рождения помечены «1914 г.»), а не 1914. ' + r['summary'].replace('Сканы — 1914 год (не 1915). ', '')
save('case/artifact-register.csv', fn, rows)

fn, rows = load('case/claims-register.csv')
c = nxt(rows, 'claim_id', 'C-')
for cl in [
    dict(claim_id=f'C-{c:04d}', claim_text='Девичья фамилия Клавдии Алексеевны (жены С.С. Соколова 1887) — Мотова; ≈1890 г.р.; крестьянка с. Михалево Бронницкого у.',
         subject_person_ids='P-0014', claim_type='name', artifact_ids=f'A-{n+1:04d};A-0107', supporting_independence_groups='IG-CGAM-1910',
         status='single-source', confidence='high', rationale='Прямая брачная запись, фамилия прочитана визуально двумя исследователями; один документ.',
         next_action='Рождение ≈1889–90 Михалево/Гвоздня (ЦГАМО ф.43); Алексей Ильин Мотов — кандидат в отцы'),
    dict(claim_id=f'C-{c+1:04d}', claim_text='ф.60 оп.6 д.3 ск.203–250 — рождения XII.1914–X.1915 (книга 1915); Челухоевские рождения 1914 не просмотрены — отрицательный результат по Ольге за 1914 снят',
         subject_person_ids='P-0021', claim_type='coverage', artifact_ids=f'A-{n+2:04d};A-0118;{ext}', supporting_independence_groups='IG-METRIC-BACHATY',
         status='single-source', confidence='high', rationale='Пометка «1914 г.» у декабрьских рождений с январским крещением.',
         next_action='Книги 1913–1914: вторые экземпляры (ГАТО) / брак Ольги с Серафимом'),
]:
    rows.append({k: cl.get(k, '') for k in fn})
save('case/claims-register.csv', fn, rows)

fn, rows = load('case/search-log.csv')
s = nxt(rows, 'search_id', 'S-')
rows.append({k: v for k, v in dict(search_id=f'S-{s:04d}', timestamp=D, target_person_ids='P-0014;P-0021;P-0013;P-0016',
             research_goal='Проверка стороннего отчёта 09.11', query='визуальная сверка ЦГА Москвы 203-782-179 ск.291 №122; ГА Кузбасса 60-6-3 ск.203',
             language_locale='ru', source_or_domain='ya.ru/archive', result_status='confirmed: Мотова; corrected: д.3 = 1915',
             artifact_ids=f'{ext};A-{n+1:04d};A-{n+2:04d}', next_step='Рождение Клавдии ≈1889–90; РГВА 37976-1-180 сверить опись').items() if k in fn})
for r in rows[-1:]:
    for k in fn:
        r.setdefault(k, '')
save('case/search-log.csv', fn, rows)

for r in []:
    pass
fn, rows = load('case/person-register.csv')
for r in rows:
    if r['person_id'] == 'P-0014':
        r['preferred_label'] = 'Соколова (Мотова) Клавдия Алексеевна (жена P-0011)'
        r['names_as_written'] = '«крестьянская девица Клавдия Алексеева»; «клавдія Алексѣева Мо-/това» (1910)'
        r['birth_estimate'] = '≈1889–1890 (20 л. в 09.1910)'
        r['source_artifact_ids'] = (r['source_artifact_ids'] + f';A-0107;A-{n+1:04d}').strip(';')
save('case/person-register.csv', fn, rows)

st = open('case/research-state.md', encoding='utf-8').read()
st += f'''
## 09.11 (23) — проверка стороннего отчёта (docx) [{ext}…A-{n+2:04d}, C-{c:04d}, C-{c+1:04d}]
- **Мотова** — подтверждено глазами: №122 «Мо-/това», «т» как в «Почетн.», не «х». Клавдия ≈1890, Михалево. Алексей Ильин Мотов (восприемник 1899) — кандидат в отцы (гипотеза). Евдокия Васильева Мотова † 04.05.1915, 70 л., Гвоздня — ЦГАМО 43-1-141 л.131 (индекс, не скан).
- **Ошибка исправлена**: ф.60 оп.6 д.3 ск.203–250 — книга 1915 (рождения XII.1914–X.1915), а не 1914. Рождения 1914 в Челухоеве не смотрены; по Хронографу Кузбасса 2018 книг 1913–14 в Кемерове нет.
- Наводки из отчёта, не сверены: РГВА 37976-1-180 (Маркел Розин, 1935–46, 8 л., по ВГД); ГАТО 170-9-601 (1857, 531 л.), 633 (1858), 661 (1859); ГАБО 247-1 д.113, 117; АВПРИ «Канцелярия» 1853 д.164 л.234 (Бацов); Начов «Калофер в миналото» с.356.
- Не принято: Фрайеры/Выдрины — новых документов нет; сборник 2012 «…В рабочие колонны» — та же семейная память (не независим); дерево «Черепанов» — производное.
- Дальше: рождение Клавдии (ЦГАМО ф.43, Михалево/Гвоздня 1889–90).
'''
open('case/research-state.md', 'w', encoding='utf-8').write(st)
print(ext, n, c, s)
