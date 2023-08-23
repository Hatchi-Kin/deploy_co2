# 01best_model.ipynb
Dans ce notebook, j'utilise GridSearchCV pour tester plusieurs modèles de regression avec plusieurs hyper-paramètres.
Je determine grace aux métriques d'évaluation le modèle et ses paramètres qui donnent les meilleurs résultats sur mon jeu de donées.

# 02best_training.ipynb
Dans ce notebook, j'entraine le meilleur modele sur TOUT mon jeu de donnée et je l'enregistre dans un .pkl pour pouvoir le deployer

# app.py
Dans ce script python, je déploie mon modèle via une web app streamlit

Pensez à run 02best_training.ipynb avant app.py pour être sur d'avoir créer un fichier .pkl qui contient le modèle
