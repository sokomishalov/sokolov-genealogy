import re,html,sys
t=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
ids=re.findall(r'id="(\d{5,})"',t)
t=re.sub(r'<script.*?</script>','',t,flags=re.S)
t=re.sub(r'<[^>]+>',' ',t)
t=re.sub(r'\s+',' ',html.unescape(t))
t=t.replace('0}"--> --> 0}" th:id="${result.id}" src="images/img_preview.png" height="21" width="21" /> -->','\n')
i=t.find('Записи с'); j=t.find('О проекте')
print(t[i:j]); print(ids)
