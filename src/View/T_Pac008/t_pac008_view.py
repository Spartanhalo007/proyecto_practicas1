import tkinter as tk
from Repository.conexion_bd import obtener_conexion
from Service.pac008_service import Pac008Service

from View.T_Pac008.t_pac008_display import t_pac008_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_pac008_view(t_view):
    def __init__(self, root):
        self.title = "Tabla de parametros - Etiquetas - XML - pacs.008.001.08"
        self.app = tk.Toplevel(root)
        self.app.title("t_pac008")
        self.data_display_frame = t_pac008_display

        self.h = 265
        self.w = 640

        conexion = obtener_conexion()
        self.service = Pac008Service(conexion)

        super().__init__()

        crud_display(
            t_view=self,
            app                  = self.app,
            display              = [self.get_display()],
            c_func               = lambda vals: self.service.create({
                                     "pc8_conse": int(vals[0]),
                                     "pc8_nivel": int(vals[1]),
                                     "pc8_etique": vals[2],
                                     "pc8_llave": vals[3],
                                     "pc8_eticor": vals[4],
                                     "pc8_varia": vals[5]
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
                                     {"pc8_nivel": int(vals[1]),
                                      "pc8_etique": vals[2],
                                      "pc8_llave": vals[3],
                                      "pc8_eticor": vals[4],
                                      "pc8_varia": vals[5]}
                                 ),
            d_func               = lambda **kw: self.service.delete(int(self.display_frame.get_pk())),
            min_id_func          = lambda: self.service.first()[0],
            max_id_func          = lambda: self.service.last()[0],
            table_atributes_func = lambda: ["pc8_conse","pc8_nivel","pc8_etique","pc8_llave","pc8_eticor","pc8_varia"],
            pk_func              = lambda: "pc8_conse",
            pdf_func             = lambda data: print("PDF con", data)
        )