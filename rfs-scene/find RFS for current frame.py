import re

txt = avsp.GetText()
script = avsp.GetWindow().currentScript
curpos = script.GetSelectionStart()
curframe = avsp.GetFrameNumber()

for mo in re.finditer(r'\[\s*(\d+)\s+(\d+)\s*\]', txt[curpos:] + txt):
    f1, f2 = int(mo.group(1)), int(mo.group(2))
    if f1 <= curframe <= f2:
        script.SetSelection((mo.start(1)-1+curpos) % len(txt), (mo.end(2)+1+curpos) % len(txt))
        return