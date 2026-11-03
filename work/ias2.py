import sys,json,urllib.parse,urllib.request,re
item,server,path,q=sys.argv[1:5]; docs=sys.argv[5].split("|"); flt=sys.argv[6] if len(sys.argv)>6 else "."; W=int(sys.argv[7]) if len(sys.argv)>7 else 220
for doc in docs:
  print("####",doc)
  u=f"https://{server}/fulltext/inside.php?item_id={urllib.parse.quote(item)}&doc={urllib.parse.quote(doc)}&path={urllib.parse.quote(path)}&q={urllib.parse.quote(q)}"
  try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=180))
  except Exception as e: print("ERR",e); continue
  for m in d.get("matches",[]):
    t=re.sub(r"\s+"," ",m["text"])
    i=t.find("<IA_FTS_MATCH>"); s=t[max(0,i-W):i+W] if i>=0 else t[:2*W]
    if re.search(flt,s,re.I): print("  leaf",m["par"][0]["page"],"|",s.replace("<IA_FTS_MATCH>","[").replace("</IA_FTS_MATCH>","]"))
