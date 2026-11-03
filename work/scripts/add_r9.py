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
rows = [
 ('S-0109','P-0006','Федосовы: GWAR/ПН родственники','GWAR донесение 13463176, госп. 22067616, выгрузки Рождественской/Тюковской вол.; ПН Федосов/Федосеев + Вихляевка/Байчуровский/Поворинский/Песковский; Пролейка','gwar.mil.ru; pamyat-naroda.ru','not found','A-0066;A-0068;A-0088','','Федосеев Иван — Рождественская вол., а Вихляйка в Тюковской → слабо; Пролейка = склейка с Федоровым (Сталинград) → версия снята; дальше наградные листы А.Ф. Федосова, ЦАМО личное дело Якова; '+SP+'fedosov/r5/report.md'),
 ('S-0110','P-0021','Ольга Елескина: Бачаты 1908–09','OCR ф.60 оп.4 д.394 (c99a9bbe-5b65-4eb6-b891-4b1162c84fae, ск.1–215) «Елеск»','ya.ru/archive','not found','','','Елескины: Иаков Иванов (ск.5), дѣвица Елена Васильева (ск.75), брак Василия Николаева 2-м браком (ск.180); Ольги нет'),
]
app('search-log.csv',[dict(search_id=a,timestamp='2026-11-02',target_person_ids=b,research_goal=c,query=d,language_locale='ru',source_or_domain=e,result_status=f,artifact_ids=g,blocker=h,captcha_attempts='0',next_step=i) for a,b,c,d,e,f,g,h,i in rows])
print('ok')
