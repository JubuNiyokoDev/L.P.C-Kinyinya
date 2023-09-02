#coding:utf-8
from argparse import FileType
from tkinter import *
import time
import ttkthemes
from tkinter import ttk
from tkinter import messagebox,filedialog
import sqlite3
from PIL import ImageTk , Image



root=ttkthemes.ThemedTk()
root.get_themes()

root.set_theme("black")
root.state("zoomed")
root.title("Student Managment System")
root.iconbitmap("iconapp.ico")


def Toplevel_of_update_notes():
    global noteEntry_update,screen,idEntry_update
    screen =Toplevel()
    screen.title("Search Notes")
    screen.grab_set()
    screen.resizable(False,False)
    
    
    idLabel =Label(screen,text='Id',font=("times new romain",12,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry_update =Entry(screen,font=("roman",12,'bold'),width=24)
    idEntry_update.grid(row=0,column=1,padx=15,pady=10)

    noteLabel =Label(screen,text='Notes',font=("times new romain",12,'bold'))
    noteLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    noteEntry_update =Entry(screen,font=("roman",12,'bold'),width=24)
    noteEntry_update.grid(row=1,column=1,padx=15,pady=10)
    
    add_note_button = ttk.Button(screen,text="UPDATE",command=update_event)
    add_note_button.grid(row=8,columnspan=2,pady=15)

def Toplevel_of_saerch_notes():
    global idEntry_search,screen
    screen =Toplevel()
    screen.title("Search Notes")
    screen.grab_set()
    screen.resizable(False,False)


    idLabel_search =Label(screen,text='Id',font=("times new romain",12,'bold'))
    idLabel_search.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry_search =Entry(screen,font=("roman",12,'bold'),width=24)
    idEntry_search.grid(row=0,column=1,padx=15,pady=10)
    
    add_note_button = ttk.Button(screen,text="SEARCH",command=search_event)
    add_note_button.grid(row=8,columnspan=2,pady=15)

def Toplevel_of_add_notes():
    global noteEntry,screen
    screen =Toplevel()
    screen.title("Search Notes")
    screen.grab_set()
    screen.resizable(False,False)


    noteLabel =Label(screen,text='Notes',font=("times new romain",12,'bold'))
    noteLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    noteEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    noteEntry.grid(row=0,column=1,padx=15,pady=10)
    
    add_note_button = ttk.Button(screen,text="ADD NOTES",command=add_notes)
    add_note_button.grid(row=8,columnspan=2,pady=15)


def add_notes():
    if noteEntry.get()=='':
        messagebox.showerror("ERROR","Fill All Place",parent=screen)
    else:
        try:
            connection = sqlite3.connect("school.db")
            mycursor= connection.cursor()
            mycursor.execute("INSERT INTO cours_trimestre1_anne1_science_examen (NOTES,Added_Time,Added_Date) VALUES(?,?,?)",(noteEntry.get(),currenttime,date))
            connection.commit()
            result = messagebox.askyesno('Data Added Successfully','Do You Want To Clean The Form ?',parent=screen)
            if result:
                noteEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror("ERROR",'Id Cannot Be Repeated',parent=screen)
            return
        query="SELECT * FROM cours_trimestre1_anne1_science_examen"
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())

        for data in fetched_data:
              studentTable.insert('',END,values=data)

def update_event():
    connection = sqlite3.connect("school.db")
    mycursor= connection.cursor()
    query="update cours_trimestre1_anne1_science_examen set NOTES = ? where Id = ?"
    mycursor.execute(query,(noteEntry_update.get(),idEntry_update.get()))
    connection.commit()
    messagebox.showinfo('SUCCESS',f'Id {idEntry_update.get()} Is Modified Successfully',parent=screen)
    screen.destroy()
    show_event()

def search_event():
    global search_event
    connection = sqlite3.connect("school.db")
    mycursor= connection.cursor()
    query = ("select * from cours_trimestre1_anne1_science_examen where Id=?")
    mycursor.execute(query,[(idEntry_search.get())])
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)



def delete_event():
    try :
        connection = sqlite3.connect("school.db")
        mycursor= connection.cursor()
        indexing=studentTable.focus()
        content=studentTable.item(indexing)
        content_id=content['values'][0]
        query='delete from cours_trimestre1_anne1_science_examen where Id=?'
        mycursor.execute(query,[(content_id)])
        connection.commit()
        messagebox.showinfo('DELETED',f'This {content_id} Is Deleted     Succesfully')
        query="select * from cours_trimestre1_anne1_science_examen"
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('',END,values=data)
    except :
        messagebox.showerror("Error","Choose the item to delete first")




def show_event():
    connection = sqlite3.connect("school.db")
    mycursor = connection.cursor()
    query="SELECT * FROM cours_trimestre1_anne1_science_examen"
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)






def connect():
     try:
        connection = sqlite3.connect("school.db")
        mycursor= connection.cursor()
        connection.commit()
        messagebox.showinfo("SUCCEFUL","Database Connection Is Successful")
        searchButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)
        exportButton.config(state=NORMAL)
        importeventButton.config(state=NORMAL)
        maths.config(state=NORMAL)
     except:
        messagebox.showerror("ERROR","Invalid Server")
     try:
        connection = sqlite3.connect("school.db")
        mycursor = connection.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS  cours_trimestre1_anne1_science_examen (Id integer PRIMARY KEY,NOTES TEXT,Added_Time,Added_Date)")
        connection.commit()
     except:
          messagebox.showerror("Error","Sorry Something went wrong")
     
 

def math():
    show =ttk.Button(root,text="Show Notes",command=show_event)
    show.place(x=340,y=5)
    update =ttk.Button(root,text="Update Notes",command=Toplevel_of_update_notes)
    update.place(x=460,y=5)
    delete =ttk.Button(root,text="Delete Notes",command=delete_event)
    delete.place(x=590,y=5)
    search =ttk.Button(root,text="Search Notes",command=Toplevel_of_saerch_notes)
    search.place(x=710,y=5)
  
 

def import_data():
    url=filedialog.askopenfilenames(title='Select A File',filetypes=(('png files','*.png'),('all files','*.*')))
    myfile=Label(rightFrame,text=url)
    myfile.place(x=100,y=100)
    myimage=ImageTk.PhotoImage(Image.open(url))
    myimage_label= Label(image=myimage)
    myimage_label.place(x=100,y=400)
    file=open(url,'w')
    file.close()




   


    




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
    sliderLabel.after(300,slider)

def clock():
       global date,currenttime
       date=time.strftime("%d/%m/%Y")
       currenttime=time.strftime("%H:%M:%S")
       datetimeLabel.config(text=f"   Date:{date}\nTime:{currenttime}")
       datetimeLabel.after(1000,clock)


datetimeLabel = Label(root,font=("time new roman",18,"bold"))
datetimeLabel.place(x=5,y=5)
clock()


s="WELCOME CLIENT :"
sliderLabel = Label(root,text=s,font=("arial",28,"bold"))
sliderLabel.place(x=280,y=50)
slider()
Label_canvas = Canvas(root,width=1015,height=5.0,bg="blue",highlightthickness=0)
Label_canvas.place(x=5,y=110)


conncectButton =ttk.Button(root,text="Connect To DataBase",cursor="hand2",command=connect)
conncectButton.place(x=820,y=5)








def exportfonction_for_user():
      messagebox.showinfo("HELLO","COMMING SOON",parent=root)
      global exportButton,exitButton


searchButton =ttk.Button(root,text="Add Notes",command=Toplevel_of_add_notes,state=DISABLED)
searchButton.place(x=5,y=70)

exportButton =ttk.Button(root,text="Export File",command=exportfonction_for_user,state=DISABLED)
exportButton.place(x=95,y=70)

exitButton =ttk.Button(root,text="Exit Here",command=exit,state=DISABLED)
exitButton.place(x=183,y=70)

importeventButton =ttk.Button(root,text="Import Document",cursor="hand2",command=import_data,state=DISABLED)
importeventButton.place(x=830,y=50)





rightFrame =Frame(root)
rightFrame.place(x=120,y=120,width=900,height=585)


scolBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scolBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=("Id","Welcome"),xscrollcommand=scolBarX.set,yscrollcommand=scolBarY.set)

scolBarX.config(command=studentTable.xview)
scolBarY.config(command=studentTable.yview)


scolBarX.pack(side=BOTTOM,fill=X)
scolBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Welcome',text='Les Examens')
studentTable.heading('Id',text='Id')


studentTable.column('Id',width=50)
studentTable.column('Welcome',width=50)


style = ttk.Style()
style.configure('Treeview',rowheight=30,font=('arial',11,'bold'))
style.configure('Treeview.Heading',font=('arial',11,'bold'))

studentTable.config(show='headings')






maths =ttk.Button(root,text="SHOW FONCTION",command=math,state=DISABLED)
maths.place(x=3,y=120)









root.mainloop()