import re,html,sys
pat=sys.argv[1]
for f in sys.argv[2:]:
    t=open(f,encoding='utf-8',errors='ignore').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'\s+',' ',t)
    hits=[m for m in re.finditer(pat,t,flags=re.I)]
    print('##',f,len(hits))
    for m in hits: print('  >>',t[max(0,m.start()-350):m.end()+350])
