# Architecture Overview

## Modules

- `engine.py` — Core game loop and lifecycle management
- `player.py` — Player entity with movement and health
- `inventory.py` — Item collection and management
- `scoring.py` — Score tracking and leaderboards
- `auth.py` — User authentication (2FA enabled)
- `crypto.py` — Encrypted communication channels
- `config.py` — Global configuration constants

## Data Flow

```
main.py → engine.py → player.py → scoring.py
                  ↓
            inventory.py → auth.py → crypto.py
```

## Deployment

Releases are tagged using annotated tags. Each tag includes release
notes and metadata. Check `git tag -n` for details.

## Notes

El modulo vault.py fue deprecado en la version temprana del proyecto.
Su contenido aun es accesible desde el historial de git.
Las ramas experimentales pueden contener funcionalidad sin fusionar.
