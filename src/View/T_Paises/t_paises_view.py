import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.paises_service import PaisesService

from View.T_Paises.t_paises_display import t_paises_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_paises_view(t_view):
    def __init__(self, root):
        self.title = "Tabla PAISES"
        self.app = tk.Toplevel(root)
        self.app.title("t_paises")

        self.w = 430
        self.h = 170
        
        self.data_display_frame = t_paises_display

        conexion = obtener_conexion()
        self.service = PaisesService(conexion)

        super().__init__()

        crud_display(
            t_view=self,
            app                  = self.app,
            display              = [self.get_display()],
            c_func               = lambda vals: self.service.create({
                                     "pai_codigo": vals[0],
                                     "pai_nombre": vals[1]
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
                                     {"pai_nombre": vals[1]}
                                 ),
            d_func               = lambda **kw: self.service.delete(
                                     self.display_frame.get_pk()
                                 ),
            min_id_func          = lambda: self.service.first()[0],
            max_id_func          = lambda: self.service.last()[0],
            table_atributes_func = lambda: ["pai_codigo","pai_nombre"],
            pk_func              = lambda: "pai_codigo",
            pdf_func             = lambda data: print("PDF con", data)
        )
