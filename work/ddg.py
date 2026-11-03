import sys,urllib.parse,urllib.request,re,html
q=sys.argv[1]
req=urllib.request.Request('https://html.duckduckgo.com/html/',data=urllib.parse.urlencode({'q':q}).encode(),headers={'User-Agent':'Mozilla/5.0'})
t=urllib.request.urlopen(req,timeout=30).read().decode('utf-8','ignore')
s=lambda x:re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',x))).strip()
blocks=t.split('class="result__body')[1:]
for b in blocks:
  a=re.search(r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',b,re.S)
  sn=re.search(r'class="result__snippet"[^>]*>(.*?)</(a|div)>',b,re.S)
  if not a: continue
  u=a.group(1); mm=re.search(r'uddg=([^&]+)',u)
  if mm:u=urllib.parse.unquote(mm.group(1))
  print('-',s(a.group(2)),'|',u,'\n   ',s(sn.group(1))[:300] if sn else '')
if not blocks: print('NO RESULTS',len(t))
