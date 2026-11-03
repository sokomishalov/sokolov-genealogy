# -*- coding: utf-8 -*-
import csv,os
C=os.path.expanduser('~/kinship-cases/sokolov/')
def upd(fn,key,val,changes):
    rows=list(csv.DictReader(open(C+fn,newline='',encoding='utf-8')))
    hdr=list(rows[0].keys())
    for r in rows:
        if r[key]==val:
            for k,v in changes.items(): r[k]=v(r[k]) if callable(v) else v
    w=csv.DictWriter(open(C+fn,'w',newline='',encoding='utf-8'),fieldnames=hdr); w.writeheader(); w.writerows(rows)
upd('claims-register.csv','claim_id','C-0005',{'artifact_ids':lambda s:s+';A-0056;A-0057;A-0058','supporting_independence_groups':lambda s:s+';IG-MVD-RT-KAZAN;IG-MOSCOW-REHAB','status':'corroborated','confidence':'high','rationale':lambda s:s+'; 30.10: дата ареста 12.11.1941 и ст.58-10 ч.2 подтверждены казанским списком МВД РТ и московским списком реабилитированных','next_action':''})
upd('person-register.csv','person_id','P-0011',{'death_estimate':'1942, Казань, спец. (тюремная) психбольница: 10.07.1942 (досье; «Бессмертный барак», дело ИЦ МВД РТ 16458) / 10.12.1942 (Книга памяти РТ) — C-0032','source_artifact_ids':lambda s:s+';A-0056;A-0057;A-0058'})
upd('person-register.csv','person_id','P-0012',{'relatives_as_reported':lambda s:s+'; брат Тихон Иванович 23.11.1863 (РРФ, A-0059)'})
upd('person-register.csv','person_id','P-0019',{'relatives_as_reported':lambda s:s+'; дети (метрики, A-0060): Владимир 7.07.1911–11.02.1912, Николай 6.12.1912'})
print('ok')
