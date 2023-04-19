# GBM3100-Projet
# Outil de classification du mouvement du bras à partir de signaux électromyographiques (EMG)

## Mise en contexte 
Plusieurs conditions médicales causent une atrophie, dystrophie ou faiblesse musculaire des membres supérieurs, nécessitant le recours à des prothèses, des exosquelettes, des bras robotiques, etc.LE contrôle de ces robots est assez complexe et nécessite des données biologiques en temps réel de l’usager, les signaux électromyographiques (EMG) sont les plus utilisés, en addition à d’autres types de capteurs d’angle et de position. Un des défis est le traitement du signal EMG et l’extraction d’information utile de ce dernier. Ces signaux sont de très basse amplitude et sont sujets à plusieurs types de bruit (Wu et al., 2019). Mon projet se focalise sur le traitement du signal EMG lors du mouvement de l’avant bras, l’objectif est de prédire le mouvement effectué à partir de signaux EMG bruts provenant d’une base de donnée publique (Jarque-Bou et al., 2019).

Les détails théoriques du projet sont brièvement expliquées dans [l'affiche](https://github.com/doha-z/GBM3100-Projet/blob/main/Affiche_Doha_Zrouki_GBM3100H23.pdf) et plus en détail dans le [rapport](ttps://github.com/doha-z/GBM3100-Projet/blob/main/RapportDoha_Zrouki_GBM3100H23.pdf).

## Base de données
Les données EMG proviennent d'une [base de données publique](https://zenodo.org/record/3469380#.ZEAhgNLMJFQ).\
La taille du fichier RAW_EMG.mat dépasse les limites de GitHub, ce dernier doit dont être téléchargé localement si besoin.\
Puisque les données sont en format .mat et organisées en structures. Le fichier [database_loading.py](https://github.com/doha-z/GBM3100-Projet/blob/main/database_loading.py) permet la conversion en format .csv à partir d'une structure Pandas.DataFrame.\
Le fichier résultant est également trop volumineux pour Github. Pour simplifier le tout, il est préférable de télécharger le fichier [projet_EMG](https://drive.google.com/drive/folders/1RKFosSexkSFuZpBkKaBENc__k7Xnzkdq?usp=sharing) et de le téléverser sur google drive.

Le fichier [Demo](https://github.com/doha-z/GBM3100-Projet/blob/main/projet_EMG/Demo.ipynb) permet de tester les prédictions de différents modèles préentrainés.\
Le fichier [EMG_project_developpement.ipynb](https://github.com/doha-z/GBM3100-Projet/blob/main/projet_EMG/EMG_project_developpement.ipynb) permet de réentrainer les modèles, sélectionner les mouvements considérés et les canaux EMG. Ce fichier contient toutes les fonctions de prétraitement, d'entrainement et d'optimisation des hyperparamètres.


## Analyse des résultats
Le graphique suivant illustre les performances de chacun des 5 modèles entrainées pour chacune des 25 classes de mouvement considérée.
![alt text](/projet_EMG/graph.svg)

On observe que le classifieur XGB a la meilleure performance (supérieure à 80% pour 20 mouvements différents).

Note : Tout le travail et code est le travail de l'auteure, sauf les fonctions préexistantes d'extraction de 'features'. Les fichiers [digital_processing.py](https://github.com/doha-z/GBM3100-Projet/blob/main/projet_EMG/digital_processing.py) et [feature_extraction.py](https://github.com/doha-z/GBM3100-Projet/blob/main/projet_EMG/feature_extraction.py) proviennent d'un [répositoire existant]([https://github.com/SebastianRestrepoA](https://github.com/SebastianRestrepoA/EMG-pattern-recognition)).

## Références
Jarque-Bou, N. J., Vergara, M., Sancho-Bru, J. L., Gracia-Ibáñez, V., & Roda-Sales, A. (2019). A calibrated database
of kinematics and EMG of the forearm and hand during activities of daily living. Scientific Data, 6(1), Article 1.
https://doi.org/10.1038/s41597-019-0285-1
SebastianRestrepoA. (2023). SebastianRestrepoA/EMG-pattern-recognition [Python].
https://github.com/SebastianRestrepoA/EMG-pattern-recognition/blob/c3a5db8f5b19bb2dc7cf0755b13f14b20403457c/feature_extraction.py (Original work
published 2019)
Wu, J., Li, X., Liu, W., & Wang, Z. J. (2019). sEMG Signal Processing Methods : A Review. Journal of Physics:
Conference Series, 1237(3), 032008. https://doi.org/10.1088/1742-6596/1237/3/032008

## Auteure: 
Doha Zrouki\
Dans le cadre du cours GBM3100 - H2023\
doha.zrouki@polymtl.ca
