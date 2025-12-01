#!/usr/bin/env python3
# Script that checks URLs against Google's Safe Browsing API
# https://developers.google.com/safe-browsing/v4
# By 

import tkinter as tk
window =tk.Tk()

label_prompt =tk.Label(window, text="Enter total amount:")
label_prompt.pack(pady=5)

entry_amount =tk.Entry(window)
entry_amount.pack(pady=5)

label_result =tk.Label(window, text="")
label_result.pack(pady=10)

def calculate_tip():
    amount = entry_amount.get()
    tip = float(amount) * 0.20
    label_result.config(text=f"Tip: ${tip:.2}")

button_calc = tk.Button(window, text="Calculate 20% Tip", command=calculate_tip)
button_calc.pack(pady=10)

window.mainloop()