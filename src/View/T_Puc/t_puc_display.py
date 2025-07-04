import tkinter as tk
from View.t_display import t_display

def v_int(P, width):
    return P=="" or (P.isdigit() and len(P)<=width)

def v_str(P, width):
    return len(P)<=width

class t_puc_display(t_display):
    """Display de campos para la tabla t_puc."""
    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Registramos validadores genéricos
        v10n = self.frame.register(lambda P: v_int(P,10))
        v1n  = self.frame.register(lambda P: v_int(P,1))
        v40s = self.frame.register(lambda P: v_str(P,40))
        v1s  = self.frame.register(lambda P: v_str(P,1))

        # 1–2: PUC_CUENTA, PUC_CUENT (10 dígitos cada uno)
        for label,width,typ in [("Cuenta:",10,"num"),("Subcuenta:",10,"num")]:
            vcmd = v10n
            ent = tk.Entry(self.frame, width=width, validate="key", validatecommand=(vcmd,'%P'),
                           bd=0,bg="white")
            self.elements.append([tk.Label(self.frame,text=label,font=("Arial",8,"bold"),bg="#c0c0c0"),ent])
            self.elements_types.append("num")

        # 3. PUC_NOMBRE (40 chars)
        ent = tk.Entry(self.frame, width=40, validate="key", validatecommand=(v40s,'%P'),
                       bd=0,bg="white")
        self.elements.append([tk.Label(self.frame,text="Nombre:",font=("Arial",8,"bold"),bg="#c0c0c0"),ent])
        self.elements_types.append("str")

        # 4. PUC_NATURA (1 char)
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1s,'%P'),
                       bd=0,bg="white")
        self.elements.append([tk.Label(self.frame,text="Natura:",font=("Arial",8,"bold"),bg="#c0c0c0"),ent])
        self.elements_types.append("str")

        # 5–34: PUC_01 … PUC_30 (1 dígito cada uno)
        for i in range(1,31):
            lbl = f"{i:02}:"
            ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1n,'%P'),
                           bd=0,bg="white")
            self.elements.append([tk.Label(self.frame,text=lbl,font=("Arial",8,"bold"),bg="#c0c0c0"),ent])
            self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)
