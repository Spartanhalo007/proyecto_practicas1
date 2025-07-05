import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.propre_service import PropreService

from View.T_Propre.t_propre_display import t_propre_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_propre_view(t_view):
    def __init__(self, root):
        self.title = "Tabla del Prestamo"
        self.app   = tk.Toplevel(root)
        self.app.title("t_propre")

        self.w = 465
        self.h = 160
        
        self.data_display_frame = t_propre_display

        conexion = obtener_conexion()
        self.service = PropreService(conexion)

        super().__init__()

        crud_display(
            t_view=self,
            app                  = self.app,
            display              = [self.get_display()],
            c_func               = lambda vals: self.service.create({
                                     "propre_cod": int(vals[0]),
                                     "propre_nom": vals[1]
                                 }),
            r_func               = lambda index=None, index_name=None: (
                                     [self.service.first()]  if index_name=="first" else
                                     [self.service.last()]   if index_name=="last"  else
                                     [self.service.prev(index)] if index_name=="prev" else
                                     [self.service.next(index)] if index_name=="next" else
                                     self.service.browse()
                                 ),
            u_func               = lambda vals: self.service.update(
                                     self.display_frame.get_pk(),
                                     {"propre_nom": vals[1]}
                                 ),
            d_func               = lambda **kw: self.service.delete(
                                     self.display_frame.get_pk()
                                 ),
            min_id_func          = lambda: self.service.first()[0],
            max_id_func          = lambda: self.service.last()[0],
            table_atributes_func = lambda: ["propre_cod","propre_nom"],
            pk_func              = lambda: "propre_cod",
            pdf_func             = lambda data: print("PDF con", data)
        )
