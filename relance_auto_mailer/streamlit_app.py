# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 13:02:35 2025

@author: roman
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import tempfile
import logging
from pathlib import Path

from relance_auto_mailer import extract_data, envoyer_mails, settings

# Configuration de base du logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Configuration de la page Streamlit
    st.set_page_config(page_title="Relance Automatique", layout="centered")
    st.title("📧 Relance automatique")

    # Description succincte de l'application
    st.markdown("Ce logiciel génère et envoie automatiquement les relances issues du portefeuille en deux étapes :")
    st.markdown("1. Génération du fichier de relance à partir du portefeuille")
    st.markdown("2. Envoi des e-mails de relance aux fournisseurs")

    # Étape 1 : upload du fichier de commandes
    st.header("1. Chargement du fichier de commandes")
    st.markdown("Attention a nommer la feuille des retards : 'Retards'")
    commandes_file = st.file_uploader(
        "📄 Sélectionnez le fichier portefeuille (.xlsx)", type=["xlsx"], key="cmd"
    )

    # Bouton de génération du fichier de relance
    if commandes_file and st.button("🛠 Générer le fichier de relance"):
        # Affichage de la barre de progression
        progress = st.progress(0)
        # Écriture temporaire du fichier uploadé
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
            tmp.write(commandes_file.read())
            cmd_path = Path(tmp.name)
        progress.progress(30)  # Mise à jour de la progression

        try:
            # Appel à la fonction d'extraction de données
            nb, sortie = extract_data(cmd_path)
            progress.progress(60)
            # Notification de succès avec détail
            st.success(f"✅ Fichier généré : {sortie} ({nb} lignes)")
            # Bouton de téléchargement du fichier généré
            with open(sortie, "rb") as f:
                st.download_button(
                    "📥 Télécharger le fichier de relance", data=f, file_name=Path(sortie).name
                )
        except Exception as e:
            # Log et affichage d'erreur
            logger.exception("Erreur lors de la génération du fichier de relance")
            st.error(f"Erreur : {e}")
        progress.progress(100)

    # Étape 2 : paramètres et envoi des relances
    st.header("2. Envoi des relances par e-mail")
    with st.expander("⚙️ Paramètres de messagerie et de la signature"):
        # Champs pour les paramètres SMTP
        sender_name = st.text_input("Nom de l'expéditeur", value=settings.SENDER_NAME)
        sender_email = st.text_input("Adresse e-mail expéditeur", value=settings.SENDER_EMAIL)
        sender_password = st.text_input("Mot de passe ou token SMTP", type="password")
        st.markdown("⚠️ Le mot de passe n'est pas conservé")
        # Choix de la langue
        language = st.selectbox(
            "Langue par défaut", options=["FR", "EN"],
            index=0 if settings.DEFAULT_LANGUAGE.upper()=="FR" else 1
        )

    # Bouton pour déclencher l'envoi des relances
    if st.button("📤 Envoyer les relances"):
        relance_path = Path("relance_fournisseurs.xlsx")  # fichier généré à l'étape 1
        # Vérification préalable
        if not relance_path.exists():
            st.error("Veuillez d'abord générer le fichier de relance.")
        elif not sender_email or not sender_password:
            st.error("Merci de remplir tous les paramètres de messagerie.")
        else:
            # Mise à jour des settings dynamiquement
            settings.SENDER_NAME = sender_name
            settings.DEFAULT_LANGUAGE = language
            settings.SENDER_EMAIL = sender_email
            settings.SENDER_PASSWORD = sender_password

            try:
                # Appel à la fonction d'envoi des e-mails
                memoire_file = envoyer_mails(relance_path, sender_email, sender_password)
                st.success("📬 E-mails envoyés avec succès !")
                # Bouton de téléchargement du mémo des relances
                with open(memoire_file, "rb") as f:
                    st.download_button(
                        "📥 Télécharger le mémo des relances", data=f,
                        file_name=Path(memoire_file).name
                    )
            except Exception as e:
                # Log et affichage d'erreur en cas d'échec
                logger.exception("Erreur lors de l'envoi des relances")
                st.error(f"Erreur : {e}")
                
    st.markdown("© Réalisé par Romane Fourrier - 2025 - Tous droits réservés.")

# Point d'entrée
if __name__ == "__main__":
    main()
