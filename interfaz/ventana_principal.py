
# ==============================================
# SOFTWARE FJ
# VENTANA PRINCIPAL DE LA APLICACIÓN
# ==============================================

import tkinter as tk
from tkinter import ttk, messagebox

from clases.cliente import Cliente

# ==============================================
# CLASE: VENTANA PRINCIPAL
# ==============================================

class VentanaPrincipal:

    def __init__(self, ventana):

        # Configuración de la ventana
        self.ventana = ventana
        # Lista donde se almacenarán los clientes registrados
        self.clientes = []
        self.ventana.title("Software FJ - Gestión de Servicios y Reservas")
        self.ventana.geometry("1100x700")
        self.ventana.minsize(950, 600)
        self.ventana.configure(bg="#F0F4F8")

        # Colores principales
        self.azul_oscuro = "#142D50"
        self.azul = "#1769AA"
        self.azul_claro = "#E8F1FA"
        self.blanco = "#FFFFFF"
        self.gris = "#F0F4F8"
        self.texto = "#243447"

        # Configuración de estilos
        self.configurar_estilos()

        # Construcción de la interfaz
        self.crear_menu_lateral()
        self.crear_encabezado()
        self.crear_contenido()
        self.crear_panel_eventos()

        # Mostrar la página inicial
        self.mostrar_inicio()

    # ==========================================
    # CONFIGURAR ESTILOS
    # ==========================================

    def configurar_estilos(self):

        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Tarjeta.TFrame",
            background=self.blanco
        )

        estilo.configure(
            "Titulo.TLabel",
            background=self.blanco,
            foreground=self.texto,
            font=("Times New Roman", 12, "bold")
        )

    # ==========================================
    # CREAR MENU LATERAL
    # ==========================================

    def crear_menu_lateral(self):

        self.menu = tk.Frame(
            self.ventana,
            bg=self.azul_oscuro,
            width=220
        )

        self.menu.pack(side="left", fill="y")
        self.menu.pack_propagate(False)

        # Nombre de la empresa
        tk.Label(
            self.menu,
            text="FJ",
            bg=self.azul_oscuro,
            fg="white",
            font=("Segoe UI", 38, "bold")
        ).pack(pady=(30, 0))

        tk.Label(
            self.menu,
            text="SOFTWARE FJ",
            bg=self.azul_oscuro,
            fg="white",
            font=("Times New Roman", 16, "bold")
        ).pack(pady=5)

        tk.Label(
            self.menu,
            text="Gestión de servicios",
            bg=self.azul_oscuro,
            fg="#B9D7F2",
            font=("Segoe UI", 10)
        ).pack(pady=(0, 30))

        # Opciones del menú
        opciones = [
            ("⌂  Inicio", "Inicio"),
            ("♙  Clientes", "Clientes"),
            ("▤  Servicios", "Servicios"),
            ("▦  Reservas", "Reservas"),
            ("⌕  Consultas", "Consultas"),
            ("▣  Reportes", "Reportes"),
            ("⚠  Registro de errores", "Errores")
        ]

        for texto, seccion in opciones:

            boton = tk.Button(
                self.menu,
                text=texto,
                bg=self.azul_oscuro,
                fg="white",
                activebackground=self.azul,
                activeforeground="white",
                font=("Segoe UI", 11),
                relief="flat",
                anchor="w",
                padx=20,
                pady=12,
                cursor="hand2",
                command=lambda s=seccion: self.mostrar_seccion(s)
            )

            boton.pack(fill="x", padx=10, pady=3)

        # Botón para salir
        tk.Button(
            self.menu,
            text="⏻  Salir",
            bg=self.azul_oscuro,
            fg="white",
            activebackground="#A83232",
            activeforeground="white",
            font=("Times New Roman", 11),
            relief="flat",
            cursor="hand2",
            command=self.ventana.destroy
        ).pack(side="bottom", fill="x", padx=10, pady=20)

    # ==========================================
    # CREAR ENCABEZADO
    # ==========================================

    def crear_encabezado(self):

        self.encabezado = tk.Frame(
            self.ventana,
            bg=self.azul_oscuro,
            height=115
        )

        self.encabezado.pack(fill="x")
        self.encabezado.pack_propagate(False)

        tk.Label(
            self.encabezado,
            text="Bienvenido a Software FJ",
            bg=self.azul_oscuro,
            fg="white",
            font=("Times New Roman", 23, "bold")
        ).pack(anchor="w", padx=30, pady=(20, 5))

        tk.Label(
            self.encabezado,
            text="Sistema Integral de Clientes, Servicios y Reservas",
            bg=self.azul_oscuro,
            fg="#D5E6F7",
            font=("Segoe UI", 12)
        ).pack(anchor="w", padx=30)

    # ==========================================
    # CREAR AREA DE CONTENIDO
    # ==========================================

    def crear_contenido(self):

        self.contenido = tk.Frame(
            self.ventana,
            bg=self.gris
        )

        self.contenido.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

    # ==========================================
    # MOSTRAR PAGINA INICIAL
    # ==========================================

    def mostrar_inicio(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Panel principal",
            bg=self.gris,
            fg=self.texto,
            font=("Times New Roman", 20, "bold")
        ).pack(anchor="w", pady=(5, 15))

        # Contenedor de tarjetas
        contenedor_tarjetas = tk.Frame(
            self.contenido,
            bg=self.gris
        )

        contenedor_tarjetas.pack(fill="x")

        tarjetas = [
            ("Clientes registrados", "0", "#1769AA"),
            ("Servicios disponibles", "0", "#16865B"),
            ("Reservas activas", "0", "#7542B8")
        ]

        for titulo, cantidad, color in tarjetas:

            tarjeta = tk.Frame(
                contenedor_tarjetas,
                bg=self.blanco,
                highlightbackground="#D5DFEA",
                highlightthickness=1
            )

            tarjeta.pack(
                side="left",
                fill="both",
                expand=True,
                padx=6,
                pady=5
            )

            tk.Label(
                tarjeta,
                text=titulo,
                bg=self.blanco,
                fg=self.texto,
                font=("Times New Roman", 11, "bold")
            ).pack(pady=(20, 5))

            tk.Label(
                tarjeta,
                text=cantidad,
                bg=self.blanco,
                fg=color,
                font=("Times New Roman", 28, "bold")
            ).pack(pady=(0, 20))

        # Mensaje de bienvenida
        bienvenida = tk.Frame(
            self.contenido,
            bg=self.blanco,
            highlightbackground="#D5DFEA",
            highlightthickness=1
        )

        bienvenida.pack(fill="both", expand=True, pady=20)

        tk.Label(
            bienvenida,
            text="Sistema de gestión Software FJ",
            bg=self.blanco,
            fg=self.azul_oscuro,
            font=("Times New Roman", 18, "bold")
        ).pack(pady=(50, 15))

        tk.Label(
            bienvenida,
            text="Administra tus clientes, servicios y reservas\n"
                 "desde una sola aplicación.",
            bg=self.blanco,
            fg=self.texto,
            font=("Times New Roman", 12),
            justify="center"
        ).pack(pady=10)

        tk.Label(
            bienvenida,
            text="Selecciona una opción del menú lateral para comenzar.",
            bg=self.blanco,
            fg=self.azul,
            font=("Times New Roman", 11, "bold")
        ).pack(pady=15)





    # ==========================================
    # MODULO DE CLIENTES
    # ==========================================

    def mostrar_clientes(self):

        self.limpiar_contenido()

        # Titulo del modulo
        tk.Label(
            self.contenido,
            text="Gestión de clientes",
            bg=self.gris,
            fg=self.azul_oscuro,
            font=("Times New Roman", 20, "bold")
        ).pack(anchor="w", pady=(5, 15))

        # Formulario de registro
        formulario = tk.LabelFrame(
            self.contenido,
            text="Registrar nuevo cliente",
            bg=self.blanco,
            fg=self.azul_oscuro,
            font=("Times New Roman", 11, "bold"),
            padx=15,
            pady=15
        )

        formulario.pack(fill="x", pady=10)

        # Variables para almacenar los datos
        self.nombre_var = tk.StringVar()
        self.documento_var = tk.StringVar()
        self.telefono_var = tk.StringVar()
        self.correo_var = tk.StringVar()

        # Campo nombre
        tk.Label(formulario, text="Nombre completo:",
                 bg=self.blanco).grid(row=0, column=0,
                                      sticky="w", padx=5, pady=5)

        ttk.Entry(formulario, textvariable=self.nombre_var,
                  width=35).grid(row=0, column=1, padx=5, pady=5)

        # Campo documento
        tk.Label(formulario, text="Documento:",
                 bg=self.blanco).grid(row=0, column=2,
                                      sticky="w", padx=5, pady=5)

        ttk.Entry(formulario, textvariable=self.documento_var,
                  width=25).grid(row=0, column=3, padx=5, pady=5)

        # Campo telefono
        tk.Label(formulario, text="Teléfono:",
                 bg=self.blanco).grid(row=1, column=0,
                                      sticky="w", padx=5, pady=5)

        ttk.Entry(formulario, textvariable=self.telefono_var,
                  width=35).grid(row=1, column=1, padx=5, pady=5)

        # Campo correo
        tk.Label(formulario, text="Correo electrónico:",
                 bg=self.blanco).grid(row=1, column=2,
                                      sticky="w", padx=5, pady=5)

        ttk.Entry(formulario, textvariable=self.correo_var,
                  width=25).grid(row=1, column=3, padx=5, pady=5)

        # Boton guardar
        ttk.Button(
            formulario,
            text="Guardar cliente",
            command=self.registrar_cliente
        ).grid(row=2, column=1, pady=15)

        # Tabla de clientes
        tk.Label(
            self.contenido,
            text="Clientes registrados",
            bg=self.gris,
            fg=self.azul_oscuro,
            font=("Times New Roman", 14, "bold")
        ).pack(anchor="w", pady=(15, 8))

        self.tabla_clientes = ttk.Treeview(
            self.contenido,
            columns=("nombre", "documento", "telefono", "correo"),
            show="headings",
            height=8
        )

        self.tabla_clientes.heading("nombre", text="Nombre")
        self.tabla_clientes.heading("documento", text="Documento")
        self.tabla_clientes.heading("telefono", text="Teléfono")
        self.tabla_clientes.heading("correo", text="Correo electrónico")

        self.tabla_clientes.column("nombre", width=180)
        self.tabla_clientes.column("documento", width=120)
        self.tabla_clientes.column("telefono", width=120)
        self.tabla_clientes.column("correo", width=220)

        self.tabla_clientes.pack(fill="both", expand=True)

        # Mostrar clientes que ya estén registrados
        self.actualizar_tabla_clientes()

    # ==========================================
    # REGISTRAR CLIENTE
    # ==========================================

    def registrar_cliente(self):

        try:

            # Obtener los datos del formulario
            nombre = self.nombre_var.get()
            documento = self.documento_var.get()
            telefono = self.telefono_var.get()
            correo = self.correo_var.get()

            # Comprobar si el documento ya existe
            for cliente in self.clientes:

                if cliente.obtener_datos()["documento"] == documento.strip():
                    raise ValueError("Ya existe un cliente con ese documento.")

            # Crear el objeto cliente
            nuevo_cliente = Cliente(
                nombre,
                documento,
                telefono,
                correo
            )

            # Guardar el objeto en la lista
            self.clientes.append(nuevo_cliente)

            # Actualizar la tabla
            self.actualizar_tabla_clientes()

            # Limpiar formulario
            self.nombre_var.set("")
            self.documento_var.set("")
            self.telefono_var.set("")
            self.correo_var.set("")

            messagebox.showinfo(
                "Registro exitoso",
                "El cliente se registró correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error de registro",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error inesperado",
                f"Ocurrió un problema: {error}"
            )

    # ==========================================
    # ACTUALIZAR TABLA DE CLIENTES
    # ==========================================

    def actualizar_tabla_clientes(self):

        # Eliminar filas anteriores
        for fila in self.tabla_clientes.get_children():
            self.tabla_clientes.delete(fila)

        # Agregar los clientes registrados
        for cliente in self.clientes:

            datos = cliente.obtener_datos()

            self.tabla_clientes.insert(
                "",
                "end",
                values=(
                    datos["nombre"],
                    datos["documento"],
                    datos["telefono"],
                    datos["correo"]
                )
            )

    # ==========================================
    # LIMPIAR CONTENIDO
    # ==========================================

    def limpiar_contenido(self):

        for elemento in self.contenido.winfo_children():
            elemento.destroy()

    # ==========================================
    # NAVEGACION ENTRE SECCIONES
    # ==========================================

    def mostrar_seccion(self, seccion):

        if seccion == "Clientes":
            self.mostrar_clientes()
            return

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text=seccion,
            bg=self.gris,
            fg=self.azul_oscuro,
            font=("Times New Roman", 22, "bold")
        ).pack(anchor="w", pady=20)

        tk.Label(
            self.contenido,
            text=f"El módulo de {seccion} se desarrollará en las siguientes fases.",
            bg=self.gris,
            fg=self.texto,
            font=("Times New Roman", 12)
        ).pack(anchor="w", pady=10)

    # ==========================================
    # PANEL DE EVENTOS
    # ==========================================

    def crear_panel_eventos(self):

        self.panel_eventos = tk.Frame(
            self.ventana,
            bg=self.blanco,
            height=85
        )

        self.panel_eventos.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        self.panel_eventos.pack_propagate(False)

        tk.Label(
            self.panel_eventos,
            text="Eventos del sistema",
            bg=self.blanco,
            fg=self.azul_oscuro,
            font=("Times New Roman", 10, "bold")
        ).pack(anchor="w", padx=10, pady=(8, 3))

        self.texto_eventos = tk.Label(
            self.panel_eventos,
            text="Software FJ iniciado correctamente.",
            bg=self.blanco,
            fg="#16865B",
            font=("Segoe UI", 9)
        )

        self.texto_eventos.pack(anchor="w", padx=10)


# ==============================================
# INICIAR APLICACION
# ==============================================

if __name__ == "__main__":

    ventana = tk.Tk()

    aplicacion = VentanaPrincipal(ventana)

    ventana.mainloop()
