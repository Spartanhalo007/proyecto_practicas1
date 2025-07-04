import tkinter as tk
from View.t_display import t_display

class t_novxml_display(t_display):
    """Display de campos para la tabla t_novxml."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v1  = self.frame.register(lambda P: len(P) <= 1)
        v10 = self.frame.register(lambda P: len(P) <= 10)

        # 1. NX_CARACTE
        lbl = tk.Label(self.frame, text="Carácter:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v1, '%P'),
                       justify="center", bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 2. NX_VALIDO
        lbl = tk.Label(self.frame, text="Válido:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=15, validate="key", validatecommand=(v10, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
        
        for lbl, entry, _ in self.elements:
            lbl.config(width=7, anchor="w")
            entry.grid_configure(padx=7)