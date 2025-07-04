import os
import tkinter as tk
from tkinter import Frame, Label, Button, X, LEFT, messagebox

from Repository.conexion_bd import obtener_conexion
from Service.autcom_service import AutcomService
from View.T_Autcom.t_autcom_display import t_autcom_display
from View.Components.crud_display import crud_display


class t_autcom_view:

    boton_archivo = False

    def on_boton_archivo(self):
        self.boton_archivo = not self.boton_archivo
        if self.boton_archivo:
            self.left_button.config(bg="#a0a0a0")
        else:
            self.left_button.config(bg="SystemButtonFace")

    def __init__(self, root):
        self.app = tk.Toplevel(root)
        self.app.title("t_autcom")
        self.app.geometry("600x220")
        self.app.configure(bg="#c0c0c0")

        self.title = "Tabla Autorizaciones de Compras"
        self.service = AutcomService(obtener_conexion())
        self.button_img = self._cargar_icono("file.png")

        # === Encabezado con botón y título ===
        header_top = Frame(self.app, bg="#c0c0c0")
        header_top.pack(fill="x", padx=5, pady=(10, 0))

        self.left_button = Button(
            header_top,
            image=self.button_img,
            text="Archivo" if self.button_img is None else "",
            compound=LEFT if self.button_img else None,
            font=("Arial", 10, "bold"),
            relief="raised",
            borderwidth=2,
            command=self.on_boton_archivo,
        )
        self.left_button.pack(side=LEFT, padx=(0, 10))

        self.title_label = Label(
            header_top,
            text=self.title,
            font=("Arial", 14, "bold"),
            bg="#c0c0c0",
            fg="#000080",
            anchor="center",
        )
        self.title_label.pack(side=LEFT, fill=X, expand=True)

        tk.Frame(self.app, height=2, bd=1, relief="sunken", bg="#c0c0c0").pack(fill="x", padx=5, pady=5)

        # === Campos de entrada ===
        row1 = tk.Frame(self.app, bg="#c0c0c0")
        row1.pack(pady=2)

        tk.Label(row1, text="Código Nivel:", bg="#c0c0c0", font=("Arial", 10)).grid(row=0, column=0, sticky="e")
        self.ent_codigo = tk.Entry(row1, width=5, justify="right", bg="white",
                                   highlightthickness=1, highlightcolor="black",
                                   highlightbackground="black", relief="flat")
        self.ent_codigo.grid(row=0, column=1, padx=(5, 20))

        tk.Label(row1, text="Nombre Nivel:", bg="#c0c0c0", font=("Arial", 10)).grid(row=0, column=2, sticky="e")
        self.ent_nombre = tk.Entry(row1, width=30, justify="right", bg="white",
                                   highlightthickness=1, highlightcolor="black",
                                   highlightbackground="black", relief="flat")
        self.ent_nombre.grid(row=0, column=3, padx=(5, 0))

        row_bancos = tk.Frame(self.app, bg="#c0c0c0")
        row_bancos.pack(pady=(10, 0), padx=20)

        # Banco Caja Social
        frame_caja = tk.LabelFrame(row_bancos, text="BANCO CAJA SOCIAL", font=("Arial", 9, "bold"),
                                   bg="#c0c0c0", fg="#000080", labelanchor="n")
        frame_caja.pack(side="left", padx=10)

        tk.Label(frame_caja, text="Mensual  USD", bg="#c0c0c0").grid(row=0, column=0, padx=5, pady=2)
        self.ent_mensual_b = tk.Entry(frame_caja, width=10, justify="right", bg="white",
                                      highlightthickness=1, highlightcolor="black",
                                      highlightbackground="black", relief="flat")
        self.ent_mensual_b.grid(row=1, column=0, padx=5)

        tk.Label(frame_caja, text="Anual    USD", bg="#c0c0c0").grid(row=0, column=1, padx=5, pady=2)
        self.ent_anual_b = tk.Entry(frame_caja, width=10, justify="right", bg="white",
                                    highlightthickness=1, highlightcolor="black",
                                    highlightbackground="black", relief="flat")
        self.ent_anual_b.grid(row=1, column=1, padx=5)

        # Banco Colmena
        frame_colmena = tk.LabelFrame(row_bancos, text="BANCO COLMENA", font=("Arial", 9, "bold"),
                                      bg="#c0c0c0", fg="#000080", labelanchor="n")
        frame_colmena.pack(side="left", padx=10)

        tk.Label(frame_colmena, text="Mensual  USD", bg="#c0c0c0").grid(row=0, column=0, padx=5, pady=2)
        self.ent_mensual_c = tk.Entry(frame_colmena, width=10, justify="right", bg="white",
                                      highlightthickness=1, highlightcolor="black",
                                      highlightbackground="black", relief="flat")
        self.ent_mensual_c.grid(row=1, column=0, padx=5)

        tk.Label(frame_colmena, text="Anual    USD", bg="#c0c0c0").grid(row=0, column=1, padx=5, pady=2)
        self.ent_anual_c = tk.Entry(frame_colmena, width=10, justify="right", bg="white",
                                    highlightthickness=1, highlightcolor="black",
                                    highlightbackground="black", relief="flat")
        self.ent_anual_c.grid(row=1, column=1, padx=5)

        tk.Frame(self.app, height=2, bd=1, relief="sunken", bg="#c0c0c0").pack(fill="x", padx=5, pady=10)

        # === Display ===
        self.display_frame = t_autcom_display(
            self.app,
            self.ent_codigo, self.ent_nombre,
            self.ent_mensual_b, self.ent_anual_b,
            self.ent_mensual_c, self.ent_anual_c
        )

        # === Funciones internas ===
        def _build_payload():
            return {
                "ac_nivel_c": int(self.ent_codigo.get() or 0),
                "ac_nivel_n": self.ent_nombre.get().strip(),
                "ac_aumen_b": float(self.ent_mensual_b.get() or 0),
                "ac_auanu_b": float(self.ent_anual_b.get() or 0),
                "ac_aumen_c": float(self.ent_mensual_c.get() or 0),
                "ac_auanu_c": float(self.ent_anual_c.get() or 0),
            }

        def guardar(_):
            exito = self.service.create(_build_payload())
            messagebox.showinfo(
                "Guardado" if exito else "Error",
                "Registro guardado exitosamente." if exito else "No se pudo guardar."
            )

        def actualizar(_):
            pk = self.display_frame.get_pk()
            exito = self.service.update(int(pk), _build_payload())
            messagebox.showinfo(
                "Actualización" if exito else "Error",
                "Registro actualizado." if exito else "No se pudo actualizar."
            )

        def eliminar(index=None, index_name=None):
            pk = self.display_frame.get_pk()
            exito = self.service.delete(int(pk))
            if exito:
                messagebox.showinfo("Eliminado", "Registro eliminado.")
                self.display_frame.clear()
            else:
                messagebox.showerror("Error", "No se pudo eliminar.")

        # === CRUD display ===
        crud_display(
            app=self.app,
            display=[self.display_frame],
            c_func=guardar,
            r_func=lambda index=None, index_name=None: (
                [self.service.first()]   if index_name == "first" else
                [self.service.last()]    if index_name == "last"  else
                [self.service.prev(index)] if index_name == "prev" else
                [self.service.next(index)] if index_name == "next" else
                self.service.browse()
            ),
            u_func=actualizar,
            d_func=eliminar,
            min_id_func=lambda: self.service.first()[0],
            max_id_func=lambda: self.service.last()[0],
            table_atributes_func=lambda: [
                "ac_nivel_c", "ac_nivel_n",
                "ac_aumen_b", "ac_auanu_b",
                "ac_aumen_c", "ac_auanu_c"
            ],
            pk_func=lambda: "ac_nivel_c",
            pdf_func=lambda data: print("PDF con", data),
            t_view=self
        )

    def _cargar_icono(self, filename):
        ruta = os.path.join(os.path.dirname(os.path.dirname(__file__)), "iconos", filename)
        try:
            return tk.PhotoImage(file=ruta)
        except Exception as e:
            print(f"Error cargando ícono {filename}: {e}")
            return None

    def get_display(self):
        return self.display_frame
