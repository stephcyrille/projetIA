# Projet IA: Outil de détection de fake news

Ce projet à pour but de mettre en place un outil de détection de fake news en utilisant la puissance des transformers qu'offre le modèle BERT. Il est structuré comme suit:<br>

    ├── scrapping/                      # Repertoire de scrapping de META données
    │   ├── data/                       # Notebook conténant les fichiers CSV générés par Scrapping
    │   ├── notebooks/                  # Notebook de scrapping
    │   └── src/                        # Script développés
    ├── fake_news_detector/             # Repertoire de construction du modèle 
    │   └── analysis/                   # Notebooks analyse
    │   └── data_prep/                  # Notebooks préparation des données
    │   └── modelisation/               # Notebooks de modélisation    
    ├── LICENCE                         # Licence utilisé
    ├── requirements.txt                # Dépendances du projet
    └── README.md                       # Project README file

## Etapes de traitements
- ### Etape 1: La Data preparation
  Dans cette étapes l'on procèdes a la lecture, traitement des différents Datasets puis à leur fusion en un jeu de données comportant toutes les carractéristiques necessaire au traitements suivants.<br>
  Tous les notebooks de cette étape sont dans le dossier ```fake_news_detector/data_prep/```

- ### Etape 2: Analyse:
  Tous les notebooks de cette étape sont dans le dossier ```fake_news_detector/analysis/```

- ### Etape 4: Modélisation 
    Tous les notebooks de cette étape sont dans le dossier ```fake_news_detector/modelisation/```

