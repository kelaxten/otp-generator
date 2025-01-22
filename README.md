# One-Time Pad (OTP) Generator with GUI

This repository provides a simple **one-time pad** generator script in Python, featuring a **Tkinter**-based graphical user interface (GUI). The script allows you to generate random uppercase letters (`A–Z`) for use in physical (paper-and-pencil) cryptography.

> **Disclaimer**: While a properly used one-time pad can offer information-theoretic security, **this code** (like all software-based solutions) depends on the security of your computer environment. Additionally, **never reuse** any portion of a pad for more than one message, and keep your pads physically secure.

## Table of Contents

1. [Features](#features)  
2. [Screenshots](#screenshots)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [How It Works](#how-it-works)  
7. [Security Notes](#security-notes)  
8. [License](#license)

---

## Features

- **Graphical User Interface (GUI)** built with **Tkinter**.
- **Cryptographically secure randomness** using Python’s `secrets` module.
- **Customizable parameters**:
  - **Length**: Total number of letters in the pad.
  - **Group Size**: Number of letters per group for readability.
  - **Line Length**: Number of letters per line (excluding spaces).
- **Preview** the generated pad in the GUI’s text box.
- **Save** the pad to a text file via the GUI.

---

## Screenshots

*(Optional: Insert screenshots here if you wish. For example, images showing the GUI in action.)*

---

## Requirements

- **Python 3.6+** (Tested on Python 3.9+)
- **Tkinter** (Usually included with Python on Windows; on Linux, install the `python3-tk` package if needed.)

Example installation for Linux (Debian/Ubuntu):
```bash
sudo apt-get update
sudo apt-get install python3 python3-tk
```

---

## Installation

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/kelaxten/otp-generator.git
   cd otp-generator
   ```

2. **(Optional) Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   - Typically, Python’s standard library modules (`tkinter`, `secrets`, `string`) are included by default, so there’s no separate installation needed unless your distribution excludes Tkinter by default.

---

## Usage

### 1. Command Line

- **Windows**:
  1. Open Command Prompt or PowerShell.
  2. Navigate (`cd`) to the directory containing `otp_gen.py`.
  3. Run:  
     ```shell
     python otp_gen.py
     ```
  4. The GUI window should appear.

- **Linux**:
  1. Open a Terminal.
  2. Navigate (`cd`) to the project directory.
  3. Run:  
     ```bash
     python3 otp_gen.py
     ```
  4. The GUI window should appear.

### 2. Double-Click (Windows Only)

If you have the `.py` extension associated with Python, you can just **double-click** `otp_gen.py`. However, to see error messages (if any), running from the command line is usually more informative.

---

## How It Works

1. **Input Fields** (top of the GUI):  
   - **Length**: Total number of random letters (default `1000`).  
   - **Group Size**: Letters per group before a space is inserted (default `5`).  
   - **Line Length**: How many letters per line (excluding spaces) before line break (default `50`).

2. **Generate** button:  
   - Reads your inputs and generates a random pad (A–Z) using the `secrets` module.  
   - Displays the pad in the central **ScrolledText** widget.

3. **Save to File** button:  
   - Lets you choose a file path and saves the entire displayed pad as text.

4. **Quit** button:  
   - Closes the GUI.

---

## Security Notes

1. **One-Time Pads**:
   - A genuine one-time pad requires **truly random** data and **no reuse** of any part of the pad.  
   - When used correctly, OTPs provide **information-theoretic security**.

2. **Machine Security**:
   - If your system is compromised, an attacker may intercept the generated pad.  
   - For maximum security, generate and print your pad on an **offline, trusted** machine using a one-time use operating system like [Tails](https://tails.net/).

3. **Reuse Destroys Security**:
   - **Never reuse** an OTP or parts of it for more than one message.

4. **Physical Handling**:
   - Print or write down your pad, store it securely, and **destroy** any used sections.

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this code as permitted by the license terms.

---

> **Questions / Issues?**  
> Feel free to open an [issue](https://github.com/kelaxten/otp-generator/issues) or submit a pull request if you have any suggestions or find a bug!
