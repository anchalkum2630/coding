# import tkinter as tk

# def calculate_payment():
#     try:
#         loan_amount = float(loan_amount_entry.get())
#         interest_rate = float(interest_rate_entry.get()) / 100
#         loan_term = int(loan_term_entry.get())
#         monthly_interest_rate = interest_rate / 12
#         monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_term)
#         monthly_payment_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")
#     except ValueError:
#         monthly_payment_label.config(text="Invalid input")

# # Create main window
# root = tk.Tk()
# root.title("Loan Calculator")
# root.geometry("400x400")

# # Create labels and entry widgets
# loan_amount_label = tk.Label(root, text="Loan Amount:")
# loan_amount_label.pack()
# loan_amount_entry = tk.Entry(root)
# loan_amount_entry.pack()

# interest_rate_label = tk.Label(root, text="Interest Rate (%):")
# interest_rate_label.pack()
# interest_rate_entry = tk.Entry(root)
# interest_rate_entry.pack()

# loan_term_label = tk.Label(root, text="Loan Term (months):")
# loan_term_label.pack()
# loan_term_entry = tk.Entry(root)
# loan_term_entry.pack()

# calculate_button = tk.Button(root, text="Calculate", command=calculate_payment)
# calculate_button.pack()

# monthly_payment_label = tk.Label(root, text="")
# monthly_payment_label.pack()

# root.mainloop()


# second program
# import tkinter as tk
# from tkinter import messagebox
# import matplotlib.pyplot as plt
# import numpy as np

# def calculate_payment():
#     try:
#         loan_amount = float(loan_amount_entry.get())
#         interest_rate = float(interest_rate_entry.get()) / 100
#         loan_term = int(loan_term_entry.get())
#         monthly_interest_rate = interest_rate / 12
#         monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_term)
#         total_payment = monthly_payment * loan_term
#         total_interest = total_payment - loan_amount

#         # Update loan summary
#         summary_text.set(f"Loan Amount: ${loan_amount:.2f}\n"
#                          f"Interest Rate: {interest_rate * 100:.2f}%\n"
#                          f"Loan Term: {loan_term} months\n"
#                          f"Monthly Payment: ${monthly_payment:.2f}\n"
#                          f"Total Payment: ${total_payment:.2f}\n"
#                          f"Total Interest: ${total_interest:.2f}")

#         # Plot loan balance over time
#         time_period = np.arange(1, loan_term + 1)
#         loan_balance = loan_amount * ((1 + monthly_interest_rate) ** time_period - (1 + monthly_interest_rate) ** loan_term) / ((1 + monthly_interest_rate) ** loan_term - 1)
#         plt.figure(figsize=(8, 4))
#         plt.plot(time_period, loan_balance)
#         plt.xlabel("Month")
#         plt.ylabel("Loan Balance")
#         plt.title("Loan Balance Over Time")
#         plt.grid(True)
#         plt.show()
#     except ValueError:
#         messagebox.showerror("Error", "Invalid input")

# # Create main window
# root = tk.Tk()
# root.title("Loan Calculator")

# # Create labels and entry widgets
# loan_amount_label = tk.Label(root, text="Loan Amount:")
# loan_amount_label.grid(row=0, column=0)
# loan_amount_entry = tk.Entry(root)
# loan_amount_entry.grid(row=0, column=1)

# interest_rate_label = tk.Label(root, text="Interest Rate (%):")
# interest_rate_label.grid(row=1, column=0)
# interest_rate_entry = tk.Entry(root)
# interest_rate_entry.grid(row=1, column=1)

# loan_term_label = tk.Label(root, text="Loan Term (months):")
# loan_term_label.grid(row=2, column=0)
# loan_term_entry = tk.Entry(root)
# loan_term_entry.grid(row=2, column=1)

# calculate_button = tk.Button(root, text="Calculate", command=calculate_payment)
# calculate_button.grid(row=3, column=0, columnspan=2)

# summary_text = tk.StringVar()
# summary_label = tk.Label(root, textvariable=summary_text, justify="left")
# summary_label.grid(row=4, column=0, columnspan=2)

# root.mainloop()

# third program
import tkinter as tk
from tkinter import messagebox

def calculate_payment():
    try:
        loan_amount = float(loan_amount_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100
        loan_term = int(loan_term_entry.get())
        monthly_interest_rate = interest_rate / 12
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_term)
        total_payment = monthly_payment * loan_term
        total_interest = total_payment - loan_amount

        # Update loan summary
        summary_text.set(f"Loan Amount: ${loan_amount:.2f}\n"
                         f"Interest Rate: {interest_rate * 100:.2f}%\n"
                         f"Loan Term: {loan_term} months\n"
                         f"Monthly Payment: ${monthly_payment:.2f}\n"
                         f"Total Payment: ${total_payment:.2f}\n"
                         f"Total Interest: ${total_interest:.2f}")

        # Update loan balance over time
        loan_balance_text = ""
        for month in range(1, loan_term + 1):
            remaining_balance = loan_amount * ((1 + monthly_interest_rate) ** month - (1 + monthly_interest_rate) ** (month - 1))
            loan_balance_text += f"Month {month}: ${remaining_balance:.2f}\n"

        loan_balance_text.set(loan_balance_text)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Create main window
root = tk.Tk()
root.title("Loan Calculator")
root.geometry("400x400")

# Create labels and entry widgets
loan_amount_label = tk.Label(root, text="Loan Amount:")
loan_amount_label.grid(row=0, column=0)
loan_amount_entry = tk.Entry(root)
loan_amount_entry.grid(row=0, column=1)

interest_rate_label = tk.Label(root, text="Interest Rate (%):")
interest_rate_label.grid(row=1, column=0)
interest_rate_entry = tk.Entry(root)
interest_rate_entry.grid(row=1, column=1)

loan_term_label = tk.Label(root, text="Loan Term (months):")
loan_term_label.grid(row=2, column=0)
loan_term_entry = tk.Entry(root)
loan_term_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_payment)
calculate_button.grid(row=3, column=0, columnspan=2)

summary_text = tk.StringVar()
summary_label = tk.Label(root, textvariable=summary_text, justify="left")
summary_label.grid(row=4, column=0, columnspan=2)

loan_balance_text = tk.StringVar()
loan_balance_label = tk.Label(root, textvariable=loan_balance_text, justify="left")
loan_balance_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
