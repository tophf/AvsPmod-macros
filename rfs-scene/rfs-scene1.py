import re
import bisect

keyword = '#1'
coalesce_adjacent = True

curframe = avsp.GetFrameNumber()
bm = sorted(avsp.GetBookmarkList())
i = bisect.bisect_left(bm, curframe)
if i<len(bm) and bm[i]==curframe:
    i+=1
f1 = bm[i-1] if i>0 else 0
f2 = bm[i]-1 if i<len(bm) else avsp.GetVideoFramecount()-1

txt = avsp.GetText()
script = avsp.GetWindow().currentScript
rx = re.compile(r'^(.*?")([0-9\[\]\s].+?)(\s*"\s*\)\s*'+re.escape(keyword)+'.*?)$',re.MULTILINE | re.IGNORECASE)
for mo in reversed(list(rx.finditer(txt))):
    line_start, mappings, line_end = mo.groups()
    _f1, _f2 = f1,f2

    L = [[f for f in r.strip('[ ').split()] for r in mappings.split(']') if len(r)]
    if len(L[0])<2:
        L = []
    L.append([str(_f1),str(_f2)])
    L.sort(key = lambda r: int(r[0]))

    L2 = []
    p = L[0]
    for i,r in enumerate(L[1:]):
        if int(r[0]) <= int(p[1])+1:
            p = [p[0],max(r[1],p[1])]
            if coalesce_adjacent:
                if _f1 >= int(p[0]) and _f2 <= int(p[1]):
                    _f1,_f2 = int(p[0]),int(p[1])
        else:
            L2.append(p)
            p = r
    L2.append(p)
    if coalesce_adjacent:
        if _f1 >= int(p[0]) and _f2 <= int(p[1]):
            _f1,_f2 = int(p[0]),int(p[1])

    script.SetSelection(mo.start(2), mo.end(2))
    s = ' '.join('['+' '.join(r)+']' for r in L2)
    avsp.InsertText(s, None)

    f1_2 = '[%d %d]' % (_f1, _f2)
    i = s.find(f1_2)
    script.SetSelection(mo.start(2)+i, mo.start(2)+i+len(f1_2))
