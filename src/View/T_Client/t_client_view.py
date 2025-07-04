import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.client_service import ClientService

from View.T_Client.t_client_display import t_client_display
from ..Components.crud_display import crud_display
from ..t_scrollable_view import t_scrollable_view

class t_client_view(t_scrollable_view):

    def __init__(self, root):
        self.title = "Tabla de Clientes"
        self.app = tk.Toplevel(root)
        self.app.title("t_client")
        self.data_display_frame = t_client_display

        conexion = obtener_conexion()
        self.service = ClientService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "cli_tp":      int(vals[0]),
                "cli_codigo":  int(vals[1]),
                "cli_dv":      int(vals[2]),
                "cli_ape01":   vals[3],
                "cli_ape02":   vals[4],
                "cli_nom01":   vals[5],
                "cli_nom02":   vals[6],
                "cli_nombre":  vals[7],
                "cli_dirant":  vals[8],
                "cli_direcc":  vals[9],
                "cli_tivipr":  vals[10],
                "cli_viapri":  vals[11],
                "cli_letras":  vals[12],
                "cli_sufijo":  vals[13],
                "cli_sector":  vals[14],
                # ... y así hasta vals[59] ...
                "cli_vigila":  vals[59],
            }
            exito = self.service.create(payload)
            if exito:
                messagebox.showinfo("Guardado", "Registro guardado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el registro.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "cli_dv":      int(vals[2]),
                "cli_ape01":   vals[3],
                # ... campos editables ...
                "cli_vigila":  vals[59],
            }
            exito = self.service.update(int(pk), payload)
            if exito:
                messagebox.showinfo("Actualización", "Registro actualizado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo actualizar el registro.")

        def eliminar(index=None, index_name=None):
            pk = self.display_frame.get_pk()
            exito = self.service.delete(int(pk))
            if exito:
                messagebox.showinfo("Eliminado", "Registro eliminado correctamente.")
                self.display_frame.clear()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el registro.")

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
            min_id_func          = lambda: self.service.first()[1],  # índice en tuple
            max_id_func          = lambda: self.service.last()[1],
            table_atributes_func = lambda: [ 
                "cli_tp","cli_codigo","cli_dv","cli_ape01","cli_ape02","cli_nom01","cli_nom02","cli_nombre",
                "cli_dirant","cli_direcc","cli_tivipr","cli_viapri","cli_letras","cli_sufijo","cli_sector",
                # ... todos los demás hasta cli_vigila
            ],
            pk_func              = lambda: "cli_codigo",
            pdf_func             = lambda all_data: print("PDF con", all_data)
        )
