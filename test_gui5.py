import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TreeView Example")

# Create TreeView widget
tree = ttk.Treeview(root)
tree["columns"] = ("Quantity to craftw", "Input2", "Label1", "Label2")

# Configure column headings
tree.heading("#0", text="Row", anchor=tk.W)
tree.heading("Quantity to craft", text="Input 1", anchor=tk.W)
tree.heading("Input2", text="Input 2", anchor=tk.W)
tree.heading("Label1", text="Label 1", anchor=tk.W)
tree.heading("Label2", text="Label 2", anchor=tk.W)

# Configure column widths
tree.column("#0", width=100, minwidth=100, anchor=tk.W)
tree.column("Quantity to craft", width=100, minwidth=100, anchor=tk.W)
tree.column("Input2", width=100, minwidth=100, anchor=tk.W)
tree.column("Label1", width=100, minwidth=100, anchor=tk.W)
tree.column("Label2", width=100, minwidth=100, anchor=tk.W)

# Add sample data to the TreeView
data = [
    ["Row 1", "Input 1 Value", "Input 2 Value", "Label 1 Value", "Label 2 Value"],
    ["Row 1", "Input 1 Value", "Input 2 Value", "Label 1 Value", "Label 2 Value"],
]

for item in data:
    # Insert the row with label and inputs
    item_id = tree.insert("", "end", text=item[0], values=(item[1], item[2], "", ""))

    # Insert labels after the inputs
    tree.insert(item_id, "end", text="", values=("", item[3], item[4], ""))

# Pack the TreeView widget
tree.pack(fill=tk.BOTH, expand=True)

root.mainloop()
