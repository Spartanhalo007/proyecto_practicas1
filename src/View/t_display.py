import tkinter as tk

class t_display:

    def __init__(self, frame, elements, elements_types, bg="#c0c0c0"):
        """Inicializa el display: crea labels, entries y mensajes de validación."""
        self.frame = frame
        self.elements = elements
        self.elements_types = elements_types
        self.combo_index = 0

        bg = bg or "#c0c0c0"
        self.frame.configure(bg=bg)
        self.entries = {}

        row = 0  # Controla solo las filas que se pintan realmente

        for i, ((lbl, entry), tipo) in enumerate(zip(self.elements, self.elements_types)):

            if lbl is not None:
                lbl.config(width=18, anchor="w", bg=bg)
                lbl.grid(row=row, column=0, padx=25, pady=3)

                entry.config(highlightthickness=1, highlightcolor="black", highlightbackground="black",
                             justify="right", bg="white")
                entry.grid(row=row, column=1, padx=5, pady=3, sticky="w")

                lbl_mensaje = tk.Label(self.frame, text="", font=("Arial", 8, "bold"), bg=bg)
                lbl_mensaje.grid(row=row, column=2, padx=3, pady=3)

                row += 1  # Solo incrementa fila si se dibujó
            else:
                # No se pinta la fila, pero se crea un mensaje de validación dummy
                lbl_mensaje = tk.Label(self.frame)  # sin .grid()

            self.elements[i].append(lbl_mensaje)
            self.entries[i] = entry

    def get_info(self):
        """Devuelve lista con valores validados; retorna -1 si falla."""
        self.combo_index = 0
        info = []
        for i in range(len(self.elements)):
            valor = self.elements[i][1].get()
            tipo = self.elements_types[i]
            lbl_msg = self.elements[i][2]
            validado = self.check_type(valor, tipo, lbl_msg)
            if validado == -1:
                return -1
            info.append(validado)
        return info

    def check_type(self, info, tipo, message_label):
        """Valida el tipo de info y retorna convertido o muestra error."""
        if tipo == "num":
            try:
                return int(info)
            except ValueError:
                message_label.configure(text="Este valor debe ser numerico")
                return -1
        elif tipo == "combo":
            print(f"t_display: {info}")
        return info

    def get_pk(self):
        """Retorna la clave primaria validada del primer entry."""
        valor = self.elements[0][1].get()
        tipo = self.elements_types[0]
        lbl_msg = self.elements[0][2]
        return self.check_type(valor, tipo, lbl_msg)

    def set_info(self, info):
        """Carga los valores en los entries."""
        for i in range(len(info)):
            entry = self.elements[i][1]
            entry.delete(0, tk.END)
            entry.insert(0, info[i])

    def clear(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

