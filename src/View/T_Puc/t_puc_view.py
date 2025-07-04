import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.puc_service import PucService

from View.T_Puc.t_puc_display import t_puc_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_puc_view(t_view):
    def __init__(self, root):
        self.title = "Tabla PUC"
        self.app   = tk.Toplevel(root)
        self.app.title("t_puc")
        self.data_display_frame = t_puc_display

        conexion = obtener_conexion()
        self.service = PucService(conexion)

        super().__init__()

        def make_payload(vals):
            keys = ["puc_cuenta","puc_cuent","puc_nombre","puc_natura"] + [f"puc_{str(i).zfill(2)}" for i in range(1,31)]
            payload = {}
            for k,v in zip(keys, vals):
                payload[k] = int(v) if k.startswith("puc_0") or k in ("puc_cuenta","puc_cuent") else v
            return payload

        crud_display(
            t_view=self,
            app                  = self.app,
            display              = [self.get_display()],
            c_func               = lambda vals: self.service.create(make_payload(vals)),
            r_func               = lambda index=None,index_name=None: (
                                     [self.service.first()]  if index_name=="first" else
                                     [self.service.last()]   if index_name=="last"  else
                                     [self.service.prev(index)] if index_name=="prev" else
                                     [self.service.next(index)] if index_name=="next" else
                                     self.service.browse()
                                 ),
            u_func               = lambda vals: self.service.update(
                                     (int(vals[0]),int(vals[1])),
                                     {k:v for k,v in make_payload(vals).items() if k not in ("puc_cuenta","puc_cuent")}
                                 ),
            d_func               = lambda **kw: self.service.delete((
                                     self.display_frame.get_info()[0],
                                     self.display_frame.get_info()[1]
                                 )),
            min_id_func          = lambda: self.service.first()[:2],
            max_id_func          = lambda: self.service.last()[:2],
            table_atributes_func = lambda: ["puc_cuenta","puc_cuent","puc_nombre","puc_natura"] + [f"puc_{str(i).zfill(2)}" for i in range(1,31)],
            pk_func              = lambda: ("puc_cuenta","puc_cuent"),
            pdf_func             = lambda data: print("PDF con",data)
        )
