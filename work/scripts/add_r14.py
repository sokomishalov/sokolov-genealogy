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
D = dict(captured_at='2026-11-02', language_script='ru (дореф.)')
app('artifact-register.csv', [
 D | dict(artifact_id='A-0104', source_title='Сенатские объявления о запрещениях на имения 1835 и 1857 — Соколовы Карачевского у. (Старое, Обельна, Суханка, Пырятинка)',
   source_url_or_path=Y+'e979bb5b-8b2d-4005-ae1b-3767bb0c11b3/9 ; '+Y+'8187ec96-e940-417d-9cab-eddbe2e692ca/31 ; '+Y+'1e797da8-8b21-429a-bac0-7856bac1f630/92 ; '+Y+'37ca1e70-f45b-489c-9b93-7c7d4a0c47eb/2',
   source_type='official gazette (printed)', repository_or_archive='Яндекс Архив (периодика)', archival_reference='1835 №29 с.9; №33 с.31; №48 с.92; 1857 №5 с.2', record_date='1835; 15.11.1856',
   place_as_written='Карачевскаго уѣзда: село Старое, деревни Обельна, Суханка, Пырятинка', person_ids='P-0028;P-0026',
   names_as_written='Соколовъ Дмитрій Ивановъ, Поручикъ; СОКОЛОВЪ Иванъ Дмитріевъ, Капитанъ',
   summary='1835: Д.И. — Старое 112, Обельна 119, Суханка 60 душ; отдельно Пырятинка 103 души. 1856/57: И.Д. (капитан) — Пырятинка 115 душ по 9-й ревизии. Переход Пырятинки от Д.И. к И.Д. поддерживает отцовство.',
   provenance_level='primary (printed official)', directness='indirect', originality='OCR', independence_group='IG-SENAT', legibility='OCR, глазами не сверено', status='registered'),
 D | dict(artifact_id='A-0105', source_title='Брачные документы Митрофана Дмитриевича Соколова, Москва 1880 (справка Успенской ц. Карачевского у.)',
   source_url_or_path=Y+'0a0ea694-0843-4b3b-95ba-2e707f68793d/34', source_type='image of original (copy of certificate)', repository_or_archive='ЦГА Москвы',
   archival_reference='ф.2125 оп.3 д.224 ск.34; д.225 ск.18; ф.203 оп.776 д.959 ск.194', record_date='24.09.1880', place_as_written='Карачевский у., Успенская ц. (с. Старое); Москва, ц. Спаса Преображения на Песках', person_ids='P-0028',
   names_as_written='Митрофанъ Дмитріевичъ Соколовъ, 39 лѣтъ; отставной поручикъ Димитрій Ивановичъ и законная жена его (нынѣ умершая) Соколовы; невеста Зинаида Дмитриевна Макарова',
   summary='Прямое отцовство Д.И. для Митрофана (~1841); прихожане Успенской ц. (с. Старое). Мать не названа (умерла до 1880).',
   provenance_level='primary', directness='direct', originality='image', independence_group='IG-CGAM-1880', legibility='сверено глазами', status='registered'),
 D | dict(artifact_id='A-0106', source_title='Копия справки Орловской консистории 30.01.1896 о рождении Сергея Сергеевича Соколова (Апальково, 29.12.1887)',
   source_url_or_path=Y+'94f03d92-b420-4fcb-b332-daccd1129682/74', source_type='image of certified copy', repository_or_archive='ЦГА Москвы', archival_reference='ф.2122 оп.3 д.218 ск.74 (копия МК Николаевской ц. с. Апальково 1888 ч.1 №3)', record_date='29.12.1887 / 11.01.1888',
   place_as_written='село Апальково Кромского уѣзда', person_ids='P-0011;P-0012;P-0013',
   names_as_written='Сергій; Артиллеріи поручикъ Сергій Ивановъ Соколовъ и законная жена его Екатерина Иванова; восприемники свящ. Григорий Иванов Переверзев и Губерн. гор. Орла вдова титулярнаго совѣтника Анна Николаева Соколова',
   summary='Независимая от досье Вики копия записи о рождении С.С. 1887; отец С.И. — артиллерии поручик (1887), коллежский асессор, кромской землевладелец (1896). Крёстная Анна Николаевна Соколова — вероятно, бабушка (вдова И.Д.?) — гипотеза.',
   provenance_level='derivative (certified copy)', directness='direct', originality='image', independence_group='IG-CGAM-1896', legibility='сверено глазами', status='registered'),
 D | dict(artifact_id='A-0107', source_title='Брак С.С. Соколова и Клавдии Алексеевны (Москва, 09.1910) и метрики с. Михалево ~1912',
   source_url_or_path=Y+'5ccd31f0-8538-4d53-9359-33a52721dec0/291', source_type='OCR of images of originals', repository_or_archive='ЦГА Москвы; ЦГАМО', archival_reference='ЦГА Москвы ф.203 оп.782 д.179 ск.291 (№122); ЦГАМО ф.43 оп.1 д.145 ск.142,152,209', record_date='09.1910; ~1912',
   place_as_written='Трёхсвятительская ц. на Кулишках; с. Михалево Бронницкого у.; имение Соколовка Кромского у.', person_ids='P-0011;P-0014',
   names_as_written='Ветеринарный врачъ Сергѣй Сергѣевъ Соколовъ, 22; Клавдия Алексеевна (OCR Мохова/Мотова), крестьянка с. Михалево; дочь Милица; сын Георгий † 1 г.',
   summary='Брак 09.1910 в Москве; С.С. окончил Харьковский ветинститут 1910; имение Соколовка. В Михалево ~1912: рождение Милицы, смерть Георгия (OCR; годы и мать в индексе сомнительны).',
   provenance_level='primary', directness='direct', originality='OCR', independence_group='IG-CGAM-1910', legibility='OCR, фамилия невесты неясна', reliability_notes='даты Михалево не сверены', status='registered'),
])
app('claims-register.csv', [dict(claim_id='C-0051', claim_text='Иван Дмитриевич Соколов (1829–1870) — сын поручика Дмитрия Ивановича Соколова (ок.1802–1888)', subject_person_ids='P-0026;P-0028', claim_type='parentage',
   artifact_ids='A-0104;A-0105;A-0096', supporting_independence_groups='IG-SENAT;IG-CGAM-1880;IG-GAOO-1858', status='probable', confidence='medium',
   rationale='Пырятинка: 1835 — Д.И., 1856 — И.Д. (переход имения); отчество; Д.И. — отец Митрофана (~1841), прихожане Успенской ц. с. Старого, как и С.И. 1861 (род. близ Пырятинки). Прямой метрики нет.',
   next_action='ГАБО ф.247 оп.1 д.114 (1826–36) — рождение Ивана 1829 (эл. читальный зал, регистрация — пользователь)')])
app('search-log.csv', [dict(search_id='S-0115', timestamp='2026-11-02', target_person_ids='P-0026;P-0028;P-0011;P-0012', research_goal='Соколовы: дворянские списки, метрики Старого, военные', query='Яндекс Архив (сенатские объявления, ЦГА Москвы, ЦГАМО), каталог ГАБО ф.247, goldarms, ВГД, Русский инвалид', language_locale='ru', source_or_domain='ya.ru/archive; el.archive-bryansk.ru; web', result_status='found', artifact_ids='A-0104;A-0105;A-0106;A-0107', blocker='НашиПредки CAPTCHA (стоп); ГАБО эл. зал — регистрация; FS каталог — вход', captcha_attempts='0', next_step='C-0051 probable; ГАБО ф.247 оп.1 д.114; соседние сканы ф.2125 оп.3 д.224; '+SP+'sokolov/r2/report.md')])
print('ok')
