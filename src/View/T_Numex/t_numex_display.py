import tkinter as tk
from View.t_display import t_display

class t_numex_display(t_display):
    """Display de campos para la tabla t_numex."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v4   = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=4))
        v80  = self.frame.register(lambda P: len(P)<=80)
        v1   = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=1))
        v4c  = self.frame.register(lambda P: len(P)<=4)
        v2   = self.frame.register(lambda P: len(P)<=2)

        # 1. NUM_CODIGO (4 dígitos)
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=4, validate="key", validatecommand=(v4, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. NUM_CONCEP (80 chars)
        lbl = tk.Label(self.frame, text="Concepto:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=80, validate="key", validatecommand=(v80, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3–6. NUM_INEGRE, NUM_FORM1–3 (1 dígito cada uno)
        for text in ["I Negativo:", "Form1:", "Form2:", "Form3:"]:
            lbl = tk.Label(self.frame, text=text, font=("Arial",8,"bold"), bg="#c0c0c0")
            ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1, '%P'),
                           bd=0, bg="white")
            self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 7–23. NUM_DESX01 .. NUM_DESX17 (4 chars cada uno)
        for i in range(1,18):
            lbl = tk.Label(self.frame, text=f"Desx{i:02}:", font=("Arial",8,"bold"), bg="#c0c0c0")
            ent = tk.Entry(self.frame, width=4, validate="key", validatecommand=(v4c, '%P'),
                           bd=0, bg="white")
            self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 24. NUM_TIPOIN (4 chars)
        lbl = tk.Label(self.frame, text="Tipo In:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=4, validate="key", validatecommand=(v4c, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 25. NUM_ACCION (1 char)
        v1c = self.frame.register(lambda P: len(P)<=1)
        lbl = tk.Label(self.frame, text="Acción:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1c, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 26–34. NUM_RECE01/02, NUM_INVE01–07 (2 chars cada uno)
        for text in ["Rece01","Rece02"] + [f"Inve0{i}" for i in range(1,8)]:
            lbl = tk.Label(self.frame, text=f"{text}:", font=("Arial",8,"bold"), bg="#c0c0c0")
            ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'),
                           bd=0, bg="white")
            self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 35. NUM_DIAN (1 dígito num)
        lbl = tk.Label(self.frame, text="Dian:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)
