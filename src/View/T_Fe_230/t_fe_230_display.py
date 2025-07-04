import tkinter as tk
from View.t_display import t_display

class t_fe_230_display(t_display):
    """Display de campos para la tabla t_fe_230."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # No hay validación de formato de fecha aquí; se asume 'YYYY-MM-DD'
        # Permitimos 10 chars para fechas y 1 char para números
        vdate = self.frame.register(lambda P: len(P) <= 10)
        vnum  = self.frame.register(lambda P: P == "" or (P.isdigit() and len(P) <= 1))

        # 1. FE_DIA_PRO
        lbl = tk.Label(self.frame, text="Día Programado:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, validate="key", validatecommand=(vdate, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 2. FE_DIA_01
        lbl = tk.Label(self.frame, text="Día 01:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, validate="key", validatecommand=(vdate, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. FE_NRO_01
        lbl = tk.Label(self.frame, text="Número 01:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(vnum, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 4. FE_DIA_02
        lbl = tk.Label(self.frame, text="Día 02:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, validate="key", validatecommand=(vdate, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 5. FE_NRO_02
        lbl = tk.Label(self.frame, text="Número 02:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(vnum, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 6. FE_DIA_03
        lbl = tk.Label(self.frame, text="Día 03:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, validate="key", validatecommand=(vdate, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 7. FE_NRO_03
        lbl = tk.Label(self.frame, text="Número 03:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(vnum, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)
