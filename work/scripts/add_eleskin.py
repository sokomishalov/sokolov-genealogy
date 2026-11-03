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
Y = 'https://ya.ru/archive/catalog/'
app('artifact-register.csv', [
    dict(artifact_id='A-0093', captured_at='2026-11-02',
         source_title='Метрики Бачатской и Челухоевской церквей — семья инородца Василия Димитриева Елескина (Больше-Бачатский улус)',
         source_url_or_path=' ; '.join(Y + x for x in ['8de75cae-32c6-4666-8981-91dc3c4eb195/87', 'ebfbc3f3-276e-4267-98d0-8b46e3273498/289', 'a7054b47-3378-4623-811c-4dd2c6a6b6bc/192', '271c639f-6411-4e47-9ec0-9d25df1a4c58/165', '89d414ca-7b49-4b7f-b80d-2a91520a4dce/62', 'bb2430b0-0121-44ef-a042-c1771c0d4b39/142']),
         source_type='OCR of images of originals (Яндекс Поиск по архивам)', repository_or_archive='ГА Кузбасса',
         archival_reference='ф.60 оп.1 д.550 ск.87 (брак 1890/91); оп.1 д.715 ск.289; оп.1 д.876 ск.192 (1895); оп.4 д.20 ск.165 (1900); оп.4 д.157 ск.62 (1904); оп.6 д.63 ск.142 (смерть 1917)',
         record_date='1890–1917', place_as_written='Телеутской управы 2 половины улуса Больше-Бачатскаго; 1917: «Улуса Полше Вочатскаго» [OCR]',
         language_script='ru (дореф.)', person_ids='P-0021',
         names_as_written='Василій Димитріевъ Елескинъ; Александра Егорова (Пушкарева); дети: Мавра, Іоаннъ, Татіана, Василиса',
         summary='Брак 1890/91: жених Василий Димитриев Елескин 19 л., невеста Александра Егорова (Пушкарева), крестьянка д. Артыштинской, 20 л. Дети: Мавра (~1893), Иоанн (1895), Татьяна (1900), Василиса (1904). Смерть 04.1917: «гражданинъ Василій Димитріевъ Елескинъ», от чахотки, 48 л. Ольги/Августы среди проиндексированных детей нет (OCR книг 1906–1916 неполон).',
         provenance_level='primary', directness='indirect', originality='image+OCR', independence_group='IG-METRIC-BACHATY',
         legibility='OCR; сканы глазами не сверены', status='registered'),
    dict(artifact_id='A-0094', captured_at='2026-11-02',
         source_title='Метрики Бачатской/Челухоевской церквей — две Августы Васильевны Елескины',
         source_url_or_path='ya.ru/archive: ф.60 оп.1 д.473 ск.57; ' + Y + 'bb2430b0-0121-44ef-a042-c1771c0d4b39/48 ; /84 ; /125',
         source_type='OCR of images of originals', repository_or_archive='ГА Кузбасса',
         archival_reference='ф.60 оп.1 д.473 ск.57; оп.6 д.63 ск.48, 84, 125', record_date='1887–1917',
         language_script='ru (дореф.)', person_ids='P-0021',
         names_as_written='Августа; Василій Павловъ Елескинъ; Павелъ Семеновъ Елескинъ и жена его Августа Васильева; дѣвица Мавра Васильева Елескина (1912)',
         summary='(1) Августа, дочь Василия Павлова Елескина, рожд. 1887–89 (Василий Павлов: брак 1885/86 в 19 л.; жив 10.1917 — поручитель). (2) Августа Васильева — жена Павла Семенова Елескина, мать Анны (10.1912), крёстная 1917 (может быть = (1)). В 1912 крёстная — девица Мавра Васильева Елескина (= дочь В.Д.?).',
         provenance_level='primary', directness='indirect', originality='image+OCR', independence_group='IG-METRIC-BACHATY',
         legibility='OCR', status='registered'),
])
app('claims-register.csv', [dict(
    claim_id='C-0049',
    claim_text='Гипотеза: отец Ольги — Василий Димитриев Елескин (≈1870 – 04.1917, ум. от чахотки), мать — Александра Егоровна (урожд. Пушкарева, крестьянка д. Артыштинской, ≈1870); тогда Ольга рожд. ≈1913–14 (а не 1909), сёстры — Мавра, Татьяна, Василиса',
    subject_person_ids='P-0021', claim_type='parentage', artifact_ids='A-0093;A-0092',
    supporting_independence_groups='IG-METRIC-BACHATY;IG-mom', contradicting_artifact_ids='A-0030',
    status='hypothesis', confidence='low',
    rationale='Согласуется с «отец умер, когда ей было 3» только при рождении Ольги ≈1914; 1909 (запись бабушки) — «не точно». Августа в семье В.Д. не найдена; Августа 1887–89 — дочь Василия Павлова (жив в 1917) → не подходит к «отец умер в 3 года». Смерти других Василиев Елескиных 1911–14 не найдены в OCR.',
    next_action='маме/бабушке: год рождения Ольги, имена сестёр, мать Александра?; глазами — рождения 1913–14 Челухоевской ц. (оп.6 д.46)')])
print('ok')
