# -*- coding: utf-8 -*-
import csv,os
os.chdir(os.path.expanduser('~/kinship-cases/sokolov'))
def rd(f):
    with open(f,encoding='utf-8') as fh: r=csv.DictReader(fh); return r.fieldnames,list(r)
def wr(f,h,rows):
    with open(f,'w',newline='',encoding='utf-8') as fh: w=csv.DictWriter(fh,fieldnames=h); w.writeheader(); w.writerows(rows)
h,rows=rd('person-register.csv')
for r in rows:
    if r['person_id']=='P-0019':
        r['birth_estimate']='май 1874 (заголовок стр. д.73 ск.42 «1874»; согласуется с браком родителей 22.01.1873)'
    if r['person_id']=='P-0024':
        r['birth_estimate']='ок. 1851–52 (21 год при браке 22.01.1873)'
    if r['person_id']=='P-0025':
        r['birth_estimate']='ок. 1852–53 (20 лет при браке 22.01.1873)'
wr('person-register.csv',h,rows)
h,rows=rd('claims-register.csv')
for r in rows:
    if r['claim_id']=='C-0024':
        r['claim_text']=r['claim_text'].replace('в мае 1874 или 1875','в мае 1874')
        r['next_action']='противоречие снято 30.10: брак родителей — книга 1873 г. (д.108 ск.239–285), «1875» на ск.265 — ошибка OCR'
wr('claims-register.csv',h,rows)
h,rows=rd('artifact-register.csv')
for r in rows:
    if r['artifact_id']=='A-0042':
        for k,v in r.items():
            if v and 'вероятно 1874' in v: r[k]=v.replace('вероятно 1874','1873')
    if r['artifact_id']=='A-0041':
        for k,v in r.items():
            if v and '(1875)' in v: r[k]=v.replace('(1875)','(1874)')
wr('artifact-register.csv',h,rows)
h,rows=rd('search-log.csv')
rows.append(dict(zip(h,['S-0047','2026-10-30','P-0019;P-0024','год брака Никиты / рождения Ивана','ф.60 оп.1 д.108: OCR-перебор 341 ск. «Никит Анан»; годы заголовков ск.200–341','ru','ya.ru/archive','','found','A-0042','','0','д.108: ск.239 титул 1873, 240–268 рожд., 269–277 браки (277 «1873»), 278–285 смерти (279 «1873»), 287 титул 1874 → брак Никиты (ск.270) = 22.01.1873; Иван род. май 1874; ск.247 Никита — восприемник; ск.334 смерть Павла, сына Никиты, 6 мес.'])))
wr('search-log.csv',h,rows)
print('ok')
