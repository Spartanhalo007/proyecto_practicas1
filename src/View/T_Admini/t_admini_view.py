import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.admini_service import AdminiService

from View.T_Admini.t_admini_display import t_admini_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_admini_view(t_view):

    def __init__(self, root):
        self.title = "Tabla T_ADMINI"
        self.app = tk.Toplevel(root)
        self.app.title("t_admini")
        self.data_display_frame = t_admini_display

        conexion = obtener_conexion()
        self.service = AdminiService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "ad_nit_ent": int(vals[0]),
                "ad_nom_ent": vals[1],
                "ad_nit_pri": int(vals[2]),
                "ad_nom_pri": vals[3],
                "ad_fecha":   vals[4]
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "ad_nom_ent": vals[1],
                "ad_nit_pri": int(vals[2]),
                "ad_nom_pri": vals[3],
                "ad_fecha":   vals[4]
            }
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
            table_atributes_func = lambda: ["ad_nit_ent","ad_nom_ent","ad_nit_pri","ad_nom_pri","ad_fecha"],
            pk_func              = lambda: "ad_nit_ent",
            pdf_func             = lambda data: print("PDF con", data),
            t_view=self
        )
