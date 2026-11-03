# -*- coding: utf-8 -*-
import sys
f=sys.argv[1]; t=open(f,encoding='utf-8').read()
def rep(old,new):
    global t
    assert t.count(old)==1, old[:60]
    t=t.replace(old,new)
rep('.treebox { background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; overflow-x: auto; }',
    '.treebox { background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; overflow-x: auto; width: min(1760px, calc(100vw - 32px)); position: relative; left: 50%; transform: translateX(-50%); }')
rep('  .treebox { border: 0; overflow: visible; break-after: page; }',
    '  .treebox { border: 0; overflow: visible; break-after: page; width: auto; left: 0; transform: none; }')
rep('  .treebox svg { min-width: 0; width: auto; max-width: 100%; height: 140mm; margin: 0 auto; }',
    '  .treebox svg { min-width: 0; width: auto; max-width: 100%; height: 150mm; margin: 0 auto; }')
open(f,'w',encoding='utf-8').write(t); print('ok')
