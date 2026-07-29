# Project Phoenix

Prototipo colaborativo de videojuego desarrollado como parte del curso de Git y CI/CD del **GLUD — Universidad Distrital**.

## Requisitos

- Python 3.10+
- pytest (opcional, para pruebas)

```
pip install -r requirements.txt
```

## Cómo ejecutar

```bash
python src/main.py
```

## Cómo probar

```bash
pytest tests/
```

## Estructura del proyecto

```
src/
  main.py        — Punto de entrada
  engine.py      — Motor del juego
  player.py      — Sistema de jugador
  inventory.py   — Sistema de inventario
  scoring.py     — Sistema de puntuación
  auth.py        — Autenticación
  crypto.py      — Comunicaciones cifradas
  config.py      — Configuración
docs/
  ARCHITECTURE.md — Documentación de arquitectura
tests/
  test_engine.py — Pruebas unitarias
```

## Convenciones

- **Conventional Commits**: feat, fix, docs, test, chore, refactor
- **Git Flow**: main, develop, feature/*, release/*
- **Code Review**: Toda fusión requiere revisión

## Créditos

| Rol | Persona |
|-----|---------|
| Tech Lead | Ana María López |
| Backend | Carlos Ruiz |
| Gameplay | Valentina Ortiz |
| QA | Diego Torres |
| Documentación | Sofía Herrera |

---

*Proyecto académico sin fines de lucro. GLUD 2026.*
