import re,sys,html
for fn in sys.argv[2:]:
  raw=open(fn,'rb').read()
  try: t=raw.decode('utf-8')
  except: t=raw.decode('cp1251',errors='replace')
  title=re.search(r'<title>(.*?)</title>',t,re.S)
  print('==',fn,title.group(1).strip() if title else '')
  t=re.sub(r'<script.*?</script>','',t,flags=re.S); t=re.sub(r'<style.*?</style>','',t,flags=re.S); t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
  for k in sys.argv[1].split('|'):
    for m in re.finditer(k,t,re.I): print(k,'::',t[max(0,m.start()-250):m.start()+350]); print('---')
