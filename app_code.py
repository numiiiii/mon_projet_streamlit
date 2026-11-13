
# --- IMPORTATION DES BIBLIOTHÈQUES ---
import pandas as pd                              # Manipulation et lecture de données tabulaires (CSV, DataFrame)
from pathlib import Path                         # Gestion propre des chemins de fichiers indépendamment du dossier d'exécution
import streamlit as st                           # Création de l'interface web interactive
from streamlit_option_menu import option_menu    # Composant tiers pour afficher un menu de navigation stylisé avec icônes

st.set_page_config(layout="wide")

# --- 1. INITIALISATION DE LA SESSION ---
# st.session_state conserve les variables en mémoire d'un rechargement de page à l'autre
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False        # Par défaut, l'utilisateur n'est pas connecté
if "username" not in st.session_state:
    st.session_state["username"] = ""            # Par défaut, aucun nom d'utilisateur n'est enregistré


# --- 2. FONCTION DE VÉRIFICATION DES IDENTIFIANTS ---
@st.cache_data                                   # Met en cache le CSV en mémoire pour éviter de le relire à chaque clic
def load_accounts():
    # Construit le chemin absolu vers accounts.csv situé dans le même dossier que ce script
    chemin_fichier = Path(__file__).parent / "account.csv"
    # Lit le fichier en forçant le type texte (str) pour éviter que les mots de passe numériques soient lus comme des entiers
    return pd.read_csv(chemin_fichier, dtype=str)

def authenticate(username_input, password_input):
    accounts_df = load_accounts()                # Récupère la table des comptes autorisés
    # Filtre le DataFrame pour chercher une ligne correspondant exactement au login ET au mot de passe saisis
    user_match = accounts_df[
        (accounts_df["name"] == username_input) & (accounts_df["password"] == password_input)
    ]
    # Renvoie True si au moins une ligne correspond (DataFrame non vide), False sinon
    return not user_match.empty


# --- 3. GESTION DE L'AFFICHAGE CONDITIONNEL ---
# Si l'utilisateur n'est PAS encore authentifié, on affiche uniquement l'écran de connexion
if not st.session_state["logged_in"]:
    # --- PAGE DE CONNEXION ---
    st.title("Connexion à l'Application Data")
    st.subheader("Veuillez vous identifier pour accéder au contenu")

    # Champs de saisie utilisateur (type="password" masque les caractères saisis)
    username_input = st.text_input("Nom d'utilisateur")
    password_input = st.text_input("Mot de passe", type="password")

    # Déclenche la vérification au clic sur le bouton
    if st.button("Se connecter"):
        if authenticate(username_input, password_input):
            st.session_state["logged_in"] = True           # Enregistre l'état connecté dans la session
            st.session_state["username"] = username_input  # Mémorise le nom de l'utilisateur connecté
            st.success(f"Bienvenue {username_input} !")
            st.rerun()                                     # Force le rechargement immédiat du script pour basculer dans le bloc "else"
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")

# Si l'utilisateur EST authentifié, on affiche l'application complète
else:
    # --- APPLICATION SÉCURISÉE (UTILISATEUR CONNECTÉ) ---
    # 1. Barre latérale (sidebar) : profil, déconnexion et menu de navigation
    with st.sidebar:
        st.write(f"Bienvenue, **{st.session_state['username']}**!")

        # Bouton de déconnexion : réinitialise la session et recharge la page vers l'écran de login
        if st.button("Se déconnecter"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.rerun()

        st.divider()                                       # Ligne horizontale de séparation visuelle

        # Menu de navigation latéral retournant le nom de l'onglet sélectionné
        selected_page = option_menu(
            menu_title="Menu principal",
            options=["Accueil", "Galerie Photos"],         # Liste des pages disponibles
            icons=["house", "images"],                     # Icônes Bootstrap associées à chaque page
            default_index=0                                # Onglet sélectionné par défaut au démarrage ("Accueil")
        )

    # 2. Contenu principal affiché selon le choix effectué dans le menu latéral
    if selected_page == "Accueil":
        st.title("Page d'Accueil Réservée")
        st.write("Ce contenu est uniquement accessible aux utilisateurs authentifiés.")

    elif selected_page == "Galerie Photos":
        st.title("Album Photos")
        st.write("Voici la galerie multimédia organisée sur 3 colonnes:")

        # Crée 3 colonnes de largeur égale côte à côte
        cols = st.columns(3)

        # Liste d'images à afficher
        dossier_images = Path(__file__).parent / "images"
        galerie = [
            (dossier_images / "tux.jpeg", "Linux (Tux)"),
            (dossier_images / "pandas.jpeg", "Pandas"),
            (dossier_images / "python.jpeg", "Python")
        ]

        for idx, (img_path, titre) in enumerate(galerie):
            with cols[idx % 3]:
                st.image(str(img_path), caption=titre, width="stretch")

with st.sidebar:
    st.write("Debug session_state :")
    st.write(st.session_state)

    