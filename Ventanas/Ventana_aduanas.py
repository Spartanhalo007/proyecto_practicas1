import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import PhotoImage
from acciones.acciones_gui import guardar_datos, eliminar_datos, consultar_datos

def solo_numeros(P):
    return P == "" or (P.isdigit() and len(P) <= 2)

def abrir_aduanas(root):
    ventana = tk.Toplevel(root)
    ventana.title("t_aduana")
    ventana.geometry("370x130")
    ventana.configure(bg="#c0c0c0")

    vcmd = ventana.register(solo_numeros)

    # Título de la tabla
    lbl_titulo = tk.Label(ventana, 
                          text="Tabla de Aduanas", 
                          font=("Arial", 14, "bold"), 
                          bg="#c0c0c0", 
                          fg= "#000080"
                          )
    lbl_titulo.grid(row=0, 
                    column=0, 
                    columnspan=2
                    )

    # Línea debajo del título
    linea1 = tk.Frame(ventana, 
                      height=2, 
                      bd=2, 
                      relief="sunken", 
                      bg="#c0c0c0"
                      )
    linea1.grid(row=1, 
                column=0, 
                columnspan=2, 
                sticky="ew", 
                padx=10, 
                pady=5
                )

    # Campo Código
    lbl_codigo = tk.Label(ventana, 
                          text="Código:", 
                          font=("Arial", 8, "bold"), 
                          bg="#c0c0c0"
                          )
    lbl_codigo.grid(row=2, 
                    column=0, 
                    padx=8, 
                    pady=2, 
                    sticky="e"
                    )

    frame_codigo = tk.Frame(ventana, 
                            bg="black", 
                            padx=1, 
                            pady=1
                            )
    frame_codigo.grid(row=2, 
                      column=1, 
                      sticky="w", 
                      padx=5
                      )

    entry_codigo = tk.Entry(frame_codigo, 
                            width=2, 
                            validate="key", 
                            validatecommand=(vcmd, '%P'), 
                            justify="center", 
                            bd=0, 
                            bg="white",
                            )
    entry_codigo.insert(0, "00")
    entry_codigo.pack()

    # Campo Nombre
    lbl_nombre = tk.Label(ventana, 
                          text="Nombre:", 
                          font=("Arial", 8, "bold"), 
                          bg="#c0c0c0"
                          )
    lbl_nombre.grid(row=3, 
                    column=0, 
                    padx=8, 
                    pady=2, 
                    sticky="e"
                    )

    frame_nombre = tk.Frame(ventana, 
                            bg="black", 
                            padx=1, 
                            pady=1
                            )
    frame_nombre.grid(row=3, 
                      column=1, 
                      sticky="w", 
                      padx=5
                      )

    entry_nombre = tk.Entry(frame_nombre, 
                            width=45,
                            bd=0, 
                            bg="white"
                            )
    entry_nombre.pack()

    # Línea debajo de campos
    linea2 = tk.Frame(ventana, height=2, bd=2, relief="sunken", bg="#c0c0c0")
    linea2.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

    base_dir = os.path.dirname(__file__)


    ruta_icono_archivo = os.path.join(base_dir, "iconos", "file.png")    
    ruta_icono_buscar = os.path.join(base_dir, "iconos", "search.png") #temporalmente consultar
    ruta_icono_primero = os.path.join(base_dir, "iconos", "rewind.png")
    ruta_icono_anterior = os.path.join(base_dir, "iconos", "Previus.png")
    ruta_icono_siguiente = os.path.join(base_dir, "iconos", "next.png")
    ruta_icono_ultimo = os.path.join(base_dir, "iconos", "last.png")
    ruta_icono_editar = os.path.join(base_dir, "iconos", "edit.png")
    ruta_icono_eliminar = os.path.join(base_dir, "iconos", "delete.png")
    ruta_icono_cuadrado = os.path.join(base_dir, "iconos", "square.png") #Temporalmente guardar
    ruta_icono_deshacer = os.path.join(base_dir, "iconos", "undo.png")
    ruta_icono_imprimir = os.path.join(base_dir, "iconos", "print.png")
    ruta_icono_abir = os.path.join(base_dir, "iconos", "open.png")

    ventana.icono_archivo = PhotoImage(file=ruta_icono_archivo)
    ventana.icono_primero = PhotoImage(file=ruta_icono_primero)
    ventana.icono_anterior = PhotoImage(file=ruta_icono_anterior)
    ventana.icono_buscar = PhotoImage(file=ruta_icono_buscar) #temporalmente consultar
    ventana.icono_siguiente = PhotoImage(file=ruta_icono_siguiente)
    ventana.icono_ultimo = PhotoImage(file=ruta_icono_ultimo)
    ventana.icono_editar = PhotoImage(file=ruta_icono_editar)
    ventana.icono_eliminar = PhotoImage(file=ruta_icono_eliminar)
    ventana.icono_cuadrado = PhotoImage(file=ruta_icono_cuadrado) #Temporalmente guardar
    ventana.icono_deshacer = PhotoImage(file=ruta_icono_deshacer)
    ventana.icono_imprimir = PhotoImage(file=ruta_icono_imprimir)
    ventana.icono_abrir = PhotoImage(file=ruta_icono_abir)

    frame_boton_titulo = tk.Frame(ventana, bg="#c0c0c0")
    frame_boton_titulo.grid(row=0, column=0, columnspan=2, sticky="w", padx= 10)

    btn_archivo = tk.Button(frame_boton_titulo, image=ventana.icono_archivo)

    btn_archivo.pack(side="left")


    # Botones de navegación
    frame_botones = tk.Frame(ventana, bg="#c0c0c0")
    frame_botones.grid(row=7, column=0, columnspan=2, sticky="w", padx=10)

    btn_primero = tk.Button(frame_botones, image=ventana.icono_primero)
    btn_anterior = tk.Button(frame_botones, image=ventana.icono_anterior)
    btn_buscar = tk.Button(frame_botones, image=ventana.icono_buscar, command= lambda: consultar_datos(entry_codigo, entry_nombre)) #temporalmente consultar
    btn_siguiente = tk.Button(frame_botones, image=ventana.icono_siguiente)
    btn_ultimo = tk.Button(frame_botones, image=ventana.icono_ultimo)

    btn_primero.pack(side="left", padx=2)
    btn_anterior.pack(side="left", padx=2)
    btn_buscar.pack(side="left", padx=2)
    btn_siguiente.pack(side="left", padx=2)
    btn_ultimo.pack(side="left", padx=2)

    frame_botones = tk.Frame(ventana, bg="#c0c0c0")
    frame_botones.grid(row=7, column=1, columnspan=2, sticky="w", padx=130)

    btn_editar = tk.Button(frame_botones, image=ventana.icono_editar)
    btn_eliminar = tk.Button(frame_botones, image=ventana.icono_eliminar, command= lambda: eliminar_datos(entry_codigo))
    btn_cuadrado = tk.Button(frame_botones, image=ventana.icono_cuadrado, command=lambda: guardar_datos(entry_codigo, entry_nombre)) #Temporalmente guardar
    btn_deshacer = tk.Button(frame_botones, image=ventana.icono_deshacer)
    btn_imprimir = tk.Button(frame_botones, image=ventana.icono_imprimir)
    btn_abrir = tk.Button(frame_botones, image=ventana.icono_abrir)

    btn_editar.pack(side="left", padx=2)
    btn_eliminar.pack(side="left", padx=2)
    btn_cuadrado.pack(side="left", padx=2)
    btn_deshacer.pack(side="left", padx=2)
    btn_imprimir.pack(side="left", padx=2)
    btn_abrir.pack(side="left", padx=2)