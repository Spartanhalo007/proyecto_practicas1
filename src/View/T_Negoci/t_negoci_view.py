import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.negoci_service import NegociService

from View.T_Negoci.t_negoci_display import t_negoci_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_negoci_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de Negociadores del Banco"
        self.app = tk.Toplevel(root)
        self.app.title("t_negoci")
        self.data_display_frame = t_negoci_display
        
        self.w = 450
        self.h = 270

        conexion = obtener_conexion()
        self.service = NegociService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "ng_nit":   int(vals[0]),
                "ng_nombre":vals[1],
                "ng_codigo":vals[2],
                "ng_conse": int(vals[3]),
                "ng_mtomin":vals[4]
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "ng_nombre": vals[1],
                "ng_codigo": vals[2],
                "ng_conse":  int(vals[3]),
                "ng_mtomin": vals[4]
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
            table_atributes_func = lambda: ["ng_nit","ng_nombre","ng_codigo","ng_conse","ng_mtomin"],
            pk_func              = lambda: "ng_nit",
            pdf_func             = lambda data: print("PDF con", data)
        )
