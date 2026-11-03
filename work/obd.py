import sys,re,html,urllib.parse,subprocess,time
UA="Mozilla/5.0 (X11; Linux x86_64) Chrome/120"
def get(url):
    for k in range(5):
        t=subprocess.run(["curl","-s","-A",UA,"--max-time","40","-b","/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/fa7e9f22-0344-405f-8da9-6094acf0931a/scratchpad/obdck","-c","/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/fa7e9f22-0344-405f-8da9-6094acf0931a/scratchpad/obdck",url],capture_output=True,text=True).stdout
        if len(t)>20000 or ('info.htm' not in url and 'search-navigation' in t) or ('info.htm' in url and 'Отчество' in t): return t
        time.sleep(2)
    return t
def search(f,n="",s="",y="",p=1,ps=100,extra=""):
    q=urllib.parse.urlencode({"f":f,"n":n,"s":s,"y":y,"r":"","p":p,"ps":ps})+extra
    t=get("https://obd-memorial.ru/html/search.htm?"+q)
    out=[]
    for blk in re.split(r'class="row search-result"',t)[1:]:
        ids=re.findall(r't =(\d+);',blk)+re.findall(r'id_common="(\d+)"',blk)
        txt=html.unescape(re.sub(r'<!--.*?-->','',re.sub(r'<script.*?</script>','',blk,flags=re.S),flags=re.S))
        txt=re.sub(r'<[^>]+>','|',txt); txt=re.sub(r'\s+',' ',txt); txt=re.sub(r'(\|\s*)+','|',txt)
        out.append((ids[0] if ids else '?',txt[:300]))
    return t,out
if __name__=="__main__":
    f=sys.argv[1]; n=sys.argv[2] if len(sys.argv)>2 else ""; s=sys.argv[3] if len(sys.argv)>3 else ""
    flt=sys.argv[4] if len(sys.argv)>4 else ""
    for p in range(1,30):
        t,out=search(f,n,s,p=p)
        if not out: break
        for i,x in out:
            if not flt or re.search(flt,x): print(i,x)
        if len(out)<100: break
        time.sleep(1)

def info(i):
    t=get("https://obd-memorial.ru/html/info.htm?id=%s"%i)
    t=re.sub(r'<script.*?</script>|<style.*?</style>|<!--.*?-->','',t,flags=re.S)
    s=html.unescape(re.sub(r'<[^>]+>','\n',t))
    L=[l.strip() for l in s.split('\n') if l.strip()]
    try:
        a=next(k for k,l in enumerate(L) if l.startswith('Фамилия'))
    except StopIteration:
        a=0
    return L[a:a+60]
