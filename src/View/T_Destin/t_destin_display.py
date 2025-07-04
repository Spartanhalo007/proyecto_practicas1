import tkinter as tk
from View.t_display import t_display

def validar_num(P, maxlen):
    return P == "" or (P.isdigit() and len(P) <= maxlen)

class t_destin_display(t_display):
    """Display de campos para la tabla t_destin."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        v2 = self.frame.register(lambda P: validar_num(P, 2))
        v1 = self.frame.register(lambda P: validar_num(P, 1))
        v60 = self.frame.register(lambda P: len(P) <= 60)

        # 1. INV_CODIGO
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. INV_TIPO
        lbl = tk.Label(self.frame, text="Tipo:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v1, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 3. INV_NOMBRE
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=60, validate="key", validatecommand=(v60, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)

        #Edita los campos originales
        for lbl, entry, _ in self.elements:
            lbl.config(width=7, anchor="w")
            entry.grid_configure(padx=0)
