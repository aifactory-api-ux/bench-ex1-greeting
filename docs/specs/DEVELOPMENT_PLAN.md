# DEVELOPMENT PLAN: bench-ex1-greeting

## 1. ARCHITECTURE OVERVIEW

- Utilidad local y síncrona escrita en Python 3.11, sin dependencias de terceros.
- `src.greeting` será el único módulo de producción y exportará exclusivamente `greet(name: str) -> str`.
- La función aplicará `strip()`, devolverá `"Hello, World!"` para valores vacíos y `"Hello, <nombre>!"` para valores no vacíos.
- `tests/test_greeting.py` contendrá una clase `unittest.TestCase` llamada `TestGreeting` con exactamente los métodos `test_normal_name`, `test_name_with_spaces` y `test_empty_string`.
- `README.md` documentará la invocación de la función y la ejecución de las pruebas con `python -m unittest discover tests`.
- No existirán modelos persistentes, endpoints HTTP, base de datos, variables de entorno, servicios, contenedores, frontend ni infraestructura adicional.
- La estructura final será:

```text
.
├── README.md
├── src/
│   └── greeting.py
└── tests/
    └── test_greeting.py
```

Los comentarios eventuales y los mensajes de commit deberán redactarse en español neutro.

## 2. ACCEPTANCE CRITERIA

1. `from src.greeting import greet` permite importar la función y `greet(" Alice ")` devuelve exactamente `"Hello, Alice!"`, mientras que `greet("")` devuelve exactamente `"Hello, World!"`.
2. `python -m unittest discover tests` finaliza correctamente y ejecuta exactamente las tres pruebas especificadas en `TestGreeting`.
3. `README.md` incluye literalmente el comando de invocación de la función y `python -m unittest discover tests`, sin introducir dependencias, endpoints ni archivos de infraestructura no especificados.

## TEAM SCOPE (MANDATORY — PARSED BY THE PIPELINE)

- role-be: Implementación de la función pública y de sus pruebas unitarias.
- role-doc: Documentación breve de ejecución local.

## 3. EXECUTABLE ITEMS

### ITEM 1: Foundation — greet(name: str) y pruebas unitarias
**Goal:** Crear la única función pública del proyecto, `greet(name: str) -> str`, aplicando exactamente el algoritmo de `strip()`, fallback a `"World"` y formato de saludo. Crear sus tres pruebas unitarias con los nombres, entradas y resultados exigidos por la especificación.
**Files to create:**
- `src/greeting.py` (create) - Definir a nivel de módulo exclusivamente `greet(name: str) -> str`, sin imports, efectos secundarios, punto de entrada ni与其他 exportaciones.
- `tests/test_greeting.py` (create) - Contener `import unittest`, `from src.greeting import greet` y la clase `TestGreeting` con exactamente `test_normal_name`, `test_name_with_spaces` y `test_empty_string`, usando las aserciones especificadas.
**Dependencies:** None
**Validation:** Ejecutar `python -m unittest discover tests` desde la raíz y comprobar que pasan las tres pruebas. Verificar además mediante `python -c "from src.greeting import greet; print(greet(' Alice '))"` que la salida es `Hello, Alice!`.
**Role:** role-be (backend_developer)

### ITEM 2: Infrastructure & Deployment — ejecución local documentada
**Goal:** Crear el README breve con la descripción de la utilidad, el comando de invocación de `greet` y el comando de ejecución de las pruebas. Como la especificación prohíbe servicios, despliegue, contenedores y archivos adicionales, esta/item de infraestructura se limita al único artefacto permitido: `README.md`.
**Files to create:**
- `README.md` (create) - Incluir la instrucción literal `python -c "from src.greeting import greet; print(greet(' Alice '))"` y `python -m unittest discover tests`, indicando que ambos comandos se ejecutan desde la raíz del repositorio.
**Dependencies:** Item 1
**Validation:** Comprobar que `README.md` contiene literalmente ambos comandos y ejecutar `python -m unittest discover tests` desde la raíz, confirmando que las tres pruebas finalizan correctamente.
**Role:** role-doc (documentation_writer)