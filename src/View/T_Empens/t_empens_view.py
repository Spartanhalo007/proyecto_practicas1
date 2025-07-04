import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.empens_service import EmpensService

from View.T_Empens.t_empens_display import t_empens_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_empens_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de Empresas de Pensiones"
        self.app = tk.Toplevel(root)
        self.app.title("t_empens")
        self.data_display_frame = t_empens_display

        self.w = 460
        self.h = 500

        conexion = obtener_conexion()
        self.service = EmpensService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "pen_nit":    int(vals[0]),
                "pen_dv":     int(vals[1]),
                "pen_nombre": vals[2],
                "pen_codigo": vals[3],
                "pen_cuenta": int(vals[4]),
                "pen_direcc": vals[5],
                "pen_cociu":  int(vals[6]),
                "pen_ciudad": vals[7],
                "pen_copais": vals[8],
                "pen_pais":   vals[9],
                "pen_telef":  int(vals[10]),
                "pen_oficod": int(vals[11]),
                "pen_ofinom": vals[12],
                "pen_men_us": float(vals[13]),
                "pen_poriva": float(vals[14]),
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "pen_dv":     int(vals[1]),
                "pen_nombre": vals[2],
                "pen_codigo": vals[3],
                "pen_cuenta": int(vals[4]),
                "pen_direcc": vals[5],
                "pen_cociu":  int(vals[6]),
                "pen_ciudad": vals[7],
                "pen_copais": vals[8],
                "pen_pais":   vals[9],
                "pen_telef":  int(vals[10]),
                "pen_oficod": int(vals[11]),
                "pen_ofinom": vals[12],
                "pen_men_us": float(vals[13]),
                "pen_poriva": float(vals[14]),
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
                "pen_nit","pen_dv","pen_nombre","pen_codigo","pen_cuenta",
                "pen_direcc","pen_cociu","pen_ciudad","pen_copais","pen_pais",
                "pen_telef","pen_oficod","pen_ofinom","pen_men_us","pen_poriva"
            ],
            pk_func              = lambda: "pen_nit",
            pdf_func             = lambda data: print("PDF con", data)
        )
