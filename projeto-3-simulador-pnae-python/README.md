# Simulador de Repasse do PNAE em Python

**Objetivo:** Este programa calcula o valor anual que o governo federal repassa a uma escola pública por meio do Programa Nacional de Alimentação Escolar (PNAE), classifica o porte da instituição e estima o custo anual apenas dos alimentos servidos. O simulador serve para avaliar o percentual do custo de matéria-prima que a verba da União efetivamente cobre e calcular a diferença financeira que precisa ser complementada pelo estado ou município.

## Como usar

1. **Pré-requisitos:** É necessário ter o **Python 3** instalado no computador. Nenhuma biblioteca externa precisa ser instalada.
2. **Execução:** Abra o terminal (ou prompt de comando) na pasta onde está o arquivo do projeto e execute o comando:
   ```bash
   python simulador_pnae.py
   ```
3. **Interação:** O programa solicitará, um por vez, os seguintes dados (digite os textos solicitados e, para os dados numéricos, digite apenas números inteiros, sem pontos ou vírgulas):
   * Seu nome.
   * Nome da escola.
   * Quantidade de dias letivos no ano (padrão: `200`).
   * Número de matrículas na Creche.
   * Número de matrículas na Pré-escola.
   * Número de matrículas no Ensino Fundamental.
4. **Saída:** Após pressionar `Enter` na última pergunta, o terminal exibirá o porte da escola, os repasses discriminados por etapa, o custo anual estimado dos alimentos, o percentual de cobertura federal e o saldo financeiro restante a ser coberto por outras fontes.

## Prints do resultado
[Acesse a pasta de prints do Projeto 3  ](./printsprojeto3)

---

## Escola simulada

Para a aplicação prática do simulador, o grupo selecionou a seguinte instituição pública de ensino:

* **Nome da Escola:** República do Paraguay
* **Código INEP:** 35001892
* **Município / UF:** São Paulo / SP
* **Dependência Administrativa:** 2 (Estadual)
* **Matrículas Creche:** 0
* **Matrículas Pré-escola:** 0
* **Matrículas Ensino Fundamental:** 479
* **Total de Matrículas Consideradas:** 479

### Como os dados foram encontrados
Os dados foram extraídos diretamente da planilha oficial do **Censo Escolar 2024** (INEP). O grupo abriu o arquivo em Excel, aplicou um filtro na coluna de município para selecionar `São Paulo`, filtrou a dependência administrativa estadual (`2`) e localizou a escola pelo seu nome e código INEP (`35001892`). Para validar e cruzar as informações de matrículas e etapas atendidas, utilizamos também o portal **QEdu**. Como a escola atende exclusivamente o Ensino Fundamental (não possuindo turmas de Educação Infantil), o simulador recebeu `0` para creche e `0` para pré-escola, conforme orientado nas instruções.

---

## Custo dos alimentos

Para avaliar a suficiência do repasse federal, isolamos o custo exclusivo de aquisição de gêneros alimentícios (conforme determina a Lei nº 11.947/2009), desconsiderando gastos estruturais com gás, equipamentos e salários de merendeiras.

* **Valor adotado por refeição:** **R$ 3,60**
* **Fonte:** Estudo *"Análise dos Gastos Reais X Repasse de Verbas para a Alimentação Escolar de Duas Escolas Estaduais do Interior de SP"*, publicado nos anais do Congresso Nacional de Alimentos e Nutrição (CONAN).
* **Link:** [Anais CONAN - Análise de Gastos Reais](https://even3.com.br)
* **Data da informação:** Julho de 2025.

### Justificativa e ressalvas de comparabilidade
Consideramos o valor de R$ 3,60 razoável porque o estudo mapeou o custo real de nota fiscal da matéria-prima necessária para cumprir as metas nutricionais do PNAE em **escolas estaduais de Ensino Fundamental da Região Sudeste** — exatamente o mesmo perfil administrativo, regional e de etapa de ensino da E.E. República do Paraguay.

**Ressalvas contextuais:**
1. **Diferença de município e escala:** O estudo foi realizado em escolas estaduais do interior de São Paulo, enquanto a escola simulada fica na capital (São Paulo). Na capital, o custo logístico e o preço de hortifrúti no varejo tendem a ser maiores, embora grandes redes estaduais ganhem poder de barganha em licitações de grande escala.
2. **Etapa de ensino:** Como 100% das matrículas da escola simulada pertencem ao Ensino Fundamental (479 alunos), a média de R$ 3,60 por refeição apresenta altíssima aderência à realidade porcionada da escola, sem distorções causadas por fórmulas infantis de creche.
3. **Defasagem temporal:** Os dados de custo são de 2025, enquanto os repasses *per capita* do programa são de 2026. A inflação acumulada de alimentos entre um ano e outro pode fazer com que o custo real atual seja ligeiramente superior aos R$ 3,60 adotados.

---

## Resultados e reflexão

Considerando **200 dias letivos** e as 479 matrículas do Ensino Fundamental, o simulador gerou os seguintes resultados consolidados:

* **Porte da Escola:** Grande
* **Repasse Anual Total (União):** R$ 54.606,00 *(sendo R$ 0,00 de Creche + R$ 0,00 de Pré-escola + R$ 54.606,00 de Fundamental)*
* **Custo Anual Estimado dos Alimentos:** R$ 344.880,00
* **Cobertura do Repasse Federal:** **15,83%**
* **Diferença a ser coberta por outras fontes:** **R$ 290.274,00**

### Reflexão sobre o financiamento da alimentação escolar
Os resultados demonstram que o repasse federal de caráter suplementar cobre apenas **15,83%** do custo básico dos ingredientes, deixando um déficit anual de **R$ 290.274,00** a ser custeado pelo Governo do Estado de São Paulo. Conforme apontam as notas técnicas do *Todos Pela Educação (2023)* e as análises do *Observatório da Alimentação Escolar (2025)*, os valores *per capita* do PNAE sofreram forte defasagem inflacionária ao longo dos anos, tornando a contrapartida local indispensável.

Quando estados e municípios não possuem capacidade fiscal ou planejamento orçamentário para cobrir essa diferença expressiva com recursos próprios, o impacto recai diretamente sobre a qualidade nutricional servida ao estudante. Na prática, a falta de complementação obriga as gestões escolares a reduzirem a oferta de proteínas animais, diminuírem a compra de frutas e verduras frescas (da agricultura familiar) e substituírem refeições completas por preparações mais baratas e pobres em nutrientes — o que compromete a segurança alimentar, a permanência e o desempenho escolar de crianças e adolescentes que dependem da merenda como principal refeição do dia.

**Simplificações do modelo:** Esta análise considera o cruzamento de matrículas de 2024 com valores *per capita* de 2026; restringe o cálculo a apenas três etapas de ensino (excluindo Ensino Médio e EJA); e assume a premissa simplificada de apenas uma refeição por aluno por dia letivo.

---

## Organização do programa

O código foi estruturado mantendo os parâmetros fixos no topo, seguidos pelas funções de processamento e pelo fluxo principal de interação com o usuário:

| Função | O que faz | Correspondência no Projeto 1 (Excel) |
| :--- | :--- | :--- |
| `ler_numero(mensagem)` | Solicita um dado ao usuário no terminal e valida com `while` se o valor digitado é um número inteiro positivo. | Células de entrada de dados (Inputs de matrículas e dias letivos). |
| `calcular_repasse(matriculas, valor, dias)` | Multiplica o número de alunos pelo valor *per capita* da etapa e pelos dias letivos para obter o repasse anual. | Fórmulas de multiplicação das colunas de repasse por etapa de ensino. |
| `classificar_porte(numMatriculas)` | Utiliza condicionais (`if/elif/else`) para classificar o porte da escola conforme o total de matrículas. | Fórmula lógica `SE` aninhada que define o porte da escola pelo total de alunos. |
| `calcular_custo_anual(total, dias, custo)` | Multiplica o total de matrículas pelos dias letivos e pelo parâmetro fixo de R$ 3,60 por refeição. | *Nova funcionalidade (sem correspondência direta na planilha do Projeto 1).* |
| `calcula_cobertura(repasse, custo)` | Calcula o percentual de cobertura do PNAE e usa `if/else` para definir o saldo de déficit a ser coberto por outras fontes. | *Nova funcionalidade (sem correspondência direta na planilha do Projeto 1).* |

---

## Uso de Inteligência Artificial

* **Ferramenta utilizada:** Gemini (Google).
* **Para que foi usada:** Pesquisa de referências acadêmicas atualizadas sobre o custo real de gêneros alimentícios na Região Sudeste, esclarecimento de dúvidas sobre sintaxe em Python (uso de condicionais, operadores matemáticos e estruturação de funções) e apoio na organização estrutural deste documento.

## Fonte de Dados

* **Fontes oficiais:** Censo Escolar 2024 (INEP), Portal QEdu e Resolução CD/FNDE nº 1/2026 (valores *per capita* PNAE).
* **Links oficiais:** 
  * [Microdados do Censo Escolar - INEP](https://www.gov.br)
  * [Portal QEdu - Dados Educacionais](https://qedu.org.br)
  * [FNDE - Valores Per Capita PNAE](https://www.gov.br)
 
##  Participação do Grupo

### O que aprendemos com este projeto?

Aprendemos a desenvolver um programa em **Python** para analisar a quantidade de matrículas escolares e calcular os repasses destinados às diferentes etapas de ensino.

Ao longo do projeto, aprendemos a:

- Organizar o código em **funções**;
- Utilizar **parâmetros** e **variáveis**;
- **Validar** as entradas do usuário;
- Retornar resultados por meio do `return`.

Também compreendemos a importância de dividir o programa em etapas menores, tornando o código mais organizado, funcional e fácil de compreender. Além disso, a pesquisa sobre os custos dos alimentos contribuiu para fundamentar os valores utilizados nos cálculos.

### Papel de cada integrante

| Integrante | Responsabilidade |
|---|---|
| **Jamilly Cardoso** | Elaboração da nova estrutura do código, criação de uma nova função e definição das variáveis necessárias para o funcionamento do programa. |
| **Lara Morais** | Elaboração da reflexão do projeto e pesquisa sobre os custos dos alimentos, contribuindo para a fundamentação dos cálculos. |
| **Ana Clara Oliveira** | Auxiliou na elaboração e organização do `README`, contribuindo para a documentação do projeto. |
| **Marcely Macedo** | Ofereceu suporte ao desenvolvimento do projeto e às atividades realizadas pelo grupo. |
| **Joohyeon Lee** | Ofereceu suporte ao desenvolvimento do projeto e às atividades realizadas pelo grupo. |

