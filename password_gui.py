import tkinter as tk
from zxcvbn import zxcvbn

def check_password():
    pwd = entry.get()
    res = zxcvbn(pwd)
    result_label.config(text=f"Score: {res['score']}\n{res['feedback']['suggestions']}")

root = tk.Tk()
root.title("Password Strength Analyzer")
entry = tk.Entry(root, show="*")
entry.pack()
tk.Button(root, text="Check Strength", command=check_password).pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
