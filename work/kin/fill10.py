# -*- coding: utf-8 -*-
import csv, os
B=os.path.expanduser('~/kinship-cases/sokolov/')
def rd(f):
    with open(B+f,encoding='utf-8',newline='') as h: r=csv.DictReader(h); return r.fieldnames,list(r)
def wr(f,fn,rows):
    with open(B+f,'w',encoding='utf-8',newline='') as h: w=csv.DictWriter(h,fieldnames=fn); w.writeheader(); w.writerows(rows)
fn,rows=rd('artifact-register.csv'); b={k:'' for k in fn}
rows.append(b|{'artifact_id':'A-0037','captured_at':'2026-10-30','source_title':'Метрическая книга Ур-Бедаревской церкви 1891–1898, ч. 2 о бракосочетавшихся, 1896 г., запись №15 от 4 ноября','source_url_or_path':'https://ya.ru/archive/catalog/85ebaabe-6fd7-41ce-ad20-7843617e0702/85 ; inputs/yandex-archive/ivan-bedarev-brak-1896-d657-s85.png','source_type':'image of original + OCR','repository_or_archive':'ГА Кузбасса','archival_reference':'ф.60 оп.1 д.657 скан 85 (л.80 об.–81)','record_date':'1896-11-04 (ст. ст.)','place_as_written':'Кузнецкого округа Бачатской волости села Урскобедаревского; Касьминской волости деревни Пестеревой','language_script':'ru (дореформ.)','person_ids':'P-0019;P-0020','names_as_written':'Иванъ Никитинъ Бедаревъ; дѣвица Анна Іосифова Пестерева; Іосифъ Ильинъ Пестеревъ','summary':'Жених — крестьянин с. Урско-Бедаревского Иван Никитин Бедарев, православный, первым браком, 21 год; невеста — девица Анна Иосифова Пестерева, дочь крестьянина Касьминской вол. д. Пестеревой Иосифа Ильина Пестерева. Венчал свящ. Василий Юрьев. Поручители по жениху — Алексей Ананьев Бедарев и Вонифатий Терентьев Салагаев; по невесте — Иван Вонифатьев Салагаев и Андрей Бедарев. Прочитано визуально, совпадает с OCR','provenance_level':'A','directness':'direct','originality':'image of original','independence_group':'IG-METRIC-1896-D657','legibility':'good','status':'captured'})
wr('artifact-register.csv',fn,rows)
fn,rows=rd('claims-register.csv'); b={k:'' for k in fn}
rows.append(b|{'claim_id':'C-0022','claim_text':'Иван Никитин Бедарев (р. ок. 1875) венчался 4.11.1896 с девицей Анной Иосифовой Пестеревой из д. Пестеревой Касьминской вол., дочерью Иосифа Ильина Пестерева','subject_person_ids':'P-0019;P-0020','claim_type':'marriage','artifact_ids':'A-0037','supporting_independence_groups':'IG-METRIC-1896-D657','status':'single-source','confidence':'high','rationale':'прямая запись; что это родители Серафима — по совпадению имён супругов «Иван Никитин и Анна Осипова/Иосифова» в метриках детей 1897–1914 того же села','next_action':'рождение Ивана ок. 1875 (ф.60 оп.1 д.108); рождение Анны в Пестеревской/Касьминской церкви ок. 1875–77'})
wr('claims-register.csv',fn,rows)
fn,rows=rd('person-register.csv')
for r in rows:
    if r['person_id']=='P-0020':
        r['preferred_label']='Бедарева (Пестерева) Анна Иосифовна — мать Серафима'
        r['names_as_written']='дѣвица Анна Іосифова Пестерева (брак 1896); Анна Осипова / Анна Иосифова (метрики детей); Анна […]нова (д.104)'
        r['places']='д. Пестерева Касьминской вол. (родина); с. Урско-Бедаревское (после 1896)'
        r['relatives_as_reported']='отец Иосиф Ильин Пестерев; муж P-0019 (брак 4.11.1896); сын P-0007'
        r['source_artifact_ids']+=';A-0037'; r['candidate_status']='probable'
    if r['person_id']=='P-0019':
        r['birth_estimate']='ок. 1875 (21 год на 4.11.1896)'
        r['relatives_as_reported']='жена Анна Иосифова Пестерева (брак 4.11.1896); сын Серафим 1905; отец — Никита (вероятно Никита Ананьев Бедарев — проверяется)'
        r['source_artifact_ids']+=';A-0037'
wr('person-register.csv',fn,rows)
fn,rows=rd('relationship-register.csv'); b={k:'' for k in fn}
rows.append(b|{'relationship_id':'R-0022','person_a_id':'P-0019','relationship_type':'spouse-of','person_b_id':'P-0020','biological_legal_household':'legal (church marriage)','claim_ids':'C-0022','supporting_artifact_ids':'A-0037;A-0020;A-0021','independence_groups':'IG-METRIC-1896-D657;IG-METRIC-1905-D104','status':'corroborated','confidence':'high','rationale':'запись о браке 1896 + метрики детей (Анна Осипова/Иосифова — жена Ивана Никитина)'})
wr('relationship-register.csv',fn,rows)
print('ok')
