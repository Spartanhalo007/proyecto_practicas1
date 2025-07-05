import tkinter as tk
from View.t_display import t_display

class t_tasas_display(t_display):
    """Display de campos para la tabla t_tasas."""

    def __init__(self, app, bg="#135547"):
        self.frame = tk.Frame(app, bg=bg)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v2  = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=2))
        v35 = self.frame.register(lambda P: len(P)<=35)
        v9  = self.frame.register(lambda P: P=="" or (all(c.isdigit() or c=='.' for c in P) and len(P)<=9))

        # 1. TASA_COD (2 dígitos num)
        lbl = tk.Label(self.frame, text="Código:", font=("Arial Black",8,"bold"), bg=bg)
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. TASA_NOMBR (35 chars)
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial Black",8,"bold"), bg=bg)
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. TASA_COTIZ (hasta 9 caracteres, dígitos y punto)
        lbl = tk.Label(self.frame, text="Cotización:", font=("Arial Black",8,"bold"), bg=bg)
        ent = tk.Entry(self.frame, width=9, validate="key", validatecommand=(v9, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types, bg=bg)
