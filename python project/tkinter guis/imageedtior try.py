from tkinter import *
import cv2 
from PIL import ImageTk, Image 
from tkinter import filedialog
import numpy as np

root= Tk()
root.title('Image Viewer')
root.geometry("500x500")

def open_in_cv(path):
    global image_label
    global imgtk
    global img
    img= cv2.imread(path)
    #cv2.imshow('image', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    b,g,r= cv2.split(img)
    img= cv2.merge((r,g,b))
    
    im = Image.fromarray(img)
    imgtk= ImageTk.PhotoImage(image= im)
    image_label= Label(root, image = imgtk).pack()
    resize_button['state']= "active"

def rescaleFrame(frame, scale= 0.75):
    scale= value.get()
    print(scale)
    scale= float(scale)
    print(scale)
    width= int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)
    dimentions= (width, height)

    return cv2.resize(frame, dimentions, interpolation= cv2.INTER_AREA)
    

def open_file():
    global my_image
    global img_path
    img_path= filedialog.askopenfilename(initialdir= "/Saved Pictures", title= "Select A File", filetypes= (("png files", "*.png"),("all files", "*.*")))
    path_label= Label(root, text= img_path).pack()
    #my_image= ImageTk.PhotoImage(Image.open(root.filename))
    #image_label= Label(image= my_image).pack()
    open_in_cv(img_path)

def resize():
    global scale
    global value
    global top
    top= Toplevel()
    text= Label(top, text="Enter rescale value in point")
    text.pack()
    value= Entry(top)
    value.pack()
    ok= Button(top, text="ok", command= lambda: rescaleFrame(img))
    ok.pack()
    
    

welcom= Label(root, text="Select a file to open").pack()
select= Button(root, text="open", command= open_file).pack()

img_display= Frame(root)

leftside= Frame(root, bg='white')
leftside.pack(side= LEFT)

resize_button= Button(root, text="Resize", state= DISABLED, command= resize)
resize_button.pack()

root.mainloop()

