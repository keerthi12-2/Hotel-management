from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install poillow
from tkinter import messagebox
import mysql.connector

class Register:
    def _init_(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #==============variables=========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_passward=StringVar()
        self.var_cpassward=StringVar()
        self.var_security=StringVar()
        self.var_securityans=StringVar()
        


        #====back ground image============
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #=============left image=======
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images\thought-good-morning-messages-LoveSove.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)

        #=============label and entry==========
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        lname.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact no",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        

        security=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        security.place(x=50,y=240)
        self.combo_security=ttk.Combobox(frame,textvariable=self.var_security,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","your birth place","father name","primary school name")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)



        securityans=Label(frame,text="Security Question Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        securityans.place(x=370,y=240)
        self.txt_securityans=ttk.Entry(frame,textvariable=self.var_securityans,font=("times new roman",15))
        self.txt_securityans.place(x=370,y=270,width=250)


        passward=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        passward.place(x=50,y=310)
        self.txt_passward=ttk.Entry(frame,textvariable=self.var_passward,font=("times new roman",15))
        self.txt_passward.place(x=50,y=340,width=250)

        cpassward=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        cpassward.place(x=370,y=310)
        self.txt_cpassward=ttk.Entry(frame,textvariable=self.var_cpassward,font=("times new roman",15))
        self.txt_cpassward.place(x=370,y=340,width=250)

        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0,bg="white")
        self.checkbtn.place(x=50,y=380)

      
        img=Image.open(r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images\register-now-button1.jpg")
        img=img.resize((100,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=470,width=300)

        img1=Image.open(r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images\loginpng.png")
        img1=img1.resize((100,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=330,y=470,width=300)

#===================function declaration==============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security.get()=="Select":
            messagebox.showerror("error","all fields are required")
        elif self.var_passward.get()!=self.var_cpassward.get():
            messagebox.showerror("Error","Passward and confirm passward must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("error","please agree our terms and conditions")
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Keerthi@182!",database="hotelmanagement")
           my_cursor=conn.cursor()
           query=("select * from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if row!=None:
               messagebox.showerror("Error","user already exits,please try another email")
           else:
               my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                      self.var_lname.get(),
                                                                                      self.var_contact.get(),
                                                                                      self.var_email.get(),
                                                                                      self.var_security.get(),
                                                                                      self.var_securityans.get(),
                                                                                      self.var_passward.get()
                                                                                   ))
           conn.commit()
           conn.close() 
           messagebox.showinfo("success","Register Successfully")      
               
               
        













if __name__ == "_main_":
    root=Tk()
    obj=Register(root)
    root.mainloop()