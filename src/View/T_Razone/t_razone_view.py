import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.razone_service import RazonEService

from View.T_Razone.t_razone_display import t_razone_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_razone_view(t_view):
    def __init__(self, root):
        self.title = "Tabla Razones de NO Canalización"
        self.app   = tk.Toplevel(root)
        self.app.title("t_razone")
        self.data_display_frame = t_razone_display

        self.h = 450
        self.w = 510

        conexion = obtener_conexion()
        self.service = RazonEService(conexion)

        super().__init__()

        crud_display(
            t_view=self,
            app                  = self.app,
            display              = [self.get_display()],
            c_func               = lambda vals: self.service.create({
                                      "raz_codigo":  int(vals[0]),
                                      "raz_nombre":  vals[1],
                                      **{f"raz_propr{i}": int(vals[1+i]) for i in range(1,7)},
                                      **{f"raz_numer{i}": int(vals[7+i]) for i in range(1,6)}
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
                                      {
                                        "raz_nombre": vals[1],
                                        **{f"raz_propr{i}": int(vals[1+i]) for i in range(1,7)},
                                        **{f"raz_numer{i}": int(vals[7+i]) for i in range(1,6)}
                                      }
                                 ),
            d_func               = lambda **kw: self.service.delete(
                                      self.display_frame.get_pk()
                                 ),
            min_id_func          = lambda: self.service.first()[0],
            max_id_func          = lambda: self.service.last()[0],
            table_atributes_func = lambda: [
                "raz_codigo","raz_nombre",
                *[f"raz_propr{i}" for i in range(1,7)],
                *[f"raz_numer{i}" for i in range(1,6)]
            ],
            pk_func              = lambda: "raz_codigo",
            pdf_func             = lambda data: print("PDF con", data)
        )
