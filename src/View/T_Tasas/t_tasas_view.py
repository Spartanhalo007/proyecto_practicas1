import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.tasas_service import TasasService

from View.T_Tasas.t_tasas_display import t_tasas_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_tasas_view(t_view):

    def __init__(self, root):
        self.title = "Tasas de Interes"
        self.app = tk.Toplevel(root)
        self.app.title("t_tasas")
        self.app.configure(bg="#135547")
        self.data_display_frame = lambda parent: t_tasas_display(parent, bg="#135547")

        self.h = 185
        self.w = 480

        conexion = obtener_conexion()
        self.service = TasasService(conexion)

        super().__init__(bg="#135547")

        def guardar(vals):
            payload = {
                "tasa_cod":   int(vals[0]),
                "tasa_nombr": vals[1],
                "tasa_cotiz": float(vals[2]) if vals[2] else 0.0
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {"tasa_cotiz": float(vals[2])}
            exito = self.service.update(pk, payload)
            messagebox.showinfo("Actualización", "Registro actualizado." if exito else "Error al actualizar.")

        def eliminar(index=None, index_name=None):
            pk = self.display_frame.get_pk()
            exito = self.service.delete(pk)
            if exito:
                messagebox.showinfo("Eliminado", "Registro eliminado.")
                self.display_frame.clear()
            else:
                messagebox.showerror("Error", "No se pudo eliminar.")

        crud_display(
            t_view=self,
            app                  = self.app,
            display              = [self.get_display()],
            c_func               = guardar,
            r_func               = lambda index=None, index_name=None: (
                                      [ self.service.first() ]  if index_name=="first" else
                                      [ self.service.last()  ]   if index_name=="last"  else
                                      [ self.service.prev(index) ] if index_name=="prev" else
                                      [ self.service.next(index) ] if index_name=="next" else
                                      self.service.browse()
                                  ),
            u_func               = actualizar,
            d_func               = eliminar,
            min_id_func          = lambda: self.service.first()[0],
            max_id_func          = lambda: self.service.last()[0],
            table_atributes_func = lambda: ["tasa_cod", "tasa_nombr", "tasa_cotiz"],
            pk_func              = lambda: "tasa_cod",
            pdf_func             = lambda data: print("PDF con", data)
        )
