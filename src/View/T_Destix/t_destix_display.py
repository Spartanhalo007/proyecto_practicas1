import tkinter as tk
from View.t_display import t_display

class t_destix_display(t_display):
    """Display de campos para la tabla t_destix."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores de longitud
        v4  = self.frame.register(lambda P: len(P) <= 4)
        v60 = self.frame.register(lambda P: len(P) <= 60)

        # 1. INV_CODIGO
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=4, validate="key", validatecommand=(v4, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 2. INV_NOMBRE
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=50, validate="key", validatecommand=(v60, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)

        #Edita los campos originales
        for lbl, entry, _ in self.elements:
            lbl.config(width=7, anchor="w")
            entry.grid_configure(padx=10)
