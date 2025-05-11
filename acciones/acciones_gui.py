import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox
from acciones.acciones_bd import guardar_aduana, eliminar_aduana, consultar_aduana


def guardar_datos(entry_codigo, entry_nombre):
    codigo = entry_codigo.get()
    nombre = entry_nombre.get()

    if not codigo or not nombre:
        messagebox.showwarning("Campos vacíos", "Por favor, complete ambos campos.")
        return

    if guardar_aduana(codigo, nombre):
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
        entry_codigo.delete(0, tk.END)
        entry_codigo.insert(0, "00")
        entry_nombre.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "No se pudieron guardar los datos.")

def eliminar_datos(entry_codigo):
    codigo = entry_codigo.get()

    if not codigo:
        messagebox.showwarning("Código vacío", "Por favor, introduzca un código.")
        return

    confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este registro?")
    if confirmacion:
        if eliminar_aduana(codigo):
            messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
            entry_codigo.delete(0, tk.END)
            entry_codigo.insert(0, "00")
        else:
            messagebox.showerror("Error", "No se encontró el registro o ocurrió un error.")

def consultar_datos(entry_codigo, entry_nombre):
    codigo = entry_codigo.get()

    if not codigo:
        messagebox.showwarning("Codigo vacio", "Por favor, introduzca un codigo.")
        return
    
    resultado = consultar_aduana(codigo)

    if resultado:
        entry_codigo.delete(0, tk.END)
        entry_codigo.insert(0, resultado[0])

        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, resultado[1])

        messagebox.showinfo("Éxito", "Registro encontrado.")
    else:
        messagebox.showerror("No encontrado", "No se encontró un registro con ese código.")