# -*- coding: utf-8 -*-
import csv, os
os.chdir(os.path.expanduser('~/kinship-cases/sokolov'))
def app(f, new):
    with open(f, newline='', encoding='utf-8') as h:
        hdr = next(csv.reader(h))
    with open(f, 'a', newline='', encoding='utf-8') as h:
        w = csv.DictWriter(h, fieldnames=hdr)
        for r in new:
            w.writerow({k: r.get(k, '') for k in hdr})
SP = '/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/fa7e9f22-0344-405f-8da9-6094acf0931a/scratchpad/agents/'
app('search-log.csv', [dict(search_id='S-0108', timestamp='2026-11-02', target_person_ids='P-0021', research_goal='Ольга и Августа Елескины: рождения; смерть отца', query='ф.60 оп.6 д.70, д.259, д.63, д.385, д.46, д.3 — OCR «Елеск/Ольг/Август»', language_locale='ru', source_or_domain='ya.ru/archive (ГА Кузбасса)', result_status='partial', artifact_ids='A-0093', blocker='Челухоевские книги 1913–14 онлайн нет', captcha_attempts='0', next_step='смерть В.Д. 1917 сверена глазами (д.63 ск.142); Мавра Васильева — брак 13.10.1917 с Д.Е. Нарышевым (ск.126); Ольги нет в Бачатах 1912–14, 1916–18; дальше: оп.4 д.394 (1908), д.3 ск.66+ (1909), ГАТО 2-е экз.; ' + SP + 'eleskin/r2/report.md')])
print('ok')
