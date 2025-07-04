import tkinter as tk
from View.t_display import t_display

def v_num(P, width):
    return P == "" or (P.isdigit() and len(P) <= width)

def v_str(P, width):
    return len(P) <= width

class t_razone_display(t_display):
    """Display de campos para la tabla t_razone."""
    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v2 = self.frame.register(lambda P: v_num(P,2))
        v100 = self.frame.register(lambda P: v_str(P,100))

        # 1. RAZ_CODIGO (2 dígitos numéricos)
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. RAZ_NOMBRE (100 caracteres)
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=50, validate="key", validatecommand=(v100, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3–8. RAZ_PROPR1 .. RAZ_PROPR6 (2 dígitos cada uno)
        for i in range(1,7):
            lbl = tk.Label(self.frame, text=f"PropR{i}:", font=("Arial",8,"bold"), bg="#c0c0c0")
            ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'),
                           bd=0, bg="white")
            self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 9–13. RAZ_NUMER1 .. RAZ_NUMER5 (4 dígitos cada uno)
        v4 = self.frame.register(lambda P: v_num(P,4))
        for i in range(1,6):
            lbl = tk.Label(self.frame, text=f"Numer{i}:", font=("Arial",8,"bold"), bg="#c0c0c0")
            ent = tk.Entry(self.frame, width=4, validate="key", validatecommand=(v4, '%P'),
                           bd=0, bg="white")
            self.elements.append([lbl, ent]); self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)
