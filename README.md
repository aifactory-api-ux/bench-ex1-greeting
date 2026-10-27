# Aplicación de ejemplo

Utilidad Python pequeña y autónoma que genera saludos a partir de un nombre.

La función `greet(name: str) -> str` elimina los espacios iniciales y finales del
nombre recibido. Si el valor resultante queda vacío, usa `World` como nombre por
defecto; en caso contrario devuelve `Hello, <nombre>!`.

No requiere dependencias de terceros: solo la biblioteca estándar de Python 3.11.

## Estructura

```text
.
├── README.md
├── src/
│   └── greeting.py
└── tests/
    └── test_greeting.py
```

## Uso

Los comandos siguientes se ejecutan desde la raíz del repositorio.

Invocar la función directamente:

```bash
python -c "from src.greeting import greet; print(greet(' Alice '))"
```

Salida esperada:

```text
Hello, Alice!
```

También puede importarse desde el propio código:

```python
from src.greeting import greet

resultado = greet(" Alice ")
```

## Pruebas

Suite de pruebas con `unittest` (biblioteca estándar, sin dependencias adicionales):

```bash
python -m unittest discover tests
```

Como alternativa, si `pytest` está disponible en el entorno:

```bash
python -m pytest
```

Las pruebas cubren un nombre normal, un nombre con espacios y una cadena vacía.
