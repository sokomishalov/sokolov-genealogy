import re,html,sys,subprocess,time
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for i in range(hi,lo-1,-1):
    t=subprocess.run(['curl','-s','-m','20',f'https://el.archive-bryansk.ru/archives/gabo/documents/{i}'],capture_output=True).stdout.decode('utf-8','ignore')
    t=re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>','',t)
    s=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',t)))
    m=re.search(r'Номер фонда: (\d+) Номер описи: (\d+) Номер единицы хранения: (\S+) Заголовок: (.*?) Крайние даты: (\S*) Кол-во листов: (\S*)',s)
    if m: print(i,'|',f'ф.{m[1]} оп.{m[2]} д.{m[3]}','|',m[4][:400],'|',m[5],'|',m[6],flush=True)
    time.sleep(0.25)
