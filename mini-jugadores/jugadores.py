class Jugador:
    def __init__(self, nombre: str, equipo: str, partidas_jugadas: int = 0):
        self.nombre: str = nombre
        self.equipo: str = equipo
        self.partidas_jugadas: int = partidas_jugadas

    @property
    def es_veterano(self) -> bool:
        """Devuelve True si el jugador tiene más de 10 partidas."""
        return self.partidas_jugadas > 10

    @property
    def descripcion_corta(self) -> str:
        """Devuelve una descripción corta del jugador."""
        estado = "veterano" if self.es_veterano else "novato"
        return f"{self.nombre} ({self.equipo}) - {estado}"

    def __repr__(self) -> str:
        return f"Jugador({self.nombre}, equipo={self.equipo}, partidas={self.partidas_jugadas})"