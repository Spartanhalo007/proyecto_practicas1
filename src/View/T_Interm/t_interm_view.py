import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.interm_service import IntermService

from View.T_Interm.t_interm_display import t_interm_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_interm_view(t_view):

    def __init__(self, root):
        self.title = "Tabla INTERM"
        self.app = tk.Toplevel(root)
        self.app.title("t_interm")
        self.data_display_frame = t_interm_display

        conexion = obtener_conexion()
        self.service = IntermService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "if_nit":     int(vals[0]),
                "if_nombre":  vals[1],
                "if_codcar":  vals[2],
                "if_codigo":  int(vals[3]) if vals[3] else None,
                "if_tipoint": int(vals[4]) if vals[4] else None,
                "if_nomtipi": vals[5],
                "if_imc":     vals[6],
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "if_nombre":  vals[1],
                "if_codcar":  vals[2],
                "if_codigo":  int(vals[3]) if vals[3] else None,
                "if_tipoint": int(vals[4]) if vals[4] else None,
                "if_nomtipi": vals[5],
                "if_imc":     vals[6],
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
                "if_nit","if_nombre","if_codcar",
                "if_codigo","if_tipoint","if_nomtipi","if_imc"
            ],
            pk_func              = lambda: "if_nit",
            pdf_func             = lambda data: print("PDF con", data)
        )
