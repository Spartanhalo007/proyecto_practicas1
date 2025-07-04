import os
import tkinter as tk
from tkinter import messagebox

class crud_display:

    def __init__(self, 
                 app: tk.Toplevel,
                 display,
                 c_func=lambda *args: None, 
                 r_func=lambda *args: [],
                 u_func=lambda *args: None, 
                 d_func=lambda *args: None, 
                 max_id_func=lambda: None, 
                 min_id_func=lambda: None,
                 table_atributes_func=lambda: [],
                 pk_func=lambda: None, 
                 pdf_func=lambda *args: None,
                 t_view=None
                 ):
        
        self.app = app
        self.min_id_func = min_id_func
        self.max_id_func = max_id_func
        self.table_atributes_func = table_atributes_func
        self.pk_func = pk_func
        self.t_view = t_view
        self.display = display[0]

        self.icons = self.cargar_iconos()

        datos = r_func()
        if datos:
            self.min_id = self.min_id_func()
            self.max_id = self.max_id_func()
            self.on_id = self.min_id
        else:
            self.min_id = self.max_id = self.on_id = 0

        bg = app.cget("bg")
        frame = tk.Frame(app, bg=bg)
        frame.pack(padx=1, pady=1)

        def get_info():
            return [entry.get() for entry in self.display.entries.values()]

        def set_info(data):
            if not data:
                messagebox.showinfo("Info", "No hay datos para mostrar")
                return
            for key, value in zip(self.display.entries.keys(), data):
                entry = self.display.entries[key]
                entry.delete(0, tk.END)
                entry.insert(0, value)

        def on_create():
            data = get_info()
            self.on_id = c_func(data)
            self.actualizar_rangos()

        def on_update():
            u_func(get_info())

        def on_delete():
            d_func(index=self.display.get_pk(), index_name=self.pk_func())
            self.actualizar_rangos()

        def on_first():
            record = r_func(index=None, index_name="first")
            record = record if isinstance(record[0], (int, float, str)) else record[0]
            self.on_id = record[0]
            set_info(record)

        def on_last():
            record = r_func(index=None, index_name="last")
            record = record if isinstance(record[0], (int, float, str)) else record[0]
            self.on_id = record[0]
            set_info(record)

        def on_back():
            id = self.on_id
            data = r_func(index=id, index_name="prev")
            if data != -1 and data:
                data = data if isinstance(data[0], (int, float, str)) else data[0]
                self.on_id = data[0]
                set_info(data)
            else:
                messagebox.showinfo("Info", "No hay registro anterior")

        def on_next():
            id = self.on_id
            data = r_func(index=id, index_name="next")
            if data != -1 and data:
                data = data if isinstance(data[0], (int, float, str)) else data[0]
                self.on_id = data[0]
                set_info(data)
            else:
                messagebox.showinfo("Info", "No hay registro siguiente")

        def on_browse():
            dialog = tk.Toplevel(app)
            dialog.title("Tabla de Registros")
            headings = table_atributes_func()
            data = r_func()

            for j, head in enumerate(headings):
                tk.Label(dialog, text=head, font=("Arial", 10, "bold")).grid(row=0, column=j)

            for i, row in enumerate(data, start=1):
                for j, item in enumerate(row):
                    lbl = tk.Label(dialog, text=item)
                    lbl.grid(row=i, column=j)
                    def handler(r=row):
                        set_info(r)
                        self.on_id = r[0]
                        dialog.destroy()
                    lbl.bind("<Button-1>", lambda e, h=handler: h())

        def on_pdf():
            pdf_func(r_func())

        def on_close():
            self.app.destroy()

        # Reglas según t_view.boton_archivo
        def solo_si_archivo_activo(funcion_real):
            def wrapper(*args, **kwargs):
                if getattr(self.t_view, 'boton_archivo', False):
                    return funcion_real(*args, **kwargs)
                else:
                    messagebox.showwarning("Advertencia", "Debe activar el archivo para esta acción.")
            return wrapper

        def solo_si_archivo_no_activo(funcion_real):
            def wrapper(*args, **kwargs):
                if not getattr(self.t_view, 'boton_archivo', False):
                    return funcion_real(*args, **kwargs)
                else:
                    messagebox.showwarning("Advertencia", "Esta acción no está permitida con el archivo activo.")
            return wrapper

        botones = {
            "Primero":   (self.icons["primero"], solo_si_archivo_no_activo(on_first)),
            "Anterior":  (self.icons["anterior"], solo_si_archivo_no_activo(on_back)),
            "Buscar":    (self.icons["buscar"], solo_si_archivo_no_activo(on_browse)),
            "Siguiente": (self.icons["siguiente"], solo_si_archivo_no_activo(on_next)),
            "Último":    (self.icons["ultimo"], solo_si_archivo_no_activo(on_last)),
            "Editar":    (self.icons["editar"], solo_si_archivo_no_activo(on_update)),
            "Eliminar":  (self.icons["eliminar"], solo_si_archivo_no_activo(on_delete)),
            "Guardar":   (self.icons["guardar"], solo_si_archivo_activo(on_create)),
            "Imprimir":  (self.icons["imprimir"], solo_si_archivo_no_activo(on_pdf)),
            "Close":     (self.icons["close"], on_close),
        }

        self.frame_botones(frame, botones)

    def frame_botones(self, frame, botones):
        separador_after = "Último"
        col = 0
        for texto, (icono, comando) in botones.items():
            b = tk.Button(frame, image=icono, command=comando, bg="#ffffff", activebackground="#a0a0a0",)
            b.grid(row=0, column=col, padx=5, pady=5)
            col += 1
            if texto == separador_after:
                tk.Frame(frame, width=20, bg=frame.cget("bg")).grid(row=0, column=col)
                col += 1

    def actualizar_rangos(self):
        self.min_id = self.min_id_func()
        self.max_id = self.max_id_func()

    def cargar_iconos(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        ruta = lambda nombre: os.path.join(base_dir, "iconos", nombre)
        nombres = {
            "guardar": "square.png",
            "editar": "edit.png",
            "eliminar": "delete.png",
            "primero": "rewind.png",
            "anterior": "Previus.png",
            "buscar": "search.png",
            "siguiente": "next.png",
            "ultimo": "last.png",
            "imprimir": "print.png",
            "close": "close.png",
            "file": "file.png"
        }
        iconos = {}
        for clave, archivo in nombres.items():
            try:
                iconos[clave] = tk.PhotoImage(file=ruta(archivo))
            except Exception as e:
                print(f"Error cargando ícono {archivo}: {e}")
                iconos[clave] = None
        return iconos
