from tkinter import *
from tkinter.filedialog import *

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(1.0, END)

def saveFile():
    global filename
    if filename:
        t = text.get(1.0, END)
        with open(filename, 'w') as f:
            f.write(t)
    else:
        saveAs()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    t = text.get(1.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save file...")

def openFile():
    global filename
    f = askopenfile(mode='r')
    if f is None:
        return
    filename = f.name
    t = f.read()
    text.delete(1.0, END)
    text.insert(1.0, t)

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def increase_font_size(event=None):
    global current_font_size
    current_font_size += 2
    text.config(font=("Helvetica", current_font_size))

def decrease_font_size(event=None):
    global current_font_size
    current_font_size -= 2
    text.config(font=("Helvetica", current_font_size))

current_font_size = 12

root = Tk()
root.title("My Python Text Editor")
root.geometry("800x600")

text = Text(root, wrap=WORD, font=("Helvetica", current_font_size))
text.pack(fill=BOTH, expand=True)

# Create a menu bar
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As..", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
editmenu.add_separator()
editmenu.add_command(label="Increase Font Size", command=increase_font_size)
editmenu.add_command(label="Decrease Font Size", command=decrease_font_size)
menubar.add_cascade(label="Edit", menu=editmenu)

# Bind keyboard events
root.bind("<Control-=>", increase_font_size)
root.bind("<Control-minus>", decrease_font_size)

# Create a status bar
statusbar = Label(root, text="Ready", anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
