import tkinter as tk

root = tk.Tk()

# Column headings
headings = ["Name", "Quantity", "Inventory", "Crafting Cost", "Sell to Vendor"]

# Add column headings
for col, heading in enumerate(headings):
    label = tk.Label(root, text=heading, relief=tk.RAISED, padx=10, pady=5)
    label.grid(row=0, column=col, sticky=tk.NSEW)

# Add sample data
data = [
    ["Item 1", 10, 20, 5.99, 8.99],
    ["Item 2", 5, 15, 3.99, 6.99],
    ["Item 3", 2, 10, 2.49, 4.49],
]

# Add data rows
for row, item in enumerate(data, start=1):
    for col, value in enumerate(item):
        label = tk.Label(root, text=value, padx=10, pady=5)
        label.grid(row=row, column=col, sticky=tk.NSEW)

# Configure grid weights to allow column resizing
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)
root.grid_columnconfigure(index=2, weight=1)
root.grid_columnconfigure(index=3, weight=1)
root.grid_columnconfigure(index=4, weight=1)

root.mainloop()
