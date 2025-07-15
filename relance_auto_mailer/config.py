# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 13:32:08 2025

@author: roman
"""

from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Configuration du chargement depuis le fichier .env
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

    SMTP_HOST: str                 = Field('smtp.office365.com', description="Adresse du serveur SMTP")
    SMTP_PORT: int                 = Field(587, description="Port du serveur SMTP")

    SENDER_NAME: str               = Field('Romane Fourrier', description="Nom complet de l'expéditeur")
    SENDER_EMAIL: str              = Field('r.fourrier@couach.com', description="Adresse e-mail de l'expéditeur")
    SENDER_PASSWORD: str           = Field('rmoo28FnW', description="Mot de passe ou token SMTP")

    DEFAULT_LANGUAGE: str          = Field('FR', description="Langue par défaut : 'FR' ou 'EN'")
    LOGO_FILENAME: str             = Field('logo.png', description="Nom du fichier logo dans resources/")

    SUBJECT_FR: str                = Field('Suivi commandes en cours', description="Sujet du mail en français")
    SUBJECT_EN: str                = Field('Follow-up on ongoing orders', description="Sujet du mail en anglais")

    BASE_DIR: Path                 = Field(default_factory=lambda: Path(__file__).resolve().parent.parent)
    RESOURCES_DIR: Path            = Field(default_factory=lambda: Path(__file__).resolve().parent.parent / 'resources')
    TEMPLATES_DIR: Path            = Field(default_factory=lambda: Path(__file__).resolve().parent / 'relance_auto_mailer')

# Instanciation des paramètres avec valeurs par défaut
settings = Settings()

