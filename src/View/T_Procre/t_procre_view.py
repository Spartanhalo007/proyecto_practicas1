import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.procre_service import ProcreService

from View.T_Procre.t_procre_display import t_procre_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_procre_view(t_view):
    def __init__(self, root):
        self.title = "Tabla PROCRE"
        self.app   = tk.Toplevel(root)
        self.app.title("t_procre")
        self.data_display_frame = t_procre_display

        conexion = obtener_conexion()
        self.service = ProcreService(conexion)

        super().__init__()

        crud_display(
            t_view=self,
            app                  = self.app,
            display              = [self.get_display()],
            c_func               = lambda vals: self.service.create({
                                     "pc_codigo":  int(vals[0]),
                                     "pc_nombre":  vals[1],
                                     "pc_tipocre": vals[2]
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
                                     {"pc_nombre":  vals[1],
                                      "pc_tipocre": vals[2]}
                                 ),
            d_func               = lambda **kw: self.service.delete(
                                     self.display_frame.get_pk()
                                 ),
            min_id_func          = lambda: self.service.first()[0],
            max_id_func          = lambda: self.service.last()[0],
            table_atributes_func = lambda: ["pc_codigo","pc_nombre","pc_tipocre"],
            pk_func              = lambda: "pc_codigo",
            pdf_func             = lambda data: print("PDF con", data)
        )
