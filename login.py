import tkinter as tk
from tkinter import messagebox


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()



def login_window():

    clear_window() # clear the window before creating new widgets

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

            with open("data/password.txt", "r") as file:
                for line in file:
                    saved_username, saved_password = [item.strip() for item in line.strip().split(",")] 

                    if username == saved_username and password == saved_password:
                        messagebox.showinfo("Login Sucessful",f"Welcome {username}! \n ")
                        return
                    
                messagebox.showerror("Login Failed", "Invalid username or password")
                    
        except FileNotFoundError:
            messagebox.showerror("Error", "User data file not found.")

    tk.Button(root, text="Login", command=login).pack(pady=10)
    tk.Button(root, text="Create Account", command=create_account_window).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

def create_account_window():
        
    clear_window()

    tk.Label(root, text="Create Account", font=("Arial", 14)).pack(pady = 20) 
    
    tk.Label(root, text="Username").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Full Name").pack(pady=5)
    full_name_entry = tk.Entry(root)
    full_name_entry.pack()

    tk.Label(root, text="Password").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Label(root, text="Confirm Password").pack(pady=5)
    confirm_password_entry = tk.Entry(root, show="*")
    confirm_password_entry.pack()

    role_var = tk.StringVar(value="Student") # Default value
    tk.Label(root, text="Select Role").pack(pady=5)
    tk.Radiobutton(root, text="Student", value="Student", variable=role_var).pack()

    def create_account():
        username = username_entry.get().strip()
        full_name = full_name_entry.get().strip()
        password = password_entry.get().strip()
        confirm_password = confirm_password_entry.get().strip()
        role = role_var.get()

        if not username or not full_name or not password or not confirm_password or not role:
            messagebox.showerror("Error", "All fields are required.")

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # cjeclk if username already exists
        try:
            with open("data/users.txt", "r") as file:
                for line in file:
                    saved_username = line.strip().split(",")[0]
                    if username == saved_username:
                        messagebox.showerror("Error", "Username already exists", "Please choose a different username.")
                        return
        
        # if file donesn't exist,
        except FileNotFoundError:
            pass 

        try:
            with open("data/users.txt", "a") as user_file:
                user_file.write(f"{username},{full_name},{role}\n")
            
            with open("data/password.txt", "a") as pass_file:
                pass_file.write(f"{username},{password}\n")

            messagebox.showinfo("Success",f"Account Created for {username}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    tk.Button(root, text="Create Account", command=create_account).pack(pady=10)
    tk.Button(root, text="Back to Login", command=login_window).pack(pady=10)

# creating login window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x450")
root.configure() # for background color

login_window()

root.mainloop()    

