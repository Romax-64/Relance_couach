# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 13:02:35 2025

@author: roman
"""

import re
from datetime import date
from pathlib import Path


def is_valid_email(address: str) -> bool:
    # Vérifie que l'adresse correspond au pattern e-mail
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(address and re.match(pattern, address))


def extract_valid_emails(text: str) -> list[str]:
    # Sépare la chaîne en candidats, filtre les adresses valides
    if not text:
        return []
    parts = re.split(r'[;,\s]+', text)
    valid = []
    for email in parts:
        email = email.strip()
        if is_valid_email(email):
            valid.append(email)
    return valid


def get_today_str(fmt: str = '%d/%m/%Y') -> str:
    # Retourne la date du jour formatée selon le format donné
    return date.today().strftime(fmt)


def generate_memory_filename(prefix: str = 'Memoire', suffix: str = 'xlsx') -> Path:
    # Construit un nom de fichier avec date du jour, ex: Memoire_15_07_2025.xlsx
    today = get_today_str().replace('/', '_')
    filename = f"{prefix}_{today}.{suffix}"
    return Path(filename)
