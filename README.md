# Extracteur de Données API

## Description
Ce projet est un script d'automatisation en Python conçu pour interroger une API distante, extraire des données brutes au format JSON, les nettoyer, et les structurer dans un format tabulaire exploitable (CSV). 

Il illustre de manière concrète les principes fondamentaux de l'ingénierie des données (ETL : Extract, Transform, Load) et la manipulation d'interfaces de programmation applicative.

## Technologies & Bibliothèques
- Langage : Python 3
- Requêtes HTTP :`requests` (Connexion et récupération des flux JSON)
- Traitement de données : `pandas` (Nettoyage, formatage et export)

## Fonctionnalités du Pipeline
1. Extract : Connexion sécurisée à une API publique (gestion des codes statuts HTTP 200) et extraction des flux de données brutes.
2. Transform : Nettoyage dynamique des données avec `pandas`. Filtrage des colonnes pertinentes, renommage, et extraction d'éléments imbriqués (listes) via des fonctions `lambda`.
3. Load : Exportation automatisée du jeu de données finalisé vers un fichier `.csv` structuré (encodage UTF-8 avec signature et séparateurs configurés pour une compatibilité native avec Excel).

## Installation et Utilisation

1. Installer les dépendances :
Assurez-vous d'avoir installé Python, puis exécutez la commande suivante dans votre terminal :
`pip install requests pandas`

2. Lancer l'extraction :
Exécutez le script principal depuis votre invite de commande :
`python extracteur_api.py`

3. Résultat :
Le script générera automatiquement un fichier `donnees_universites.csv` dans le répertoire courant, contenant les données nettoyées et prêtes à être analysées.
