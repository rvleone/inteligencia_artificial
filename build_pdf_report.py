"""
Script para compilação direta do Relatório Técnico Acadêmico em PDF
Utiliza fpdf2 com fontes TrueType do sistema (Arial) para suporte total a Unicode e acentuação da Língua Portuguesa.
"""

import os
from fpdf import FPDF

OUTPUT_PDF = os.path.join(os.path.dirname(__file__), "docs", "Relatorio_AF_Inteligencia_Artificial.pdf")
OUTPUTS_DIR = os.path.join(os.path.dirname(__file__), "outputs")

class AcademicReportPDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Carrega fontes TrueType com suporte Unicode completo
        self.add_font("CustomArial", "", "C:/Windows/Fonts/arial.ttf")
        self.add_font("CustomArial", "B", "C:/Windows/Fonts/arialbd.ttf")
        self.add_font("CustomArial", "I", "C:/Windows/Fonts/ariali.ttf")

    def header(self):
        self.set_font('CustomArial', 'B', 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, 'UNIVERSIDADE SALGADO DE OLIVEIRA (UNIVERSO) | REVISTA PESQUISA & EDUCAÇÃO A DISTÂNCIA', align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_font('CustomArial', 'I', 7)
        self.cell(0, 4, 'Avaliação Formativa (AF) - Semestre 2026-II | Disciplina: Inteligência Artificial | Profa. Dsc. Edhelmira L. M.', align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_draw_color(200, 200, 200)
        self.line(self.l_margin, self.get_y() + 2, self.w - self.r_margin, self.get_y() + 2)
        self.ln(6)

    def footer(self):
        self.set_y(-12)
        self.set_draw_color(200, 200, 200)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.set_font('CustomArial', '', 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f'Página {self.page_no()}/{{nb}}', align='R')

def build_pdf():
    pdf = AcademicReportPDF(format='A4', unit='mm')
    pdf.set_margins(left=20, top=18, right=20)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.alias_nb_pages()
    pdf.add_page()

    # Título Principal
    pdf.set_font('CustomArial', 'B', 13)
    pdf.set_text_color(27, 54, 93) # Azul Escuro Institucional (#1B365D)
    pdf.multi_cell(0, 6.5, 'APLICAÇÃO DE APRENDIZADO DE MÁQUINA SUPERVISIONADO E NÃO SUPERVISIONADO NO DIAGNÓSTICO DE CÂNCER DE MAMA (WDBC)', align='C')
    pdf.ln(2.5)

    # Identificação do Aluno e Curso
    pdf.set_font('CustomArial', 'B', 9)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 4.5, 'Aluno(a): [Preencha seu Nome Completo] | Curso: Sistemas de Informação / ADS', align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.set_font('CustomArial', 'I', 8)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 4, 'Orientadora: Profa. Dsc. Edhelmira L. M. | Universo EAD', align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(4)

    # Box do Resumo
    pdf.set_fill_color(245, 248, 252)
    pdf.set_draw_color(180, 200, 225)
    resumo_y = pdf.get_y()
    pdf.rect(pdf.l_margin, resumo_y, pdf.epw, 54, 'DF')
    pdf.set_xy(pdf.l_margin + 4, resumo_y + 2.5)
    
    pdf.set_font('CustomArial', 'B', 8.5)
    pdf.set_text_color(27, 54, 93)
    pdf.cell(0, 4, 'RESUMO', new_x='LMARGIN', new_y='NEXT')
    pdf.set_font('CustomArial', '', 7.5)
    pdf.set_text_color(30, 30, 30)
    resumo_text = (
        "Este trabalho apresenta um estudo experimental comparativo entre algoritmos de aprendizado supervisionado "
        "e não supervisionado aplicados ao diagnóstico de neoplasias mamárias, utilizando a base de dados pública "
        "Breast Cancer Wisconsin Diagnostic (WDBC - UCI). Foram avaliadas 569 observações e 30 atributos morfológicos "
        "contínuos extraídos de biópsias aspirativas por agulha fina (PAAF). Após pré-processamento e padronização Z-score, "
        "o algoritmo K-Means revelou conformidade intrínseca com os diagnósticos reais (ARI = 0,6707 e Silhueta = 0,3450 com k=2), "
        "corroborado por projeções 2D e 3D via PCA. Na classificação supervisionada, foram implementados cinco algoritmos "
        "(Árvore de Decisão, KNN, SVM com kernel RBF, Naive Bayes Gaussiano e Redes Neurais MLP) validados por Stratified 10-Fold Cross-Validation. "
        "O modelo SVM atingiu o melhor equilíbrio global com 97,54% de acurácia, 96,21% de sensibilidade (recall de maligno) e AUC de 99,56%, "
        "enquanto o KNN obteve a maior especificidade (99,44%). Os resultados consolidam os modelos como ferramentas eficazes "
        "de suporte à decisão clínica com foco na mitigação de falsos negativos."
    )
    pdf.set_x(pdf.l_margin + 4)
    pdf.multi_cell(pdf.epw - 8, 3.6, resumo_text, align='J')
    pdf.ln(1)
    pdf.set_x(pdf.l_margin + 4)
    pdf.set_font('CustomArial', 'B', 7.5)
    pdf.cell(pdf.epw - 8, 4, 'Palavras-chave: Inteligência Artificial; Classificação; Clusterização; K-Means; Support Vector Machine; Câncer de Mama.', new_x='LMARGIN', new_y='NEXT')
    
    pdf.set_y(resumo_y + 58)

    def print_section(title):
        pdf.set_font('CustomArial', 'B', 10.5)
        pdf.set_text_color(27, 54, 93)
        pdf.cell(0, 5.5, title, new_x='LMARGIN', new_y='NEXT')
        pdf.set_draw_color(27, 54, 93)
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.l_margin + 35, pdf.get_y())
        pdf.ln(2)

    def print_subsection(title):
        pdf.set_font('CustomArial', 'B', 9)
        pdf.set_text_color(43, 92, 143)
        pdf.cell(0, 4.5, title, new_x='LMARGIN', new_y='NEXT')
        pdf.ln(1)

    def print_p(text, bold_prefix=""):
        pdf.set_font('CustomArial', '', 8.5)
        pdf.set_text_color(30, 30, 30)
        if bold_prefix:
            pdf.set_font('CustomArial', 'B', 8.5)
            pdf.write(4.2, bold_prefix)
            pdf.set_font('CustomArial', '', 8.5)
        pdf.multi_cell(0, 4.2, text, align='J')
        pdf.ln(1.8)

    def print_image_box(img_name, caption, w_mm=130):
        img_path = os.path.join(OUTPUTS_DIR, img_name)
        if not os.path.exists(img_path):
            return
        # Checa se cabe na página atual ou força quebra
        if pdf.get_y() + (w_mm * 0.55) > 270:
            pdf.add_page()
        x = (pdf.w - w_mm) / 2
        pdf.image(img_path, x=x, w=w_mm)
        pdf.ln(1)
        pdf.set_font('CustomArial', 'I', 7.5)
        pdf.set_text_color(90, 90, 90)
        pdf.cell(0, 3.5, f"Figura: {caption}", align='C', new_x='LMARGIN', new_y='NEXT')
        pdf.ln(2.5)

    # 1. Introdução
    print_section("1. INTRODUÇÃO")
    print_p(
        "O câncer de mama representa uma das principais causas de mortalidade feminina no cenário epidemiológico global. "
        "A intervenção precoce e o diagnóstico diferencial tempestivo entre lesões benignas e malignas são determinantes "
        "para o aumento substancial das taxas de sobrevida livre de doença. Tradicionalmente, o procedimento de Punção Aspirativa "
        "por Agulha Fina (PAAF) é realizado para coleta de material celular, o qual é examinado microscopicamente por patologistas."
    )
    print_p(
        "A aplicação de modelos computacionais inteligentes (Machine Learning) surge como um vetor transformador, capaz de mitigal "
        "a subjetividade humana e a fadiga diagnóstica, provendo sistemas de apoio à decisão clínica (CAD). "
        "O presente trabalho aborda a implementação prática de algoritmos de aprendizado de máquina supervisionado e não supervisionado, "
        "investigando o trade-off entre sensibilidade diagnóstica (capacidade de detectar lesões malignas) e especificidade estatística."
    )

    # 2. Metodologia
    print_section("2. METODOLOGIA")
    print_subsection("2.1 Banco de Dados Clínicos (UCI WDBC)")
    print_p(
        "Adotou-se o conjunto público Breast Cancer Wisconsin (Diagnostic) - WDBC, mantido no repositório UCI. A base compreende "
        "569 instâncias clínicas sem dados faltantes (0 missing values). Cada observação é composta por 30 atributos contínuos que quantificam "
        "dez características morfológicas nucleares (raio, textura, perímetro, área, suavidade, compacidade, concavidade, pontos côncavos, "
        "simetria e dimensão fractal), estratificadas em três medidas estatísticas: média (mean), erro-padrão (se) e pior valor (worst). "
        "A variável alvo é binária: 357 casos Benignos (62,74%) e 212 casos Malignos (37,26%). Visando total fidelidade médica, a classe "
        "Maligno foi codificada como positiva (1) e Benigno como negativa (0), tornando o cálculo de Sensibilidade representativo da detecção tumoral."
    )

    print_subsection("2.2 Pré-Processamento e Normalização")
    print_p(
        "Devido à acentuada disparidade de ordens de magnitude entre os atributos (ex.: área média com valores superiores a 2500 e suavidade média "
        "em torno de 0,1), a normalização é mandatória para modelos métricos e estocásticos. Aplicou-se a padronização por Z-score (StandardScaler), "
        "garantindo média zero e desvio-padrão unitário. Fundamentalmente, a transformação foi computada dentro de cada dobra de treino na validação "
        "cruzada, prevenindo categoricamente o vazamento de dados (data leakage)."
    )

    print_subsection("2.3 Clusterização Não Supervisionada (K-Means)")
    print_p(
        "Para testar a hipótese de que a morfologia nuclear forma grupos espontâneos condizentes com a condição clínica, empregou-se o "
        "algoritmo K-Means. O número ideal de clusters foi determinado pelo Método do Cotovelo (monitoramento da inércia) e pelo Coeficiente "
        "Médio de Silhueta para k variando de 2 a 10. A dispersão espacial dos agrupamentos foi mapeada via Análise de Componentes Principais (PCA) em 2D e 3D."
    )

    print_subsection("2.4 Algoritmos de Classificação Supervisionada")
    print_p(
        "Foram implementados cinco algoritmos consagrados na literatura de Inteligência Artificial:\n"
        "• Árvore de Decisão: Baseada no critério de impureza de Gini com poda de profundidade (max_depth=4) para manter alta transparência explicativa.\n"
        "• K-Nearest Neighbors (KNN): Classificador geométrico não-paramétrico com k=5 vizinhos e distância euclidiana após padronização Z-score.\n"
        "• Support Vector Machine (SVM): Kernel RBF (Base Radial Gaussiana) com hiperparâmetro de regularização C=1,0 para fronteiras de separação não-lineares.\n"
        "• Naive Bayes: Modelo probabilístico baseado no Teorema de Bayes sob a hipótese simplificadora de independência condicional dos atributos.\n"
        "• Redes Neurais (MLP): Perceptron Multicamadas densamente conectado com 2 camadas ocultas (64 e 32 neurônios), ReLU e otimizador Adam."
    )

    print_subsection("2.5 Validação Cruzada Estratificada (Stratified 10-Fold)")
    print_p(
        "Todos os classificadores foram submetidos à validação cruzada estratificada em 10 dobras (Stratified 10-Fold Cross-Validation), "
        "preservando estritamente a proporção de 62,7% de benignos e 37,3% de malignos em cada iteração de teste. Foram computadas formalmente: "
        "Acurácia Global, Sensibilidade (Recall = VP/(VP+FN)), Especificidade (VN/(VN+FP)), Área sob a Curva ROC (AUC-ROC) e a Matriz de Confusão agregada."
    )

    # 3. Resultados
    pdf.add_page()
    print_section("3. RESULTADOS EXPERIMENTAIS E ANÁLISES GRÁFICAS")
    print_subsection("3.1 Análise Exploratória dos Dados (EDA)")
    print_p("A Figura 1 apresenta a distribuição das classes e a Figura 2 apresenta a matriz de correlação de Pearson entre as medidas médias.")
    print_image_box("eda_distribuicao_classes.png", "Distribuição Absoluta e Relativa das Classes Diagnósticas (WDBC).", 140)
    print_image_box("eda_matriz_correlacao.png", "Matriz de Correlação Linear entre Atributos Morfológicos Médios.", 130)

    print_subsection("3.2 Análise de Agrupamento (K-Means e PCA)")
    print_p(
        "O Coeficiente de Silhueta (Figura 3) apresentou seu ápice exato em k=2 (score = 0,3450), confirmando a partição binária natural dos dados. "
        "Na projeção PCA 2D (Figura 4), as duas primeiras componentes explicam 63,2% da variância total, atingindo Adjusted Rand Index (ARI) de 0,6707 "
        "em relação às anotações médicas reais."
    )
    print_image_box("cluster_elbow_silhouette.png", "Método do Cotovelo e Coeficiente Médio de Silhueta para seleção de k ótimo.", 135)
    print_image_box("cluster_pca_2d.png", "Projeção PCA 2D: Agrupamentos K-Means vs Classes Diagnósticas Reais.", 145)

    # 3.3 Tabela de Classificação
    pdf.add_page()
    print_subsection("3.3 Desempenho dos Modelos de Classificação Supervisionada")
    print_p(
        "A Tabela 1 sintetiza os resultados comparativos das métricas obtidas na validação cruzada de 10 dobras (médias ± desvios-padrão)."
    )

    # Tabela estilizada em PDF
    pdf.set_font('CustomArial', 'B', 8)
    pdf.set_fill_color(27, 54, 93)
    pdf.set_text_color(255, 255, 255)
    cols_w = [45, 31, 31, 31, 32]
    headers = ["Algoritmo", "Acurácia (%)", "Sensibilidade (%)", "Especificidade (%)", "AUC-ROC (%)"]
    for i, h in enumerate(headers):
        pdf.cell(cols_w[i], 6, h, border=1, align='C', fill=True)
    pdf.ln()

    rows_data = [
        ["Árvore de Decisão", "91,04 ± 3,87", "85,80 ± 10,24", "94,13 ± 4,56", "91,45 ± 7,34"],
        ["KNN (k=5)", "97,01 ± 1,76", "92,90 ± 4,90", "99,44 ± 1,11", "98,68 ± 1,46"],
        ["SVM (Kernel RBF)", "97,54 ± 1,95", "96,21 ± 3,56", "98,33 ± 2,83", "99,56 ± 0,55"],
        ["Naive Bayes Gaussiano", "93,15 ± 3,08", "89,57 ± 7,65", "95,26 ± 4,82", "98,56 ± 1,12"],
        ["Redes Neurais (MLP)", "96,84 ± 1,89", "95,24 ± 5,63", "97,75 ± 2,45", "99,26 ± 1,00"]
    ]

    pdf.set_font('CustomArial', '', 8)
    pdf.set_text_color(30, 30, 30)
    for idx, row in enumerate(rows_data):
        fill = (idx % 2 == 1)
        pdf.set_fill_color(245, 248, 252) if fill else pdf.set_fill_color(255, 255, 255)
        if idx == 2: # SVM em destaque
            pdf.set_font('CustomArial', 'B', 8)
            pdf.set_text_color(27, 54, 93)
        else:
            pdf.set_font('CustomArial', '', 8)
            pdf.set_text_color(30, 30, 30)
        pdf.cell(cols_w[0], 5.5, row[0], border=1, align='L', fill=True)
        pdf.cell(cols_w[1], 5.5, row[1], border=1, align='C', fill=True)
        pdf.cell(cols_w[2], 5.5, row[2], border=1, align='C', fill=True)
        pdf.cell(cols_w[3], 5.5, row[3], border=1, align='C', fill=True)
        pdf.cell(cols_w[4], 5.5, row[4], border=1, align='C', fill=True)
        pdf.ln()

    pdf.ln(1)
    pdf.set_font('CustomArial', 'I', 7.5)
    pdf.set_text_color(90, 90, 90)
    pdf.cell(0, 4, "Tabela 1: Métricas de Desempenho dos Classificadores (Média ± Desvio Padrão em 10 Folds).", align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2.5)

    print_image_box("comparativo_metricas_barras.png", "Gráfico Comparativo das Métricas Clínicas dos Modelos.", 145)

    print_subsection("3.4 Curvas ROC e Matrizes de Confusão")
    print_p(
        "A Figura 6 exibe as Curvas ROC comparativas, evidenciando a supremacia do classificador SVM (AUC de 99,56%), "
        "seguido pela Rede Neural MLP (99,26%). A Figura 7 expõe as matrizes de confusão agregadas de todos os 569 pacientes avaliados."
    )
    print_image_box("curvas_roc_comparativas.png", "Curvas ROC Sobrepostas dos Cinco Classificadores sob Validação Cruzada.", 130)
    print_image_box("matrizes_confusao.png", "Matrizes de Confusão Agregadas com Contagens e Frequências Relativas.", 145)

    # 4. Discussão
    pdf.add_page()
    print_section("4. DISCUSSÃO CRÍTICA COMPARATIVA")
    print_p(
        "No domínio da inteligência médica, a análise estrita da acurácia global é insuficiente. O impacto de um Falso Negativo "
        "(paciente com tumor maligno classificada erroneamente como benigna) pode resultar em perda de janela terapêutica e óbito. "
        "Por conseguinte, a Sensibilidade (Recall) assume primazia ética e operacional no desenho do algoritmo."
    )
    print_p(
        "Sob essa ótica, o classificador Support Vector Machine (SVM com kernel RBF) consolidou-se como o modelo de melhor perfil "
        "clínico, registrando 96,21% de sensibilidade e acumulando apenas 8 falsos negativos em todo o conjunto de 569 biópsias. "
        "A projeção não-linear em espaço dimensional infinito pelo kernel RBF viabilizou a conformação de superfícies de decisão estritas "
        "em torno das instâncias limítrofes."
    )
    print_p(
        "A Rede Neural Artificial (MLP) demonstrou capacidade preditiva comparável (95,24% de sensibilidade e 99,26% de AUC), "
        "porém com custo computacional de convergência superior e menor transparência decisória em relação a modelos com margem determinística."
    )
    print_p(
        "O algoritmo K-Nearest Neighbors (KNN) obteve a mais alta especificidade registrada (99,44%), cometendo apenas 2 falsos alarmes "
        "em 357 casos benignos, o que denota alta densidade na vizinhança celular sadia. No entanto, sua sensibilidade de 92,90% implicou "
        "em 15 falsos negativos, quase o dobro do observado no SVM."
    )
    print_p(
        "O Naive Bayes Gaussiano demonstrou rapidez e AUC consistente (98,56%), mas sua acurácia foi contida em 93,15% devido à violação "
        "da independência condicional causada pela forte colinearidade entre raio, perímetro e área demonstrada na análise exploratória. "
        "Finalmente, a Árvore de Decisão com max_depth=4 proporcionou regras de fácil inspeção visual para a junta médica, com acurácia de 91,04%."
    )

    # 5. Conclusões
    print_section("5. CONCLUSÕES")
    print_p(
        "O trabalho atingiu com êxito todos os objetivos metodológicos e avaliativos fixados pela disciplina de Inteligência Artificial. "
        "Demonstrou-se que a morfologia nuclear celular extraída por biópsias aspirativas possui alto poder discriminante, permitindo "
        "agrupamento não supervisionado consistente (K-Means, ARI=0,6707) e classificação supervisionada de alta precisão (SVM, Acurácia=97,54%, Sensibilidade=96,21%)."
    )
    print_p(
        "Como direções futuras, propõe-se a integração de métodos ensemble (Random Forest, Gradient Boosting) e a implementação de seleção "
        "esparsa de atributos (LASSO) para otimizar os tempos de inferência em dispositivos médicos portáteis."
    )

    # 6. Referências
    print_section("6. REFERÊNCIAS BIBLIOGRÁFICAS")
    pdf.set_font('CustomArial', '', 7.5)
    pdf.set_text_color(50, 50, 50)
    refs = [
        "DUDA, R. O.; HART, P. E.; STORK, D. G. Pattern Classification. 2. ed. New York: John Wiley & Sons, 2001.",
        "FAWCETT, T. An introduction to ROC analysis. Pattern Recognition Letters, v. 27, n. 8, p. 861-874, 2006.",
        "HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. The Elements of Statistical Learning. 2. ed. New York: Springer, 2009.",
        "PEDREGOSA, F. et al. Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, v. 12, p. 2825-2830, 2011.",
        "ROUSSEEUW, P. J. Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. J. Comput. Appl. Math., v. 20, p. 53-65, 1987.",
        "WOLBERG, W. H.; STREET, W. N.; MANGASARIAN, O. L. Breast Cancer Wisconsin (Diagnostic) Data Set. UCI ML Repository, 1995."
    ]
    for r in refs:
        pdf.multi_cell(0, 3.8, r)
        pdf.ln(1)

    os.makedirs(os.path.dirname(OUTPUT_PDF), exist_ok=True)
    pdf.output(OUTPUT_PDF)
    print(f"Relatório PDF gerado com sucesso em: {OUTPUT_PDF}")

if __name__ == "__main__":
    build_pdf()
