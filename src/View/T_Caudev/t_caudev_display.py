import tkinter as tk
from View.t_display import t_display

def validar_numero(P):
    return P == "" or (P.isdigit() and len(P) <= 4)

class t_caudev_display(t_display):
    """Display de campos para la tabla t_caudev."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        vcmd = self.frame.register(validar_numero)

        # 1. dev_codigo (numérico de hasta 4 dígitos)
        lbl1 = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry1 = tk.Entry(self.frame, width=4, validate="key", validatecommand=(vcmd, '%P'), bd=0, bg="white")
        self.elements.append([lbl1, entry1])
        self.elements_types.append("num")

        # 2. dev_concep (texto hasta 50 chars)
        lbl2 = tk.Label(self.frame, text="Concepto:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry2 = tk.Entry(self.frame, width=53, bd=0, bg="white")
        self.elements.append([lbl2, entry2])
        self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
        for lbl, entry, _ in self.elements:
            lbl.config(width=8, anchor="w")
            entry.grid_configure(padx=7)
