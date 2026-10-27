"""Utilidad de saludo para nombres arbitrarios."""


def greet(name: str) -> str:
    """Genera un saludo a partir del nombre recibido.

    Elimina los espacios iniciales y finales del nombre. Si el valor
    resultante queda vacío, se usa ``World`` como nombre por defecto.

    Args:
        name: Nombre al que dirigir el saludo.

    Returns:
        ``"Hello, <nombre>!"`` o ``"Hello, World!"`` si el nombre queda vacío.
    """
    stripped_name = name.strip()
    if not stripped_name:
        return "Hello, World!"
    return f"Hello, {stripped_name}!"
