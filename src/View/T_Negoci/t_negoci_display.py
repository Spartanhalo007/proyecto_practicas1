import tkinter as tk
from View.t_display import t_display

class t_negoci_display(t_display):
    """Display de campos para la tabla t_negoci."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v12  = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=12))
        v30  = self.frame.register(lambda P: len(P)<=30)
        v8   = self.frame.register(lambda P: len(P)<=8)
        v2   = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=2))
        v16  = self.frame.register(lambda P: len(P)<=16)

        # 1. NG_NIT
        lbl = tk.Label(self.frame, text="NIT:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key", validatecommand=(v12, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. NG_NOMBRE
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=30, validate="key", validatecommand=(v30, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. NG_CODIGO
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=8, validate="key", validatecommand=(v8, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 4. NG_CONSE
        lbl = tk.Label(self.frame, text="Consecutivo:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 5. NG_MTOMIN
        lbl = tk.Label(self.frame, text="Monto Mínimo:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=16, validate="key", validatecommand=(v16, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
