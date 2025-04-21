import tkinter as tk
from tkinter import messagebox
import os

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("800x500")
        self.root.configure() # for background color

        title = tk.Label(root, text="Admin dahboard", font=("Arial", 20))
        title.pack(pady=20)

        tk.Button(root, text="Manage Users", command=self.manage_users).pack(pady=10)
        tk.Button(root, text="Manage Courses", command=self.manage_courses).pack(pady=10)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    def manage_users(self):

        # self.clear_window()
        messagebox.showinfo("Manage Users", "This feature is under development.")

    def manage_courses(self):

        # self.clear_window()
        messagebox.showinfo("Manage Courses", "This feature is under development.")

    def exit(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminDashboard(root)
    root.mainloop()

