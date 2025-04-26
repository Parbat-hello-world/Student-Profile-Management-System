import tkinter as tk
from tkinter import messagebox

def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()

def show_update_user_screen(root, clear_window, manage_users):
    clear_window(root)
    root.geometry("600x400")

    # Make these variables global so they can be accessed by other functions
    global search_entry, details_frame, username_entry, fullname_entry, password_entry, confirm_password_entry, role_var
    
    tk.Label(root, text="Update User", font=("Arial", 14)).pack(pady=20)

    # Search Frame 
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)

    tk.Label(search_frame, text="Search Username:").pack(side=tk.LEFT, padx=5)
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=5)

    tk.Button(search_frame, text="Search", command=lambda: search_user(search_entry.get(), details_frame, manage_users)).pack(side=tk.LEFT)

    # User Details Frame
    details_frame = tk.Frame(root)
    details_frame.pack(pady=10)

    # Initialize variables
    username_entry = None 
    fullname_entry = None
    password_entry = None
    confirm_password_entry = None
    role_var = None

def search_user(username, details_frame, manage_users):
    username = username.strip()

    if not username:
        messagebox.showerror("Error", "Please enter a username.")
        return

    try: # check if user exists
        user_found = False
        user_data = {}

        with open("data/users.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == username:
                    user_data = {
                        "username": data[0],
                        "fullname": data[1],
                        "role": data[2]
                    }
                    user_found = True
                    break

        if not user_found:
            messagebox.showerror("Error", "User not found.")
            return
        
        password = ""
        try:
            with open("data/password.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if data[0] == username:
                        password = data[1] if len(data) > 1 else ""
                        break
        except FileNotFoundError:
            messagebox.showerror("Error", "Password file not found.")
            return

        # display user details form
        show_user_form(user_data, password, details_frame, manage_users)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def show_user_form(user_data, password, details_frame, manage_users):
    # clear previous widgets
    for widget in details_frame.winfo_children():
        widget.destroy()

    # Make these variables global
    global fullname_entry, password_entry, confirm_password_entry, role_var
    
    # Username (display only, shouldn't be changed)
    tk.Label(details_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(details_frame, text=user_data["username"]).grid(row=0, column=1, padx=5, pady=5)
    
    # Fullname
    tk.Label(details_frame, text="Fullname:").grid(row=1, column=0, padx=5, pady=5)
    fullname_entry = tk.Entry(details_frame)
    fullname_entry.insert(0, user_data["fullname"])
    fullname_entry.grid(row=1, column=1, sticky="w")

    # Password
    tk.Label(details_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
    password_entry = tk.Entry(details_frame, show="*")
    password_entry.insert(0, password)
    password_entry.grid(row=2, column=1, sticky="w")

    # confirm password
    tk.Label(details_frame, text="Confirm Password:").grid(row=3, column=0, padx=5, pady=5)
    confirm_password_entry = tk.Entry(details_frame, show="*")
    confirm_password_entry.insert(0, password)
    confirm_password_entry.grid(row=3, column=1, sticky="w")

    # Role
    tk.Label(details_frame, text="Role:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    role_var = tk.StringVar(value=user_data["role"])
    tk.Radiobutton(details_frame, text="Admin", variable=role_var, value="admin").grid(row=4, column=1, sticky="w")
    tk.Radiobutton(details_frame, text="Student", variable=role_var, value="student").grid(row=5, column=1, sticky="w")

    # Update button
    tk.Button(details_frame, text="Update", 
              command=lambda: save_user_changes(user_data["username"], fullname_entry.get(), 
                                              password_entry.get(), confirm_password_entry.get(), 
                                              role_var.get(), manage_users)).grid(row=6, columnspan=2, pady=10)

    tk.Button(details_frame, text="Back", command=manage_users).grid(row=7, columnspan=2)

def save_user_changes(original_username, fullname, password, confirm_password, role, manage_users):
    # validate inputs
    if not fullname or not password or not confirm_password or not role:
        messagebox.showerror("Error", "All fields are required.")
        return
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    try:
        # Update users.txt
        updated_users = []
        with open("data/users.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == original_username:
                    updated_users.append(f"{original_username},{fullname},{role}\n")
                else:
                    updated_users.append(line)

        with open("data/users.txt", "w") as file:
            file.writelines(updated_users)

        # Update password.txt
        if password:
            updated_passwords = []
            password_found = False

            try:
                with open("data/password.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        if data[0] == original_username:
                            updated_passwords.append(f"{original_username},{password}\n")
                            password_found = True
                        else:
                            updated_passwords.append(line)
            except FileNotFoundError:
                messagebox.showerror("Error", "Password file not found")
                return

            if not password_found:
                updated_passwords.append(f"{original_username},{password}\n")

            with open("data/password.txt", "w") as pass_file:
                pass_file.writelines(updated_passwords)

        messagebox.showinfo("Success", "User updated successfully.")
        manage_users()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")