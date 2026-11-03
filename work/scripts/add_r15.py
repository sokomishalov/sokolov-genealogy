# -*- coding: utf-8 -*-
import csv, os
C = os.path.expanduser('~/kinship-cases/sokolov')
V6 = '/Users/sokomishalov/Downloads/aggregated-genealogy-findings-2026-11-02-v6.txt'
SP = '/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/fa7e9f22-0344-405f-8da9-6094acf0931a/scratchpad/v6'
OD = 'https://archive.od.gov.ua/wp-content/uploads/metrics/%D0%A4%D0%BE%D0%BD%D0%B4%D0%B8%20%D0%BD%D0%BE%D0%B2%D0%B8%D1%85%20%D0%B0%D0%BA%D1%82%D1%96%D0%B2/r_08001_08300/r_08201_08300/'


def append(name, rows):
    p = os.path.join(C, name)
    with open(p, newline='', encoding='utf-8') as f:
        hdr = next(csv.reader(f))
    with open(p, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=hdr)
        for r in rows:
            assert set(r) <= set(hdr), set(r) - set(hdr)
            w.writerow(r)


D = '2026-11-02'
append('artifact-register.csv', [
    dict(artifact_id='A-0108', captured_at=D,
         source_title='Блинова О.Э. Воспоминания матери, Фишлер (Фрайер) Анны Робертовны, 1920–1997 // Немецкое население на Южном Урале в военные и послевоенные годы. Оренбург, 2013',
         source_url_or_path='https://www.osu.ru/sites/niisu/docs/germans.pdf#page=118; ' + SP + '/germans.pdf',
         source_type='published memoir (derivative of family notebook 1996)', repository_or_archive='ОГУ НИИ истории и этнографии Южного Урала',
         archival_reference='печ. с.116–120 (PDF 117–121)', record_date='1996 (написано); 2013 (публ.)',
         place_as_written='хутор в 30 км от Одессы; д. Выгода (с 1925); Вологда, монастырь Прилуки (1930); кирпичный завод №5 (1932–34); ст. Коноша, пос. Норминга (08.1934); Бугуруслан (трудармия 1942)',
         language_script='ru', person_ids='P-0018;P-0035;P-0036;P-0037',
         names_as_written='Фрайер Анна Робертовна 1920; Фрайер Роберт Вильгельмович; Фрайер (Энгель) Каролина Фридриховна; Фишлер Эрих Александрович',
         summary='6 дочерей Роберта и Каролины: 1918, 1920 (Анна), 1922, 1924, 1926 и младенец (~1929). Выгода 1925; раскулачены 11.1929; высылка 02.1930 в Вологду; младшая умерла 1930, ещё одна — на Украине ~1932; 4 дочери в Вологде 1932; 08.1934 — Коноша, пос. Норминга; отец арестован (~1935), 5 лет, Печора, не вернулся; бабушка (мать отца) жила на хуторе. Имена сестёр не названы. Норминга = Норменга, место рождения Николая Яковлевича 14.04.1938.',
         provenance_level='derivative', directness='direct for Anna; indirect for Lidia', originality='derivative', independence_group='IG-BLINOVA-MEMOIR',
         legibility='clear', access_notes='open PDF, прочитано 02.11.2026', sha256='', related_claim_ids='C-0052',
         reliability_notes='прочитано лично; внутреннее противоречие: «старшая сестра, 1920-го года рождения» при старшей 1918', status='captured'),
    dict(artifact_id='A-0109', captured_at=D, source_title='ДАОО ф.Р-8220 (Беляевский райЗАГС): описи оп.2а (кадр 00003) и оп.1а (кадр 00004)',
         source_url_or_path=OD + 'r_08220_02a/ukrnod01d_fr-8220-op2a-opys_m_00003.jpg; ' + OD + 'r_08220_01a/ukrnod01d_fr-8220-op1a-opys_m_00004.jpg',
         source_type='archival inventory images', repository_or_archive='ДАОО (Держархів Одеської обл.)',
         archival_reference='Р-8220 оп.2а д.2 (алфавит рождений 1924–1925, 98 л., Біляївський р-н вкл. Фрейденталь, К.Лібенталь, Нейбург, Петерсталь); Р-8220 оп.1а д.20 (рождения 1925, 377 л.; Фрейденталь 13.01.192[4→5]–31.12.1925)',
         record_date='1924–1925', place_as_written='Біляївський район, с. Фрейденталь', language_script='uk', person_ids='P-0018;P-0035',
         names_as_written='', summary='Описи (не акты). Адрес поиска рождения дочери Фрайеров 1924 г. (если в Фрейдентале). Выгода в описях 1920-х не выделена (только 1934 — оп.1а д.74; 1935 — д.82). Сами книги онлайн не выложены.',
         provenance_level='primary', directness='indirect', originality='original images', independence_group='IG-DAOO-R8220',
         legibility='clear', access_notes='open jpg; сверено глазами 02.11.2026', sha256='', related_claim_ids='', reliability_notes='наличие семьи внутри неизвестно', status='captured'),
    dict(artifact_id='A-0110', captured_at=D, source_title='Книга памяти Краснодарского края, т.3: ФРАЕР Адольф Вильгельмович 1904',
         source_url_or_path='https://bessmertnybarak.com/books/person/294838/', source_type='published memorial book (web)',
         repository_or_archive='Бессмертный барак', archival_reference='шифр не указан («20174» без легенды)', record_date='1938',
         place_as_written='род. г. Одесса; Туапсе', language_script='ru', person_ids='P-0038', names_as_written='ФРАЕР Адольф Вильгельмович',
         summary='1904 г.р., Одесса, немец; агент снабжения Туапсинского дома отдыха НКВД; арест 05.01.1938; ОСО 31.01.1938 ВМН; расстрелян 11.02.1938; реабилитирован 12.11.1955. Отчество совпадает с Робертом Вильгельмовичем — возможный брат, не доказано.',
         provenance_level='derivative', directness='indirect', originality='derivative', independence_group='IG-KK-MEMORY',
         legibility='clear', access_notes='прочитано 02.11.2026', sha256='', related_claim_ids='', reliability_notes='родство не установлено', status='captured'),
    dict(artifact_id='A-0111', captured_at=D, source_title='Википедия: Бацов, Владимир Иванович (раздел литературы)',
         source_url_or_path='https://ru.wikipedia.org/wiki/Бацов,_Владимир_Иванович', source_type='secondary biography',
         repository_or_archive='РГВИА (ссылки)', archival_reference='РГВИА ф.409 оп.1 «п/с 259 (1912 г.)»; ф.400 оп.9 д.34943 л.4об.; ф.400 оп.12 д.26977 л.57–59 (1914)',
         record_date='1912–1914', place_as_written='', language_script='ru', person_ids='P-0013;P-0016', names_as_written='Бацов Владимир Иванович, 01.10.1865',
         summary='Адрес проверки послужного списка брата Екатерины Ивановны; родители в нём могут быть названы. «п/с 259» — не современный шифр дела.',
         provenance_level='derivative', directness='indirect', originality='derivative', independence_group='IG-WIKI-BATSOV',
         legibility='clear', access_notes='прочитано 02.11.2026', sha256='', related_claim_ids='', reliability_notes='шифры не сверены с описью РГВИА', status='captured'),
    dict(artifact_id='A-0112', captured_at=D, source_title='ДАХО ф.928 оп.1 т.2 ч.2, с.56: д.3967 Соколов Сергей Сергеевич 1906–1913, 17 л.',
         source_url_or_path='https://archives.kh.gov.ua/wp-content/uploads/2018/02/ф.928-оп.1-том-2-частина-2.pdf (PDF стр.6)', source_type='archival inventory image',
         repository_or_archive='ДАХО (Держархів Харківської обл.)', archival_reference='ф.928 оп.1 д.3967', record_date='1906–1913',
         place_as_written='Харьков', language_script='ru', person_ids='P-0011', names_as_written='Соколов Сергей Сергеевич',
         summary='Личное дело учащегося 1906–1913. С.С. Соколов 1887 к 09.1910 — «ветеринарный врач»; Харьковский ветеринарный институт — вероятный кандидат, но название фонда 928 не сверено.',
         provenance_level='primary', directness='indirect', originality='original image of inventory', independence_group='IG-DAHO-928',
         legibility='clear', access_notes='сверено глазами 02.11.2026', sha256='', related_claim_ids='', reliability_notes='тождество не доказано', status='lead'),
])

append('claims-register.csv', [
    dict(claim_id='C-0052', claim_text='Лидия Робертовна Фраер — одна из дочерей Роберта Вильгельмовича Фрайера и Каролины Фридриховны Энгель (Выгода 1925 → Вологда 1930 → Коноша/Норминга 1934)',
         subject_person_ids='P-0018;P-0035;P-0036', claim_type='parentage', artifact_ids='A-0108;A-0030',
         supporting_independence_groups='IG-BLINOVA-MEMOIR;IG-FAMILY-LIDIYA', contradicting_artifact_ids='', status='corroborated', confidence='medium',
         rationale='Независимые источники совпадают по 5 признакам: фамилия Фрайер/Фраер, отчество Робертовна, д. Выгода Беляевского р-на, немцы-лютеране, пос. Норменга/Норминга Коношского р-на (где 14.04.1938 родился Николай). Сестёр Анна не называет; Лидия — вероятно 1918 или 1922 г.р. (к 1938 матери 20/16 лет).',
         next_action='ЗАГС Арх. обл.: рождение Николая 14.04.1938 / брак Якова ~1936–37 (возраст, место рождения матери); ИЦ УМВД Арх. обл.: учётное дело спецпоселенцев Фрайер (Роберт, Каролина); семья Блиновой О.Э. (Бугуруслан) — имена сестёр — только по «да»'),
])

append('search-log.csv', [
    dict(search_id='S-0116', timestamp=D, target_person_ids='P-0018;P-0013;P-0011;P-0014;P-0021',
         research_goal='Проверка внешнего отчёта v6 (агрегатор)', query='сверка источников v6: osu.ru germans.pdf; ДАОО Р-8220 описи; бессмертный барак; Википедия Бацов; ДАХО ф.928; ДАОО ф.630 указатель; familio Мотов; Ницца',
         language_locale='ru;uk;fr', source_or_domain='osu.ru; archive.od.gov.ua; bessmertnybarak.com; ru.wikipedia.org; archives.kh.gov.ua; familio.org; recherche.archives.nicecotedazur.org',
         filters='', result_status='found', artifact_ids='A-0108;A-0109;A-0110;A-0111;A-0112',
         blocker='Ницца: anti-bot (Anubis) — не обходили; ГААО/ГАТО/Кузбасс/old-kursk — не перепроверялись (приняты как наводки v6)', captcha_attempts='0',
         next_step='C-0052; запрос ЗАГС Арх. обл. и ИЦ УМВД (по «да»); РГВИА ф.409 оп.1 п/с 259; ДАХО ф.928 д.3967; ДАОО Р-8220 оп.2а д.2 / оп.1а д.20 (запрос); ' + V6),
])
print('ok')

append('person-register.csv', [
    dict(person_id='P-0035', preferred_label='Фрайер Роберт Вильгельмович (кандидат в отцы Лидии Робертовны)', living_status='deceased',
         names_as_written='Фрайер Роберт Вильгельмович', normalized_name_variants='Фраер; Freier; Freuer; Frayer', birth_estimate='до ~1897', death_estimate='после ~1935 (Печора, не вернулся)',
         places='хутор ~30 км от Одессы; Выгода (1925–29); Вологда (1930–34); Коноша, пос. Норминга (1934–~35); Коми АССР, Печора',
         historical_jurisdictions='Одесский окр./Беляевский р-н; Северный край', relatives_as_reported='жена P-0036; дочери 1918,1920 (P-0037),1922,1924,1926,~1929; мать жила на хуторе (1929–30)',
         occupation_or_status='крестьянин; раскулачен 11.1929; спецпоселенец; лесозаготовки; арестован ~1935, 5 лет', confession_or_community_as_recorded='немцы (лютеране?)',
         source_artifact_ids='A-0108', candidate_status='probable', merge_or_split_rationale='', notes='см. C-0052; брат? — Адольф Вильгельмович P-0038'),
    dict(person_id='P-0036', preferred_label='Фрайер (Энгель) Каролина Фридриховна (кандидат в матери Лидии)', living_status='deceased',
         names_as_written='Фрайер (Энгель) Каролина Фридриховна', normalized_name_variants='Engel', birth_estimate='до ~1900', death_estimate='',
         places='Выгода; Вологда (кирпичный завод №5); Коноша, Норминга (доярка в колхозе)', historical_jurisdictions='', relatives_as_reported='муж P-0035; «мамин племянник» вывез детей 04.1930',
         occupation_or_status='', confession_or_community_as_recorded='немка', source_artifact_ids='A-0108', candidate_status='probable', merge_or_split_rationale='', notes=''),
    dict(person_id='P-0037', preferred_label='Фишлер (Фрайер) Анна Робертовна 1920–1997 (вероятная сестра Лидии)', living_status='deceased',
         names_as_written='Фрайер Анна Робертовна; Фишлер-Фрайер', normalized_name_variants='', birth_estimate='1920', death_estimate='1997',
         places='хутор ~30 км от Одессы; Норминга (до 10.1942); Бугуруслан', historical_jurisdictions='', relatives_as_reported='отец P-0035; мать P-0036; муж Фишлер Эрих Александрович (1907–1976); дочь Блинова О.Э.',
         occupation_or_status='трудармия 1942', confession_or_community_as_recorded='', source_artifact_ids='A-0108', candidate_status='probable', merge_or_split_rationale='',
         notes='её потомки живы — не исследовать; контакт только по «да»'),
    dict(person_id='P-0038', preferred_label='Фраер Адольф Вильгельмович 1904–1938 (возможный брат Роберта)', living_status='deceased',
         names_as_written='ФРАЕР Адольф Вильгельмович', normalized_name_variants='Freier', birth_estimate='1904', death_estimate='11.02.1938',
         places='Одесса; Туапсе', historical_jurisdictions='', relatives_as_reported='', occupation_or_status='агент снабжения; расстрелян 1938',
         confession_or_community_as_recorded='немец', source_artifact_ids='A-0110', candidate_status='hypothesis', merge_or_split_rationale='не объединять с Adolf Freier 1904 (EWZ, Freudental) без первичных данных', notes=''),
])

append('relationship-register.csv', [
    dict(relationship_id='R-0034', person_a_id='P-0035', relationship_type='parent-of', person_b_id='P-0018', biological_legal_household='biological',
         claim_ids='C-0052', supporting_artifact_ids='A-0108;A-0030', contradicting_artifact_ids='', independence_groups='IG-BLINOVA-MEMOIR;IG-FAMILY-LIDIYA',
         status='corroborated', confidence='medium', rationale='совпадение фамилии, отчества, Выгоды и Норменги; прямого акта нет'),
    dict(relationship_id='R-0035', person_a_id='P-0036', relationship_type='parent-of', person_b_id='P-0018', biological_legal_household='biological',
         claim_ids='C-0052', supporting_artifact_ids='A-0108', contradicting_artifact_ids='', independence_groups='IG-BLINOVA-MEMOIR',
         status='hypothesis', confidence='medium', rationale='следует из C-0052, если Лидия — дочь Роберта от этого брака'),
])

p = os.path.join(C, 'person-register.csv')
rows = list(csv.DictReader(open(p, encoding='utf-8')))
hdr = list(rows[0].keys())
for r in rows:
    if r['person_id'] == 'P-0018':
        r['relatives_as_reported'] += '; вероятные родители P-0035/P-0036; сестра? P-0037'
        r['source_artifact_ids'] += ';A-0108'
        r['candidate_status'] = 'probable'
        r['notes'] += ' | 02.11 (v6): воспоминания Анны Робертовны Фрайер (Блинова 2013) — Роберт Вильгельмович × Каролина Энгель, Выгода 1925, Норминга 1934; дочери 1918/1922/1924/1926; C-0052.'
with open(p, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=hdr); w.writeheader(); w.writerows(rows)
print('persons ok')
