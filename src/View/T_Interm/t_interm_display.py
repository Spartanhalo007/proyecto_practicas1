import tkinter as tk
from View.t_display import t_display

class t_interm_display(t_display):
    """Display de campos para la tabla t_interm."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Registramos validadores
        v12 = self.frame.register(lambda P: P == "" or (P.isdigit() and len(P) <= 12))
        v80 = self.frame.register(lambda P: len(P) <= 80)
        v3  = self.frame.register(lambda P: len(P) <= 3)
        v4  = self.frame.register(lambda P: P == "" or (P.isdigit() and len(P) <= 4))
        v2  = self.frame.register(lambda P: P == "" or (P.isdigit() and len(P) <= 2))
        v1c = self.frame.register(lambda P: len(P) <= 1)

        # 1. IF_NIT
        lbl = tk.Label(self.frame, text="NIT:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key", validatecommand=(v12, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. IF_NOMBRE
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=80, validate="key", validatecommand=(v80, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. IF_CODCAR
        lbl = tk.Label(self.frame, text="CodCar:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=3, validate="key", validatecommand=(v3, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 4. IF_CODIGO
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=4, validate="key", validatecommand=(v4, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 5. IF_TIPOINT
        lbl = tk.Label(self.frame, text="TipoInt:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 6. IF_NOMTIPI
        lbl = tk.Label(self.frame, text="NomTipi:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v80, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 7. IF_IMC
        lbl = tk.Label(self.frame, text="IMC:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1c, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
