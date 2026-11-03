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
app('artifact-register.csv', [
    dict(artifact_id='A-0096', captured_at='2026-11-02',
         source_title='Окладные ведомости о помещичьих крестьянах 1858, Карачевский у. — Соколовы (НСА ГАОО)',
         source_url_or_path='https://nsa.gaorel.ru/landowners/pages/gubernia/1/uezd/5/land/1173/index.html ; https://nsa.gaorel.ru/landowners/pages/gubernia/1/uezd/5/land/3363/index.html',
         source_type='archival finding aid (electronic index)', repository_or_archive='ГАОО (Орёл)',
         archival_reference='ГАОО ф.760 оп.1 д.237 л.52 об., 54 об.', record_date='1858',
         place_as_written='Карачевский у.: с. Старое, д. Обельна, д. Суханка; д. Пирятинка', language_script='ru',
         person_ids='P-0026;P-0028', names_as_written='Соколов Дмитрий Иванович, поручик; Соколов Иван Дмитриевич, гвардии поручик',
         summary='Д.И. Соколов: с. Старое (13 дворовых, 100 м.п.), д. Обельна (122), д. Суханка (85). И.Д. Соколов: д. Пирятинка (11 дворовых, 100 м.п.). Там же однофамильцы: полковник Иван и поручик Юрий Александровичи (Девять Дубов, Ефремовское, Благовещенская). Бацовых нет.',
         provenance_level='derivative (index of original)', directness='indirect', originality='index',
         independence_group='IG-GAOO-1858', legibility='typed index', access_notes='копия ф.760 оп.1 д.237 — платно по запросу; ГАОО генеалогию приостановил',
         reliability_notes='отец–сын Д.И./И.Д. только по отчеству — гипотеза', status='lead'),
    dict(artifact_id='A-0097', captured_at='2026-11-02',
         source_title='Black Sea German Research: Freuer во Freudental (метрики 1833–1913, репрессированные, EWZ)',
         source_url_or_path='https://www.blackseagr.org/pdfs/freudental-repressed.pdf ; https://www.blackseagr.org/blksea-db/getperson.php?personID=I25332&tree=63 ; odessa3.org freu18xx.txt',
         source_type='published transcriptions and indexes', repository_or_archive='BSGR / odessa3 (СПб ев.-лют. консистория; ГАОдО ф.894; NARA EWZ)',
         archival_reference='EWZ50-B045 fr.1186 (Lydia Freuer 1920); консистория 1882646-2 с.30 з.20 (Freier=Freuer)', record_date='1836–1942',
         place_as_written='Freudental; Wygoda (приход Freudental); Peterstal', language_script='de/en',
         names_as_written='Freuer / Freier / Fraier / Freyer; Lydia Freuer 20.05.1920 Freudental (муж Alexander Enzi)',
         summary='BSGR: в советских делах Freuer пишется «Fraier/Freyer» → «Фраер» ≈ Freuer, коренная лютеранская фамилия Freudental (родоначальник Adam Freuer 1796–1877). Роберт Freuer в индексах не найден (метрики 1886–1901 и 1914–25 не опубликованы). Лидии-однофамилицы: 1902 (отец Wilhelm), 1913 (отец Johann), 1920 (EWZ, родители не указаны, жила под оккупацией → маловероятно). Wygoda входила в приход Freudental.',
         provenance_level='derivative', directness='indirect', originality='transcription',
         person_ids='P-0018', independence_group='IG-BSGR', legibility='typed', access_notes='сканы ф.894 (1899–1916) — проект «МЕТРИКА» archive.od.gov.ua, бесплатно',
         reliability_notes='отождествление Фраер=Freuer — гипотеза', status='lead'),
])
rows = [
    ('S-0100', 'P-0021', 'Ольга Елескина: рождение 1912–13', 'весь OCR ф.60 оп.6 д.46 (Бачатская ц. 1912–1913, 261 ск.): «Елеск», «Ольга», июльские рождения', 'ya.ru/archive', 'not found', '', 'книга 1914 г. и Челухоевская ц. — отдельно', 'Ольги 1912 (ск.35–38) и 1913 (ск.170) — дети других семей; Елескины в книге только Аполинария, Илья, Иоанн (крёстный), девица …Васильева (ск.136)'),
    ('S-0101', 'P-0006', 'Федосовы: губернские ведомости', 'Яндекс «Периодика»: Федосов+Вихляевка/Тюковка/Новохоперский/мельница', 'ya.ru/archive (Воронежские губ. ведомости)', 'not found', '', '', '1907 №85 — Резанов, не наш; Федосовы Новохопёрского у. не встречаются'),
    ('S-0102', 'P-0018', 'Фраер: черноморские немцы', 'Freuer/Freier/Freyer/Fraier: odessa3, BSGR (76 PDF метрик 1899–1917, 42 списка, БД), EWZ', 'blackseagr.org; odessa3.org', 'found', 'A-0097', 'метрики 1886–1901, 1914–25 не опубликованы', 'смотреть сканы ГАОдО ф.894 Freudental (проект «МЕТРИКА»); ' + SP + 'fraer/report-blacksea.md'),
    ('S-0103', 'P-0026;P-0028', 'Покрытие онлайн-архивов', 'Яндекс Архив, FS Full-Text, ГАОО nsa, ИАОО, ГААО ЕАИС, ГАОдО МЕТРИКА', 'web', 'found', 'A-0096', 'ГАВО/ГАБО из-за рубежа не открываются', SP + 'coverage/report-2026-11-02.md'),
]
app('search-log.csv', [dict(search_id=a, timestamp='2026-11-02', target_person_ids=b, research_goal=c, query=d, language_locale='ru/de', source_or_domain=e, result_status=f, artifact_ids=g, blocker=h, captcha_attempts='0', next_step=i) for a, b, c, d, e, f, g, h, i in rows])
print('ok')
