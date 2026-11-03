import re,html,sys
f,pid=sys.argv[1],sys.argv[2]
t=open(f,encoding='utf-8',errors='ignore').read()
t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'\s+',' ',t)
i=t.find('#'+pid+' от')
if i<0: print('NOTFOUND',pid); sys.exit()
j=re.search(r'#\d{3,6} от ',t[i+10:])
body=t[i:i+10+(j.start() if j else 6000)]
# show head + Vydrin contexts
print('HEAD:',body[:700])
for m in re.finditer(r'Выдр\w*',body): print('  >>',body[max(0,m.start()-250):m.end()+150])
