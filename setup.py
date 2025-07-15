# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 13:16:29 2025

@author: roman
"""

from setuptools import setup, find_packages

setup(
    name='relance_auto_mailer',
    version='1.0.0',
    description='Automatisation des relances fournisseurs par e-mail via Streamlit',
    author='Romane FOURRIER',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit>=1.0',
        'openpyxl>=3.0',
        'jinja2>=3.0',
        'pydantic>=2.0',
        'python-dotenv>=0.19'
    ],
    entry_points={
        'console_scripts': [
            'relance-mailer=relance_auto_mailer.streamlit_app:main'
        ]
    }
)
