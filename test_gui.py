import tkinter as tk


def increment():
    if not hasattr(increment, "counter"):
        increment.counter = -1
    increment.counter += 1
    return increment.counter


def submit():
    for index, row in enumerate(rows):
        label_text = row[f"label{index}"]["text"]
        input_text = row[f"entry{index}"].get()
        print(f"{label_text}: {input_text}")


root = tk.Tk()

# List of rows
rows = []


# Function to add a new row
def add_row():
    index = increment()
    new_row = {}
    label = tk.Label(root, text=f"Label{index}")
    entry = tk.Entry(root)
    label.grid(row=len(rows), column=0, padx=10, pady=5)
    entry.grid(row=len(rows), column=1, padx=10, pady=5)

    new_row[f"label{index}"] = label
    new_row[f"entry{index}"] = entry
    rows.append(new_row)


# Button to add a new row
add_button = tk.Button(root, text="Add Row", command=add_row)
add_button.grid(row=0, column=9, columnspan=2, padx=10, pady=5)

# Button to submit the form
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=1, column=10, columnspan=2, padx=10, pady=5)

root.mainloop()
