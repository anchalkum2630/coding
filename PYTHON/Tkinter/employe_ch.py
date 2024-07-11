import tkinter as tk
from tkinter import messagebox

class EmployeeManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Management System")

        self.employees = []

        self.label = tk.Label(master, text="Employee Name:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=30)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(master, text="Add Employee", command=self.add_employee)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(master, text="View Employees", command=self.view_employees)
        self.view_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete Employee", command=self.delete_employee)
        self.delete_button.pack(pady=5)

        self.listbox = tk.Listbox(master, width=40)
        self.listbox.pack(pady=10)

    def add_employee(self):
        employee_name = self.entry.get()
        if employee_name:
            self.employees.append(employee_name)
            self.listbox.insert(tk.END, employee_name)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an employee name.")

    def view_employees(self):
        if self.employees:
            messagebox.showinfo("Employees", "\n".join(self.employees))
        else:
            messagebox.showinfo("Employees", "No employees added yet.")

    def delete_employee(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            employee_name = self.listbox.get(index)
            self.listbox.delete(index)
            self.employees.remove(employee_name)
        else:
            messagebox.showwarning("Warning", "Please select an employee to delete.")

root = tk.Tk()
root.geometry("400x400")
app = EmployeeManagementApp(root)
root.mainloop()
