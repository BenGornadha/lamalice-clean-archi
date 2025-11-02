# Clean Architecture Python Example

Ce projet est un exemple d'implémentation de Clean Architecture en Python, comprenant l'injection de dépendances.

## Structure du Projet

```
.
├── application/          # Cas d'utilisation de l'application
├── domain/              # Règles métier et entités
├── infrastructures/     # Implémentations concrètes
└── interfaces/          # Interfaces et contrats
```

## Fonctionnalités

- Enregistrement d'utilisateur avec validation
- Gestion des emails comme value objects
- Persistence avec repository pattern
- Injection de dépendances avec dependency-injector

## Installation

1. Cloner le repository
```bash
git clone [URL_DU_REPO]
cd clean-archi
```

2. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Utilisation

Vous pouvez exécuter l'application de deux façons :

1. Version standard :
```bash
python main.py
```

2. Version avec injection de dépendances :
```bash
python main_injection_dependances.py
```

## Architecture

Ce projet suit les principes de Clean Architecture :
- Indépendance des frameworks
- Testabilité
- Indépendance de l'UI
- Indépendance de la base de données
- Indépendance de toute agence externe
