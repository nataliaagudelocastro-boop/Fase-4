import tkinter as tk
from tkinter import ttk, messagebox
from sistema_gestion import SistemaGestion, ErrorDominio


class VistaReservas(ttk.Frame):
    def __init__(self, parent, sistema: SistemaGestion, on_error_callback=None):
        super().__init__(parent, padding=20)
        self.sistema = sistema
        self.on_error_callback = on_error_callback
        self._construir_ui()
        self.refrescar_datos()

    def _construir_ui(self):
        ttk.Label(self, text="Gestión de reservas", font=("Segoe UI", 18, "bold")).pack(anchor="w", pady=(0, 15))

        form = ttk.Frame(self)
        form.pack(fill="x", pady=(0, 15))

        ttk.Label(form, text="Cliente (Documento):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.combo_cliente = ttk.Combobox(form, width=32)
        self.combo_cliente.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(form, text="Servicio (Código):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.combo_servicio = ttk.Combobox(form, width=32)
        self.combo_servicio.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(form, text="Fecha y hora:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_fecha = ttk.Entry(form, width=35)
        self.entry_fecha.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        btn_registrar = ttk.Button(form, text="Registrar reserva", command=self._registrar_reserva)
        btn_registrar.grid(row=3, column=1, sticky="e", padx=5, pady=10)

        columnas = ("cliente", "documento", "servicio", "fecha_hora", "estado")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=8)
        for col, texto in zip(columnas, ["Cliente", "Documento", "Servicio", "Fecha y hora", "Estado"]):
            self.tabla.heading(col, text=texto)
            self.tabla.column(col, width=150, anchor="w")
        self.tabla.pack(fill="both", expand=True)

    def refrescar_datos(self):
        self.combo_cliente["values"] = [
            f"{doc} - {cli.nombre}" for doc, cli in self.sistema.clientes.items()
        ]
        self.combo_servicio["values"] = [
            f"{cod} - {srv.nombre}" for cod, srv in self.sistema.servicios.items()
        ]

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for r in self.sistema.reservas:
            self.tabla.insert(
                "",
                "end",
                values=(r.cliente.nombre, r.cliente.documento, r.servicio.nombre, r.fecha_hora, r.estado),
            )

    def _registrar_reserva(self):
        # Extrae el documento o código antes del " - " si viene del Combobox, o usa lo escrito a mano
        raw_cliente = self.combo_cliente.get().split(" - ")[0].strip()
        raw_servicio = self.combo_servicio.get().split(" - ")[0].strip()
        fecha_hora = self.entry_fecha.get()

        try:
            self.sistema.crear_reserva(raw_cliente, raw_servicio, fecha_hora)
            self.entry_fecha.delete(0, "end")
            self.refrescar_datos()
            messagebox.showinfo("Reserva exitosa", "La reserva se registró correctamente.")
        except ErrorDominio as exc:
            if self.on_error_callback:
                self.on_error_callback()
            messagebox.showwarning("Error controlado en reserva", str(exc))