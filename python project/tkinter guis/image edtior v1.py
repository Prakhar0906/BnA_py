from tkinter import *
from tkinter import filedialog 
from PIL import ImageTk, Image 
import cv2 
import numpy as np

root= Tk()
root.title('image edtior')

def initiate():
    global img_path
    global display_img
    global img
    global cv_img
    img_path= filedialog.askopenfilename(initialdir= "/Saved Pictures", title= "Select A File", filetypes= (("png files", "*.png"),("all files", "*.*")))
    img = ImageTk.PhotoImage(Image.open(img_path))
    display_img= Label(root, image= img)
    display_img.pack()
    select.forget()
    welcom.forget()
    cv_img= cv2.imread(img_path)
    tools= Frame(root)
    tools.pack(side= LEFT)
    resize_button= Button(tools, text="resize", command= resize )
    resize_button.pack()
    blurr_button= Button(tools, text="Blurr", command= blur_input)
    blurr_button.pack()
    


def show(img):
    global imgtk 
    global display_img
    global cv_img
    display_img.forget() 
    b,g,r= cv2.split(img)
    img= cv2.merge((r,g,b))
    im = Image.fromarray(img)
    imgtk= ImageTk.PhotoImage(image= im)
    display_img= Label(root, image = imgtk)
    display_img.pack()
    cv_img= img

def resize():
    global value 
    top= Toplevel()
    value= Entry(top)
    value.pack()
    ok= Button(top, text="ok", command= lambda: rescaleFrame(cv_img))
    ok.pack()
    
def rescaleFrame(frame, scale= 0.75):
    scale= value.get()
    print(scale)
    scale= float(scale)
    print(scale)
    width= int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)
    dimentions= (width, height)
    img=  cv2.resize(frame, dimentions, interpolation= cv2.INTER_AREA)
    show(img)

def blur_input():
    global value 
    top= Toplevel()
    value= Entry(top)
    value.pack()
    ok= Button(top, text="ok", command= blur)
    ok.pack()

def blur():
    (x,y)= value.get().split(",")
    print(type(x))
    x=int(x)
    y=int(y)
    
    blured_img= cv2.GaussianBlur(cv_img, (x,y), cv2.BORDER_DEFAULT)
    show(blured_img)


welcom= Label(root, text="Welcom")
welcom.pack()

select= Button(root, text="Open file", command= initiate)
select.pack()

root.mainloop()