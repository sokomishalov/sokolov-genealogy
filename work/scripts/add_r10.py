# -*- coding: utf-8 -*-
import csv, os
os.chdir(os.path.expanduser('~/kinship-cases/sokolov'))
with open('search-log.csv', newline='', encoding='utf-8') as h:
    hdr = next(csv.reader(h))
with open('search-log.csv', 'a', newline='', encoding='utf-8') as h:
    csv.DictWriter(h, fieldnames=hdr).writerow({k: '' for k in hdr} | dict(search_id='S-0111', timestamp='2026-11-02', target_person_ids='P-0006', research_goal='А.Ф. Федосов: адрес семьи в наградных листах', query='ПН podvig-chelovek_nagrazhdenie18349303 (Кр. Звезда 03.09.1943, 115 гв. иптап) и 43964495 (Кр. Звезда, 41 гв. пабр)', language_locale='ru', source_or_domain='pamyat-naroda.ru', result_status='not found', artifact_ids='A-0068', blocker='п.12 «домашний адрес»: в 1943 пусто, в 1945 скрыт сайтом (заливка)', captcha_attempts='0', next_step='русский, член ВКП(б), в РККА с 04.1941, Коношский РВК; родных нет'))
print('ok')
