import tkinter as tk
from tkinter import messagebox
import customtkinter
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

app= customtkinter.CTk()
app.title('Login')
app.geometry('450x360')
app.config(bg='#001220')

font1=('Helvetica', 25, 'bold')
font2=('Arial', 17, 'bold')
font3=('Arial', 13, 'bold')
font4=('Arial', 13, 'bold','underline')
conn=sqlite3.connect('data.db')
cursor=conn.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
              username TEXT NOT NULL,
              password TEXT NOT NULL)''' )

def signup():
    username = username_entry.get()
    password = password_entry.get()
    if username!= '' and password !='':
        cursor.execute('SELECT username FROM users WHERE username=?', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('Error', 'Username already exists')

        else:
            encoded_password =password.encode('utf-8')
            hashed_password =bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            #print(hashed_password)
            cursor.execute('INSERT INTO users VALUES (?, ?)', [username,hashed_password])
            conn.commit()
            messagebox.showinfo('Success', 'Account has been created.')
    else:
        messagebox.showerror('Error', 'Enter all data!')


def login_account():
    username = username_entry2.get()
    password = password_entry2.get()
    if username!= '' and password !='':
        cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result=cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                messagebox.showinfo('Success', 'Logged in successfully')
            else:
                messagebox.showerror('Error', 'Invalid password')
        else:
            messagebox.showerror('Error', 'Invalid Username')
    else:
        messagebox.showerror('Error', 'Enter all data!')        

def login():
    frame1.destroy()
    frame2=customtkinter.CTkFrame(app, bg_color='#001220',fg_color='#001220', width=470, height=360)
    frame2.place(x=0, y=0)

    image1=PhotoImage(file="1.png")
    image1_label= Label(frame2, image=image1, bg='#001220')
    image1_label.place(x=0, y=0)
    frame2.image1=image1

    login_label2 = customtkinter.CTkLabel(frame2, font=font3, text='Log in',text_color='#fff', bg_color='#001220')
    login_label2.place(x=280, y=20)

    global username_entry2
    global password_entry2

    username_entry2 = customtkinter.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='User Name', placeholder_text_color='#a3a3a3', width=200, height=50)
    username_entry2.place(x=230, y=80)

    password_entry2 = customtkinter.CTkEntry(frame2, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200, height=50)
    password_entry2.place(x=230, y=150)

    login_button2= customtkinter.CTkButton(frame2,command=login_account, font=font4, text='Login',text_color='#fff', bg_color='#001220')
    login_button2.place(x=305, y=250)

frame1=customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=470, height=360)
frame1.place(x=0, y=0)

image1=PhotoImage(file="ja.png")
image1_label= Label(frame1, image=image1, bg='#001220')
image1_label.place(x=0, y=0)

signup_label = customtkinter.CTkLabel(frame1, font=font1, text='Sign up',text_color='#fff', bg_color='#001220')
signup_label.place(x=280, y=20)

username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Username', placeholder_text_color='#a3a3a3', width=200, height=50)
username_entry.place(x=230, y=80)

password_entry = customtkinter.CTkEntry(frame1, font=font2, show='*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Password', placeholder_text_color='#a3a3a3', width=200, height=50)
password_entry.place(x=230, y=150)


signup_button=customtkinter.CTkButton(frame1,command=signup, font=font2, text_color='#fff', text='Sign up', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=120)
signup_button.place(x=230, y=230)

login_label = customtkinter.CTkLabel(frame1, font=font3, text='Already have an account',text_color='#fff', bg_color='#001220')
login_label.place(x=230, y=280)

login_button= customtkinter.CTkButton(frame1, command=login, font=font4, text='Login',text_color='#fff', bg_color='#001220')
login_button.place(x=230, y=320)

# Initialize main window
root = tk.Tk()
root.title("Volunteer Management System")

# Volunteer list
volunteers = []

# Functions
def add_volunteer():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()

    if name and email and phone:
        volunteer = {"Name": name, "Email": email, "Phone": phone}
        volunteers.append(volunteer)
        update_volunteer_list()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "All fields are required.")

def update_volunteer_list():
    listbox_volunteers.delete(0, tk.END)
    for volunteer in volunteers:
        listbox_volunteers.insert(tk.END, f"Name: {volunteer['Name']}, Email: {volunteer['Email']}, Phone: {volunteer['Phone']}")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def delete_volunteer():
    selected_index = listbox_volunteers.curselection()
    if selected_index:
        volunteers.pop(selected_index[0])
        update_volunteer_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a volunteer to delete.")

# GUI Layout
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Email:").grid(row=1, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame)
entry_email.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Phone:").grid(row=2, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame)
entry_phone.grid(row=2, column=1, padx=5, pady=5)

btn_add = tk.Button(frame, text="Add Volunteer", command=add_volunteer)
btn_add.grid(row=3, column=0, columnspan=2, pady=10)

listbox_volunteers = tk.Listbox(root, width=50)
listbox_volunteers.pack(pady=20)

btn_delete = tk.Button(root, text="Delete Volunteer", command=delete_volunteer)
btn_delete.pack(pady=10)

# Run the application
root.mainloop()

app.mainloop()