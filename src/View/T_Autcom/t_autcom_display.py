import tkinter as tk
from View.t_display import t_display

def solo_numeros(P):
    # hasta 2 dígitos para ac_nivel_c
    return P == "" or (P.isdigit() and len(P) <= 2)

class t_autcom_display(t_display):
    """Display de campos para la tabla t_autcom."""

    def __init__(self, app, ent_codigo, ent_nombre, ent_mensual_b, ent_anual_b, ent_mensual_c, ent_anual_c):

        self.frame = tk.Frame(app, bg="#c0c0c0")
        self.frame.pack()

        self.elements = []
        self.elements_types = []

        self.elements.append([None, ent_codigo])
        self.elements_types.append("num")

        self.elements.append([None, ent_nombre])
        self.elements_types.append("str")

        self.elements.append([None, ent_mensual_b])
        self.elements_types.append("num")

        self.elements.append([None, ent_anual_b])
        self.elements_types.append("num")

        self.elements.append([None, ent_mensual_c])
        self.elements_types.append("num")

        self.elements.append([None, ent_anual_c])
        self.elements_types.append("num")

        super().__init__(self.frame, self.elements, self.elements_types)
        
        for item in self.elements:
            if len(item) >= 2:
                lbl, entry = item[0], item[1]
                if lbl:
                    lbl.grid_forget()

