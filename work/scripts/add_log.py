# -*- coding: utf-8 -*-
import csv, os, sys
os.chdir(os.path.expanduser('~/kinship-cases/sokolov'))
def app(f, new):
    with open(f, newline='', encoding='utf-8') as h:
        hdr = next(csv.reader(h))
    with open(f, 'a', newline='', encoding='utf-8') as h:
        w = csv.DictWriter(h, fieldnames=hdr)
        for r in new:
            w.writerow({k: r.get(k, '') for k in hdr})
with open('search-log.csv', newline='', encoding='utf-8') as h:
    print(next(csv.reader(h)))
R = 'scratchpad/agents/fedosov/r3/'
rows = [
    ('S-0091', 'P-0006', 'Федосовы: метрики/ревизии Вихляевки и Тюковки', 'ВГД ветки Вихляевка/Тюковка/Новохопёрский у.; nashipredki; перечень оцифровки ГАВО; КП т.6', 'forum.vgd.ru; arsvo.ru; nashipredki.com', 'found-finding-aids', '', 'Яндекс Архив (агенту) и АИС ГАВО — вход/платно', 'И-282 оп.2 д.76 = обыски 1891–1912 оцифрованы в АИС ГАВО (платно); Тюковка И-84 оп.2 дд.27,42,62,120; ' + R + 'report-metrics.md'),
    ('S-0092', 'P-0006', 'Федосовы: военные (ПМВ/ВОВ)', 'GWAR Федосов+Воронежская губ. (341), Тюковская вол. (2936), Федосеев/Федосьин; КП ПМВ Воронежской т.I указатель; moypolk Федосов А.Ф.', 'gwar.mil.ru; genrogge.ru; moypolk.ru', 'not found', '', 'ПН 403; ОБД JS', 'новохопёрских Федосовых в GWAR нет; ' + R + 'report-military.md'),
    ('S-0093', 'P-0006', 'Федосовы: раскулачивание/спецпоселение', 'Трагедия сов. деревни т.2; путеводитель ГАВО; ГАОПИ ВО фонды; Поморский мемориал; Вологодская база', 'history.org.ua; arsvo.ru; bessmertnybarak.com', 'found-finding-aids', '', 'booksite.ru 403; memo DNS; visz.nlr.ru', 'ГАВО указатель «Репрессированные» (Р-1172, Р-1439), Р-1818 Песковский РИК; ' + R + 'report-repress.md'),
    ('S-0094', 'P-0006', 'Яков: Тобольск, МВД, могила', 'Федосов Яков Васильевич + Тобольск/МВД/кладбище; Лидия Робертовна', 'web', 'not found', '', 'timenote 403; ПН 403; 72to refused', 'Каргопольлаг (Ерцево) — вероятный ИТЛ 1946; ' + R + 'report-tobolsk.md'),
    ('S-0095', 'P-0006', 'Федосовы: краеведение и онлайн-деревья', 'Федосов + Вихляевка/Тюковка/Песковский; Geni/MyHeritage/WikiTree/FS; riavrn; peskovskoe', 'web', 'not found', '', 'Rodovid 503', 'Байчуровский р-н как вариант; Федосов Г.И. 25-тысячник — однофамилец; ' + R + 'report-kraeved.md'),
    ('S-0096', 'P-0021', 'Елескины: отец/мать/сёстры Ольги', '«Августа Елескина», «Августа Васильева Елескина», «Умерший Василий Елескин», «Василий Димитриев/Павлов Елескин», «Александра Егорова Елескина»', 'ya.ru/archive', 'found', 'A-0093;A-0094', '', 'В.Д. Елескин †04.1917 (чахотка, 48) → C-0049 hypothesis'),
]
app('search-log.csv', [dict(search_id=a, timestamp="2026-11-02", target_person_ids=b, research_goal=c, query=d, language_locale="ru", source_or_domain=e, result_status=f, artifact_ids=g, blocker=h, captcha_attempts="0", next_step=i) for a, b, c, d, e, f, g, h, i in rows])
print('ok')
