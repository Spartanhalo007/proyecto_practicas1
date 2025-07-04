import tkinter as tk
from View.t_display import t_display

def validar_num(P, maxlen):
    return P == "" or (P.isdigit() and len(P) <= maxlen)

class t_coraba_display(t_display):
    """Display de campos para la tabla t_coraba."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v9  = self.frame.register(lambda P: validar_num(P, 9))
        v40 = self.frame.register(lambda P: len(P) <= 40)
        v2  = self.frame.register(lambda P: len(P) <= 2)
        v25 = self.frame.register(lambda P: len(P) <= 25)

        # 1. ABA_CODIGO
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=9, validate="key", validatecommand=(v9,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. ABA_NOMBRE
        lbl = tk.Label(self.frame, text="Aba_nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=40, validate="key", validatecommand=(v40,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. ABA_ESTADO
        lbl = tk.Label(self.frame, text="Aba_estado:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 4. ABA_CIUDAD
        lbl = tk.Label(self.frame, text="Aba_ciudad:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=25, validate="key", validatecommand=(v25,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)

        #Edita los campos originales
        for lbl, entry, _ in self.elements:
            lbl.config(width=11, anchor="w")
            entry.grid_configure(padx=17)
