import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.corswi_service import CorswiService

from View.T_Corswi.t_corswi_display import t_corswi_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_corswi_view(t_view):

    def __init__(self, root):
        self.title = "Tabla Códigos SWIFT de Corresponsales"
        self.app = tk.Toplevel(root)
        self.app.title("t_corswi")
        self.data_display_frame = t_corswi_display

        conexion = obtener_conexion()
        self.service = CorswiService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "bic_codswi": vals[0],
                "bic_sucswi": vals[1],
                "bic_nom01":  vals[2],
                "bic_dir01":  vals[3],
                "bic_ciudad": vals[4],
                "bic_copais": vals[5],
                "bic_nopais": vals[6],
                "bic_abba":   vals[7],
                "bic_doble":  vals[8],
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "bic_sucswi": vals[1],
                "bic_nom01":  vals[2],
                "bic_dir01":  vals[3],
                "bic_ciudad": vals[4],
                "bic_copais": vals[5],
                "bic_nopais": vals[6],
                "bic_abba":   vals[7],
                "bic_doble":  vals[8],
            }
            exito = self.service.update(pk, payload)
            messagebox.showinfo("Actualización",
                "Registro actualizado." if exito else "Error al actualizar.")

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
                "bic_codswi","bic_sucswi","bic_nom01","bic_dir01","bic_ciudad",
                "bic_copais","bic_nopais","bic_abba","bic_doble"
            ],
            pk_func              = lambda: "bic_codswi",
            pdf_func             = lambda data: print("PDF con", data)
        )
