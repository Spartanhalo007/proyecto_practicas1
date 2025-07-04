import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.comdef_service import ComdefService

from View.T_Combef.t_combef_display import t_comdef_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_comdef_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de Comisiones DEFAULT"
        self.app = tk.Toplevel(root)
        self.app.title("t_comdef")
        self.app.configure(bg="#135547")

        self.h = 325
        self.w = 500
        
        self.data_display_frame = lambda parent: t_comdef_display(parent, bg="#135547")

        conexion = obtener_conexion()
        self.service = ComdefService(conexion)

        super().__init__((), bg="#135547")


        def guardar(vals):
            payload = {
                "com_codigo": int(vals[0]),
                "com_nombr":  vals[1],
                "com_porce":  float(vals[2]),
                "com_minima": float(vals[3]),
                "com_fija":   float(vals[4]),
                "com_mensa":  float(vals[5]),
                "com_gtos":   float(vals[6]),
                "com_poriva": float(vals[7]),
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado",
                "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "com_nombr":  vals[1],
                "com_porce":  float(vals[2]),
                "com_minima": float(vals[3]),
                "com_fija":   float(vals[4]),
                "com_mensa":  float(vals[5]),
                "com_gtos":   float(vals[6]),
                "com_poriva": float(vals[7]),
            }
            exito = self.service.update(int(pk), payload)
            messagebox.showinfo("Actualización",
                "Registro actualizado." if exito else "Error al actualizar.")

        def eliminar(index=None, index_name=None):
            pk = self.display_frame.get_pk()
            exito = self.service.delete(int(pk))
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
                "com_codigo","com_nombr","com_porce","com_minima",
                "com_fija","com_mensa","com_gtos","com_poriva"
            ],
            pk_func              = lambda: "com_codigo",
            pdf_func             = lambda data: print("PDF con", data)
        )
