import re,sys,html,urllib.parse,urllib.request
def get(url): return urllib.request.urlopen(url,timeout=120).read().decode('utf-8','replace')
def items(t):
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    seen=[]
    for m in re.finditer(r'href="\s*(/object/\d+)\?[^"]*"[^>]*>(.*?)</a>',t,flags=re.S):
        txt=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',m.group(2)))).strip()
        if not txt or 'Посмотреть' in txt or any(m.group(1)==s for s,_ in seen): continue
        seen.append((m.group(1),txt))
    return seen,t
# usage: d.py FOND|- TITLE [maxpages] [filterregex]
fond,title=sys.argv[1],sys.argv[2]
maxp=int(sys.argv[3]) if len(sys.argv)>3 else 5
flt=sys.argv[4] if len(sys.argv)>4 else None
p=[('type','custom'),('searchObjectType','DOCUMENTS'),('customSearchUniqueId','')]
spec=[('13348','23',fond if fond!='-' else ''),('2416811','23',''),('13352','23',''),('13354','12',title),('13706','10',''),('13708','10','')]
for i,(a,c,v) in enumerate(spec):
    p+= [('p%d.v'%i,v),('p%d.t'%i,''),('p%d.d'%i,''),('p%d.c'%i,c),('p%d.a'%i,a)]
base='https://catalog.gaorel.ru/search?'+urllib.parse.urlencode(p)+'&pageSize=100'
it,t=items(get(base))
tot=re.findall(r'Найдено[^<]*',t)
pg=[int(x) for x in re.findall(r'page12924=(\d+)',t)]
print('total',tot,'pages',max(pg) if pg else 1)
allit=list(it)
for n in range(2,min(max(pg) if pg else 1,maxp)+1):
    allit+=items(get(base+'&page12924=%d'%n))[0]
for o,x in allit:
    if not flt or re.search(flt,x,re.I): print(o,'|',x[:400])
