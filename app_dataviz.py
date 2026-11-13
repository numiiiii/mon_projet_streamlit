
import pandas as pd
from pathlib import Path
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#config affichage

st.set_page_config(layout="wide")

st.title("Suivi du nombre de passagers en avions")

#Texte de presentation est capable d'afficher des dataframes
st.write("Bienvenue sur cette application interactive dédiée à l'analyse du nombre de passagers en avion en fonction de la periode")
#Fonction pour charger le fichier CSS externe
st.html(Path(__file__).parent / "style.css")

url ="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"

#mise en cache pour eviter les chargement et les lenteurs
@st.cache_data
def load_data(url):
    return pd.read_csv(url)

#charger le fichier
df_flights= load_data(url)

listemois = df_flights["month"].unique()
ordre_mois = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

table_heatmap = df_flights.pivot(index="month", columns="year", values="passengers").reindex(ordre_mois)

col_annee, col_mois = st.columns(2)
with col_annee:
    annee = st.slider(label="Plage de selection année :", min_value=1949, max_value=1960, step=1)
with col_mois:
    mois = st.multiselect(label = " Mois",options=listemois,select_all=True)

masquefiltre = (df_flights["month"].isin(mois)) & (df_flights["year"] == annee)
total_passagers = df_flights.loc[masquefiltre, "passengers"].sum()

col_kpi, col_check = st.columns([2, 1])

with col_kpi:
    st.metric(label = f"Nombre de passagers pris en charge sur l'année : {annee} et pour mois {mois}", value = int(total_passagers))
with col_check:
    afficher_heatmap = st.checkbox(label="Afficher la heatmap",value=False)


if afficher_heatmap:
    col1, col2 = st.columns([2, 1])
else:
    col1 = st.container()

with col1:
    fig = px.line(df_flights[masquefiltre], x="month", y="passengers",line_shape="spline",color_discrete_sequence= ["#7fff00"],markers=True,
                   title=f"Évolution du nombre de passagers en {annee}")
    st.plotly_chart(fig, width = "stretch")

if afficher_heatmap:
    with col2:
        plt.style.use("dark_background")
        table_heatmap = df_flights.pivot(index="month", columns="year", values="passengers").reindex(ordre_mois)
        fig, ax = plt.subplots(figsize=(3, 3))
        sns.heatmap(table_heatmap, ax=ax)
        ax.set_title("Nombre de passagers par mois et par année")
        st.pyplot(fig,width="content")

st.dataframe(df_flights[masquefiltre].head(5))