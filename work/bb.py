import re,html,sys,urllib.request,urllib.parse,time
q=sys.argv[1]; maxp=int(sys.argv[2]) if len(sys.argv)>2 else 60
pat=re.compile(sys.argv[3] if len(sys.argv)>3 else r'Воронеж|Вихля|Конош|Архангел|Подюг|Новохоп|Борисоглеб|Поворин|Песков|Сев\. ?кра|Северн|Тобольск|Елань')
seen=0
for p in range(1,maxp+1):
  d=urllib.parse.urlencode({'post_name':'search','query':q,'section':'books','page':p}).encode()
  try: t=urllib.request.urlopen(urllib.request.Request('https://bessmertnybarak.com/',data=d,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read().decode('utf-8','ignore')
  except Exception as e: print('ERR',p,e); continue
  if p==1:
    m=re.search(r'Результатов:\s*<span>(\d+)',t); print('total',m and m.group(1))
  arts=re.findall(r'<a href="(/books/person/\d+/)" class="title"[^>]*>(.*?)</a>.*?<div class="desc">(.*?)</div>.*?class="showContentBook">(.*?)</a>',t,re.S)
  if not arts: break
  for u,n,ds,b in arts:
    seen+=1
    ds=html.unescape(re.sub('<[^>]+>','',ds))
    if pat.search(ds) or pat.search(b): print('*',n,'|',ds[:330],'|',b,'| https://bessmertnybarak.com'+u)
print('seen',seen)
