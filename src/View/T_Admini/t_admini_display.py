import tkinter as tk
from View.t_display import t_display

class t_admini_display(t_display):
    """Display de campos para la tabla t_admini."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores
        v12  = self.frame.register(lambda P: P=="" or (P.isdigit() and len(P)<=12))
        v35  = self.frame.register(lambda P: len(P)<=35)
        v10  = self.frame.register(lambda P: len(P)<=10)  # para fecha YYYY-MM-DD

        # 1. AD_NIT_ENT (12 dígitos num)
        lbl = tk.Label(self.frame, text="NIT Entidad Administrada:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key", validatecommand=(v12, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. AD_NOM_ENT (35 chars)
        lbl = tk.Label(self.frame, text="Nombre Entidad Administrada:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. AD_NIT_PRI (12 dígitos num)
        lbl = tk.Label(self.frame, text="NIT Entidad Administradora (Principal):", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key", validatecommand=(v12, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 4. AD_NOM_PRI (35 chars)
        lbl = tk.Label(self.frame, text="Nombre Entidad Administradora (Principal):", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
        #Edita los campos originales
        for lbl, entry, _ in self.elements:
            lbl.config(width=36, anchor="w")
            entry.grid_configure(padx=17)
