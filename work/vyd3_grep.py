import re,sys
for f in sys.argv[2:]:
    b=open(f,'rb').read()
    for enc in ('utf-8','cp1251'):
        try: t=b.decode(enc); break
        except: continue
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    t=re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',t))
    print('##',f,enc,len(t))
    for m in re.finditer(sys.argv[1],t,re.I):
        print('  ..',t[max(0,m.start()-250):m.end()+250])
