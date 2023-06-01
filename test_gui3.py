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
input_entries = []  # Store the Entry widgets


def on_entry_change(event):
    # Get the new value from the Entry widget
    new_value = event.widget.get()
    # Update the data list with the new value
    row_index = int(event.widget.grid_info()["row"])
    col_index = int(event.widget.grid_info()["column"])
    data[row_index - 1][col_index - 1] = new_value


for row, item in enumerate(data, start=1):
    for col, value in enumerate(item):
        if col == 1 or col == 2:
            # Create Entry widgets for columns 2, 3, 4, 5
            entry = tk.Entry(root, justify=tk.RIGHT)
            entry.insert(tk.END, value)
            entry.grid(row=row, column=col, sticky=tk.NSEW)
            entry.bind("<FocusOut>", on_entry_change)
            input_entries.append(entry)
        else:
            # Create Label widgets for other columns
            label = tk.Label(root, text=value, padx=10, pady=5)
            label.grid(row=row, column=col, sticky=tk.NSEW)

# Configure grid weights to allow column resizing
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)
root.grid_columnconfigure(index=2, weight=1)
root.grid_columnconfigure(index=3, weight=1)
root.grid_columnconfigure(index=4, weight=1)

root.mainloop()
