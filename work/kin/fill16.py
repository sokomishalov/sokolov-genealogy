# -*- coding: utf-8 -*-
import csv,os
os.chdir(os.path.expanduser('~/kinship-cases/sokolov'))
row=["S-0046","2026-10-30","P-0018","Robert/Lydia Freuer/Freier в базе BSGR (Cloudflare пройден)","blksea-db search: Freuer/Freier/Freyer/Frayer + Robert; Freier/Freuer + Lydia/Lidia; Fr* + Robert/Rupert","de","blackseagr.org/blksea-db","","not found","","","0","Robert Freuer/Freier в Причерноморье нет (Freier Robert 1928 Neu Danzig, 1930 Житомир — не те). Lydia Freuer: 1897 Peterstal; 26.01.1902 Freudental (отец Wilhelm, мать Magdalene Schneider); 07.02.1913 Freudental (отец Johann ~1881, мать Christina Becker); 1920 (Enzi) — ни одна не дочь Роберта → наша Лидия в базах не записана; вероятно, отчество/фамилия записаны иначе или род. вне Фрейденталя"]
with open('search-log.csv','a',newline='',encoding='utf-8') as f: csv.writer(f).writerow(row)
with open('research-state.md','a',encoding='utf-8') as f: f.write("\n- 30.10 (BSGR, доступ есть): Robert Freuer/Freier нет; Lydia Freuer 1902 (отец Wilhelm), 1913 (отец Johann, мать Christina Becker), 1897 Peterstal, 1920 Enzi — не наши. Возможно, «Робертовна» — русифицированное отчество (Рупрехт/Рейнгольд/Рудольф?) — спросить бабушку, как точно звали отца Лидии.\n")
print('ok')
