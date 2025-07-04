import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.ciudad_service import CiudadService

from View.T_Ciudad.t_ciudad_display import t_ciudad_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_ciudad_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de Ciudades de Colombia"
        self.app = tk.Toplevel(root)
        self.app.title("t_ciudad")

        self.h = 265
        self.w = 570

        self.data_display_frame = t_ciudad_display

        conexion = obtener_conexion()
        self.service = CiudadService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "ciu_codigo": int(vals[0]),
                "ciu_nombre": vals[1],
                "ciu_depto":  vals[2],
                "ciu_indica": int(vals[3]),
                "ciu_unisup": int(vals[4]),
                "ciu_cocisu": int(vals[5]),
            }
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
            app                  = self.app,
            display              = [self.get_display()],
            c_func               = guardar,
            r_func               = lambda index=None, index_name=None: (
                                     [self.service.first()] if index_name=="first" else
                                     [self.service.last()]  if index_name=="last"  else
                                     [self.service.prev(index)] if index_name=="prev" else
                                     [self.service.next(index)] if index_name=="next" else
                                     self.service.browse()
                                 ),
            u_func               = actualizar,
            d_func               = eliminar,
            min_id_func          = lambda: self.service.first()[0],
            max_id_func          = lambda: self.service.last()[0],
            table_atributes_func = lambda: [
                "ciu_codigo","ciu_nombre","ciu_depto",
                "ciu_indica","ciu_unisup","ciu_cocisu"
            ],
            pk_func              = lambda: "ciu_codigo",
            pdf_func             = lambda data: print("PDF con", data),
            t_view=self
        )
