# Architecture Overview

## Modules

- `engine.py` — Core game loop
- `player.py` — Player entity
- `inventory.py` — Item system
- `vault.py` — Key management (deprecated)

## Fragment Storage

The three fragments of the activation key are stored using different
Git mechanisms. This is intentional — each mechanism corresponds to
a concept covered in the course.

### Known locations

- Fragment 1: stored in an early module (now removed from working tree)
- Fragment 2: exists only in an experimental branch (never merged)
- Fragment 3: marked in the release metadata (check the stars)

> *"The code is just a snapshot. The real story is in the history."*
