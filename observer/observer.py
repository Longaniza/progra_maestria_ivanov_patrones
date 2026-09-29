from abc import ABC, abstractmethod
from typing import List

class IObservador(ABC):
    """Interfaz pura para los observadores."""

    @abstractmethod
    def actualizar(self, mensaje: str) -> None:
        """Método que el sujeto llamará para enviar la notificación."""
        pass


class ISujeto(ABC):
    """Interfaz pura que define el contrato que debe cumplir cualquier sujeto."""

    @abstractmethod
    def suscribir(self, observador: IObservador) -> None:
        pass

    @abstractmethod
    def desuscribir(self, observador: IObservador) -> None:
        pass

    @abstractmethod
    def notificar(self, mensaje: str) -> None:
        pass


class SujetoBase(ISujeto):
    """
    Clase base que implementa el contrato de ISujeto y gestiona
    la colección de observadores para evitar duplicar código.
    """

    def __init__(self) -> None:
        self._observadores: List[IObservador] = []

    def suscribir(self, observador: IObservador) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def desuscribir(self, observador: IObservador) -> None:
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar(self, mensaje: str) -> None:
        for observador in self._observadores:
            observador.actualizar(mensaje)


class CanalYouTube(SujetoBase):
    """Sujeto concreto de dominio."""

    def __init__(self, nombre: str) -> None:
        super().__init__()
        self.nombre = nombre

    def subir_video(self, titulo: str) -> None:
        print(f"\n🎬 [{self.nombre}] Ha publicado: '{titulo}'")
        self.notificar(f"Nuevo video en {self.nombre}: {titulo}")


class Usuario(IObservador):
    """Observador concreto de dominio."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def actualizar(self, mensaje: str) -> None:
        print(f"🔔 {self.nombre} recibió notificación: {mensaje}")
