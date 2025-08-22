import tkinter as tk
from tkinter import messagebox

# Coffee prices
menu = {
    "Cold Coffee": 150,
    "Hot Coffee": 150
}

# Function to calculate total
def calculate_bill():
    coffee_type = coffee_var.get()
    quantity = quantity_entry.get()

    if coffee_type not in menu:
        messagebox.showerror("Invalid Selection", "Please select a valid coffee type.")
        return

    if not quantity.isdigit() or int(quantity) <= 0:
        messagebox.showerror("Invalid Quantity", "Please enter a valid quantity (number > 0).")
        return

    price = menu[coffee_type]
    total = price * int(quantity)
    bill_text.set(f"{coffee_type} x {quantity} = Rs. {total}/-")
    thank_you_label.config(text="✅ Thank you for your order! Please visit us again. ☕")

# Create main window
root = tk.Tk()
root.title("Coffee Management System")
root.geometry("400x400")
root.resizable(False, False)

# Heading
title_label = tk.Label(root, text="☕ Coffee Management System ☕", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Coffee type selection
coffee_var = tk.StringVar()
coffee_var.set("Select Coffee")

coffee_menu = tk.OptionMenu(root, coffee_var, *menu.keys())
coffee_menu.config(width=20, font=("Arial", 12))
coffee_menu.pack(pady=10)

# Quantity input
quantity_label = tk.Label(root, text="Enter Quantity:", font=("Arial", 12))
quantity_label.pack()

quantity_entry = tk.Entry(root, font=("Arial", 12), justify="center")
quantity_entry.pack(pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate Bill", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=calculate_bill)
calc_button.pack(pady=15)

# Bill display
bill_text = tk.StringVar()
bill_label = tk.Label(root, textvariable=bill_text, font=("Arial", 14, "bold"), fg="blue")
bill_label.pack()

# Thank-you message
thank_you_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
thank_you_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
