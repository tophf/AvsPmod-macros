import wx

fnum=str(avsp.GetFrameNumber())
if wx.TheClipboard.Open():
	data = wx.TextDataObject(fnum)
	wx.TheClipboard.SetData(data)
	wx.TheClipboard.Close()
else:
	avsp.GetTextEntry('frame',fnum,'copy FAILED')