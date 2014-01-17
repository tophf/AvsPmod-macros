import wx
import bisect

curframe = avsp.GetFrameNumber()
bm = sorted(avsp.GetBookmarkList())
i = bisect.bisect_left(bm, curframe)
if i<len(bm) and bm[i]==curframe:
    i+=1
bm1 = bm[i-1] if i>0 else 0
bm2 = bm[i]-1 if i<len(bm) else avsp.GetVideoFramecount()-1

script = avsp.GetWindow().currentScript
sel1 = script.GetSelectionStart()
priortext = '' if script.GetTextRange(sel1-1,sel1) in '" ' else ' '
avsp.InsertText('%s[%s %s]' % (priortext,bm1,bm2), None)
