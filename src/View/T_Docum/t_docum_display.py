import tkinter as tk
from View.t_display import t_display

class t_docum_display(t_display):
    """Display de campos para la tabla t_docum."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores de longitud para textos memo (permitimos hasta 255 here, ajuste si necesario)
        v2   = self.frame.register(lambda P: P.isdigit() and len(P) <= 2 or P == "")
        # Para memo no validamos caracteres, solo longitud
        vmax = self.frame.register(lambda P: len(P) <= 255)

        # 1. DOCU_CODIG
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. DOCU_NOM_E
        lbl = tk.Label(self.frame, text="Nombre Español:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=60, validate="key", validatecommand=(vmax,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. DOCU_NOM_I
        lbl = tk.Label(self.frame, text="Nombre Inglés:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=60, validate="key", validatecommand=(vmax,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 4. DOCU_NOM_F
        lbl = tk.Label(self.frame, text="Nombre Francés:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=60, validate="key", validatecommand=(vmax,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 5. DOCU_NOM_A
        lbl = tk.Label(self.frame, text="Nombre Alemán:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=60, validate="key", validatecommand=(vmax,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
