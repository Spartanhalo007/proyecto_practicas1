import tkinter as tk
from Ventana_aduanas import abrir_aduanas

# Ventana principal
root = tk.Tk()
root.title("I.B.W. - International Business World")
root.geometry("800x600")
root.configure(bg="#DAD0F4")

# Menú principal
barra_menu = tk.Menu(root)
root.configure(menu=barra_menu)

menu_tablas = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Tablas", menu=menu_tablas)
menu_tablas.add_command(label="Aduanas", command=lambda: abrir_aduanas(root))

root.mainloop()