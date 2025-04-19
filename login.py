import tkinter as tk
from tkinter import messagebox

def login_window():

    title = tk.Label(root, text="Student Profile Management System", font=("Arial", 14))
    title.pack(pady=20)

    tk.Label(root, text="Username", font=("Arial", 10)).pack(pady=10)
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password", font=("Arial", 10)).pack(pady=10)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    
    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        try:

            with open("password.txt", "r") as file:
                for line in file:
                    saved_username, saved_password = [item.strip() for item in line.strip().split(",")] 

                    if username == saved_username and password == saved_password:
                        messagebox.showinfo("Login Sucessful",f"Welome {username}! \n ")
                        return
                    
                messagebox.showerror("Login Failed", "Invalid username or password")
                    
        except FileNotFoundError:
            messagebox.showerror("Error", "User data file not found.")


    tk.Button(root, text="Login", command=login).pack(pady=10)
    tk.Button(root, text="Create Account").pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    

# creating login window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x400")
root.configure() # for background color

login_window()

root.mainloop()    

