import tkinter as tk
from View.t_display import t_display

def validar_num(P, maxlen):
    return P == "" or (P.isdigit() and len(P) <= maxlen)

class t_corr_display(t_display):
    """Display de campos para la tabla t_corr."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v4  = self.frame.register(lambda P: validar_num(P, 4))
        v11 = self.frame.register(lambda P: len(P) <= 11)
        v3  = self.frame.register(lambda P: len(P) <= 3)
        v35 = self.frame.register(lambda P: len(P) <= 35)
        v2  = self.frame.register(lambda P: len(P) <= 2)
        v9  = self.frame.register(lambda P: validar_num(P, 9))
        v20 = self.frame.register(lambda P: len(P) <= 20)

        # 1. COR_COD
        lbl = tk.Label(self.frame, text="Código Contable:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=4, validate="key", validatecommand=(v4,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. COR_SWIFT
        lbl = tk.Label(self.frame, text="Código SWIFT:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=11, validate="key", validatecommand=(v11,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. COR_MDA
        lbl = tk.Label(self.frame, text="Cód Moneda:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=3, validate="key", validatecommand=(v3,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 4. COR_NOMB
        lbl = tk.Label(self.frame, text="Nombre Corresp:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 5. COR_DIR
        lbl = tk.Label(self.frame, text="Dirección Corresp:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 6. COR_CIUD
        lbl = tk.Label(self.frame, text="Ciudad:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 7. COR_COPAIS
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2,'%P'), bd=0, bg="white")
        self.elements.append([None, ent]); self.elements_types.append("str")

        # 8. COR_PAIS
        lbl = tk.Label(self.frame, text="País:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 9. COR_COSUPE
        lbl = tk.Label(self.frame, text="Cod Super:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=5, validate="key", validatecommand=(lambda P: validar_num(P,5),'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 10. COR_ABA
        lbl = tk.Label(self.frame, text="Codigo ABA:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=9, validate="key", validatecommand=(v9,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 11. COR_CTA
        lbl = tk.Label(self.frame, text="Cuenta Corriente:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 12. COR_CNV
        lbl = tk.Label(self.frame, text="Convenio/Ordinario:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(lambda P: validar_num(P,1),'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)

