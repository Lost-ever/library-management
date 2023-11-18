import mysql.connector as mysql
import tkinter as tk
import webbrowser
from tkinter import font,YES,BOTH
from PIL import Image , ImageTk
import os

app_icon = r"G:\Windows10Upgrade\cs class 12 project\app_icon.ico"
app_back = r"G:\Windows10Upgrade\cs class 12 project\back_img1.png"

def resize_image(event):
    image = copy_of_image.resize((winwidth , winheight))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo

def menu_screen():
    try:
        '''#host = host_text.get('1.0', 'end-1c')
        user = user_text.get('1.0', 'end-1c')
        password = pass_text.get('1.0', 'end-1c')'''
        lib_database = mysql.connect(host="localhost", user="root", passwd="root", database="library_data")
        lib_database._execute_query("create table book(bno integer primary key, bookname varchar(30) , price integer );")
        lib_database.commit()
        
    except mysql.errors.InterfaceError:
        print("you want to install mysql!")
        webbrowser.open_new("https://dev.mysql.com/downloads/installer/")

    except:
        pass
    menu_frame = tk.Frame(main_win , width=winwidth-100 , height=winheight-100 , background="white" , highlightbackground="black" , highlightthickness=5)
    menu_frame.place(x=50 , y=50)
    left_frame.destroy()
    menu_frame.tkraise()
    admin_button = tk.Button(menu_frame , width=50 , height=3 , text='Admin')
    books_button = tk.Button(menu_frame , width=50 , height=3 , text="Books")
    #buttons widget
    admin_button.place(x=500 , y=100)
    

main_win = tk.Tk("OUR LIBRARY")
winheight = main_win.winfo_screenheight()
winwidth = main_win.winfo_screenwidth()
main_win.geometry(f"{winwidth}x{winheight}")
image = Image.open(app_back)
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = tk.Label(main_win, image = photo)
label.bind('<Configure>', resize_image(main_win))
label.pack(fill=BOTH, expand = YES)
left_frame = tk.Frame(main_win , width=520 , height=500 , highlightbackground="black" , highlightthickness=5)
left_frame.place(x=400 , y= 90)
main_win.iconbitmap(app_icon)
main_win.title("OUR LIBRARY")
user_text = tk.Entry(left_frame , width=40 , font=("system" , "17"))
pass_text = tk.Entry(left_frame , width=40 , font=("system" , "17"))
sign_button = tk.Button(left_frame , text="Sign-in" , width=20 , height=2 , command= menu_screen , font=("system" , "7"))
main_label = tk.Label(left_frame , text="OUR LIBRARY" , width=20 , height=4 , font=("system" , "20") , anchor="center")
user_label = tk.Label(left_frame , text="Username" , width=50 , height=1 , font=("system" , "5") , anchor="w")
pass_label = tk.Label(left_frame , text="password" , width=50 , height=1 , font=("system" , "5") , anchor="w")
#text widget
user_text.place(x=70 , y=210)
pass_text.place(x=70 , y=280)
#label widget
main_label.place(x=80 , y=40)
user_label.place(x=70 , y=180)
pass_label.place(x=70 , y=250)
sign_button.place(x=160 , y=350)
main_win.mainloop(0)

def Book_entry():
    pass
