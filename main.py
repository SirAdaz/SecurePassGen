import tkinter as tk
from password_gen import generate_password

# -------------------------
# Actions
# -------------------------
def on_generate():
    pwd = generate_password(
        length_var.get(),
        uppercase_var.get(),
        digits_var.get(),
        specials_var.get()
    )
    entry_var.set(pwd)

def on_copy():
    root.clipboard_clear()
    root.clipboard_append(entry_var.get())
    root.update()

def increase_length():
    if length_var.get() < 64:
        length_var.set(length_var.get() + 1)

def decrease_length():
    if length_var.get() > 8:
        length_var.set(length_var.get() - 1)

def validate_length(event=None):
    try:
        val = int(length_entry.get())
        if val < 8:
            val = 8
        elif val > 64:
            val = 64
        length_var.set(val)
    except ValueError:
        length_entry.delete(0, tk.END)
        length_entry.insert(0, str(length_var.get()))

# -------------------------
# Fenêtre principale
# -------------------------
root = tk.Tk()
root.title("SecurePassGen - Hacker Edition")
root.configure(bg="black")
root.geometry("600x300")

# -------------------------
# Style commun
# -------------------------
label_style = {"bg": "black", "fg": "#00FF00", "font": ("Courier", 12)}
btn_style = {"bg": "black", "fg": "#00FF00", "font": ("Courier", 12), "activebackground": "black", "activeforeground": "#00FF00", "relief": "ridge", "bd": 2}

# -------------------------
# Widgets
# -------------------------
# Champ mot de passe
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=50, font=("Courier", 14), bg="black", fg="#00FF00", insertbackground="#00FF00", justify="center")
entry.pack(pady=15)

# Options
length_var = tk.IntVar(value=20)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
specials_var = tk.BooleanVar(value=True)

# Compteur + entrée manuelle
tk.Label(root, text="Longueur :", **label_style).pack()
length_frame = tk.Frame(root, bg="black")
length_frame.pack(pady=5)

tk.Button(length_frame, text="-", command=decrease_length, width=3, **btn_style).grid(row=0, column=0, padx=5)

length_entry = tk.Entry(length_frame, textvariable=length_var, width=4, font=("Courier", 14, "bold"), bg="black", fg="#00FF00", justify="center", insertbackground="#00FF00")
length_entry.grid(row=0, column=1, padx=5)
length_entry.bind("<Return>", validate_length)
length_entry.bind("<FocusOut>", validate_length)

tk.Button(length_frame, text="+", command=increase_length, width=3, **btn_style).grid(row=0, column=2, padx=5)


# Cases à cocher
options_frame = tk.Frame(root, bg="black")
options_frame.pack(pady=5)

tk.Checkbutton(options_frame, text="Majuscules", variable=uppercase_var, **label_style, selectcolor="black").grid(row=0, column=0, padx=10)
tk.Checkbutton(options_frame, text="Chiffres", variable=digits_var, **label_style, selectcolor="black").grid(row=0, column=1, padx=10)
tk.Checkbutton(options_frame, text="Spéciaux", variable=specials_var, **label_style, selectcolor="black").grid(row=0, column=2, padx=10)

# Boutons
btn_frame = tk.Frame(root, bg="black")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Générer", command=on_generate, **btn_style).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Copier", command=on_copy, **btn_style).grid(row=0, column=1, padx=10)

# -------------------------
# Lancement
# -------------------------
root.mainloop()
