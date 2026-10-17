"""
Módulo de Análise Exploratória de Dados (EDA)
Gera gráficos estatísticos de alta resolução para o relatório e apresentação.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from src.data_loader import export_and_load_data

OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
os.makedirs(OUTPUTS_DIR, exist_ok=True)

# Configuração visual profissional
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#CCCCCC'
plt.rcParams['axes.linewidth'] = 0.8

def plot_class_distribution(df):
    """Gera gráfico combinado (Barras + Rosca) da distribuição de classes."""
    counts = df['diagnosis_label'].value_counts()
    colors = ['#2b5c8f', '#d9534f'] # Azul sóbrio para benigno, vermelho para maligno
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)
    
    # 1. Gráfico de Barras
    bars = ax1.bar(counts.index, counts.values, color=colors, width=0.5, edgecolor='black', alpha=0.85)
    ax1.set_title("Frequência Absoluta das Classes", fontsize=12, fontweight='bold', pad=12)
    ax1.set_ylabel("Quantidade de Casos", fontsize=11)
    ax1.set_ylim(0, max(counts.values) * 1.15)
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 10, f"{yval} ({yval/len(df)*100:.1f}%)", 
                 ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # 2. Gráfico de Rosca
    wedges, texts, autotexts = ax2.pie(
        counts.values, 
        labels=counts.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colors,
        wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2),
        textprops=dict(fontsize=10, fontweight='bold')
    )
    for at in autotexts:
        at.set_color('white')
    ax2.set_title("Proporção Relativa (%)", fontsize=12, fontweight='bold', pad=12)
    
    plt.suptitle("Distribuição Diagnóstica - Câncer de Mama Wisconsin (WDBC)", fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    output_path = os.path.join(OUTPUTS_DIR, "eda_distribuicao_classes.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Gráfico de classes salvo: {output_path}")

def plot_correlation_matrix(df, features):
    """Gera mapa de calor da correlação de Pearson para os atributos 'mean'."""
    # Seleciona os 10 primeiros atributos (estatística média) para máxima legibilidade
    mean_cols = [col for col in features if 'mean' in col]
    # Dicionário de tradução para rótulos legíveis
    traducao = {
        'mean radius': 'Raio Médio',
        'mean texture': 'Textura Média',
        'mean perimeter': 'Perímetro Médio',
        'mean area': 'Área Média',
        'mean smoothness': 'Suavidade Média',
        'mean compactness': 'Compacidade Média',
        'mean concavity': 'Concavidade Média',
        'mean concave points': 'Pontos Côncavos Méd.',
        'mean symmetry': 'Simetria Média',
        'mean fractal dimension': 'Dim. Fractal Média'
    }
    sub_df = df[mean_cols].rename(columns=traducao)
    corr = sub_df.corr()

    plt.figure(figsize=(9, 7.5), dpi=300)
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1,
                linewidths=0.5, cbar_kws={"shrink": 0.8, "label": "Coeficiente de Correlação de Pearson"},
                annot_kws={"size": 9})
    plt.title("Matriz de Correlação Linear entre Atributos Morfológicos Médios", fontsize=13, fontweight='bold', pad=15)
    plt.xticks(rotation=45, ha='right', fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    output_path = os.path.join(OUTPUTS_DIR, "eda_matriz_correlacao.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Matriz de correlação salva: {output_path}")

def plot_feature_distributions(df):
    """Gera gráficos de densidade (KDE) comparativos entre Benigno e Maligno."""
    key_features = [
        ('mean radius', 'Raio Médio'),
        ('mean perimeter', 'Perímetro Médio'),
        ('mean concavity', 'Concavidade Média'),
        ('mean texture', 'Textura Média')
    ]
    
    fig, axes = plt.subplots(2, 2, figsize=(11, 8), dpi=300)
    axes = axes.flatten()
    
    for idx, (col, title) in enumerate(key_features):
        ax = axes[idx]
        sns.kdeplot(data=df, x=col, hue='diagnosis_label', palette={'Benigno': '#2b5c8f', 'Maligno': '#d9534f'},
                    fill=True, common_norm=False, alpha=0.45, linewidth=2, ax=ax)
        ax.set_title(f"Distribuição de {title}", fontsize=11, fontweight='bold')
        ax.set_xlabel(f"{title} (valor mensurado)", fontsize=9)
        ax.set_ylabel("Densidade Estimada", fontsize=9)
        ax.grid(True, linestyle='--', alpha=0.6)
        
    plt.suptitle("Comparação das Distribuições Morfológicas por Diagnóstico", fontsize=13, fontweight='bold', y=0.99)
    plt.tight_layout()
    output_path = os.path.join(OUTPUTS_DIR, "eda_distribuicoes_atributos.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Distribuições comparativas salvas: {output_path}")

def plot_boxplots(df):
    """Gera boxplots padronizados para visualização de separabilidade e outliers."""
    cols_to_plot = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean concavity']
    labels = ['Raio', 'Textura', 'Perímetro', 'Área', 'Concavidade']
    
    # Normalização min-max temporária apenas para visualização no mesmo eixo
    df_norm = df.copy()
    for col in cols_to_plot:
        df_norm[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
        
    df_melted = pd.melt(df_norm, id_vars=['diagnosis_label'], value_vars=cols_to_plot,
                        var_name='Atributo', value_name='Valor Normalizado [0, 1]')
    df_melted['Atributo'] = df_melted['Atributo'].map(dict(zip(cols_to_plot, labels)))
    
    plt.figure(figsize=(10, 5), dpi=300)
    sns.boxplot(x='Atributo', y='Valor Normalizado [0, 1]', hue='diagnosis_label', data=df_melted,
                palette={'Benigno': '#2b5c8f', 'Maligno': '#d9534f'}, width=0.6, fliersize=3)
    plt.title("Boxplot Comparativo de Atributos Clínicos Normalizados", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Atributo Clínico", fontsize=10, fontweight='bold')
    plt.ylabel("Valor Normalizado [0 - 1]", fontsize=10, fontweight='bold')
    plt.legend(title="Diagnóstico", loc='upper right')
    plt.tight_layout()
    output_path = os.path.join(OUTPUTS_DIR, "eda_boxplots.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Boxplots salvos: {output_path}")

def run_all_eda():
    df, X, y, features = export_and_load_data()
    print("Iniciando geração de gráficos exploratórios...")
    plot_class_distribution(df)
    plot_correlation_matrix(df, features)
    plot_feature_distributions(df)
    plot_boxplots(df)
    print("Análise Exploratória concluída com sucesso!")

if __name__ == "__main__":
    run_all_eda()
