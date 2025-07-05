import tkinter as tk
from View.t_display import t_display

def solo_numeros(P):
    return P == "" or (P.isdigit() and len(P) <= 7)

class t_cam053_display(t_display):
    """Display para t_cam053."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        vcmd = self.frame.register(solo_numeros)

        # 1. PC8_CONSE (7 dígitos)
        lbl1 = tk.Label(self.frame, text="Consecutivo:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry1 = tk.Entry(self.frame, width=7, validate="key", validatecommand=(vcmd, '%P'), bd=0, bg="white")
        self.elements.append([lbl1, entry1])
        self.elements_types.append("num")

        # 2. PC8_NIVEL (2 dígitos)
        lbl2 = tk.Label(self.frame, text="Nivel:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry2 = tk.Entry(self.frame, width=2, validate="key", validatecommand=(vcmd, '%P'), bd=0, bg="white")
        self.elements.append([lbl2, entry2])
        self.elements_types.append("num")

        # 3. PC8_ETIQUE (texto 145)
        lbl3 = tk.Label(self.frame, text="Etiqueta:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry3 = tk.Entry(self.frame, width=65, bd=0, bg="white")  # ancho visual
        self.elements.append([lbl3, entry3])
        self.elements_types.append("str")

        # 4. PC8_LLAVE (texto 145)
        lbl4 = tk.Label(self.frame, text="Llave:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry4 = tk.Entry(self.frame, width=65, bd=0, bg="white")
        self.elements.append([lbl4, entry4])
        self.elements_types.append("str")

        # 5. PC8_ETICOR (texto 30)
        lbl5 = tk.Label(self.frame, text="Etiqueta Corta:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry5 = tk.Entry(self.frame, width=30, bd=0, bg="white")
        self.elements.append([lbl5, entry5])
        self.elements_types.append("str")

        # 6. PC8_VARIA (texto 10)
        lbl6 = tk.Label(self.frame, text="Variable:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry6 = tk.Entry(self.frame, width=10, bd=0, bg="white")
        self.elements.append([lbl6, entry6])
        self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)

        for lbl,entry, _ in self.elements:
            lbl.config(fg="#004488")
