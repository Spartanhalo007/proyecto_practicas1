import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.sucur_service import SucurService

from View.T_Sucur.t_sucur_display import t_sucur_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_sucur_view(t_view):

    def __init__(self, root):
        self.title = "Tabla de Oficinas"
        self.app = tk.Toplevel(root)
        self.app.title("t_sucur")
        self.data_display_frame = t_sucur_display

        self.w = 450
        self.h = 420

        conexion = obtener_conexion()
        self.service = SucurService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "suc_marca":  int(vals[0]),
                "suc_nomarc": vals[1],
                "suc_codigo": int(vals[2]),
                "suc_region": int(vals[3]),
                "suc_nomreg": vals[4],
                "suc_zona":   int(vals[5]),
                "suc_nomzon": vals[6],
                "suc_nombre": vals[7],
                "suc_gerent": vals[8],
                "suc_suc_dg": int(vals[9]),
                "suc_ciudad": int(vals[10]),
                "suc_nomciu": vals[11],
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {"suc_nombre": vals[7]}  # ejemplo: sólo editar nombre
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
                                      [self.service.first()]  if index_name=="first" else
                                      [self.service.last()]   if index_name=="last"  else
                                      [self.service.prev(index)] if index_name=="prev" else
                                      [self.service.next(index)] if index_name=="next" else
                                      self.service.browse()
                                  ),
            u_func               = actualizar,
            d_func               = eliminar,
            min_id_func          = lambda: self.service.first()[2],  # el PK está en la tercera posición
            max_id_func          = lambda: self.service.last()[2],
            table_atributes_func = lambda: ["suc_marca","suc_nomarc","suc_codigo","suc_region","suc_nomreg",
                                            "suc_zona","suc_nomzon","suc_nombre","suc_gerent",
                                            "suc_suc_dg","suc_ciudad","suc_nomciu"],
            pk_func              = lambda: "suc_codigo",
            pdf_func             = lambda data: print("PDF con", data)
        )
