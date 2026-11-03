# -*- coding: utf-8 -*-
import csv, os
os.chdir(os.path.expanduser('~/kinship-cases/sokolov'))
with open('search-log.csv', newline='', encoding='utf-8') as h:
    hdr = next(csv.reader(h))
with open('search-log.csv', 'a', newline='', encoding='utf-8') as h:
    csv.DictWriter(h, fieldnames=hdr).writerow({k: v for k, v in dict(search_id='S-0107', timestamp='2026-11-02', target_person_ids='P-0018', research_goal='Роберт Freuer и дочь Лидия во Фройдентале', query='ф.894 оп.1 спр.23 (1908), спр.29 (1911): рождения/смерти Николаевки, Петерсталя, Мариенталя', language_locale='ru/de', source_or_domain='archive.od.gov.ua «МЕТРИКА»', result_status='not found', artifact_ids='', blocker='онлайн только 1908 и 1911; за 1914–16 книг прихода в ф.894 нет', captcha_attempts='0', next_step='ГАОдО запрос: дд.2,5,10,25,28,34,38 (1899–1903, 1909–13); Freuer-отцы 1908/1911: Wilhelm, Johann, Jakob — не Роберт; scratchpad/agents/fraer/report-daoo-894.md').items() if k in hdr})
print('ok')
