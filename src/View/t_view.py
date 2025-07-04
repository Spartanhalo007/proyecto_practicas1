import os
from tkinter import *
from View.Components.crud_display import crud_display

class t_view:

    w = 700
    h = 400

    boton_archivo = False

    def on_boton_archivo(self):
        self.boton_archivo = not self.boton_archivo
        if self.boton_archivo:
            self.left_button.config(bg="#a0a0a0")  # Color más oscuro al activar
        else:
            self.left_button.config(bg="SystemButtonFace")  # Color por defecto



    def __init__(self, args_display=(), bg="#c0c0c0"):

        self.app.geometry(f"{self.w}x{self.h}")
        self.app.configure(bg=bg)

        # === Botón izquierdo con imagen ===
        base_dir = os.path.dirname(os.path.dirname(__file__))
        ruta_icono = os.path.join(base_dir, "View\iconos", "file.png")

        try:
            self.button_img = PhotoImage(file=ruta_icono)
        except Exception as e:
            print(f"Error cargando ícono archivo: {e}")
            self.button_img = None

        # === Título centrado ===
        title_container = Frame(self.app, bg=bg)
        title_container.pack(fill="x", padx=5, pady=10)

        self.left_button = Button(title_container, 
                             image=self.button_img,
                             text="Archivo" if self.button_img is None else "",
                             compound=LEFT if self.button_img else None,
                             font=("Arial", 10, "bold"),
                             relief=RAISED,
                             borderwidth=2,
                             command= lambda: self.on_boton_archivo()
                             )
        self.left_button.pack(side=LEFT, padx=(0,10))

        title_frame = Label(title_container, text=self.title, font=("Arial", 14, "bold"),
                            bg=bg, fg="#000080")
        title_frame.pack()

        # === Línea divisoria ===
        linea = Frame(self.app, height=2, bd=1, relief="sunken", bg=bg)
        linea.pack(fill="x", padx=5, pady=5)

        # === Instanciar el formulario (display_frame) ===
        if len(args_display) == 0:
            display_frame = self.data_display_frame(self.app)
        else:
            display_frame = self.data_display_frame(self.app, args_display)

        self.display_frame = display_frame

        # === Otra línea divisoria ===
        linea = Frame(self.app, height=2, bd=1, relief="sunken", bg=bg)
        linea.pack(fill="x", padx=5, pady=5)
    def get_display(self):
        return self.display_frame

