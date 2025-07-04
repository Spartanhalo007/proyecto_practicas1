import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.coroba_service import CorabaService

from View.T_Coraba.t_coraba_display import t_coraba_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_coraba_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de codigos ABA"
        self.app = tk.Toplevel(root)
        self.app.title("t_coraba")
        self.data_display_frame = t_coraba_display

        self.h = 210
        self.w = 430

        conexion = obtener_conexion()
        self.service = CorabaService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "aba_codigo": int(vals[0]),
                "aba_nombre": vals[1],
                "aba_estado": vals[2],
                "aba_ciudad": vals[3],
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "aba_nombre": vals[1],
                "aba_estado": vals[2],
                "aba_ciudad": vals[3],
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
            table_atributes_func = lambda: ["aba_codigo","aba_nombre","aba_estado","aba_ciudad"],
            pk_func              = lambda: "aba_codigo",
            pdf_func             = lambda data: print("PDF con", data)
        )
