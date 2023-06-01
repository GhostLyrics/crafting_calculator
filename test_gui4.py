import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TreeView Example")

# Create TreeView widget
tree = ttk.Treeview(root)
tree["columns"] = ("Quantity", "Inventory", "Crafting Cost", "Sell to Vendor")

# Configure column headings
tree.heading("#0", text="Name", anchor=tk.W)
tree.heading("Quantity", text="Quantity", anchor=tk.W)
tree.heading("Inventory", text="Inventory", anchor=tk.W)
tree.heading("Crafting Cost", text="Crafting Cost", anchor=tk.W)
tree.heading("Sell to Vendor", text="Sell to Vendor", anchor=tk.W)

# Configure column widths
tree.column("#0", width=150, minwidth=150, anchor=tk.W)
tree.column("Quantity", width=100, minwidth=100, anchor=tk.W)
tree.column("Inventory", width=100, minwidth=100, anchor=tk.W)
tree.column("Crafting Cost", width=100, minwidth=100, anchor=tk.W)
tree.column("Sell to Vendor", width=100, minwidth=100, anchor=tk.W)

# Add sample data to the TreeView
data = [
    ["Item 1", 10, 20, 5.99, 8.99],
    ["Sub-item 1.1", 5, 15, 3.99, 6.99],
    ["Sub-item 1.2", 2, 10, 2.49, 4.49],
    ["Item 2", 7, 18, 4.49, 7.99],
    ["Item 3", 3, 8, 6.99, 9.99],
]


def add_items(parent, items):
    for item in items:
        item_id = tree.insert(parent, "end", text=item[0], values=item[1:])
        if isinstance(item[0], list):
            add_items(item_id, item[0])


add_items("", data)

# Pack the TreeView widget
tree.pack(fill=tk.BOTH, expand=True)

root.mainloop()
