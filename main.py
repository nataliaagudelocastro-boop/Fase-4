
# ==============================================
# SOFTWARE FJ
# ARCHIVO PRINCIPAL
# ==============================================

import tkinter as tk

from interfaz.ventana_principal import VentanaPrincipal


# Crear ventana principal
ventana = tk.Tk()

# Crear la aplicación
aplicacion = VentanaPrincipal(ventana)

# Mantener la ventana abierta
ventana.mainloop()
