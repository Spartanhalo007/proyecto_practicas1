import tkinter as tk
from View.t_display import t_display

def validar_fecha(P):
    # hasta 6 dígitos numéricos: YYYYMM o similar
    return P == "" or (P.isdigit() and len(P) <= 6)

def validar_monto(P):
    # permite hasta 16 dígitos enteros y opcionalmente 2 decimales
    if P == "": return True
    try:
        # convierte a float y comprueba longitud antes/ después del punto
        parts = P.split('.')
        if not (len(parts[0]) <= 16 and (len(parts[1]) <= 2 if len(parts) == 2 else True)):
            return False
        float(P)
        return True
    except:
        return False

class t_patec_display(t_display):
    """Display de campos para la tabla t_patec."""
    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        vfecha = self.frame.register(validar_fecha)
        vmon   = self.frame.register(validar_monto)

        # 1. PT_FECHA (numérico 6)
        lbl = tk.Label(self.frame, text="Fecha (AAAMM):", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=6, validate="key", validatecommand=(vfecha, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. PT_VLR_USD (numérico 16,2)
        lbl = tk.Label(self.frame, text="Valor Patrim Tec en USD:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(vmon, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 3. PT_CON_USD (numérico 16,2)
        lbl = tk.Label(self.frame, text="Valor Patrim Tec Consolid en USD:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(vmon, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)

        for lbl, entry, _ in self.elements:
            lbl.config(width=28, anchor="w")
            entry.grid_configure(padx=10)

        
