import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Stationery Order Manager")
root.geometry("800x600")
root.resizable(False, False)

# -----------------------------
# Canvas + Background
# -----------------------------
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

# Create a simple background
canvas.create_rectangle(
    0, 0, 800, 600,
    fill=R"#EAF4FF",
    outline=""
)

# -----------------------------
# Styling
# -----------------------------
style = ttk.Style()
style.configure(
    "Title.TLabel",
    font=("Arial", 24, "bold")
)

style.configure(
    "Header.TLabel",
    font=("Arial", 12, "bold")
)

style.configure(
    "Normal.TLabel",
    font=("Arial", 11)
)

# -----------------------------
# Stationery Data
# -----------------------------
stationery = [
    ("Notebook", 5.00),
    ("Pencil", 1.50),
    ("Eraser", 1.00),
    ("Pen", 2.00),
    ("Markers", 6.00),
    ("Ruler", 3.00),
    ("Glue Stick", 2.50),
    ("Colored Pencils", 8.00)
]

# -----------------------------
# Title
# -----------------------------
title = ttk.Label(
    root,
    text="✏️ Stationery Order Manager",
    style="Title.TLabel"
)
title.place(x=230, y=30)

# -----------------------------
# Currency
# -----------------------------
currency = tk.StringVar(value="USD")

currency_label = ttk.Label(
    root,
    text="Currency:",
    style="Header.TLabel"
)
currency_label.place(x=580, y=40)

currency_box = ttk.Combobox(
    root,
    textvariable=currency,
    values=["USD", "INR"],
    state="readonly",
    width=8
)
currency_box.place(x=650, y=40)

# -----------------------------
# Headers
# -----------------------------
ttk.Label(
    root,
    text="Item",
    style="Header.TLabel"
).place(x=100, y=100)

ttk.Label(
    root,
    text="Price",
    style="Header.TLabel"
).place(x=300, y=100)

ttk.Label(
    root,
    text="Quantity",
    style="Header.TLabel"
).place(x=450, y=100)

# -----------------------------
# Quantity Entries
# -----------------------------
quantity_entries = []

# Generate rows using enumerate()
for i, (item, price) in enumerate(stationery):

    y_position = 135 + i * 45

    # Item name
    ttk.Label(
        root,
        text=item,
        style="Normal.TLabel"
    ).place(x=100, y=y_position)

    # Price
    price_label = ttk.Label(
        root,
        text=f"${price:.2f}",
        style="Normal.TLabel"
    )
    price_label.place(x=300, y=y_position)

    # Quantity entry
    quantity_entry = ttk.Entry(
        root,
        width=12
    )
    quantity_entry.place(x=450, y=y_position)

    quantity_entries.append(quantity_entry)


# -----------------------------
# Update Prices
# -----------------------------
def update_currency(event=None):

    selected_currency = currency.get()

    # Ternary expression
    symbol = "$" if selected_currency == "USD" else "₹"

    conversion_rate = 1 if selected_currency == "USD" else 83

    for i, (item, price) in enumerate(stationery):

        converted_price = price * conversion_rate

        # Find the price label
        # Labels are positioned according to enumerate()
        # and are recreated when currency changes.
        y_position = 135 + i * 45

        ttk.Label(
            root,
            text=f"{symbol}{converted_price:.2f}",
            style="Normal.TLabel"
        ).place(x=300, y=y_position)


currency_box.bind("<<ComboboxSelected>>", update_currency)


# -----------------------------
# Calculate Order
# -----------------------------
def calculate_order():

    total = 0
    selected_currency = currency.get()

    # Ternary expression
    conversion_rate = 1 if selected_currency == "USD" else 83

    # Check every quantity
    for i, (item, price) in enumerate(stationery):

        quantity = quantity_entries[i].get()

        # Validate using .isdigit()
        if quantity == "":
            continue

        if not quantity.isdigit():
            messagebox.showerror(
                "Invalid Quantity",
                f"Please enter a whole number for {item}."
            )
            return

        quantity = int(quantity)

        total += price * quantity

    # Currency symbol using ternary expression
    symbol = "$" if selected_currency == "USD" else "₹"

    converted_total = total * conversion_rate

    total_label.config(
        text=f"Total: {symbol}{converted_total:.2f}"
    )


# -----------------------------
# Clear Order
# -----------------------------
def clear_order():

    for entry in quantity_entries:
        entry.delete(0, tk.END)

    total_label.config(text="Total: $0.00")


# -----------------------------
# Buttons
# -----------------------------
calculate_button = ttk.Button(
    root,
    text="Calculate Order",
    command=calculate_order
)
calculate_button.place(x=300, y=520)

clear_button = ttk.Button(
    root,
    text="Clear",
    command=clear_order
)
clear_button.place(x=450, y=520)


# -----------------------------
# Total
# -----------------------------
total_label = ttk.Label(
    root,
    text="Total: $0.00",
    font=("Arial", 15, "bold")
)
total_label.place(x=100, y=520)


# -----------------------------
# Start Program
# -----------------------------
root.mainloop()