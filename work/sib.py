# -*- coding: utf-8 -*-
import re,sys
t=open(sys.argv[1],encoding='utf-8').read()
for m in re.finditer(r'<details class="person[^"]*" id="(\w+)">(.*?)</details>', t, re.S):
    pid, body = m.group(1), re.sub(r'<[^>]+>','',m.group(2))
    hits=[]
    for k in re.finditer(r'(Свет|Тан[яи]|сестр|брат|Мари[яи]|Митрофан|Пелаге|Захар|дет(и|ей)|сын|доч)', body):
        hits.append(body[max(0,k.start()-120):k.end()+160].replace('\n',' '))
    if hits:
        print('==',pid); [print('  ·',h) for h in hits[:8]]
