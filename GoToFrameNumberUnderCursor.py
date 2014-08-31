script = avsp.GetWindow().currentScript
cursorpos = script.GetCurrentPos()
startpos = script.WordStartPosition(cursorpos, True)
endpos = script.WordEndPosition(cursorpos, True)
frametext = script.GetTextRange(startpos, endpos)
avsp.ShowVideoFrame(int(frametext))
