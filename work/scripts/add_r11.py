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
Y = 'https://ya.ru/archive/catalog/'
app('artifact-register.csv', [
 dict(artifact_id='A-0100', captured_at='2026-11-02', source_title='Метрики Урско-Бедаревской ц. 1897–1912 — дети Ивана Никитина и Анны Осиповой (Иосифовой) Бедаревых',
      source_url_or_path=' ; '.join(Y+x for x in ['85ebaabe-6fd7-41ce-ad20-7843617e0702/114','3347c189-e4b0-4549-baf3-feb31396c927/53','b105f887-6b7f-41bc-8688-eb5d1d206c5a/110']),
      source_type='images of originals + OCR (Яндекс Поиск по архивам)', repository_or_archive='ГА Кузбасса',
      archival_reference='ф.60 оп.1 д.657 ск.25,76,114; оп.6 д.1 ск.50,111; оп.4 д.104 ск.20,43,89,171; оп.5 д.31 ск.53,163,276; оп.4 д.386 ск.60,173,207,230; оп.6 д.44 ск.92,110',
      record_date='1897–1913', place_as_written='с. Урско-Бедаревское', language_script='ru (дореф.)', person_ids='P-0019;P-0020;P-0007',
      names_as_written='Ѳива 1897; Александр 1898†1899; Мария 1900†1900; Анна 1902†1904; Руффина †1903; Серафим 26(25).12.1905; Василий 1908; Анфиса 1910†1910; Владимир 1911†; Николай 6.12.1912',
      summary='Сверено глазами: Ѳива, Александр, Мария, Анна, Серафим, Владимир, Николай; по OCR: Василий, Анфиса, Руффина†. Прежняя «Ольга» — ошибка OCR (= Ѳива). Мать до 1911 «Анна Осипова», 1912 «Анна Іосифова». Крёстные-родня: дев. Ѳива и На[та]лья Никитины, Пётр Никитин Бедарев (братья/сёстры Ивана).',
      provenance_level='primary', directness='direct', originality='image', independence_group='IG-METRIC-URBEDAREVO', legibility='частично нечётко (месяцы, дни)', reliability_notes='Руффина/Василий/Анфиса — только OCR', status='registered'),
 dict(artifact_id='A-0101', captured_at='2026-11-02', source_title='Метрики Урско-Бедаревской ц.: брак Никиты Ананьева 1873 и рождение Наталии 1881/82 (крёстная Надежда Гри[горьева])',
      source_url_or_path=Y+'e42a102d-489c-4576-895f-ff655205ec3f/270 ; '+Y+'01bc0367-b9e8-41e9-a143-5f333d189fdb/247', source_type='images of originals', repository_or_archive='ГА Кузбасса',
      archival_reference='ф.60 оп.1 д.108 ск.270 (№3, 22.01.1873); оп.5 д.1 ск.247 (№28 ж.), ск.7', record_date='1861–1882', place_as_written='с. Урско-Бедаревское', language_script='ru (дореф.)', person_ids='P-0024;P-0025',
      names_as_written='Никита Ананьев Бедарев 21; дѣвица Параскева Петрова Ма[к]сонова 20; поруч. Алексей Иванов Бедарев, Гавриил Зеновьев Базов, Фёдор Васильев Максонов; Наталия д. Никиты Ананьева и Параскевы Петровой; восприемница кр. жена Надежда Гри[…]',
      summary='Фамилия невесты читается «Максонова» (не Мансонова). Крёстная внучки — Надежда Гри[горьева] = жена Анания Иванова Бедарева (в оп.5 д.1 с 1861); других Ананиев Бедаревых нет → Ананий Иванов — отец Никиты (сильная косвенная).',
      provenance_level='primary', directness='indirect', originality='image', independence_group='IG-METRIC-URBEDAREVO', legibility='фамилия крёстной в переплёте', status='registered'),
])
app('claims-register.csv', [dict(claim_id='C-0050', claim_text='Отец Никиты Ананьева Бедарева (≈1851–52) — Ананий Иванов Бедарев (жена Надежда Григорьева), с. Урско-Бедаревское',
    subject_person_ids='P-0024', claim_type='parentage', artifact_ids='A-0101;A-0042', supporting_independence_groups='IG-METRIC-URBEDAREVO', status='probable', confidence='medium',
    rationale='Единственный Ананий Бедарев в книгах 1861–1890-х; Надежда Гри[горьева] — крёстная дочери Никиты 1881/82; поручитель на свадьбе 1873 — Алексей Иванов Бедарев (вероятно, брат Анания). Прямой записи рождения Никиты нет (метрик 1850-х нет).',
    next_action='ревизская сказка 1858 / исповедные — ГАТО (Томск); оп.1 д.648, д.703 дочитать')])
app('search-log.csv', [dict(search_id='S-0112', timestamp='2026-11-02', target_person_ids='P-0019;P-0020;P-0024;P-0025', research_goal='Бедаревы: сверка детей, отец Никиты, боковые линии', query='поиск Яндекс Архива + сплошной OCR оп.1 д.657; оп.6 д.1,44,74,249; оп.4 д.104,386; оп.5 д.1,31', language_locale='ru', source_or_domain='ya.ru/archive (ГА Кузбасса ф.60)', result_status='found', artifact_ids='A-0100;A-0101', blocker='1850-х метрик и ревизий 1858 онлайн нет', captcha_attempts='0', next_step='C-0050 probable; Максонова вместо Мансоновой; Илья Петров Пестерев ~1832–36 †1897; не просмотрено оп.1 д.648, д.703, книги 1899, 1903–04, 1909; '+SP+'bedarev/r2/report.md')])
# fix P-0025 name
rows = list(csv.reader(open('person-register.csv', encoding='utf-8')))
for r in rows:
    if r and r[0] == 'P-0025':
        r[1] = r[1].replace('(Мансонова)', '(Максонова)')
        r[-1] = (r[-1] + '; ' if r[-1] else '') + '02.11: визуально «Ма[к]сонова», поручитель Фёдор Васильев Максонов (A-0101)'
csv.writer(open('person-register.csv', 'w', newline='', encoding='utf-8')).writerows(rows)
print('ok')
