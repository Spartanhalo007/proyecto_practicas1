import tkinter as tk
from View.t_display import t_display

def v_tp(P):
    return P == "" or (P.isdigit() and len(P) <= 2)

def v_tpn(P):
    return len(P) <= 50

def v_cod(P):
    return len(P) <= 20

def v_dv(P):
    return P == "" or (P.isdigit() and len(P) <= 1)

def v_nom(P):
    return len(P) <= 35

def v_dir(P):
    return len(P) <= 35

def v_tel(P):
    return len(P) <= 35

def v_ciudad(P):
    return len(P) <= 35

def v_pais(P):
    return len(P) <= 2

def v_nopais(P):
    return len(P) <= 35

def v_fecha(P):
    return len(P) <= 8

class t_provee_display(t_display):
    """Display de campos para la tabla t_provee."""
    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Registrar validadores
        v_tp_cmd     = self.frame.register(v_tp)
        v_tpn_cmd    = self.frame.register(v_tpn)
        v_cod_cmd    = self.frame.register(v_cod)
        v_dv_cmd     = self.frame.register(v_dv)
        v_nom_cmd    = self.frame.register(v_nom)
        v_dir_cmd    = self.frame.register(v_dir)
        v_tel_cmd    = self.frame.register(v_tel)
        v_ciud_cmd   = self.frame.register(v_ciudad)
        v_pais_cmd   = self.frame.register(v_pais)
        v_nop_cmd    = self.frame.register(v_nopais)
        v_fecha_cmd  = self.frame.register(v_fecha)

        # 1. PR_TP
        lbl = tk.Label(self.frame, text="Tipo Docum Cod:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v_tp_cmd, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. PR_TPNOM
        lbl = tk.Label(self.frame, text="Tipo Docum:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=50, validate="key", validatecommand=(v_tpn_cmd, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 3. PR_CODIGO
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v_cod_cmd, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 4. PR_DV
        lbl = tk.Label(self.frame, text="DV:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v_dv_cmd, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 5. PR_NOMBRE
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v_nom_cmd, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 6. PR_DIRECC
        lbl = tk.Label(self.frame, text="Dirección:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v_dir_cmd, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 7. PR_TELEF
        lbl = tk.Label(self.frame, text="Teléfono:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v_tel_cmd, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 8. PR_CIUDAD
        lbl = tk.Label(self.frame, text="Ciudad:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v_ciud_cmd, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 9. PR_PAIS
        lbl = tk.Label(self.frame, text="Cod País:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v_pais_cmd, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 10. PR_NOPAIS
        lbl = tk.Label(self.frame, text="Nombre País:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v_nop_cmd, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 11. PR_FECHA
        lbl = tk.Label(self.frame, text="Fecha:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=8, validate="key", validatecommand=(v_fecha_cmd, '%P'),
                       bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        super().__init__(self.frame, self.elements, self.elements_types)
