import csv

import time

from dotenv import load_dotenv
import wx

from GUI.MainFrame import MainFrame

load_dotenv()  # take environment variables from .env.
start = time.time()
app = wx.App()
MainFrame("Hello world")
app.MainLoop()
print(time.time() - start)
