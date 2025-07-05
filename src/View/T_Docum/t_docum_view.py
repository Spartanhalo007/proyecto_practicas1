import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.docum_service import DocumService

from View.T_Docum.t_docum_display import t_docum_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_docum_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de Textos"
        self.app = tk.Toplevel(root)
        self.app.title("t_docum")
        self.app.configure(bg="#135547")
        self.data_display_frame = lambda parent: t_docum_display(parent, bg="#135547")

        self.h = 245
        self.w = 590

        conexion = obtener_conexion()
        self.service = DocumService(conexion)

        super().__init__(bg="#135547")

        def guardar(vals):
            payload = {
                "docu_codig": int(vals[0]),
                "docu_nom_e": vals[1],
                "docu_nom_i": vals[2],
                "docu_nom_f": vals[3],
                "docu_nom_a": vals[4],
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "docu_nom_e": vals[1],
                "docu_nom_i": vals[2],
                "docu_nom_f": vals[3],
                "docu_nom_a": vals[4],
            }
            exito = self.service.update(int(pk), payload)
            messagebox.showinfo("Actualización", "Registro actualizado." if exito else "Error al actualizar.")

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
                "docu_codig","docu_nom_e","docu_nom_i","docu_nom_f","docu_nom_a"
            ],
            pk_func              = lambda: "docu_codig",
            pdf_func             = lambda data: print("PDF con", data)
        )
