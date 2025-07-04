import tkinter as tk
from View.t_display import t_display

class t_sucur_display(t_display):
    """Display de campos para la tabla t_sucur."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v1   = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=1))
        v3   = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=3))
        v4   = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=4))
        v20  = self.frame.register(lambda P: len(P)<=20)
        v25  = self.frame.register(lambda P: len(P)<=25)
        v30  = self.frame.register(lambda P: len(P)<=30)
        v35  = self.frame.register(lambda P: len(P)<=35)

        # 1. SUC_MARCA
        lbl = tk.Label(self.frame, text="Marca:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. SUC_NOMARC
        lbl = tk.Label(self.frame, text="Nombre Marca:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. SUC_CODIGO (pk)
        lbl = tk.Label(self.frame, text="Código Sucursal:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=4,  validate="key", validatecommand=(v4,'%P'),  bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 4. SUC_REGION
        lbl = tk.Label(self.frame, text="Región:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=3, validate="key", validatecommand=(v3,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 5. SUC_NOMREG
        lbl = tk.Label(self.frame, text="Nombre Región:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=30, validate="key", validatecommand=(v30,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 6. SUC_ZONA
        lbl = tk.Label(self.frame, text="Zona:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=3, validate="key", validatecommand=(v3,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 7. SUC_NOMZON
        lbl = tk.Label(self.frame, text="Nombre Zona:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=30, validate="key", validatecommand=(v30,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 8. SUC_NOMBRE
        lbl = tk.Label(self.frame, text="Nombre Suc.:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=25, validate="key", validatecommand=(v25,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 9. SUC_GERENT
        lbl = tk.Label(self.frame, text="Gerente:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 10. SUC_SUC_DG
        lbl = tk.Label(self.frame, text="Suc. DG:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 11. SUC_CIUDAD
        lbl = tk.Label(self.frame, text="Código Ciudad:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=5, validate="key", validatecommand=(self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=5)),'%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 12. SUC_NOMCIU
        lbl = tk.Label(self.frame, text="Nombre Ciudad:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=25, validate="key", validatecommand=(v25,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
