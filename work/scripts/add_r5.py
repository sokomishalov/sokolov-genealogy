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
app('artifact-register.csv', [dict(artifact_id='A-0098', captured_at='2026-11-02',
    source_title='Бессмертный барак: Фрейер/Фрайер — трудармейцы из Фриденталя и Одесского у.',
    source_url_or_path='https://bessmertnybarak.com/search/#query=Фрейер&section=books ; #query=Фрайер',
    source_type='database index (Книга памяти трудармейцев «Челябметаллургстроя», ОГАЧО)', repository_or_archive='Бессмертный барак / ОГАЧО',
    record_date='1942–1947', place_as_written='Одесская обл., Спартаковский р-н, с. Фриденталь; Херсонская обл., Одесский уезд', language_script='ru',
    person_ids='P-0018', names_as_written='Фрейер Фридрих Яковлевич 1910; Фрайер Иван Яковлевич 1904; Фрайер Яков Рудольфович 1924 (Чкаловская обл.)',
    summary='Фрейер Фридрих Яковлевич 1910 г.р., род. и прож. с. Фриденталь Спартаковского р-на — мобилизован в трудармию, убыл 01.07.1947. Фрайер Иван Яковлевич 1904, род. Одесский у., прож. Чкаловская обл. (хут. Егоровка), трудармия 1942. Подтверждает: фамилия Freuer/Freier во Фрейдентале в советских документах = «Фрейер/Фрайер». «Фройер» — 0.',
    provenance_level='derivative', directness='indirect', originality='index', independence_group='IG-BESSBARAK',
    legibility='typed', reliability_notes='однофамильцы; связь с Лидией Робертовной не установлена', status='lead')])
rows = [
    ('S-0104', 'P-0018', 'Фраер: варианты в базах репрессированных', 'Фройер/Фрейер/Фрайер: Бессмертный барак; веб; Открытый список (поиск закрыт входом)', 'bessmertnybarak.com; openlist.wiki', 'found', 'A-0098', 'openlist: поиск только после входа', 'Фрейер Фридрих Яковлевич 1910 Фриденталь — однофамилец'),
    ('S-0105', 'P-0021', 'Ольга Елескина: рождение; смерть отца', 'весь OCR ф.60 оп.6 д.3 (Челухоево 1905,1910–11,1915; 293 ск.) и оп.4 д.157 (Бачаты 1900–08,1912,1915; 307 ск.): Ольга+Елеск, Василий … Елескин', 'ya.ru/archive', 'not found', '', 'книги 1909, 1914, 1916 не найдены; OCR слабый', 'Василий Петров Елескин ум. 11.(1915?) 86 л. (оп.6 д.3 ск.290) — не отец; опись 6: д.70 Бачаты 1913–1915 ещё не найдена в каталоге'),
]
app('search-log.csv', [dict(search_id=a, timestamp='2026-11-02', target_person_ids=b, research_goal=c, query=d, language_locale='ru', source_or_domain=e, result_status=f, artifact_ids=g, blocker=h, captcha_attempts='0', next_step=i) for a, b, c, d, e, f, g, h, i in rows])
print('ok')
