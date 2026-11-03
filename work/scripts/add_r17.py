# -*- coding: utf-8 -*-
import csv, os
D = os.path.expanduser('~/kinship-cases/sokolov/')

def append(fn, row):
    with open(D + fn, encoding='utf-8') as f:
        hdr = next(csv.reader(f))
    with open(D + fn, 'a', encoding='utf-8', newline='') as f:
        csv.DictWriter(f, fieldnames=hdr).writerow(row)

append('artifact-register.csv', dict(
    artifact_id='A-0113', captured_at='2026-11-03',
    source_title='Ответ мамы: братья и сёстры Ольги Васильевны',
    source_url_or_path='inputs/family/mom-answers-2026-11-03.txt', source_type='family-oral',
    language_script='ru-Cyrl', person_ids='P-0021',
    names_as_written='Августа; Мавра; Антонина; Михаил; Дмитрий; Иван',
    summary='Сёстры Ольги: Августа, Мавра, Антонина; братья: Михаил, Дмитрий, Иван.',
    provenance_level='secondary-oral', directness='direct', originality='recollection',
    independence_group='IG-mom', legibility='clear', related_claim_ids='C-0049;C-0053', status='registered'))

append('claims-register.csv', dict(
    claim_id='C-0053',
    claim_text='У Ольги Васильевны Елескиной были сёстры Августа, Мавра, Антонина и братья Михаил, Дмитрий, Иван',
    subject_person_ids='P-0021', claim_type='relationship', artifact_ids='A-0113',
    supporting_independence_groups='IG-mom', status='single-source', confidence='medium',
    rationale='семейная память мамы (вторая волна ответов, 03.11)',
    next_action='метрики Челухоевской/Бачатской ц.: рождения Михаила, Димитрия, Августы, Антонины Васильевых Елескиных'))

rows = list(csv.DictReader(open(D + 'claims-register.csv', encoding='utf-8')))
hdr = list(rows[0].keys())
for r in rows:
    if r['claim_id'] == 'C-0049':
        r['artifact_ids'] = 'A-0093;A-0092;A-0113'
        r['rationale'] += (' 03.11: мама назвала сестёр Августа, Мавра, Антонина и братьев Михаил, Дмитрий, Иван — '
                           'совпадают Мавра (~1893) и Иван (Иоанн 1895); брат Дмитрий — по имени деда (Василий Димитриев), обычный обычай. '
                           'Татьяна и Василиса маме не известны (могли умереть рано). Независимого документа о самой Ольге нет.')
        r['next_action'] = 'найти рождения Михаила, Димитрия, Августы, Антонины, Ольги у Василия Димитриева и Александры Егоровны'
with open(D + 'claims-register.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=hdr); w.writeheader(); w.writerows(rows)

prs = list(csv.DictReader(open(D + 'person-register.csv', encoding='utf-8')))
ph = list(prs[0].keys())
for r in prs:
    if r['person_id'] == 'P-0021':
        r['relatives_as_reported'] += '; сёстры Августа, Мавра, Антонина; братья Михаил, Дмитрий, Иван (мама, 03.11)'
        r['source_artifact_ids'] += ';A-0113'
with open(D + 'person-register.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=ph); w.writeheader(); w.writerows(prs)
print('ok')
