from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root= Tk()
root.title('Image Viewer')

def open_file():
    global my_image
    root.filename= filedialog.askopenfilename(initialdir= "/Saved Pictures", title= "Select a fiel", filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label= Label(root, text=root.filename).pack()
    my_image= ImageTk.PhotoImage(Image.open(root.filename))
    image_label= Label(image= my_image).pack()

button= Button(root, text="open", command= open_file)
button.pack()
root.mainloop()
