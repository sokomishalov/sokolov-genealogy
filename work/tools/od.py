import re,sys,html,urllib.request
for o in sys.argv[1:]:
    t=urllib.request.urlopen('https://catalog.gaorel.ru/object/'+o,timeout=90).read().decode('utf-8','replace')
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    t=re.sub(r'<a [^>]*href="\s*([^"]*)"[^>]*>',lambda m:' [%s] '%m.group(1).split('?')[0],t)
    s=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',t)))
    s=s[s.find('КОНТАКТЫ')+8:s.find('© ГОСУДАРСТВЕННЫЙ')]
    s=s.replace('[/search] Открыть список в новом окне','')
    print('##',o,s.strip()[:1500]); print()
