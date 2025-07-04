import tkinter as tk
from View.t_display import t_display

def validar_long(P, maxlen):
    return len(P) <= maxlen

class t_corswi_display(t_display):
    """Display de campos para la tabla t_corswi."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Validadores de longitud
        v8   = self.frame.register(lambda P: validar_long(P, 8))
        v3   = self.frame.register(lambda P: validar_long(P, 3))
        v35  = self.frame.register(lambda P: validar_long(P, 35))
        v9   = self.frame.register(lambda P: validar_long(P, 9))
        v1   = self.frame.register(lambda P: validar_long(P, 1))

        # 1. BIC_CODSWI
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=8, validate="key", validatecommand=(v8, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 2. BIC_SUCSWI
        lbl = tk.Label(self.frame, text=" Ext Sucursal:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=3, validate="key", validatecommand=(v3, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. BIC_NOM01
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 4. BIC_DIR01
        lbl = tk.Label(self.frame, text="Dirección:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 5. BIC_CIUDAD
        lbl = tk.Label(self.frame, text="Ciudad:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 6. BIC_COPAIS
        lbl = tk.Label(self.frame, text="", font=("Arial",8,"bold"), bg="#c0c0c0") #debe ir en la misma linea que Pais
        ent = tk.Entry(self.frame, width=3, validate="key", validatecommand=(v3, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 7. BIC_NOPAIS
        lbl = tk.Label(self.frame, text="País:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 8. BIC_ABBA
        lbl = tk.Label(self.frame, text="Codigo ABBA:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=9, validate="key", validatecommand=(v9, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 9. BIC_DOBLE
        lbl = tk.Label(self.frame, text="Doble:", font=("Arial",8,"bold"), bg="#c0c0c0") # no esta en la screenshot proporcionada
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
