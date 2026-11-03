import sys,json,urllib.request,urllib.parse,gzip,re,os
q=sys.argv[1]; pat=sys.argv[2]; ids=set(sys.argv[3].split(',')) if len(sys.argv)>3 and sys.argv[3] else None
out='/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/fa7e9f22-0344-405f-8da9-6094acf0931a/scratchpad/rozina3/ia'
u='https://archive.org/services/search/beta/page_production/?'+urllib.parse.urlencode({'user_query':q,'service_backend':'fts','hits_per_page':50})
d=json.load(urllib.request.urlopen(u,timeout=60))
for h in d['response']['body']['hits']['hits']:
  f=h['fields']; i=f['identifier']
  if ids and i not in ids: continue
  fn=f['filename']; print('##',i,'|',fn,'|',f.get('title'))
  p=os.path.join(out,re.sub(r'[^A-Za-z0-9._-]','_',i+'__'+fn[-60:]))
  if not os.path.exists(p):
    try:
      data=urllib.request.urlopen('https://archive.org/download/'+urllib.parse.quote(i)+'/'+urllib.parse.quote(fn),timeout=120).read()
      open(p,'wb').write(data)
    except Exception as e: print('DLERR',e); continue
  raw=open(p,'rb').read()
  try: raw=gzip.decompress(raw)
  except: pass
  t=raw.decode('utf-8','ignore')
  for m in re.finditer(pat,t):
    print('  >>',t[max(0,m.start()-int(sys.argv[4]) if len(sys.argv)>4 else m.start()-300):m.end()+(int(sys.argv[5]) if len(sys.argv)>5 else 300)].replace('\n',' / '))
