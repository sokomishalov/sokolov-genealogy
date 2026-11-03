# -*- coding: utf-8 -*-
import csv,os
os.chdir(os.path.expanduser('~/kinship-cases/sokolov'))
row=["S-0045","2026-10-30","P-0017","Выдрины — многопоколенные линии, казачьи гнёзда у Казахстана","Выдрины + казаки/Сибирское войско/Качиры/Песчаное/Усть-Каменогорск/Уйская станица; Выдрины родословная","ru","forum.vgd.ru; ru.wikipedia; archive74.ru; pomnirod.ru; pavlodarica.fandom.com; olketanu-shko.kz; rodnaya-vyatka.ru","","partial","","Яндекс/DDG — капча (не обходили); chel-portal, culture.ru, totmamuz, pavlodar-eparhia — не открылись","0","связь с нашей семьёй НЕ установлена; гнёзда: Уйская ст. Оренбургского войска (пос. Выдринский); ст. Песчанская под Павлодаром (Выдрин В.С. 1902–1975); Усть-Каменогорск; Вятка (роспись от 1687)"]
with open('search-log.csv','a',newline='',encoding='utf-8') as f: csv.writer(f).writerow(row)
print('ok')
