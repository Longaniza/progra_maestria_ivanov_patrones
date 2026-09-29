from __future__ import annotations
from datetime import datetime


class Documento:
    """
    Originador que encapsula su propia implementación de Recuerdo
    como una clase anidada/interna para proteger su estructura interna.
    """

    class _RecuerdoInterno:
        """
        Clase anidada privada. Solo Documento manipula directamente
        sus atributos de estado (_titulo, _contenido).
        """

        def __init__(self, titulo: str, contenido: str) -> None:
            self._titulo = titulo
            self._contenido = contenido
            self._fecha = str(datetime.now())[:19]

        def obtener_estado(self) -> tuple[str, str]:
            return self._titulo, self._contenido

        def obtener_nombre(self) -> str:
            vista_previa = self._contenido[:10] + "..." if len(self._contenido) > 10 else self._contenido
            return f"{self._fecha} / [{self._titulo}] ({vista_previa})"

        def obtener_fecha(self) -> str:
            return self._fecha

    def __init__(self, titulo: str, contenido: str) -> None:
        self._titulo = titulo
        self._contenido = contenido
        print(f"Documento: Estado inicial -> Título: '{self._titulo}', Contenido: '{self._contenido}'")

    def editar(self, titulo: str, contenido: str) -> None:
        """Modifica ambos estados simulando lógica de negocio."""
        self._titulo = titulo
        self._contenido = contenido
        print(f"Documento: Estado actualizado -> Título: '{self._titulo}', Contenido: '{self._contenido}'")

    def guardar(self) -> Documento._RecuerdoInterno:
        """Instancia la clase anidada empaquetando el estado actual."""
        return self._RecuerdoInterno(self._titulo, self._contenido)

    def restaurar(self, recuerdo: Documento._RecuerdoInterno) -> None:
        """Recupera los datos del recuerdo anidado."""
        if not isinstance(recuerdo, self._RecuerdoInterno):
            raise TypeError("El objeto proporcionado no es un recuerdo válido para este documento.")

        titulo, contenido = recuerdo.obtener_estado()
        self._titulo = titulo
        self._contenido = contenido
        print(f"Documento: Estado restaurado -> Título: '{self._titulo}', Contenido: '{self._contenido}'")


class Conserje:
    """
    El Conserje administra la colección de recuerdos sin conocer
    los detalles del estado interno que contienen.
    """

    def __init__(self, documento: Documento) -> None:
        self._recuerdos: list[Documento._RecuerdoInterno] = []
        self._documento = documento

    def respaldar(self) -> None:
        print("\nConserje: Guardando copia de respaldo...")
        self._recuerdos.append(self._documento.guardar())

    def deshacer(self) -> None:
        if not len(self._recuerdos):
            print("Conserje: No hay estados previos para restaurar.")
            return

        recuerdo = self._recuerdos.pop()
        print(f"Conserje: Restaurando hacia snapshot -> {recuerdo.obtener_nombre()}")
        try:
            self._documento.restaurar(recuerdo)
        except Exception:
            self.deshacer()

    def mostrar_historial(self) -> None:
        print("\nConserje: Historial de versiones guardadas:")
        for recuerdo in self._recuerdos:
            print(f"  - {recuerdo.obtener_nombre()}")