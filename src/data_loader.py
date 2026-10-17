"""
Módulo de Carregamento e Preparação dos Dados
Dataset: Breast Cancer Wisconsin (Diagnostic) - UCI Machine Learning Repository
"""

import os
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
CSV_PATH = os.path.join(DATA_DIR, "breast_cancer_wisconsin.csv")

def export_and_load_data():
    """
    Carrega o dataset Breast Cancer Wisconsin e salva em CSV se ainda não existir.
    Retorna o DataFrame completo, features (X), labels (y) e metadados.
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    raw = load_breast_cancer(as_frame=True)
    df = raw.frame.copy()
    
    # Mapeamento do target: no scikit-learn 0=malignant, 1=benign.
    # Por convenção médica em classificação binária onde o evento de interesse/positivo é 'Maligno':
    # Definimos: 1 = Maligno (Positivo), 0 = Benigno (Negativo)
    # Isso torna a Sensibilidade (Recall do tumor maligno) perfeitamente interpretável clinicamente.
    df['diagnosis_numeric'] = df['target'].map({0: 1, 1: 0}) # 1: Maligno, 0: Benigno
    df['diagnosis_label'] = df['diagnosis_numeric'].map({1: 'Maligno', 0: 'Benigno'})
    
    # Salva em CSV para atender aos requisitos de entrega de arquivos
    df.to_csv(CSV_PATH, index=False)
    
    feature_names = list(raw.feature_names)
    X = df[feature_names]
    y = df['diagnosis_numeric']
    
    return df, X, y, feature_names

def get_data_summary(df):
    """
    Gera um resumo estatístico do conjunto de dados para a análise exploratória e relatório.
    """
    summary = {
        "n_samples": len(df),
        "n_features": len([c for c in df.columns if c not in ['target', 'diagnosis_numeric', 'diagnosis_label']]),
        "missing_values": int(df.isnull().sum().sum()),
        "classes_count": df['diagnosis_label'].value_counts().to_dict(),
        "classes_percent": (df['diagnosis_label'].value_counts(normalize=True) * 100).round(2).to_dict()
    }
    return summary

if __name__ == "__main__":
    df, X, y, features = export_and_load_data()
    summary = get_data_summary(df)
    print("Dataset Carregado com Sucesso!")
    print(f"Total de Amostras: {summary['n_samples']}")
    print(f"Total de Atributos Clínicos: {summary['n_features']}")
    print(f"Valores Faltantes: {summary['missing_values']}")
    print(f"Distribuição das Classes: {summary['classes_count']} ({summary['classes_percent']}%)")
    print(f"Arquivo CSV salvo em: {CSV_PATH}")
