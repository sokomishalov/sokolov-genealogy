import sys,re,html
fn,k,a,b=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
t=open(fn,'rb').read().decode('cp1251','replace')
t=html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>','',t,flags=re.S)));t=re.sub(r'\s+',' ',t)
for m in re.finditer(re.escape(k),t): print(t[max(0,m.start()-a):m.start()+b]); print('=====')
