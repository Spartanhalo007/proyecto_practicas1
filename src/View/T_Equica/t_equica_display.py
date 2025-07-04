import tkinter as tk
from View.t_display import t_display

def validar_long(P, maxlen):
    return len(P) <= maxlen

class t_equica_display(t_display):
    """Display de campos para la tabla t_equica."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # validadores
        v10 = self.frame.register(lambda P: validar_long(P, 10))
        v40 = self.frame.register(lambda P: validar_long(P, 40))

        # 1. EQUI_BANCO
        lbl = tk.Label(self.frame, text="Banco:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, validate="key", validatecommand=(v10, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 2. EQUI_CATAS
        lbl = tk.Label(self.frame, text="CATA Sucursal:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, validate="key", validatecommand=(v10, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. EQUI_CONCE
        lbl = tk.Label(self.frame, text="Concepto:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=40, validate="key", validatecommand=(v40, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
