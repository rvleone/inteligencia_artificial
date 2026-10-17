"""
Módulo de Agrupamento Não Supervisionado (Clusterização)
Algoritmo: K-Means
Análise: Método do Cotovelo (Inertia), Coeficiente de Silhueta e Projeções PCA 2D e 3D.
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, adjusted_rand_score, confusion_matrix
from src.data_loader import export_and_load_data

OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
os.makedirs(OUTPUTS_DIR, exist_ok=True)

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

def evaluate_optimal_clusters(X_scaled, max_k=10):
    """Calcula inércia e silhueta para k de 2 até max_k."""
    k_range = list(range(2, max_k + 1))
    inertias = []
    silhouettes = []
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X_scaled)
        inertias.append(kmeans.inertia_)
        silhouettes.append(silhouette_score(X_scaled, labels))
        
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5), dpi=300)
    
    # 1. Método do Cotovelo
    ax1.plot(k_range, inertias, marker='o', color='#1f77b4', linewidth=2, markersize=7)
    ax1.set_title("Método do Cotovelo (Elbow Method)", fontsize=12, fontweight='bold')
    ax1.set_xlabel("Número de Clusters (k)", fontsize=10)
    ax1.set_ylabel("Inércia (Soma dos Quadrados Intra-Cluster)", fontsize=10)
    ax1.set_xticks(k_range)
    ax1.grid(True, linestyle='--', alpha=0.6)
    
    # Destaca k=2
    ax1.axvline(x=2, color='red', linestyle=':', alpha=0.8, label='k=2 sugerido')
    ax1.legend()
    
    # 2. Coeficiente de Silhueta
    ax2.plot(k_range, silhouettes, marker='s', color='#2ca02c', linewidth=2, markersize=7)
    ax2.set_title("Coeficiente Médio de Silhueta", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Número de Clusters (k)", fontsize=10)
    ax2.set_ylabel("Score de Silhueta", fontsize=10)
    ax2.set_xticks(k_range)
    ax2.grid(True, linestyle='--', alpha=0.6)
    
    # Ponto de máximo
    best_k = k_range[np.argmax(silhouettes)]
    ax2.scatter(best_k, max(silhouettes), color='red', s=100, zorder=5, label=f'Máximo em k={best_k} ({max(silhouettes):.3f})')
    ax2.legend()
    
    plt.suptitle("Determinação do Número Ideal de Clusters para K-Means", fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    output_path = os.path.join(OUTPUTS_DIR, "cluster_elbow_silhouette.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Gráfico Elbow/Silhouette salvo em: {output_path}")
    
    return best_k, silhouettes

def run_kmeans_and_pca(X, y):
    """Executa K-Means (k=2) e projeta os resultados em 2D e 3D via PCA."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 1. Encontra métricas de silhueta
    evaluate_optimal_clusters(X_scaled)
    
    # 2. Treina K-Means com k=2
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=20)
    cluster_labels = kmeans.fit_predict(X_scaled)
    
    # Alinhamento de rótulos com ground truth para fins de concordância
    # (o cluster que mais tem malignos vira rótulo de maligno)
    ari = adjusted_rand_score(y, cluster_labels)
    sil = silhouette_score(X_scaled, cluster_labels)
    print(f"K-Means (k=2) -> Silhueta: {sil:.4f} | Rand Index Ajustado (ARI): {ari:.4f}")
    
    # 3. PCA 2D
    pca_2d = PCA(n_components=2, random_state=42)
    X_pca_2d = pca_2d.fit_transform(X_scaled)
    var_exp_2d = pca_2d.explained_variance_ratio_ * 100
    
    centroids_2d = pca_2d.transform(kmeans.cluster_centers_)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), dpi=300)
    
    # Subplot 1: Clusters K-Means
    colors_km = ['#2b5c8f' if l == 0 else '#e67e22' for l in cluster_labels]
    ax1.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=colors_km, alpha=0.6, edgecolors='none', s=40)
    ax1.scatter(centroids_2d[:, 0], centroids_2d[:, 1], c='black', marker='X', s=160, linewidths=2, edgecolors='white', label='Centroides')
    ax1.set_title("Agrupamento Não Supervisionado (K-Means, k=2)", fontsize=11, fontweight='bold')
    ax1.set_xlabel(f"PC1 ({var_exp_2d[0]:.1f}% da variância explicada)", fontsize=10)
    ax1.set_ylabel(f"PC2 ({var_exp_2d[1]:.1f}% da variância explicada)", fontsize=10)
    ax1.legend(loc='upper right')
    
    # Subplot 2: Classes Reais (Ground Truth)
    colors_real = ['#2b5c8f' if l == 0 else '#d9534f' for l in y] # 0=Benigno (azul), 1=Maligno (vermelho)
    scatter2 = ax2.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=colors_real, alpha=0.6, edgecolors='none', s=40)
    ax2.set_title("Diagnóstico Real dos Pacientes (Supervisionado)", fontsize=11, fontweight='bold')
    ax2.set_xlabel(f"PC1 ({var_exp_2d[0]:.1f}% da variância explicada)", fontsize=10)
    ax2.set_ylabel(f"PC2 ({var_exp_2d[1]:.1f}% da variância explicada)", fontsize=10)
    
    # Custom legend for Ground Truth
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Benigno', markerfacecolor='#2b5c8f', markersize=8),
        Line2D([0], [0], marker='o', color='w', label='Maligno', markerfacecolor='#d9534f', markersize=8)
    ]
    ax2.legend(handles=legend_elements, loc='upper right')
    
    plt.suptitle("Projeção PCA 2D: Comparativo entre Clusters Não Supervisionados e Classes Reais", 
                 fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    output_path_2d = os.path.join(OUTPUTS_DIR, "cluster_pca_2d.png")
    plt.savefig(output_path_2d, bbox_inches='tight')
    plt.close()
    print(f"Projeção PCA 2D salva em: {output_path_2d}")
    
    # 4. PCA 3D
    pca_3d = PCA(n_components=3, random_state=42)
    X_pca_3d = pca_3d.fit_transform(X_scaled)
    var_exp_3d = pca_3d.explained_variance_ratio_ * 100
    
    fig = plt.figure(figsize=(9, 7), dpi=300)
    ax = fig.add_subplot(111, projection='3d')
    
    # Rótulo de cores: Benigno vs Maligno
    colors_3d = ['#2b5c8f' if l == 0 else '#d9534f' for l in y]
    ax.scatter(X_pca_3d[:, 0], X_pca_3d[:, 1], X_pca_3d[:, 2], c=colors_3d, alpha=0.7, edgecolors='k', linewidth=0.2, s=35)
    
    ax.set_title("Visualização Espacial 3D dos Dados via PCA\n(Azul = Benigno, Vermelho = Maligno)", 
                 fontsize=12, fontweight='bold', pad=15)
    ax.set_xlabel(f"PC1 ({var_exp_3d[0]:.1f}%)", fontweight='bold')
    ax.set_ylabel(f"PC2 ({var_exp_3d[1]:.1f}%)", fontweight='bold')
    ax.set_zlabel(f"PC3 ({var_exp_3d[2]:.1f}%)", fontweight='bold')
    ax.view_init(elev=20, azim=125)
    
    plt.tight_layout()
    output_path_3d = os.path.join(OUTPUTS_DIR, "cluster_pca_3d.png")
    plt.savefig(output_path_3d, bbox_inches='tight')
    plt.close()
    print(f"Projeção PCA 3D salva em: {output_path_3d}")
    
    return {
        "silhouette_k2": float(sil),
        "ari_k2": float(ari),
        "pca_variance_2d": var_exp_2d.tolist(),
        "pca_variance_3d": var_exp_3d.tolist()
    }

if __name__ == "__main__":
    df, X, y, features = export_and_load_data()
    print("Iniciando rotina de clusterização...")
    results = run_kmeans_and_pca(X, y)
    print("Resultados de Clusterização:", results)
