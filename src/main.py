import time
import tkinter as tk
from tkinter import PhotoImage
import sys

if sys.platform == "win32":
    import ctypes
    myappid = "org.gorotopor.pomodoro"
    shell32 = ctypes.windll.shell32 # the following comments are so that pycharm doesn't complain about warning
    # noinspection PyUnresolvedReferences
    shell32.SetCurrentProcessExplicitAppUserModelID.argtypes = [ctypes.c_wchar_p]
    # noinspection PyUnresolvedReferences
    shell32.SetCurrentProcessExplicitAppUserModelID.restype = ctypes.HRESULT
    # noinspection PyUnresolvedReferences
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
# the above allows for a custom taskbar icon, putting it later makes it too slow, windows applies its icon first

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pomodoro Timer")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = screen_width - 540
        y = screen_height - 550
        self.window.geometry(f"500x500+{x}-{y}")
        self.window.resizable(False, False)
        icon = PhotoImage(file="..\images\Tomato250.png")
        self.window.iconbitmap("..\images\Tomato250.ico")
        self.window.iconphoto(True, icon)

app = App()
app.window.mainloop()
