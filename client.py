import socket
import threading
import tkinter 
import time
from tkinter import messagebox
import sqlite3

import tkinter.scrolledtext
from tkinter import simpledialog

HOST = '127.0.0.1'
PORT = 3000

class Client :
    def __init__(self,host,port):
        self.sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        self.sock.connect((host,port))

        msg = tkinter.Tk()
        msg.withdraw()
        connection = sqlite3.connect("school.db")
        mycursor = connection.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS sms (User TEXT,Message TEXT,Created_Date TEXT,Created_Time TEXT)")
        connection.commit()



        self.nickname = simpledialog.askstring("LPC KINYINYA","Please choose a nickname")
        if self.nickname=="":
            messagebox.showerror("ERROR","Please enter your username") 
            return
        else :
            connection = sqlite3.connect("school.db")
            mycursor = connection.cursor()
            check_user = 'SELECT * FROM userinfos WHERE Name = ?'
            mycursor.execute(check_user,[(self.nickname)])
            if not mycursor.fetchone():
                messagebox.showerror("ERROR","Username not exists")
                return
            else:
                messagebox.showinfo("SUCCESS",f"Welcome Prof {self.nickname}")
                pass 


        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target = self.gui_loop)
        receive_thread = threading.Thread(target = self.receive)

        connection = sqlite3.connect("school.db")
        mycursor = connection.cursor()

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.title("LPC KINYINYA")
        self.win.iconbitmap("iconapp.ico")
        self.win.geometry("500x600")
        self.win.resizable(False,False)
        self.win.configure(bg="lightgray") 
        connection = sqlite3.connect('school.db')
        mycursor = connection.cursor()
        get_all_from_sms_table = mycursor.execute('SELECT * FROM sms')
        chek_all_data_get = mycursor.fetchall()
        # self.current_sms = chek_all_data_get[0]
        # self.current_user = chek_all_data_get[1]
        self.chat_label=tkinter.Label(self.win,text="Chat Group Of Prof",bg="lightgray")
        self.chat_label.config(font=("Arial",12))
        self.chat_label.pack(padx=20,pady=5)
        self.text_area=tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20,pady=5)
        self.text_area.config(state="disabled")
        self.msg_label=tkinter.Label(self.win,text="Write Message",bg="lightgray")
        self.msg_label.config(font=("Arial",12))
        self.msg_label.pack(padx=20,pady=5)
        self.input_area = tkinter.Text(self.win , height = 3 )
        self.input_area.pack(padx=20,pady=5)
        self.send_button = tkinter.Button(self.win, text = 'Send' , command = self.write)
        self.send_button.config(font = ("Arial",12))
        self.send_button.pack(padx = 20 ,pady =5)
        for data_get in chek_all_data_get :
            self.current_user = data_get[0]
            self.current_sms = data_get[1]
            self.created_time = data_get[2]
            self.created_date = data_get[3]
            message = f"\n{self.current_user} : {self.current_sms}\t\t\t@{self.created_date} {self.created_time}\n"
            self.text_area.config(state = 'normal')
            self.text_area.insert('end',message)
            self.text_area.yview('end')
            self.text_area.config(state = 'disabled')
          
        self.gui_done = True
        self.win.protocol("WM_DELETE_WINDOW",self.stop)
        self.win.mainloop()


    def write(self):
        SMS = self.input_area.get('1.0' ,'end')
        USER = self.nickname
        date=time.strftime("%d/%m/%Y")
        currenttime=time.strftime("%H:%M:%S")
        message = f"\n{self.nickname} : {self.input_area.get('1.0' ,'end')}\t\t\t@{self.created_date} {self.created_time}\n" 
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete("1.0","end")
        connection = sqlite3.connect("school.db")
        mycursor = connection.cursor()
        check_user = 'SELECT * FROM userinfos WHERE Name = ?'
        mycursor.execute(check_user,[(self.nickname)])
        mycursor.execute("INSERT INTO sms (User,Message,Created_Date,Created_Time) VALUES (?,?,?,?)",(USER,SMS,currenttime,date))
        connection.commit()
        connection.close()





    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)



    def receive(self):
        while self.running :
            try :
                message = self.sock.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                else :
                    if self.gui_done :
                        self.text_area.config(state = 'normal')
                        self.text_area.insert('end',message)
                        self.text_area.yview('end')
                        self.text_area.config(state = 'disabled')
            except ConnectionAbortedError :
                break 

            except :
                print('error')
                self.sock.close()
                break


client = Client(HOST , PORT )

