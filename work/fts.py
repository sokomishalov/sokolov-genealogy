import sys,json,urllib.parse,urllib.request,re
for q in sys.argv[1:]:
  print("#####",q)
  u="https://archive.org/services/search/beta/page_production/?"+urllib.parse.urlencode({"user_query":q,"service_backend":"fts","hits_per_page":40,"page_type":"search_results"})
  try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=90))
  except Exception as e: print(e); continue
  r=d["response"]
  if not r["header"]["succeeded"]: print(r.get("errors")); continue
  print("total",r["body"]["hits"]["total"])
  for h in r["body"]["hits"]["hits"]:
    f=h["fields"]; hl=h.get("highlight") or {}
    print("-",f.get("identifier"),f.get("filename"),"|",str(f.get("title"))[:80],"|",f.get("year"),"| p",f.get("page_num"))
    for v in (hl.get("text") or [])[:2]: print("    ",re.sub(r"\s+"," ",v)[:260])
