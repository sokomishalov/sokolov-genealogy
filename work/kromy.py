# -*- coding: utf-8 -*-
import re,sys
for y in sys.argv[1:]:
    L=open('dl-istmat/%s.ocr.txt'%y,encoding='utf-8').read().split('\n')
    page=''
    pages=[]
    for i,l in enumerate(L):
        if l.startswith('### '): page=l[4:]
        pages.append(page)
    print('=====',y)
    for i,l in enumerate(L):
        if re.search(r'Соколов',l) and any(re.search(r'Кром|Апальк|Апальков',L[j]) for j in range(max(0,i-25),min(len(L),i+25))):
            print(pages[i], i, '|', ' / '.join(L[max(0,i-2):i+2]))
        if re.search(r'предвод',l,re.I) and any(re.search(r'Кром',L[j]) for j in range(i-1,i+3)):
            print('  ПРЕДВ', pages[i], i, '|', ' / '.join(L[i-1:i+3]))
