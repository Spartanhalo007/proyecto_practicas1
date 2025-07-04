import tkinter as tk
from View.t_display import t_display

class t_festiv_display(t_display):
    """Display de campos para la tabla t_festiv."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # validadores para numérico con hasta 4,2 dígitos
        v4 = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=4))
        v2 = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=2))

        # 1. FE_AÑO
        lbl = tk.Label(self.frame, text="Año:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=4, validate="key", validatecommand=(v4, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. FE_MES
        lbl = tk.Label(self.frame, text="Mes:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 3. FE_DIA
        lbl = tk.Label(self.frame, text="Día:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 4. FE_COL
        lbl = tk.Label(self.frame, text="Festivo en COL:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v2, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 5. FE_USA
        lbl = tk.Label(self.frame, text="Festivo en USA:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v2, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)
