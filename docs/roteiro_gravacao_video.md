# Roteiro Completo para Gravação do Vídeo de Apresentação (AF 2026-II)

> **Atenção às Regras Oficiais do Enunciado:**
> - É **obrigatório mostrar o seu rosto** durante toda a gravação (webcam visível no canto ou lado da tela).
> - **Não utilize voz sintética por IA ou leitores automáticos** (o enunciado atribui nota ZERO em caso de detecção).
> - Você deve falar naturalmente. Este roteiro traz as falas prontas, divididas slide por slide, com marcações de tempo e dicas de postura.
> - **Tempo estimado total:** 5 a 7 minutos.

---

## 🛠️ Como Preparar a Gravação Facilmente

1. **Ferramenta de Gravação Recomendada:**
   - **OBS Studio** (gratuito) OU **Loom** (grava tela + webcam no círculo) OU gravador nativo do Windows (**Clipchamp** / **PowerPoint**) OU abra uma reunião sozinho no **Google Meet** e grave a tela com sua câmera ligada.
2. **Abra os Slides:**
   - Dê um duplo clique no arquivo [`docs/slides_apresentacao.html`](file:///c:/ProjetosLocais/Universo/inteligencia_artificial/docs/slides_apresentacao.html) no seu navegador (Chrome, Edge, etc.).
   - Pressione a tecla **F** para colocar em tela cheia.
   - Use as setas do teclado (← e →) para passar os slides.
3. **Posicione a Câmera:**
   - Posicione sua webcam no canto superior ou inferior direito, garantindo boa iluminação no seu rosto.
   - Respire fundo, mantenha um tom de voz firme, acadêmico e confiante.

---

## 🎙️ Roteiro Passo a Passo (Falas Slide por Slide)

---

### 🟢 SLIDE 1: Capa e Identificação
*(Tempo estimado: ~35 segundos)*

**Ação:** Olhe para a webcam, sorria e inicie a apresentação com clareza.

> *"Olá, professora Edhelmira e colegas. Meu nome é **[Fale o seu nome completo]**, sou aluno do curso de **[Sistemas de Informação / Análise e Desenvolvimento de Sistemas]** da Universidade Salgado de Oliveira (UNIVERSO).*
>
> *Hoje apresento a minha Avaliação Formativa da disciplina de **Inteligência Artificial**, referente ao semestre 2026-II.*
>
> *O tema do meu projeto é a **'Aplicação de Técnicas de Aprendizado de Máquina Supervisionado e Não Supervisionado no Diagnóstico de Câncer de Mama'**, utilizando a base de dados pública Breast Cancer Wisconsin Diagnostic do repositório UCI.*
>
> *Vamos ao detalhamento metodológico e aos resultados obtidos."*

*(Aperte a seta para a direita para mudar para o Slide 2)*

---

### 🟢 SLIDE 2: Formulação do Problema & Base de Dados
*(Tempo estimado: ~50 segundos)*

**Ação:** Gesticule em direção ao slide mostrando os números do dataset.

> *"O câncer de mama é uma das principais causas de mortalidade feminina no mundo, e o diagnóstico precoce é o fator decisivo para elevar as taxas de cura. Quando uma paciente apresenta uma lesão mamária, realiza-se a Punção Aspirativa por Agulha Fina (PAAF), cujas imagens celulares microscópicas servem para diferenciar tumores benignos de malignos.*
>
> *Para este estudo, selecionei o banco de dados público **Breast Cancer Wisconsin Diagnostic (WDBC)**, mantido na Universidade da Califórnia em Irvine (UCI).*
>
> *A base possui **569 instâncias clínicas** e **30 atributos morfológicos contínuos**, sem nenhum dado faltante. Entre as amostras, temos **357 casos benignos** (cerca de 62,7%) e **212 casos malignos** (37,3%).*
>
> *Um ponto metodológico fundamental que adotei foi codificar o diagnóstico Maligno como a classe positiva (1) e Benigno como a classe negativa (0). Dessa forma, a métrica de Sensibilidade reflete a capacidade exata do algoritmo de detectar o tumor maligno, que é o evento clínico crítico."*

*(Mude para o Slide 3)*

---

### 🟢 SLIDE 3: Pré-Processamento & Análise Exploratória (EDA)
*(Tempo estimado: ~55 segundos)*

**Ação:** Aponte para a matriz de correlação no slide.

> *"Na fase de pré-processamento, realizei uma análise exploratória minuciosa. Como podemos observar na matriz de correlação de Pearson, existem fortes correlações lineares — muitas superiores a 0,98 — entre raio, perímetro e área dos núcleos celulares, o que evidencia colinearidade e justifica o uso de técnicas de redução de dimensionalidade.*
>
> *Além disso, os atributos originais possuem escalas numéricas muito discrepantes: a área atinge valores na casa de milhares, enquanto a suavidade fica em frações decimais. Por isso, apliquei a padronização por Z-score com o **StandardScaler**, trazendo todos os atributos para média zero e desvio-padrão unitário.*
>
> *Destaco um cuidado metodológico essencial: para evitar o chamado **data leakage** (ou vazamento de dados), o cálculo de escalonamento foi realizado estritamente dentro de cada dobra de treinamento da validação cruzada, sem nunca utilizar informações do conjunto de teste."*

*(Mude para o Slide 4)*

---

### 🟢 SLIDE 4: Clusterização Não Supervisionada (K-Means & PCA)
*(Tempo estimado: ~50 segundos)*

**Ação:** Mostre o gráfico de comparação entre clusters e as classes reais.

> *"Antes de treinar modelos supervisionados, apliquei técnicas de aprendizado não supervisionado para verificar se os atributos celulares formam agrupamentos naturais congruentes com a patologia real.*
>
> *Utilizei o algoritmo **K-Means** e investiguei o número ideal de clusters através do **Método do Cotovelo** e do **Coeficiente Médio de Silhueta**, variando k de 2 a 10. O teste indicou unanimemente que **k=2** é a partição ótima, com o maior score de silhueta (0,3450).*
>
> *Para visualização, realizei uma redução dimensional via **PCA**, onde as duas primeiras componentes explicam 63,2% da variância total dos dados. Como vemos no gráfico lado a lado, os agrupamentos descobertos pelo K-Means coincidem fortemente com os diagnósticos médicos reais, atingindo um **Adjusted Rand Index (ARI) de 0,6707**. Isso comprova que a morfologia celular possui uma separabilidade patológica espontânea no espaço latente."*

*(Mude para o Slide 5)*

---

### 🟢 SLIDE 5: Classificação Supervisionada & Validação 10-Fold
*(Tempo estimado: ~55 segundos)*

**Ação:** Olhe para a câmera e cite os 5 modelos com segurança.

> *"Na etapa de aprendizado supervisionado, implementei e comparei **cinco algoritmos de classificação**, superando o mínimo de três exigido no enunciado:*
>
> 1. *A **Árvore de Decisão**, configurada com critério de Gini e profundidade máxima 4 para prover alta interpretabilidade médica sem sobreajuste;*
> 2. *O **K-Nearest Neighbors (KNN)** com 5 vizinhos e métrica euclidiana;*
> 3. *O **Support Vector Machine (SVM)** com kernel de Base Radial Gaussiana (RBF) e regularização C=1,0;*
> 4. *O **Naive Bayes Gaussiano**, como baseline probabilístico rápido;*
> 5. *E uma **Rede Neural Artificial do tipo MLP**, com duas camadas ocultas de 64 e 32 neurônios e ativação ReLU.*
>
> *Para garantir rigor científico, todos os modelos foram submetidos a uma **validação cruzada estratificada em 10 dobras (Stratified 10-Fold Cross-Validation)**, preservando a proporção de classes em cada partição e eliminando qualquer dependência de divisões aleatórias únicas."*

*(Mude para o Slide 6)*

---

### 🟢 SLIDE 6: Resultados Comparativos e Métricas
*(Tempo estimado: ~65 segundos)*

**Ação:** Destaque os números do SVM e do KNN na tabela.

> *"Neste slide temos o quadro comparativo consolidado das métricas de desempenho avaliadas em 10 folds.*
>
> *O algoritmo **Support Vector Machine (SVM com kernel RBF)** alcançou o desempenho superior geral, conquistando **97,54% de acurácia média**, a mais alta **sensibilidade com 96,21%**, e uma impressionante **AUC-ROC de 99,56%**.*
>
> *A **Rede Neural MLP** obteve resultados muito próximos, com **96,84% de acurácia** e **95,24% de sensibilidade**.*
>
> *Um destaque muito importante vai para o **KNN**, que obteve a maior **especificidade** de todo o experimento, atingindo **99,44%**. Ele cometeu apenas dois falsos positivos em todo o conjunto de 357 casos benignos.*
>
> *O Naive Bayes obteve 93,15% de acurácia e a Árvore de Decisão 91,04%, servindo esta última como um excelente modelo de regras explícitas para auditoria clínica."*

*(Mude para o Slide 7)*

---

### 🟢 SLIDE 7: Curvas ROC & Matrizes de Confusão Agregadas
*(Tempo estimado: ~50 segundos)*

**Ação:** Aponte para as curvas ROC e a matriz de confusão do SVM.

> *"Visualizando graficamente: à esquerda temos a sobreposição das **Curvas ROC**. Quanto mais próxima a curva se situa do canto superior esquerdo, maior a capacidade de discriminação do modelo. O SVM e a Rede Neural destacam-se com áreas sob a curva praticamente perfeitas, superiores a 99%.*
>
> *À direita, apresento as **Matrizes de Confusão agregadas** com as 569 amostras de teste. Observem que o SVM cometeu apenas **8 falsos negativos** em 212 pacientes com neoplasia maligna, enquanto a Árvore de Decisão gerou 30 e o KNN gerou 15 falsos negativos.*
>
> *Essa diferença é crucial, como discutiremos a seguir."*

*(Mude para o Slide 8)*

---

### 🟢 SLIDE 8: Discussão Clínica & Conclusões
*(Tempo estimado: ~60 segundos)*

**Ação:** Olhe diretamente para a webcam com tom conclusivo e profissional.

> *"Para concluir, precisamos interpretar esses resultados sob a perspectiva médica real. Em oncologia, o custo de um **Falso Negativo** — isto é, dizer a uma paciente com câncer que o tumor é benigno — é trágico, pois atrasa o início da quimioterapia ou cirurgia e coloca sua vida em risco. Por outro lado, um Falso Positivo acarreta apenas a realização de uma nova biópsia confirmatória.*
>
> *Portanto, a métrica clínica mandatória é a **Sensibilidade (Recall)**. E sob este critério, o **SVM com kernel RBF** demonstrou ser o classificador mais seguro e eficaz, com 96,21% de sensibilidade e o menor número absoluto de falsos negativos.*
>
> *O trabalho cumpriu rigorosamente todas as etapas propostas: carregamento, análise exploratória, clusterização não supervisionada, modelagem supervisionada com 5 algoritmos, validação cruzada estratificada e confecção do relatório técnico no template da Universo.*
>
> *Agradeço à professora Edhelmira pela proposta deste projeto prático e me coloco à disposição para esclarecimentos. Muito obrigado!"*

**Fim da gravação!** Pare a gravação, revise o vídeo e envie o link conforme as instruções abaixo.

---

## 📋 Checklist Final para a Gravação

- [ ] Meu rosto aparece com clareza na câmera durante todo o vídeo?
- [ ] O áudio está limpo e sem eco ou ruído excessivo?
- [ ] Os slides estão nítidos e legíveis na gravação da tela?
- [ ] O vídeo tem entre 5 e 8 minutos de duração?
- [ ] O link foi compartilhado no Google Drive ou YouTube como "Não listado" com acesso público/aberto para a professora poder assistir sem solicitar permissão?
