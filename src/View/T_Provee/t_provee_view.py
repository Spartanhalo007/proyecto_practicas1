import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.provee_service import ProveeService

from View.T_Provee.t_provee_display import t_provee_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_provee_view(t_view):
    def __init__(self, root):
        self.title = "Tabla PROVEE"
        self.app   = tk.Toplevel(root)
        self.app.title("t_provee")
        self.data_display_frame = t_provee_display

        conexion = obtener_conexion()
        self.service = ProveeService(conexion)

        super().__init__()

        crud_display(
            t_view=self,
            app                  = self.app,
            display              = [self.get_display()],
            c_func               = lambda vals: self.service.create({
                                      "pr_tp":      int(vals[0]),
                                      "pr_tpnom":   vals[1],
                                      "pr_codigo":  vals[2],
                                      "pr_dv":      int(vals[3]),
                                      "pr_nombre":  vals[4],
                                      "pr_direcc":  vals[5],
                                      "pr_telef":   vals[6],
                                      "pr_ciudad":  vals[7],
                                      "pr_pais":    vals[8],
                                      "pr_nopais":  vals[9],
                                      "pr_fecha":   vals[10]
                                 }),
            r_func               = lambda index=None, index_name=None: (
                                     [self.service.first()]  if index_name=="first" else
                                     [self.service.last()]   if index_name=="last"  else
                                     [self.service.prev(index)] if index_name=="prev" else
                                     [self.service.next(index)] if index_name=="next" else
                                     self.service.browse()
                                 ),
            u_func               = lambda vals: self.service.update(
                                     (int(vals[0]), vals[2]),
                                     {
                                      "pr_tpnom":  vals[1],
                                      "pr_dv":     int(vals[3]),
                                      "pr_nombre": vals[4],
                                      "pr_direcc": vals[5],
                                      "pr_telef":  vals[6],
                                      "pr_ciudad": vals[7],
                                      "pr_pais":   vals[8],
                                      "pr_nopais": vals[9],
                                      "pr_fecha":  vals[10]
                                     }
                                 ),
            d_func               = lambda **kw: self.service.delete(
                                     (self.display_frame.get_info()[0], self.display_frame.get_info()[2])
                                 ),
            min_id_func          = lambda: self.service.first()[0:2],
            max_id_func          = lambda: self.service.last()[0:2],
            table_atributes_func = lambda: [
                                     "pr_tp","pr_tpnom","pr_codigo","pr_dv",
                                     "pr_nombre","pr_direcc","pr_telef","pr_ciudad",
                                     "pr_pais","pr_nopais","pr_fecha"
                                 ],
            pk_func              = lambda: ("pr_tp","pr_codigo"),
            pdf_func             = lambda data: print("PDF con", data)
        )
