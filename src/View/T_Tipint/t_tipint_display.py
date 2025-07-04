import tkinter as tk
from View.t_display import t_display

class t_tipint_display(t_display):
    """Display de campos para la tabla t_tipint."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v2  = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=2))
        v40 = self.frame.register(lambda P: len(P) <= 40)

        # 1. TIPINT_COD (2 dígitos num)
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. TIPINT_NOM (40 chars)
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=40, validate="key", validatecommand=(v40, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
