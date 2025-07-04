import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.cam053_service import Cam053Service

from View.T_Cam053.t_cam053_display import t_cam053_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_cam053_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de parametros - Etiquetas - XML - camt.053.001.08"
        self.app = tk.Toplevel(root)
        self.app.title("t_cam053")
        self.data_display_frame = t_cam053_display
        conexion = obtener_conexion()

        self.w = 590
        self.h = 250

        self.service = Cam053Service(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "pc8_conse": int(vals[0]),
                "pc8_nivel": int(vals[1]),
                "pc8_etique": vals[2],
                "pc8_llave": vals[3],
                "pc8_eticor": vals[4],
                "pc8_varia": vals[5],
            }
            exito = self.service.create(payload)
            if exito:
                messagebox.showinfo("Guardado", "Registro guardado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el registro.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "pc8_nivel": int(vals[1]),
                "pc8_etique": vals[2],
                "pc8_llave": vals[3],
                "pc8_eticor": vals[4],
                "pc8_varia": vals[5],
            }
            exito = self.service.update(int(pk), payload)
            if exito:
                messagebox.showinfo("Actualización", "Registro actualizado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo actualizar el registro.")

        def eliminar(index=None, index_name=None):
            pk = self.display_frame.get_pk()
            exito = self.service.delete(int(pk))
            if exito:
                messagebox.showinfo("Eliminado", "Registro eliminado exitosamente.")
                self.display_frame.clear()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el registro.")

        crud_display(
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
                "pc8_conse","pc8_nivel","pc8_etique",
                "pc8_llave","pc8_eticor","pc8_varia"
            ],
            pk_func              = lambda: "pc8_conse",
            pdf_func             = lambda data: print("PDF con", data),
            t_view=self
        )
