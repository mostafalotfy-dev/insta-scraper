import wx


class MainFrame(wx.Frame):
    def __init__(self, title: str):
        super().__init__(parent=None, title=title)
        status_bar = self.CreateStatusBar(name="Status bar")
        status_bar.SetStatusText("Hello")
        self.Show()



