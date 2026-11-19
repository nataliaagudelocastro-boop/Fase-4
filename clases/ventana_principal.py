import tkinter as tk
from tkinter import ttk, messagebox

from sistema_gestion import SistemaGestion, ErrorDominio
from vista_reservas import VistaReservas


class VentanaPrincipal:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Software FJ - Gestion de Servicios y Clientes")
        self.ventana.geometry("1100x700")
        self.ventana.minsize(900, 600)
        self.ventana.configure(bg="#F2F4F8")

        # Gestor único en memoria (sin base de datos)
        self.sistema = SistemaGestion()
        self.registro_inicial = True

        self.configurar_estilos()

        self.menu = tk.Frame(self.ventana, bg="#1E3A5F", width=220)
        self.menu.pack(side="left", fill="y")
        self.menu.pack_propagate(False)

        self.contenedor_principal = tk.Frame(self.ventana, bg="#F2F4F8")
        self.contenedor_principal.pack(side="right", fill="both", expand=True)

        self.encabezado = tk.Frame(self.contenedor_principal, bg="#FFFFFF", height=70)
        self.encabezado.pack(fill="x")
        self.encabezado.pack_propagate(False)

        tk.Label(
            self.encabezado,
            text="SOFTWARE FJ",
            font=("Arial", 18, "bold"),
            bg="#FFFFFF",
            fg="#1E3A5F",
        ).pack(side="left", padx=25, pady=18)

        self.contenido = tk.Frame(self.contenedor_principal, bg="#F2F4F8")
        self.contenido.pack(fill="both", expand=True, padx=20, pady=20)

        self.crear_menu()
        self.mostrar_registro_inicial()

    def configurar_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "Treeview",
            background="#FFFFFF",
            foreground="#333333",
            rowheight=28,
            fieldbackground="#FFFFFF",
            font=("Arial", 10),
        )
        estilo.configure(
            "Treeview.Heading",
            background="#1E3A5F",
            foreground="white",
            font=("Arial", 10, "bold"),
        )
        estilo.map(
            "Treeview",
            background=[("selected", "#D4AF37")],
            foreground=[("selected", "#1E3A5F")],
        )

    def crear_menu(self):
        tk.Label(
            self.menu,
            text="SOFTWARE FJ",
            font=("Arial", 17, "bold"),
            bg="#1E3A5F",
            fg="white",
        ).pack(pady=30)

        opciones = [
            ("Inicio", self.mostrar_inicio),
            ("Clientes", self.mostrar_clientes),
            ("Servicios", self.mostrar_servicios),
            ("Reservas", self.mostrar_reservas),
            ("Consultas", self.mostrar_consultas),
            ("Reportes", self.mostrar_reportes),
            ("Registro de errores", self.mostrar_errores),
        ]

        for texto, comando in opciones:
            tk.Button(
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
                command=comando,
            ).pack(fill="x", padx=8, pady=3)

    def limpiar_contenido(self):
        for elemento in self.contenido.winfo_children():
            elemento.destroy()

    def mostrar_registro_inicial(self):
        self.limpiar_contenido()
        self.menu.pack_forget()

        tk.Label(
            self.contenido,
            text="Bienvenido a Software FJ",
            font=("Arial", 24, "bold"),
            bg="#F2F4F8",
            fg="#1E3A5F",
        ).pack(pady=(20, 5))

        tk.Label(
            self.contenido,
            text="Para comenzar, registra tus datos personales",
            font=("Arial", 12),
            bg="#F2F4F8",
            fg="#555555",
        ).pack(pady=5)

        formulario = tk.Frame(self.contenido, bg="white", padx=40, pady=20)
        formulario.pack(fill="x", padx=80, pady=15)

        self.nombre_inicial = tk.StringVar()
        self.documento_inicial = tk.StringVar()
        self.telefono_inicial = tk.StringVar()
        self.correo_inicial = tk.StringVar()

        campos = [
            ("Nombre completo:", self.nombre_inicial),
            ("Documento:", self.documento_inicial),
            ("Telefono:", self.telefono_inicial),
            ("Correo electronico:", self.correo_inicial),
        ]

        for texto, variable in campos:
            tk.Label(
                formulario, text=texto, font=("Arial", 11, "bold"), bg="white", fg="#1E3A5F"
            ).pack(anchor="w", pady=(8, 3))
            tk.Entry(
                formulario, textvariable=variable, font=("Arial", 11), width=40, relief="solid", bd=1
            ).pack(fill="x", ipady=6, pady=3)

        tk.Button(
            formulario,
            text="REGISTRAR Y CONTINUAR",
            font=("Arial", 12, "bold"),
            bg="#1E3A5F",
            fg="white",
            activebackground="#D4AF37",
            activeforeground="#1E3A5F",
            relief="flat",
            cursor="hand2",
            command=self.registrar_cliente,
        ).pack(fill="x", pady=(20, 5), ipady=10)

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

            self.sistema.registrar_cliente(nombre, documento, telefono, correo)

            if self.registro_inicial:
                self.registro_inicial = False
                messagebox.showinfo("Registro exitoso", "Tus datos fueron registrados correctamente.")
                self.mostrar_menu_principal()
            else:
                self.actualizar_tabla_clientes()
                self.nombre_cliente.set("")
                self.documento_cliente.set("")
                self.telefono_cliente.set("")
                self.correo_cliente.set("")
                messagebox.showinfo("Registro exitoso", "El cliente fue registrado correctamente.")

        except ErrorDominio as error:
            messagebox.showerror("Error de validacion", str(error))
        except Exception as error:
            self.sistema.registrar_error("Clientes", f"Error inesperado: {error}")
            messagebox.showerror("Error inesperado", f"Ocurrio un error: {error}")

    def mostrar_menu_principal(self):
        self.menu.pack(side="left", fill="y", before=self.contenedor_principal)
        self.mostrar_inicio()

    def mostrar_inicio(self):
        self.limpiar_contenido()
        tk.Label(
            self.contenido, text="Panel principal", font=("Arial", 23, "bold"), bg="#F2F4F8", fg="#1E3A5F"
        ).pack(anchor="w", pady=15)

        panel = tk.Frame(self.contenido, bg="white", padx=25, pady=25)
        panel.pack(fill="x", pady=15)

        resumen = (
            f"Clientes: {len(self.sistema.clientes)}   |   "
            f"Servicios: {len(self.sistema.servicios)}   |   "
            f"Reservas: {len(self.sistema.reservas)}   |   "
            f"Errores registrados: {len(self.sistema.errores)}"
        )
        tk.Label(panel, text="RESUMEN EN MEMORIA", font=("Arial", 12, "bold"), bg="white", fg="#1E3A5F").pack(anchor="w")
        tk.Label(panel, text=resumen, font=("Arial", 14, "bold"), bg="white", fg="#D4AF37").pack(anchor="w", pady=10)

    def mostrar_clientes(self):
        self.limpiar_contenido()
        tk.Label(
            self.contenido, text="Gestion de clientes", font=("Arial", 22, "bold"), bg="#F2F4F8", fg="#1E3A5F"
        ).pack(anchor="w", pady=10)

        formulario = tk.Frame(self.contenido, bg="white", padx=20, pady=15)
        formulario.pack(fill="x", pady=10)

        self.nombre_cliente = tk.StringVar()
        self.documento_cliente = tk.StringVar()
        self.telefono_cliente = tk.StringVar()
        self.correo_cliente = tk.StringVar()

        for texto, variable in [
            ("Nombre:", self.nombre_cliente),
            ("Documento:", self.documento_cliente),
            ("Telefono:", self.telefono_cliente),
            ("Correo:", self.correo_cliente),
        ]:
            fila = tk.Frame(formulario, bg="white")
            fila.pack(fill="x", pady=5)
            tk.Label(fila, text=texto, font=("Arial", 10, "bold"), bg="white", fg="#1E3A5F", width=15, anchor="w").pack(side="left")
            tk.Entry(fila, textvariable=variable, font=("Arial", 10), width=40).pack(side="left", ipady=4)

        tk.Button(
            formulario,
            text="Registrar cliente",
            font=("Arial", 10, "bold"),
            bg="#1E3A5F",
            fg="white",
            activebackground="#D4AF37",
            activeforeground="#1E3A5F",
            relief="flat",
            cursor="hand2",
            command=self.registrar_cliente,
        ).pack(anchor="e", pady=12, ipadx=10, ipady=5)

        tabla_frame = tk.Frame(self.contenido, bg="white", padx=10, pady=10)
        tabla_frame.pack(fill="both", expand=True, pady=10)

        columnas = ("nombre", "documento", "telefono", "correo")
        self.tabla_clientes = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
        for col, tit in zip(columnas, ["Nombre", "Documento", "Telefono", "Correo electronico"]):
            self.tabla_clientes.heading(col, text=tit)
            self.tabla_clientes.column(col, width=160, anchor="w")
        self.tabla_clientes.pack(fill="both", expand=True)
        self.actualizar_tabla_clientes()

    def actualizar_tabla_clientes(self):
        for elemento in self.tabla_clientes.get_children():
            self.tabla_clientes.delete(elemento)
        for cli in self.sistema.clientes.values():
            self.tabla_clientes.insert("", "end", values=(cli.nombre, cli.documento, cli.telefono, cli.correo))

    def mostrar_servicios(self):
        self.limpiar_contenido()
        tk.Label(
            self.contenido, text="Gestion de servicios", font=("Arial", 22, "bold"), bg="#F2F4F8", fg="#1E3A5F"
        ).pack(anchor="w", pady=10)

        form = tk.Frame(self.contenido, bg="white", padx=20, pady=15)
        form.pack(fill="x", pady=10)

        self.cod_servicio = tk.StringVar()
        self.nom_servicio = tk.StringVar()
        self.precio_servicio = tk.StringVar()
        self.cupo_servicio = tk.StringVar(value="1")

        for texto, var in [
            ("Codigo:", self.cod_servicio),
            ("Nombre:", self.nom_servicio),
            ("Precio:", self.precio_servicio),
            ("Cupo maximo:", self.cupo_servicio),
        ]:
            fila = tk.Frame(form, bg="white")
            fila.pack(fill="x", pady=4)
            tk.Label(fila, text=texto, font=("Arial", 10, "bold"), bg="white", fg="#1E3A5F", width=15, anchor="w").pack(side="left")
            tk.Entry(fila, textvariable=var, font=("Arial", 10), width=35).pack(side="left", ipady=4)

        def guardar_servicio():
            try:
                self.sistema.crear_servicio(
                    self.cod_servicio.get(),
                    self.nom_servicio.get(),
                    self.precio_servicio.get(),
                    self.cupo_servicio.get(),
                )
                self.cod_servicio.set("")
                self.nom_servicio.set("")
                self.precio_servicio.set("")
                self.cupo_servicio.set("1")
                refrescar_servicios()
                messagebox.showinfo("Servicio creado", "El servicio se registró correctamente.")
            except ErrorDominio as exc:
                messagebox.showerror("Error en servicio", str(exc))

        tk.Button(
            form,
            text="Crear servicio",
            font=("Arial", 10, "bold"),
            bg="#1E3A5F",
            fg="white",
            activebackground="#D4AF37",
            activeforeground="#1E3A5F",
            relief="flat",
            cursor="hand2",
            command=guardar_servicio,
        ).pack(anchor="e", pady=10, ipadx=10, ipady=5)

        cols = ("codigo", "nombre", "precio", "cupo")
        tabla = ttk.Treeview(self.contenido, columns=cols, show="headings", height=7)
        for col, tit in zip(cols, ["Codigo", "Nombre", "Precio", "Cupo maximo"]):
            tabla.heading(col, text=tit)
            tabla.column(col, width=150, anchor="w")
        tabla.pack(fill="both", expand=True)

        def refrescar_servicios():
            for item in tabla.get_children():
                tabla.delete(item)
            for srv in self.sistema.servicios.values():
                tabla.insert("", "end", values=(srv.codigo, srv.nombre, f"{srv.precio:.2f}", srv.cupo_maximo))

        refrescar_servicios()

    def mostrar_reservas(self):
        self.limpiar_contenido()
        vista = VistaReservas(self.contenido, self.sistema)
        vista.pack(fill="both", expand=True)

    def mostrar_consultas(self):
        self.limpiar_contenido()
        tk.Label(
            self.contenido, text="Consultas", font=("Arial", 22, "bold"), bg="#F2F4F8", fg="#1E3A5F"
        ).pack(anchor="w", pady=10)

        resumen = tk.Text(self.contenido, height=22, font=("Consolas", 10), bg="white", padx=15, pady=15)
        resumen.pack(fill="both", expand=True)

        lineas = ["=== CLIENTES ==="]
        for cli in self.sistema.clientes.values():
            lineas.append(f"- {cli.documento} | {cli.nombre} | {cli.telefono} | {cli.correo}")

        lineas.append("\n=== SERVICIOS ===")
        for srv in self.sistema.servicios.values():
            lineas.append(f"- {srv.codigo} | {srv.nombre} | ${srv.precio:.2f} | Cupo: {srv.cupo_maximo}")

        lineas.append("\n=== RESERVAS ===")
        for r in self.sistema.reservas:
            lineas.append(f"- {r.cliente.documento} ({r.cliente.nombre}) -> {r.servicio.codigo} ({r.servicio.nombre}) | {r.fecha_hora} | {r.estado}")

        resumen.insert("1.0", "\n".join(lineas))
        resumen.configure(state="disabled")

    def mostrar_reportes(self):
        self.limpiar_contenido()
        tk.Label(
            self.contenido, text="Reportes", font=("Arial", 22, "bold"), bg="#F2F4F8", fg="#1E3A5F"
        ).pack(anchor="w", pady=10)

        panel = tk.Frame(self.contenido, bg="white", padx=25, pady=25)
        panel.pack(fill="x", pady=10)

        total_ingresos = sum(r.servicio.precio for r in self.sistema.reservas)
        datos = [
            f"Total de clientes registrados: {len(self.sistema.clientes)}",
            f"Total de servicios creados: {len(self.sistema.servicios)}",
            f"Total de reservas confirmadas: {len(self.sistema.reservas)}",
            f"Total de errores controlados: {len(self.sistema.errores)}",
            f"Monto estimado en reservas: ${total_ingresos:.2f}",
        ]
        for d in datos:
            tk.Label(panel, text=d, font=("Arial", 12, "bold"), bg="white", fg="#1E3A5F").pack(anchor="w", pady=5)

    def mostrar_errores(self):
        self.limpiar_contenido()
        tk.Label(
            self.contenido, text="Registro de errores", font=("Arial", 22, "bold"), bg="#F2F4F8", fg="#1E3A5F"
        ).pack(anchor="w", pady=10)

        cols = ("fecha", "modulo", "mensaje")
        tabla = ttk.Treeview(self.contenido, columns=cols, show="headings", height=14)
        for col, tit, w in zip(cols, ["Fecha", "Modulo", "Mensaje"], [170, 130, 500]):
            tabla.heading(col, text=tit)
            tabla.column(col, width=w, anchor="w")
        tabla.pack(fill="both", expand=True)

        for err in self.sistema.errores:
            tabla.insert("", "end", values=(err["fecha"], err["modulo"], err["mensaje"]))