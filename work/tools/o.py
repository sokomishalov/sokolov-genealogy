import re,sys,html,urllib.request
for o in sys.argv[1:]:
    t=urllib.request.urlopen('https://catalog.gaorel.ru/object/'+o,timeout=90).read().decode('utf-8','replace')
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    i=t.find('<div class="main')
    t=re.sub(r'<a [^>]*href="\s*([^"]*)"[^>]*>',lambda m:' [%s] '%m.group(1).split('?')[0],t)
    s=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',t)))
    j=s.find('Путеводитель') 
    k=s.find('© ГОСУДАРСТВЕННЫЙ')
    s=s[:k]
    # drop header nav
    m=s.find('Поиск по архивному шифру')
    print('#####',o); print(s[-3500:])
