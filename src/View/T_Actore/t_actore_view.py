import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.actore_service import ActoreService
from View.t_scrollable_view import t_scrollable_view
from View.T_Actore.t_actore_display import t_actore_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_actore_view(t_scrollable_view):

    def __init__(self, root):
        self.title = "Tabla Actore"
        self.app = tk.Toplevel(root)
        self.app.title("t_actore")
        self.data_display_frame = t_actore_display

        conexion = obtener_conexion()
        self.service = ActoreService(conexion)

        super().__init__()

        def guardar(vals):
            payload = {
                "ac_f_cremo": vals[0],        # como cadena 'YYYY-MM-DD'
                "ac_tip_act": int(vals[1]),
                "ac_tip_con": vals[2],
                "ac_tp_idvc": vals[3],
                "ac_tp_id": vals[4],
                "ac_nu_id": vals[5],
                "ac_nombre": vals[6],
                "ac_ciudad": vals[7],
                "ac_nom_ciu": vals[8],
                "ac_ciiu": vals[9],
                "ac_ciiunom": vals[10],
                "ac_telef": vals[11],
                "ac_direcc": vals[12],
                "ac_correo": vals[13],
                "ac_tp_empr": int(vals[14]),
                "ac_tp_emno": vals[15],
                "ac_sector": vals[16],
                "ac_sec_nom": vals[17],
                "ac_tp_efin": int(vals[18]),
                "ac_tiefino": vals[19],
                "ac_supervi": int(vals[20]),
                "ac_tp_sinp": vals[21],
                "ac_tp_sino": vals[22],
                "ac_regimen": int(vals[23]),
                "ac_regi_no": vals[24],
                "ac_act_sue": int(vals[25]),
                "ac_nu_admi": int(vals[26]),
                "ac_nu_patr": int(vals[27]),
                "ac_no_patr": vals[28],
                "ac_tpidvac": vals[29],
                "ac_natural": int(vals[30]),
                "ac_paisres": vals[31]
            }
            exito = self.service.create(payload)
            if exito:
                messagebox.showinfo("Guardado", "Registro guardado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el registro.")

        def actualizar(vals):
            pk = self.display_frame.get_pk()
            payload = {
                # omitimos AC_NU_ID porque es PK
                # repetimos todas menos índice 5
                "ac_f_cremo": vals[0],
                "ac_tip_act": int(vals[1]),
                "ac_tip_con": vals[2],
                "ac_tp_idvc": vals[3],
                "ac_tp_id": vals[4],
                "ac_nombre": vals[6],
                "ac_ciudad": vals[7],
                "ac_nom_ciu": vals[8],
                "ac_ciiu": vals[9],
                "ac_ciiunom": vals[10],
                "ac_telef": vals[11],
                "ac_direcc": vals[12],
                "ac_correo": vals[13],
                "ac_tp_empr": int(vals[14]),
                "ac_tp_emno": vals[15],
                "ac_sector": vals[16],
                "ac_sec_nom": vals[17],
                "ac_tp_efin": int(vals[18]),
                "ac_tiefino": vals[19],
                "ac_supervi": int(vals[20]),
                "ac_tp_sinp": vals[21],
                "ac_tp_sino": vals[22],
                "ac_regimen": int(vals[23]),
                "ac_regi_no": vals[24],
                "ac_act_sue": int(vals[25]),
                "ac_nu_admi": int(vals[26]),
                "ac_nu_patr": int(vals[27]),
                "ac_no_patr": vals[28],
                "ac_tpidvac": vals[29],
                "ac_natural": int(vals[30]),
                "ac_paisres": vals[31]
            }
            exito = self.service.update(pk, payload)
            if exito:
                messagebox.showinfo("Actualización", "Registro actualizado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo actualizar el registro.")

        def eliminar(index=None, index_name=None):
            pk = self.display_frame.get_pk()
            exito = self.service.delete(pk)
            if exito:
                messagebox.showinfo("Eliminado", "Registro eliminado exitosamente.")
                self.display_frame.clear()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el registro.")

        crud_display(
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
            min_id_func          = lambda: self.service.first()[5],  # índice de AC_NU_ID en tuple
            max_id_func          = lambda: self.service.last()[5],
            table_atributes_func = lambda: [
                "ac_f_cremo","ac_tip_act","ac_tip_con","ac_tp_idvc","ac_tp_id",
                "ac_nu_id","ac_nombre","ac_ciudad","ac_nom_ciu","ac_ciiu",
                "ac_ciiunom","ac_telef","ac_direcc","ac_correo","ac_tp_empr",
                "ac_tp_emno","ac_sector","ac_sec_nom","ac_tp_efin","ac_tiefino",
                "ac_supervi","ac_tp_sinp","ac_tp_sino","ac_regimen","ac_regi_no",
                "ac_act_sue","ac_nu_admi","ac_nu_patr","ac_no_patr","ac_tpidvac",
                "ac_natural","ac_paisres"
            ],
            pk_func              = lambda: "ac_nu_id",
            pdf_func             = lambda data: print("PDF con", data),
            t_view=self
        )
