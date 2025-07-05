import tkinter as tk
from View.t_display import t_display

class t_lineas_display(t_display):
    """Display de campos para la tabla t_lineas."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Registramos validadores
        v5  = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=5))
        v3  = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=3))
        v120= self.frame.register(lambda P: len(P) <= 120)
        v1  = self.frame.register(lambda P: len(P) <= 1)

        # 1. LINEA_COD
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=8, validate="key", validatecommand=(v5, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. LINEA_COSU
        lbl = tk.Label(self.frame, text="Codugo Super:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=5, validate="key", validatecommand=(v3, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 3. LINEA_NOMB
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=50, validate="key", validatecommand=(v120, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 4. LINEA_GMF
        lbl = tk.Label(self.frame, text="genera GMF:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=3, validate="key", validatecommand=(v1, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)
