#coding:utf-8
from argparse import FileType
from tkinter import *
import time
import ttkthemes
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import ImageTk , Image



root=ttkthemes.ThemedTk()
root.get_themes()

root.set_theme("black")
root.state("zoomed")
root.title("Student Managment System")
root.iconbitmap("iconapp.ico")










def Toplevel_of_search_notes():
    global idEntry_search,screen
    screen =Toplevel()
    screen.title("Search Notes")
    screen.grab_set()
    screen.resizable(False,False)
    idLabel_search =Label(screen,text='Id',font=("times new romain",12,'bold'))
    idLabel_search.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry_search =Entry(screen,font=("roman",12,'bold'),width=24)
    idEntry_search.grid(row=0,column=1,padx=15,pady=10)
    
    add_note_button = ttk.Button(screen,text="SEARCH",command=searchfonction_for_user)
    add_note_button.grid(row=8,columnspan=2,pady=15)
    # my_list = Listbox(screen,width=40,height=20)
    # my_list.grid(row=2,columnspan=1)
    
    # def update(data):
    #     my_list.delete(0,END)
    #     for item in data :
    #        my_list.insert(END,item)
    
    # def fillout(event):
    #     noteEntry.delete(0,END)
        
    #     noteEntry.insert(0,my_list.get(ACTIVE))
    
    # def check(event):
    #     typed = noteEntry.get()
    #     if typed == '':
    #         data = toppings
    #     else:
    #         data = []
    #         for item in toppings :
    #             if typed.lower() in item :
    #                 data.append(item)
    #     update(data)
    # connection = sqlite3.connect("school.db")
    # mycursor= connection.cursor()
    # mycursor.execute("SELECT * FROM cours_trimestre1_anne1_science_examen")
    # connection.commit()
    # toppings = mycursor.fetchall()
    # update(toppings)
    # my_list.bind("<<ListboxSelect>>",fillout)
    # noteEntry.bind("<KeyRelease>",check)
        
def searchfonction_for_user():
    global searchfonction_for_user
    connection = sqlite3.connect("school.db")
    mycursor= connection.cursor()
    query = ("select * from cours_trimestre1_anne1_science_examen where Id=?")
    mycursor.execute(query,[(idEntry_search.get())])
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)

    
    
    



    
   
    
    









def connect_database():
    try:
        connection = sqlite3.connect("school.db")
        mycursor= connection.cursor()
        connection.commit()
        messagebox.showinfo("SUCCEFUL","Database Connection Is Successful")
        searchButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)
        exportButton.config(state=NORMAL)
    except:
        messagebox.showerror("ERROR","Invalid Server")
    
     
 







   


    




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


conncectButton =ttk.Button(root,text="Connect To DataBase",cursor="hand2",command=connect_database)
conncectButton.place(x=820,y=5)








def exportfonction_for_user():
      messagebox.showinfo("HELLO","COMMING SOON",parent=root)
      global exportButton,exitButton


searchButton =ttk.Button(root,text="Search Notes",command=Toplevel_of_search_notes,state=DISABLED)
searchButton.place(x=5,y=70)

exportButton =ttk.Button(root,text="Export Notes",command=exportfonction_for_user,state=DISABLED)
exportButton.place(x=95,y=70)

exitButton =ttk.Button(root,text="Exit Here",command=exit,state=DISABLED)
exitButton.place(x=183,y=70)







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















root.mainloop()