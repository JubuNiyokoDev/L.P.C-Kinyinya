#coding:utf-8
from tkinter import*
from turtle import back
from PIL import ImageTk , Image
from tkinter import messagebox,ttk
import time
import sqlite3
import random
import os
from email.message import EmailMessage
import ssl 
import smtplib
import re 
import dns.resolver
from  tkcalendar import *






class Loginform:
    def generate_second_otp(self):
            global otp 
            otp = ''.join([str(random.randint(1,10000000)) for i in range(1)])
            self.otp = otp
    def __init__(self,window):
         self.window = window
         self.window.state("zoomed")
         self.window.title("LPC KINYINYA")
         self.window.iconbitmap("iconapp.ico")
         self.window.resizable(False,False)

         

    
            
        
         


        

#background image window =====================================================================================================
         self.bg_frame = Image.open("background1.png")
         photo = ImageTk.PhotoImage(self.bg_frame)
         self.bg_panel = Label(self.window, image=photo)
         self.bg_panel.image = photo
         self.bg_panel.pack(fill="both",expand="yes")


#Widow Frame============================================================================================================
         self.bar = Frame(self.window, bg="#00ffee" ,width="900", height="480")
         self.bar.place(x=70, y=0)
#search bar  window============================================================================================================
         self.bar_entry = Entry(self.bar,highlightthickness=0,relief=FLAT,bg="white",fg="black",
                                     font=("Stylus",11))
         self.bar_entry.insert(0,"Search Event or type URL")
         self.bar_entry.place(x=30,y=5,width=720,height=35)
         self.bar_entry.configure(state=DISABLED)
         def on_click(event):
          self.bar_entry.configure(state=NORMAL)
          self.bar_entry.delete(0,END)
         self.bar_entry.bind("<Button-1>",on_click)


       

#search bar button=======================================================================================================================================================================================================================  
         self.btn_icon_search_bar = Image.open("btn1.png")
         photo_btn_icon_search_bar = ImageTk.PhotoImage(self.btn_icon_search_bar)
         self.btn_search = Label(self.bar, image=photo_btn_icon_search_bar,bg="#040405",width=120,height=31)
         self.btn_search.image = photo_btn_icon_search_bar
         self.btn_search.place(x=720,y=5)




         
       


         self.btn_search_icon = Button(self.btn_search, text="SEARCH",font=("yu gothic ui",13,"bold"),width=12,bd=0,bg="#3047ff"
                                          ,cursor="hand2",activebackground="#3047ff",fg="white",activeforeground="white")                          
         self.btn_search_icon.place(x=0,y=0)

        
        
    

         
             

        


#under bar frame window========================================================================================================================================================================
         self.under_bar_frame = Frame(self.window,bg="#00ffee",width="900",height="60")
         self.under_bar_frame.place(x=70,y=625)
         self.text_label = "Conditions of Use   Privacy Notice  Interest-Based Ads\n© 2022-2022 , jubuniyoko.com , Inc. or its affiliates"
         self.under_bar_frame_label1 = Label(self.under_bar_frame,text=self.text_label,fg="black",bg="#00ffee",font=("Roman", 15,"bold"))
         self.under_bar_frame_label1.place(x=220,y=2)
         


         
#login form window ============================================================================================================
         self.lgn_frame = Frame(self.window, bg="#040405" ,width="900", height="580")
         self.lgn_frame.place(x=70, y=45)

         self.txt = "WELCOME TO JUBU NIYOKO"
         self.heading = Label(self.lgn_frame, text=self.txt, font=("CASTELLAR", 15,"bold"), bg="#040405",fg="#00ffee" )
         self.heading.place(x=300,y=20, height=30)
    
 
#background image left side  ============================================================================================
         self.side_image = Image.open("vector.png")
         photo = ImageTk.PhotoImage(self.side_image)
         self.side_image_label = Label(self.lgn_frame, image=photo,bg="#040405")
         self.side_image_label.image = photo
         self.side_image_label.place(x=0 ,y=65)


#background image sign in  ===============================================================================================
         self.sign_in_image = Image.open("hyy.png")
         photo = ImageTk.PhotoImage(self.sign_in_image)
         self.sign_in_image_label = Label(self.lgn_frame, image=photo,bg="#040405")
         self.sign_in_image_label.image = photo
         self.sign_in_image_label.place(x=570 ,y=100)


         self.sign_in_label = Label(self.lgn_frame,text="Sign In",bg="#040405",fg="white",font=("yu gothic ui",13,"bold"))
         self.sign_in_label.place(x=615,y=215)

#username    ==============================================================================================================
         self.username_label = Label(self.lgn_frame,text="Username",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
         self.username_label.place(x=500,y=230)
         self.username_entry = Entry(self.lgn_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"))
         self.username_entry.place(x=525,y=258,width=275)

         self.username_line = Canvas(self.lgn_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
         self.username_line.place(x=500,y=280)
#Placeholder of UserName=======================================================================================================================================================================================================================

         self.username_entry.insert(0,"Jubu Niyoko")
         self.username_entry.configure(state=DISABLED)
         def click2(event):
          self.username_entry.configure(state=NORMAL)
          self.username_entry.delete(0,END)
         self.username_entry.bind("<Button-1>",click2)
        


#username icon =============================================================================================================
         self.username_icon = Image.open("username_icon.png")
         photo = ImageTk.PhotoImage(self.username_icon)
         self.username_icon_label = Label(self.lgn_frame, image=photo,bg="#040405")
         self.username_icon_label.image = photo
         self.username_icon_label.place(x=495 ,y=253)



#Password    ==============================================================================================================
         self.password_label = Label(self.lgn_frame,text="Password",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
         self.password_label.place(x=500,y=300)
         self.password_entry = Entry(self.lgn_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"),show="*")
         self.password_entry.place(x=521,y=338,width=280)

         self.password_line = Canvas(self.lgn_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
         self.password_line.place(x=500,y=360)

#Placeholder of Password=======================================================================================================================================================================================================================
         self.password_entry.insert(0,"Bujumbura257")
         self.password_entry.configure(state=DISABLED)
         def click3(event):
          self.password_entry.configure(state=NORMAL)
          self.password_entry.delete(0,END)
         self.password_entry.bind("<Button-1>",click3)


        

#agree condition and terms====================================================================================================
         radio = IntVar()
         self.radio = Checkbutton(self.lgn_frame ,text="",variable=radio,bg="#040405",fg="#000000",cursor="hand2",onvalue=1,offvalue=0)
         self.radio_value_label = Label(self.lgn_frame,text="By Continuing , You Agree To Jubu's\nConditons Of Use And Privacy Notice."
                                                   ,bg="#040405",fg="#00ffee")
         self.radio.place(x=530,y=380)
         self.radio_value_label.place(x=553,y=373)
#Password icon =============================================================================================================
         self.password_icon = Image.open("password_icon.png")
         photo = ImageTk.PhotoImage(self.password_icon)
         self.password_icon_label = Label(self.lgn_frame, image=photo,bg="#040405")
         self.password_icon_label.image = photo
         self.password_icon_label.place(x=495 ,y=333)
  



#window from butoon login========================================================================================================================
         def openLogin():
            self.open_login = Toplevel(self.window)
            self.open_login.title("Jubu Niyoko.apk")
            self.open_login.state("zoomed")
            self.open_login.resizable(False,False)

         def clock1():
            self.date=time.strftime("%d/%m/%Y")
            self.currenttime=time.strftime("%H:%M:%S")
            self.datetimeLabel.config(text=f"   Date:{self.date}\nTime:{self.currenttime}")
            self.datetimeLabel.after(1000,clock1)


         self.datetimeLabel = Label(self.lgn_frame,font=("time new roman",18,"bold"),bg="#040405",fg="white")
         self.datetimeLabel.place(x=0,y=0)
         clock1()
       


           




#Login In button ============================================================================================================
         def BOOM():
            if radio.get()!=1:
                messagebox.showerror("ERROR","Please Agree Our Conditions !")
            else:
                
                if self.username_entry.get()=='' or self.password_entry.get()=='':
                    messagebox.showerror('error','Please fill all field')
                    
                
                elif self.username_entry.get()=='LPC' and self.password_entry.get()=='':
                    if self.username_entry.get()=='LPC':
                        messagebox.showerror('error','please admin input your password')
                    
               
                elif self.username_entry.get()=='LPC' and self.    password_entry.get()!='1234':
                    messagebox.showerror('error','admin incorrect password')
                    
                
                
                elif  self.username_entry.get()!='' and self.password_entry.get()!='':
                   if self.username_entry.get()=='LPC' and self.password_entry.get()=='1234':
                       messagebox.showinfo('success','welcome admin')
                       self.window.destroy()
                       import admin
                       
                   else :
                        connection = sqlite3.connect("school.db")
                        mycursor = connection.cursor()
                        check_user = 'SELECT * FROM userinfos WHERE Name = ?'
                        mycursor.execute(check_user,[(self.username_entry.get())])
                        
                        result = mycursor.fetchone()
                        if result:
                            check_user = 'SELECT * FROM userinfos WHERE Name = ? AND Password = ?'
                            mycursor.execute(check_user,(self.username_entry.get(),self.password_entry.get()))
                            result = mycursor.fetchall()
                            if result:
                                messagebox.showinfo("Success","Login Successfully")
                                self.window.destroy()
                                import client
                            else :
                                messagebox.showerror('ERROR','Invalid Password')    
                        else :
                            messagebox.showerror('ERROR','UserName Not Exists')
                else : 
                    messagebox.showerror('ERROR','Something went wrong !')
                       
                   
                   
            
            
               
               
               
               
               
               
               
               
               
               
          
                       
           

                       





            
         self.lgn_btn = Image.open("btn1.png")
         photo = ImageTk.PhotoImage(self.lgn_btn)
         self.lgn_btn_label = Label(self.lgn_frame, image=photo,bg="#040405")
         self.lgn_btn_label.image = photo
         self.lgn_btn_label.place(x=495 ,y=410)


         self.Login = Button(self.lgn_btn_label, text="LOGIN",font=("yu gothic ui",13,"bold"),width=25,bd=0,bg="#3047ff"
                                            ,cursor="hand2",activebackground="#3047ff",fg="white",command=BOOM,activeforeground="white")
         self.Login.place(x=20,y=10)


#window from forget password========================================================================================================================
#========================================================================================================================
#========================================================================================================================
         def openForgetPassword():
            self.open_forget_password = Toplevel(self.window)
            self.open_forget_password.title("Jubu Niyoko.apk")
            self.open_forget_password.state("zoomed")
            self.open_forget_password.iconbitmap("iconapp.ico")

            def check_email_and_send_otp():
                self.generate_second_otp()
                if self.find_user_entry.get()=='' :
                    messagebox.showerror('ERROR','Please enter your email',parent=self.open_forget_password)
                else :
                  try :
                    connection = sqlite3.connect("school.db")
                    mycursor = connection.cursor()
                    query='SELECT * FROM userinfos WHERE Mobile_Or_Email = ?'
                    mycursor.execute(query,[(self.find_user_entry.get())])
                    if not mycursor.fetchone():
                        messagebox.showerror('ERROR','Email Not Exists',parent=self.open_forget_password)
                    else:
                        email_sender = 'niyondikojoffreasjubu@gmail.com'
                        email_password = 'jxequhctgzjuzxlp'
                        email_receiver = self.find_user_entry.get()
                   
                        subject = "Turye Twese"
                        body = 'Hello Your OTP is :' + self.otp + '.' 
                        em = EmailMessage()
                        em['From'] = 'Turye Twese'
                        em['To'] = email_receiver
                        em['Subject'] = subject
                   
                        em.set_content(body)
                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
                            smtp.login(email_sender,email_password)
                            smtp.sendmail(email_sender,email_receiver,em.as_string())
                        messagebox.showinfo('SUCCESS','OTP Sended',parent=self.open_forget_password)
                  except :
                    messagebox.showerror('ERROR','Send OTP feiled',parent=self.open_forget_password)
                


            def recover_password():
                if self.forget_password_entry1.get()=='' or self.forget_password_entry2.get()=='':
                    messagebox.showerror('ERROR','Fill All Place',parent=self.open_forget_password)
                else :
                        if  self.forget_password_entry1.get()!= self.forget_password_entry2.get():
                             messagebox.showerror('ERROR','Password Not Match',parent=self.open_forget_password)
                        else :
                            if self.otp_entry.get() == '':
                                messagebox.showerror('ERROR','Please enter your OTP',parent=self.open_forget_password)
                            else :
                                if self.otp_entry.get() != otp :
                                   messagebox.showerror('ERROR','Incorrect OTP',parent=self.open_forget_password) 
                                else : 
                                   try :
                                      query='UPDATE userinfos SET Password = ? WHERE Name = ? '
                                      mycursor.execute(query,(self.forget_password_entry1.get(),self.find_user_entry.get()))
                                      connection.commit()
                                      connection.close()
                                      messagebox.showinfo('Success','Password Recovered Successfully',parent=self.open_forget_password)
                                      self.open_forget_password.destroy()
                                   except :
                                      messagebox.showerror('ERROR','Something went wrong !',parent=self.open_forget_password) 

                            
                            
                        
                    


               

           


                                    
    




         
                


            def exit_forget_window():
                    self.open_forget_password.destroy()

         



#background image window from forget password=====================================================================================================
#========================================================================================================================
#======================================================================================================================== 
            self.bg_frame = Image.open("background1.png")
            photo = ImageTk.PhotoImage(self.bg_frame)
            self.bg_panel = Label(self.open_forget_password, image=photo)
            self.bg_panel.image = photo
            self.bg_panel.pack(fill="both",expand="yes")


#Frame from forget password=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
#========================================================================================================================

            self.forget_password_frame = Frame(self.open_forget_password,width="900",height="580",bg="#040405")
            self.forget_password_frame.place(x=70,y=45)
            self.txt = "WELCOME TO JUBU NIYOKO"
            self.heading = Label(self.forget_password_frame, text=self.txt, font=("CASTELLAR", 15,"bold"), bg="#040405",fg="#00FFEE" )
            self.heading.place(x=30,y=20, height=30)


#background image left side in forget password form  ============================================================================================
#=========================================================================================================================
#======================================================================================================================================
            self.side_image = Image.open("vector.png")
            photo = ImageTk.PhotoImage(self.side_image)
            self.side_image_label = Label(self.forget_password_frame, image=photo,bg="#040405",width="400")
            self.side_image_label.image = photo
            self.side_image_label.place(x=0 ,y=65)



#background image sign  in forget password form ===============================================================================================
#======================================================================================================================================
#======================================================================================================================================  
            self.sign_in_image = Image.open("hyy.png")
            photo = ImageTk.PhotoImage(self.sign_in_image)
            self.sign_in_image_label = Label(self.forget_password_frame, image=photo,bg="#040405")
            self.sign_in_image_label.image = photo
            self.sign_in_image_label.place(x=570 ,y=20)


            self.sign_in_label = Label(self.forget_password_frame,text="Recover Password",bg="#040405",fg="white",font=("yu gothic ui",13,"bold"))
            self.sign_in_label.place(x=570,y=130)


#search bar in forget password form  ============================================================================================================
#==================================================================================================================================
#==================================================================================================================================
            self.bar_forget_password = Frame(self.open_forget_password, bg="#00ffee" ,width="900", height="48")
            self.bar_forget_password.place(x=70, y=0)

            self.bar_entry_forget_password = Entry(self.bar_forget_password,highlightthickness=0,relief=FLAT,bg="white",fg="blue",
                                     font=("Stylus",11))


#Placeholder of search bar=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================    
#==================================================================================================================================
            self.bar_entry_forget_password.insert(0,"Search Event or type URL")
            self.bar_entry_forget_password.place(x=30,y=5,width=720,height=35)
            self.bar_entry_forget_password.configure(state=DISABLED)
            def click8(event):
             self.bar_entry_forget_password.configure(state=NORMAL)
             self.bar_entry_forget_password.delete(0,END)
            self.bar_entry_forget_password.bind("<Button-1>",click8)


#Search bar Button in forget password =======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.btn_icon_search_bar_open_forget_password = Image.open("btn1.png")
            photo_btn_icon_search_bar_open_forget_password = ImageTk.PhotoImage(self.btn_icon_search_bar_open_forget_password)
            self.btn_search_open_forget_password = Label(self.bar_forget_password, image=photo_btn_icon_search_bar_open_forget_password,bg="#040405",width=120,height=31)
            self.btn_search_open_forget_password.image = photo_btn_icon_search_bar_open_forget_password
            self.btn_search_open_forget_password.place(x=720,y=5)


            self.btn_search_icon = Button(self.btn_search_open_forget_password, text="SEARCH",font=("yu gothic ui",13,"bold"),width=12,bd=0,bg="#3047ff"
                                            ,cursor="hand2",activebackground="#3047ff",fg="white",activeforeground="white")
            self.btn_search_icon.place(x=0,y=0)

            def my_menu():
               pass




#bar menu in forget password form  ============================================================================================================
 #=====================================================================================================================================
#=====================================================================================================================================
            self.menu = Menu(self.open_forget_password)
            self.menu_menu = Menu(self.menu,bg="#00F8EE",fg="black")
         
            self.menu_menu1 = Menu(self.menu_menu,bg="yellow",fg="black")
            self.menu_menu1.add_command(label="Setting Theme Color")
            self.menu_menu1.add_command(label="Setting Language")
            self.menu_menu1.add_command(label="Setting cookies")
            self.menu_menu1.add_command(label="Setting Save Infos")
            self.menu_menu1.add_command(label="Setting Voice")

            self.menu_menu2 = Menu(self.menu_menu,bg="blue",fg="white")
            self.menu_menu2.add_command(label="News Products")
            self.menu_menu2.add_command(label="News Cost")
            self.menu_menu2.add_command(label="News Members")
            self.menu_menu2.add_command(label="News Bonus")
            self.menu_menu2.add_command(label="News Infos")


            self.menu_menu3 = Menu(self.menu_menu,bg="red",fg="white")
            self.menu_menu3.add_command(label="Exit Here",command=back)
            self.menu_menu3.add_command(label="Exit Page",command=exit_forget_window)


            self.menu_menu5 = Menu(self.menu_menu,bg="blue",fg="white")

            self.menu_menu5.add_command(label="Reflesh Page")
            self.menu_menu5.add_command(label="Reflesh Info")
            self.menu_menu5.add_command(label="Reflesh All")



            self.menu_menu4 = Menu(self.menu_menu,bg="yellow",fg="black")
    

            self.menu_menu4.add_command(label="How we can help You ?")
            self.menu_menu4.add_command(label="Contact Us")
            self.menu_menu4.add_command(label="Leave The Comment")

            self.menu.add_cascade(label="MENU",menu=self.menu_menu)
            self.menu_menu.add_cascade(label="NEWS",menu=self.menu_menu2)
            self.menu_menu.add_cascade(label="REFLESH",menu=self.menu_menu5)
            self.menu_menu.add_cascade(label="SETTINGS",menu=self.menu_menu1)
            self.menu_menu.add_cascade(label="HELP",menu=self.menu_menu4)
            self.menu_menu.add_cascade(label="EXIT",menu=self.menu_menu3)
            self.open_forget_password.config(menu=self.menu)

#under bar fram in sgn up forme========================================================================================================================================================================
#====================================================================================================================================================
#====================================================================================================================================================
            self.under_bar_frame = Frame(self.open_forget_password,bg="#00ffee",width="900",height="60")
            self.under_bar_frame.place(x=70,y=625)
            self.text_label = "Conditions of Use   Privacy Notice   Interest-Based  Ads\n© 2022-2022 , jubuniyoko.com , Inc. or its affiliates"
            self.under_bar_frame_label1 = Label(self.under_bar_frame,text=self.text_label,fg="black",bg="#00ffee",font=("Roman", 15,"bold"))
            self.under_bar_frame_label1.place(x=220,y=2)


#Find your adress in forget password form=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.find_user_label = Label(self.forget_password_frame,text="Enter Your Adress Or Your Number",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.find_user_label.place(x=500,y=165)
            self.find_user_label = Label(self.forget_password_frame,text="Waitting...............Sending............OTP",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.find_user_label.place(x=500,y=260)
            self.find_user_entry = Entry(self.forget_password_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"))
            self.find_user_entry.place(x=500,y=190,width=300)

            self.find_user_line = Canvas(self.forget_password_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
            self.find_user_line.place(x=500,y=213)

            self.btn_recover_password_check_otp = Image.open("btn1.png")
            photo_btn_recover_password_check_otp = ImageTk.PhotoImage(self.btn_recover_password_check_otp)
            self.btn_recover_labe = Label(self.forget_password_frame, image=photo_btn_recover_password_check_otp,bg="#040405",width=50,height=30)
            self.btn_recover_labe.image = photo_btn_recover_password_check_otp
            self.btn_recover_labe.place(x=620,y=220)


            self.btn__recover_icon = Button(self.btn_recover_labe, text="Send",font=("yu gothic ui",13,"bold"),bd=0,bg="#3047ff"
                                            ,cursor="hand2",activebackground="#3047ff",fg="white",activeforeground="white",command=check_email_and_send_otp)
            self.btn__recover_icon.place(x=0,y=0)


            self.find_user_label1 = Label(self.forget_password_frame,text="We Sent OTP In X ,Go Check Your X",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.find_user_label1.place(x=500,y=325)

            self.otp_entry = Entry(self.forget_password_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"))
            self.otp_entry.place(x=500,y=355,width=300)

            self.otp_line = Canvas(self.forget_password_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
            self.otp_line.place(x=500,y=355)

#Placeholder of otp entry =======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================    
#==================================================================================================================================
            self.otp_entry.insert(0,"Enter OTP You Have Received")
            self.otp_entry.configure(state=DISABLED)
            def click10(event):
             self.otp_entry.configure(state=NORMAL)
             self.otp_entry.delete(0,END)
            self.otp_entry.bind("<Button-1>",click10)


#Placeholder of find user entry=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================    
#==================================================================================================================================
      
            self.find_user_entry.insert(0,"niyondikojoffreasjubu@gmail.com")
            self.find_user_entry.configure(state=DISABLED)
            def click9(event):
             self.find_user_entry.configure(state=NORMAL)
             self.find_user_entry.delete(0,END)
            self.find_user_entry.bind("<Button-1>",click9)


#Forget Password1 in sgn form=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
#============================================================================================================================================
            self.forget_password_label1 = Label(self.forget_password_frame,text="Create Password",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.forget_password_label1.place(x=500,y=385)
            self.forget_password_entry1 = Entry(self.forget_password_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"),show="*")
            self.forget_password_entry1.place(x=500,y=415,width=300)

            self.forget_password_line1 = Canvas(self.forget_password_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
            self.forget_password_line1.place(x=500,y=437)

#Placeholder of forget Password1=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
#============================================================================================================================================
            self.forget_password_entry1.insert(0,"Bujumbura+257")
            self.forget_password_entry1.configure(state=DISABLED)
            def click11(event):
             self.forget_password_entry1.configure(state=NORMAL)
             self.forget_password_entry1.delete(0,END)
            self.forget_password_entry1.bind("<Button-1>",click11)   


#Forget Password2 of sgn Up form=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
#============================================================================================================================================
            self.forget_password_label2 = Label(self.forget_password_frame,text="Confirm Password",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.forget_password_label2.place(x=500,y=445)
            self.forget_password_entry2 = Entry(self.forget_password_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"),show="*")
            self.forget_password_entry2.place(x=500,y=475,width=300)

            self.forget_password_line2 = Canvas(self.forget_password_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
            self.forget_password_line2.place(x=500,y=497)
#Placeholder forget Password2=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
#============================================================================================================================================
            self.forget_password_entry2.insert(0,"Bujumbura+257")
            self.forget_password_entry2.configure(state=DISABLED)
            def click12(event):
             self.forget_password_entry2.configure(state=NORMAL)
             self.forget_password_entry2.delete(0,END)
            self.forget_password_entry2.bind("<Button-1>",click12)  

#show or hide password1/password2 IN SGN UP FORM=========================================================================================================
#============================================================================================================================================
#============================================================================================================================================
            self.show_image15 = Image.open("show.png")
            self.photo16 = ImageTk.PhotoImage(self.show_image15)
            self.show_btn15 = Button(self.forget_password_frame, image=self.photo16,bg="white",background="white",cursor="hand2",bd=0,command=self.show15)
            self.show_btn15.image = self.photo16
            self.show_btn15.place(x=780,y=478)

 
            self.hide_image15 = Image.open("hide.png")
            self.photo15 = ImageTk.PhotoImage(self.hide_image15)




            self.show_image20 = Image.open("show.png")
            self.photo21 = ImageTk.PhotoImage(self.show_image20)
            self.show_btn20 = Button(self.forget_password_frame, image=self.photo21,bg="white",background="white",cursor="hand2",bd=0,command=self.show20)
            self.show_btn20.image = self.photo21
            self.show_btn20.place(x=780,y=417)

 
            self.hide_image20 = Image.open("hide.png")
            self.photo20 = ImageTk.PhotoImage(self.hide_image20)


#Didin't get OTP============================================================================================================
# ============================================================================================================
#============================================================================================================

            self.dint_get_otp = Button(self.forget_password_frame,text="Didin't Get It",
                                     font=("yu gothic ui",13,"bold underline"),fg="#D50F0F",width=25,bd=0,bg="#040405",
                                          activebackground="#040405",cursor="hand2",activeforeground="#D50F0F")
            self.dint_get_otp.place(x=520,y=285)

#Search bar Button =======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.btn_recover_password = Image.open("btn1.png")
            photo_btn_recover_password = ImageTk.PhotoImage(self.btn_recover_password)
            self.btn_recover_labe = Label(self.forget_password_frame, image=photo_btn_recover_password,bg="#040405",width=120,height=31)
            self.btn_recover_labe.image = photo_btn_recover_password
            self.btn_recover_labe.place(x=590,y=520)


            self.btn__recover_icon = Button(self.btn_recover_labe, text="RECOVER",font=("yu gothic ui",13,"bold"),width=12,bd=0,bg="#3047ff"
                                            ,cursor="hand2",activebackground="#3047ff",fg="white",activeforeground="white",command=recover_password)
            self.btn__recover_icon.place(x=0,y=0)






#forgot password ============================================================================================================
         self.forgot_button = Button(self.lgn_frame,text="Forgot Password ?",
                                     font=("yu gothic ui",13,"bold underline"),fg="#D50F0F",width=25,bd=0,bg="#040405",
                                          activebackground="#040405",cursor="hand2",command=openForgetPassword,activeforeground="#D50F0F")
         self.forgot_button.place(x=520,y=470)
                                                              

#WINDOW FOR SIGN UP OPEN========================================================================================================================
#=================================================================================================================================== 
         def openSign_up():
            self.open_sgn = Toplevel(self.window)
            self.open_sgn.title("Jubu Niyoko.apk")
            self.open_sgn.state("zoomed")
            self.open_sgn.iconbitmap("iconapp.ico")
            self.open_sgn.resizable(False,False)


            def exit_sign_up():
                    self.open_sgn.destroy()
                 

        

#background image in sgn up form =====================================================================================================
#=================================================================================================================================================
            self.bg_frame = Image.open("background1.png")
            photo = ImageTk.PhotoImage(self.bg_frame)
            self.bg_panel = Label(self.open_sgn, image=photo)
            self.bg_panel.image = photo
            self.bg_panel.pack(fill="both",expand="yes")

#search bar in sgn up form  ============================================================================================================
#==================================================================================================================================
            self.bar_sgn_up = Frame(self.open_sgn, bg="#00ffee" ,width="900", height="48")
            self.bar_sgn_up.place(x=70, y=0)

            self.bar_entry_sgn_up = Entry(self.bar_sgn_up,highlightthickness=0,relief=FLAT,bg="white",fg="blue",
                                     font=("Stylus",11))
#Placeholder of search bar=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================    
            self.bar_entry_sgn_up.insert(0,"Search Event or type URL")
            self.bar_entry_sgn_up.place(x=30,y=5,width=720,height=35)
            self.bar_entry_sgn_up.configure(state=DISABLED)
            def click1(event):
             self.bar_entry_sgn_up.configure(state=NORMAL)
             self.bar_entry_sgn_up.delete(0,END)
            self.bar_entry_sgn_up.bind("<Button-1>",click1)

#Search bar Button =======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.btn_icon_search_bar_open_sgn_up = Image.open("btn1.png")
            photo_btn_icon_search_bar_open_sgn_up = ImageTk.PhotoImage(self.btn_icon_search_bar_open_sgn_up)
            self.btn_search_open_sgn_up = Label(self.bar_sgn_up, image=photo_btn_icon_search_bar_open_sgn_up,bg="#040405",width=120,height=31)
            self.btn_search_open_sgn_up.image = photo_btn_icon_search_bar_open_sgn_up
            self.btn_search_open_sgn_up.place(x=720,y=5)


            self.btn_search_icon = Button(self.btn_search_open_sgn_up, text="SEARCH",font=("yu gothic ui",13,"bold"),width=12,bd=0,bg="#3047ff"
                                            ,cursor="hand2",activebackground="#3047ff",fg="white",activeforeground="white")
            self.btn_search_icon.place(x=0,y=0)





        


#under bar fram in sgn up forme========================================================================================================================================================================
#====================================================================================================================================================
            self.under_bar_frame = Frame(self.open_sgn,bg="#00ffee",width="900",height="60")
            self.under_bar_frame.place(x=70,y=625)
            self.text_label = "Conditions of Use   Privacy Notice   Interest-Based  Ads\n© 2022-2022 , jubuniyoko.com , Inc. or its affiliates"
            self.under_bar_frame_label1 = Label(self.under_bar_frame,text=self.text_label,fg="black",bg="#00ffee",font=("Roman", 15,"bold"))
            self.under_bar_frame_label1.place(x=220,y=2)



            def my_menu():
               pass




#bar menu in sgn up form  ============================================================================================================
 #=====================================================================================================================================
            self.menu = Menu(self.open_sgn)
            self.menu_menu = Menu(self.menu,bg="#00F8EE",fg="black")
         
            self.menu_menu1 = Menu(self.menu_menu,bg="yellow",fg="black")
            self.menu_menu1.add_command(label="Setting Theme Color")
            self.menu_menu1.add_command(label="Setting Language")
            self.menu_menu1.add_command(label="Setting cookies")
            self.menu_menu1.add_command(label="Setting Save Infos")
            self.menu_menu1.add_command(label="Setting Voice")

            self.menu_menu2 = Menu(self.menu_menu,bg="blue",fg="white")
            self.menu_menu2.add_command(label="News Products")
            self.menu_menu2.add_command(label="News Cost")
            self.menu_menu2.add_command(label="News Members")
            self.menu_menu2.add_command(label="News Bonus")
            self.menu_menu2.add_command(label="News Infos")


            self.menu_menu3 = Menu(self.menu_menu,bg="red",fg="white")
            self.menu_menu3.add_command(label="Exit Here",command=back)
            self.menu_menu3.add_command(label="Exit Page",command=exit_sign_up)


            self.menu_menu5 = Menu(self.menu_menu,bg="blue",fg="white")

            self.menu_menu5.add_command(label="Reflesh Page")
            self.menu_menu5.add_command(label="Reflesh Info")
            self.menu_menu5.add_command(label="Reflesh All")



            self.menu_menu4 = Menu(self.menu_menu,bg="yellow",fg="black")
    

            self.menu_menu4.add_command(label="How we can help You ?")
            self.menu_menu4.add_command(label="Contact Us")
            self.menu_menu4.add_command(label="Leave The Comment")

            self.menu.add_cascade(label="MENU",menu=self.menu_menu)
            self.menu_menu.add_cascade(label="NEWS",menu=self.menu_menu2)
            self.menu_menu.add_cascade(label="REFLESH",menu=self.menu_menu5)
            self.menu_menu.add_cascade(label="SETTINGS",menu=self.menu_menu1)
            self.menu_menu.add_cascade(label="HELP",menu=self.menu_menu4)
            self.menu_menu.add_cascade(label="EXIT",menu=self.menu_menu3)
            self.open_sgn.config(menu=self.menu)

         

#Frame from Sgn Up=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.sgn_up_frame = Frame(self.open_sgn,width="900",height="580",bg="#040405")
            self.sgn_up_frame.place(x=70,y=45)
            self.txt = "WELCOME TO JUBU NIYOKO"
            self.heading = Label(self.sgn_up_frame, text=self.txt, font=("CASTELLAR", 15,"bold"), bg="#040405",fg="#00FFEE" )
            self.heading.place(x=30,y=20, height=30)



    

#select age/country/sexe in sgn up form====================================================================================================
#===================================================================================================================================
            self.enter_sexe_label = Label(self.sgn_up_frame,text="Enter Your Sexe :",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.enter_sexe_label.place(x=500,y=360)


            self.enter_sexe_entry = ttk.Combobox(self.sgn_up_frame,font=("Stylus",12,"bold"),state="readonly")
            self.enter_sexe_entry["values"]=("Male","Femmel",'Not Personalyse')
            self.enter_sexe_entry.current(0)
            self.enter_sexe_entry.place(x=650,y=360)
        
            
         
            





#background image left side in sgn up form  ============================================================================================
#=========================================================================================================================
            self.side_image = Image.open("vector.png")
            photo = ImageTk.PhotoImage(self.side_image)
            self.side_image_label = Label(self.sgn_up_frame, image=photo,bg="#040405",width="400")
            self.side_image_label.image = photo
            self.side_image_label.place(x=0 ,y=65)

#background image sign  in sgn up form ===============================================================================================
#======================================================================================================================================
            self.sign_in_image = Image.open("hyy.png")
            photo = ImageTk.PhotoImage(self.sign_in_image)
            self.sign_in_image_label = Label(self.sgn_up_frame, image=photo,bg="#040405")
            self.sign_in_image_label.image = photo
            self.sign_in_image_label.place(x=570 ,y=20)


            self.sign_in_label = Label(self.sgn_up_frame,text="Sign Up",bg="#040405",fg="white",font=("yu gothic ui",13,"bold"))
            self.sign_in_label.place(x=615,y=130)


#Username1 in sgn up form   ==============================================================================================================
#=====================================================================================================================================
            self.username_label1 = Label(self.sgn_up_frame,text="First And Last Name",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.username_label1.place(x=500,y=155)
            self.username_entry1 = Entry(self.sgn_up_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"))
            self.username_entry1.place(x=500,y=178,width=300)

            self.username_line1 = Canvas(self.sgn_up_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
            self.username_line1.place(x=500,y=200)

#Placeholder of UserName1=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.username_entry1.insert(0,"Niyondiko Joffre")
            self.username_entry1.configure(state=DISABLED)
            def click4(event):
             self.username_entry1.configure(state=NORMAL)
             self.username_entry1.delete(0,END)
            self.username_entry1.bind("<Button-1>",click4)




#Username2 in sgn form=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.username_label2 = Label(self.sgn_up_frame,text="Mobile Number Or Email",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.username_label2.place(x=500,y=205)
            self.username_entry2 = Entry(self.sgn_up_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"))
            self.username_entry2.place(x=500,y=228,width=300)

            self.username_line2 = Canvas(self.sgn_up_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
            self.username_line2.place(x=500,y=250)

#Placeholder of Username2=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.username_entry2.insert(0,"niyondikojoffreasjubu@gmail.com")
            self.username_entry2.configure(state=DISABLED)
            def click5(event):
             self.username_entry2.configure(state=NORMAL)
             self.username_entry2.delete(0,END)
            self.username_entry2.bind("<Button-1>",click5)



#Password1 in sgn form=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.password_label1 = Label(self.sgn_up_frame,text="Create Password",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.password_label1.place(x=500,y=255)
            self.password_entry1 = Entry(self.sgn_up_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"),show="*")
            self.password_entry1.place(x=500,y=278,width=300)

            self.password_line1 = Canvas(self.sgn_up_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
            self.password_line1.place(x=500,y=300)

#Placeholder ofPassword1=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.password_entry1.insert(0,"Bujumbura+257")
            self.password_entry1.configure(state=DISABLED)
            def click6(event):
             self.password_entry1.configure(state=NORMAL)
             self.password_entry1.delete(0,END)
            self.password_entry1.bind("<Button-1>",click6)   


#Password2 of sgn Up form=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.password_label2 = Label(self.sgn_up_frame,text="Confirm Password",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.password_label2.place(x=500,y=305)
            self.password_entry2 = Entry(self.sgn_up_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"),show="*")
            self.password_entry2.place(x=500,y=328,width=300)

            self.password_line2 = Canvas(self.sgn_up_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
            self.password_line2.place(x=500,y=350)
#Placeholder Password2=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.password_entry2.insert(0,"Bujumbura+257")
            self.password_entry2.configure(state=DISABLED)
            def click7(event):
             self.password_entry2.configure(state=NORMAL)
             self.password_entry2.delete(0,END)
            self.password_entry2.bind("<Button-1>",click7)  

        

#show or hide password1/password2 IN SGN UP FORM=========================================================================================================
#============================================================================================================================================
            self.show_image10 = Image.open("show.png")
            self.photo11 = ImageTk.PhotoImage(self.show_image10)
            self.show_btn10 = Button(self.sgn_up_frame, image=self.photo11,bg="white",background="white",cursor="hand2",bd=0,command=self.show10)
            self.show_btn10.image = self.photo11
            self.show_btn10.place(x=780,y=330)

 
            self.hide_image10 = Image.open("hide.png")
            self.photo10 = ImageTk.PhotoImage(self.hide_image10)




            self.show_image5 = Image.open("show.png")
            self.photo6 = ImageTk.PhotoImage(self.show_image5)
            self.show_btn5 = Button(self.sgn_up_frame, image=self.photo6,bg="white",background="white",cursor="hand2",bd=0,command=self.show5)
            self.show_btn5.image = self.photo6
            self.show_btn5.place(x=780,y=280)

 
            self.hide_image5 = Image.open("hide.png")
            self.photo5 = ImageTk.PhotoImage(self.hide_image5)


#day-date-year of bd in sgn up form ====================================================================================================================================
#====================================================================================================================================

            self.bd_label = Label(self.sgn_up_frame,text="Select Your BirthDay Date :",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.bd_label.place(x=400,y=405)

            self.sel=StringVar()
            self.select_date = DateEntry(self.sgn_up_frame,textvariable=self.sel,bg="white",font=("Stylus",12,"bold"),date_pattern="dd/mm/yy",state="readonly")
            self.select_date.place(x=625,y=400)



#Enter your location province/commune/coline=======================================================================================================================================================================================================================
#==============================================================================================================================================================================================================================================================================================================
            self.local = Label(self.sgn_up_frame,text="Select Your Location In Burundi",bg="#040405",font=("Stylus",13,"bold"),fg="#00ffee")
            self.local.place(x=530,y=440)

            self.local = Label(self.sgn_up_frame,text="Select Your Province",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.local.place(x=300,y=460)
            self.local = Label(self.sgn_up_frame,text="Select Your Commune",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.local.place(x=500,y=460)
            self.local = Label(self.sgn_up_frame,text="Select Your Coline",bg="#040405",font=("Stylus",13,"bold"),fg="#41484d")
            self.local.place(x=700,y=460)
            
            self.province = Entry(self.sgn_up_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"))
            self.province.place(x=300,y=490)
            self.commune = Entry(self.sgn_up_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"))
            self.commune.place(x=500,y=490)
            self.colline = Entry(self.sgn_up_frame,highlightthickness=0,relief=FLAT,bg="white",fg="blue",font=("Stylus",12,"bold"))
            self.colline.place(x=700,y=490)

            self.province.insert(0,"Ruyigi")
            self.commune.insert(0,"Kinyinya")
            self.colline.insert(0,"Kinyinya")
            self.province.configure(state=DISABLED)
            self.commune.configure(state=DISABLED)
            self.colline.configure(state=DISABLED)
            def click_province(event):
             self.province.configure(state=NORMAL)
             self.province.delete(0,END)
            self.province.bind("<Button-1>",click_province)
            def click_commune(event):
             self.commune.configure(state=NORMAL)
             self.commune.delete(0,END)
            self.commune.bind("<Button-1>",click_commune)
            def click_colline(event):
             self.colline.configure(state=NORMAL)
             self.colline.delete(0,END)
            self.colline.bind("<Button-1>",click_colline) 

#Button de Sign UP=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
            self.resister_btn = Image.open("btn1.png")
            photo = ImageTk.PhotoImage(self.resister_btn)
            self.resister_btn_label = Label(self.sgn_up_frame, image=photo,bg="#040405")
            self.resister_btn_label.image = photo
            self.resister_btn_label.place(x=495 ,y=520)



            def clear():
                self.username_entry1.delete(0,END)
                self.username_entry2.delete(0,END)
                self.password_entry1.delete(0,END)
                self.password_entry2.delete(0,END)
                self.enter_sexe_entry.delete(0,END)
                self.commune.delete(0,END)
                self.province.delete(0,END)
                self.colline.delete(0,END)
                self.select_date.delete(0,END)
          


            def connect_data_signup():
                 if self.username_entry1.get()=='' or self.username_entry2.get()=='' or self.password_entry1.get()=='' or self.password_entry2.get()=='' or  self.commune.get()=='' or self.province.get()=='' or self.colline.get()=='' or self.enter_sexe_entry.get()=='' or self.select_date.get()=='':
                     messagebox.showerror('ERROR','Fill All Place',parent=self.sgn_up_frame) 
                 else :
                     try:
                         connection = sqlite3.connect("school.db")
                         mycursor = connection.cursor()
                         mycursor.execute("CREATE TABLE IF NOT EXISTS userinfos (Id integer PRIMARY KEY,Name TEXT,Mobile_Or_Email TEXT,Password TEXT,Password_Conf TEXT,Sexe TEXT,Date TEXT,Province TEXT,Commune TEXT,Colline TEXT,Message TEXT)")
                         connection.commit()
                     except Exception as es:
                         messagebox.showerror("Error","Cant Connect Something went wrong try again")
                     try :
                         if self.password_entry1.get() !=self.password_entry2.get():
                            messagebox.showerror('ERROR','Password Not Match',parent=self.sgn_up_frame)
                         else :
                            password = self.password_entry1.get()
                            if len(password) < 8 :
                                messagebox.showerror('ERROR','Password must have caractere more than 8',parent=self.sgn_up_frame)
                            else :
                                password_check = self.password_entry1.get()
                                if not re.match("[A-Z-]+[a-z-]+[0-9]",password_check):
                                    messagebox.showerror('ERROR','Password must have Upper , Lower and number !',parent=self.sgn_up_frame)
                                else :
                                    email =  self.username_entry2.get()
                                    if not re.search("@gmail.com",email):
                                        messagebox.showerror('ERROR','Email not valid !',parent=self.sgn_up_frame)
                                    else :
                                        connection = sqlite3.connect("school.db")
                                        mycursor= connection.cursor()
                                        check_if_exist_user = ("SELECT * FROM userinfos WHERE Name = ?")
                                        mycursor.execute(check_if_exist_user,[(self.username_entry1.get())])
                                        if not mycursor.fetchone():
                                           check_if_exist_user = ("SELECT * FROM userinfos WHERE Mobile_Or_Email = ?")
                                           mycursor.execute(check_if_exist_user,[(self.username_entry2.get())])
                                           if not mycursor.fetchone():
                                              mycursor.execute("INSERT INTO userinfos (Name,Mobile_Or_Email,Password,Password_Conf,Sexe,Date,Province,Commune,Colline) VALUES (?,?,?,?,?,?,?,?,?)",(self.username_entry1.get(),self.username_entry2.get(),self.password_entry1.get(),self.password_entry2.get(),self.enter_sexe_entry.get(),self.select_date.get(),self.province.get(),self.commune.get(),self.colline.get()))
                                              connection.commit()
                                              connection.close()
                                              clear()
                                              messagebox.showinfo("Succes","Account created successfully")
                                           else:
                                              messagebox.showerror('Error','Email Already Exists',parent=self.sgn_up_frame)
                                        else :
                                            messagebox.showerror("Error","Username Already Exists",parent=self.sgn_up_frame)      
                     except Exception as es:
                         messagebox.showerror("Error","Cant Registre Something went wrong try again")
                         
                 

                    



                     


            self.register = Button(self.resister_btn_label, text="SIGN UP",font=("yu gothic ui",13,"bold"),bg="#3047ff",fg="white",cursor="hand2",bd=0,width=25,activebackground="#3047ff",activeforeground="white",command=connect_data_signup)
            self.register.place(x=20,y=10)

  


            





            
          


 










#Sign up =====================================================================================================================
         self.sgn_label = Label(self.lgn_frame,text="No Account Yet ?", font=("yu gothic ui",11,"bold"),
                                     background="#040405",fg="#00EEFF")
         self.sgn_label.place(x=460,y=520)

         self.signup_btn = Image.open("register.png")
         photo = ImageTk.PhotoImage(self.signup_btn)
         self.signup_btn_label = Button(self.lgn_frame, image=photo,bg="#040405",background="#040405",cursor="hand2",bd=0,command=openSign_up)
         self.signup_btn_label.image = photo
         self.signup_btn_label.place(x=590 ,y=520,width=111,height=35)
     

      


#show or hide password IN window=========================================================================================================
         self.show_image = Image.open("show.png")
         self.photo1 = ImageTk.PhotoImage(self.show_image)
         self.show_btn = Button(self.lgn_frame, image=self.photo1,bg="white",background="white",cursor="hand2",bd=0,command=self.show)
         self.show_btn.image = self.photo1
         self.show_btn.place(x=780,y=340)

 
         self.hide_image = Image.open("hide.png")
         self.photo = ImageTk.PhotoImage(self.hide_image)




        
          


         def my_menu():
            pass




#Bar Menu ============================================================================================================
         self.menu = Menu(self.lgn_frame)
         self.menu_menu = Menu(self.menu,bg="#00F8EE",fg="black")
         
         self.menu_menu1 = Menu(self.menu_menu,bg="yellow",fg="black")
         self.menu_menu1.add_command(label="Setting Theme Color")
         self.menu_menu1.add_command(label="Setting Language")
         self.menu_menu1.add_command(label="Setting cookies")
         self.menu_menu1.add_command(label="Setting Save Infos")
         self.menu_menu1.add_command(label="Setting Voice")

         self.menu_menu2 = Menu(self.menu_menu,bg="blue",fg="white")
         self.menu_menu2.add_command(label="News Products")
         self.menu_menu2.add_command(label="News Cost")
         self.menu_menu2.add_command(label="News Members")
         self.menu_menu2.add_command(label="News Bonus")
         self.menu_menu2.add_command(label="News Infos")


         self.menu_menu3 = Menu(self.menu_menu,bg="red",fg="white")
         self.menu_menu3.add_command(label="Exit Here",command=back)
         self.menu_menu3.add_command(label="Exit Page",command=exit)


         self.menu_menu5 = Menu(self.menu_menu,bg="blue",fg="white")

         self.menu_menu5.add_command(label="Reflesh Page")
         self.menu_menu5.add_command(label="Reflesh Info")
         self.menu_menu5.add_command(label="Reflesh All")



         self.menu_menu4 = Menu(self.menu_menu,bg="yellow",fg="black")
    

         self.menu_menu4.add_command(label="How we can help You ?")
         self.menu_menu4.add_command(label="Contact Us")
         self.menu_menu4.add_command(label="Leave The Comment")

         self.menu.add_cascade(label="MENU",menu=self.menu_menu)
         self.menu_menu.add_cascade(label="NEWS",menu=self.menu_menu2)
         self.menu_menu.add_cascade(label="REFLESH",menu=self.menu_menu5)
         self.menu_menu.add_cascade(label="SETTINGS",menu=self.menu_menu1)
         self.menu_menu.add_cascade(label="HELP",menu=self.menu_menu4)
         self.menu_menu.add_cascade(label="EXIT",menu=self.menu_menu3)


         self.window.config(menu=self.menu)

#Definition of  hide or show password in window form================================================================================================================

    def show(self):
        self.hide_btn = Button(self.lgn_frame, image=self.photo,bg="white",background="white",cursor="hand2",bd=0,command=self.hide)
        self.hide_btn.image = self.photo
        self.hide_btn.place(x=780,y=340)
        self.password_entry.config(show="")

    def hide(self):
        self.show_btn = Button(self.lgn_frame, image=self.photo1,bg="white",background="white",cursor="hand2",bd=0,command=self.show)
        self.show_btn.image = self.photo1
        self.show_btn.place(x=780,y=340)
        self.password_entry.config(show="*")


# Definition of hide or show password1/password2 in sgn up form================================================================================================================
#==================================================================================================================================================================
    def show10(self):
        self.hide_btn10 = Button(self.sgn_up_frame, image=self.photo10,bg="white",background="white",cursor="hand2",bd=0,command=self.hide10)
        self.hide_btn10.image = self.photo10
        self.hide_btn10.place(x=780,y=330)
        self.password_entry2.config(show="")

    def hide10(self):
        self.show_btn10 = Button(self.sgn_up_frame, image=self.photo11,bg="white",background="white",cursor="hand2",bd=0,command=self.show10)
        self.show_btn10.image = self.photo11
        self.show_btn10.place(x=780,y=330)
        self.password_entry2.config(show="*")




    def show5(self):
        self.hide_btn5 = Button(self.sgn_up_frame, image=self.photo5,bg="white",background="white",cursor="hand2",bd=0,command=self.hide5)
        self.hide_btn5.image = self.photo5
        self.hide_btn5.place(x=780,y=280)
        self.password_entry1.config(show="")

    def hide5(self):
        self.show_btn5 = Button(self.sgn_up_frame, image=self.photo6,bg="white",background="white",cursor="hand2",bd=0,command=self.show5)
        self.show_btn5.image = self.photo6
        self.show_btn5.place(x=780,y=280)
        self.password_entry1.config(show="*")



# Definition of hide or show password1/password2 in sgn up form================================================================================================================
#==================================================================================================================================================================
#==================================================================================================================================================================
    def show15(self):
        self.hide_btn15 = Button(self.forget_password_frame, image=self.photo15,bg="white",background="white",cursor="hand2",bd=0,command=self.hide15)
        self.hide_btn15.image = self.photo15
        self.hide_btn15.place(x=780,y=478)
        self.forget_password_entry2.config(show="")

    def hide15(self):
        self.show_btn15 = Button(self.forget_password_frame, image=self.photo16,bg="white",background="white",cursor="hand2",bd=0,command=self.show15)
        self.show_btn15.image = self.photo16
        self.show_btn15.place(x=780,y=478)
        self.forget_password_entry2.config(show="*")




    def show20(self):
        self.hide_btn20 = Button(self.forget_password_frame, image=self.photo20,bg="white",background="white",cursor="hand2",bd=0,command=self.hide20)
        self.hide_btn20.image = self.photo20
        self.hide_btn20.place(x=780,y=417)
        self.forget_password_entry1.config(show="")

    def hide20(self):
        self.show_btn20 = Button(self.forget_password_frame, image=self.photo21,bg="white",background="white",cursor="hand2",bd=0,command=self.show20)
        self.show_btn20.image = self.photo21
        self.show_btn20.place(x=780,y=417)
        self.forget_password_entry1.config(show="*")



  
        

#button ================================================================================================================
#============================================================================================================================================
#window from forget password========================================================================================================================
#========================================================================================================================
#========================================================================================================================




#Widow Frame from forget password============================================================================================================
#========================================================================================================================
#========================================================================================================================




 #background image in sgn up form =====================================================================================================
#=================================================================================================================================================

#search bar in sgn up form  ============================================================================================================
#==================================================================================================================================
   
#Placeholder of search bar=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================    
      





       
    






            
def page():
    window = Tk()
    Loginform(window)
    window.mainloop()


if __name__ == "__main__":
    try:
        connection = sqlite3.connect("school.db")
        mycursor = connection.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS userinfos (Id integer PRIMARY KEY,Name TEXT,Mobile_Or_Email TEXT,Password TEXT,Password_Conf TEXT,Sexe TEXT,Date TEXT,Province TEXT,Commune TEXT,Colline TEXT,Message TEXT)")
        connection.commit()
    except Exception as es:
        messagebox.showerror("Error","Cant Connect Something went wrong try again")
    page()