import os
from tkinter import *
from View.Components.crud_display import crud_display

class t_scrollable_view:

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

        self.left_button = Button(
            title_container,
            image=self.button_img,
            text="Archivo" if self.button_img is None else "",
            compound=LEFT if self.button_img else None,
            font=("Arial", 10, "bold"),
            relief=RAISED,
            borderwidth=2,
            command=self.on_boton_archivo
        )
        self.left_button.pack(side=LEFT, padx=(0, 10))

        title_frame = Label(title_container, text=self.title, font=("Arial", 14, "bold"),
                            bg=bg, fg="#000080")
        title_frame.pack()

        # === Línea divisoria ===
        Frame(self.app, height=2, bd=1, relief="sunken", bg=bg).pack(fill="x", padx=5, pady=5)

        # === Contenedor con scroll vertical ===
        container = Frame(self.app)
        container.pack(fill="both", expand=True)

        canvas = Canvas(container, bg=bg)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        self.scrollable_frame = Frame(canvas, bg=bg)

        # Ajustar scroll automáticamente
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas_window = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", tags="frame")

        # Ajustar ancho del canvas al redimensionar
        canvas.bind(
            "<Configure>",
            lambda e: canvas.itemconfig(canvas_window, width=e.width)
        )

        # Habilitar scroll con el mouse
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # === Instanciar el formulario (display_frame) ===
        if len(args_display) == 0:
            display_frame = self.data_display_frame(self.scrollable_frame)
        else:
            display_frame = self.data_display_frame(self.scrollable_frame, args_display)

        self.display_frame = display_frame

        # === Otra línea divisoria ===
        Frame(self.scrollable_frame, height=2, bd=1, relief="sunken", bg=bg).pack(fill="x", padx=5, pady=5)

    def get_display(self):
        return self.display_frame
