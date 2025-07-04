import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.caudev_service import CaudevService

from View.T_Caudev.t_caudev_display import t_caudev_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_caudev_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de Causales De Devolución - Pensiones"
        self.app = tk.Toplevel(root)
        self.app.title("t_caudev")

        self.w = 510
        self.h =160

        self.data_display_frame = t_caudev_display
        conexion = obtener_conexion()
        self.service = CaudevService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "dev_codigo": int(vals[0]),
                "dev_concep": vals[1]
            }
            exito = self.service.create(payload)
            if exito:
                messagebox.showinfo("Guardado", "Registro guardado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el registro.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "dev_concep": vals[1]
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
            table_atributes_func = lambda: ["dev_codigo", "dev_concep"],
            pk_func              = lambda: "dev_codigo",
            pdf_func             = lambda data: print("PDF con", data),
            t_view=self
        )
