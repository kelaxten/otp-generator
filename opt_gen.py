"""
----------------------------------------------------------------------
One-Time Pad Generator with GUI (Tkinter)
----------------------------------------------------------------------
Generates a cryptographically random one-time pad (OTP) composed of 
uppercase letters (A–Z). The output can be previewed in a text box and 
optionally saved to a file.

Requirements:
    - Python 3.6+ recommended.
    - Tkinter (comes pre-installed with most Python installations).
    - The 'secrets' module is used for cryptographically secure randomness.

Usage:
    python otp_gui.py
        -> Opens a GUI window.

Key Features:
    - User can enter 'Length', 'Group Size', 'Line Length' via text fields.
    - Output is shown in a scrollable text area.
    - Output can be saved to a file via a "Save to File" button.
    - Each line is grouped for readability based on user-supplied 'group_size' 
      and 'line_length'.

Tips:
    - NEVER reuse a one-time pad for more than one message.
    - Keep any printed or stored pads physically secure.
----------------------------------------------------------------------
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import secrets
import string

def generate_one_time_pad(length: int, group_size: int, line_length: int) -> list:
    """
    Generate a random one-time pad consisting of uppercase letters.

    :param length:      Total number of random characters to generate.
    :param group_size:  Number of characters in each group (for readability).
    :param line_length: Number of characters (not counting spaces) per line.
                        For example, if line_length=50 and group_size=5,
                        you get 10 groups of 5 letters per line.

    :return: A list of strings, each representing one line of grouped characters.
    """
    # Generate all random characters using a cryptographically secure source
    all_chars = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(length))

    lines = []
    # Break the generated string into lines of `line_length` characters
    for i in range(0, length, line_length):
        line_segment = all_chars[i : i + line_length]

        # Insert spaces every 'group_size' characters for readability
        grouped_line = ' '.join(
            line_segment[j : j + group_size]
            for j in range(0, len(line_segment), group_size)
        )
        lines.append(grouped_line)

    return lines

class OTPGeneratorApp:
    """
    Main application class for the One-Time Pad Generator GUI.
    """

    def __init__(self, root: tk.Tk):
        """
        Initialize the main window and its widgets.
        """
        self.root = root
        self.root.title("One-Time Pad Generator")

        # Frame for input parameters
        self.input_frame = ttk.LabelFrame(self.root, text="Parameters")
        self.input_frame.pack(padx=10, pady=10, fill="x")

        # Length
        ttk.Label(self.input_frame, text="Length (Default 1000):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.length_var = tk.StringVar(value="1000")
        ttk.Entry(self.input_frame, textvariable=self.length_var, width=10).grid(row=0, column=1, sticky="w", padx=5, pady=5)

        # Group Size
        ttk.Label(self.input_frame, text="Group Size (Default 5):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.group_size_var = tk.StringVar(value="5")
        ttk.Entry(self.input_frame, textvariable=self.group_size_var, width=10).grid(row=1, column=1, sticky="w", padx=5, pady=5)

        # Line Length
        ttk.Label(self.input_frame, text="Line Length (Default 50):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.line_length_var = tk.StringVar(value="50")
        ttk.Entry(self.input_frame, textvariable=self.line_length_var, width=10).grid(row=2, column=1, sticky="w", padx=5, pady=5)

        # Button to generate
        self.generate_button = ttk.Button(self.input_frame, text="Generate", command=self.on_generate)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Scrolled text for displaying the generated pad
        self.output_frame = ttk.LabelFrame(self.root, text="Generated One-Time Pad")
        self.output_frame.pack(padx=10, pady=(0,10), fill="both", expand=True)

        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD, width=80, height=20)
        self.output_text.pack(padx=5, pady=5, fill="both", expand=True)

        # Frame for additional actions
        self.actions_frame = ttk.Frame(self.root)
        self.actions_frame.pack(fill="x", padx=10, pady=(0, 10))

        # Button to save to a file
        self.save_button = ttk.Button(self.actions_frame, text="Save to File", command=self.on_save)
        self.save_button.pack(side="left", padx=5)

        # Quit button
        self.quit_button = ttk.Button(self.actions_frame, text="Quit", command=self.root.quit)
        self.quit_button.pack(side="right", padx=5)

    def on_generate(self):
        """
        Generate the one-time pad and display it in the text box.
        """
        # Clear previous output
        self.output_text.delete("1.0", tk.END)

        # Validate input and convert to int
        try:
            length = int(self.length_var.get())
            group_size = int(self.group_size_var.get())
            line_length = int(self.line_length_var.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers for Length, Group Size, and Line Length.")
            return

        # Basic sanity checks
        if length <= 0 or group_size <= 0 or line_length <= 0:
            messagebox.showerror("Invalid Input", "Values must be positive integers.")
            return

        # Generate the pad
        pad_lines = generate_one_time_pad(length, group_size, line_length)

        # Display in the text area
        for line in pad_lines:
            self.output_text.insert(tk.END, line + "\n")

    def on_save(self):
        """
        Save the generated text to a file chosen by the user.
        """
        # Get the text from the text box
        pad_text = self.output_text.get("1.0", tk.END).strip()
        if not pad_text:
            messagebox.showinfo("No Data", "No one-time pad generated to save.")
            return

        # Ask user for a filename/location
        filename = filedialog.asksaveasfilename(
            title="Save One-Time Pad",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        # If the user canceled, filename will be empty
        if filename:
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(pad_text)
                messagebox.showinfo("Success", f"Pad successfully saved to: {filename}")
            except Exception as e:
                messagebox.showerror("Error Saving File", str(e))

def main():
    """
    Main entry point: Initialize the Tkinter application and run it.
    """
    root = tk.Tk()
    app = OTPGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
