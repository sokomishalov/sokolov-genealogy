import re,sys,html,urllib.parse,urllib.request
def get(url): return urllib.request.urlopen(url,timeout=120).read().decode('utf-8','replace')
for name in sys.argv[1:]:
    p=[('type','custom'),('searchObjectType','STOCKS'),('customSearchUniqueId','')]
    for i,(a,c,v) in enumerate([('13628','23',''),('13692','12',name)]):
        p+=[('p%d.v'%i,v),('p%d.t'%i,''),('p%d.d'%i,''),('p%d.c'%i,c),('p%d.a'%i,a)]
    t=get('https://catalog.gaorel.ru/search?'+urllib.parse.urlencode(p)+'&pageSize=100')
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    print('###',name)
    seen=set()
    for m in re.finditer(r'href="\s*(/object/\d+)\?[^"]*"[^>]*>(.*?)</a>',t,flags=re.S):
        txt=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',m.group(2)))).strip()
        if not txt or 'Посмотреть' in txt or m.group(1) in seen: continue
        seen.add(m.group(1)); print('  ',m.group(1),'|',txt[:200])
