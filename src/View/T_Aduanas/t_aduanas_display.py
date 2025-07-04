import tkinter as tk
from View.t_display import t_display

def solo_numeros(P):
    return P == "" or (P.isdigit() and len(P) <= 2)

class t_aduana_display(t_display):

    def __init__(self, app):

        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        # Create elements

        self.elements = []
        self.elements_types = []

        vcmd = self.frame.register(solo_numeros)

        # Código
        lbl_codigo = tk.Label(self.frame, text="Código:", font=("Arial", 8, "bold"), bg="#c0c0c0")
        entry_codigo = tk.Entry(self.frame, width=2, validate="key", validatecommand=(vcmd, '%P'),
                                justify="center", bd=0, bg="white")
        entry_codigo.insert(0, "00")

        self.elements.append([lbl_codigo ,entry_codigo])
        self.elements_types.append("num")

        # Nombre
        lbl_nombre = tk.Label(self.frame, text="Nombre:", font=("Arial", 8, "bold"), bg="#c0c0c0")
        entry_nombre = tk.Entry(self.frame, width=45, bd=0, bg="white")

        self.elements.append([lbl_nombre ,entry_nombre])
        self.elements_types.append("str")
        super().__init__(self.frame, self.elements, self.elements_types)

        for lbl, entry, _ in self.elements:
            lbl.config(width=10, anchor="w")
            entry.grid_configure(padx=10)
        