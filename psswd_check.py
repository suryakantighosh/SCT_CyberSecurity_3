import re
import tkinter as tk
from tkinter import messagebox

###developed by Mr. Suryakanti Ghosh####

def check_psswd(psswd):
    length = 1 if len(psswd) >= 8 else 0
    lower = 1 if re.search(r'[a-z]',psswd) else 0
    upper = 1 if re.search(r'[A-Z]',psswd) else 0
    digit = 1 if re.search(r'[0-9]',psswd) else 0
    special = 1 if re.search(r'[!@#$%^&*()_={}|\<,>.?/"`~]',psswd) else 0
    match = [length,lower,upper,digit,special]
    
    strength = sum(match)
    error = []
    if not length:
        error.append("Password should contain more than 7 charectors")
    if not lower:
        error.append("Password should contain atleast 1 lower case charector")
    if not upper:
        error.append("Password should contain atleast 1 upper case charector")
    if not digit:
        error.append("Password should contain atleast one digit")
    if not special:
        error.append("Password should contain atleast one special charector")

    return strength , error

def check(entry):
    psswd = entry.get()
    strength , error = check_psswd(psswd)
    if strength <= 2  :
        messagebox.showerror("Strength Error","Password is very Weak, "+"strength of Password is -> "+str(strength)+"/5")
        messagebox.showerror("Incorrect Format For Password",error)
    if 2<strength <5 :
        messagebox.showerror("Strength Error","Password is Weak, "+"strength of Password is -> "+str(strength)+"/5")
        messagebox.showerror("Incorrect Format For Password",error)
    if strength ==5 :
        messagebox.showinfo("Strength Perfect","Password is Strong")
def show(entry):
    psswd = entry.get()
    messagebox.showinfo("Password","Password is - >  "+psswd)


root = tk.Tk()
root.geometry("600x400")
root.title("Password Strength Checker")

tk.Label(root, text = "Enter Password to Check->").pack(pady=20)
entry = tk.Entry(root, show = "*", width =40)
entry.pack(pady=20)
button = tk.Button(root, text = "Check Strength", command = lambda:check(entry))
button.pack(pady = 20)
button2 = tk.Button(root,text = "Show Password", command = lambda:show(entry))
button2.pack(pady =10)
root.mainloop()
