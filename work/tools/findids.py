# -*- coding: utf-8 -*-
import re,sys
t=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
t=t.replace('\\n','\n').replace('\\"','"')
uu=re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
for key in sys.argv[2:]:
    seen={}
    for m in re.finditer(key,t):
        w=t[max(0,m.start()-400):m.end()+400]
        for u in uu.findall(w):
            seen[u]=seen.get(u,0)+1
    print(key, sorted(seen.items(),key=lambda x:-x[1])[:6])
