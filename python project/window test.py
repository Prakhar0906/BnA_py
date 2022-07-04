# Python 3
import tkinter
import tkinter.scrolledtext as scrolledtext

root = tkinter.Tk()
# make the top right close button minimize (iconify) the main window
root.protocol("WM_DELETE_WINDOW", root.iconify)
# make Esc exit the program
root.bind('<Escape>', lambda e: root.destroy())

# create a menu bar with an Exit command
menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# create a Text widget with a Scrollbar attached
txt = scrolledtext.ScrolledText(root, undo=True)
txt['font'] = ('consolas', '12')
txt.pack(expand=True, fill='both')

root.mainloop()
