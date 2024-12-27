from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox,Tk
import pymysql as sqltor
import cv2 


class help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")


        title_lbl=Label(self.root,text="HELP DESK" ,font=("times new roman",35,"bold"),bg="white",fg="Dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"C:\Users\Dell\Downloads\face recognition images\Help.jpg")
        img_top=img_top.resize((1530,725))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=725)

        dev_label=Label(f_lbl,bd=2,relief=RIDGE,text="Email:sanidhyasrivastava771@gmail.com",font=("times new roman",36,"bold"),fg="black",bg="white")
        dev_label.place(x=350,y=280)


if __name__ == "__main__": 
    root=Tk()
    obj=help(root)
    root.mainloop()
























