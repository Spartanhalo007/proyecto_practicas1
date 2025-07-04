# src/View/T_CLIENT/t_client_display.py

import tkinter as tk
from tkinter import ttk
from View.t_display import t_display

def validar_num(P, maxlen):
    return P == "" or (P.isdigit() and len(P) <= maxlen)

class t_client_display(t_display):
    """Display de campos para la tabla t_client."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # Registramos validadores para distintos anchos
        v2   = self.frame.register(lambda P: validar_num(P, 2))
        v1   = self.frame.register(lambda P: validar_num(P, 1))
        v12  = self.frame.register(lambda P: validar_num(P, 12))
        v15  = self.frame.register(lambda P: validar_num(P, 15))
        v35  = self.frame.register(lambda P: validar_num(P, 35))
        v40  = self.frame.register(lambda P: validar_num(P, 40))
        v60  = self.frame.register(lambda P: validar_num(P, 60))
        v25  = self.frame.register(lambda P: validar_num(P, 25))
        v20  = self.frame.register(lambda P: validar_num(P, 20))
        v10  = self.frame.register(lambda P: validar_num(P, 10))
        v5   = self.frame.register(lambda P: validar_num(P, 5))
        v3   = self.frame.register(lambda P: validar_num(P, 3))
        v4   = self.frame.register(lambda P: validar_num(P, 4))
        v18  = self.frame.register(lambda P: validar_num(P, 18))

        # 1. CLI_TP (num, 2)
        lbl = tk.Label(self.frame, text="Tp:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2, validate="key", validatecommand=(v2, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 2. CLI_CODIGO (num, 12)
        lbl = tk.Label(self.frame, text="Código:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key", validatecommand=(v12, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 3. CLI_DV (num, 1)
        lbl = tk.Label(self.frame, text="Dv:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1, validate="key", validatecommand=(v1, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 4. CLI_APE01 (str, 15)
        lbl = tk.Label(self.frame, text="Apellido:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=15, validate="key", validatecommand=(v15, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 5. CLI_APE02 (str, 15)
        lbl = tk.Label(self.frame, text="2do", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=15, validate="key", validatecommand=(v15, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 6. CLI_NOM01 (str, 15)
        lbl = tk.Label(self.frame, text="Nombre:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=15, validate="key", validatecommand=(v15, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 7. CLI_NOM02 (str, 15)
        lbl = tk.Label(self.frame, text="2do", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=15, validate="key", validatecommand=(v15, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 8. CLI_NOMBRE (str, 35)
        lbl = tk.Label(self.frame, text="CLI_NOMBRE:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 9. CLI_DIRANT (str, 35)
        lbl = tk.Label(self.frame, text="CLI_DIRANT:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 10. CLI_DIRECC (str, 35)
        lbl = tk.Label(self.frame, text="CLI_DIRECC:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=35, validate="key", validatecommand=(v35, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        opciones_dir = ["av", "cll", "crr"]

        # 11. CLI_TIVIPR (str, 20)
        lbl = tk.Label(self.frame, text="CLI_TIVIPR:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = ttk.Combobox(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), values=opciones_dir)
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 12. CLI_VIAPRI (str, 20)
        lbl = tk.Label(self.frame, text="CLI_VIAPRI:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        opciones_letras = ["A", "B", "C", "D", "E"]

        # 13. CLI_LETRAS (str, 1)
        lbl = tk.Label(self.frame, text="CLI_LETRAS:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = ttk.Combobox(self.frame, width=1, validate="key", validatecommand=(v1, '%P'), values=opciones_letras)
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        opciones_sufijo = ["", "Bis"]

        # 14. CLI_SUFIJO (str, 3)
        lbl = tk.Label(self.frame, text="CLI_SUFIJO:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = ttk.Combobox(self.frame, width=3, validate="key", validatecommand=(v3, '%P'), values=opciones_sufijo)
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        opciones_sector = ["1", "2", "3", "4"]

        # 15. CLI_SECTOR (str, 5)
        lbl = tk.Label(self.frame, text="CLI_SECTOR:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = ttk.Combobox(self.frame, width=5, validate="key", validatecommand=(v5, '%P'), values=opciones_sector)
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 16. CLI_TIVIGE (str, 20)
        lbl = tk.Label(self.frame, text="CLI_TIVIGE:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = ttk.Combobox(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), values=opciones_dir)
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 17. CLI_VIAGEN (str, 20)
        lbl = tk.Label(self.frame, text="CLI_VIAGEN:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 18. CLI_LETRGE (str, 1)
        lbl = tk.Label(self.frame, text="CLI_LETRGE:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = ttk.Combobox(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), values=opciones_letras)
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 19. CLI_SECTGE (str, 5)
        lbl = tk.Label(self.frame, text="CLI_SECTGE:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = ttk.Combobox(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), values=opciones_sector)
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 20. CLI_NROPRE (str, 20)
        lbl = tk.Label(self.frame, text="CLI_NROPRE:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 21. CLI_TIOTR1 (str, 20)
        lbl = tk.Label(self.frame, text="CLI_TIOTR1:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 22. CLI_OTRO1 (str, 20)
        lbl = tk.Label(self.frame, text="CLI_OTRO1:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 23. CLI_TIOTR2 (str, 20)
        lbl = tk.Label(self.frame, text="CLI_TIOTR2:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 24. CLI_OTRO2 (str, 20)
        lbl = tk.Label(self.frame, text="CLI_OTRO2:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 25. CLI_TIOTR3 (str, 20)
        lbl = tk.Label(self.frame, text="CLI_TIOTR3:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 26. CLI_OTRO3 (str, 20)
        lbl = tk.Label(self.frame, text="CLI_OTRO3:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 27. CLI_TIOTR4 (str, 20)
        lbl = tk.Label(self.frame, text="CLI_TIOTR4:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 28. CLI_OTRO4 (str, 20)
        lbl = tk.Label(self.frame, text="CLI_OTRO4:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=20, validate="key", validatecommand=(v20, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 29. CLI_COCIUD (num, 5)
        lbl = tk.Label(self.frame, text="CLI_COCIUD:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=5,  validate="key", validatecommand=(v5,  '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 30. CLI_CIUDAD (str, 40)
        lbl = tk.Label(self.frame, text="CLI_CIUDAD:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=40, validate="key", validatecommand=(v40, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 31. CLI_COPAIS (str, 2)
        lbl = tk.Label(self.frame, text="CLI_COPAIS:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=2,  validate="key", validatecommand=(v2,  '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 32. CLI_NOPAIS (str, 60)
        lbl = tk.Label(self.frame, text="CLI_NOPAIS:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=60, validate="key", validatecommand=(v60, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 33. CLI_TELEF (str, 25)
        lbl = tk.Label(self.frame, text="CLI_TELEF:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=25, validate="key", validatecommand=(v25, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 34. CLI_CELOPE (num, 3)
        lbl = tk.Label(self.frame, text="CLI_CELOPE:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=3,  validate="key", validatecommand=(v3,  '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 35. CLI_CELNUM (str, 10)
        lbl = tk.Label(self.frame, text="CLI_CELNUM:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, validate="key", validatecommand=(v10, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 36. CLI_E_MAIL (str, 40)
        lbl = tk.Label(self.frame, text="CLI_E_MAIL:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=40, validate="key", validatecommand=(v40, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 37. CLI_CTCBCS (num, 12)
        lbl = tk.Label(self.frame, text="CLI_CTCBCS:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key", validatecommand=(v12, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 38. CLI_CTABCS (num, 12)
        lbl = tk.Label(self.frame, text="CLI_CTABCS:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key", validatecommand=(v12, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 39. CLI_CTCCOL (num, 12)
        lbl = tk.Label(self.frame, text="CLI_CTCCOL:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key", validatecommand=(v12, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 40. CLI_CTACOL (num, 12)
        lbl = tk.Label(self.frame, text="CLI_CTACOL:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=12, validate="key", validatecommand=(v12, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 41. CLI_OFI (num, 1)
        lbl = tk.Label(self.frame, text="CLI_OFI:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1,  validate="key", validatecommand=(v1,  '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 42. CLI_OFICIN (num, 4)
        lbl = tk.Label(self.frame, text="CLI_OFICIN:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=4,  validate="key", validatecommand=(v4,  '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 43. CLI_OFINOM (str, 25)
        lbl = tk.Label(self.frame, text="CLI_OFINOM:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=25, validate="key", validatecommand=(v25, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 44. CLI_OFNRCO (num, 4)
        lbl = tk.Label(self.frame, text="CLI_OFNRCO:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=4,  validate="key", validatecommand=(v4,  '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 45. CLI_OFNOCO (str, 25)
        lbl = tk.Label(self.frame, text="CLI_OFNOCO:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=25, validate="key", validatecommand=(v25, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 46. CLI_CIIU (num, 4)
        lbl = tk.Label(self.frame, text="CLI_CIIU:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=4,  validate="key", validatecommand=(v4,  '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 47. CLI_NOCIIU (str, 40)
        lbl = tk.Label(self.frame, text="CLI_NOCIIU:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=40, validate="key", validatecommand=(v40, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 48. CLI_INGRES (num, 16,2) ≈ width 18
        lbl = tk.Label(self.frame, text="CLI_INGRES:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=18, validate="key", validatecommand=(v18,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 49. CLI_FEACTU (date)
        lbl = tk.Label(self.frame, text="CLI_FEACTU:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 50. CLI_CCP_FE (date)
        lbl = tk.Label(self.frame, text="CLI_CCP_FE:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 51. CLI_CCP_FV (date)
        lbl = tk.Label(self.frame, text="CLI_CCP_FV:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=10, bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 52. CLI_CCP_UM (num, 16,2)
        lbl = tk.Label(self.frame, text="CLI_CCP_UM:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=18, validate="key", validatecommand=(v18,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 53. CLI_CCP_UA (num, 16,2)
        lbl = tk.Label(self.frame, text="CLI_CCP_UA:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=18, validate="key", validatecommand=(v18,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 54. CLI_CCP_US (num, 16,2)
        lbl = tk.Label(self.frame, text="CLI_CCP_US:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=18, validate="key", validatecommand=(v18,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 55. CLI_CCP_UT (num, 16,2)
        lbl = tk.Label(self.frame, text="CLI_CCP_UT:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=18, validate="key", validatecommand=(v18,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 56. CLI_CCP_SA (num, 16,2)
        lbl = tk.Label(self.frame, text="CLI_CCP_SA:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=18, validate="key", validatecommand=(v18,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 57. CLI_SEGMEN (num, 3)
        lbl = tk.Label(self.frame, text="CLI_SEGMEN:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=3,  validate="key", validatecommand=(v3, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 58. CLI_CUPOCA (num, 16,2)
        lbl = tk.Label(self.frame, text="CLI_CUPOCA:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=18,validate="key", validatecommand=(v18,'%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("num")

        # 59. CLI_TIPO (str, 5)
        lbl = tk.Label(self.frame, text="CLI_TIPO:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=5,  validate="key", validatecommand=(v5, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        # 60. CLI_VIGILA (str, 1)
        lbl = tk.Label(self.frame, text="CLI_VIGILA:", font=("Arial",8,"bold"), bg="#c0c0c0")
        ent = tk.Entry(self.frame, width=1,  validate="key", validatecommand=(v1, '%P'), bd=0, bg="white")
        self.elements.append([lbl, ent]); self.elements_types.append("str")

        bg = "#c0c0c0"
        self.frame.configure(bg=bg)

                # Aplicar estilo a todos los Entry
        for _, entry in self.elements:
            if type(entry) is tk.Entry:
                entry.config(
                    highlightthickness=1,
                    highlightcolor="black",
                    highlightbackground="black",
                    justify="right",
                    bg="white"
                )
        i = 0
        largo_entries = 45

        # Row 0: CLI_TP, CLI_CODIGO, CLI_DV
        self.elements[i][0].grid(row=0, column=0, padx=25, pady=3, sticky="w") # CLI_TP Label
        self.elements[i][1].config(width=2) # CLI_TP Entry
        self.elements[i][1].grid(row=0, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=0, column=2, padx=5, pady=3, sticky="w") # CLI_CODIGO Label
        self.elements[i+1][1].config(width=largo_entries) # CLI_CODIGO Entry
        self.elements[i+1][1].grid(row=0, column=3, padx=5, pady=3, sticky="w")

        self.elements[i+2][0].grid(row=0, column=4, padx=5, pady=3, sticky="w") # CLI_DV Label
        self.elements[i+2][1].config(width=1) # CLI_DV Entry
        self.elements[i+2][1].grid(row=0, column=5, padx=5, pady=3, sticky="w")
        i += 3 # i is now 3

        # Row 1: CLI_APE01, CLI_APE02
        self.elements[i][0].grid(row=1, column=0, padx=25, pady=3, sticky="w") # CLI_APE01 Label
        self.elements[i][1].config(width=largo_entries//2) # CLI_APE01 Entry
        self.elements[i][1].grid(row=1, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=1, column=2, padx=5, pady=3, sticky="w") # CLI_APE02 Label
        self.elements[i+1][1].config(width=largo_entries//2) # CLI_APE02 Entry
        self.elements[i+1][1].grid(row=1, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 5

        # Row 2: CLI_NOM01, CLI_NOM02
        self.elements[i][0].grid(row=2, column=0, padx=25, pady=3, sticky="w") # CLI_NOM01 Label
        self.elements[i][1].config(width=largo_entries//2) # CLI_NOM01 Entry
        self.elements[i][1].grid(row=2, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=2, column=2, padx=5, pady=3, sticky="w") # CLI_NOM02 Label
        self.elements[i+1][1].config(width=largo_entries//2) # CLI_NOM02 Entry
        self.elements[i+1][1].grid(row=2, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 7

        # Row 3: CLI_NOMBRE
        self.elements[i][0].grid(row=3, column=0, padx=25, pady=3, sticky="w") # CLI_NOMBRE Label
        self.elements[i][1].config(width=largo_entries) # CLI_NOMBRE Entry
        self.elements[i][1].grid(row=3, column=1, padx=5, pady=3, columnspan=4, sticky="ew") # Span to use more space
        i += 1 # i is now 8

        # Row 4: CLI_DIRANT
        self.elements[i][0].grid(row=4, column=0, padx=25, pady=3, sticky="w") # CLI_DIRANT Label
        self.elements[i][1].config(width=largo_entries) # CLI_DIRANT Entry
        self.elements[i][1].grid(row=4, column=1, padx=5, pady=3, columnspan=4, sticky="ew")
        i += 1 # i is now 9

        # Row 5: CLI_DIRECC
        self.elements[i][0].grid(row=5, column=0, padx=25, pady=3, sticky="w") # CLI_DIRECC Label
        self.elements[i][1].config(width=int(largo_entries*0.7)) # CLI_DIRECC Entry
        self.elements[i][1].grid(row=5, column=1, padx=5, pady=3, columnspan=4, sticky="ew")
        i += 1 # i is now 10

        # Row 6: CLI_TIVIPR, CLI_VIAPRI, CLI_LETRAS, CLI_SUFIJO, CLI_SECTOR
        # These are all related to address components, so they fit well on one row.
        self.elements[i][0].grid(row=6, column=0, padx=25, pady=3, sticky="w") # CLI_TIVIPR Label
        self.elements[i][1].config(width=5) # CLI_TIVIPR Entry
        self.elements[i][1].grid(row=6, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=6, column=2, padx=5, pady=3, sticky="w") # CLI_VIAPRI Label
        self.elements[i+1][1].config(width=10) # CLI_VIAPRI Entry
        self.elements[i+1][1].grid(row=6, column=3, padx=5, pady=3, sticky="w")

        self.elements[i+2][0].grid(row=6, column=4, padx=5, pady=3, sticky="w") # CLI_LETRAS Label
        self.elements[i+2][1].config(width=2) # CLI_LETRAS Entry
        self.elements[i+2][1].grid(row=6, column=5, padx=5, pady=3, sticky="w")

        self.elements[i+3][0].grid(row=6, column=6, padx=5, pady=3, sticky="w") # CLI_SUFIJO Label
        self.elements[i+3][1].config(width=4) # CLI_SUFIJO Entry
        self.elements[i+3][1].grid(row=6, column=7, padx=5, pady=3, sticky="w")

        self.elements[i+4][0].grid(row=6, column=8, padx=5, pady=3, sticky="w") # CLI_SECTOR Label
        self.elements[i+4][1].config(width=5) # CLI_SECTOR Entry
        self.elements[i+4][1].grid(row=6, column=9, padx=5, pady=3, sticky="w")
        i += 5 # i is now 15

        # Row 7: CLI_TIVIGE, CLI_VIAGEN, CLI_LETRGE, CLI_SECTGE
        # Similar to the previous row, these can be grouped horizontally.
        self.elements[i][0].grid(row=7, column=0, padx=25, pady=3, sticky="w") # CLI_TIVIGE Label
        self.elements[i][1].config(width=5) # CLI_TIVIGE Entry
        self.elements[i][1].grid(row=7, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=7, column=2, padx=5, pady=3, sticky="w") # CLI_VIAGEN Label
        self.elements[i+1][1].config(width=10) # CLI_VIAGEN Entry
        self.elements[i+1][1].grid(row=7, column=3, padx=5, pady=3, sticky="w")

        self.elements[i+2][0].grid(row=7, column=4, padx=5, pady=3, sticky="w") # CLI_LETRGE Label
        self.elements[i+2][1].config(width=2) # CLI_LETRGE Entry
        self.elements[i+2][1].grid(row=7, column=5, padx=5, pady=3, sticky="w")

        self.elements[i+3][0].grid(row=7, column=6, padx=5, pady=3, sticky="w") # CLI_SECTGE Label
        self.elements[i+3][1].config(width=5) # CLI_SECTGE Entry
        self.elements[i+3][1].grid(row=7, column=7, padx=5, pady=3, sticky="w")
        i += 4 # i is now 19

        # Row 8: CLI_NROPRE
        self.elements[i][0].grid(row=8, column=0, padx=25, pady=3, sticky="w") # CLI_NROPRE Label
        self.elements[i][1].config(width=10) # CLI_NROPRE Entry
        self.elements[i][1].grid(row=8, column=1, padx=5, pady=3, sticky="w")
        i += 1 # i is now 20

        current_row = 9 # Starting row for "Other" fields

        # Rows 9-12: "Other" fields (CLI_TIOTRx, CLI_OTROx)
        # Each pair will occupy one row, spanning two columns for entry values
        for j in range(4):
            lbl_tiotr_idx = i + (j * 2)
            ent_tiotr_idx = lbl_tiotr_idx
            lbl_otro_idx = i + (j * 2) + 1
            ent_otro_idx = lbl_otro_idx

            # Label and Entry for CLI_TIOTRx
            self.elements[lbl_tiotr_idx][0].grid(row=current_row + j, column=0, padx=25, pady=3, sticky="w")
            self.elements[ent_tiotr_idx][1].config(width=int(largo_entries * 0.4))
            self.elements[ent_tiotr_idx][1].grid(row=current_row + j, column=1, padx=5, pady=3, sticky="w")

            # Label and Entry for CLI_OTROx
            self.elements[lbl_otro_idx][0].grid(row=current_row + j, column=2, padx=5, pady=3, sticky="w")
            self.elements[ent_otro_idx][1].config(width=int(largo_entries * 0.6))
            self.elements[ent_otro_idx][1].grid(row=current_row + j, column=3, padx=5, pady=3, sticky="w")

        i += 8 # i is now 28 (20 + 8)
        current_row += 4 # current_row is now 13

        # Row 13: CLI_COCIUD, CLI_CIUDAD
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_COCIUD Label
        self.elements[i][1].config(width=5) # CLI_COCIUD Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_CIUDAD Label
        self.elements[i+1][1].config(width=20) # CLI_CIUDAD Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 30
        current_row += 1 # current_row is now 14

        # Row 14: CLI_COPAIS, CLI_NOPAIS
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_COPAIS Label
        self.elements[i][1].config(width=2) # CLI_COPAIS Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_NOPAIS Label
        self.elements[i+1][1].config(width=25) # CLI_NOPAIS Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 32
        current_row += 1 # current_row is now 15

        # Row 15: CLI_TELEF
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_TELEF Label
        self.elements[i][1].config(width=20) # CLI_TELEF Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, columnspan=3, sticky="ew")
        i += 1 # i is now 33
        current_row += 1 # current_row is now 16

        # Row 16: CLI_CELOPE, CLI_CELNUM
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_CELOPE Label
        self.elements[i][1].config(width=3) # CLI_CELOPE Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_CELNUM Label
        self.elements[i+1][1].config(width=10) # CLI_CELNUM Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 35
        current_row += 1 # current_row is now 17

        # Row 17: CLI_E_MAIL
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_E_MAIL Label
        self.elements[i][1].config(width=30) # CLI_E_MAIL Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, columnspan=3, sticky="ew")
        i += 1 # i is now 36
        current_row += 1 # current_row is now 18

        # Row 18: CLI_CTCBCS, CLI_CTABCS
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_CTCBCS Label
        self.elements[i][1].config(width=12) # CLI_CTCBCS Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_CTABCS Label
        self.elements[i+1][1].config(width=12) # CLI_CTABCS Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 38
        current_row += 1 # current_row is now 19

        # Row 19: CLI_CTCCOL, CLI_CTACOL
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_CTCCOL Label
        self.elements[i][1].config(width=12) # CLI_CTCCOL Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_CTACOL Label
        self.elements[i+1][1].config(width=12) # CLI_CTACOL Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 40
        current_row += 1 # current_row is now 20

        # Row 20: CLI_OFI, CLI_OFICIN
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_OFI Label
        self.elements[i][1].config(width=1) # CLI_OFI Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_OFICIN Label
        self.elements[i+1][1].config(width=4) # CLI_OFICIN Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 42
        current_row += 1 # current_row is now 21

        # Row 21: CLI_OFINOM
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_OFINOM Label
        self.elements[i][1].config(width=25) # CLI_OFINOM Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, columnspan=3, sticky="ew")
        i += 1 # i is now 43
        current_row += 1 # current_row is now 22

        # Row 22: CLI_OFNRCO, CLI_OFNOCO
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_OFNRCO Label
        self.elements[i][1].config(width=4) # CLI_OFNRCO Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_OFNOCO Label
        self.elements[i+1][1].config(width=25) # CLI_OFNOCO Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="ew")
        i += 2 # i is now 45
        current_row += 1 # current_row is now 23

        # Row 23: CLI_CIIU, CLI_NOCIIU
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_CIIU Label
        self.elements[i][1].config(width=4) # CLI_CIIU Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_NOCIIU Label
        self.elements[i+1][1].config(width=25) # CLI_NOCIIU Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="ew")
        i += 2 # i is now 47
        current_row += 1 # current_row is now 24

        # Row 24: CLI_INGRES
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_INGRES Label
        self.elements[i][1].config(width=18) # CLI_INGRES Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")
        i += 1 # i is now 48
        current_row += 1 # current_row is now 25

        # Row 25: CLI_FEACTU, CLI_CCP_FE, CLI_CCP_FV (Dates)
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_FEACTU Label
        self.elements[i][1].config(width=10) # CLI_FEACTU Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_CCP_FE Label
        self.elements[i+1][1].config(width=10) # CLI_CCP_FE Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="w")

        self.elements[i+2][0].grid(row=current_row, column=4, padx=5, pady=3, sticky="w") # CLI_CCP_FV Label
        self.elements[i+2][1].config(width=10) # CLI_CCP_FV Entry
        self.elements[i+2][1].grid(row=current_row, column=5, padx=5, pady=3, sticky="w")
        i += 3 # i is now 51
        current_row += 1 # current_row is now 26

        # Row 26: CLI_CCP_UM, CLI_CCP_UA (Financial Amounts)
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_CCP_UM Label
        self.elements[i][1].config(width=18) # CLI_CCP_UM Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_CCP_UA Label
        self.elements[i+1][1].config(width=18) # CLI_CCP_UA Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 53
        current_row += 1 # current_row is now 27

        # Row 27: CLI_CCP_US, CLI_CCP_UT (Financial Amounts)
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_CCP_US Label
        self.elements[i][1].config(width=18) # CLI_CCP_US Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_CCP_UT Label
        self.elements[i+1][1].config(width=18) # CLI_CCP_UT Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 55
        current_row += 1 # current_row is now 28

        # Row 28: CLI_CCP_SA (Financial Amount)
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_CCP_SA Label
        self.elements[i][1].config(width=18) # CLI_CCP_SA Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")
        i += 1 # i is now 56
        current_row += 1 # current_row is now 29

        # Row 29: CLI_SEGMEN, CLI_CUPOCA
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_SEGMEN Label
        self.elements[i][1].config(width=3) # CLI_SEGMEN Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_CUPOCA Label
        self.elements[i+1][1].config(width=18) # CLI_CUPOCA Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 58
        current_row += 1 # current_row is now 30

        # Row 30: CLI_TIPO, CLI_VIGILA
        self.elements[i][0].grid(row=current_row, column=0, padx=25, pady=3, sticky="w") # CLI_TIPO Label
        self.elements[i][1].config(width=5) # CLI_TIPO Entry
        self.elements[i][1].grid(row=current_row, column=1, padx=5, pady=3, sticky="w")

        self.elements[i+1][0].grid(row=current_row, column=2, padx=5, pady=3, sticky="w") # CLI_VIGILA Label
        self.elements[i+1][1].config(width=1) # CLI_VIGILA Entry
        self.elements[i+1][1].grid(row=current_row, column=3, padx=5, pady=3, sticky="w")
        i += 2 # i is now 60 (covering elements up to 59, which is the 60th element)