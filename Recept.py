# import tkinter as tk
# from tkinter import messagebox

# class ReceiptPrinterGUI:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Receipt Printer")

#         # Create GUI elements
#         self.label_item = tk.Label(self.window, text="Item:")
#         self.label_item.pack()
#         self.entry_item = tk.Entry(self.window)
#         self.entry_item.pack()

#         self.label_price = tk.Label(self.window, text="Price:")
#         self.label_price.pack()
#         self.entry_price = tk.Entry(self.window)
#         self.entry_price.pack()

#         self.button_print = tk.Button(self.window, text="Print Receipt", command=self.print_receipt)
#         self.button_print.pack()

#     def print_receipt(self):
#         item = self.entry_item.get()
#         price = self.entry_price.get()

#         if item and price:
#             receipt_text = f"Item: {item}\nPrice: ${price}"

#             # Display receipt in a messagebox
#             messagebox.showinfo("Receipt", receipt_text)
#         else:
#             messagebox.showerror("Error", "Please enter both item and price.")

#     def run(self):
#         self.window.mainloop()

# # Create an instance of the ReceiptPrinterGUI class and run the program
# receipt_printer = ReceiptPrinterGUI()
# receipt_printer.run()

import tkinter as tk
from tkinter import messagebox

class ReceiptPrinterGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Nabbona Prossy's SuperMarket")

        # Create GUI elements
        self.label_item = tk.Label(self.window, text="Item:")
        self.label_item.pack()
        self.entry_item = tk.Entry(self.window)
        self.entry_item.pack()

        self.label_quantity = tk.Label(self.window, text="Quantity:")
        self.label_quantity.pack()
        self.entry_quantity = tk.Entry(self.window)
        self.entry_quantity.pack()

        self.label_price = tk.Label(self.window, text="Price:")
        self.label_price.pack()
        self.entry_price = tk.Entry(self.window)
        self.entry_price.pack()

        self.button_add = tk.Button(self.window, text="Add Item", command=self.add_item)
        self.button_add.pack()

        self.scrollbar = tk.Scrollbar(self.window)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.receipt_text = tk.Text(self.window, height=10, width=70)
        self.receipt_text.pack()
        self.receipt_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.receipt_text.yview)

        self.label_subtotal = tk.Label(self.window, text="Subtotal:")
        self.label_subtotal.pack()
        self.label_subtotal_value = tk.Label(self.window, text="shs 0.00")
        self.label_subtotal_value.pack()

        self.label_tax = tk.Label(self.window, text="Tax (5%):")
        self.label_tax.pack()
        self.label_tax_value = tk.Label(self.window, text="shs 0.00")
        self.label_tax_value.pack()

        self.label_total = tk.Label(self.window, text="Total:")
        self.label_total.pack()
        self.label_total_value = tk.Label(self.window, text="shs 0.00")
        self.label_total_value.pack()

        self.button_print = tk.Button(self.window, text="Print Receipt", command=self.print_receipt)
        self.button_print.pack()

        # Initialize variables
        self.items = []
        self.subtotal = 0.0

    def add_item(self):
        item = self.entry_item.get()
        quantity = self.entry_quantity.get()
        price = self.entry_price.get()

        if item and quantity and price:
            try:
                quantity = int(quantity)
                price = float(price)
            except ValueError:
                messagebox.showerror("Error", "Please enter valid quantity and price.")
                return

            item_total = quantity * price
            self.items.append((item, quantity, price, item_total))
            self.subtotal += item_total

            self.update_receipt()

            # Clear input fields
            self.entry_item.delete(0, tk.END)
            self.entry_quantity.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter item, quantity, and price.")

    def update_receipt(self):
        self.receipt_text.delete("1.0", tk.END)
        for item in self.items:
            item_text = f"{item[0]} ({item[1]} x shs {item[2]:.2f}) = shs {item[3]:.2f}"
            self.receipt_text.insert(tk.END, item_text + "\n")
        self.receipt_text.insert(tk.END, "\n")

        self.label_subtotal_value.config(text=f"shs {self.subtotal:.2f}")

        tax = self.subtotal * 0.05
        self.label_tax_value.config(text=f"shs {tax:.2f}")

        total = self.subtotal + tax
        self.label_total_value.config(text=f"shs {total:.2f}")

    def print_receipt(self):
        receipt_text = self.receipt_text.get("1.0", tk.END)
        if receipt_text:
            messagebox.showinfo("Receipt: Thanks  for shopping with us", receipt_text)
        else:
            messagebox.showerror("Error", "No items to print.")

    def run(self):
        self.window.mainloop()

# Create an instance of the ReceiptPrinterGUI class and run the program
receipt_printer = ReceiptPrinterGUI()
receipt_printer.run()
