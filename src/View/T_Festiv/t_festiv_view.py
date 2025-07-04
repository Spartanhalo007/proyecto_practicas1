import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.festiv_service import FestivService

from View.T_Festiv.t_festiv_display import t_festiv_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_festiv_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de Festivos"
        self.app = tk.Toplevel(root)
        self.app.title("t_festiv")

        self.w = 450
        self.h = 240
        self.data_display_frame = t_festiv_display

        conexion = obtener_conexion()
        self.service = FestivService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "fe_ano":  int(vals[0]),
                "fe_mes":  int(vals[1]),
                "fe_dia":  int(vals[2]),
                "fe_col":  int(vals[3]),
                "fe_usa":  int(vals[4]),
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "fe_mes": int(vals[1]),
                "fe_dia": int(vals[2]),
                "fe_col": int(vals[3]),
                "fe_usa": int(vals[4]),
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
            table_atributes_func = lambda: ["fe_ano","fe_mes","fe_dia","fe_col","fe_usa"],
            pk_func              = lambda: "fe_ano",
            pdf_func             = lambda data: print("PDF con", data)
        )
