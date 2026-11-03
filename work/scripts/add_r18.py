# -*- coding: utf-8 -*-
import csv, os
D = os.path.expanduser('~/kinship-cases/sokolov/')
def append(fn, row):
    hdr = next(csv.reader(open(D + fn, encoding='utf-8')))
    with open(D + fn, 'a', encoding='utf-8', newline='') as f:
        csv.DictWriter(f, fieldnames=hdr).writerow(row)
def edit(fn, key, val, fnc):
    rows = list(csv.DictReader(open(D + fn, encoding='utf-8'))); hdr = list(rows[0].keys())
    for r in rows:
        if r[key] == val: fnc(r)
    with open(D + fn, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=hdr); w.writeheader(); w.writerows(rows)

Y = 'https://ya.ru/archive/catalog/'
append('artifact-register.csv', dict(
    artifact_id='A-0114', captured_at='2026-11-03',
    source_title='Метрики Пестеревской/Бачатской/Челухоевской ц. — дети Василия Павлова Елескина и Анны Захаровой',
    source_url_or_path=f'{Y}4ea8d58c-c9fc-4d1e-81db-0bf11dd9a9d8/213 ; /57 ; {Y}ebfbc3f3-276e-4267-98d0-8b46e3273498/230 ; {Y}271c639f-6411-4e47-9ec0-9d25df1a4c58/130 ; {Y}89d414ca-7b49-4b7f-b80d-2a91520a4dce/5 ; /73 ; {Y}a8c34558-db15-4772-b96f-5973e0585d1d/59 ; {Y}07781ef5-6d70-40be-aa09-326d0a439a05/48 ; {Y}bb2430b0-0121-44ef-a042-c1771c0d4b39/84 ; /125 ; /142',
    source_type='OCR of images of originals (Яндекс Поиск по архивам)', repository_or_archive='ГА Кузбасса',
    archival_reference='ф.60 оп.1 д.423 ск.223 (брак); оп.1 д.473 ск.213, 57; оп.1 д.715 ск.230; оп.4 д.20 ск.130; оп.4 д.157 ск.5, 73; оп.4 д.275 ск.59; оп.6 д.3 ск.48; оп.6 д.63 ск.84, 125, 142; оп.6 д.385 ск.4',
    record_date='1885–1918', place_as_written='Больше-Бачатский улус; д. Заречная Телеутской вол.', language_script='ru (дореф.)',
    person_ids='P-0021',
    names_as_written='Василій Павловъ Елескинъ; Анна Захарова (Буймова); Михаилъ; Августа; Димитрій; Іоаннъ; Анна; Петръ; Антонида',
    summary='Дети В.П. и Анны Захаровой: Михаил 11.01.1887, Августа 11.1889, Димитрий 26.10.1893, Иоанн 14.08.1899, Анна 21.01.1902, Петр 12.06.1903, Антонида 28.02.1906. В.П. жив в 1917 (поручитель, д.63 ск.125). Брак Михаила Васильева 18 л. с Антонидой Ивановой Буймовой 16.10.1912 (д.3 ск.48, визуально). Рождения Ольги у пары не найдено.',
    provenance_level='primary-digitized', directness='indirect', originality='image of original',
    independence_group='IG-METRIC-BACHATY', legibility='OCR; визуально — д.3 ск.48 и д.63 ск.142',
    related_claim_ids='C-0054;C-0049;C-0053', reliability_notes='в основном OCR; Михаил 1887 vs жених 18 л. в 1912 — вероятно два Михаила Васильевича', status='registered'))
append('claims-register.csv', dict(
    claim_id='C-0054',
    claim_text='Гипотеза: Ольга Васильевна Елескина — дочь Василия Павлова Елескина и Анны Захаровой; её братья и сёстры — Михаил 1887, Августа 1889, Димитрий 1893, Иоанн 1899, Антонида 1906',
    subject_person_ids='P-0021', claim_type='parentage', artifact_ids='A-0114;A-0113',
    supporting_independence_groups='IG-METRIC-BACHATY;IG-mom', status='hypothesis', confidence='medium',
    rationale='5 из 6 имён, названных мамой, совпадают с детьми этой пары; Мавры у них нет (Мавра 1894 — дочь В. Димитриева). Против: В.П. жив в 1917, а отец Ольги, по памяти семьи, умер, когда ей было ~3; матери в 1909 было ~43; рождение Ольги не найдено.',
    next_action='смерть Василия Павлова Елескина после 1917; рождения 1907–1916 у пары (книги вне индекса, ГАТО 2-е экз.); маме — Мавра точно родная сестра?'))
def c49(r):
    r['status'] = 'hypothesis'; r['confidence'] = 'low'
    r['rationale'] += ' 03.11 (позже): 5 из 6 названных мамой имён — дети Василия Павлова (C-0054); у Димитриева совпадает только Мавра (Иван есть в обеих семьях). Версия ослабла.'
edit('claims-register.csv', 'claim_id', 'C-0049', c49)
def c53(r): r['artifact_ids'] = 'A-0113;A-0114'
edit('claims-register.csv', 'claim_id', 'C-0053', c53)
append('search-log.csv', dict(
    search_id='S-0117', timestamp='2026-11-03', target_person_ids='P-0021',
    research_goal='Метрики братьев и сестёр Ольги (Михаил, Дмитрий, Иван, Августа, Антонина, Мавра)',
    query='«Михаил/Димитрий/Иоанн/Августа/Антонида/Антонина/Ольга Васильева Елескина»; «Анна Захарова Елескина»; «Александра Егорова Елескина»',
    language_locale='ru', source_or_domain='ya.ru/archive (ГА Кузбасса ф.60)', result_status='found', artifact_ids='A-0114',
    blocker='книги 1907–1916 частично вне индекса', captcha_attempts='0',
    next_step='смерть В.П. Елескина после 1917; ГАТО 2-е экз. Челухоевской ц. 1913–14'))
def p21(r):
    r['source_artifact_ids'] += ';A-0114'
    r['notes'] += ' | 03.11: вероятная семья — Василий Павлов Елескин × Анна Захарова (C-0054), альтернатива — Василий Димитриев (C-0049, ослаблена)'
edit('person-register.csv', 'person_id', 'P-0021', p21)
print('ok')
