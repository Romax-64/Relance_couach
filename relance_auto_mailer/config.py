# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 13:32:08 2025

@author: roman
"""

import streamlit as st
from pathlib import Path

# Chargement des paramètres depuis Streamlit Secrets
class Settings:
    SMTP_HOST: str = st.secrets["SMTP_HOST"]
    SMTP_PORT: int = int(st.secrets.get("SMTP_PORT", 587))

    SENDER_NAME: str = st.secrets["SENDER_NAME"]
    SENDER_EMAIL: str = st.secrets["SENDER_EMAIL"]
    SENDER_PASSWORD: str = st.secrets["SENDER_PASSWORD"]

    DEFAULT_LANGUAGE: str = st.secrets.get("DEFAULT_LANGUAGE", "FR")
    LOGO_FILENAME: str = st.secrets.get("LOGO_FILENAME", "logo.png")

    SUBJECT_FR: str = st.secrets.get("SUBJECT_FR", "Suivi commandes en cours")
    SUBJECT_EN: str = st.secrets.get("SUBJECT_EN", "Follow-up on ongoing orders")

    # Chemins internes
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    RESOURCES_DIR: Path = BASE_DIR / 'resources'
    TEMPLATES_DIR: Path = BASE_DIR / 'relance_auto_mailer'

# Instanciation pour import
settings = Settings()


