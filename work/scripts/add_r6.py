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
app('artifact-register.csv', [dict(artifact_id='A-0099', captured_at='2026-11-02',
    source_title='Каталог ГАОО: дела о помещиках Соколовых Карачевского у. и Дорогой-Бацевой',
    source_url_or_path='https://catalog.gaorel.ru/object/1877484254 ; /object/405330174 ; /object/405278074 ; /object/406352554 ; /object/1875669494 ; /object/11592582',
    source_type='archival catalog (titles only)', repository_or_archive='ГАОО (Орёл)',
    archival_reference='ф.672 оп.1 д.1991 (1845); ф.580 оп.1 д.965 (1854), д.625 (1848); ф.4 оп.1 д.7796 (1904–05, Обельна); ф.6 оп.1 д.1897 (1794–1803); ф.760 оп.1 д.344 л.47об (1858, Дорогая Бацева В.Н.)',
    record_date='1780–1905', place_as_written='Карачевский у.; сц. Обельна; Ливенский у., д. Ивановская', language_script='ru',
    person_ids='P-0026;P-0028', names_as_written='Соколов Д.И.; поручик Соколов; Дорогая Бацева Вера Николаевна, прапорщица',
    summary='Заголовки дел: спор о лугах с участием Соколова Д.И. (1845); земля крестьян помещика Соколова (Карачевский земский суд, 1854); межевание сц. Обельна (1904–05); раздел имения Соколовых (1794–1803). Ведомость 1858: «Дорогая Бацева Вера Николаевна, прапорщица», Ливенский у. Метрик с. Старое и Пирятинки в ГАОО нет — вероятно ГАБО (Брянск). ОДДС ф.68: указатели д.15, 52, 66–69; родословные книги д.55–65.',
    provenance_level='finding aid', directness='indirect', originality='catalog', independence_group='IG-GAOO-CAT',
    legibility='typed', access_notes='сканов нет; копии по запросу (генеалогия в ГАОО приостановлена)', reliability_notes='связь с прямыми предками не проверена', status='lead')])
app('search-log.csv', [dict(search_id='S-0106', timestamp='2026-11-02', target_person_ids='P-0026;P-0028', research_goal='Соколовы/Бацовы: шифры дел ГАОО', query='Соколов, Пирятинка, Обельна, Старое, Бацов, Дорога-Бацев, Калофер; ф.68, ф.101, ф.220', language_locale='ru', source_or_domain='catalog.gaorel.ru', result_status='found', artifact_ids='A-0099', blocker='nsa.gaorel.ru — 404 заглушка', captcha_attempts='0', next_step='метрики Старого/Пирятинки — ГАБО (Брянск); указатели ф.68 — только читальный зал; scratchpad/agents/sokolov/report-gaoo-catalog.md')])
print('ok')
