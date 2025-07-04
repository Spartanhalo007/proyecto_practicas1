import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.aduanas_service import AduanasService

from View.T_Aduanas.t_aduanas_display import t_aduana_display
from ..Components.crud_display import crud_display
from ..t_view               import t_view

class t_aduanas_view(t_view):

    def __init__(self, root):
        self.title = "Tabla Aduanas"
        self.repo = None
        self.app = tk.Toplevel(root)
        self.app.title("t_aduana")
        self.s_reporte_tabla = None

        self.w = 430
        self.h = 170

        self.data_display_frame = t_aduana_display

        conexion = obtener_conexion()
        self.service = AduanasService(conexion)

        super().__init__() 

        def guardar_registro(vals):
            exito = self.service.create({
                "ad_codigo": int(vals[0]),
                "ad_nombre": vals[1]
            })
            if exito:
                messagebox.showinfo("Guardado", "El registro se ha guardado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el registro.")

        def actualizar_registro(vals):
            exito = self.service.update(
                int(self.display_frame.get_pk()),
                {"ad_nombre": vals[1]}
            )
            if exito:
                messagebox.showinfo("Actualización", "El registro ha sido actualizado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo actualizar el registro.")

        def eliminar_registro(index=None, index_name=None):
            pk = self.display_frame.get_pk()
            exito = self.service.delete(int(pk))
            if exito:
                messagebox.showinfo("Eliminado", "El registro ha sido eliminado exitosamente.")
                self.display_frame.clear()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el registro.")


        crud_display(
            app      = self.app,
            display  = [self.get_display()],
            c_func   = guardar_registro,
            r_func = lambda index=None, index_name=None: (
                            [ self.service.first() ]  if index_name == "first" else
                            [ self.service.last()  ]   if index_name == "last"  else
                            [ self.service.prev(index) ] if index_name == "prev"  else
                            [ self.service.next(index) ] if index_name == "next"  else
                            self.service.browse()
                        ),
            u_func   = actualizar_registro,
            d_func   = eliminar_registro,
            min_id_func          = lambda: self.service.first()[0],
            max_id_func          = lambda: self.service.last()[0],
            table_atributes_func = lambda: ["ad_codigo", "ad_nombre"],
            pk_func              = lambda: "ad_codigo",
            pdf_func             = lambda all_data: print("PDF con", all_data),
            t_view= self
        )

