import tkinter as tk
from View.t_display import t_display

def validar_codigo(P):
    return P == "" or (len(P) <= 2)

def validar_nombre(P):
    return len(P) <= 60

class t_paises_display(t_display):
    """Display de campos para la tabla t_paises."""
    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        vcode = self.frame.register(validar_codigo)
        vname = self.frame.register(validar_nombre)

        # 1. PAI_CODIGO (2 caracteres)
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(vcode, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 2. PAI_NOMBRE (60 caracteres)
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=50, validate="key", validatecommand=(vname, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)

