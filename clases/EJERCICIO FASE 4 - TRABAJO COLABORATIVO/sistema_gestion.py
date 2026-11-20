from datetime import datetime


class ErrorDominio(Exception):
    """Excepción base controlada para reglas del sistema."""


class ValidacionError(ErrorDominio):
    """Error por datos inválidos o campos incompletos."""


class EntidadNoEncontradaError(ErrorDominio):
    """Error cuando no existe un cliente o servicio."""


class ConflictoReservaError(ErrorDominio):
    """Error por regla de negocio (ej. horario ocupado o cupo lleno)."""


class Cliente:
    def __init__(self, nombre: str, documento: str, telefono: str, correo: str):
        nombre = nombre.strip()
        documento = documento.strip()
        telefono = telefono.strip()
        correo = correo.strip()

        if not nombre or not documento or not telefono or not correo:
            raise ValidacionError("Todos los campos del cliente son obligatorios.")
        if not documento.isdigit():
            raise ValidacionError("El documento debe contener solo números.")
        if not telefono.isdigit() or len(telefono) < 7:
            raise ValidacionError("El teléfono debe ser numérico y tener al menos 7 dígitos.")
        if "@" not in correo or "." not in correo.split("@")[-1]:
            raise ValidacionError("El correo electrónico no tiene un formato válido.")

        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono
        self.correo = correo


class Servicio:
    def __init__(self, codigo: str, nombre: str, precio: float, cupo_maximo: int = 1):
        codigo = codigo.strip().upper()
        nombre = nombre.strip()

        if not codigo or not nombre:
            raise ValidacionError("El código y el nombre del servicio son obligatorios.")
        if precio <= 0:
            raise ValidacionError("El precio del servicio debe ser mayor que cero.")
        if cupo_maximo <= 0:
            raise ValidacionError("El cupo máximo debe ser mayor que cero.")

        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)
        self.cupo_maximo = int(cupo_maximo)


class Reserva:
    def __init__(self, cliente: Cliente, servicio: Servicio, fecha_hora: str):
        fecha_hora = fecha_hora.strip()
        if not fecha_hora:
            raise ValidacionError("La fecha y hora de la reserva son obligatorias.")

        self.cliente = cliente
        self.servicio = servicio
        self.fecha_hora = fecha_hora
        self.estado = "Confirmada"


class SistemaGestion:
    """Almacena todo en memoria (listas/diccionarios) sin base de datos."""

    def __init__(self):
        self.clientes: dict[str, Cliente] = {}
        self.servicios: dict[str, Servicio] = {}
        self.reservas: list[Reserva] = []
        self.errores: list[dict] = []

    def registrar_error(self, modulo: str, mensaje: str):
        self.errores.append({
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "modulo": modulo,
            "mensaje": mensaje,
        })

    def registrar_cliente(self, nombre: str, documento: str, telefono: str, correo: str) -> Cliente:
        try:
            cliente = Cliente(nombre, documento, telefono, correo)
            if cliente.documento in self.clientes:
                raise ValidacionError(f"Ya existe un cliente con documento {cliente.documento}.")
            self.clientes[cliente.documento] = cliente
            return cliente
        except ErrorDominio as exc:
            self.registrar_error("Clientes", str(exc))
            raise

    def crear_servicio(self, codigo: str, nombre: str, precio_texto: str, cupo_texto: str = "1") -> Servicio:
        try:
            try:
                precio = float(precio_texto)
                cupo = int(cupo_texto)
            except ValueError as exc:
                raise ValidacionError("Precio y cupo deben ser valores numéricos válidos.") from exc

            servicio = Servicio(codigo, nombre, precio, cupo)
            if servicio.codigo in self.servicios:
                raise ValidacionError(f"Ya existe un servicio con el código {servicio.codigo}.")
            self.servicios[servicio.codigo] = servicio
            return servicio
        except ErrorDominio as exc:
            self.registrar_error("Servicios", str(exc))
            raise

    def crear_reserva(self, documento_cliente: str, codigo_servicio: str, fecha_hora: str) -> Reserva:
        try:
            doc = documento_cliente.strip()
            cod = codigo_servicio.strip().upper()

            if not doc or not cod:
                raise ValidacionError("Debes seleccionar o indicar cliente y servicio.")
            if doc not in self.clientes:
                raise EntidadNoEncontradaError(f"No existe un cliente con documento '{doc}'.")
            if cod not in self.servicios:
                raise EntidadNoEncontradaError(f"No existe un servicio con código '{cod}'.")

            servicio = self.servicios[cod]
            cliente = self.clientes[doc]

            # Regla de negocio: verificar cupo o conflicto en misma fecha/hora para el servicio
            reservas_mismo_horario = [
                r for r in self.reservas
                if r.servicio.codigo == cod and r.fecha_hora == fecha_hora.strip()
            ]
            if len(reservas_mismo_horario) >= servicio.cupo_maximo:
                raise ConflictoReservaError(
                    f"Sin disponibilidad para '{servicio.nombre}' en '{fecha_hora.strip()}'."
                )

            reserva = Reserva(cliente, servicio, fecha_hora)
            self.reservas.append(reserva)
            return reserva
        except ErrorDominio as exc:
            self.registrar_error("Reservas", str(exc))
            raise