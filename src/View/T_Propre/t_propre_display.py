import tkinter as tk
from View.t_display import t_display

def validar_codigo(P):
    return P=="" or (P.isdigit() and len(P)<=2)

def validar_nombre(P):
    return len(P) <= 40

class t_propre_display(t_display):
    """Display de campos para la tabla t_propre."""
    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        vcod = self.frame.register(validar_codigo)
        vnom = self.frame.register(validar_nombre)

        # 1. PROPRE_COD (2 dígitos numéricos)
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(vcod, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. PROPRE_NOM (40 caracteres)
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=40, validate="key", validatecommand=(vnom, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
