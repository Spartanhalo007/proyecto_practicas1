import tkinter as tk
from View.t_display import t_display

class t_segmen_display(t_display):
    """Display de campos para la tabla t_segmen."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v3   = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=3))
        v30  = self.frame.register(lambda P: len(P)<=30)

        # 1. SEGMEN_COD (3 dígitos num)
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=3, validate="key", validatecommand=(v3, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. SEGMEN_NOM (30 chars)
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=30, validate="key", validatecommand=(v30, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
