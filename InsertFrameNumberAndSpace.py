script = avsp.GetWindow().currentScript
sel1 = script.GetSelectionStart()
prepend = '' if script.GetTextRange(sel1-1,sel1) in '" \t[' else ' '
avsp.InsertText('%s%d' % (prepend, avsp.GetFrameNumber()), None)
