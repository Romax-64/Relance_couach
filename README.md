# Relance_couach
Relance Automatique - Guide d'installation et d'utilisation

1. Prérequis
   - Python 3.7 ou supérieur
   - pip (gestionnaire de paquets Python)

2. Installation des dépendances
   Ouvrez un terminal dans le dossier racine du projet et lancez :

       pip install -r requirements.txt

3. Configuration
   Copiez le fichier modèle d'environnement et modifiez-le :

       cp .env.example .env
       # Ouvrez .env et renseignez vos identifiants SMTP et paramètres

4. Lancement de l'application
   En mode développement (Streamlit) :

       streamlit run relance_auto_mailer/streamlit_app.py

   Ou via le script console installé :

       relance-mailer

5. Utilisation
   - Étape 1 : Téléchargez votre fichier de commandes (.xlsx). Cliquez sur **Générer** pour créer
     `relance_fournisseurs.xlsx` et téléchargez-le.
   - Étape 2 : Remplissez les paramètres SMTP (nom, e‑mail, mot de passe, langue). Cliquez sur **Envoyer** pour
     envoyer les relances et générez un mémo téléchargeable.

6. Packaging (optionnel)
   Pour obtenir un exécutable Windows :

       cd scripts
       ./build_executable.sh

   Le binaire sera disponible dans `dist/relance-auto-mailer.exe`.

7. Support
   Pour toute question, ouvrez une issue dans le dépôt ou contactez l'équipe technique.
