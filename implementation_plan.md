# Plano de Implementação - Avaliação Formativa de Inteligência Artificial (2026-II)

Projeto acadêmico para a disciplina de **Inteligência Artificial** (Cursos: Sistemas de Informação / Análise e Desenvolvimento de Sistemas - Universo EAD, Profa. Dsc. Edhelmira L. M.).

---

## 1. Visão Geral e Entendimento dos Requisitos

O trabalho solicita a aplicação prática de técnicas de aprendizado de máquina em problemas de **classificação supervisionada** e **clusterização não supervisionada**, utilizando um banco de dados público, com as seguintes obrigações:
- **Linguagem & Bibliotecas**: Python (NumPy, Pandas, Matplotlib/Seaborn, Scikit-learn).
- **Banco de Dados**: Seleção de uma base pública (Kaggle ou UCI). Recomendamos fortemente o **Breast Cancer Wisconsin (Diagnostic)** devido à sua natureza binária, atributos contínuos clínicos de alta qualidade e perfeita adequação para o cálculo das métricas exigidas (Acurácia, Sensibilidade, Especificidade, AUC-ROC e Matriz de Confusão).
- **Pré-processamento**: Análise exploratória (EDA), tratamento de valores nulos/outliers, normalização/padronização dos dados (`StandardScaler`).
- **Classificação**: Implementação de pelo menos 3 algoritmos (implementaremos 4 a 5: **Árvore de Decisão**, **KNN**, **SVM**, **Naive Bayes** e **MLP / Redes Neurais**), com justificativa técnica dos hiperparâmetros.
- **Clusterização**: Aplicação de algoritmo não supervisionado (**K-Means**) com avaliação (Elbow / Silhouette) e visualização de clusters em 2D/3D via PCA.
- **Validação Cruzada**: Uso de **k-fold cross-validation** (Stratified 10-Fold).
- **Entregáveis Exigidos**:
  1. Relatório técnico em PDF completo (Introdução, Metodologia, Resultados, Discussão, Conclusões).
  2. Notebook executável (`.ipynb`) compatível com Google Colab e VS Code, além de scripts modulares em Python.
  3. Gráficos em alta resolução salvos como figuras (distribuição, correlação, matrizes de confusão, curvas ROC, projeção dos clusters).
  4. Apresentação em slides e **roteiro detalhado de gravação** para o vídeo obrigatório do aluno (mostrando o rosto).
  5. Arquivo `links_e_entrega.txt` formatado para envio no AVA.

---

## 2. Decisões de Arquitetura e Estrutura do Projeto

Propomos a seguinte estrutura organizada no workspace `c:\ProjetosLocais\Universo\inteligencia_artificial`:

```
inteligencia_artificial/
│
├── AF_InteligenciaArtificial_2026-II.pdf    # Enunciado oficial copiado para referência
├── requirements.txt                         # Dependências do projeto (numpy, pandas, scikit-learn, etc.)
├── README.md                                # Documentação completa do projeto e instruções de execução
├── links_e_entrega.txt                      # Modelo pronto para preenchimento dos links e submissão no AVA
│
├── data/                                    # Armazenamento do dataset
│   └── breast_cancer_wisconsin.csv          # Base de dados em CSV
│
├── outputs/                                 # Gráficos e resultados exportados
│   ├── eda_distribuicao_classes.png
│   ├── eda_matriz_correlacao.png
│   ├── eda_boxplots.png
│   ├── cluster_elbow_silhouette.png
│   ├── cluster_pca_2d.png
│   ├── cluster_pca_3d.png
│   ├── matrizes_confusao.png
│   ├── curvas_roc_comparativas.png
│   └── tabela_metricas_comparativas.csv
│
├── src/                                     # Código modular Python
│   ├── __init__.py
│   ├── data_loader.py                       # Carregamento e pré-processamento
│   ├── eda.py                               # Geração de gráficos exploratórios
│   ├── clustering.py                        # K-Means e redução de dimensionalidade (PCA)
│   ├── classification.py                    # Treinamento com K-Fold e cálculo de métricas
│   └── utils_metrics.py                     # Cálculo de Sensibilidade, Especificidade, AUC, Matriz Confusão
│
├── notebooks/                               # Notebook interativo formatado
│   └── AF_Inteligencia_Artificial.ipynb     # Notebook comentado e pronto para rodar no Google Colab ou localmente
│
└── docs/                                    # Documentação de entrega e apresentação
    ├── relatorio_tecnico.md                 # Conteúdo do relatório acadêmico formatado
    ├── relatorio_tecnico.pdf                # Relatório acadêmico compilado em PDF
    ├── slides_apresentacao.html / .md       # Slides para apoio visual da gravação
    └── roteiro_gravacao_video.md            # Roteiro passo a passo com falas prontas para o aluno gravar o vídeo
```

---

## 3. User Review Required

> [!IMPORTANT]
> **Confirmação do Banco de Dados**:
> Sugerimos utilizar o **Breast Cancer Wisconsin Diagnostic (WDBC)** pela robustez clínica e matemática para cálculo de sensibilidade e especificidade. Caso você prefira **Heart Disease** ou **Wine**, podemos adotar o outro dataset sem problemas.
>
> **Template do Relatório**:
> O enunciado menciona um arquivo chamado `Template_relatorioIA_AF` disponível no AVA. Se você tiver esse arquivo de modelo (Word ou PDF), podemos baixá-lo ou reproduzir exatamente as seções e formatação exigidas pela professora. Caso contrário, estruturaremos segundo o padrão acadêmico rigoroso da ABNT/SBC com as seções obrigatórias especificadas no PDF.

---

## 4. Open Questions

1. Você já baixou o arquivo `Template_relatorioIA_AF` do AVA para seu computador ou Google Drive? Se sim, em qual pasta ele está? (Se não tiver, construiremos a estrutura padrão completa solicitada no enunciado).
2. Você concorda com a escolha do dataset **Breast Cancer Wisconsin** (ou prefere **Heart Disease**)?

---

## 5. Plano de Ação Passo a Passo

### Fase 1: Ambiente e Extração de Dados
- Instalar dependências no ambiente Python (`numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `fpdf2`).
- Criar script para exportar o dataset para `data/breast_cancer_wisconsin.csv` com nomes de atributos claros em português e inglês.

### Fase 2: Análise Exploratória e Pré-Processamento
- Inspecionar dimensões, tipos de dados, dados faltantes e proporção de classes.
- Gerar gráficos de EDA e salvar em `outputs/`:
  - Distribuição das classes (benigno vs maligno).
  - Mapa de calor de correlação de Pearson.
  - Distribuições das variáveis mais relevantes.
- Aplicar `StandardScaler` para normalização necessária aos modelos baseados em distância (KNN, SVM, MLP, K-Means).

### Fase 3: Clusterização (K-Means + PCA)
- Avaliar número de clusters usando Método do Cotovelo (Inertia) e Coeficiente de Silhueta para $k \in [2, 10]$.
- Executar K-Means com $k=2$ e avaliar concordância com as classes reais.
- Projetar os clusters em 2D e 3D utilizando Análise de Componentes Principais (PCA) e salvar as figuras.

### Fase 4: Classificação e Validação Cruzada (K-Fold)
- Implementar 5 classificadores:
  1. **Árvore de Decisão** (`max_depth`, `criterion='gini'`)
  2. **K-Nearest Neighbors** (`n_neighbors=5`, métrica euclidiana)
  3. **Support Vector Machine** (`kernel='rbf'`, `C=1.0`, `probability=True`)
  4. **Naive Bayes** (`GaussianNB`)
  5. **Rede Neural MLP** (`hidden_layer_sizes=(64, 32)`, `activation='relu'`, `max_iter=500`)
- Configurar `StratifiedKFold(n_splits=10, shuffle=True, random_state=42)`.
- Coletar e calcular para cada modelo:
  - **Acurácia média e desvio padrão**
  - **Sensibilidade (Recall)**: $TP / (TP + FN)$
  - **Especificidade**: $TN / (TN + FP)$
  - **AUC-ROC**: Área sob a curva ROC
  - **Matriz de Confusão agregada**
- Salvar gráfico comparativo das curvas ROC e matrizes de confusão em `outputs/`.

### Fase 5: Criação do Jupyter Notebook e Script Modular
- Montar o arquivo `AF_Inteligencia_Artificial.ipynb` com células de texto ricas em Markdown, explicações conceituais e código executável de ponta a ponta.
- Garantir botão "Open in Colab" para que você possa rodar na nuvem se desejar.

### Fase 6: Relatório Acadêmico em PDF e Material de Apresentação
- Redigir o relatório técnico acadêmico cobrindo:
  - Capa e identificação
  - 1. Introdução e Contextualização do Problema
  - 2. Metodologia (Base de Dados, Pré-processamento, Algoritmos, Hiperparâmetros, Validação Cruzada)
  - 3. Resultados e Gráficos (EDA, Clusterização, Tabela de Métricas, Curvas ROC, Matrizes de Confusão)
  - 4. Discussão Crítica Comparativa
  - 5. Conclusões e Trabalhos Futuros
  - 6. Referências Bibliográficas
- Gerar o arquivo PDF profissional do relatório pronto para submissão.
- Criar roteiro de gravação em vídeo (script pronto de 5 a 10 minutos para você ler e apresentar naturalmente na gravação de webcam).
- Gerar slides visuais da apresentação para você exibir durante a gravação.
- Preencher o arquivo `links_e_entrega.txt` com o roteiro de instruções de postagem no AVA.

---

## 6. Plano de Verificação

### Verificação Automatizada
- Executar os scripts Python gerados e verificar se todas as métricas são calculadas sem erros.
- Checar se todos os gráficos em `outputs/` foram gerados corretamente em formato PNG de alta resolução.
- Executar o notebook do início ao fim validando o kernel sem warnings ou erros de runtime.

### Verificação Manual
- Validar se todas as 5 métricas exigidas pelo PDF estão presentes no relatório.
- Conferir se os critérios da professora (Clareza do relatório 20%, Pré-processamento 15%, Implementação 25%, Justificativa e métricas 20%, Apresentação 20%) foram atendidos com nota máxima (100%).
