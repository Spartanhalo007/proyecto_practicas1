import tkinter as tk
from View.t_display import t_display

class t_actore_display(t_display):
    """Display de campos para la tabla t_actore."""

    def __init__(self, app):
        self.frame = tk.Frame(app)
        self.frame.pack(fill="x", padx=1, pady=1)

        self.elements = []
        self.elements_types = []

        # 1. AC_F_CREMO (fecha) → lo tratamos como texto
        lbl1 = tk.Label(self.frame, text="F_CREMO:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry1 = tk.Entry(self.frame, width=10, bd=0, bg="white")
        self.elements.append([lbl1, entry1])
        self.elements_types.append("str")

        # 2. AC_TIP_ACT (numérico 1 dígito)
        lbl2 = tk.Label(self.frame, text="TIP_ACT:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry2 = tk.Entry(self.frame, width=2, bd=0, bg="white")
        self.elements.append([lbl2, entry2])
        self.elements_types.append("num")

        # 3. AC_TIP_CON (texto 45)
        lbl3 = tk.Label(self.frame, text="TIP_CON:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry3 = tk.Entry(self.frame, width=45, bd=0, bg="white")
        self.elements.append([lbl3, entry3])
        self.elements_types.append("str")

        # 4. AC_TP_IDVC (texto 2)
        lbl4 = tk.Label(self.frame, text="TP_IDVC:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry4 = tk.Entry(self.frame, width=2, bd=0, bg="white")
        self.elements.append([lbl4, entry4])
        self.elements_types.append("str")

        # 5. AC_TP_ID (texto 3)
        lbl5 = tk.Label(self.frame, text="TP_ID:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry5 = tk.Entry(self.frame, width=3, bd=0, bg="white")
        self.elements.append([lbl5, entry5])
        self.elements_types.append("str")

        # 6. AC_NU_ID (texto 20) ← lo usamos como PK
        lbl6 = tk.Label(self.frame, text="NU_ID:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry6 = tk.Entry(self.frame, width=20, bd=0, bg="white")
        self.elements.append([lbl6, entry6])
        self.elements_types.append("str")

        # 7. AC_NOMBRE (texto 100)
        lbl7 = tk.Label(self.frame, text="NOMBRE:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry7 = tk.Entry(self.frame, width=45, bd=0, bg="white")
        self.elements.append([lbl7, entry7])
        self.elements_types.append("str")

        # 8. AC_CIUDAD (texto 5)
        lbl8 = tk.Label(self.frame, text="CIUDAD:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry8 = tk.Entry(self.frame, width=5, bd=0, bg="white")
        self.elements.append([lbl8, entry8])
        self.elements_types.append("str")

        # 9. AC_NOM_CIU (texto 45)
        lbl9 = tk.Label(self.frame, text="NOM_CIU:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry9 = tk.Entry(self.frame, width=45, bd=0, bg="white")
        self.elements.append([lbl9, entry9])
        self.elements_types.append("str")

        # 10. AC_CIIU (texto 4)
        lbl10 = tk.Label(self.frame, text="CIIU:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry10 = tk.Entry(self.frame, width=4, bd=0, bg="white")
        self.elements.append([lbl10, entry10])
        self.elements_types.append("str")

        # 11. AC_CIIUNOM (texto 50)
        lbl11 = tk.Label(self.frame, text="CIIUNOM:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry11 = tk.Entry(self.frame, width=50, bd=0, bg="white")
        self.elements.append([lbl11, entry11])
        self.elements_types.append("str")

        # 12. AC_TELEF (texto 25)
        lbl12 = tk.Label(self.frame, text="TELEF:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry12 = tk.Entry(self.frame, width=25, bd=0, bg="white")
        self.elements.append([lbl12, entry12])
        self.elements_types.append("str")

        # 13. AC_DIRECC (texto 100)
        lbl13 = tk.Label(self.frame, text="DIRECC:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry13 = tk.Entry(self.frame, width=45, bd=0, bg="white")
        self.elements.append([lbl13, entry13])
        self.elements_types.append("str")

        # 14. AC_CORREO (texto 100)
        lbl14 = tk.Label(self.frame, text="CORREO:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry14 = tk.Entry(self.frame, width=45, bd=0, bg="white")
        self.elements.append([lbl14, entry14])
        self.elements_types.append("str")

        # 15. AC_TP_EMPR (numérico 4)
        lbl15 = tk.Label(self.frame, text="TP_EMPR:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry15 = tk.Entry(self.frame, width=4, bd=0, bg="white")
        self.elements.append([lbl15, entry15])
        self.elements_types.append("num")

        # 16. AC_TP_EMNO (texto 60)
        lbl16 = tk.Label(self.frame, text="TP_EMNO:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry16 = tk.Entry(self.frame, width=60, bd=0, bg="white")
        self.elements.append([lbl16, entry16])
        self.elements_types.append("str")

        # 17. AC_SECTOR (texto 2)
        lbl17 = tk.Label(self.frame, text="SECTOR:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry17 = tk.Entry(self.frame, width=2, bd=0, bg="white")
        self.elements.append([lbl17, entry17])
        self.elements_types.append("str")

        # 18. AC_SEC_NOM (texto 10)
        lbl18 = tk.Label(self.frame, text="SEC_NOM:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry18 = tk.Entry(self.frame, width=10, bd=0, bg="white")
        self.elements.append([lbl18, entry18])
        self.elements_types.append("str")

        # 19. AC_TP_EFIN (numérico 3)
        lbl19 = tk.Label(self.frame, text="TP_EFIN:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry19 = tk.Entry(self.frame, width=3, bd=0, bg="white")
        self.elements.append([lbl19, entry19])
        self.elements_types.append("num")

        # 20. AC_TIEFINO (texto 45)
        lbl20 = tk.Label(self.frame, text="TIEFINO:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry20 = tk.Entry(self.frame, width=45, bd=0, bg="white")
        self.elements.append([lbl20, entry20])
        self.elements_types.append("str")

        # 21. AC_SUPERVI (numérico 3)
        lbl21 = tk.Label(self.frame, text="SUPERVI:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry21 = tk.Entry(self.frame, width=3, bd=0, bg="white")
        self.elements.append([lbl21, entry21])
        self.elements_types.append("num")

        # 22. AC_TP_SINP (texto 3)
        lbl22 = tk.Label(self.frame, text="TP_SINP:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry22 = tk.Entry(self.frame, width=3, bd=0, bg="white")
        self.elements.append([lbl22, entry22])
        self.elements_types.append("str")

        # 23. AC_TP_SINO (texto 30)
        lbl23 = tk.Label(self.frame, text="TP_SINO:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry23 = tk.Entry(self.frame, width=30, bd=0, bg="white")
        self.elements.append([lbl23, entry23])
        self.elements_types.append("str")

        # 24. AC_REGIMEN (numérico 3)
        lbl24 = tk.Label(self.frame, text="REGIMEN:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry24 = tk.Entry(self.frame, width=3, bd=0, bg="white")
        self.elements.append([lbl24, entry24])
        self.elements_types.append("num")

        # 25. AC_REGI_NO (texto 10)
        lbl25 = tk.Label(self.frame, text="REGI_NO:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry25 = tk.Entry(self.frame, width=10, bd=0, bg="white")
        self.elements.append([lbl25, entry25])
        self.elements_types.append("str")

        # 26. AC_ACT_SUE (numérico 1)
        lbl26 = tk.Label(self.frame, text="ACT_SUE:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry26 = tk.Entry(self.frame, width=1, bd=0, bg="white")
        self.elements.append([lbl26, entry26])
        self.elements_types.append("num")

        # 27. AC_NU_ADMI (numérico 15)
        lbl27 = tk.Label(self.frame, text="NU_ADMI:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry27 = tk.Entry(self.frame, width=15, bd=0, bg="white")
        self.elements.append([lbl27, entry27])
        self.elements_types.append("num")

        # 28. AC_NU_PATR (numérico 15)
        lbl28 = tk.Label(self.frame, text="NU_PATR:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry28 = tk.Entry(self.frame, width=15, bd=0, bg="white")
        self.elements.append([lbl28, entry28])
        self.elements_types.append("num")

        # 29. AC_NO_PATR (texto 100)
        lbl29 = tk.Label(self.frame, text="NO_PATR:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry29 = tk.Entry(self.frame, width=45, bd=0, bg="white")
        self.elements.append([lbl29, entry29])
        self.elements_types.append("str")

        # 30. AC_TPIDVAC (texto 2)
        lbl30 = tk.Label(self.frame, text="TPIDVAC:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry30 = tk.Entry(self.frame, width=2, bd=0, bg="white")
        self.elements.append([lbl30, entry30])
        self.elements_types.append("str")

        # 31. AC_NATURAL (numérico 3)
        lbl31 = tk.Label(self.frame, text="NATURAL:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry31 = tk.Entry(self.frame, width=3, bd=0, bg="white")
        self.elements.append([lbl31, entry31])
        self.elements_types.append("num")

        # 32. AC_PAISRES (texto 3)
        lbl32 = tk.Label(self.frame, text="PAISRES:", font=("Arial",8,"bold"), bg="#c0c0c0")
        entry32 = tk.Entry(self.frame, width=3, bd=0, bg="white")
        self.elements.append([lbl32, entry32])
        self.elements_types.append("str")

        bg = "#c0c0c0"
        self.frame.configure(bg=bg)

                # Aplicar estilo a todos los Entry
        for _, entry in self.elements:
            entry.config(
                highlightthickness=1,
                highlightcolor="black",
                highlightbackground="black",
                justify="right",
                bg="white"
            )


        largo_entries = 70  # o el valor que necesites

        i = 0

        # 1. AC_F_CREMO
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].grid(row=i, column=1, padx=5, pady=3, sticky="w")
        i += 1

        # 2. AC_TIP_ACT
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].grid(row=i, column=1, padx=5, pady=3, sticky="w")

        # 3. AC_TIP_CON
        # self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i+1][1].config(width=largo_entries)
        self.elements[i+1][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 2

        # 4. AC_TP_IDVC
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 5. AC_TP_ID
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 6. AC_NU_ID
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 7. AC_NOMBRE
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 8. AC_CIUDAD
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].grid(row=i, column=1, padx=5, pady=3, sticky="w")

        # 9. AC_NOM_CIU
        # self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i+1][1].config(width=largo_entries)
        self.elements[i+1][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 2

        # 10. AC_CIIU
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].grid(row=i, column=1, padx=5, pady=3, sticky="w")

        # 11. AC_CIIUNOM
        # self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i+1][1].config(width=largo_entries)
        self.elements[i+1][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 2

        # 12. AC_TELEF
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 13. AC_DIRECC
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 14. AC_CORREO
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 15. AC_TP_EMPR
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].grid(row=i, column=1, padx=5, pady=3, sticky="w")
        i += 1

        # 16. AC_TP_EMNO
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 17. AC_SECTOR
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].grid(row=i, column=1, padx=5, pady=3, sticky="w")

        # 18. AC_SEC_NOM
        # self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i+1][1].config(width=largo_entries)
        self.elements[i+1][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 2

        # 19. AC_TP_EFIN
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].grid(row=i, column=1, padx=5, pady=3, sticky="w")
        i += 1

        # 20. AC_TIEFINO
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 21. AC_SUPERVI
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].grid(row=i, column=1, padx=5, pady=3, sticky="w")
        i += 1

        # 22. AC_TP_SINP
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].grid(row=i, column=1, padx=5, pady=3, sticky="w")
        i += 1

        # 23. AC_TP_SINO
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 24. AC_REGIMEN
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].grid(row=i, column=1, padx=5, pady=3, sticky="w")

        # 25. AC_REGI_NO
        # self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i+1][1].config(width=largo_entries)
        self.elements[i+1][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 2

        # 26. AC_ACT_SUE
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].grid(row=i, column=1, padx=5, pady=3, sticky="w")
        i += 1

        # 27. AC_NU_ADMI
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 28. AC_NU_PATR
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 29. AC_NO_PATR
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 30. AC_TPIDVAC
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 31. AC_NATURAL
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1

        # 32. AC_PAISRES
        self.elements[i][0].grid(row=i, column=0, padx=25, pady=3, sticky="w")
        self.elements[i][1].config(width=largo_entries)
        self.elements[i][1].grid(row=i, column=2, padx=5, pady=3, sticky="w")
        i += 1
