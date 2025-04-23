import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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
        
        self.root.geometry("600x400")
        
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
        self.clear_window()
        self.root.geometry("800x600")
        tk.Label(self.root, text="View Users", font=("Arial", 14)).pack(pady=20)

        # Read and separate data from users.txt
        admins = []
        students = []

        try:
            with open("data/users.txt","r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 3:
                        if data[2] == "Admin":
                            admins.append(data)
                        elif data[2] == "Student":
                            students.append(data)

        except FileNotFoundError:
            messagebox.showerror("Error", "User data file not found.")
            return

        # Create admin table
        tk.Label(self.root, text="Admins", font=("Arial", 12)).pack(pady=5)

        admin_columns = ("sn", "username", "fullname", "role")
        admin_tree = ttk.Treeview(self.root, columns=admin_columns, show="headings", height=5)

        # headings
        admin_tree.heading("sn", text="SN")
        admin_tree.heading("username", text="Username")
        admin_tree.heading("fullname", text="Fullname")
        admin_tree.heading("role", text="Role")

        # columns size
        admin_tree.column("sn", width=40, anchor="center")
        admin_tree.column("username", width=120, anchor="w")
        admin_tree.column("fullname", width=180, anchor="w")
        admin_tree.column("role", width=80, anchor="center")

        for idx, admin in enumerate(admins, start=1):
            admin_tree.insert("", tk.END, values=(idx, *admin))
  
        admin_tree.pack(pady=5, padx=20, fill=tk.BOTH)
        
        # Add a scrollbar to the admin table


        # Create student table
        tk.Label(self.root, text="Students", font=("Arial", 12)).pack(pady=5)

        student_columns = ("sn", "username", "fullname", "role")
        student_tree = ttk.Treeview(self.root, columns=student_columns, show="headings", height=5)

        # set headings
        student_tree.heading("sn", text="SN")
        student_tree.heading("username", text="Username")
        student_tree.heading("fullname", text="Fullname")
        student_tree.heading("role", text="Role")

        # set columns size
        student_tree.column("sn", width=40, anchor="center")
        student_tree.column("username", width=120, anchor="w")
        student_tree.column("fullname", width=180, anchor="w")
        student_tree.column("role", width=80, anchor="center")

        for idx, student in enumerate(students, start=1):
            student_tree.insert("", tk.END, values=(idx, *student))
        
        student_tree.pack(pady=5, padx=20, fill=tk.BOTH)

        # Add a scrollbar to the student table


        tk.Button(self.root, text="Back", command=self.manage_users).pack(pady=10)

    def add_user(self):
        messagebox.showinfo("Add User", "This feature is under development.")

    def update_user(self):
        messagebox.showinfo("Update User", "This feature is under development.")

    def delete_user(self):
        messagebox.showinfo("Delete User", "This feature is under development.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminDashboard(root)
    root.mainloop()

