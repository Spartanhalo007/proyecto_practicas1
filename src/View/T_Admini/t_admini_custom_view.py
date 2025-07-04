import os
import tkinter as tk
from tkinter import Frame, Label, Button, X, LEFT, messagebox

from View.Components.crud_display import crud_display
from Repository.conexion_bd import obtener_conexion
from Service.admini_service import AdminiService
from View.T_Admini.t_admini_custom_display import t_admini_display


class t_admini_custom_view:

    boton_archivo = False

    def on_boton_archivo(self):
        self.boton_archivo = not self.boton_archivo
        if self.boton_archivo:
            self.left_button.config(bg="#a0a0a0")  # Color más oscuro al activar
        else:
            self.left_button.config(bg="SystemButtonFace")  # Color por defecto        
    
    def __init__(self, root):
        self.app = tk.Toplevel(root)
        self.app.title("t_admini")
        self.app.geometry("600x250")
        self.app.configure(bg="#c0c0c0")

        conexion = obtener_conexion()
        self.service = AdminiService(conexion)

        self.button_img = self._cargar_icono("file.png")

        header_top = Frame(self.app, bg="#c0c0c0")
        header_top.pack(fill=X, padx=5, pady=(10, 0))

        self.left_button = Button(
            header_top,
            image=self.button_img,
            text="Archivo" if self.button_img is None else "",
            compound=LEFT if self.button_img else None,
            font=("Arial", 10, "bold"),
            relief="raised",
            borderwidth=2,
            command=self.on_boton_archivo,
        )
        self.left_button.pack(side=LEFT, padx=(0, 10))

        self.title_label = Label(
            header_top,
            text="Tabla de Empresas Administradas",
            font=("Arial", 14, "bold"),
            bg="#c0c0c0",
            fg="#000080",
            anchor="center",
        )
        self.title_label.pack(side=LEFT, fill=X, expand=True)

        # Campo fecha centrado
        header_date = Frame(self.app, bg="#c0c0c0")
        header_date.pack(fill=X, padx=5, pady=(5, 10))
        center_date = Frame(header_date, bg="#c0c0c0")
        center_date.pack()

        self.ent_fecha = tk.Entry(
            center_date,
            width=10,
            justify="right",
            highlightthickness=1,
            highlightcolor="black",
            highlightbackground="black",
            relief="flat",
            bg="white",
        )
        self.ent_fecha.pack(side=LEFT)

        Frame(self.app, height=2, bd=1, relief="sunken", bg="#c0c0c0").pack(
            fill="x", padx=5, pady=5
        )
        self.display_frame = t_admini_display(self.app, self.ent_fecha)
        Frame(self.app, height=2, bd=1, relief="sunken", bg="#c0c0c0").pack(
            fill="x", padx=5, pady=5
        )

        def _build_payload(vals):
            return {
                "ad_nit_ent": int(vals[0]),
                "ad_nom_ent": vals[1],
                "ad_nit_pri": int(vals[2]),
                "ad_nom_pri": vals[3],
                "ad_fecha": self.ent_fecha.get().strip(),
            }

        def guardar(vals):
                payload = _build_payload(vals)
                exito = self.service.create(payload)
                if exito:
                    messagebox.showinfo("Guardado", "Registro guardado exitosamente.")
                else:
                    messagebox.showerror("Error", "No se pudo guardar el registro.")

        def actualizar(vals):
                pk = self.display_frame.get_pk()
                payload = {
                    "ciu_nombre": vals[1],
                    "ciu_depto":  vals[2],
                    "ciu_indica": int(vals[3]),
                    "ciu_unisup": int(vals[4]),
                    "ciu_cocisu": int(vals[5]),
                }
                exito = self.service.update(int(pk), payload)
                if exito:
                    messagebox.showinfo("Actualización", "Registro actualizado exitosamente.")
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el registro.")

        def eliminar(index=None, index_name=None):
                pk = self.display_frame.get_pk()
                exito = self.service.delete(int(pk))
                if exito:
                    messagebox.showinfo("Eliminado", "Registro eliminado exitosamente.")
                    self.display_frame.clear()
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el registro.")

        crud_display(
            app=self.app,
            display=[self.get_display()],
            c_func=guardar,
            r_func=lambda index=None, index_name=None: (
                                     [self.service.first()] if index_name=="first" else
                                     [self.service.last()]  if index_name=="last"  else
                                     [self.service.prev(index)] if index_name=="prev" else
                                     [self.service.next(index)] if index_name=="next" else
                                     self.service.browse()
                                 ),
            u_func=actualizar,
            d_func=eliminar,
            min_id_func=lambda: self.service.first()[0],
            max_id_func=lambda: self.service.last()[0],
            table_atributes_func=lambda: [
                "ad_nit_ent",
                "ad_nom_ent",
                "ad_nit_pri",
                "ad_nom_pri",
                "ad_fecha",
            ],
            pk_func=lambda: "ad_nit_ent",
            pdf_func=lambda data: print("PDF con", data),
            t_view=self,
        )

    def _cargar_icono(self, filename):
        ruta = os.path.join(os.path.dirname(os.path.dirname(__file__)), "iconos", filename)
        try:
            return tk.PhotoImage(file=ruta)
        except Exception as e:
            print(f"Error cargando ícono {filename}: {e}")
            return None

    def get_display(self):
        return self.display_frame

