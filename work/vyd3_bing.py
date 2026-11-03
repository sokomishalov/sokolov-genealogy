import re,html,sys,urllib.parse,urllib.request
q=sys.argv[1]
u="https://www.bing.com/search?setlang=ru&cc=RU&q="+urllib.parse.quote(q)
r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36","Accept-Language":"ru-RU,ru;q=0.9"})
t=urllib.request.urlopen(r,timeout=25).read().decode('utf-8','ignore')
for m in re.finditer(r'<li class="b_algo".*?<h2[^>]*><a[^>]*href="([^"]+)"[^>]*>(.*?)</a>.*?(?:<p[^>]*>(.*?)</p>|</li>)',t,re.S):
    print('*',html.unescape(re.sub('<[^>]+>','',m.group(2))),'|',m.group(1)[:180])
    if m.group(3): print('   ',html.unescape(re.sub('<[^>]+>','',m.group(3)))[:300])
