import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.mdas_service import MdasService

from View.T_Mdas.t_mdas_display import t_mdas_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_mdas_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de Monedas"
        self.app = tk.Toplevel(root)
        self.app.title("t_mdas")
        self.data_display_frame = t_mdas_display

        self.w = 430
        self.h = 270

        conexion = obtener_conexion()
        self.service = MdasService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "mdas_cod":   int(vals[0]),
                "mdas_swift": vals[1],
                "mdas_nomb":  vals[2],
                "mdas_tacom": vals[3],
                "mdas_taven": vals[4],
                "mdas_fecha": vals[5]
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "mdas_swift": vals[1],
                "mdas_nomb":  vals[2],
                "mdas_tacom": vals[3],
                "mdas_taven": vals[4],
                "mdas_fecha": vals[5]
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
            t_view=self,
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
                "mdas_cod","mdas_swift","mdas_nomb",
                "mdas_tacom","mdas_taven","mdas_fecha"
            ],
            pk_func              = lambda: "mdas_cod",
            pdf_func             = lambda data: print("PDF con", data)
        )
