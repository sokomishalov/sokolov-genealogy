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
app('artifact-register.csv', [dict(artifact_id='A-0103', captured_at='2026-11-02', source_title='Список репрессированных немцев Одесской обл. 1930–1950 (6618 чел.) + BSGR метрики Freudental 1902–1913',
    source_url_or_path='https://hfdr.de/wp-content/uploads/2023/10/Repressierten_1930-1950_im_Odessa-Gebiet_6618.pdf ; https://www.blackseagr.org/research_church_odessa.html',
    source_type='published lists / transcriptions', repository_or_archive='HFDR; BSGR (ГАОдО ф.894)', archival_reference='№5176, 5183, 5216, 5217; ф.894 оп.1 д.5,18,29,34,38', record_date='1902–1950',
    place_as_written='Фрейденталь, Овидиопольский р.; Выгода Немецкая', language_script='ru/de', person_ids='P-0018',
    names_as_written='Фраер Яков Яковлевич 1895; Фрайер (Фрейер, Фреер) Карл Карлович 1918; Фрейер Карл Яковлевич 1892; Фрейер Фридарика Яковлевна 1885; Lydia Freuer 7.02.1913 (Johann × Christina Becker)',
    summary='Написание «Фраер» встречается у Фрейденталя (Яков Яковлевич 1895). Отца Robert Freuer нет ни в метриках 1902–13, ни в списке репрессированных. Ohlhauser Lucas (Freudental) † 1931 Архангельск — пример маршрута. Выселение 02.1930 из Одесской округи шло в Северный край.',
    provenance_level='derivative', directness='indirect', originality='index/transcription', independence_group='IG-BSGR;IG-HFDR', legibility='typed', reliability_notes='все — однофамильцы до подтверждения', status='lead')])
app('search-log.csv', [dict(search_id='S-0114', timestamp='2026-11-02', target_person_ids='P-0018', research_goal='Фраер: высылка Выгода/Фрейденталь → Северный край', query='reabit.org.ua, HFDR список 6618, BSGR (метрики 1902–13, личные, EWZ), Поморский мемориал, DAI Wygoda, Яндекс Архив', language_locale='ru/uk/de', source_or_domain='web', result_status='not found', artifact_ids='A-0103', blocker='memo.ru/visz.nlr.ru недоступны; именных списков выселенных 1930 онлайн нет', captcha_attempts='0', next_step='главный путь — ЗАГС Арх. обл. (брак Я.В., рождение Николая 1938) — по «да»; '+SP+'fraer/r3/report.md')])
print('ok')
