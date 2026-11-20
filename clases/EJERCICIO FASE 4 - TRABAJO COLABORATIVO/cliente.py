
# ==========================================
# SOFTWARE FJ
# CLASE CLIENTE
# ==========================================

import re


class Cliente:

    # Constructor de la clase
    def __init__(self, nombre, documento, telefono, correo):

        # Validar que los campos no esten vacios
        if not nombre.strip():
            raise ValueError("El nombre es obligatorio.")

        if not documento.strip():
            raise ValueError("El documento es obligatorio.")

        if not telefono.strip():
            raise ValueError("El telefono es obligatorio.")

        if not correo.strip():
            raise ValueError("El correo electronico es obligatorio.")

        # Validar que documento y telefono contengan numeros
        if not documento.isdigit():
            raise ValueError("El documento debe contener solo numeros.")

        if not telefono.isdigit():
            raise ValueError("El telefono debe contener solo numeros.")

        # Validar el formato del correo electronico
        patron_correo = r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"

        if not re.match(patron_correo, correo):
            raise ValueError("El correo electronico no es valido.")

        # Atributos privados (encapsulamiento)
        self.__nombre = nombre.strip()
        self.__documento = documento.strip()
        self.__telefono = telefono.strip()
        self.__correo = correo.strip()

    # Metodo para obtener los datos del cliente
    def obtener_datos(self):

        return {
            "nombre": self.__nombre,
            "documento": self.__documento,
            "telefono": self.__telefono,
            "correo": self.__correo
        }

    # Metodo para mostrar la informacion del cliente
    def __str__(self):

        return (
            f"Nombre: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Telefono: {self.__telefono} | "
            f"Correo: {self.__correo}"
        )
