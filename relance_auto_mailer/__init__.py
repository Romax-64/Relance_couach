# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 13:35:06 2025

@author: roman
"""

__version__ = "1.0.0"

from .config import settings
from .extractor import extract_data
from .mailer import envoyer_mails
from .utils import (
    is_valid_email,
    extract_valid_emails,
    get_today_str,
    generate_memory_filename
)

__all__ = [
    "__version__",
    "settings",
    "extract_data",
    "envoyer_mails",
    "is_valid_email",
    "extract_valid_emails",
    "get_today_str",
    "generate_memory_filename"
]