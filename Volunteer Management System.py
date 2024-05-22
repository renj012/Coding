import tkinter as tk
from tkinter import messagebox

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
