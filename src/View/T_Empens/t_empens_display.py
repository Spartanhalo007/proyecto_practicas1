import tkinter as tk
from View.t_display import t_display

def validar_num(P, maxlen):
    return P == "" or (P.isdigit() and len(P) <= maxlen)

class t_empens_display(t_display):
    """Display de campos para la tabla t_empens."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        v12 = self.frame.register(lambda P: validar_num(P, 12))
        v1  = self.frame.register(lambda P: validar_num(P, 1))
        v35 = self.frame.register(lambda P: len(P) <= 35)
        v2  = self.frame.register(lambda P: validar_num(P, 2))
        v20 = self.frame.register(lambda P: validar_num(P, 20))
        v4  = self.frame.register(lambda P: validar_num(P, 4))
        v5  = self.frame.register(lambda P: validar_num(P, 5))

        # 1. PEN_NIT
        lbl = tk.Label(self.frame, text="NIT:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key", validatecommand=(v12,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. PEN_DV
        lbl = tk.Label(self.frame, text="DV:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 3. PEN_NOMBRE
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 4. PEN_CODIGO
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 5. PEN_CUENTA
        lbl = tk.Label(self.frame, text="Cuenta No:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key", validatecommand=(v12,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 6. PEN_DIRECC
        lbl = tk.Label(self.frame, text="Dirección:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 11. PEN_TELEF
        lbl = tk.Label(self.frame, text="Teléfono:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 7. PEN_COCIU
        lbl = tk.Label(self.frame, text="", font=("Arial",8,"bold"), bg="#c0c0c0") # debe ir ewn la misma linea que Ciudad
        ent = tk.Entry(self.frame, width=5, validate="key", validatecommand=(v5,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 8. PEN_CIUDAD
        lbl = tk.Label(self.frame, text="Ciudad:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 9. PEN_COPAIS
        lbl = tk.Label(self.frame, text="", font=("Arial",8,"bold"), bg="#c0c0c0") # debe ir en la misma linea que Pais
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(self.frame.register(lambda P: len(P)<=2),'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 10. PEN_PAIS
        lbl = tk.Label(self.frame, text="País:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(self.frame.register(lambda P: len(P)<=35),'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 12. PEN_OFICOD
        lbl = tk.Label(self.frame, text="", font=("Arial",8,"bold"), bg="#c0c0c0") # debe ir en la misma linea que Oficina
        ent = tk.Entry(self.frame, width=4, validate="key", validatecommand=(v4,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 13. PEN_OFINOM
        lbl = tk.Label(self.frame, text="Oficina Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 14. PEN_MEN_US
        lbl = tk.Label(self.frame, text="Comisión USD:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=5, validate="key", validatecommand=(v5,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 15. PEN_PORIVA
        lbl = tk.Label(self.frame, text="% IVA:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=5, validate="key", validatecommand=(v5,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)
