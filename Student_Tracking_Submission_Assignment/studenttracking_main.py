from tkinter import *
import tkinter as tk
from tkinter import messagebox

import studenttracking_gui
import studenttracking_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        
        studenttracking.center_window(self,500,300)
        self.master.title("Student Tracking.")
        self.master.configure(bg="#F0F0F0")
        
        self.master.protocol("WM_DELETE_WINDOW", lambda: studenttracking_func.ask_quit(self))
        arg = self.master

        studenttracking_gui.load_gui(self)

        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: studenttracking_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About Student Tracking Demo")
        menubar.add_cascade(label="Help", menu=helpmenu)
        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional
            functionalityor appearances such as a borderwidth.
        """
        self.master.config(menu=menubar, borderwidth='1')

"""
    It is from these few lines of code that Python will begin our gui and application
    The (if __name__ == "__main__":) part is basically telling Python that if this script
    is ran, it should start by running the code below this line....in this case we have
    instructed Python to run the following and in this order:

    root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    #This instantiates our own class as an App object
    root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                #meaning, it will stay open until we instruct it to close
"""

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
