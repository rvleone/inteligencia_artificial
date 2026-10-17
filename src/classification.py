"""
Módulo de Classificação Supervisionada e Avaliação de Desempenho
Estratégia: Stratified K-Fold Cross-Validation (k=10)
Modelos:
  1. Árvore de Decisão (Decision Tree)
  2. K-Nearest Neighbors (KNN)
  3. Support Vector Machine (SVM)
  4. Naive Bayes (Gaussian NB)
  5. Redes Neurais Artificiais (MLP - Multi-Layer Perceptron)
"""

import os
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score, recall_score, roc_auc_score,
    confusion_matrix, roc_curve, auc
)

from src.data_loader import export_and_load_data

OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outputs")
os.makedirs(OUTPUTS_DIR, exist_ok=True)

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

def get_models():
    """
    Retorna dicionário com os 5 classificadores e justificativas de hiperparâmetros.
    """
    models = {
        "Árvore de Decisão": {
            "model": DecisionTreeClassifier(criterion='gini', max_depth=4, min_samples_split=5, random_state=42),
            "use_scaler": False,
            "justification": "Critério de Gini com max_depth=4 para evitar overfitting mantendo alta interpretabilidade clínica."
        },
        "K-Nearest Neighbors (KNN)": {
            "model": KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2),
            "use_scaler": True,
            "justification": "k=5 vizinhos com distância euclidiana, garantindo equilíbrio entre viés e variância após padronização Z-score."
        },
        "Support Vector Machine (SVM)": {
            "model": SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42),
            "use_scaler": True,
            "justification": "Kernel RBF (Gaussiano) com regularização C=1.0 para mapeamento não linear em espaço de alta dimensão."
        },
        "Naive Bayes": {
            "model": GaussianNB(),
            "use_scaler": True,
            "justification": "Distribuição Gaussiana para atributos contínuos; baseline probabilístico rápido sob premissa de independência condicional."
        },
        "Rede Neural (MLP)": {
            "model": MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', solver='adam',
                                  max_iter=500, alpha=0.001, random_state=42),
            "use_scaler": True,
            "justification": "Arquitetura com 2 camadas ocultas (64 e 32 neurônios), ReLU e otimizador Adam com regularização L2 (alpha=0.001)."
        }
    }
    return models

def evaluate_models_kfold(X, y, n_splits=10):
    """
    Executa validação cruzada Stratified 10-Fold para todos os modelos,
    calculando Acurácia, Sensibilidade (Recall), Especificidade, AUC e Matriz de Confusão.
    """
    models = get_models()
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    
    results = {}
    
    for name, config in models.items():
        print(f"Treinando e avaliando: {name} ({n_splits}-fold)...")
        accuracies = []
        sensitivities = [] # Recall de Maligno (classe 1)
        specificities = [] # True Negative Rate (classe 0)
        aucs = []
        
        # Para curva ROC agregada por interpolação
        mean_fpr = np.linspace(0, 1, 100)
        tprs = []
        
        # Matriz de confusão agregada
        total_cm = np.zeros((2, 2), dtype=int)
        
        for train_idx, test_idx in skf.split(X, y):
            X_train, X_test = X.iloc[train_idx].copy(), X.iloc[test_idx].copy()
            y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
            
            if config["use_scaler"]:
                scaler = StandardScaler()
                X_train = scaler.fit_transform(X_train)
                X_test = scaler.transform(X_test)
            
            clf = config["model"]
            clf.fit(X_train, y_train)
            
            y_pred = clf.predict(X_test)
            if hasattr(clf, "predict_proba"):
                y_prob = clf.predict_proba(X_test)[:, 1]
            elif hasattr(clf, "decision_function"):
                y_prob = clf.decision_function(X_test)
            else:
                y_prob = y_pred
                
            # Métricas do fold
            cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
            total_cm += cm
            tn, fp, fn, tp = cm.ravel()
            
            acc = accuracy_score(y_test, y_pred)
            sens = tp / (tp + fn) if (tp + fn) > 0 else 0.0 # Recall
            spec = tn / (tn + fp) if (tn + fp) > 0 else 0.0 # TNR
            try:
                fold_auc = roc_auc_score(y_test, y_prob)
            except Exception:
                fold_auc = 0.5
                
            accuracies.append(acc)
            sensitivities.append(sens)
            specificities.append(spec)
            aucs.append(fold_auc)
            
            # ROC curve interpolation
            fpr, tpr, _ = roc_curve(y_test, y_prob)
            interp_tpr = np.interp(mean_fpr, fpr, tpr)
            interp_tpr[0] = 0.0
            tprs.append(interp_tpr)
            
        mean_tpr = np.mean(tprs, axis=0)
        mean_tpr[-1] = 1.0
        mean_auc = auc(mean_fpr, mean_tpr)
        
        results[name] = {
            "accuracy_mean": np.mean(accuracies),
            "accuracy_std": np.std(accuracies),
            "sensitivity_mean": np.mean(sensitivities),
            "sensitivity_std": np.std(sensitivities),
            "specificity_mean": np.mean(specificities),
            "specificity_std": np.std(specificities),
            "auc_mean": np.mean(aucs),
            "auc_std": np.std(aucs),
            "confusion_matrix": total_cm,
            "mean_fpr": mean_fpr,
            "mean_tpr": mean_tpr,
            "roc_auc": mean_auc,
            "justification": config["justification"]
        }
        
    return results

def plot_roc_curves(results):
    """Plota as curvas ROC comparativas de todos os modelos em um único gráfico."""
    plt.figure(figsize=(9, 7), dpi=300)
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    for idx, (name, res) in enumerate(results.items()):
        color = colors[idx % len(colors)]
        plt.plot(res['mean_fpr'], res['mean_tpr'], color=color, linewidth=2.2,
                 label=f"{name} (AUC = {res['auc_mean']:.4f} \u00b1 {res['auc_std']:.3f})")
                 
    plt.plot([0, 1], [0, 1], linestyle='--', color='gray', linewidth=1.5, label='Classificador Aleatório (AUC = 0.50)')
    plt.xlim([-0.01, 1.01])
    plt.ylim([0.0, 1.02])
    plt.xlabel('Taxa de Falsos Positivos (1 - Especificidade)', fontsize=11, fontweight='bold')
    plt.ylabel('Taxa de Verdadeiros Positivos (Sensibilidade)', fontsize=11, fontweight='bold')
    plt.title('Curvas ROC Comparativas (10-Fold Cross-Validation)', fontsize=13, fontweight='bold', pad=15)
    plt.legend(loc="lower right", fontsize=10, frameon=True, facecolor='white', framealpha=0.9)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    output_path = os.path.join(OUTPUTS_DIR, "curvas_roc_comparativas.png")
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Curvas ROC salvas em: {output_path}")

def plot_confusion_matrices(results):
    """Plota as matrizes de confusão agregadas de todos os modelos em subplots."""
    fig, axes = plt.subplots(2, 3, figsize=(15, 9.5), dpi=300)
    axes = axes.flatten()
    
    class_labels = ['Benigno (0)', 'Maligno (1)']
    
    for idx, (name, res) in enumerate(results.items()):
        ax = axes[idx]
        cm = res['confusion_matrix']
        
        # Anotações com contagem e percentual
        cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
        annot = np.empty_like(cm).astype(str)
        for i in range(2):
            for j in range(2):
                annot[i, j] = f"{cm[i, j]}\n({cm_percent[i, j]:.1f}%)"
                
        sns.heatmap(cm, annot=annot, fmt='', cmap='Blues', ax=ax, cbar=False,
                    xticklabels=class_labels, yticklabels=class_labels, annot_kws={"size": 11, "fontweight": "bold"})
        ax.set_title(f"{name}\nAcurácia: {res['accuracy_mean']*100:.1f}% | AUC: {res['auc_mean']:.3f}", 
                     fontsize=11, fontweight='bold', pad=8)
        ax.set_xlabel('Predição do Modelo', fontsize=9, fontweight='bold')
        ax.set_ylabel('Classe Real', fontsize=9, fontweight='bold')
        
    # Oculta o sexto subplot não utilizado
    axes[5].axis('off')
    
    plt.suptitle("Matrizes de Confusão Agregadas (Total de 569 Amostras / 10 Folds)", 
                 fontsize=14, fontweight='bold', y=0.99)
    plt.tight_layout()
    output_path = os.path.join(OUTPUTS_DIR, "matrizes_confusao.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Matrizes de confusão salvas em: {output_path}")

def plot_metrics_comparison_bar(df_summary):
    """Gera gráfico de barras agrupadas comparando as 4 métricas principais."""
    metric_cols = ['Acurácia (%)', 'Sensibilidade (%)', 'Especificidade (%)', 'AUC-ROC (%)']
    
    # Prepara dados
    df_plot = df_summary.set_index('Modelo')[metric_cols]
    
    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
    x = np.arange(len(df_plot.index))
    width = 0.2
    
    colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd']
    
    for idx, col in enumerate(metric_cols):
        rects = ax.bar(x + idx * width, df_plot[col], width, label=col.replace(' (%)', ''), 
                       color=colors[idx], edgecolor='black', alpha=0.85)
        # Adiciona rótulos nos topos
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f"{height:.1f}%",
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', fontsize=8, fontweight='bold')
                        
    ax.set_ylabel('Desempenho Médio (%)', fontsize=11, fontweight='bold')
    ax.set_title('Comparativo Geral de Desempenho dos Modelos de Classificação', fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(df_plot.index, fontsize=10, fontweight='bold')
    ax.set_ylim(80, 105)
    ax.legend(loc='lower right', fontsize=10, frameon=True, facecolor='white')
    ax.grid(True, linestyle='--', alpha=0.6, axis='y')
    
    output_path = os.path.join(OUTPUTS_DIR, "comparativo_metricas_barras.png")
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Gráfico de barras comparativo salvo em: {output_path}")

def generate_summary_table(results):
    """Gera tabela CSV e DataFrame consolidado com todas as métricas para o relatório."""
    records = []
    for name, res in results.items():
        tn, fp, fn, tp = res['confusion_matrix'].ravel()
        records.append({
            "Modelo": name,
            "Acurácia (%)": round(res['accuracy_mean'] * 100, 2),
            "Acurácia Desvio": round(res['accuracy_std'] * 100, 2),
            "Sensibilidade (%)": round(res['sensitivity_mean'] * 100, 2),
            "Sensibilidade Desvio": round(res['sensitivity_std'] * 100, 2),
            "Especificidade (%)": round(res['specificity_mean'] * 100, 2),
            "Especificidade Desvio": round(res['specificity_std'] * 100, 2),
            "AUC-ROC (%)": round(res['auc_mean'] * 100, 2),
            "AUC Desvio": round(res['auc_std'] * 100, 2),
            "Verdadeiros Positivos (TP)": tp,
            "Verdadeiros Negativos (TN)": tn,
            "Falsos Positivos (FP)": fp,
            "Falsos Negativos (FN)": fn
        })
    df_summary = pd.DataFrame(records)
    csv_path = os.path.join(OUTPUTS_DIR, "tabela_metricas_comparativas.csv")
    df_summary.to_csv(csv_path, index=False)
    print(f"Tabela de métricas salva em: {csv_path}")
    return df_summary

def run_classification_pipeline():
    df, X, y, features = export_and_load_data()
    print("Iniciando Pipeline de Classificação (10-Fold Cross-Validation)...")
    results = evaluate_models_kfold(X, y, n_splits=10)
    
    df_summary = generate_summary_table(results)
    plot_roc_curves(results)
    plot_confusion_matrices(results)
    plot_metrics_comparison_bar(df_summary)
    
    print("\n--- RESUMO DOS RESULTADOS (MÉDIA \u00b1 DESVIO PADRÃO) ---")
    for _, row in df_summary.iterrows():
        print(f"{row['Modelo']}:")
        print(f"  Acurácia:      {row['Acurácia (%)']}% (\u00b1 {row['Acurácia Desvio']}%)")
        print(f"  Sensibilidade: {row['Sensibilidade (%)']}% (\u00b1 {row['Sensibilidade Desvio']}%)")
        print(f"  Especificidade:{row['Especificidade (%)']}% (\u00b1 {row['Especificidade Desvio']}%)")
        print(f"  AUC-ROC:       {row['AUC-ROC (%)']}% (\u00b1 {row['AUC Desvio']}%)")
        print(f"  Matriz Confusão: TP={row['Verdadeiros Positivos (TP)']}, TN={row['Verdadeiros Negativos (TN)']}, FP={row['Falsos Positivos (FP)']}, FN={row['Falsos Negativos (FN)']}\n")
    return results, df_summary

if __name__ == "__main__":
    run_classification_pipeline()
