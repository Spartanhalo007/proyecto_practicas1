import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.patec_service import PatecService

from View.T_Patec.t_patec_display import t_patec_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_patec_view(t_view):
    def __init__(self, root):
        self.title = "Tabla de Patrimonio Tecnico"
        self.app   = tk.Toplevel(root)
        self.app.title("t_patec")
        self.data_display_frame = t_patec_display

        self.w = 410
        self.h = 185

        conexion = obtener_conexion()
        self.service = PatecService(conexion)

        super().__init__()

        crud_display(
            t_view=self,
            app                  = self.app,
            display              = [self.get_display()],
            c_func               = lambda vals: self.service.create({
                                     "pt_fecha":   int(vals[0]),
                                     "pt_vlr_usd": float(vals[1]),
                                     "pt_con_usd": float(vals[2])
                                 }),
            r_func               = lambda index=None, index_name=None: (
                                     [self.service.first()]  if index_name=="first" else
                                     [self.service.last()]   if index_name=="last"  else
                                     [self.service.prev(index)] if index_name=="prev" else
                                     [self.service.next(index)] if index_name=="next" else
                                     self.service.browse()
                                 ),
            u_func               = lambda vals: self.service.update(
                                     int(self.display_frame.get_pk()),
                                     {"pt_vlr_usd": float(vals[1]),
                                      "pt_con_usd": float(vals[2])}
                                 ),
            d_func               = lambda **kw: self.service.delete(
                                     int(self.display_frame.get_pk())
                                 ),
            min_id_func          = lambda: self.service.first()[0],
            max_id_func          = lambda: self.service.last()[0],
            table_atributes_func = lambda: ["pt_fecha","pt_vlr_usd","pt_con_usd"],
            pk_func              = lambda: "pt_fecha",
            pdf_func             = lambda data: print("PDF con", data)
        )
