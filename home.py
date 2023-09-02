#coding:utf-8
from tkinter import *
import time
from tkinter import messagebox,filedialog
import ttkthemes
from tkinter import ttk
import sqlite3
import pandas

 

root_home=ttkthemes.ThemedTk()
root_home.get_themes()

root_home.set_theme("itft1")
root_home.state("zoomed")
root_home.title("Student Managment System")
root_home.iconbitmap("iconapp.ico")



#fonction 
def peda_1():
    root_home.destroy()
    # screen_peda.destroy()
    import admin_peda1
def peda_2():
    root_home.destroy()
    # screen_peda.destroy()
    import admin_peda2
def peda_3():
    root_home.destroy()
    # screen_peda.destroy()
    import admin_peda3 
def peda_4():
    root_home.destroy()
    # screen_peda.destroy()
    import admin_peda4
def langue1():
    root_home.destroy()
    # screen_lng.destroy()
    import admin_lng1
def langue2():
    root_home.destroy()
    # screen_lng.destroy()
    import admin_lng2
def langue3():
    root_home.destroy()
    # screen_lng.destroy()
    import admin_lng3
def ssh_1():
    root_home.destroy()
    # screen_ssh.destroy()
    import admin_ssh1 
def ssh_2():
    root_home.destroy()
    # screen_ssh.destroy()
    import admin_ssh2 
def ssh_3():
    root_home.destroy()
    # screen_ssh.destroy()
    import admin_ssh3
def math_physique2():
    root_home.destroy()
    # screen_mp.destroy()
    import admin_mp2 
def math_physique3():
    root_home.destroy()
    # screen_mp.destroy()
    import admin_mp3 
def bio_chimie_2():
    root_home.destroy()
    # screen_biochm.destroy()
    import admin_biochm2 
def bio_chimie_3():
    root_home.destroy()
    # screen_biochm.destroy()
    import admin_biochm3 
def premiere_science():
    root_home.destroy()
    import admin_1ere_science
def toplevel_data_peda(title):
    global screen_peda
    screen_peda =Toplevel()
    screen_peda.title(title)
    screen_peda.grab_set()
    screen_peda.geometry("200x300")
    screen_peda.resizable(False,False)
    peda1 = ttk.Button(screen_peda,text='PEDA 1',command=peda_1)
    peda1.grid(row=0,columnspan=2,pady=15,padx=70)
    peda2 = ttk.Button(screen_peda,text='PEDA 2',command=peda_2)
    peda2.grid(row=1,columnspan=2,pady=15,padx=70)
    peda3 = ttk.Button(screen_peda,text='PEDA 3',command=peda_3)
    peda3.grid(row=2,columnspan=2,pady=15,padx=70)
    peda4 = ttk.Button(screen_peda,text='PEDA 4',command=peda_4)
    peda4.grid(row=3,columnspan=2,pady=15,padx=70)

def toplevel_data_lng(title):
    global screen_lng
    screen_lng =Toplevel()
    screen_lng.title(title)
    screen_lng.grab_set()
    screen_lng.geometry("200x200")
    screen_lng.resizable(False,False)
    lng1 = ttk.Button(screen_lng,text='LANGUE 1',command=langue1)
    lng1.grid(row=0,columnspan=2,pady=15,padx=60)
    lng2 = ttk.Button(screen_lng,text='LANGUE 2',command=langue2)
    lng2.grid(row=1,columnspan=2,pady=15,padx=60)
    lng3 = ttk.Button(screen_lng,text='LANGUE 3',command=langue3)
    lng3.grid(row=2,columnspan=2,pady=15,padx=60)

def toplevel_data_ssh(title):
    global screen_ssh
    screen_ssh =Toplevel()
    screen_ssh.title(title)
    screen_ssh.grab_set()
    screen_ssh.geometry("200x200")
    screen_ssh.resizable(False,False)
    ssh1 = ttk.Button(screen_ssh,text='SSH 1',command=ssh_1)
    ssh1.grid(row=0,columnspan=2,pady=15,padx=70)
    ssh2 = ttk.Button(screen_ssh,text='SSH 2',command=ssh_2)
    ssh2.grid(row=1,columnspan=2,pady=15,padx=70)
    ssh3 = ttk.Button(screen_ssh,text='SSH 3',command=ssh_3)
    ssh3.grid(row=2,columnspan=2,pady=15,padx=70)
def toplevel_data_mp(title):
    global screen_mp
    screen_mp =Toplevel()
    screen_mp.title(title)
    screen_mp.grab_set()
    screen_mp.geometry("200x200")
    screen_mp.resizable(False,False)
    mp2 = ttk.Button(screen_mp,text='MTP 2',command=math_physique2)
    mp2.grid(row=0,columnspan=2,pady=15,padx=70)
    mp3 = ttk.Button(screen_mp,text='MTP 3',command=math_physique3)
    mp3.grid(row=1,columnspan=2,pady=15,padx=70)

def toplevel_data_biochm(title):
    global screen_biochm
    screen_biochm =Toplevel()
    screen_biochm.title(title)
    screen_biochm.grab_set()
    screen_biochm.geometry("200x200")
    screen_biochm.resizable(False,False)
    bio_chimie2 = ttk.Button(screen_biochm,text='BIO-CHIMIE 2',command=bio_chimie_2)
    bio_chimie2.grid(row=0,columnspan=2,pady=15,padx=55)
    bio_chimie3 = ttk.Button(screen_biochm,text='BIO-CHIMIE 3',command=bio_chimie_3)
    bio_chimie3.grid(row=1,columnspan=2,pady=15,padx=55)
    



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


datetimeLabel = Label(root_home,font=("time new roman",18,"bold"))
datetimeLabel.place(x=5,y=5)
clock()


s ="Student Managment System"
sliderLabel = Label(root_home,text=s,font=("arial",28,"bold"),width=25)
sliderLabel.place(x=210,y=0)
slider()


leftFrame =Frame(root_home)
leftFrame.place(x=50,y=80,width=200,height=600)
logo_image= PhotoImage(file="hyy.png")
logo_label = Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0)

addstudentButton =ttk.Button(leftFrame,text="1ere SCIENCE",command=premiere_science)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton =ttk.Button(leftFrame,text="SCIENCE A",command=lambda :toplevel_data_mp('SCIENCE A'))
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton =ttk.Button(leftFrame,text="SCIENCE B",command=lambda :toplevel_data_biochm('SCIENCE B'))
deletestudentButton.grid(row=3,column=0,pady=20)

showstudentButton =ttk.Button(leftFrame,text="LANGUE",command=lambda :toplevel_data_lng('LANGUE'))
showstudentButton.grid(row=4,column=0,pady=20)

exportstudentButton =ttk.Button(leftFrame,text="PEDA",command=lambda :toplevel_data_peda('PEDA'))
exportstudentButton.grid(row=5,column=0,pady=20)

updatestudentButton =ttk.Button(leftFrame,text="SSH",command=lambda :toplevel_data_ssh('SSH'))
updatestudentButton.grid(row=6,column=0,pady=20)







rightFrame =Frame(root_home)
rightFrame.place(x=280,y=80,width=730,height=620)




root_home.mainloop()