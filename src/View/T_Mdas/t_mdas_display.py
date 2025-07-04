import tkinter as tk
from View.t_display import t_display

class t_mdas_display(t_display):
    """Display de campos para la tabla t_mdas."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v2   = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=2))
        v3s  = self.frame.register(lambda P: len(P)<=3)
        v25  = self.frame.register(lambda P: len(P)<=25)
        v14  = self.frame.register(lambda P: len(P)<=14)
        v8   = self.frame.register(lambda P: len(P)<=8)

        # 1. MDAS_COD
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'),
                       justify="center", bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. MDAS_SWIFT
        lbl = tk.Label(self.frame, text="Swift:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=3, validate="key", validatecommand=(v3s, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. MDAS_NOMB
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=25, validate="key", validatecommand=(v25, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 4. MDAS_TACOM
        lbl = tk.Label(self.frame, text="TasaComercial:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=14, validate="key", validatecommand=(v14, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 5. MDAS_TAVEN
        lbl = tk.Label(self.frame, text="TasaVenta:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=14, validate="key", validatecommand=(v14, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 6. MDAS_FECHA
        lbl = tk.Label(self.frame, text="Fecha (YYYYMMDD):", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=8, validate="key", validatecommand=(v8, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
