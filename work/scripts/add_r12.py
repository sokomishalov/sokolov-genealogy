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
app('artifact-register.csv', [dict(artifact_id='A-0102', captured_at='2026-11-02', source_title='Метрики Песчанской Пророко-Ильинской (Качиры) и Павлодарской (Черноярка) церквей 1869–1889 — все записи Выдриных',
    source_url_or_path='ya.ru/archive/catalog: 6b92da3c-8182-473b-bd6f-d6ef7d82650a (5/17), 405d4ee0-ec98-475d-a92a-5a41c10da702 (5/26), 6bf692e1-a344-4dad-b6f9-58035a80437f (6/18), 89655608-94d9-490f-b390-f85604023ac2 (6/78), 6a9d3821-773a-46a7-b2ef-d7783425dc0a (6/179) и др. — см. '+SP+'vydrin/r3/notes.md',
    source_type='OCR of images of originals', repository_or_archive='ИАОО (Омск)', archival_reference='ф.16 оп.5 д.17,22,26,30,35,41,46; оп.6 д.18,21,36,58,72,78,84,99,112,131,132,172,179,193; оп.11 д.68',
    record_date='1869–1914', place_as_written='выселок/пос. Качировский ст. Железинской (Песчановской); Черноярка', language_script='ru (дореф.)',
    names_as_written='Николай Александров, Стефан Александров, Андрей Александров, Симеон Федоров, Дионисий Стефанов, Николай Дионисиев, Сергий Адрианов, Трофим Андрианов Выдрины и др.',
    summary='~70 записей; реконструкция семей Качир/Черноярки 1810-х–1880-х. Николаев 1885–1917 нет (кроме Николая Трофимовича †1888). Книг 1890–1917 и ЗАГС 1918–25 в Яндексе нет.',
    provenance_level='primary', directness='indirect', originality='image+OCR', independence_group='IG-IAOO-VYDRIN', legibility='OCR хороший, месяцы частично', reliability_notes='связь с Николаем Выдриным (отцом С.Н.) НЕ установлена — однофамильцы', status='lead')])
app('search-log.csv', [dict(search_id='S-0113', timestamp='2026-11-02', target_person_ids='', research_goal='Выдрины Качир: все записи 1870–1917, кандидаты-Николаи', query='ИАОО ф.16 оп.4–14 перебор; сплошной OCR /Выдр|Вытр/', language_locale='ru', source_or_domain='ya.ru/archive (ИАОО)', result_status='found', artifact_ids='A-0102', blocker='книг Песчанской ц. 1890–1917 и ЗАГС 1918–25 онлайн нет', captcha_attempts='0', next_step='ждать отчество Николая от семьи; книги 1890–1917 — ИАОО/Павлодар по запросу; '+SP+'vydrin/r3/report.md')])
print('ok')
