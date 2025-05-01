import tkinter as tk
from tkinter import messagebox

def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()

def show_update_user_screen(root, call_back):
    clear_window(root) # this clear the main window

    root.geometry("600x400")

    tk.Label(root, text="Update User", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Enter username to update: ").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    fullname_var = tk.StringVar()
    role_var = tk.StringVar(value="Student")

    def fetch_user_data():
        username = username_entry.get().strip()
        if not username:
            messagebox.showerror("Error","Enter Username")
            return

        try:
            with open("data/users.txt","r") as file:
                users = file.readlines()

            user_found = False
            for line in users:
                data = line.strip().split(",")
                if data[0] == username:
                    user_found = True
                    fullname_var.set(data[1])
                    role_var.set(data[2])
                    break

            if not user_found:
                messagebox.showerror("Error", "User doesn't Exits.")
            
        except Exception as e:
            messagebox.showerror("Error",f"Error occured {e}")
            return

    def save_updates():
        username = username_entry.get().strip()
        new_fullname = fullname_var.get().strip()
        new_role = role_var.get().strip()

        if not username or not new_fullname or not new_role:
            messagebox.showerror("Error", "All fields must be filled.")
            return
        
        try:
            with open("data/users.txt", "r") as file:
                users = file.readlines()

            updated = False
            with open("data/users.txt", "w") as file:
                for line in users:
                    data = line.strip().split(",")
                    if data[0] == username:
                        file.write(f"{username},{new_fullname},{new_role}\n")
                        updated = True
                    else:
                        file.write(line)

            if updated:
                messagebox.showinfo("Sucess", "User updated Successfully.")

            else:
                messagebox.showinfo("Error", "User update failed")

        except Exception as e:
            messagebox.showerror("Error", f"Error saving changes: {e}")
            return

    tk.Button(root, text="Search User", command=fetch_user_data).pack(pady=10)

    tk.Label(root, text="Full Name").pack(pady=5)
    fullname_entry = tk.Entry(root, textvariable=fullname_var)
    fullname_entry.pack(pady=5)

    tk.Label(root, text="Role").pack(pady=5)
    tk.Radiobutton(root, text="Admin", variable=role_var, value="Admin").pack(pady=2)
    tk.Radiobutton(root, text="Student", variable=role_var, value="Student").pack(pady=2)


    tk.Button(root, text="Save Changes", command=save_updates).pack(pady=10)
    tk.Button(root, text="back", command=call_back).pack(pady=10)