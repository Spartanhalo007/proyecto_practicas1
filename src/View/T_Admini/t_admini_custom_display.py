import tkinter as tk
from View.t_display import t_display

class t_admini_display(t_display):

    def __init__(self, app, entry_fecha=None):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements        = []
        self.elements_types  = []

        v12 = self.frame.register(lambda P: P == "" or (P.isdigit() and len(P) <= 12))
        v35 = self.frame.register(lambda P: len(P) <= 35)

        # 1. AD_NIT_ENT
        lbl = tk.Label(self.frame, text="NIT Entidad Administrada:",
                       font=("Arial", 8, "bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key",
                       validatecommand=(v12, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. AD_NOM_ENT
        lbl = tk.Label(self.frame, text="Nombre Entidad Administrada:",
                       font=("Arial", 8, "bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key",
                       validatecommand=(v35, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. AD_NIT_PRI
        lbl = tk.Label(self.frame, text="NIT Entidad Administradora (Principal):",
                       font=("Arial", 8, "bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key",
                       validatecommand=(v12, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 4. AD_NOM_PRI
        lbl = tk.Label(self.frame, text="Nombre Entidad Administradora (Principal):",
                       font=("Arial", 8, "bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key",
                       validatecommand=(v35, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 5. AD_FECHA  (recibido externamente)
        if entry_fecha is not None:
            self.elements.append([None, entry_fecha])
            self.elements_types.append("str")

            # lo ocultamos para que no se vea duplicado
            lbl.grid_forget()
            entry_fecha.grid_forget()

        # === Estilo general ===
        super().__init__(self.frame, self.elements, self.elements_types)
        for item in self.elements:
            lbl, entry, *_ = item
            if lbl:  # Solo si hay label (evita None del campo fecha)
                lbl.config(width=36, anchor="w")
            entry.grid_configure(padx=17)
