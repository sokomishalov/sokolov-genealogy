# -*- coding: utf-8 -*-
import csv, os
B=os.path.expanduser('~/kinship-cases/sokolov/')
def rd(f):
    with open(B+f,encoding='utf-8',newline='') as h: r=csv.DictReader(h); return r.fieldnames,list(r)
def wr(f,fn,rows):
    with open(B+f,'w',encoding='utf-8',newline='') as h: w=csv.DictWriter(h,fieldnames=fn); w.writeheader(); w.writerows(rows)
fn,rows=rd('artifact-register.csv'); b={k:'' for k in fn}
rows.append(b|{'artifact_id':'A-0043','captured_at':'2026-10-30','source_title':'Метрики Бачатской церкви — семья инородца Василия Васильева Елескина (улус Больше-Бачатский, Телеутская управа 2 половины)','source_url_or_path':'https://ya.ru/archive/catalog/a7054b47-3378-4623-811c-4dd2c6a6b6bc/199 ; https://ya.ru/archive/catalog/c542d957-740a-4813-868a-0c0b411657c1/164','source_type':'OCR of images of originals','repository_or_archive':'ГА Кузбасса','archival_reference':'ф.60 оп.1 д.876 ск.199 (1898); оп.1 д.473 ск.58 (1887–89); оп.6 д.46 ск.164, 136 (1912–14)','record_date':'1887–1914','place_as_written':'Телеутской управы 2 половины улуса Больше Бачатскаго; «Больше-Улуская»','person_ids':'P-0021','names_as_written':'Аполинарія; инородецъ Василій Васильевъ Елескинъ и законная жена его Анна (Иванова); дѣвица Аполлинария Васильева Елескина','summary':'1898: родилась Аполлинария, родители — инородец Василий Васильев Елескин и Анна (1887–89 — «Анна Иванова»), крестил миссионер свящ. Гавриил Оттыгашев. 1912–14: девица Аполлинария Васильева Елескина «Больше-Улуская» и ещё одна «…Васильева Елескина» — крёстные. Наводка: возможная семья Ольги Васильевны («Улус» в записи бабушки = Больше-Бачатский улус). Не доказано: Василиев Елескиных в улусе несколько (Васильев, Петров, Александров, Димитриев). Рождения Ольги в 1909 (визуально), 1910–11 и 1912–14 (OCR) не найдено','provenance_level':'A','directness':'indirect','originality':'OCR','independence_group':'IG-METRIC-BACHATY-ELESKIN','legibility':'OCR','status':'lead'})
wr('artifact-register.csv',fn,rows)
fn,rows=rd('claims-register.csv')
for r in rows:
    if r['claim_id']=='C-0020':
        r['next_action']='нет в рождениях 1909 (визуально), 1910–11 (оп.5 д.5, OCR), 1912–14 (оп.6 д.46, OCR); наводка — семья Василия Васильева Елескина и Анны Ивановны (улус Больше-Бачатский; дочь Аполлинария 1898) [A-0043]; спросить у бабушки точную дату рождения Ольги, имена её матери и сестёр'
wr('claims-register.csv',fn,rows)
fn,rows=rd('search-log.csv'); b={k:'' for k in fn}
for r in rows:
    if r['search_id']=='S-0035': r['next_step']='см. S-0036'
rows.append(b|{'search_id':'S-0036','timestamp':'2026-10-30','target_person_ids':'P-0021','research_goal':'рождение Ольги Васильевны Елескиной','query':'ф.60 оп.6 д.46 (Бачаты 1912–14, 261 ск.) OCR-перебор «Елеск»/«Ольга…Васил»; Аполлинария Васильева Елескина; Василий Васильев Елескин','language_locale':'ru','source_or_domain':'ya.ru/archive','result_status':'partial','artifact_ids':'A-0043','captcha_attempts':'0','next_step':'вопрос бабушке (дата рождения Ольги, мать, сёстры); при совпадении имени матери «Анна» — искать Ольгу у Василия Васильева Елескина в 1900–1908'})
wr('search-log.csv',fn,rows)
print('ok')
