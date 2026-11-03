# -*- coding: utf-8 -*-
import csv, os
D = os.path.expanduser('~/kinship-cases/sokolov/')
def append(fn, row):
    hdr = next(csv.reader(open(D + fn, encoding='utf-8')))
    with open(D + fn, 'a', encoding='utf-8', newline='') as f:
        csv.DictWriter(f, fieldnames=hdr).writerow(row)
Y = 'https://ya.ru/archive/catalog/07781ef5-6d70-40be-aa09-326d0a439a05/'
append('artifact-register.csv', dict(
    artifact_id='A-0115', captured_at='2026-11-03',
    source_title='Челухоевская ц.: смерти детей Василия Павлова Елескина (1905); смерть Анны Захаровой Нарышевой (1915)',
    source_url_or_path=f'{Y}54 ; {Y}55 ; {Y}290', source_type='OCR of images of originals (Яндекс Поиск по архивам)',
    repository_or_archive='ГА Кузбасса', archival_reference='ф.60 оп.6 д.3 ск.54, 55, 290 (№52)', record_date='1905; 21.11.1915',
    place_as_written='Телеутская вол., д. Зарѣчная', language_script='ru (дореф.)', person_ids='P-0021',
    names_as_written='Василія Павлова Елескина дочь Анна; сынъ Петръ; инородка Анна Захарова Нарышева',
    summary='Умерли от поноса: Анна (р.1902) ~27.01.1905, Петр (р.1903) 03.1905. Анна Захарова Нарышева, д. Заречная, ум. 21.11.1915 (визуально; возраст в сгибе) — другая фамилия, скорее не мать Ольги.',
    provenance_level='primary-digitized', directness='indirect', originality='image of original',
    independence_group='IG-METRIC-BACHATY', legibility='OCR; ск.290 визуально', related_claim_ids='C-0054', status='registered'))
append('search-log.csv', dict(
    search_id='S-0118', timestamp='2026-11-03', target_person_ids='P-0021',
    research_goal='Смерть Василия Павлова Елескина и Анны Захаровой; рождения пары 1907–1916 (Ольга)',
    query='OCR «Елескин», «Павловъ Елескинъ», «Захарова/Захарьева», «Ольга», «Заречн» по книгам ф.60',
    language_locale='ru', source_or_domain='ya.ru/archive (ГА Кузбасса ф.60)',
    filters='оп.4 д.375 (1907, новая), оп.5 д.5, оп.6 д.3, д.63, д.259; ЗАГС Р-1239 оп.1 1922–25 (OCR)',
    result_status='partial', artifact_ids='A-0115',
    blocker='Челухоевских книг 1906–09, 1913, 1914, 1916 и метрик 1919–24 онлайн нет; ЗАГС-бланки 1922–25 плохо распознаются', captcha_attempts='0',
    next_step='глазами: рождения 1915 (оп.6 д.3 ск.202–258); смерти ЗАГС Р-1239 оп.1 д.231, 309 (1922), д.624 (1924), д.826–828, 866–867 (1925); ГАТО ф.170 — онлайн описи нет'))
print('ok')
