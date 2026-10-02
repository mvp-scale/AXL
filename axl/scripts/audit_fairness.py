#!/usr/bin/env python3
"""Fairness audit: does showing a source's definition make the Northstar demo objectively worse?
Every definition is rendered exactly as the site does (each preview scoped to its own page; dark-mode previews only on their own)
on all 9 demo pages at desktop 1280, tablet 820 and mobile 390, and compared with the untouched page on: horizontal scroll,
content off-screen, overlapping text, clipped text, text under 11px, axe contrast failures (tools/runners/fairness.js).
Writes reports/fairness.md. A preview is AXL's rendering, not the source's code, so any harm here is AXL's to fix."""
import json,re,subprocess,collections,sys
import os,tempfile
SP=tempfile.mkdtemp(); ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
site=open(f'{ROOT}/axl/site/index.html').read()
D=json.loads(re.search(r'const D = (\{.*?\});\n',site,re.S).group(1)); T={t['id']:t for t in D['tweaks']}
KEYF=re.compile(r'@keyframes\s+[\w-]+\s*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}')
def scoped(t):
    css=t.get('css') or ''
    if not t.get('view'): return css
    kf='\n'.join(KEYF.findall(css)); body=re.sub(r'(^|[},])\s*(html|:root)(?=[\s{.:\[,>])',r'\1 &',KEYF.sub('',css))
    return f'{kf}\n:root:has(body[data-view="{t["view"]}"]) {{\n{body}\n}}'
jobs=[]
for e in D['entries']:
    ts=[T[t] for t in e['tweaks'] if t in T]
    ts=[t for t in ts if not t.get('solo')] if len(ts)>1 else ts
    css='\n'.join(scoped(t) for t in ts if t.get('css')); patch=[o for t in ts for o in (t.get('patch') or [])]
    if not css and not patch: continue
    for v in ['overview','projects','editor','settings','reports','assistant','site','docs','signin']: jobs.append({'key':f"{e['word']}|{e['src']}",'view':v,'css':css,'patch':patch})
json.dump(jobs,open(f'{SP}/fair_defs2.json','w'))
out=json.loads(subprocess.run(['node',f'{ROOT}/axl/tools/runners/fairness.js',f'{SP}/fair_defs2.json'],cwd=f'{ROOT}/axl/tools',capture_output=True,text=True).stdout)
json.dump(out,open(f'{SP}/fair_defs2_out.json','w'))
harm=[r for r in out if r['worse']]
print('runs',len(out),'made worse',len(harm),'definitions affected',len({r['key'] for r in harm}))
print(collections.Counter(m for r in harm for m in r['worse']))
L=['# Fairness audit','',f"{len(out)} renders (definitions x 9 demo pages x desktop/tablet/mobile). **{len(harm)} made the page worse** ({len({r['key'] for r in harm})} definitions).",'',
   'A preview is AXL\'s rendering of a rule, not the source\'s own code: any harm listed here is AXL\'s to fix, not the source\'s.','','| Definition | Page | Size | Worse on | Before → after |','|---|---|---|---|---|']
def delta(r): return ', '.join('%s %s→%s' % (k, r['base'][k], r['after'][k]) for k in r['worse'])
for r in harm: L.append('| %s | %s | %s | %s | %s |' % (r['key'].replace('|', ' · '), r['view'], r['device'], ', '.join(r['worse']), delta(r)))
open(f'{ROOT}/axl/reports/fairness.md','w').write('\n'.join(L)+'\n')
for r in harm: print(' ',r['key'],r['view'],r['device'],r['worse'])
