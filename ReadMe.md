Remarques

    Le fichier model.pkl est nécessaire à app.py et est crée par le second notebook. 
    Il faut donc run 02best_training.ipynb avant app.py


# 01best_model.ipynb : 
Dans ce notebook, j'utilise GridSearchCv pour evaluer plusieurs modèles de regression sur mon jeu de données avec plusieurs hyper_paramètres différents.

# 02best_training.ipynb
Dans ce notebook, j'entraine le modèle avec les hyper-paramètres choisis dans le notebook 01
Et je l'enregistre dans 'model.pkl' pour pouvoir le déployer

# app.py
Dans ce script python, je deploie mon modèle via une web app streamlit

    streamlit run app.py

