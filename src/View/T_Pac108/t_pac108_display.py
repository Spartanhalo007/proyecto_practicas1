import tkinter as tk
from View.t_display import t_display

def solo_numeros(P):
    return P == "" or (P.isdigit() and len(P) <= 7)

def solo_nivel(P):
    return P == "" or (P.isdigit() and len(P) <= 2)

class t_pac108_display(t_display):
    """Display de campos para la tabla t_pac108."""
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

        # Campos idénticos a T_PAC008
        # PC8_CONSE
        lbl = tk.Label(self.frame, text="Consecutivo:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=7, validate="key", validatecommand=(vcons, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # PC8_NIVEL
        lbl = tk.Label(self.frame, text="Nivel:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(vniv, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # PC8_ETIQUE
        lbl = tk.Label(self.frame, text="Etiqueta:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=50, validate="key", validatecommand=(vetiq, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # PC8_LLAVE
        lbl = tk.Label(self.frame, text="Llave:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=50, validate="key", validatecommand=(vllav, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # PC8_ETICOR
        lbl = tk.Label(self.frame, text="Etiqueta Corta:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=30, validate="key", validatecommand=(vcor, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # PC8_VARIA
        lbl = tk.Label(self.frame, text="Variable:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, validate="key", validatecommand=(vvar, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)