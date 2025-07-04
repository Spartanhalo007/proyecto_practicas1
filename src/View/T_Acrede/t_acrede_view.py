import tkinter as tk
from tkinter import messagebox
from Repository.conexion_bd import obtener_conexion
from Service.acrede_service import AcredeService

from View.T_Acrede.t_acrede_display import t_acrede_display
from ..Components.crud_display import crud_display
from ..t_view import t_view

class t_acrede_view(t_view):

    def __init__(self, root):
        # Configuración básica de la ventana
        self.title = "Tabla Acrede"
        self.app = tk.Toplevel(root)
        self.app.title("t_acrede")

        self.w = 430
        self.h = 170
        
        self.data_display_frame = t_acrede_display

        # Servicio específico para t_acrede
        conexion = obtener_conexion()
        self.service = AcredeService(conexion)

        # Inicializa diseño base y form de campos
        super().__init__()

        # Función para guardar un nuevo registro
        def guardar_registro(vals):
            exito = self.service.create({
                "ac_codigo": int(vals[0]),
                "ac_nombre": vals[1]
            })
            if exito:
                messagebox.showinfo("Guardado", "Registro guardado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el registro.")

        # Función para actualizar registro existente
        def actualizar_registro(vals):
            exito = self.service.update(
                int(self.display_frame.get_pk()),
                {"ac_nombre": vals[1]}
            )
            if exito:
                messagebox.showinfo("Actualización", "Registro actualizado exitosamente.")
            else:
                messagebox.showerror("Error", "No se pudo actualizar el registro.")

        # Función para eliminar registro actual
        def eliminar_registro(index=None, index_name=None):
            pk = self.display_frame.get_pk()
            exito = self.service.delete(int(pk))
            if exito:
                messagebox.showinfo("Eliminado", "Registro eliminado exitosamente.")
                self.display_frame.clear()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el registro.")

        # Invocación del componente de botones
        crud_display(
            app      = self.app,
            display  = [self.get_display()],
            c_func   = guardar_registro,
            r_func   = lambda index=None, index_name=None: (
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
            table_atributes_func = lambda: ["ac_codigo", "ac_nombre"],
            pk_func              = lambda: "ac_codigo",
            pdf_func             = lambda data: print("PDF con", data),
            t_view= self
        )

# Test rápido
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    t_acrede_view(root)
    tk.mainloop()