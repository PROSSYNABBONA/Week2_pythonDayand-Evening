import tkinter as tk
from tkinter import messagebox

class ReceiptPrinterGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Receipt Printer")

        # Create GUI elements
        self.receipt_text = tk.Text(self.window, height=15, width=50)
        self.receipt_text.pack()

        self.button_print = tk.Button(self.window, text="Print Receipt", command=self.print_receipt)
        self.button_print.pack()

    def add_item(self, item_text, color):
        self.receipt_text.insert(tk.END, item_text, color)
        self.receipt_text.insert(tk.END, "\n")

    def print_receipt(self):
        receipt_text = self.receipt_text.get("1.0", tk.END)
        if receipt_text:
            messagebox.showinfo("Receipt", receipt_text)
        else:
            messagebox.showerror("Error", "No items to print.")

    def run(self):
        self.window.mainloop()

# Create an instance of the ReceiptPrinterGUI class and run the program
receipt_printer = ReceiptPrinterGUI()
receipt_printer.add_item("Item: Apple", "blue")
receipt_printer.add_item("Price: $1.00", "green")
receipt_printer.add_item("----------------------------", "black")
receipt_printer.add_item("Item: Orange", "blue")
receipt_printer.add_item("Price: $0.75", "green")
receipt_printer.run()
