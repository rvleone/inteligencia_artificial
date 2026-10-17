# Avaliação Formativa (AF) - Inteligência Artificial (2026-II)

**Universidade Salgado de Oliveira (UNIVERSO)**  
**Cursos:** Sistemas de Informação / Análise e Desenvolvimento de Sistemas  
**Disciplina:** Inteligência Artificial  
**Docente:** Profa. Dsc. Edhelmira L. M.  
**Prazo de Envio:** Até 14/11 via AVA (Pontuação: 2,0 pontos)

---

## 📌 Visão Geral do Projeto

Este projeto desenvolve a **Avaliação Formativa (AF)** aplicando técnicas de aprendizado de máquina supervisionado e não supervisionado sobre o banco de dados público **Breast Cancer Wisconsin (Diagnostic) - WDBC** do repositório UCI.

O trabalho contempla:
1. **Análise Exploratória de Dados (EDA):** Distribuição de classes, frequências relativas, matriz de correlação linear de Pearson e distribuições de densidade celular.
2. **Clusterização Não Supervisionada:** Aplicação do algoritmo **K-Means**, determinação do número ideal de agrupamentos via **Método do Cotovelo** e **Coeficiente de Silhueta**, além de projeções espaciais em **2D e 3D por PCA**.
3. **Classificação Supervisionada:** Implementação e avaliação rigorosa de **5 algoritmos** (Árvore de Decisão, KNN, SVM com kernel RBF, Naive Bayes Gaussiano e Rede Neural MLP) sob protocolo de **Stratified 10-Fold Cross-Validation**.
4. **Métricas Obrigatórias:** Acurácia, Sensibilidade (Recall do tumor maligno), Especificidade, Área sob a Curva ROC (AUC) e Matriz de Confusão agregada.
5. **Relatório Técnico em DOCX e PDF:** Construído a partir do template oficial da instituição (`Template_relatorioIA_AF.docx`).
6. **Material de Apresentação:** Slide deck interativo em HTML5 e roteiro falado passo a passo para a gravação de vídeo obrigatória do aluno com webcam ligada.

---

## 🏆 Resumo dos Resultados Experimentais (10-Fold Cross-Validation)

| Modelo | Acurácia (%) | Sensibilidade (%) | Especificidade (%) | AUC-ROC (%) | Falsos Negativos (FN) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Árvore de Decisão** | 91,04 ± 3,87 | 85,80 ± 10,24 | 94,13 ± 4,56 | 91,45 ± 7,34 | 30 |
| **K-Nearest Neighbors (KNN)** | 97,01 ± 1,76 | 92,90 ± 4,90 | **99,44 ± 1,11** | 98,68 ± 1,46 | 15 |
| **Support Vector Machine (SVM)** 🏆 | **97,54 ± 1,95** | **96,21 ± 3,56** | 98,33 ± 2,83 | **99,56 ± 0,55** | **8** |
| **Naive Bayes Gaussiano** | 93,15 ± 3,08 | 89,57 ± 7,65 | 95,26 ± 4,82 | 98,56 ± 1,12 | 22 |
| **Rede Neural (MLP)** | 96,84 ± 1,89 | 95,24 ± 5,63 | 97,75 ± 2,45 | 99,26 ± 1,00 | 10 |

> **Destaque Clínico:** O **SVM com kernel RBF** obteve a maior sensibilidade (96,21%) e o menor número absoluto de falsos negativos (apenas 8 em 212 pacientes com neoplasia maligna), consolidando-se como o classificador mais seguro e eficaz para suporte à decisão médica.

---

## 📁 Estrutura de Diretórios e Arquivos

```
inteligencia_artificial/
│
├── AF_InteligenciaArtificial_2026-II.pdf    # Enunciado oficial da atividade
├── Template_relatorioIA_AF.docx             # Template institucional da Universo fornecido
├── main.py                                  # Script mestre que roda todo o pipeline
├── requirements.txt                         # Dependências do projeto
├── links_e_entrega.txt                      # Modelo formatado para envio dos links no AVA
├── README.md                                # Este documento
│
├── data/                                    # Base de dados
│   └── breast_cancer_wisconsin.csv          # Dataset completo exportado em CSV
│
├── src/                                     # Código-fonte modular Python
│   ├── data_loader.py                       # Carga e pré-processamento dos dados
│   ├── eda.py                               # Geração de gráficos exploratórios
│   ├── clustering.py                        # K-Means, silhueta, cotovelo e PCA 2D/3D
│   └── classification.py                    # 5 classificadores com 10-Fold e métricas
│
├── notebooks/                               # Notebook interativo
│   └── AF_Inteligencia_Artificial.ipynb     # Pronto para Google Colab ou VS Code
│
├── outputs/                                 # Gráficos em alta resolução (300 DPI)
│   ├── eda_distribuicao_classes.png
│   ├── eda_matriz_correlacao.png
│   ├── eda_distribuicoes_atributos.png
│   ├── eda_boxplots.png
│   ├── cluster_elbow_silhouette.png
│   ├── cluster_pca_2d.png
│   ├── cluster_pca_3d.png
│   ├── curvas_roc_comparativas.png
│   ├── matrizes_confusao.png
│   ├── comparativo_metricas_barras.png
│   └── tabela_metricas_comparativas.csv
│
└── docs/                                    # Documentação acadêmica e apresentação
    ├── Relatorio_AF_Inteligencia_Artificial.docx # Relatório no template oficial do Word
    ├── Relatorio_AF_Inteligencia_Artificial.pdf  # Relatório compilado pronto para envio
    ├── slides_apresentacao.html                 # Slides interativos em HTML5
    └── roteiro_gravacao_video.md                # Roteiro com falas prontas para gravar o vídeo
```

---

## 🚀 Como Executar o Projeto

### 1. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 2. Executar o pipeline completo
```bash
python main.py
```

### 3. Abrir o Jupyter Notebook
```bash
jupyter notebook notebooks/AF_Inteligencia_Artificial.ipynb
```
*(Ou abra diretamente no VS Code com a extensão Python/Jupyter ou importe no Google Colab)*

### 4. Apresentação dos Slides
Dê um duplo clique em `docs/slides_apresentacao.html` para abrir os slides no navegador.
- Pressione **F** para tela cheia.
- Use as teclas **←** e **→** ou **Espaço** para navegar entre os slides.

---

## 🎓 Instruções para Postagem no AVA

Para obter a pontuação máxima (2,0 pontos), siga os passos:
1. **Preencher os dados do aluno:** Abra `docs/Relatorio_AF_Inteligencia_Artificial.docx` e `docs/Relatorio_AF_Inteligencia_Artificial.pdf` e insira seu nome completo e matrícula.
2. **Gravar o vídeo da apresentação:**
   - Utilize o roteiro em `docs/roteiro_gravacao_video.md`.
   - Lembre-se de **mostrar o seu rosto** na câmera durante a gravação.
   - Faça o upload do vídeo no Google Drive (como "Qualquer pessoa com o link pode visualizar") ou no YouTube (como "Não listado").
3. **Subir o código para o GitHub:** Crie um repositório público no seu GitHub e suba os arquivos do projeto.
4. **Preencher `links_e_entrega.txt`:** Cole os links do vídeo e do GitHub.
5. **Enviar no AVA:** Anexe o relatório em PDF, o arquivo `links_e_entrega.txt` e o arquivo do dataset (`breast_cancer_wisconsin.csv`).
