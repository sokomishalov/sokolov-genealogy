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
B='https://ya.ru/archive/catalog/8e1f71c4-0f8b-4aa2-b139-e84917563795/'
app('artifact-register.csv',[dict(artifact_id='A-0061',captured_at=D,source_title='Метрическая книга церкви с. Урско-Бедаревского 1907–1911 (ф.60 оп.4 д.386) — дети Ивана Никитина и Анны Осиповой Бедаревых',source_url_or_path=B+'60 ; '+B+'173 ; '+B+'207 ; '+B+'230 ; inputs/yandex-archive/vasiliy-bedarev-rozhd-1908-op4-d386-s60.png, anfisa-bedareva-rozhd-1910-op4-d386-s173.png, anfisa-bedareva-smert-1910-op4-d386-s207.png, vladimir-1911-dup-and-maria-logunova-op4-d386-s230.png',source_type='image of original',repository_or_archive='ГА Кузбасса',archival_reference='ф.60 оп.4 д.386 ск.51 (титул «на 1908 годъ»), 60, 157 (титул 1910), 173, 207, 230',record_date='1908-03-16; 1910-07-24; 1910-08-12; 1911-07-07 (ст. ст.)',place_as_written='Бачатской волости, села Урско-Бедаревского',language_script='ru (дореф., рукопись)',person_ids='P-0019;P-0020',names_as_written='Василій; Анѳиса; Иванъ Никитинъ Бедаревъ и законная жена его Анна Осипова',summary='ск.60 (1908): №19 муж., род. 16, крещ. 22 марта, Василий. ск.173 (1910): №39 жен., род. 24 июля, крещ. 28, Анфиса. ск.207 (1910, умершие): №23 жен., † 12 [авг.], погреб. 13, «крестьянина Ивана Никитина Бедарева дочь младенец Анфиса». ск.230 (1911): второй экземпляр записи о рождении Владимира (№41, 7/20 июля); следующая запись — Мария (№36) у крестьянина Терентия Логунова, НЕ Бедаревых',provenance_level='A',directness='direct',originality='image of original',independence_group='IG-METRIC-UB-1891-1914',legibility='good',related_claim_ids='C-0035;C-0036',reliability_notes='прежняя сводка A-0040 «Мария, рожд. ск.230» — ошибка OCR (склейка соседних записей)',status='captured')])
app('claims-register.csv',[dict(claim_id='C-0036',claim_text='Ещё дети Ивана Никитина и Анны Осиповой Бедаревых: Василий род. 16.03.1908 (крещ. 22.03); Анфиса род. 24.07.1910 (крещ. 28.07), † 12.08.1910. Вторая «Мария (1907–1911)» в прежней сводке — ошибка: на ск.230 Мария — дочь Терентия Логунова',subject_person_ids='P-0019;P-0020',claim_type='births/death (+ correction)',artifact_ids='A-0061',supporting_independence_groups='IG-METRIC-UB-1891-1914',status='single-source',confidence='high',rationale='первичная метрика, сверено визуально; годы по титулам ск.51 и 157',next_action='книга 1900–1906 (оп.4 д.104) — Мария†оспа и возможные дети 1899–1904')])
upd('artifact-register.csv','artifact_id','A-0040',{'reliability_notes':lambda s:s+'; 30.10: оп.4 д.386 ск.230 — НЕ Мария Бедарева (дочь Т. Логунова), а дубль рождения Владимира 1911 (A-0061)'})
upd('person-register.csv','person_id','P-0019',{'relatives_as_reported':lambda s:s.replace('Николай 6.12.1912','Николай 6.12.1912; Василий 16.03.1908; Анфиса 24.07–12.08.1910 (A-0061)')})
app('search-log.csv',[dict(search_id='S-0058',timestamp=D,target_person_ids='P-0019;P-0020',research_goal='дети Ивана Бедарева 1907–1911',query='ф.60 оп.4 д.386: OCR-перебор 265 ск. «Иван(ъ) Никит|Анна Осип/Іосиф»; визуально ск.51, 60, 157, 173, 207, 230',language_locale='ru',source_or_domain='ya.ru/archive',result_status='found',artifact_ids='A-0061',captcha_attempts='0',next_step='оп.4 д.104 (1900–1906)')])
print('ok')
