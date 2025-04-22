import tkinter as tk
from tkinter import messagebox
import os

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("600x400")
        self.root.configure() # for background color

        self.show_dashboard() # clal this to show the main screen

    def show_dashboard(self):
        self.clear_window()

        title = tk.Label(root, text="Admin dahboard", font=("Arial", 20))
        title.pack(pady=20)

        tk.Button(root, text="Manage Users", command=self.manage_users).pack(pady=10)
        tk.Button(root, text="Manage Courses", command=self.manage_courses).pack(pady=10)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def manage_users(self):

        self.clear_window()
        
        tk.Label(self.root, text="Manage Users", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="View Users", command=self.view_users).pack(pady=10)
        tk.Button(self.root, text="Add User", command=self.add_user).pack(pady=10)
        tk.Button(self.root, text="Update User", command=self.update_user).pack(pady=10)
        tk.Button(self.root, text="Delete User", command=self.delete_user).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_dashboard).pack(pady=10) # back button to go back to the dashboard


    def manage_courses(self):

        # self.clear_window()
        messagebox.showinfo("Manage Courses", "This feature is under development.")

    def exit(self):
        self.root.quit()


    def view_users(self):
        messagebox.showinfo("View Users", "This feature is under development.")

    def add_user(self):
        messagebox.showinfo("Add User", "This feature is under development.")

    def update_user(self):
        messagebox.showinfo("Update User", "This feature s under development.")

    def delete_user(self):
        messagebox.showinfo("Delete User", "This feature is under development.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminDashboard(root)
    root.mainloop()

