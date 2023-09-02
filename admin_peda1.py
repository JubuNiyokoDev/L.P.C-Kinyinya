#coding:utf-8
from tkinter import *
import time
from tkinter import messagebox,filedialog
import ttkthemes
from tkinter import ttk
import sqlite3
import pandas

 

root=ttkthemes.ThemedTk()
root.get_themes()

root.set_theme("itft1")
root.state("zoomed")
root.title("Student Managment System")
root.iconbitmap("iconapp.ico")



#fonction 
def exit():
    result=messagebox.askyesno('Exit Or Not','Do You Want To Exit?')
    if result:
       root.destroy()
    else:
        pass
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','D.O.B',"T.O.B",'Added Time','Added Date'])
    table.to_csv(url,index=False)
    messagebox.showinfo('SUCCESS','Data Was Exported Successfully')


    


def toplevel_data(title,button_text,command):
    global idEntry,phoneEntry,nameEntry,emailEntry,adressEntry,genderEntry,dobEntry,screen,tobEntry
    screen =Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False,False)


    idLabel =Label(screen,text='Id',font=("times new romain",12,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    idEntry.grid(row=0,column=1,padx=15,pady=10)

    nameLabel =Label(screen,text='Name',font=("time new romain",12,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=15,pady=10)


    phoneLabel =Label(screen,text='Phone',font=("time new romain",12,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,padx=15,pady=10)

    emailLabel =Label(screen,text='Email',font=("time new romain",12,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    emailEntry.grid(row=3,column=1,padx=15,pady=10)

    adressLabel =Label(screen,text='Address',font=("time new romain",12,'bold'))
    adressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    adressEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    adressEntry.grid(row=4,column=1,padx=15,pady=10)

    genderLabel =Label(screen,text='Gender',font=("time new romain",12,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    genderEntry.grid(row=5,column=1,padx=15,pady=10)

    dobLabel =Label(screen,text='D.O.B',font=("time new romain",12,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    dobEntry.grid(row=6,column=1,padx=15,pady=10)

    tobLabel =Label(screen,text='T.O.B',font=("time new romain",12,'bold'))
    tobLabel.grid(row=7,column=0,padx=30,pady=15,sticky=W)
    tobEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    tobEntry.grid(row=7,column=1,padx=15,pady=10)

    student_button = ttk.Button(screen,text=button_text,command=command)
    student_button.grid(row=8,columnspan=2,pady=15)
    if title=="Update Student":
        indexing=studentTable.focus()

        content=studentTable.item(indexing)
        listdata=content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        phoneEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        adressEntry.insert(0 ,listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])
        tobEntry.insert(0, listdata[7])


def update_data():
    connection = sqlite3.connect("school.db")
    mycursor= connection.cursor()
    query="update ListStudent_peda1 set Name=?,Mobile=?,Email=?,Address=?,Gender=?,D_O_B=?,T_O_B=?,Added_Time=?,Added_Date=? where Id=?"
    mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),adressEntry.get(),genderEntry.get(),dobEntry.get(),tobEntry.get(),currenttime,date,idEntry.get()))
    connection.commit()
    messagebox.showinfo('SUCCESS',f'Id {idEntry.get()} Is Modified Successfully',parent=screen)
    screen.destroy()
    show_student()



def show_student():
    connection = sqlite3.connect("school.db")
    mycursor = connection.cursor()
    query="SELECT * FROM ListStudent_peda1"
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)



def delete_student():
    connection = sqlite3.connect("school.db")
    mycursor= connection.cursor()
    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from ListStudent_peda1 where id=?'
    mycursor.execute(query,[(content_id)])
    connection.commit()
    messagebox.showinfo('DELETED',f'This {content_id} Is Deleted Succesfully')
    query="select * from ListStudent_peda1"
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)


def search_data():
    global search_data
    connection = sqlite3.connect("school.db")
    mycursor= connection.cursor()
    query = ("select * from ListStudent_peda1 where Id=? or Name=? or Mobile=? or  Email=?  or Address=? or Gender=? or D_O_B=? or T_O_B=?")
    mycursor.execute(query,[(idEntry.get()),(nameEntry.get()),(emailEntry.get()),(phoneEntry.get()),(adressEntry.get()),(genderEntry.get()),(dobEntry.get()),(tobEntry.get())])
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)




def add_data():
    if idEntry.get()=='' or  nameEntry.get()=='' or  phoneEntry.get()=='' or  emailEntry.get()=='' or  adressEntry.get()==''  or  genderEntry.get()=='' or  dobEntry.get()=='':
        messagebox.showerror("ERROR","Fill All Place",parent=screen)
    else:
        try:
            connection = sqlite3.connect("school.db")
            mycursor= connection.cursor()
            mycursor.execute("INSERT INTO ListStudent_peda1 (Id,Name,Mobile,Email,Address,Gender,D_O_B,T_O_B,Added_Time,Added_Date) VALUES(?,?,?,?,?,?,?,?,?,?)",(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),adressEntry.get(),genderEntry.get(),dobEntry.get(),tobEntry.get(),currenttime,date))
            connection.commit()
            result = messagebox.askyesno('Data Added Successfully','Do You Want To Clean The Form ?',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                emailEntry.delete(0,END)
                adressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
                tobEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror("ERROR",'Id Cannot Be Repeated',parent=screen)
            return
        query="SELECT * FROM ListStudent_peda1"
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())

        for data in fetched_data:
              studentTable.insert('',END,values=data)
              
   
    




def connect():
     global mycursor,con
     try :
        connection = sqlite3.connect("school.db")
        mycursor= connection.cursor()
        connection.commit()
        messagebox.showinfo("SUCCEFUL","Database Connection Is Successful")
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        exitstudentButton.config(state=NORMAL)
        addeventButton.config(state=NORMAL)
     except :
         messagebox.showerror("Error","Sorry Something went wrong")
         return
     
     try :
         connection = sqlite3.connect("school.db")
         mycursor = connection.cursor()
         mycursor.execute("CREATE TABLE IF NOT EXISTS ListStudent_peda1(Id int,Name TEXT,Mobile TEXT,Email TEXT,Address TEXT,Gender TEXT,D_O_B TEXT, T_O_B TEXT,Added_Time TEXT,Added_Date TEXT)")
         connection.commit()
     except :
         messagebox.showerror("Error","Sorry Something went wrong")

         
     






def addeventfonction_for_admin():
    messagebox.showinfo("WELCOME ADMIN","NOW GO!!!!!!")
    root.destroy()
    import event

count = 0
text=''

def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count=count+1
    sliderLabel.after(400,slider)

def clock():
       global date,currenttime
       date=time.strftime("%d/%m/%Y")
       currenttime=time.strftime("%H:%M:%S")
       datetimeLabel.config(text=f"   Date:{date}\nTime:{currenttime}")
       datetimeLabel.after(1000,clock)


datetimeLabel = Label(root,font=("time new roman",18,"bold"))
datetimeLabel.place(x=5,y=5)
clock()


s ="Student Managment System Pedagogie 1"
sliderLabel = Label(root,text=s,font=("arial",28,"bold"),width=25)
sliderLabel.place(x=210,y=0)
slider()

conncectButton =ttk.Button(root,text="Connect To DataBase",cursor="hand2",command=connect)
conncectButton.place(x=820,y=5)
addeventButton =ttk.Button(root,text="Add Event",state=DISABLED,command=addeventfonction_for_admin)
addeventButton.place(x=855,y=40)

leftFrame =Frame(root)
leftFrame.place(x=50,y=80,width=200,height=600)
logo_image= PhotoImage(file="hyy.png")
logo_label = Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0)

addstudentButton =ttk.Button(leftFrame,text="Add Student",state=DISABLED,command=lambda :toplevel_data('Add Student','Add Student',add_data))
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton =ttk.Button(leftFrame,text="Search Student",state=DISABLED,command=lambda :toplevel_data('Search Student','Search Student',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton =ttk.Button(leftFrame,text="Delete Student",state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton =ttk.Button(leftFrame,text="Update Student",state=DISABLED,command=lambda :toplevel_data('Update Student','Update Student',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton =ttk.Button(leftFrame,text="Show Student",state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton =ttk.Button(leftFrame,text="Export Data",state=DISABLED,command=export_data)
exportstudentButton.grid(row=6,column=0,pady=20)

exitstudentButton =ttk.Button(leftFrame,text="Exit",state=DISABLED,command=exit)
exitstudentButton.grid(row=7,column=0,pady=20)





rightFrame =Frame(root)
rightFrame.place(x=280,y=80,width=730,height=620)


scolBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scolBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=("Id","Full Name","Mobile","Email","Address","Gender"
             ,"D.O.B","T.O.B","Added Time","Added Date"),xscrollcommand=scolBarX.set,yscrollcommand=scolBarY.set)

scolBarX.config(command=studentTable.xview)
scolBarY.config(command=studentTable.yview)


scolBarX.pack(side=BOTTOM,fill=X)
scolBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Full Name',text='Full Name')
studentTable.heading('Mobile',text='Mobile N°')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('T.O.B',text='T.O.B')
studentTable.heading('Added Time',text='Added Time')
studentTable.heading('Added Date',text='Added Date')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Full Name',width=300,anchor=CENTER)
studentTable.column('Mobile',width=300,anchor=CENTER)
studentTable.column('Email',width=400,anchor=CENTER)
studentTable.column('Address',width=100,anchor=CENTER)
studentTable.column('Gender',width=80,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('T.O.B',width=100,anchor=CENTER)
studentTable.column('Added Time',width=100,anchor=CENTER)
studentTable.column('Added Date',width=100,anchor=CENTER)

style = ttk.Style()
style.configure('Treeview',rowheight=30,font=('arial',11,'bold'))
style.configure('Treeview.Heading',font=('arial',11,'bold'))

studentTable.config(show='headings')





root.mainloop()