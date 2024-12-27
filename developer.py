from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox,Tk
import pymysql as sqltor
import cv2 


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")


        title_lbl=Label(self.root,text="DEVELOPER " ,font=("times new roman",35,"bold"),bg="white",fg="Hot pink")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"C:\Users\Dell\Downloads\face recognition images\cb.jpg")
        img_top=img_top.resize((1530,725))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=725)
        
        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=100,y=0,width=500,height=600)
        
        img_top1=Image.open(r"C:\Users\Dell\Downloads\face recognition images\Sanidhya.jpg")
        img_top1=img_top1.resize((200,200))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1) 
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #Developer info
        dev_label=Label(main_frame,bd=2,relief=RIDGE,text="Developed by: ",font=("times new roman",12,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=5) 

        dev_label=Label(main_frame,bd=2,relief=RIDGE,text=" SANIDHYA SRIVASTAVA ",font=("times new roman",12,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=30) 
        
        dev_label=Label(main_frame,bd=2,relief=RIDGE,text=" ABHAY PANDEY ",font=("times new roman",12,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=55) 
        
        dev_label=Label(main_frame,bd=2,relief=RIDGE,text=" GAUTAM SHAH ",font=("times new roman",12,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=80) 
        
        dev_label=Label(main_frame,bd=2,relief=RIDGE,text=" SATYAM YADAV ",font=("times new roman",12,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=105) 

        dev_label=Label(main_frame,bd=2,relief=RIDGE,text=" ANKUR GUPTA ",font=("times new roman",12,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=130)
        
        
       
        img2=Image.open(r"C:\Users\Dell\Downloads\face recognition images\Friends.jpg")
        img2=img2.resize((500,390))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=200,width=500,height=390)




if __name__ == "__main__": 
    root=Tk()
    obj=Developer(root)
    root.mainloop()























