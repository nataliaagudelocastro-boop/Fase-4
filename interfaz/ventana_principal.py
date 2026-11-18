
# ==================================================
# SOFTWARE FJ
# VENTANA PRINCIPAL DE LA APLICACION
# ==================================================

import tkinter as tk
from tkinter import ttk, messagebox

from clases.cliente import Cliente


# ==================================================
# CLASE PRINCIPAL
# ==================================================

class VentanaPrincipal:

    def __init__(self, ventana):

        # Configuracion de la ventana
        self.ventana = ventana
        self.ventana.title("Software FJ - Gestion de Servicios y Clientes")
        self.ventana.geometry("1100x700")
        self.ventana.minsize(900, 600)
        self.ventana.configure(bg="#F2F4F8")

        # Lista donde se almacenan los clientes
        self.clientes = []

        # Variable para controlar el registro inicial
        self.registro_inicial = True

        # Configurar estilos
        self.configurar_estilos()

        # Crear los contenedores principales
        self.menu = tk.Frame(self.ventana, bg="#1E3A5F", width=220)
        self.menu.pack(side="left", fill="y")
        self.menu.pack_propagate(False)

        self.contenedor_principal = tk.Frame(
            self.ventana,
            bg="#F2F4F8"
        )
        self.contenedor_principal.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Encabezado
        self.encabezado = tk.Frame(
            self.contenedor_principal,
            bg="#FFFFFF",
            height=70
        )
        self.encabezado.pack(fill="x")
        self.encabezado.pack_propagate(False)

        self.titulo_encabezado = tk.Label(
            self.encabezado,
            text="SOFTWARE FJ",
            font=("Arial", 18, "bold"),
            bg="#FFFFFF",
            fg="#1E3A5F"
        )
        self.titulo_encabezado.pack(
            side="left",
            padx=25,
            pady=18
        )

        # Area de contenido
        self.contenido = tk.Frame(
            self.contenedor_principal,
            bg="#F2F4F8"
        )
        self.contenido.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # Crear el menu lateral
        self.crear_menu()

        # Mostrar primero el formulario de registro
        self.mostrar_registro_inicial()

    # ==================================================
    # CONFIGURACION DE ESTILOS
    # ==================================================

    def configurar_estilos(self):

        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Treeview",
            background="#FFFFFF",
            foreground="#333333",
            rowheight=30,
            fieldbackground="#FFFFFF",
            font=("Arial", 10)
        )

        estilo.configure(
            "Treeview.Heading",
            background="#1E3A5F",
            foreground="white",
            font=("Arial", 10, "bold")
        )

        estilo.map(
            "Treeview",
            background=[("selected", "#D4AF37")],
            foreground=[("selected", "#1E3A5F")]
        )

    # ==================================================
    # MENU LATERAL
    # ==================================================

    def crear_menu(self):

        titulo = tk.Label(
            self.menu,
            text="SOFTWARE FJ",
            font=("Arial", 17, "bold"),
            bg="#1E3A5F",
            fg="white"
        )
        titulo.pack(pady=30)

        opciones = [
            ("Inicio", self.mostrar_inicio),
            ("Clientes", self.mostrar_clientes),
            ("Servicios", self.mostrar_servicios),
            ("Reservas", self.mostrar_reservas),
            ("Consultas", self.mostrar_consultas),
            ("Reportes", self.mostrar_reportes),
            ("Registro de errores", self.mostrar_errores)
        ]

        for texto, comando in opciones:

            boton = tk.Button(
                self.menu,
                text=texto,
                font=("Arial", 11),
                bg="#1E3A5F",
                fg="white",
                activebackground="#D4AF37",
                activeforeground="#1E3A5F",
                relief="flat",
                anchor="w",
                padx=25,
                pady=12,
                cursor="hand2",
                command=comando
            )

            boton.pack(fill="x", padx=8, pady=3)

    # ==================================================
    # LIMPIAR AREA DE CONTENIDO
    # ==================================================

    def limpiar_contenido(self):

        for elemento in self.contenido.winfo_children():
            elemento.destroy()

    # ==================================================
    # FORMULARIO DE REGISTRO INICIAL
    # ==================================================

    def mostrar_registro_inicial(self):

        self.limpiar_contenido()

        # Ocultar el menu mientras se realiza el registro
        self.menu.pack_forget()

        titulo = tk.Label(
            self.contenido,
            text="Bienvenido a Software FJ",
            font=("Arial", 24, "bold"),
            bg="#F2F4F8",
            fg="#1E3A5F"
        )
        titulo.pack(pady=(20, 5))

        subtitulo = tk.Label(
            self.contenido,
            text="Para comenzar, registra tus datos personales",
            font=("Arial", 12),
            bg="#F2F4F8",
            fg="#555555"
        )
        subtitulo.pack(pady=5)

        # Formulario de registro
        formulario = tk.Frame(
            self.contenido,
            bg="white",
            padx=40,
            pady=20
        )
        formulario.pack(
            fill="x",
            padx=80,
            pady=15
        )

        # Variables para almacenar los datos
        self.nombre_inicial = tk.StringVar()
        self.documento_inicial = tk.StringVar()
        self.telefono_inicial = tk.StringVar()
        self.correo_inicial = tk.StringVar()

        # Campos del formulario
        campos = [
            ("Nombre completo:", self.nombre_inicial),
            ("Documento:", self.documento_inicial),
            ("Telefono:", self.telefono_inicial),
            ("Correo electronico:", self.correo_inicial)
        ]

        for texto, variable in campos:

            etiqueta = tk.Label(
                formulario,
                text=texto,
                font=("Arial", 11, "bold"),
                bg="white",
                fg="#1E3A5F"
            )
            etiqueta.pack(anchor="w", pady=(8, 3))

            entrada = tk.Entry(
                formulario,
                textvariable=variable,
                font=("Arial", 11),
                width=40,
                relief="solid",
                bd=1
            )
            entrada.pack(
                fill="x",
                ipady=6,
                pady=3
            )

        # Boton para ingresar al menu principal
        boton_registrar = tk.Button(
            formulario,
            text="REGISTRAR Y CONTINUAR",
            font=("Arial", 12, "bold"),
            bg="#1E3A5F",
            fg="white",
            activebackground="#D4AF37",
            activeforeground="#1E3A5F",
            relief="flat",
            cursor="hand2",
            command=self.registrar_cliente
        )

        boton_registrar.pack(
            fill="x",
            pady=(20, 5),
            ipady=10
        )

    # ==================================================
    # REGISTRAR CLIENTE
    # ==================================================

    def registrar_cliente(self):

        try:

            if self.registro_inicial:

                nombre = self.nombre_inicial.get()
                documento = self.documento_inicial.get()
                telefono = self.telefono_inicial.get()
                correo = self.correo_inicial.get()

            else:

                nombre = self.nombre_cliente.get()
                documento = self.documento_cliente.get()
                telefono = self.telefono_cliente.get()
                correo = self.correo_cliente.get()

            # Crear un objeto de la clase Cliente
            nuevo_cliente = Cliente(
                nombre,
                documento,
                telefono,
                correo
            )

            # Evitar documentos repetidos
            for cliente in self.clientes:

                if cliente.obtener_datos()["documento"] == documento.strip():

                    raise ValueError(
                        "Ya existe un cliente registrado con ese documento."
                    )

            # Agregar el cliente a la lista
            self.clientes.append(nuevo_cliente)

            if self.registro_inicial:

                self.registro_inicial = False

                messagebox.showinfo(
                    "Registro exitoso",
                    "Tus datos fueron registrados correctamente."
                )

                self.mostrar_menu_principal()

            else:

                self.actualizar_tabla_clientes()

                # Limpiar los campos
                self.nombre_cliente.set("")
                self.documento_cliente.set("")
                self.telefono_cliente.set("")
                self.correo_cliente.set("")

                messagebox.showinfo(
                    "Registro exitoso",
                    "El cliente fue registrado correctamente."
                )

        except ValueError as error:

            messagebox.showerror(
                "Error de validacion",
                str(error)
            )

        except Exception as error:

            messagebox.showerror(
                "Error inesperado",
                f"Ocurrio un error: {error}"
            )

    # ==================================================
    # MOSTRAR MENU PRINCIPAL
    # ==================================================

    def mostrar_menu_principal(self):

        self.menu.pack(
            side="left",
            fill="y",
            before=self.contenedor_principal
        )

        self.mostrar_inicio()

    # ==================================================
    # MODULO INICIO
    # ==================================================

    def mostrar_inicio(self):

        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Panel principal",
            font=("Arial", 23, "bold"),
            bg="#F2F4F8",
            fg="#1E3A5F"
        )
        titulo.pack(anchor="w", pady=15)

        bienvenida = tk.Label(
            self.contenido,
            text="Bienvenido al sistema de gestion de servicios.",
            font=("Arial", 12),
            bg="#F2F4F8",
            fg="#555555"
        )
        bienvenida.pack(anchor="w", pady=5)

        # Panel de informacion
        panel = tk.Frame(
            self.contenido,
            bg="white",
            padx=25,
            pady=25
        )
        panel.pack(fill="x", pady=25)

        total_clientes = len(self.clientes)

        tk.Label(
            panel,
            text="CLIENTES REGISTRADOS",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#1E3A5F"
        ).pack(anchor="w")

        tk.Label(
            panel,
            text=str(total_clientes),
            font=("Arial", 30, "bold"),
            bg="white",
            fg="#D4AF37"
        ).pack(anchor="w", pady=10)

        tk.Label(
            self.contenido,
            text="Utiliza el menu lateral para acceder a los modulos.",
            font=("Arial", 11),
            bg="#F2F4F8",
            fg="#555555"
        ).pack(anchor="w", pady=10)

    # ==================================================
    # MODULO CLIENTES
    # ==================================================

    def mostrar_clientes(self):

        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Gestion de clientes",
            font=("Arial", 22, "bold"),
            bg="#F2F4F8",
            fg="#1E3A5F"
        )
        titulo.pack(anchor="w", pady=10)

        # Formulario para agregar clientes
        formulario = tk.Frame(
            self.contenido,
            bg="white",
            padx=20,
            pady=15
        )
        formulario.pack(fill="x", pady=10)

        self.nombre_cliente = tk.StringVar()
        self.documento_cliente = tk.StringVar()
        self.telefono_cliente = tk.StringVar()
        self.correo_cliente = tk.StringVar()

        campos = [
            ("Nombre:", self.nombre_cliente),
            ("Documento:", self.documento_cliente),
            ("Telefono:", self.telefono_cliente),
            ("Correo:", self.correo_cliente)
        ]

        for texto, variable in campos:

            fila = tk.Frame(formulario, bg="white")
            fila.pack(fill="x", pady=5)

            tk.Label(
                fila,
                text=texto,
                font=("Arial", 10, "bold"),
                bg="white",
                fg="#1E3A5F",
                width=15,
                anchor="w"
            ).pack(side="left")

            tk.Entry(
                fila,
                textvariable=variable,
                font=("Arial", 10),
                width=40
            ).pack(side="left", ipady=4)

        boton_registrar = tk.Button(
            formulario,
            text="Registrar cliente",
            font=("Arial", 10, "bold"),
            bg="#1E3A5F",
            fg="white",
            activebackground="#D4AF37",
            activeforeground="#1E3A5F",
            relief="flat",
            cursor="hand2",
            command=self.registrar_cliente
        )
        boton_registrar.pack(anchor="e", pady=12, ipadx=10, ipady=5)

        # Tabla de clientes
        tabla_frame = tk.Frame(
            self.contenido,
            bg="white",
            padx=10,
            pady=10
        )
        tabla_frame.pack(fill="both", expand=True, pady=10)

        columnas = (
            "nombre",
            "documento",
            "telefono",
            "correo"
        )

        self.tabla_clientes = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_clientes.heading("nombre", text="Nombre")
        self.tabla_clientes.heading("documento", text="Documento")
        self.tabla_clientes.heading("telefono", text="Telefono")
        self.tabla_clientes.heading("correo", text="Correo electronico")

        self.tabla_clientes.column("nombre", width=180)
        self.tabla_clientes.column("documento", width=120)
        self.tabla_clientes.column("telefono", width=120)
        self.tabla_clientes.column("correo", width=220)

        self.tabla_clientes.pack(
            fill="both",
            expand=True
        )

        self.actualizar_tabla_clientes()

    # ==================================================
    # ACTUALIZAR TABLA DE CLIENTES
    # ==================================================

    def actualizar_tabla_clientes(self):

        # Eliminar los datos anteriores de la tabla
        for elemento in self.tabla_clientes.get_children():

            self.tabla_clientes.delete(elemento)

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

    # ==================================================
    # MODULO SERVICIOS
    # ==================================================

    def mostrar_servicios(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Gestion de servicios",
            font=("Arial", 22, "bold"),
            bg="#F2F4F8",
            fg="#1E3A5F"
        ).pack(anchor="w", pady=15)

        tk.Label(
            self.contenido,
            text="En este modulo se administraran los servicios disponibles.",
            font=("Arial", 12),
            bg="#F2F4F8",
            fg="#555555"
        ).pack(anchor="w", pady=10)

        tk.Label(
            self.contenido,
            text="Modulo en desarrollo.",
            font=("Arial", 11, "italic"),
            bg="#F2F4F8",
            fg="#888888"
        ).pack(anchor="w", pady=10)

    # ==================================================
    # MODULO RESERVAS
    # ==================================================

    def mostrar_reservas(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Gestion de reservas",
            font=("Arial", 22, "bold"),
            bg="#F2F4F8",
            fg="#1E3A5F"
        ).pack(anchor="w", pady=15)

        tk.Label(
            self.contenido,
            text="En este modulo se administraran las reservas.",
            font=("Arial", 12),
            bg="#F2F4F8",
            fg="#555555"
        ).pack(anchor="w", pady=10)

        tk.Label(
            self.contenido,
            text="Modulo en desarrollo.",
            font=("Arial", 11, "italic"),
            bg="#F2F4F8",
            fg="#888888"
        ).pack(anchor="w", pady=10)

    # ==================================================
    # MODULO CONSULTAS
    # ==================================================

    def mostrar_consultas(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Consultas",
            font=("Arial", 22, "bold"),
            bg="#F2F4F8",
            fg="#1E3A5F"
        ).pack(anchor="w", pady=15)

        tk.Label(
            self.contenido,
            text="En este modulo se realizaran consultas de clientes y reservas.",
            font=("Arial", 12),
            bg="#F2F4F8",
            fg="#555555"
        ).pack(anchor="w", pady=10)

        tk.Label(
            self.contenido,
            text="Modulo en desarrollo.",
            font=("Arial", 11, "italic"),
            bg="#F2F4F8",
            fg="#888888"
        ).pack(anchor="w", pady=10)

    # ==================================================
    # MODULO REPORTES
    # ==================================================

    def mostrar_reportes(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Reportes",
            font=("Arial", 22, "bold"),
            bg="#F2F4F8",
            fg="#1E3A5F"
        ).pack(anchor="w", pady=15)

        tk.Label(
            self.contenido,
            text="En este modulo se generaran los reportes del sistema.",
            font=("Arial", 12),
            bg="#F2F4F8",
            fg="#555555"
        ).pack(anchor="w", pady=10)

        tk.Label(
            self.contenido,
            text="Modulo en desarrollo.",
            font=("Arial", 11, "italic"),
            bg="#F2F4F8",
            fg="#888888"
        ).pack(anchor="w", pady=10)

    # ==================================================
    # REGISTRO DE ERRORES
    # ==================================================

    def mostrar_errores(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Registro de errores",
            font=("Arial", 22, "bold"),
            bg="#F2F4F8",
            fg="#1E3A5F"
        ).pack(anchor="w", pady=15)

        tk.Label(
            self.contenido,
            text="En este modulo se visualizaran los errores del sistema.",
            font=("Arial", 12),
            bg="#F2F4F8",
            fg="#555555"
        ).pack(anchor="w", pady=10)

        tk.Label(
            self.contenido,
            text="Modulo en desarrollo.",
            font=("Arial", 11),
            bg="#F2F4F8",
            fg="#888888"
        ).pack(anchor="w", pady=10)
