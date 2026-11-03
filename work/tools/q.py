import re,sys,html,urllib.parse,urllib.request
def get(url):
    return urllib.request.urlopen(url,timeout=90).read().decode('utf-8','replace')
def clean(t): return re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
def items(t):
    seen=[]
    for m in re.finditer(r'href="\s*(/object/\d+)\?[^"]*"[^>]*>(.*?)</a>',t,flags=re.S):
        txt=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',m.group(2)))).strip()
        if not txt or 'Посмотреть' in txt or any(m.group(1)==s for s,_ in seen): continue
        seen.append((m.group(1),txt))
    return seen
skip=set(a for a in sys.argv[1:] if a.startswith('-'))
for q in [a for a in sys.argv[1:] if not a.startswith('-')]:
    p={'type':'simple','p0.v':q,'p0.c':'12','p0.a':'19280'}
    base='https://catalog.gaorel.ru/search?'+urllib.parse.urlencode(p)
    t=clean(get(base))
    tabs=re.findall(r'class="search-result-tab ?(active)?\s*">\s*<a class="simpleSearchTab"\s*href="([^"]*)">\s*([^<]+)',t)
    print('###',q,'|',[re.sub(r'\s+',' ',x[2]).strip() for x in tabs])
    for act,href,name in tabs:
        name=re.sub(r'\s+',' ',name).strip()
        if any(s[1:] in name for s in skip): continue
        tt=t if act else clean(get(html.unescape(href)))
        pages=1
        pg=re.findall(r'[?&]page=(\d+)',tt)
        if pg: pages=max(int(x) for x in pg)
        print(' --',name, 'pages',pages)
        allit=items(tt)
        for n in range(2,min(pages,8)+1):
            u=(base if act else html.unescape(href))+'&page=%d'%n
            allit+=items(clean(get(u)))
        for o,txt in allit: print('  ',o,'|',txt[:500])
