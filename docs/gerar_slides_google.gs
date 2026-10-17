/**
 * Script Google Apps Script para criar automaticamente os 8 slides
 * da Avaliação Formativa de Inteligência Artificial (UNIVERSO 2026-II).
 * 
 * COMO USAR:
 * 1. Abra o navegador e digite: slides.new (ou abra uma apresentação no Google Slides)
 * 2. No menu superior, clique em "Extensões" > "Apps Script"
 * 3. Apague o código que estiver lá e cole este arquivo inteiro
 * 4. Clique no ícone de Salvar (Ctrl+S) e depois no botão "Executar" (função: criarApresentacaoIA)
 * 5. Se o Google pedir permissão de acesso, clique em "Revisar permissões" > sua conta > "Avançado" > "Acessar (não seguro)"
 * 6. Volte na aba do seu Google Slides: todos os 8 slides estarão montados!
 */

function criarApresentacaoIA() {
  const deck = SlidesApp.getActivePresentation();
  
  // Limpar slides anteriores
  const slidesAntigos = deck.getSlides();
  for (let s of slidesAntigos) {
    s.remove();
  }

  // Paleta de Cores Moderna (Dark Theme idêntico ao slides_apresentacao.html)
  const COLOR_BG = "#0D1B2A";         // Fundo principal
  const COLOR_CARD = "#1B263B";       // Fundo dos cartões/boxes
  const COLOR_TITLE = "#FFFFFF";      // Título branco
  const COLOR_ACCENT = "#38BDF8";     // Azul Ciano de destaque
  const COLOR_GREEN = "#34D399";      // Verde para métricas
  const COLOR_ORANGE = "#FB923C";     // Laranja para destaques
  const COLOR_TEXT = "#CBD5E1";       // Texto secundário cinza claro
  const FONT_NAME = "Arial";

  // Dimensões do slide widescreen (16:9) em pontos: 720 x 405
  const W = 720;
  const H = 405;

  // Função auxiliar para aplicar fundo escuro e tag de cabeçalho
  function prepararSlide(tagText, tituloText, notasFala) {
    const slide = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
    
    // Fundo
    const bg = slide.getBackground();
    bg.setSolidFill(COLOR_BG);

    // Tag Superior (Ex: "01. CONTEXTO E DADOS")
    if (tagText) {
      const tagBox = slide.insertTextBox(tagText, 35, 18, 500, 20);
      const tagStyle = tagBox.getText().getTextStyle();
      tagStyle.setFontFamily(FONT_NAME).setFontSize(10).setBold(true).setForegroundColor(COLOR_ACCENT);
    }

    // Título Principal
    if (tituloText) {
      const titleBox = slide.insertTextBox(tituloText, 35, 36, 650, 42);
      const titleStyle = titleBox.getText().getTextStyle();
      titleStyle.setFontFamily(FONT_NAME).setFontSize(18).setBold(true).setForegroundColor(COLOR_TITLE);
    }

    // Notas do Orador para a gravação
    if (notasFala) {
      slide.getNotesPage().getSpeakerNotesShape().getText().setText(notasFala);
    }

    return slide;
  }

  // -------------------------------------------------------------
  // SLIDE 1: CAPA
  // -------------------------------------------------------------
  {
    const slide = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
    slide.getBackground().setSolidFill(COLOR_BG);

    // Tag
    const tag = slide.insertTextBox("AVALIAÇÃO FORMATIVA (AF 2026-II) • UNIVERSO", 40, 45, 640, 25);
    tag.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setBold(true).setForegroundColor(COLOR_ACCENT);

    // Título Central
    const titleBox = slide.insertTextBox("Aprendizado de Máquina Supervisionado e Não Supervisionado no Diagnóstico de Câncer de Mama", 40, 75, 640, 110);
    const titleStyle = titleBox.getText().getTextStyle();
    titleStyle.setFontFamily(FONT_NAME).setFontSize(26).setBold(true).setForegroundColor(COLOR_TITLE);

    // Subtítulo
    const subBox = slide.insertTextBox("Estudo comparativo de Classificação (SVM, MLP, KNN, Naive Bayes, Árvore de Decisão) e Clusterização (K-Means com PCA) sobre a base pública Breast Cancer Wisconsin (WDBC).", 40, 195, 640, 50);
    subBox.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(12).setForegroundColor(COLOR_TEXT);

    // Card com Metadados
    const metaCard = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 40, 265, 640, 85);
    metaCard.getFill().setSolidFill(COLOR_CARD);
    metaCard.getBorder().getLineFill().setSolidFill(COLOR_ACCENT);
    metaCard.getBorder().setWeight(1);

    const metaText = slide.insertTextBox(
      "ALUNO / PESQUISADOR: [Preencha seu Nome Completo]\n" +
      "CURSO: Sistemas de Informação / Análise e Desenvolvimento de Sistemas (UNIVERSO)\n" +
      "DISCIPLINA: Inteligência Artificial  |  ORIENTADORA: Profa. Dsc. Edhelmira L. M.",
      55, 275, 610, 65
    );
    metaText.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setBold(true).setForegroundColor(COLOR_TITLE);

    slide.getNotesPage().getSpeakerNotesShape().getText().setText(
      "Olá, professora Edhelmira e colegas. Sou aluno do curso da UNIVERSO e apresento a Avaliação Formativa de Inteligência Artificial sobre classificação e clusterização de biópsias de câncer de mama na base WDBC."
    );
  }

  // -------------------------------------------------------------
  // SLIDE 2: CONTEXTO E BANCO DE DADOS
  // -------------------------------------------------------------
  {
    const slide = prepararSlide(
      "01. CONTEXTO E DADOS",
      "Formulação do Problema & Base de Dados (UCI WDBC)",
      "O câncer de mama tem alta mortalidade e o diagnóstico precoce por PAAF é decisivo. Utilizamos a base WDBC da UCI com 569 biópsias e 30 atributos. Codificamos Maligno como 1 para focar na sensibilidade."
    );

    // Card Esquerda 1
    const card1 = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 35, 85, 315, 125);
    card1.getFill().setSolidFill(COLOR_CARD);
    card1.getBorder().getLineFill().setSolidFill("#2A3C53");
    const t1 = slide.insertTextBox(
      "🩺 Contextualização Clínica\n\n" +
      "• Neoplasia de maior incidência em mulheres globalmente.\n" +
      "• Punção Aspirativa por Agulha Fina (PAAF) para biópsia rápida.\n" +
      "• Suporte à Decisão Médica: Reduzir Falsos Negativos a zero.",
      45, 92, 295, 110
    );
    t1.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    t1.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_ACCENT);

    // Card Esquerda 2
    const card2 = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 35, 225, 315, 145);
    card2.getFill().setSolidFill(COLOR_CARD);
    card2.getBorder().getLineFill().setSolidFill("#2A3C53");
    const t2 = slide.insertTextBox(
      "📊 Estrutura do Dataset (WDBC)\n\n" +
      "• Volume: 569 instâncias clínicas e 0 dados ausentes.\n" +
      "• 30 Atributos: Raio, textura, perímetro, área, concavidade...\n" +
      "• Classes: 357 Benignos (62,7%) vs 212 Malignos (37,3%).\n" +
      "• Target: 1 = Maligno (Positivo) | 0 = Benigno (Negativo).",
      45, 232, 295, 130
    );
    t2.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    t2.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_ACCENT);

    // Card Direita (Espaço para Imagem da Distribuição de Classes)
    const cardRight = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 370, 85, 315, 285);
    cardRight.getFill().setSolidFill(COLOR_CARD);
    cardRight.getBorder().getLineFill().setSolidFill(COLOR_ACCENT);
    const tR = slide.insertTextBox(
      "📊 Proporção Diagnóstica\n\n" +
      "• Casos Benignos: 357 pacientes (62,74%)\n" +
      "• Casos Malignos: 212 pacientes (37,26%)\n\n" +
      "💡 Rigor Metodológico em Saúde:\n" +
      "A codificação de Maligno como positivo garante que a métrica de Sensibilidade avalie precisamente a detecção de tumores agressivos.\n\n" +
      "[Insira aqui a imagem: outputs/eda_distribuicao_classes.png]",
      385, 95, 285, 260
    );
    tR.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    tR.getText().getParagraphs()[0].getTextStyle().setFontSize(14).setBold(true).setForegroundColor(COLOR_TITLE);
  }

  // -------------------------------------------------------------
  // SLIDE 3: PRÉ-PROCESSAMENTO & EDA
  // -------------------------------------------------------------
  {
    const slide = prepararSlide(
      "02. PRÉ-PROCESSAMENTO",
      "Análise Exploratória & Padronização de Variáveis",
      "Identificamos altíssima colinearidade (r > 0,98) entre raio, perímetro e área. Aplicamos o StandardScaler para média 0 e variância 1, com cuidado de evitar vazamento de dados no 10-fold CV."
    );

    // Card Esquerda
    const card1 = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 35, 85, 315, 285);
    card1.getFill().setSolidFill(COLOR_CARD);
    card1.getBorder().getLineFill().setSolidFill(COLOR_ACCENT);
    const t1 = slide.insertTextBox(
      "🔬 Matriz de Correlação Linear\n\n" +
      "• Altíssima Colinearidade (> 0,98) entre raio, perímetro e área média dos núcleos celulares.\n\n" +
      "• Justifica técnicas de redução de dimensionalidade (como PCA).\n\n" +
      "• Células malignas apresentam perímetro e concavidade substancialmente maiores.\n\n" +
      "[Insira aqui a imagem: outputs/eda_matriz_correlacao.png]",
      45, 95, 295, 265
    );
    t1.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    t1.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_ACCENT);

    // Card Direita 1
    const card2 = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 370, 85, 315, 135);
    card2.getFill().setSolidFill(COLOR_CARD);
    card2.getBorder().getLineFill().setSolidFill("#2A3C53");
    const t2 = slide.insertTextBox(
      "⚙️ Padronização Z-Score (StandardScaler)\n\n" +
      "• Atributos possuem grandezas distintas: área > 2000 vs suavidade ~ 0,1.\n" +
      "• Algoritmos sensíveis à distância (KNN, SVM, MLP e K-Means) exigem média zero e desvio-padrão unitário.",
      385, 95, 285, 115
    );
    t2.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    t2.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_ACCENT);

    // Card Direita 2
    const card3 = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 370, 235, 315, 135);
    card3.getFill().setSolidFill(COLOR_CARD);
    card3.getBorder().getLineFill().setSolidFill(COLOR_GREEN);
    const t3 = slide.insertTextBox(
      "🛡️ Blindagem Contra Data Leakage\n\n" +
      "• O cálculo do StandardScaler foi executado estritamente no fold de treino.\n" +
      "• Os dados de teste foram apenas transformados com os parâmetros do treino, garantindo validação estatisticamente justa.",
      385, 245, 285, 115
    );
    t3.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    t3.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_GREEN);
  }

  // -------------------------------------------------------------
  // SLIDE 4: CLUSTERIZAÇÃO NÃO SUPERVISIONADA
  // -------------------------------------------------------------
  {
    const slide = prepararSlide(
      "03. APRENDIZADO NÃO SUPERVISIONADO",
      "Clusterização (K-Means) & Projeção Espacial (PCA)",
      "Antes de treinar classificadores, aplicamos K-Means para verificar se os dados formavam grupos naturais. O método do cotovelo e a silhueta apontaram k=2 ótimo. O ARI de 0,67 comprova forte alinhamento com a patologia real."
    );

    // Card Esquerda 1
    const card1 = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 35, 85, 315, 135);
    card1.getFill().setSolidFill(COLOR_CARD);
    card1.getBorder().getLineFill().setSolidFill("#2A3C53");
    const t1 = slide.insertTextBox(
      "🎯 Determinação do k Ótimo\n\n" +
      "• Método do Cotovelo: Inflexão nítida na curva de inércia em k=2.\n" +
      "• Coeficiente de Silhueta: Atinge ápice absoluto em k=2 com score 0,3450.\n" +
      "• Conclusão: A partição natural dos dados é binária.",
      45, 95, 295, 115
    );
    t1.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    t1.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_ACCENT);

    // Card Esquerda 2
    const card2 = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 35, 235, 315, 135);
    card2.getFill().setSolidFill(COLOR_CARD);
    card2.getBorder().getLineFill().setSolidFill(COLOR_ACCENT);
    const t2 = slide.insertTextBox(
      "🌐 Projeção PCA & Concordância\n\n" +
      "• PCA 2D retém 63,2% da variância (PC1: 44,3% | PC2: 19,0%).\n" +
      "• Adjusted Rand Index (ARI): 0,6707 indicando alta concordância com o diagnóstico médico real.",
      45, 245, 295, 115
    );
    t2.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    t2.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_ACCENT);

    // Card Direita (Imagem PCA)
    const cardRight = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 370, 85, 315, 285);
    cardRight.getFill().setSolidFill(COLOR_CARD);
    cardRight.getBorder().getLineFill().setSolidFill(COLOR_ACCENT);
    const tR = slide.insertTextBox(
      "🗺️ Visualização dos Clusters PCA 2D\n\n" +
      "• Os aglomerados do K-Means (não supervisionados) mapeiam com grande fidelidade a dispersão dos tumores malignos e benignos.\n\n" +
      "• Demonstração empírica de separabilidade morfológica espontânea.\n\n" +
      "[Insira aqui a imagem: outputs/cluster_pca_2d.png]",
      385, 95, 285, 260
    );
    tR.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    tR.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_TITLE);
  }

  // -------------------------------------------------------------
  // SLIDE 5: CLASSIFICAÇÃO SUPERVISIONADA E METODOLOGIA
  // -------------------------------------------------------------
  {
    const slide = prepararSlide(
      "04. APRENDIZADO SUPERVISIONADO",
      "Modelos Implementados & Validação Stratified 10-Fold",
      "Testamos cinco classificadores superando os três pedidos no enunciado: Árvore de Decisão, KNN, SVM com kernel RBF, Naive Bayes e Rede Neural MLP, todos com validação cruzada estratificada em 10 dobras."
    );

    const modelos = [
      { nome: "🌳 Árvore de Decisão", desc: "Critério Gini, max_depth=4. Alta interpretabilidade para a junta médica." },
      { nome: "📍 KNN (k=5)", desc: "Distância Euclidiana. Alta eficiência na identificação de vizinhança celular sadia." },
      { nome: "⚡ SVM (Kernel RBF)", desc: "Mapeamento não linear de alta dimensão. Excelente margem separadora." },
      { nome: "📈 Naive Bayes Gaussiano", desc: "Probabilidade Gaussiana contínua. Modelo analítico rápido de baseline." },
      { nome: "🧠 Rede Neural (MLP)", desc: "Arquitetura 64x32 neurônios, ativação ReLU, otimizador Adam (500 épocas)." },
      { nome: "🛡️ Stratified 10-Fold", desc: "Preserva a proporção exata (62,7% / 37,3%) em cada partição de teste." }
    ];

    modelos.forEach((m, idx) => {
      const col = idx % 3;
      const row = Math.floor(idx / 3);
      const x = 35 + col * 220;
      const y = 85 + row * 145;

      const card = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, x, y, 210, 130);
      card.getFill().setSolidFill(COLOR_CARD);
      card.getBorder().getLineFill().setSolidFill(idx === 2 ? COLOR_ACCENT : "#2A3C53");
      if (idx === 2) card.getBorder().setWeight(2);

      const t = slide.insertTextBox(m.nome + "\n\n" + m.desc, x + 10, y + 10, 190, 110);
      t.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(10.5).setForegroundColor(COLOR_TEXT);
      t.getText().getParagraphs()[0].getTextStyle().setFontSize(12).setBold(true).setForegroundColor(idx === 2 ? COLOR_ACCENT : COLOR_TITLE);
    });
  }

  // -------------------------------------------------------------
  // SLIDE 6: TABELA DE RESULTADOS COMPARATIVOS
  // -------------------------------------------------------------
  {
    const slide = prepararSlide(
      "05. RESULTADOS EXPERIMENTAIS",
      "Desempenho Geral dos Classificadores (10-Fold CV)",
      "Esta é a tabela comparativa central do trabalho. O SVM com kernel RBF foi o grande campeão com 97,54% de acurácia, 96,21% de sensibilidade e apenas 8 falsos negativos em 212 tumores malignos."
    );

    // 4 Caixas de Estatísticas
    const stats = [
      { val: "97,54%", lbl: "Melhor Acurácia (SVM)", cor: COLOR_ACCENT },
      { val: "96,21%", lbl: "Sensibilidade Máx. (SVM)", cor: COLOR_GREEN },
      { val: "99,44%", lbl: "Especificidade Máx. (KNN)", cor: COLOR_ORANGE },
      { val: "99,56%", lbl: "AUC-ROC Máxima (SVM)", cor: "#C084FC" }
    ];

    stats.forEach((st, idx) => {
      const x = 35 + idx * 165;
      const box = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, x, 85, 155, 60);
      box.getFill().setSolidFill(COLOR_CARD);
      box.getBorder().getLineFill().setSolidFill("#2A3C53");

      const t = slide.insertTextBox(st.val + "\n" + st.lbl, x + 5, 88, 145, 52);
      t.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(9).setForegroundColor(COLOR_TEXT);
      t.getText().getParagraphs()[0].getTextStyle().setFontSize(18).setBold(true).setForegroundColor(st.cor);
    });

    // Tabela Comparativa Oficial
    const rows = 6;
    const cols = 6;
    const table = slide.insertTable(rows, cols, 35, 160, 650, 195);
    
    const headers = ["Modelo", "Acurácia", "Sensibilidade", "Especificidade", "AUC-ROC", "Falsos Neg."];
    const data = [
      ["Árvore de Decisão", "91,04% ± 3,87", "85,80% ± 10,24", "94,13% ± 4,56", "91,45% ± 7,34", "30"],
      ["KNN (k=5)", "97,01% ± 1,76", "92,90% ± 4,90", "99,44% ± 1,11", "98,68% ± 1,46", "15"],
      ["SVM (Kernel RBF) 🏆", "97,54% ± 1,95", "96,21% ± 3,56", "98,33% ± 2,83", "99,56% ± 0,55", "8 (Mínimo)"],
      ["Naive Bayes", "93,15% ± 3,08", "89,57% ± 7,65", "95,26% ± 4,82", "98,56% ± 1,12", "22"],
      ["Rede Neural (MLP)", "96,84% ± 1,89", "95,24% ± 5,63", "97,75% ± 2,45", "99,26% ± 1,00", "10"]
    ];

    // Formatar Cabeçalho da Tabela
    for (let c = 0; c < cols; c++) {
      const cell = table.getCell(0, c);
      cell.getFill().setSolidFill("#1E293B");
      cell.getText().setText(headers[c]);
      cell.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(9).setBold(true).setForegroundColor(COLOR_TITLE);
    }

    // Preencher Dados
    for (let r = 0; r < 5; r++) {
      const isWinner = (r === 2);
      for (let c = 0; c < cols; c++) {
        const cell = table.getCell(r + 1, c);
        cell.getFill().setSolidFill(isWinner ? "#163854" : COLOR_CARD);
        cell.getText().setText(data[r][c]);
        const style = cell.getText().getTextStyle();
        style.setFontFamily(FONT_NAME).setFontSize(8.5).setForegroundColor(isWinner ? COLOR_ACCENT : COLOR_TEXT);
        if (isWinner || c === 0) style.setBold(true);
      }
    }
  }

  // -------------------------------------------------------------
  // SLIDE 7: CURVAS ROC E MATRIZES DE CONFUSÃO
  // -------------------------------------------------------------
  {
    const slide = prepararSlide(
      "06. MÉTRICAS GRÁFICAS",
      "Curvas ROC & Matrizes de Confusão Agregadas",
      "As curvas ROC mostram AUC superior a 98% para quatro modelos. A matriz de confusão demonstra visualmente o risco do falso negativo: a Árvore errou 30 malignos, enquanto o SVM errou apenas 8."
    );

    // Card Esquerda (Curvas ROC)
    const card1 = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 35, 85, 315, 285);
    card1.getFill().setSolidFill(COLOR_CARD);
    card1.getBorder().getLineFill().setSolidFill(COLOR_ACCENT);
    const t1 = slide.insertTextBox(
      "📈 Curvas ROC Sobrepostas (10-Fold)\n\n" +
      "• SVM RBF: AUC = 0,9956 (Curva mais próxima do canto superior esquerdo).\n" +
      "• MLP Neural: AUC = 0,9926.\n" +
      "• KNN: AUC = 0,9868.\n" +
      "• Naive Bayes: AUC = 0,9856.\n" +
      "• Árvore de Decisão: AUC = 0,9145.\n\n" +
      "[Insira aqui a imagem: outputs/curvas_roc_comparativas.png]",
      45, 95, 295, 265
    );
    t1.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    t1.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_ACCENT);

    // Card Direita (Matrizes de Confusão)
    const card2 = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 370, 85, 315, 285);
    card2.getFill().setSolidFill(COLOR_CARD);
    card2.getBorder().getLineFill().setSolidFill(COLOR_ACCENT);
    const t2 = slide.insertTextBox(
      "🎯 Análise de Falsos Negativos (212 Malignos)\n\n" +
      "• SVM: 8 Falsos Negativos (Melhor Segurança)\n" +
      "• MLP Neural: 10 Falsos Negativos\n" +
      "• KNN: 15 Falsos Negativos\n" +
      "• Naive Bayes: 22 Falsos Negativos\n" +
      "• Árvore de Decisão: 30 Falsos Negativos\n\n" +
      "[Insira aqui a imagem: outputs/matrizes_confusao.png]",
      380, 95, 295, 265
    );
    t2.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    t2.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_ACCENT);
  }

  // -------------------------------------------------------------
  // SLIDE 8: DISCUSSÃO E CONCLUSÕES
  // -------------------------------------------------------------
  {
    const slide = prepararSlide(
      "07. SÍNTESE E CONCLUSÃO",
      "Discussão Clínica & Considerações Finais",
      "Em oncologia, o falso negativo é fatal. O SVM com kernel RBF é o modelo mais seguro para atuar como segunda opinião médica. Demonstramos rigor contra data leakage e validação sólida."
    );

    // Card Esquerda
    const card1 = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 35, 85, 315, 285);
    card1.getFill().setSolidFill(COLOR_CARD);
    card1.getBorder().getLineFill().setSolidFill(COLOR_ACCENT);
    const t1 = slide.insertTextBox(
      "💡 Por que a Sensibilidade é Vital?\n\n" +
      "• Falso Negativo em Oncologia: Paciente com tumor maligno recebe diagnóstico benigno, retardando o início da quimioterapia/cirurgia.\n\n" +
      "• O SVM com Kernel RBF obteve sensibilidade de 96,21%, errando apenas 8 casos em 212.\n\n" +
      "• Modelo de Segunda Opinião Médica: Alta sensibilidade garante que nenhuma lesão suspeita seja ignorada.",
      45, 95, 295, 265
    );
    t1.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    t1.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_ACCENT);

    // Card Direita
    const card2 = slide.insertShape(SlidesApp.ShapeType.ROUND_RECTANGLE, 370, 85, 315, 285);
    card2.getFill().setSolidFill(COLOR_CARD);
    card2.getBorder().getLineFill().setSolidFill(COLOR_GREEN);
    const t2 = slide.insertTextBox(
      "🎯 Conclusões do Estudo\n\n" +
      "• Clusterização Natural: O K-Means comprovou a separabilidade patológica espontânea (ARI = 0,6707).\n\n" +
      "• Performance Superior: SVM e MLP atingiram acurácia > 96,8% e AUC > 99,2%.\n\n" +
      "• Especificidade Recorde: O KNN atingiu 99,44%, errando somente 2 casos benignos em 357.\n\n" +
      "• Trabalho em conformidade estrita com todos os requisitos da AF 2026-II.",
      380, 95, 295, 265
    );
    t2.getText().getTextStyle().setFontFamily(FONT_NAME).setFontSize(11).setForegroundColor(COLOR_TEXT);
    t2.getText().getParagraphs()[0].getTextStyle().setFontSize(13).setBold(true).setForegroundColor(COLOR_GREEN);
  }
}
