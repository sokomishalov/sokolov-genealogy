import re,html,sys,urllib.request,urllib.parse,time,concurrent.futures as cf
D='/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/fa7e9f22-0344-405f-8da9-6094acf0931a/scratchpad/pr/'
def get(u):
  for k in range(3):
    try: return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40).read().decode('utf-8','ignore')
    except Exception as e: time.sleep(2)
  return ''
q=sys.argv[1]; pages=int(sys.argv[2]); out=open(D+sys.argv[3],'w')
def page(p):
  t=get('https://poisk.re/search?'+urllib.parse.urlencode({'query':q,'page':p}))
  return [(m.group(1),html.unescape(m.group(2)),re.sub(r'\s+',' ',html.unescape(m.group(3)))) for m in re.finditer(r'<h4><a href="https://poisk.re/person/([^"]+)">(.*?)</a><small>(.*?)</small>',t,re.S)]
with cf.ThreadPoolExecutor(4) as ex:
  for r in ex.map(page,range(1,pages+1)):
    for x in r: out.write(' | '.join(x)+'\n')
