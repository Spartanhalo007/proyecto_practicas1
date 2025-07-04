import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.corr_service import CorrService

from View.T_Corr.t_corr_display import t_corr_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_corr_view(t_view):

    def __init__(self, root):
        self.title = "Tabla Corresponsales"
        self.app = tk.Toplevel(root)
        self.app.title("t_corr")

        self.w = 550

        self.data_display_frame = t_corr_display

        conexion = obtener_conexion()
        self.service = CorrService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "cor_cod":   int(vals[0]),
                "cor_swift": vals[1],
                "cor_mda":   vals[2],
                "cor_nomb":  vals[3],
                "cor_dir":   vals[4],
                "cor_ciud":  vals[5],
                "cor_copais":vals[6],
                "cor_pais":  vals[7],
                "cor_cosupe":int(vals[8]),
                "cor_aba":   vals[9],
                "cor_cta":   vals[10],
                "cor_cnv":   int(vals[11]),
            }
            exito = self.service.create(payload)
            messagebox.showinfo("Guardado", "Registro guardado." if exito else "Error al guardar.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                "cor_swift": vals[1],
                "cor_mda":   vals[2],
                "cor_nomb":  vals[3],
                "cor_dir":   vals[4],
                "cor_ciud":  vals[5],
                "cor_copais":vals[6],
                "cor_pais":  vals[7],
                "cor_cosupe":int(vals[8]),
                "cor_aba":   vals[9],
                "cor_cta":   vals[10],
                "cor_cnv":   int(vals[11]),
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
                "cor_cod","cor_swift","cor_mda","cor_nomb",
                "cor_dir","cor_ciud","cor_copais","cor_pais",
                "cor_cosupe","cor_aba","cor_cta","cor_cnv"
            ],
            pk_func              = lambda: "cor_cod",
            pdf_func             = lambda data: print("PDF con", data)
        )