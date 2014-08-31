import wx
import ctypes as ct

class GetPoint(ct.Structure):
    _fields_ = [("x", ct.c_long), ("y", ct.c_long)]

def get_mousepos():
    pt = GetPoint()
    ct.windll.user32.GetCursorPos(ct.byref(pt))
    return int(pt.x), int(pt.y)

wnd = avsp.GetWindow()
script = wnd.currentScript
w, h = script.AVI.Width, script.AVI.Height
dc = wx.ClientDC(wnd.videoWindow)
dc.SetDeviceOrigin(wnd.xo, wnd.yo)
try: # DoPrepareDC causes NameError in wx2.9.1 and fixed in wx2.9.2
    wnd.videoWindow.DoPrepareDC(dc)
except:
    wnd.videoWindow.PrepareDC(dc)
zoomfactor = wnd.zoomfactor
if zoomfactor != 1:
    dc.SetUserScale(zoomfactor, zoomfactor)
xpos,ypos = wnd.videoWindow.ScreenToClient(get_mousepos())
x = dc.DeviceToLogicalX(xpos)
y = dc.DeviceToLogicalY(ypos)

rgb = dc.GetPixel(x, y)
R,G,B = rgb.Get()

#script.SetSelection(self.GetSelectionStart(), self.GetSelectionEnd())
script.ReplaceSelection('$%02x%02x%02x ' % (R,G,B))
