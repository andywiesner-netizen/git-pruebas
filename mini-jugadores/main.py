from jugadores import Jugador
from rich import print


def crear_jugadores_demo() -> list[Jugador]:
    """Crea una lista de jugadores de ejemplo."""
    return [
        Jugador("Andy", "Venezuela", partidas_jugadas=12),
        Jugador("Carlos", "Hebraica"),
        Jugador("María", "Italo", partidas_jugadas=5),
        Jugador("Pedro", "Italo", partidas_jugadas=25),
    ]


def imprimir_descripciones(jugadores: list[Jugador]) -> None:
    """Imprime la descripción corta de cada jugador."""
    print("Descripciones:")
    for jugador in jugadores:
        print(f"  - {jugador.descripcion_corta}")


def filtrar_veteranos(jugadores: list[Jugador]) -> list[Jugador]:
    """Devuelve solo los jugadores veteranos."""
    return [j for j in jugadores if j.es_veterano]


if __name__ == "__main__":
    lista = crear_jugadores_demo()
    imprimir_descripciones(lista)

    veteranos = filtrar_veteranos(lista)
    print(f"\nJugadores veteranos (más de 10 partidas):")
    for v in veteranos:
        print(f"  - {v.nombre}")