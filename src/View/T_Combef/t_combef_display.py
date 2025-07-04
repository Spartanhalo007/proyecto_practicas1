import tkinter as tk
from View.t_display import t_display

def validar_num(P, maxlen):
    return P == "" or (P.isdigit() and len(P) <= maxlen)

class t_comdef_display(t_display):
    """Display de campos para la tabla t_comdef."""

    def __init__(self, app, bg="#135547"):
        self.frame = tk.Frame(app, bg=bg)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v4  = self.frame.register(lambda P: validar_num(P, 4))
        v35 = self.frame.register(lambda P: len(P) <= 35)

        # 1. COM_CODIGO
        lbl = tk.Label(self.frame, text="Código:", font=("Arial Black",9,"bold"), bg=bg)
        ent = tk.Entry(self.frame, width=8, validate="key", validatecommand=(v4,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. COM_NOMBR
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial Black",9,"bold"), bg=bg)
        ent = tk.Entry(self.frame, width=40, validate="key", validatecommand=(v35,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. COM_PORCE
        lbl = tk.Label(self.frame, text="Porcentaje:", font=("Arial Black",9,"bold"), bg=bg)
        ent = tk.Entry(self.frame, width=12, bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("dec")

        # 4. COM_MINIMA
        lbl = tk.Label(self.frame, text="Mínima en USD:", font=("Arial Black",9,"bold"), bg=bg)
        ent = tk.Entry(self.frame, width=16, bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("dec")

        # 5. COM_FIJA
        lbl = tk.Label(self.frame, text="Costo Fijo en USD:", font=("Arial Black",9,"bold"), bg=bg)
        ent = tk.Entry(self.frame, width=16, bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("dec")

        # 6. COM_MENSA
        lbl = tk.Label(self.frame, text="VI mens o Cheq USD:", font=("Arial Black",9,"bold"), bg=bg)
        ent = tk.Entry(self.frame, width=16, bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("dec")

        # 7. COM_GTOS
        lbl = tk.Label(self.frame, text="Gtos en pesos:", font=("Arial Black",9,"bold"), bg=bg)
        ent = tk.Entry(self.frame, width=16, bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("dec")

        # 8. COM_PORIVA
        lbl = tk.Label(self.frame, text="Porcent IVA:", font=("Arial Black",9,"bold"), bg=bg)
        ent = tk.Entry(self.frame, width=12, bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("dec")

        super().__init__(self.frame, self.elements, self.elements_types, bg=bg)
