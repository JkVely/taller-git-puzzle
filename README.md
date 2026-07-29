<div align="center">

```
  ____            _           _   ____  _                           _     
 |  _ \ _ __ ___ (_) ___  ___| |_|  _ \| |__   ___   ___  ___  ___| |__  
 | |_) | '__/ _ \| |/ _ \/ __| __| |_) | '_ \ / _ \ / _ \/ __|/ _ \ '_ \ 
 |  __/| | | (_) | |  __/ (__| |_|  __/| | | | (_) | (_) \__ \  __/ | | |
 |_|   |_|  \___// |\___|\___|\__|_|   |_| |_|\___/ \___/|___/\___|_| |_|
               |__/                                                       
```

# Project Phoenix

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-Flow-orange?style=flat&logo=git)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=flat)
![PRs](https://img.shields.io/badge/PRs-Welcome-blueviolet?style=flat)

**Prototipo colaborativo de videojuego** desarrollado como parte del curso de Git y CI/CD del [GLUD](https://github.com/GLUD) — Universidad Distrital.

</div>

---

## Descripcion

Project Phoenix es un motor de juego modular construido con fines educativos. El proyecto simula un flujo de desarrollo profesional con Git, incluyendo ramas por feature, revisiones de codigo, y despliegue automatizado.

### Arquitectura

```
src/main.py ───→ GameEngine ──→ Player
                     │
            ┌───────┴───────┐
            ↓               ↓
      ScoreBoard        Inventory
            ↓               ↓
      Authenticator    SecureChannel
```

## Requisitos

- Python 3.10+
- pip (gestor de paquetes)

```bash
pip install -r requirements.txt
```

## Inicio rapido

```bash
# Clonar
git clone https://github.com/JkVely/taller-git-puzzle.git
cd taller-git-puzzle

# Ejecutar
python src/main.py

# Probar
pytest tests/ -v
```

## Estructura del proyecto

```
.
├── .github/workflows/   # Pipelines de CI/CD
├── docs/                # Documentacion
│   └── ARCHITECTURE.md
├── src/                 # Codigo fuente
│   ├── main.py          # Punto de entrada
│   ├── engine.py        # Motor del juego
│   ├── player.py        # Sistema de jugador
│   ├── inventory.py     # Sistema de inventario
│   ├── scoring.py       # Sistema de puntuacion
│   ├── auth.py          # Autenticacion
│   ├── crypto.py        # Comunicaciones cifradas
│   └── config.py        # Configuracion
├── tests/               # Pruebas unitarias
│   └── test_engine.py
├── CHANGELOG.md         # Registro de versiones
├── Makefile             # Automatizacion de tareas
├── requirements.txt     # Dependencias
└── README.md            # Este archivo
```

## Convenciones del equipo

| Convencion | Estandar |
|------------|----------|
| Commits | Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `chore:`) |
| Ramas | Git Flow (`main`, `develop`, `feature/*`, `release/*`) |
| Revisiones | Code Review obligatorio via Pull Request |
| Versionado | Semantico via tags anotados |

## Creditos

**Juan Carlos Quintero Rubiano** — Desarrollo y mantenimiento

---

<div align="center">

*Proyecto academico sin fines de lucro — GLUD 2026*

</div>
