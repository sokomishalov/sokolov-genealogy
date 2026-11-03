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
B='https://ya.ru/archive/catalog/ccd3ca76-193d-421d-92e7-e93ea0690ce8/'
app('artifact-register.csv',[dict(artifact_id='A-0063',captured_at=D,source_title='Метрическая книга церкви с. Урско-Бедаревского за 1894, 1897, 1904 гг. — Ольга 1897 (2-й экз.), Анна 1904',source_url_or_path=B+'50 ; '+B+'90 ; '+B+'111 ; inputs/yandex-archive/anna2-bedareva-rozhd-1904-ccd3-s90.png, anna2-bedareva-smert-1904-ccd3-s111.png',source_type='image of original',repository_or_archive='ГА Кузбасса',archival_reference='ф.60 (книга ccd3ca76…; шифр описи/дела не выписан) ск.3 (1894), 34 (1897), 70 (1904), 50, 90, 111',record_date='1897-09-01; 1904-11-26; 1904-12-22 (ст. ст.)',place_as_written='Бачатской волости, села Урско-Бедаревского',language_script='ru (дореф., рукопись)',person_ids='P-0019;P-0020',names_as_written='Ольга; Анна; Иванъ Ни[китинъ] Бедаревъ и законная жена его […]нова',summary='ск.50 (1897): №50, 1/14 сент., Ольга — 2-й экземпляр записи (восприемница девица Фива Никитина Бедарева). ск.90 (1904, декабрь): №39 жен., род. 26 нояб., крещ. 13 [дек.], Анна; родители кр. Иван Ни[китин] Бедарев и законная жена его […]нова. ск.111 (1904, умершие, декабрь): №27 жен., † 22, погреб. 23, «крестьянина Ивана Никитина Бедарева дочь младенец Анна»',provenance_level='A',directness='direct',originality='image of original',independence_group='IG-METRIC-UB-1891-1914',legibility='good; имя матери в записи рождения 1904 — [неразборчиво]…нова',related_claim_ids='C-0038',reliability_notes='шифр книги в каталоге не выписан (вероятно ф.60 оп.1 или оп.4)',status='captured')])
app('claims-register.csv',[dict(claim_id='C-0038',claim_text='Дочь Ивана Никитина Бедарева Анна (вторая) род. 26.11.1904, † 22.12.1904 (ст. ст.)',subject_person_ids='P-0019;P-0020',claim_type='birth/death',artifact_ids='A-0063',supporting_independence_groups='IG-METRIC-UB-1891-1914',status='single-source',confidence='medium-high',rationale='смерть — явно «Ивана Никитина Бедарева дочь»; в записи рождения имя матери неразборчиво («…нова»), других Иванов Никитиных Бедаревых в книгах не встречено',next_action='')])
upd('person-register.csv','person_id','P-0019',{'relatives_as_reported':lambda s:s+'; Анна (2-я) 26.11–22.12.1904 (A-0063)'})
app('search-log.csv',[dict(search_id='S-0060',timestamp=D,target_person_ids='P-0019;P-0020',research_goal='дети Ивана Бедарева 1904 (и 1903)',query='книга «1894, 1897, 1904» (ccd3ca76…) OCR-перебор 111 ск.; д.104 ск.132–160 и ccd3 ск.70–95: «Анна» + Бачатской…Бедар',language_locale='ru',source_or_domain='ya.ru/archive',result_status='found',artifact_ids='A-0063',captcha_attempts='0',next_step='1899 — д.648/657 (проверено ранее частично)')])
print('ok')
