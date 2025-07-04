import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from View.T_Admini.t_admini_custom_view import t_admini_custom_view
from View.T_Aduanas.t_aduanas_view import t_aduanas_view
from View.T_Acrede.t_acrede_view import t_acrede_view
from View.T_Actore.t_actore_view import t_actore_view
from View.T_Destin.t_destin_view import t_destin_view
from View.T_Autcom.t_autcom_view import t_autcom_view
from View.T_Cam053.t_cam053_view import t_cam053_view
from View.T_Caudev.t_caudev_view import t_caudev_view
from View.T_Ciiu.t_ciiu_view import t_ciiu_view
from View.T_Ciudad.t_ciudad_view import t_ciudad_view
from View.T_Client.t_client_view import t_client_view
from View.T_Combef.t_comdef_view import t_comdef_view
from View.T_Coraba.t_coraba_view import t_coraba_view
from View.T_Corr.t_corr_view import t_corr_view
from View.T_Corswi.t_corswi_view import t_corswi_view
from View.T_Comis.t_comis_view import t_comis_view
from View.T_Destix.t_destix_view import t_destix_view
from View.T_Docum.t_docum_view import t_docum_view
from View.T_Empens.t_empens_view import t_empens_view
from View.T_Equica.t_equica_view import t_equica_view
from View.T_Fe_230.t_fe_230_view import t_fe_230_view
from View.T_Festiv.t_festiv_view import t_festiv_view
from View.T_Gtias.t_gtias_view import t_gtias_view
from View.T_Interm.t_interm_view import t_interm_view
from View.T_Lineas.t_lineas_view import t_lineas_view
from View.T_Mdas.t_mdas_view import t_mdas_view
from View.T_Negoci.t_negoci_view import t_negoci_view
from View.T_Novxml.t_novxml_view import t_novxml_view
from View.T_Numer.t_numer_view import t_numer_view
from View.T_Numex.t_numex_view import t_numex_view
from View.T_Pac008.t_pac008_view import t_pac008_view
from View.T_Pac108.t_pac108_view import t_pac108_view
from View.T_Paises.t_paises_view import t_paises_view
from View.T_Patec.t_patec_view import t_patec_view
from View.T_Procre.t_procre_view import t_procre_view
from View.T_Propre.t_propre_view import t_propre_view
from View.T_Provee.t_provee_view import t_provee_view
from View.T_Puc.t_puc_view import t_puc_view
from View.T_Razone.t_razone_view import t_razone_view
from View.T_Segmen.t_segmen_view import t_segmen_view
from View.T_Sucur.t_sucur_view import t_sucur_view
from View.T_Tasas.t_tasas_view import t_tasas_view
from View.T_Tipefi.t_tipefi_view import t_tipefi_view
from View.T_Tipint.t_tipint_view import t_tipint_view
from View.T_Tippre.t_tippre_view import t_tippre_view
from View.T_Tporbe.t_tporbe_view import t_tporbe_view
from View.T_Transa.t_transa_view import t_transa_view


class pantalla_principal:

    def __init__(self):# Ventana principal
        self.root = tk.Tk()
        self.root.title("I.B.W. - International Business World")
        self.root.state('zoomed')
        self.root.configure(bg="#DAD0F4")

        # Menú principal
        self.barra_menu = tk.Menu(self.root)
        self.root.configure(menu=self.barra_menu)

        menu_tablas = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Tablas", menu=menu_tablas)
        menu_tablas.add_command(label="Actores", command=lambda : t_actore_view(root=self.root))
        menu_tablas.add_command(label="Aduanas", command=lambda: t_aduanas_view(root=self.root))
        menu_tablas.add_command(label="Autorizac de Compras", command=lambda: t_autcom_view(root=self.root))
        menu_tablas.add_command(label="Caracteres no Validos en XML", command=lambda : t_novxml_view(root=self.root))
        menu_tablas.add_command(label="Causales Devol Pensio", command=lambda: t_caudev_view(root=self.root))
        menu_tablas.add_command(label="Ciudades", command=lambda: t_ciudad_view(root=self.root))
        menu_tablas.add_command(label="Clientes", command=lambda: t_client_view(root=self.root))
        menu_tablas.add_command(label="Codigos CIIU", command=lambda: t_ciiu_view(root=self.root))
        menu_tablas.add_command(label="Comisiones", command=lambda : t_comis_view(root=self.root))
        menu_tablas.add_command(label="Comisiones DEFAULT", command=lambda : t_comdef_view(root=self.root))
        menu_tablas.add_command(label="Corresponsales", command=lambda : t_corr_view(root=self.root))
        menu_tablas.add_command(label="Corresponsales - BIC", command=lambda : t_corswi_view(root=self.root))
        menu_tablas.add_command(label="Corresponsales - ABA", command=lambda : t_coraba_view(root=self.root))
        menu_tablas.add_command(label="Destinos de Inversion - XML", command=lambda : t_destix_view(root=self.root))
        menu_tablas.add_command(label="Destinos de Inversion", command=lambda : t_destin_view(root=self.root))
        menu_tablas.add_command(label="Dias Festivos", command=lambda : t_festiv_view(root=self.root))
        menu_tablas.add_command(label="Empresas de Pensiones", command=lambda : t_empens_view(root=self.root))
        menu_tablas.add_command(label="Entidades Administradas", command=lambda : t_admini_custom_view(root=self.root))
        menu_tablas.add_command(label="Equivalen Catastrales", command=lambda : t_equica_view(root=self.root))
        menu_tablas.add_command(label="Etiquetas xml - Pac008 sin head: ni pacs:", command=lambda : t_pac008_view(root=self.root))
        menu_tablas.add_command(label="Etiquetas xml - Pac008 con head: y pacs:" , command=lambda : t_pac108_view(root=self.root))
        menu_tablas.add_command(label="Etiquetas xml - Cam.053", command=lambda: t_cam053_view(root=self.root))
        menu_tablas.add_command(label="Fechas promed Posici", command=lambda : t_fe_230_view(root=self.root))
        menu_tablas.add_command(label="Garantias", command=lambda : t_gtias_view(root=self.root))
        menu_tablas.add_command(label="Intermediarios Financieros", command=lambda : t_interm_view(root=self.root))
        menu_tablas.add_command(label="Monedas", command=lambda : t_mdas_view(root=self.root))
        menu_tablas.add_command(label="Negociadores del Bco", command=lambda : t_negoci_view(root=self.root))
        menu_tablas.add_command(label="Numerales cambiarios - XML", command=lambda : t_numex_view(root=self.root))
        menu_tablas.add_command(label="Numerales Cambiarios", command=lambda : t_numer_view(root=self.root))
        menu_tablas.add_command(label="Oficinas", command=lambda : t_sucur_view(root=self.root))
        menu_tablas.add_command(label="Paises", command=lambda : t_paises_view(root=self.root))
        menu_tablas.add_command(label="parametros Puc", command=lambda : t_puc_view(root=self.root))
        menu_tablas.add_command(label="Patrimonio Tecnico", command=lambda : t_patec_view(root=self.root))
        menu_tablas.add_command(label="Productos", command=lambda : t_lineas_view(root=self.root))
        menu_tablas.add_command(label="Propósitos de Credito", command=lambda : t_procre_view(root=self.root))
        menu_tablas.add_command(label="Proposito del Presam", command=lambda : t_propre_view(root=self.root))
        menu_tablas.add_command(label="Proveedores por Contratos", command=lambda : t_provee_view(root=self.root))
        menu_tablas.add_command(label="Razones de No Canalización", command=lambda : t_razone_view(root=self.root))
        menu_tablas.add_command(label="Segmentos", command=lambda : t_segmen_view(root=self.root))
        menu_tablas.add_command(label="Tasas de Interes", command=lambda : t_tasas_view(root=self.root))
        menu_tablas.add_command(label="Textos", command=lambda : t_docum_view(root=self.root))
        menu_tablas.add_command(label="Tipo de Entidad Financiera", command=lambda : t_tipefi_view(root=self.root))
        menu_tablas.add_command(label="Tipos de intermediario", command=lambda : t_tipint_view(root=self.root))
        menu_tablas.add_command(label="Tipos de prestamo", command=lambda : t_tippre_view(root=self.root))
        menu_tablas.add_command(label="Tipos de Acrededor/Deudor", command=lambda : t_acrede_view(root=self.root))
        menu_tablas.add_command(label="Tipo Ordenan/Benefic", command=lambda : t_tporbe_view(root=self.root))
        menu_tablas.add_command(label="Transaciones", command=lambda : t_transa_view(root=self.root))

        self.root.mainloop()
