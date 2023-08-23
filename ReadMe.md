- 01best_model.ipynb
Dans ce notebook, j'utilise GridSearchCV pour tester plusieurs modèles de regression avec plusieurs hyper-paramètres.
Je determine grace aux métriques d'évaluation le modèle et ses paramètres qui donnent les meilleurs résultats sur mon jeu de données.

- 02best_training.ipynb
Dans ce notebook, j'entraine le meilleur modele sur TOUT mon jeu de données 
Et je l'enregistre dans 'model.pkl' pour pouvoir le déployer

- app.py
Dans ce script python, je déploie mon modèle via une web app streamlit

Remarques

    Il est important d'exécuter 02best_training.ipynb avant app.py. Le fichier model.pkl est nécessaire à app.py.
