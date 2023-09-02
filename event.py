#coding:utf-8
from encodings import search_function
from tkinter import *
import time
from tkinter import messagebox
import ttkthemes
from tkinter import ttk



root=ttkthemes.ThemedTk()
root.get_themes()

root.set_theme("itft1")
root.state("zoomed")
root.title("Student Managment System")


def trimestre1_anne1_science_stuation():
      stuation.config(state=DISABLED)
      examen.config(state=DISABLED)
      interrogation.config(state=DISABLED)
      parie1.config(state=DISABLED)
      parie2.config(state=DISABLED)
      parie3.config(state=DISABLED)
      searchstudentButton.config(state=DISABLED)
      exportstudentButton.config(state=DISABLED)
      exitstudentButton.config(state=DISABLED)
    

      root.destroy()
      import cours_trimestre1_anne1_science_stuation

def trimestre2_anne1_science_examen():
      stuation.config(state=DISABLED)
      examen.config(state=DISABLED)
      interrogation.config(state=DISABLED)
      parie1.config(state=DISABLED)
      parie2.config(state=DISABLED)
      parie3.config(state=DISABLED)
      searchstudentButton.config(state=DISABLED)
      exportstudentButton.config(state=DISABLED)
      exitstudentButton.config(state=DISABLED)
    

      root.destroy()
      import cours_trimestre2_anne1_science_examen

def trimestre2_anne1_science_interrogation():
      stuation.config(state=DISABLED)
      examen.config(state=DISABLED)
      interrogation.config(state=DISABLED)
      parie1.config(state=DISABLED)
      parie2.config(state=DISABLED)
      parie3.config(state=DISABLED)
      searchstudentButton.config(state=DISABLED)
      exportstudentButton.config(state=DISABLED)
      exitstudentButton.config(state=DISABLED)
     

      root.destroy()
      import cours_trimestre2_anne1_science_interrogation


def trimestre2_anne1_science_situation():
      stuation.config(state=DISABLED)
      examen.config(state=DISABLED)
      interrogation.config(state=DISABLED)
      parie1.config(state=DISABLED)
      parie2.config(state=DISABLED)
      parie3.config(state=DISABLED)
      searchstudentButton.config(state=DISABLED)
      exportstudentButton.config(state=DISABLED)
      exitstudentButton.config(state=DISABLED)
 

      root.destroy()
      import cours_trimestre2_anne1_science_situation

def trimestre1_anne1_science_examen():
      stuation.config(state=DISABLED)
      examen.config(state=DISABLED)
      interrogation.config(state=DISABLED)
      parie1.config(state=DISABLED)
      parie2.config(state=DISABLED)
      parie3.config(state=DISABLED)
      searchstudentButton.config(state=DISABLED)
      exportstudentButton.config(state=DISABLED)
      exitstudentButton.config(state=DISABLED)
      

      root.destroy()
      import cours_trimestre1_anne1_science_examen_admin

def trimestre1_anne1_science_interrogation():
      stuation.config(state=DISABLED)
      examen.config(state=DISABLED)
      interrogation.config(state=DISABLED)
      parie2.config(state=DISABLED)
      parie1.config(state=DISABLED)
      parie3.config(state=DISABLED)
      searchstudentButton.config(state=DISABLED)
      exportstudentButton.config(state=DISABLED)
      exitstudentButton.config(state=DISABLED)
     

      root.destroy()
      import cours_trimestre1_anne1_science_interrogation

def trimestre3_anne1_science_situation():
      stuation.config(state=DISABLED)
      examen.config(state=DISABLED)
      interrogation.config(state=DISABLED)
      parie2.config(state=DISABLED)
      parie1.config(state=DISABLED)
      parie3.config(state=DISABLED)
      searchstudentButton.config(state=DISABLED)
      exportstudentButton.config(state=DISABLED)
      exitstudentButton.config(state=DISABLED)
     

      root.destroy()
      import cours_trimestre3_anne1_science_situation

def trimestre3_anne1_science_interrogation():
      stuation.config(state=DISABLED)
      examen.config(state=DISABLED)
      interrogation.config(state=DISABLED)
      parie2.config(state=DISABLED)
      parie1.config(state=DISABLED)
      parie3.config(state=DISABLED)
      searchstudentButton.config(state=DISABLED)
      exportstudentButton.config(state=DISABLED)
      exitstudentButton.config(state=DISABLED)
     

      root.destroy()
      import cours_trimestre3_anne1_science_interrogation

def trimestre3_anne1_science_examen():
      stuation.config(state=DISABLED)
      examen.config(state=DISABLED)
      interrogation.config(state=DISABLED)
      parie2.config(state=DISABLED)
      parie1.config(state=DISABLED)
      parie3.config(state=DISABLED)
      searchstudentButton.config(state=DISABLED)
      exportstudentButton.config(state=DISABLED)
      exitstudentButton.config(state=DISABLED)
    

      root.destroy()
      import cours_trimestre3_anne1_science_examen



def choix_event():
      print("hello")

def trimestre1_anne1_science():
      global stuation,examen,interrogation
      stuation =Button(frame_generale,text='SITUATION ',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre1_anne1_science_stuation)
      stuation.place(x=700,y=58)
      examen =Button(frame_generale,text='EXAMINTION ',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre1_anne1_science_examen)
      examen.place(x=700,y=147)
      interrogation =Button(frame_generale,text='INTERROGATION',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre1_anne1_science_interrogation)
      interrogation.place(x=700,y=236)


def trimestre2_anne1_science():
      global stuation,examen,interrogation
      stuation =Button(frame_generale,text='SITUATION ',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre2_anne1_science_situation)
      stuation.place(x=700,y=58)
      examen =Button(frame_generale,text='EXAMINTION ',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre2_anne1_science_examen)
      examen.place(x=700,y=147)
      interrogation =Button(frame_generale,text='INTERROGATION',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre2_anne1_science_interrogation)
      interrogation.place(x=700,y=236)


def trimestre3_anne1_science():
      global stuation,examen,interrogation
      stuation =Button(frame_generale,text='SITUATION ',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre3_anne1_science_situation)
      stuation.place(x=700,y=58)
      examen =Button(frame_generale,text='EXAMINTION ',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre3_anne1_science_examen)
      examen.place(x=700,y=147)
      interrogation =Button(frame_generale,text='INTERROGATION',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre3_anne1_science_interrogation)
      interrogation.place(x=700,y=236)

def trimestre1_anne2_science():
      global stuation,examen,interrogation
      stuation =Button(frame_generale,text='SITUATION ',font=("times new romain",12,'bold'),width=15,height=4)
      stuation.place(x=700,y=58)
      examen =Button(frame_generale,text='EXAMINTION ',font=("times new romain",12,'bold'),width=15,height=4)
      examen.place(x=700,y=147)
      interrogation =Button(frame_generale,text='INTERROGATION',font=("times new romain",12,'bold'),width=15,height=4)
      interrogation.place(x=700,y=236)

def trimestre2_anne2_science():
      global stuation,examen,interrogation
      stuation =Button(frame_generale,text='SITUATION ',font=("times new romain",12,'bold'),width=15,height=4)
      stuation.place(x=700,y=58)
      examen =Button(frame_generale,text='EXAMINTION ',font=("times new romain",12,'bold'),width=15,height=4)
      examen.place(x=700,y=147)
      interrogation =Button(frame_generale,text='INTERROGATION',font=("times new romain",12,'bold'),width=15,height=4)
      interrogation.place(x=700,y=236)

def trimestre3_anne2_science():
      global stuation,examen,interrogation
      stuation =Button(frame_generale,text='SITUATION ',font=("times new romain",12,'bold'),width=15,height=4)
      stuation.place(x=700,y=58)
      examen =Button(frame_generale,text='EXAMINTION ',font=("times new romain",12,'bold'),width=15,height=4)
      examen.place(x=700,y=147)
      interrogation =Button(frame_generale,text='INTERROGATION',font=("times new romain",12,'bold'),width=15,height=4)
      interrogation.place(x=700,y=236)








def premier_anne_science():
     global fisrt
     fisrt =Button(frame_generale,text='First',font=("times new romain",12,'bold'),width=15,height=2,command=anne1_scolaire_science)
     fisrt.place(x=161,y=0)
     Label_canvas = Canvas(frame_generale,width=1000,height=5.0,bg="#1220a0",highlightthickness=0)
     Label_canvas.place(x=160,y=52)

     pda.config(state=DISABLED)
     mp.config(state=DISABLED)
     bc.config(state=DISABLED)
     lng.config(state=DISABLED)
     ssh_s.config(state=DISABLED)
     
 
    



def math_physique():
       global mp2,mp3
       mp2 =Button(frame_generale,text='2nd',font=("times new romain",12,'bold'),width=15,height=1,command=mp_anne_scolaire)
       mp2.place(x=161,y=57)
       mp3 =Button(frame_generale,text='3th',font=("times new romain",12,'bold'),width=15,height=1,command=mp_anne_scolaire)
       mp3.place(x=161,y=107)
       Label_canvas = Canvas(frame_generale,width=1000,height=5.0,bg="#6c09c3",highlightthickness=0)
       Label_canvas.place(x=160,y=140)

       science.config(state=DISABLED)
       pda.config(state=DISABLED)
       bc.config(state=DISABLED)
       lng.config(state=DISABLED)
       ssh_s.config(state=DISABLED)

    

def bio_chimie():
     global bc2,bc3
     bc2 =Button(frame_generale,text='2nde',font=("times new romain",12,'bold'),width=15,height=1,command=bc_anne_scolaire)
     bc2.place(x=161,y=144)
     bc3 =Button(frame_generale,text='3th',font=("times new romain",12,'bold'),width=15,height=1,command=bc_anne_scolaire)
     bc3.place(x=161,y=192)
     Label_canvas = Canvas(frame_generale,width=1000,height=5.0,bg="#6c09c3",highlightthickness=0)
     Label_canvas.place(x=160,y=140)

     science.config(state=DISABLED)
     mp.config(state=DISABLED)
     pda.config(state=DISABLED)
     lng.config(state=DISABLED)
     ssh_s.config(state=DISABLED)
    


def langue():
      global lng1,lng2,lng3    
      lng1 =Button(frame_generale,text='Fisrt',font=("times new romain",12,'bold'),width=15,height=1,command=lng_anne_scolaire)
      lng1.place(x=161,y=229)
      lng2 =Button(frame_generale,text='2nd',font=("times new romain",12,'bold'),width=15,height=1,command=lng_anne_scolaire)
      lng2.place(x=161,y=262)
      lng3 =Button(frame_generale,text='3th',font=("times new romain",12,'bold'),width=15,height=1,command=lng_anne_scolaire)
      lng3.place(x=161,y=295)
      Label_canvas = Canvas(frame_generale,width=1000,height=5.0,bg="#472f02",highlightthickness=0)
      Label_canvas.place(x=160,y=327)

      science.config(state=DISABLED)
      mp.config(state=DISABLED)
      bc.config(state=DISABLED)
      pda.config(state=DISABLED)
      ssh_s.config(state=DISABLED)
    

def ssh():
      global ssh1,ssh2,ssh3
      ssh1 =Button(frame_generale,text='Fisrt',font=("times new romain",12,'bold'),width=15,height=1,command=ssh_anne_scolaire)
      ssh1.place(x=161,y=332)
      ssh2 =Button(frame_generale,text='2nd',font=("times new romain",12,'bold'),width=15,height=1,command=ssh_anne_scolaire)
      ssh2.place(x=161,y=365)
      ssh3 =Button(frame_generale,text='3th',font=("times new romain",12,'bold'),width=15,height=1,command=ssh_anne_scolaire)
      ssh3.place(x=161,y=398)
      Label_canvas = Canvas(frame_generale,width=1000,height=5.0,bg="#023502",highlightthickness=0)
      Label_canvas.place(x=160,y=430)

      science.config(state=DISABLED)
      mp.config(state=DISABLED)
      bc.config(state=DISABLED)
      lng.config(state=DISABLED)
      pda.config(state=DISABLED)
    

def pedagogie():
    global pda1,peda2,peda3,peda4
    pda1 =Button(frame_generale,text='Fisrt',font=("times new romain",12,'bold'),width=15,height=1,command=pda_anne_scolaire)
    pda1.place(x=161,y=435)
    peda2 =Button(frame_generale,text='2nd',font=("times new romain",12,'bold'),width=15,height=1,command=pda_anne_scolaire)
    peda2.place(x=161,y=468)
    peda3 =Button(frame_generale,text='3th',font=("times new romain",12,'bold'),width=15,height=1,command=pda_anne_scolaire)
    peda3.place(x=161,y=501)
    peda4 =Button(frame_generale,text='4th',font=("times new romain",12,'bold'),width=15,height=1,command=pda_anne_scolaire)
    peda4.place(x=161,y=534)


    science.config(state=DISABLED)
    mp.config(state=DISABLED)
    bc.config(state=DISABLED)
    lng.config(state=DISABLED)
    ssh_s.config(state=DISABLED)
    


def anne1_partie_science():
      global parie1,parie3,parie2
      parie1 =Button(frame_generale,text='1ERE TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre1_anne1_science)
      parie1.place(x=480,y=58)
      parie2 =Button(frame_generale,text='2EME TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre2_anne1_science)
      parie2.place(x=480,y=147)
      parie3 =Button(frame_generale,text='3EME-TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre3_anne1_science)
      parie3.place(x=480,y=236)
      anne1.config(state=DISABLED)
      anne2.config(state=DISABLED)
      fisrt.config(state=DISABLED)

def anne2_partie_science():
      global parie1,parie3,parie2
      parie1 =Button(frame_generale,text='1ERE TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre1_anne2_science)
      parie1.place(x=480,y=58)
      parie2 =Button(frame_generale,text='2EME TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre2_anne2_science)
      parie2.place(x=480,y=147)
      parie3 =Button(frame_generale,text='3EME-TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4,command=trimestre3_anne2_science)
      parie3.place(x=480,y=236)
      anne1.config(state=DISABLED)
      anne2.config(state=DISABLED)
      fisrt.config(state=DISABLED)

def anne1_scolaire_science():
       global anne1,anne2
       science.config(state=DISABLED)
       bc.config(state=DISABLED)
       mp.config(state=DISABLED)
       lng.config(state=DISABLED)
       ssh_s.config(state=DISABLED)
       pda.config(state=DISABLED)
       mp.config(state=DISABLED)
       anne1=Button(frame_generale,text='2022-2023',font=("times new romain",12,'bold'),width=15,height=1,command=anne1_partie_science)
       anne1.place(x=321,y=58)
       anne2=Button(frame_generale,text='2023-2024',font=("times new romain",12,'bold'),width=15,height=1,command=anne2_partie_science)
       anne2.place(x=321,y=90)
      
def mp_anne_partie():
      global parie1,parie3,parie2
      parie1 =Button(frame_generale,text='1ERE TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie1.place(x=480,y=58)
      parie2 =Button(frame_generale,text='2EME TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie2.place(x=480,y=147)
      parie3 =Button(frame_generale,text='3EME-TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie3.place(x=480,y=236)
      mp2.config(state=DISABLED)
      mp3.config(state=DISABLED)
      anne1.config(state=DISABLED)
      anne2.config(state=DISABLED)

def mp_anne_scolaire():
       global anne1,anne2
       science.config(state=DISABLED)
       bc.config(state=DISABLED)
       mp.config(state=DISABLED)
       lng.config(state=DISABLED)
       ssh_s.config(state=DISABLED)
       pda.config(state=DISABLED)
       mp.config(state=DISABLED)
       anne1=Button(frame_generale,text='2022-2023',font=("times new romain",12,'bold'),width=15,height=1)
       anne1.place(x=321,y=58)
       anne2=Button(frame_generale,text='2023-2024',font=("times new romain",12,'bold'),width=15,height=1)
       anne2.place(x=321,y=90)

def bc_anne_partie():
      global parie1,parie3,parie2
      parie1 =Button(frame_generale,text='1ERE TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie1.place(x=480,y=58)
      parie2 =Button(frame_generale,text='2EME TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie2.place(x=480,y=147)
      parie3 =Button(frame_generale,text='3EME-TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie3.place(x=480,y=236)
      bc2.config(state=DISABLED)
      bc3.config(state=DISABLED)
      anne1.config(state=DISABLED)
      anne2.config(state=DISABLED)

def bc_anne_scolaire():
       global anne1,anne2
       science.config(state=DISABLED)
       bc.config(state=DISABLED)
       mp.config(state=DISABLED)
       lng.config(state=DISABLED)
       ssh_s.config(state=DISABLED)
       pda.config(state=DISABLED)
       mp.config(state=DISABLED)
       anne1=Button(frame_generale,text='2022-2023',font=("times new romain",12,'bold'),width=15,height=1)
       anne1.place(x=321,y=58)
       anne2=Button(frame_generale,text='2023-2024',font=("times new romain",12,'bold'),width=15,height=1)
       anne2.place(x=321,y=90)

def lng_anne_partie():
      global parie1,parie3,parie2
      parie1 =Button(frame_generale,text='1ERE TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie1.place(x=480,y=58)
      parie2 =Button(frame_generale,text='2EME TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie2.place(x=480,y=147)
      parie3 =Button(frame_generale,text='3EME-TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie3.place(x=480,y=236)
      lng1.config(state=DISABLED)
      lng2.config(state=DISABLED)
      lng3.config(state=DISABLED)
      anne1.config(state=DISABLED)
      anne2.config(state=DISABLED)

def lng_anne_scolaire():
       global anne1,anne2
       science.config(state=DISABLED)
       bc.config(state=DISABLED)
       mp.config(state=DISABLED)
       lng.config(state=DISABLED)
       ssh_s.config(state=DISABLED)
       pda.config(state=DISABLED)
       mp.config(state=DISABLED)
       anne1=Button(frame_generale,text='2022-2023',font=("times new romain",12,'bold'),width=15,height=1)
       anne1.place(x=321,y=58)
       anne2=Button(frame_generale,text='2023-2024',font=("times new romain",12,'bold'),width=15,height=1)
       anne2.place(x=321,y=90)
      

def ssh_anne_partie():
      global parie1,parie3,parie2
      parie1 =Button(frame_generale,text='1ERE TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie1.place(x=480,y=58)
      parie2 =Button(frame_generale,text='2EME TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie2.place(x=480,y=147)
      parie3 =Button(frame_generale,text='3EME-TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie3.place(x=480,y=236)
      ssh1.config(state=DISABLED)
      ssh2.config(state=DISABLED)
      ssh3.config(state=DISABLED)
      anne1.config(state=DISABLED)
      anne2.config(state=DISABLED)

def ssh_anne_scolaire():
       global anne1,anne2
       science.config(state=DISABLED)
       bc.config(state=DISABLED)
       mp.config(state=DISABLED)
       lng.config(state=DISABLED)
       ssh_s.config(state=DISABLED)
       pda.config(state=DISABLED)
       mp.config(state=DISABLED)
       anne1=Button(frame_generale,text='2022-2023',font=("times new romain",12,'bold'),width=15,height=1,command=ssh_anne_partie)
       anne1.place(x=321,y=58)
       anne2=Button(frame_generale,text='2023-2024',font=("times new romain",12,'bold'),width=15,height=1,command=ssh_anne_partie)
       anne2.place(x=321,y=90)

def pda_anne_partie():
      global parie1,parie3,parie2
      parie1 =Button(frame_generale,text='1ERE TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie1.place(x=480,y=58)
      parie2 =Button(frame_generale,text='2EME TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie2.place(x=480,y=147)
      parie3 =Button(frame_generale,text='3EME-TRIMESTRE',font=("times new romain",12,'bold'),width=15,height=4)
      parie3.place(x=480,y=236)
      pda1.config(state=DISABLED)
      peda2.config(state=DISABLED)
      peda3.config(state=DISABLED)
      peda4.config(state=DISABLED)
      anne1.config(state=DISABLED)
      anne2.config(state=DISABLED)
      

def pda_anne_scolaire():
       global anne1,anne2
       science.config(state=DISABLED)
       bc.config(state=DISABLED)
       mp.config(state=DISABLED)
       lng.config(state=DISABLED)
       ssh_s.config(state=DISABLED)
       pda.config(state=DISABLED)
       mp.config(state=DISABLED)
       anne1=Button(frame_generale,text='2022-2023',font=("times new romain",12,'bold'),width=15,height=1,command=pda_anne_partie)
       anne1.place(x=321,y=58)
       anne2=Button(frame_generale,text='2023-2024',font=("times new romain",12,'bold'),width=15,height=1,command=pda_anne_partie)
       anne2.place(x=321,y=90)
           
      
      
      

 
       
       
      

  



def add_all():
    screen =Toplevel()
    screen.title('ADD ALL')
    screen.grab_set()
    screen.resizable(False,False)


    idLabel =Label(screen,text='SCIENCE 1ere',font=("times new romain",12,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    idEntry.grid(row=0,column=1,padx=15,pady=10)

    nameLabel =Label(screen,text='MATHS-PHYSIQUE',font=("time new romain",12,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=15,pady=10)


    phoneLabel =Label(screen,text='BIO-CHIMIE',font=("time new romain",12,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,padx=15,pady=10)

    emailLabel =Label(screen,text='LANGUE',font=("time new romain",12,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    emailEntry.grid(row=3,column=1,padx=15,pady=10)

    adressLabel =Label(screen,text='SSH',font=("time new romain",12,'bold'))
    adressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    adressEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    adressEntry.grid(row=4,column=1,padx=15,pady=10)

    genderLabel =Label(screen,text='PEDAGOGIE',font=("time new romain",12,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry =Entry(screen,font=("roman",12,'bold'),width=24)
    genderEntry.grid(row=5,column=1,padx=15,pady=10)


    add_all_event =ttk.Button(screen,text="ADD ALL")
    add_all_event.grid(row=6,columnspan=4)
    add_news =ttk.Button(screen,text="ADD NEWS")
    add_news.grid(row=7,columnspan=4)

   


    




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


s="SELECT WHAT YOU WANT TO VISIT :"
sliderLabel = Label(root,text=s,font=("arial",28,"bold"))
sliderLabel.place(x=280,y=50)
slider()
Label_canvas = Canvas(root,width=1015,height=5.0,bg="#00eeff",highlightthickness=0)
Label_canvas.place(x=5,y=115)



frame_generale=Frame(root,bg='#040405')
frame_generale.place(x=5,y=120,width=1015,height=650)

Label_canvas = Canvas(frame_generale,width=160,height=5.0,bg="#1220a0",highlightthickness=0)
Label_canvas.place(x=0,y=89)

Label_canvas = Canvas(frame_generale,width=160,height=5.0,bg="#6c09c3",highlightthickness=0)
Label_canvas.place(x=0,y=184)


Label_canvas = Canvas(frame_generale,width=160,height=5.0,bg="#454403",highlightthickness=0)
Label_canvas.place(x=0,y=278)


Label_canvas = Canvas(frame_generale,width=160,height=5.0,bg="#472f02",highlightthickness=0)
Label_canvas.place(x=0,y=372)


Label_canvas = Canvas(frame_generale,width=160,height=5.0,bg="#023502",highlightthickness=0)
Label_canvas.place(x=0,y=467)


Label_canvas = Canvas(frame_generale,width=160,height=5.0,bg="#00eeff",highlightthickness=0)
Label_canvas.place(x=0,y=580)
Label_canvas = Canvas(frame_generale,width=1000,height=20.0,bg="#00eeff",highlightthickness=0)
Label_canvas.place(x=160,y=566)



science =Button(frame_generale,text='SCIENCE 1ere',font=("times new romain",12,'bold'),width=15,height=4,command=premier_anne_science)
science.place(x=0,y=0)


mp =Button(frame_generale,text='MATHS-PHYSIQUE',font=("times new romain",12,'bold'),width=15,height=4,command=math_physique)
mp.place(x=0,y=94)


bc =Button(frame_generale,text='BIO-CHIMIE',font=("times new romain",12,'bold'),width=15,height=4,command=bio_chimie)
bc.place(x=0,y=188)


lng =Button(frame_generale,text='LANGUE',font=("times new romain",12,'bold'),width=15,height=4,command=langue)
lng.place(x=0,y=282)


ssh_s =Button(frame_generale,text='SSH',font=("times new romain",12,'bold'),width=15,height=4,command=ssh)
ssh_s.place(x=0,y=377)

pda =Button(frame_generale,text='PEDAGOGIE',font=("times new romain",12,'bold'),width=15,height=5,command=pedagogie)
pda.place(x=0,y=472)






def searchfonction_for_admin():
      messagebox.showinfo("HELLO","COMMING SOON",parent=root)

def exportfonction_for_admin():
      messagebox.showinfo("HELLO","COMMING SOON",parent=root)






searchstudentButton =ttk.Button(root,text="Search",command=searchfonction_for_admin)
searchstudentButton.place(x=5,y=70)

exportstudentButton =ttk.Button(root,text="Export File",command=exportfonction_for_admin)
exportstudentButton.place(x=70,y=70)

exitstudentButton =ttk.Button(root,text="Exit Here",command=exit)
exitstudentButton.place(x=150,y=70)









root.mainloop()