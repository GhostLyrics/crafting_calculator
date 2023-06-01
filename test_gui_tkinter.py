import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create root window
root = tk.Tk()
root.title("Treeview Demo - Hierarchical Data")
root.geometry("400x200")

# configure the grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# create a treeview
tree = ttk.Treeview(root)
tree.heading("#0", text="Departments", anchor=tk.W)


# adding data
tree.insert("", tk.END, text="Handwork Craft Tool", iid="parent0", open=False)
tree.insert("", tk.END, text="Logistics", iid="parent1", open=False)
tree.insert("", tk.END, text="Sales", iid="parent2", open=False)
tree.insert("", tk.END, text="Finance", iid="parent3", open=False)
tree.insert("", tk.END, text="IT", iid="parent4", open=False)

# create children
tree.insert("", tk.END, text="Zircon", iid="child5", open=False)
tree.insert("", tk.END, text="Thin String", iid="child6", open=False)
tree.insert("", tk.END, text="Normal Lumber", iid="child7", open=False)
# assign to parent
tree.move("child5", "parent0", 0)
tree.move("child6", "parent0", 1)
tree.move("child7", "parent0", 2)

# place the Treeview widget on the root window
tree.grid(row=0, column=0, sticky=tk.NSEW)

# run the app
root.mainloop()
