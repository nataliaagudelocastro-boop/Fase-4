
# ==========================================
# SOFTWARE FJ
# CLASE CLIENTE
# ==========================================

import re


class Cliente:

    # Constructor de la clase
    def __init__(self, nombre, documento, telefono, correo):

        # Validar que los campos no estén vacíos
        if not nombre.strip():
            raise ValueError("El nombre es obligatorio.")

        if not documento.strip():
            raise ValueError("El documento es obligatorio.")

        if not telefono.strip():
            raise ValueError("El teléfono es obligatorio.")

        if not correo.strip():
            raise ValueError("El correo electrónico es obligatorio.")

        # Validar que documento y teléfono contengan números
        if not documento.isdigit():
            raise ValueError("El documento debe contener solo números.")

        if not telefono.isdigit():
            raise ValueError("El teléfono debe contener solo números.")

        # Validar formato básico del correo
        patron_correo = r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"

        if not re.match(patron_correo, correo):
            raise ValueError("El correo electrónico no es válido.")

        # Atributos encapsulados
        self.__nombre = nombre.strip()
        self.__documento = documento.strip()
        self.__telefono = telefono.strip()
        self.__correo = correo.strip()

    # Método para obtener los datos del cliente
    def obtener_datos(self):

        return {
            "nombre": self.__nombre,
            "documento": self.__documento,
            "telefono": self.__telefono,
            "correo": self.__correo
        }

    # Método para mostrar la información
    def __str__(self):

        return (
            f"Nombre: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Teléfono: {self.__telefono} | "
            f"Correo: {self.__correo}"
        )
