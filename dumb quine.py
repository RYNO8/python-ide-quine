from tkinter import *
import sys, traceback

class IDE(Tk):
    def __init__(self, state="", w=1000, h=600):
        super().__init__()
        self.title("Python Quine IDE")
        if state == "fullscreen":
            self.attributes("-fullscreen", True)
        elif state == "maximised":
            self.state("zoomed")
        self.geometry(f"{w}x{h}+100+100")
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
        sys.stdout.write = lambda text : self.shellBox.insert(END, text, "blue")
        
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
        #self.textBox.insert(0.0, "Hello world")
        #self.textBox.insert(0.0, "print(\"Hello!\")")
        self.textBox.insert(0.0, open(__file__, "r").read())
        
root = IDE(state="")
root.mainloop()
