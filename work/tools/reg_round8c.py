# -*- coding: utf-8 -*-
import csv,os
C=os.path.expanduser('~/kinship-cases/sokolov/')
def app(fn,rows):
    with open(C+fn,newline='',encoding='utf-8') as f: hdr=next(csv.reader(f))
    with open(C+fn,'a',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=hdr)
        for r in rows: w.writerow({k:r.get(k,'') for k in hdr})
def upd(fn,key,val,changes):
    rows=list(csv.DictReader(open(C+fn,newline='',encoding='utf-8'))); hdr=list(rows[0].keys())
    for r in rows:
        if r[key]==val:
            for k,v in changes.items(): r[k]=v(r[k]) if callable(v) else v
    w=csv.DictWriter(open(C+fn,'w',newline='',encoding='utf-8'),fieldnames=hdr); w.writeheader(); w.writerows(rows)
D='2026-10-30'
B='https://ya.ru/archive/catalog/a48bd695-c9a3-404a-bf45-ed30d19c7844/'
app('artifact-register.csv',[dict(artifact_id='A-0062',captured_at=D,source_title='Метрическая книга церкви с. Ур-Бедаревского 1900–1903, 1905–1906 (ф.60 оп.4 д.104) — дети Ивана Никитина и Анны Осиповой Бедаревых',source_url_or_path=B+'20 ; '+B+'43 ; '+B+'89 ; '+B+'128 ; inputs/yandex-archive/maria-bedareva-rozhd-1900-op4-d104-s20.png, anna-bedareva-rozhd-1902-op4-d104-s89.png, anna-bedareva-smert-1902-op4-d104-s128.png',source_type='image of original',repository_or_archive='ГА Кузбасса',archival_reference='ф.60 оп.4 д.104 ск.3 (1900), 20, 43, 87 (1902), 89, 128',record_date='1900-07-27; 1900-12; 1902-01-24; 1902-11-04 (ст. ст.)',place_as_written='Бачатской волости, села Урско-Бедаревского',language_script='ru (дореф., рукопись)',person_ids='P-0019;P-0020',names_as_written='Марія; Анна; Иванъ Никитинъ Бедаревъ и законная жена Анна Осипова',summary='ск.20 (1900): №33 жен., род. 27 июля, крещ. 8 авг., Мария; восприемница девица Наталья Никитина Бедарева. ск.43 (1900, умершие, декабрь): «крестьянина Ивана Никитина Бедарева дочь младенец Мария», от оспы (OCR; день не сверен). ск.89 (1902): №5 жен., род. 24 янв., крещ. 27, Анна. ск.128 (1902, умершие): №21 жен., † 4 нояб., погреб. 5, «крестьянина Ивана Никитина Бедарева дочь младенец Анна»',provenance_level='A',directness='direct',originality='image of original',independence_group='IG-METRIC-UB-1891-1914',legibility='good',related_claim_ids='C-0037',reliability_notes='годы — по титулам (OCR) и порядку книги; рождение 1900 и 1902 сверены визуально; смерть Марии 1900 — по OCR',status='captured')])
app('claims-register.csv',[dict(claim_id='C-0037',claim_text='Дети Ивана Никитина и Анны Осиповой Бедаревых: Мария род. 27.07.1900, † дек. 1900 (оспа); Анна род. 24.01.1902, † 4.11.1902 (ст. ст.)',subject_person_ids='P-0019;P-0020',claim_type='births/deaths',artifact_ids='A-0062',supporting_independence_groups='IG-METRIC-UB-1891-1914',status='single-source',confidence='high',rationale='первичная метрика; итог по книгам 1897–1914: Ольга 1897, Александр 1898†, Мария 1900†, Анна 1902†, Серафим 1905, Василий 1908, Анфиса 1910†, Владимир 1911†, Николай 1912; 1899, 1904 — в работе/нет книги',next_action='1904 — книга ф.60 (1894, 1897, 1904); 1899 — д.648/657')])
upd('person-register.csv','person_id','P-0019',{'relatives_as_reported':lambda s:s.replace('Анфиса 24.07–12.08.1910 (A-0061)','Анфиса 24.07–12.08.1910 (A-0061); Мария 27.07–дек.1900, Анна 24.01–4.11.1902 (A-0062)')})
app('search-log.csv',[dict(search_id='S-0059',timestamp=D,target_person_ids='P-0019;P-0020',research_goal='дети Ивана Бедарева 1900–1906',query='ф.60 оп.4 д.104: OCR-перебор 275 ск.; визуально ск.20, 89, 128',language_locale='ru',source_or_domain='ya.ru/archive',result_status='found',artifact_ids='A-0062',captcha_attempts='0',next_step='1904 (книга 1894, 1897, 1904)')])
print('ok')
