import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.fe_230_service import Fe230Service

from View.T_Fe_230.t_fe_230_display import t_fe_230_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_fe_230_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de Fechas - Promedio Posición - F-230"
        self.app = tk.Toplevel(root)
        self.app.title("t_fe_230")
        self.data_display_frame = t_fe_230_display

        self.w = 520
        self.h = 295

        conexion = obtener_conexion()
        self.service = Fe230Service(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "fe_dia_pro": vals[0],
                "fe_dia_01": vals[1],
                "fe_nro_01": int(vals[2]) if vals[2] else None,
                "fe_dia_02": vals[3],
                "fe_nro_02": int(vals[4]) if vals[4] else None,
                "fe_dia_03": vals[5],
                "fe_nro_03": int(vals[6]) if vals[6] else None,
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "fe_dia_01": vals[1],
                "fe_nro_01": int(vals[2]) if vals[2] else None,
                "fe_dia_02": vals[3],
                "fe_nro_02": int(vals[4]) if vals[4] else None,
                "fe_dia_03": vals[5],
                "fe_nro_03": int(vals[6]) if vals[6] else None,
            }
            exito = self.service.update(vals[0], payload)
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
                "fe_dia_pro","fe_dia_01","fe_nro_01",
                "fe_dia_02","fe_nro_02","fe_dia_03","fe_nro_03"
            ],
            pk_func              = lambda: "fe_dia_pro",
            pdf_func             = lambda data: print("PDF con", data)
        )
