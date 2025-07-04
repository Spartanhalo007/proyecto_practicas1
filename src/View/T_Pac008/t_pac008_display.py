import tkinter as tk
from View.t_display import t_display

def solo_numeros(P):
    return P == "" or (P.isdigit() and len(P) <= 7)

def solo_nivel(P):
    return P == "" or (P.isdigit() and len(P) <= 2)

class t_pac008_display(t_display):
    """Display de campos para la tabla t_pac008."""
    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        vcons = self.frame.register(solo_numeros)
        vniv  = self.frame.register(solo_nivel)
        vetiq = self.frame.register(lambda P: len(P) <= 200)
        vllav = self.frame.register(lambda P: len(P) <= 200)
        vcor  = self.frame.register(lambda P: len(P) <= 30)
        vvar  = self.frame.register(lambda P: len(P) <= 10)

        # 1. PC8_CONSE (7 dígitos numéricos)
        lbl = tk.Label(self.frame, text="Consecutivo:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=7, validate="key", validatecommand=(vcons, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. PC8_NIVEL (2 dígitos numéricos)
        lbl = tk.Label(self.frame, text="Nivel:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(vniv, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 3. PC8_ETIQUE (200 chars)
        lbl = tk.Label(self.frame, text="Etiqueta:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=50, validate="key", validatecommand=(vetiq, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 4. PC8_LLAVE (200 chars)
        lbl = tk.Label(self.frame, text="Llave:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=50, validate="key", validatecommand=(vllav, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 5. PC8_ETICOR (30 chars)
        lbl = tk.Label(self.frame, text="Etiqueta Corta:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=30, validate="key", validatecommand=(vcor, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 6. PC8_VARIA (10 chars)
        lbl = tk.Label(self.frame, text="Variable:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, validate="key", validatecommand=(vvar, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)