import tkinter as tk
from tkinter import messagebox


# Function to open the reading planner window
def open_planner():
    
    # Create a new Toplevel window
    planner_window = tk.Toplevel(root)
    planner_window.title("Reading Schedule Planner")
    planner_window.geometry("400x350")

    # Title
    title_label = tk.Label(
        planner_window,
        text="Reading Schedule Planner",
        font=("Arial", 18, "bold")
    )
    title_label.pack(pady=15)

    # Total pages label and entry
    pages_label = tk.Label(
        planner_window,
        text="Total number of pages in the book:"
    )
    pages_label.pack()

    pages_entry = tk.Entry(planner_window)
    pages_entry.pack(pady=5)

    # Pages per day label and entry
    daily_label = tk.Label(
        planner_window,
        text="Number of pages to read each day:"
    )
    daily_label.pack()

    daily_entry = tk.Entry(planner_window)
    daily_entry.pack(pady=5)

    # Function to calculate reading schedule
    def calculate_schedule():
        try:
            total_pages = int(pages_entry.get())
            pages_per_day = int(daily_entry.get())

            # Check that numbers are positive
            if total_pages <= 0 or pages_per_day <= 0:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter positive numbers."
                )
                return

            # Floor division for complete reading days
            complete_days = total_pages // pages_per_day

            # Modulo for remaining pages
            remaining_pages = total_pages % pages_per_day

            # Display result
            result_label.config(
                text=f"Complete reading days: {complete_days}\n"
                     f"Remaining pages: {remaining_pages}"
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter valid whole numbers."
            )

    # Calculate button
    calculate_button = tk.Button(
        planner_window,
        text="Calculate Schedule",
        command=calculate_schedule
    )
    calculate_button.pack(pady=15)

    # Result label
    result_label = tk.Label(
        planner_window,
        text="",
        font=("Arial", 14)
    )
    result_label.pack(pady=10)


# Create main window
root = tk.Tk()
root.title("Reading Planner")
root.geometry("400x250")

# Main title
main_label = tk.Label(
    root,
    text="Welcome to the Reading Schedule Planner!",
    font=("Arial", 16, "bold"),
    wraplength=350
)
main_label.pack(pady=40)

# Button to open Toplevel window
open_button = tk.Button(
    root,
    text="Open Reading Planner",
    command=open_planner,
    font=("Arial", 12)
)
open_button.pack()

# Start the program
root.mainloop()