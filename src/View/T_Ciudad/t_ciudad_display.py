import tkinter as tk
from View.t_display import t_display

def validar_numero(P, maxlen):
    return P == "" or (P.isdigit() and len(P) <= maxlen)

class t_ciudad_display(t_display):
    """Display de campos para la tabla t_ciudad."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores con distintos tamaños
        vcmd5 = self.frame.register(lambda P: validar_numero(P, 5))
        vcmd3 = self.frame.register(lambda P: validar_numero(P, 3))
        vcmd2 = self.frame.register(lambda P: validar_numero(P, 2))

        # 1. CIU_CODIGO (hasta 5 dígitos)
        lbl1 = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry1 = tk.Entry(self.frame, width=8, validate="key", validatecommand=(vcmd5, '%P'), bd=0, bg="white")
        self.elements.append([lbl1, entry1])
        self.elements_types.append("num")

        # 2. CIU_NOMBRE (texto 40)
        lbl2 = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry2 = tk.Entry(self.frame, width=51, bd=0, bg="white")
        self.elements.append([lbl2, entry2])
        self.elements_types.append("str")

        # 3. CIU_DEPTO (texto 40)
        lbl3 = tk.Label(self.frame, text="Departamento:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry3 = tk.Entry(self.frame, width=51, bd=0, bg="white")
        self.elements.append([lbl3, entry3])
        self.elements_types.append("str")

        # 4. CIU_INDICA (hasta 3 dígitos)
        lbl4 = tk.Label(self.frame, text="Indicativo:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry4 = tk.Entry(self.frame, width=6, validate="key", validatecommand=(vcmd3, '%P'), bd=0, bg="white")
        self.elements.append([lbl4, entry4])
        self.elements_types.append("num")

        # 5. CIU_UNISUP (hasta 2 dígitos)
        lbl5 = tk.Label(self.frame, text="Unidad Super:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry5 = tk.Entry(self.frame, width=3, validate="key", validatecommand=(vcmd2, '%P'), bd=0, bg="white")
        self.elements.append([lbl5, entry5])
        self.elements_types.append("num")

        # 6. CIU_COCISU (hasta 3 dígitos)
        lbl6 = tk.Label(self.frame, text="Subcuenta Super:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry6 = tk.Entry(self.frame, width=5, validate="key", validatecommand=(vcmd3, '%P'), bd=0, bg="white")
        self.elements.append([lbl6, entry6])
        self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)

        for lbl, entry, _ in self.elements:
            entry.grid_configure(padx=20)


