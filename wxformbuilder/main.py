import wx
from modul import Frameku

class tampilan(Frameku):
    def __init__(self, parent):
        Frameku.__init__(self, parent)

app = wx.App()
frame = tampilan(parent=None)
frame.Show()
app.MainLoop()