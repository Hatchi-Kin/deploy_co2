import streamlit as st
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
import joblib


def main():

    # Load the dictionary from the .pkl file
    objects = joblib.load('model.pkl')
    # Access the individual objects
    X = objects['X']
    y = objects['y']
    le = objects['Encoder']
    scaler = objects['Scaler']
    top_model = objects['Model']



    st.title('Déploiement Modèle IA')

    with st.form("my_form"):

        X['Carrosserie'] = le.inverse_transform(X['Carrosserie'])

        carrosserie = st.selectbox('Choisissez votre carosserie', X['Carrosserie'].unique())
        masse_min=st.slider("Masse Minimale Admissible", min_value=800, max_value=3200, value=2000)
        masse_max=st.slider("Masse Maximale Autorisée", min_value=800, max_value=3200, value=2000)
        submitted=st.form_submit_button("Prédire le CO2")

        if submitted:

            new_data = pd.DataFrame([[carrosserie, masse_min, masse_max]], columns=['Carrosserie', 'masse_ordma_min', 'masse_ordma_max'])
            
            # Encode ans scale the inputs
            new_data['Carrosserie'] = le.transform(new_data['Carrosserie'])

            column = new_data['masse_ordma_min'].values.reshape(-1, 1)
            scaled_column = scaler.transform(column)
            new_data['masse_ordma_min'] = scaled_column

            column2 = new_data['masse_ordma_max'].values.reshape(-1, 1)
            scaled_column2 = scaler.transform(column2)
            new_data['masse_ordma_max'] = scaled_column2

            # make a prediction on print it
            prediction = top_model.predict(new_data)
            st.header(f"prédiction CO2 : {int(prediction[0].round())}")


if __name__ == "__main__":
    main()


