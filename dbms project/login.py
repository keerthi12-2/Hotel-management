from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install poillow
from tkinter import messagebox
import mysql.connector
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom
from employee import Employee
#from hotel import HotelManagementSystem

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()




class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images/loginpic.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images/LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbling1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbling1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #----------------icon img--------------
        img2=Image.open(r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images/LoginIconAppl.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbling1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbling1.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images/lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbling1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbling1.place(x=650,y=395,width=25,height=25)

          #loginbtn
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbtn
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),border=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        #forgotbtn
        #forgotbtn=Button(frame,text="Forgot Password",command=self.forget_passward_window,font=("times new roman",10,"bold"),border=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        #forgotbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)



    def login(self):
        if  self.txtuser.get()=="" or self.txtpass.get()=="" :
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="keerthi" or self.txtpass.get()=="keer":
            messagebox.showinfo("success","welcome to hotel")
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Keerthi@182!",database="hotelmanagement")
           my_cursor=conn.cursor()
           my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                               self.txtuser.get(),
                                                                               self.txtpass.get()
                                                                    ))
           row=my_cursor.fetchone()
           if row==None:
               messagebox.showerror("error","invalid username and password")
           else:
               open_main=messagebox.askyesno("YesNo","Access only admin")
               if open_main>0:
                   self.new_window=Toplevel(self.root)
                   self.app=HotelManagementSystem(self.new_window)
               else:
                   if not open_main:
                       return
           conn.commit()
           conn.close()
           #=============reset passward============
    def reset_passward(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error","select the security question")
        elif self.txt_securityans.get=="":
            messagebox.showerror("error","please enter the answer")
        elif self.txt_new_passward.get=="":
            messagebox.showerror("error","please enter the new password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Keerthi@182!",database="hotelmanagement")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and security=%s and securityans=%s")
            value=(self.txtuser.get(),self.combo_security.get(),self.txt_securityans)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("error","please enter the correct answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_passward.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showerror("error","new password has set successfully")
                    
                   

    

           #=============forgot passward=============

    def forget_passward_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Keerthi@182!",database="hotelmanagement")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
           # print(row)
            

            if row==None:
                messagebox.showerror=("error","please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("forgot password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                security=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
                security.place(x=50,y=80)
                self.combo_security=ttk.Combobox(self.root2,textvariable=self.combo_security,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","your birth place","father name","primary school name")
                self.combo_security.place(x=50,y=110,width=250)
                self.combo_security.current(0)



                securityans=Label(self.root2,text="Security Question Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
                securityans.place(x=50,y=150)
                self.txt_securityans=ttk.Entry(self.root2,textvariable= self.var_securityans,font=("times new roman",15))
                self.txt_securityans.place(x=50,y=180,width=250)

                new_passward=Label(self.root2,text="New password",font=("times new roman",15,"bold"),fg="black",bg="white")
                new_passward.place(x=50,y=220)
                self.txt_new_passward=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_new_passward.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),fg="black",bg="white")
                btn.place(x=100,y=300)








class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #==============variables=========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_cpassword=StringVar()
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
        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        self.txt_password.place(x=50,y=340,width=250)

        cpassward=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        cpassward.place(x=370,y=310)
        self.txt_cpassword=ttk.Entry(frame,textvariable=self.var_cpassword,font=("times new roman",15))
        self.txt_cpassword.place(x=370,y=340,width=250)

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
            messagebox.showerror("Error","Password and confirm password must be same")
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
                                                                                      self.var_password.get()
                                                                                   ))
           conn.commit()
           conn.close() 
           messagebox.showinfo("success","Register Successfully")











class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

       # ===================1st img=================
        img1=Image.open(r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images\hotel1.png")
        img1=img1.resize((1550,140), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=140)

        # ===================logo=================
        img2=Image.open(r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images\logohotel.png")
        img2=img2.resize((230,140), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=230,height=140)
        
        # =======================title==============
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)        
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # ==============main frame=================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)


        # ====================menu===============
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)        
        lbl_menu.place(x=0,y=0,width=230)

        # ================btn frame============
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="EMPLOYEE",command=self.emp_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="----",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)


        
        # ===============right side img============
        img3=Image.open(r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images\slide3.jpg")
        img3=img3.resize((1310,590), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling1.place(x=225,y=0,width=1310,height=590)

    # =============down img====================
        
        img4=Image.open(r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images\myh.jpg")
        img4=img4.resize((230,210), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbling1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r"C:\Users\SAIKEERTHIBS\OneDrive\Desktop\dbms project\hotel images\khana.jpg")
        img5=img5.resize((230,190), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lbling1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=420,width=230,height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def emp_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window)


  
        

            

    
        

    


            
        
    

        






        


if __name__ == "__main__":
   main()
        