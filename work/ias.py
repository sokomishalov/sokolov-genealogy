import sys,json,urllib.parse,urllib.request,re
item,server,path,doc,q=sys.argv[1:6]
flt=sys.argv[6] if len(sys.argv)>6 else ""
u=f"https://{server}/fulltext/inside.php?item_id={urllib.parse.quote(item)}&doc={urllib.parse.quote(doc)}&path={urllib.parse.quote(path)}&q={urllib.parse.quote(q)}"
r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=120)
d=json.load(r)
for m in d.get("matches",[]):
  t=m["text"].replace("\n"," ")
  if re.search(flt,t,re.I):
    print("p.",m["par"][0]["page"],"|",t[:700]); print()
