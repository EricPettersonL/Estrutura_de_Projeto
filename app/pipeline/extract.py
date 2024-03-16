"""modulo de extract necessárias para consolidar os dados de entrada."""

import glob
import os

import pandas as pd


def extract_excel(input_folder):
    """
    função para extrair dados de arquivos Excel da pasta data/input.

    type: input_folder(str): Caminho da pasta de arquivos (data/input)
    
    return: todos os dados
    """
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))
    if not files:
        raise ValueError("No Excel files found in the specified folder")
    all_data = [pd.read_excel(file) for file in files]
    return all_data
