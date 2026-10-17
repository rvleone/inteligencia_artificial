"""
Script Principal de Execução - Avaliação Formativa de Inteligência Artificial
Universidade Salgado de Oliveira (UNIVERSO)
Executa todo o fluxo de ponta a ponta:
  1. Carregamento e exportação do banco de dados para CSV
  2. Análise Exploratória de Dados (EDA)
  3. Clusterização Não Supervisionada (K-Means + PCA)
  4. Classificação Supervisionada com Validação Cruzada (10-Fold)
"""

import sys
import os

# Adiciona o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.data_loader import export_and_load_data, get_data_summary
from src.eda import run_all_eda
from src.clustering import run_kmeans_and_pca
from src.classification import run_classification_pipeline

def main():
    print("=" * 70)
    print(" PROJETO DE INTELIGÊNCIA ARTIFICIAL - AVALIAÇÃO FORMATIVA (AF 2026-II)")
    print(" Aluno / Pesquisador: Ricardo Vieira Leone")
    print(" Instituição: UNIVERSO EAD - Sistemas de Informação / ADS")
    print("=" * 70)
    
    # 1. Dados
    print("\n[ETAPA 1/4] Carregamento do Banco de Dados Breast Cancer Wisconsin...")
    df, X, y, features = export_and_load_data()
    summary = get_data_summary(df)
    print(f"-> Base carregada com {summary['n_samples']} amostras e {summary['n_features']} atributos.")
    print(f"-> Diagnósticos: {summary['classes_count']['Benigno']} Benignos ({summary['classes_percent']['Benigno']}%) | {summary['classes_count']['Maligno']} Malignos ({summary['classes_percent']['Maligno']}%)")
    
    # 2. EDA
    print("\n[ETAPA 2/4] Executando Análise Exploratória de Dados (EDA)...")
    run_all_eda()
    
    # 3. Clusterização
    print("\n[ETAPA 3/4] Executando Clusterização Não Supervisionada (K-Means & PCA)...")
    cluster_res = run_kmeans_and_pca(X, y)
    print(f"-> Silhueta k=2: {cluster_res['silhouette_k2']:.4f} | Rand Index Ajustado: {cluster_res['ari_k2']:.4f}")
    
    # 4. Classificação
    print("\n[ETAPA 4/4] Executando Classificação Supervisionada (Stratified 10-Fold)...")
    clf_results, df_summary = run_classification_pipeline()
    
    print("\n" + "=" * 70)
    print(" EXECUÇÃO CONCLUÍDA COM SUCESSO!")
    print(" Todos os gráficos e tabelas foram gerados no diretório: outputs/")
    print("=" * 70)

if __name__ == "__main__":
    main()
