# -*- coding: utf-8 -*-
import csv, os
os.chdir(os.path.expanduser('~/kinship-cases/sokolov'))
def app(f, new):
    with open(f, newline='', encoding='utf-8') as h: hdr = next(csv.reader(h))
    with open(f, 'a', newline='', encoding='utf-8') as h:
        w = csv.DictWriter(h, fieldnames=hdr)
        for r in new: w.writerow({k: r.get(k, '') for k in hdr})
app('artifact-register.csv', [dict(artifact_id='A-0095', captured_at='2026-11-02',
    source_title='GWAR: донесение о потерях — Федосеев Иван, рядовой 236-го пехотного Борисоглебского полка (12.11.1915)',
    source_url_or_path='https://gwar.mil.ru/heroes/chelovek_donesenie13463176/ ; scratchpad/agents/fedosov/r3/gwar/rozhd.json',
    source_type='index of original (GWAR)', repository_or_archive='РГВИА (через gwar.mil.ru)', record_date='1915-11-12',
    place_as_written='Воронежская губ., Новохоперский уезд, Рождественская вол.; событие: д. Войши', language_script='ru',
    names_as_written='Федосеев Иван', summary='Единственный Фед-однофамилец в 3260 карточках GWAR по Рождественской вол. Воронежской губ. (в 1900 Вихляйка — в Рождественской вол., СНМ 1900). Село не указано. Связь с Федосовыми Вихляевки не установлена.',
    provenance_level='index', directness='indirect', originality='index', independence_group='IG-GWAR', legibility='clear', status='lead')])
app('search-log.csv', [
    dict(search_id='S-0097', timestamp='2026-11-02', target_person_ids='P-0006', research_goal='Федосовы: справочники 1880–1917', query='ПК Воронежской губ. 1908, 1915 (поиск+указатель); СНМ 1900; Вся Россия', language_locale='ru', source_or_domain='archive.org; istmat.org', result_status='not found', blocker='istmat 429; elib.shpl; rusneb 403; prlib', captcha_attempts='0', next_step='СНМ 1900: Вихляйка — Рождественская вол.; scratchpad/agents/fedosov/r3/report-printed.md'),
    dict(search_id='S-0098', timestamp='2026-11-02', target_person_ids='P-0006', research_goal='GWAR по Рождественской вол.', query='gwar.py volost --volost Рождественская --gubernia Воронежская (3260)', language_locale='ru', source_or_domain='gwar.mil.ru', result_status='lead', artifact_ids='A-0095', captcha_attempts='0', next_step='Федосеев Иван 236 пп — кандидат, не сливать')])
print('ok')
