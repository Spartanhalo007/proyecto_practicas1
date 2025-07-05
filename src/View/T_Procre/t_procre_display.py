import tkinter as tk
from View.t_display import t_display

def validar_codigo(P):
    return P == "" or (P.isdigit() and len(P) <= 2)

def validar_nombre(P):
    return len(P) <= 200

def validar_tipocre(P):
    return len(P) <= 1

class t_procre_display(t_display):
    """Display de campos para la tabla t_procre."""
    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        vcode   = self.frame.register(validar_codigo)
        vname   = self.frame.register(validar_nombre)
        vtype   = self.frame.register(validar_tipocre)

        # 1. PC_CODIGO (2 dígitos numéricos)
        lbl = tk.Label(self.frame, text="Código:",   font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2,  validate="key", validatecommand=(vcode, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 3. PC_TIPOCRE (1 carácter)
        lbl = tk.Label(self.frame, text="Tipo:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1,  validate="key", validatecommand=(vtype, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 2. PC_NOMBRE (200 caracteres)
        lbl = tk.Label(self.frame, text="Descipción:",   font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=50, validate="key", validatecommand=(vname, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
