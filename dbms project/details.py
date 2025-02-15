from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox 

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+0+0")

          # =========title===============
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)        
        lbl_title.place(x=0,y=0,width=1295,height=50)

     # ===============logo=================
        
        img2=Image.open(r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images\logohotel.png")
        img2=img2.resize((100,40), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

        # ====================labelFrame==============

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),bg="white",fg="black",padx=2,)
        labelframeleft.place(x=5,y=50,width=540,height=350)

         # ==========labels and entry==================
        # floor
        lbl_floor=Label(labelframeleft,font=("arial",12,"bold"),text="Floor:",padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        self.var_floor=StringVar()

        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("arial",13,"bold"),width=20)
        enty_floor.grid(row=0,column=1,sticky=W)

        ####room number=====================

        lbl_RoomNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Room Number:",padx=2,pady=6)
        lbl_RoomNumber.grid(row=1,column=0,sticky=W,padx=20)

        self.var_roomno=StringVar()

        enty_RoomNumber=ttk.Entry(labelframeleft,textvariable=self.var_roomno,font=("arial",13,"bold"),width=20)
        enty_RoomNumber.grid(row=1,column=1,sticky=W)
        
        #============room Type====================
        lbl_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W,padx=20)

        self.var_RoomType=StringVar()

        enty_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,font=("arial",13,"bold"),width=20)
        enty_RoomType.grid(row=2,column=1,sticky=W)

        # ---------------------btn---------------------------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.Update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=2,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=3,padx=1)

       # ===========table from search system==================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show room details",font=("times new roman",12,"bold"),bg="white",fg="black",padx=2,)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomtype"
                                                                   ),xscrollcommand=scroll_x.set,
                                                                   yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room Number")
        self.room_table.heading("roomtype",text="RoomType")
        
        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
         #add data

    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Keerthi@182!",database="hotelmanagement")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                self.var_floor.get(),
                                                                                self.var_roomno.get(),
                                                                                self.var_RoomType.get(),
                                                                            ))
                conn.commit()
                self.fetch_data()
                
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning","some thing went wrong:{str(es)}",parent=self.root)

                 #=====fetch data==============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Keerthi@182!",database="hotelmanagement")            
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #get_cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_RoomType.set(row[2])
        
        #====update function==============
    def Update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Keerthi@182!",database="hotelmanagement")            
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(                                                                                                                                                         
                                                                                            self.var_floor.get(),
                                                                                            self.var_RoomType.get(),
                                                                                            self.var_roomno.get(),
                                                                                          ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update"," New Room details has been updated successfully",parent=self.root)

            #=============delete========
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","do you want delete Room details",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Keerthi@182!",database="hotelmanagement")            
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.cl.set("")

    def reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_RoomType.set("")

    
        










if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()

