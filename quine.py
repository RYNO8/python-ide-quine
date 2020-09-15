from tkinter import *
import sys, traceback

class IDE(Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Quine IDE")
        self.geometry("1000x600+100+100")
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        
        self.createMenu()
        self.createBox()
        self.createShell()
        
    def createMenu(self):
        self.menubar = Menu(self)
        self.menubar.add_command(label="Run", command=self.run)
        self.menubar.add_command(label="Try Sample", command=self.trySample)
        self.config(menu=self.menubar)
    
    def createBox(self):
        self.textBox = Text(self, borderwidth=2, padx=5, pady=5)
        self.textBox.pack(expand=True, fill="both")

    def createShell(self):
        self.shellBox = Text(self, borderwidth=2, padx=5, pady=5)
        self.shellBox.tag_configure("red", foreground="red")
        self.shellBox.tag_configure("blue", foreground="blue")
        self.shellBox.pack(expand=True, fill="both")
    
    def run(self):
        self.shellBox.insert(END, "========== PROGRAM RUNNING ==========\n")
        stdout = sys.stdout.write
        sys.stdout.write = lambda text:self.shellBox.insert(END, text, "blue")
        try:
            exec(self.textBox.get(0.0, END))
        except Exception:
            self.shellBox.insert(END, traceback.format_exc(), "red")
            self.shellBox.insert(END, "========== PROGRAM FINISHED UNSUCCESSFULLY ==========\n\n")
        else:
            self.shellBox.insert(END, "========== PROGRAM FINISHED SUCCESSFULLY ==========\n\n")
            
        sys.stdout.write = stdout
    
    def trySample(self):
        self.textBox.delete(0.0, END)
        text = 'from tkinter import *\nimport sys, traceback\n\nclass IDE(Tk):\n    def __init__(self):\n        super().__init__()\n        self.title("Python Quine IDE")\n        self.geometry("1000x600+100+100")\n        self.protocol("WM_DELETE_WINDOW", self.destroy)\n        \n        self.createMenu()\n        self.createBox()\n        self.createShell()\n        \n    def createMenu(self):\n        self.menubar = Menu(self)\n        self.menubar.add_command(label="Run", command=self.run)\n        self.menubar.add_command(label="Try Sample", command=self.trySample)\n        self.config(menu=self.menubar)\n    \n    def createBox(self):\n        self.textBox = Text(self, borderwidth=2, padx=5, pady=5)\n        self.textBox.pack(expand=True, fill="both")\n\n    def createShell(self):\n        self.shellBox = Text(self, borderwidth=2, padx=5, pady=5)\n        self.shellBox.tag_configure("red", foreground="red")\n        self.shellBox.tag_configure("blue", foreground="blue")\n        self.shellBox.pack(expand=True, fill="both")\n    \n    def run(self):\n        self.shellBox.insert(END, "========== PROGRAM RUNNING ==========\\n")\n        stdout = sys.stdout.write\n        sys.stdout.write = lambda text:self.shellBox.insert(END, text, "blue")\n        try:\n            exec(self.textBox.get(0.0, END))\n        except Exception:\n            self.shellBox.insert(END, traceback.format_exc(), "red")\n            self.shellBox.insert(END, "========== PROGRAM FINISHED UNSUCCESSFULLY ==========\\n\\n")\n        else:\n            self.shellBox.insert(END, "========== PROGRAM FINISHED SUCCESSFULLY ==========\\n\\n")\n            \n        sys.stdout.write = stdout\n    \n    def trySample(self):\n        self.textBox.delete(0.0, END)\n        text = %r\n        self.textBox.insert(0.0, text%%text)\n        \nIDE().mainloop()'
        self.textBox.insert(0.0, text%text)
        
IDE().mainloop()
