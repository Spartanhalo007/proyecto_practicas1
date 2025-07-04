import tkinter as tk
from View.t_display import t_display

def solo_numeros(P):
    return P == "" or (P.isdigit() and len(P) <= 2)

class t_acrede_display(t_display):
    """Display de campos para la tabla t_acrede."""
    def __init__(self, app):
        # Frame contenedor
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        # Elementos y tipos
        self.elements = []
        self.elements_types = []

        # Validador de código
        vcmd = self.frame.register(solo_numeros)

        # Campo ac_codigo
        lbl_codigo = tk.Label(self.frame, text="Código:", font=("Arial", 8, "bold"), bg="#c0c0c0")
        entry_codigo = tk.Entry(self.frame, width=2, validate="key", validatecommand=(vcmd, '%P'), bd=0, bg="white")
        entry_codigo.insert(0, "00")
        self.elements.append([lbl_codigo, entry_codigo])
        self.elements_types.append("num")

        # Campo ac_nombre
        lbl_nombre = tk.Label(self.frame, text="Nombre:", font=("Arial", 8, "bold"), bg="#c0c0c0")
        entry_nombre = tk.Entry(self.frame, width=45, bd=0, bg="white")
        self.elements.append([lbl_nombre, entry_nombre])
        self.elements_types.append("str")

        # Llamada a constructor de la clase base
        super().__init__(self.frame, self.elements, self.elements_types)

        #Edita los campos originales
        for lbl, entry, _ in self.elements:
            lbl.config(width=7, anchor="w")
            entry.grid_configure(padx=17)
