----------------------------------------------------------------------------------------------------
-                                APPLICATION DE DÉMO STREAMLIT                                     -
----------------------------------------------------------------------------------------------------

1 - PRÉSENTATION DU PROJET
--------------------------
app-code.py est une application pédagogique qui met en pratique les notions acquises lors de ma 
formation Bootcamp Data Analytics (modules Streamlit, Git et GitHub).

Application déployée en ligne : https://mon-app-code.streamlit.app/


2 - FONCTIONNALITÉS PRINCIPALES
-------------------------------
Cette application illustre la gestion des accès sur Streamlit, la création de menus interactifs, 
le filtrage dynamique et l'affichage de données ou de visualisations selon les choix de l'utilisateur.

Elle s'articule autour de trois vues principales :
  - La page de connexion : l'utilisateur saisit ses identifiants pour accéder au reste de l'application.
  - Le menu latéral : propose la navigation entre les pages « Accueil » et « Galerie Photos », ainsi 
    qu'un bouton de déconnexion.
  - La page Accueil : affiche un tableau de bord interactif sur le trafic aérien (filtres par année 
    et par mois, indicateur clé, courbe d'évolution et heatmap optionnelle).
  - La page Galerie Photos : présente une série de trois images organisées en colonnes.


3 - TECHNOLOGIES UTILISÉES
--------------------------
L'application est développée en Python avec les outils et bibliothèques suivants :
  - Pandas : récupération, filtrage et exploitation des données.
  - Plotly, Matplotlib et Seaborn : création des graphiques interactifs et statiques.
  - Streamlit : conception de l'interface web interactive.
  - CSS : personnalisation de la mise en page et gestion des marges en plein écran.
  - Git & GitHub : suivi de version et hébergement du code source.
  - Streamlit Community Cloud : déploiement et hébergement de l'application en ligne.


4 - STRUCTURE DU DÉPÔT
----------------------
Dans ce dépôt, vous trouverez :
  - images/          : dossier contenant les visuels affichés dans la galerie.
  - .gitignore       : liste des fichiers et dossiers exclus du suivi Git.
  - account.csv      : fichier contenant les identifiants et mots de passe autorisés (utilisé ici 
                       à des fins pédagogiques pour valider la connexion).
  - app-code.py      : script principal de l'application Streamlit.
  - requirements.txt : liste des bibliothèques Python nécessaires et de leurs versions pour 
                       reproduire l'environnement virtuel.
  - style.css        : feuille de style gérant les marges et l'affichage web de l'application.


5 - INSTALLATION ET EXÉCUTION EN LOCAL
--------------------------------------
Pour lancer l'application sur votre machine :

  1. Cloner le dépôt :
     git clone <URL_DU_DEPOT>
     cd <NOM_DU_DOSSIER>

  2. Créer et activer un environnement virtuel, puis installer les dépendances :
     python3 -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt

  3. Lancer l'application en local :
     streamlit run app-code.py


6 - UTILISATION
---------------
Une fois l'application lancée, ouvrez le fichier account.csv pour récupérer un couple 
identifiant / mot de passe valide, saisissez-le sur l'écran de connexion, puis naviguez entre 
les différentes pages via le menu latéral. Cliquez sur « Se déconnecter » pour fermer la session.

Enjoy!

       .--.           .--.
      : (\ ". _..._ ." /) :
       '.    `     `    .'
        /   _       _   \
       |   (o)     (o)   |
       |        ^        |
        \     '---'     /
         '.           .'
        _.-'`'-----'`'-._
      .'   _         _   '.
     /    / \       / \    \
    |    |   |     |   |    |
     \    \_/       \_/    /
      '.                 .'
        '-.___________.-'