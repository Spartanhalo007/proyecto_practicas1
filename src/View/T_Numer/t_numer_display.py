import tkinter as tk
from View.t_display import t_display

class t_numer_display(t_display):
    """Display de campos para la tabla t_numer."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v4   = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=4))
        v80  = self.frame.register(lambda P: len(P)<=80)
        v1   = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=1))
        v2   = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=2))

        # 1. NUM_CODIGO (4 dígitos num)
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=4, validate="key", validatecommand=(v4, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. NUM_CONCEP (80 chars)
        lbl = tk.Label(self.frame, text="Concepto:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=80, validate="key", validatecommand=(v80, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. NUM_INEGRE (1 dígito num)
        lbl = tk.Label(self.frame, text="I Negativo:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 4. NUM_FORM1 (1 dígito num)
        lbl = tk.Label(self.frame, text="Form1:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 5. NUM_FORM2
        lbl = tk.Label(self.frame, text="Form2:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 6. NUM_FORM3
        lbl = tk.Label(self.frame, text="Form3:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 7–19. NUM_DEST01 ... NUM_DEST13 (2 dígitos num cada uno)
        for i in range(1, 14):
            lbl = tk.Label(self.frame, text=f"Dest{i:02}:", font=("Arial",8,"bold"), bg="#c0c0c0")
            ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'),
                           bd=0, bg="white")
            self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 20. NUM_IC_IE (1 dígito num)
        lbl = tk.Label(self.frame, text="IC_IE:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 21. NUM_ACCION (1 char)
        vcmd_accion = self.frame.register(lambda P: len(P) <= 1)
        lbl_accion = tk.Label(self.frame, text="Acción:", font=("Arial", 8, "bold"), bg="#c0c0c0")
        ent_accion = tk.Entry(self.frame, width=1, validate="key", validatecommand=(vcmd_accion, '%P'), 
                              bd=0, bg="white")
        self.elements.append([lbl_accion, ent_accion])
        self.elements_types.append("str")

        # 22–25. NUM_RECE01, NUM_RECE02, NUM_INVE01, NUM_INVE02 (2 chars cada uno)
        for field,label in [("Rece01",22),("Rece02",23),("Inve01",24),("Inve02",25)]:
            lbl = tk.Label(self.frame, text=f"{field}:", font=("Arial",8,"bold"), bg="#c0c0c0")
            ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'),
                           bd=0, bg="white")
            self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 26–29. NUM_INVE03..NUM_INVE06 (2 chars)
        for i in range(3,7):
            lbl = tk.Label(self.frame, text=f"Inve0{i}:", font=("Arial",8,"bold"), bg="#c0c0c0")
            ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'),
                           bd=0, bg="white")
            self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 30. NUM_INVE07
        lbl = tk.Label(self.frame, text="Inve07:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 31. NUM_DIAN (1 dígito)
        lbl = tk.Label(self.frame, text="DIAN:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)
