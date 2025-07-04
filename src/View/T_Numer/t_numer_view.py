import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.numer_service import NumerService

from View.T_Numer.t_numer_display import t_numer_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_numer_view(t_view):

    def __init__(self, root):
        self.title = "Tabla NUMER"
        self.app = tk.Toplevel(root)
        self.app.title("t_numer")
        self.data_display_frame = t_numer_display

        conexion = obtener_conexion()
        self.service = NumerService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "num_codigo": int(vals[0]),
                "num_concep": vals[1],
                "num_inegre": int(vals[2]),
                "num_form1": int(vals[3]),
                "num_form2": int(vals[4]),
                "num_form3": int(vals[5]),
                **{f"num_dest{str(i).zfill(2)}": int(vals[5+i]) for i in range(1,14)},
                "num_ic_ie":  int(vals[18]),
                "num_accion": vals[19],
                **{f"num_rece{str(i).zfill(2)}": vals[19+i] for i in range(1,3)},
                **{f"num_inve{str(i).zfill(2)}": vals[21+i] for i in range(1,7)},
                "num_dian":   int(vals[-1])
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            # similar payload but sin num_codigo
            data = guardar(vals)  # o reconstruir payload sin la clave
            exito = self.service.update(pk, data)
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
                "num_codigo","num_concep","num_inegre","num_form1","num_form2","num_form3",
                *[f"num_dest{str(i).zfill(2)}" for i in range(1,14)],
                "num_ic_ie","num_accion",
                "num_rece01","num_rece02",
                *[f"num_inve{str(i).zfill(2)}" for i in range(1,8)],
                "num_dian"
            ],
            pk_func              = lambda: "num_codigo",
            pdf_func             = lambda data: print("PDF con", data)
        )
