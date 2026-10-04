# Painel do Censo Escolar 2024 — Versão 2.0 (Atualizado)

Este repositório apresenta a evolução do **Projeto 2 - Painel do Censo Escolar**. Enquanto a primeira versão dependia de manipulações estáticas e filtros manuais, esta nova versão consolida um **pipeline de dados totalmente automatizado e dinâmico** utilizando recursos avançados do Power Query e do Microsoft Excel.

A grande meta desta atualização foi fechar o fluxo de engenharia de dados de ponta a ponta, permitindo que **o painel inteiro se atualize com apenas um clique**, adaptando-se instantaneamente a qualquer município escolhido pelo usuário.

## 🎯 Objetivo do Projeto

O projeto tem como objetivo desenvolver um **painel de análise dos dados do Censo Escolar 2024**, permitindo que o usuário selecione diferentes municípios e visualize automaticamente indicadores relacionados às escolas e à infraestrutura educacional.

A versão 2.0 busca principalmente aumentar a **automação, flexibilidade, eficiência e facilidade de atualização** do painel, reduzindo a necessidade de manipulações manuais e tornando o processo de análise mais dinâmico.


## 🚀 Principais Evoluções (V1.0 vs. V2.0)

A tabela abaixo resume as melhorias estruturais implementadas nesta nova versão do projeto:

| Recurso / Etapa | Versão Anterior (V1.0) | Nova Versão Atualizada (V2.0) |
| :--- | :--- | :--- |
| **Cruzamento de Dados** | PROCVs estáticos no Excel tradicional. | **Left Joins** eficientes direto no Power Query. |
| **Filtro de Município** | Filtros manuais fixos na base de dados. | **Inner Join dinâmico** controlado por célula do Excel. |
| **Classificação de Tamanho** | Fórmulas manuais ou tabelas De/Até. | **Coluna Condicional customizada** via linguagem M. |
| **Mapeamento de Infraestrutura** | Dados binários isolados (0 e 1). | **Tratamento de nulos (`null`)** e consolidação categórica. |
| **Atualização do Painel** | Lentidão e necessidade de múltiplos cliques. | **Otimização de Background** (atualização imediata). |
| **Interface Visual** | Gráficos padrão com poluição visual. | **Design integrado translúcido** com segmentação textual. |

---

## 🛠️ Detalhamento Técnico das Implementações

### 1. Modelagem de Dados com Joins (Junção de Tabelas)

- **Left Outer Joins:** Substituímos o raciocínio do PROCV exato no Excel por junções externas à esquerda dentro do Power Query. Conectamos a tabela principal (`Microdados`) às tabelas de apoio de códigos, como `TP_DEPENDENCIA` e `TP_SITUACAO_FUNCIONAMENTO`, expandindo as descrições textuais correspondentes sem o risco de perder registros por incompatibilidade.

- **Inner Join Automático:** Criamos uma tabela de controle dinâmica no Excel (UF e Município). Essa tabela foi transformada em uma consulta no Power Query e ligada à base principal por meio de um *Inner Join* multivariável simultâneo, cruzando UF e Município ao mesmo tempo. Isso garante que apenas as escolas da cidade escolhida passem pelo pipeline.

### 2. Criação de Colunas Condicionais Avançadas

- **Tamanho da Escola:** Implementamos uma estrutura lógica baseada na coluna `QT_MAT_BAS` para categorizar as instituições em faixas automáticas (*Microescola, Pequena, Média, Grande, Muito Grande e Mega escola*).

- **Indicadores de Infraestrutura:** Criamos colunas calculadas para **Água, Energia, Esgoto e Lixo**. A lógica percorre sequencialmente as colunas binárias da base bruta. Caso nenhuma opção seja marcada, o sistema atribui o valor `null` (vazio), separando corretamente escolas sem recurso daquelas que não responderam ao censo.

### 3. Conexão e Otimização do Painel Visual

- **Modelagem Dinâmica:** Os gráficos dinâmicos foram conectados diretamente às tabelas dinâmicas alimentadas pelo Power Query, eliminando intervalos fixos de células.

- **Segmentação de Dados com Texto:** Substituímos os filtros de códigos numéricos por descrições textuais por extenso. As segmentações foram unificadas através de *Conexões de Relatório*, permitindo que um único clique do usuário filtre todos os gráficos do dashboard simultaneamente.

- **Desativação de Atualização em Segundo Plano:** Ajustamos as propriedades da consulta (`Microdados`) desmarcando a opção de atualização em segundo plano. Isso força o Excel a aguardar a conclusão do pipeline de dados antes de renderizar os gráficos, garantindo a sincronia perfeita do painel em um único clique no botão **Atualizar Tudo**.

---

## 📂 Base de Dados

Como os microdados do **Censo Escolar 2024** possuem um tamanho elevado, a base bruta é disponibilizada separadamente do arquivo principal do painel.

### 📥 Download da Base

[**Baixar a base de dados — Censo Escolar 2024**](https://drive.google.com/uc?export=download&id=1v34Db7utOq1LZY0WIe33axuDlBm6qips)

> **Importante:** após baixar a base, salve o arquivo em uma pasta de fácil acesso no seu computador. O caminho do arquivo deverá ser configurado no Power Query antes da primeira atualização do painel. Consulte a seção **"Como rodar o projeto no seu computador"** abaixo para realizar essa configuração.

---

## 📈 Como Testar a Automação do Painel

1. Abra o arquivo do projeto no Excel.

2. Navegue até a aba da tabela de controle do município.

3. Altere as células da tabela para a cidade desejada.  
   **Exemplo:** alterar a UF para `RO` e o Município para `Alta Floresta D'Oeste`.

4. Vá até a aba **Dados** e clique em **Atualizar Tudo** ou utilize o atalho `Ctrl + Alt + F5`.

5. Vá para a aba **Painel** e observe todos os gráficos e indicadores se reajustando automaticamente para a nova localidade.

---

## ⚠️ IMPORTANTE: Como Rodar o Projeto no Seu Computador

Como a base de dados do Censo Escolar é muito grande, ela fica salva em um arquivo separado. Para conseguir mudar de cidade e fazer as análises sem erros, qualquer pessoa do grupo ou o professor precisa sincronizar o caminho do arquivo apenas uma vez.

### Passo a passo

1. **Baixe os dois arquivos:** Faça o download do arquivo deste **Painel** e da **base de dados do Censo Escolar 2024**, disponibilizada na seção [**📂 Base de Dados**](#-base-de-dados), para o seu computador.

2. **Abra o Editor:** Abra o arquivo do Painel no Excel. Vá até a aba **Dados**, no menu superior, e clique em **Consultas e Conexões**. Um painel será aberto à direita.

3. **Acesse a Fonte:** Dê um duplo clique na consulta chamada **`Microdados`** para abrir o Editor do Power Query.

4. **Ajuste o Caminho:** No canto direito da tela, na lista de **Etapas Aplicadas**, clique no ícone de engrenagem ⚙️ que fica ao lado da primeira etapa, chamada **`Fonte`**.

5. **Selecione o arquivo:** Na janela que abrir, clique em **Procurar...**, selecione o arquivo do **Censo Escolar 2024** que você baixou no seu computador e clique em **OK**.

6. **Salvar e Sair:** No canto superior esquerdo da tela, clique em **Fechar e Carregar**.

Pronto! Agora o Excel já sabe onde a base de dados está guardada.

Você já pode digitar qualquer cidade na tabela de controle e clicar em **Atualizar Tudo** para ver o painel funcionar.

---

## 🔄 Fluxo de Funcionamento

O funcionamento do projeto pode ser resumido da seguinte forma:

**Base de Dados do Censo Escolar 2024**  
↓  
**Power Query — Importação dos Microdados**  
↓  
**Tratamento e Transformação dos Dados**  
↓  
**Joins com Tabelas de Apoio**  
↓  
**Filtro Dinâmico de Município**  
↓  
**Classificação e Criação de Indicadores**  
↓  
**Tabelas Dinâmicas**  
↓  
**Dashboard / Painel Interativo**

---

## 💻 Tecnologias e Recursos Utilizados

- **Microsoft Excel**
- **Power Query**
- **Linguagem M**
- **Tabelas Dinâmicas**
- **Gráficos Dinâmicos**
- **Segmentação de Dados**
- **Joins / Junções de Tabelas**
- **Microdados do Censo Escolar 2024**


# 🤖 Uso de Inteligência Artificial

**Ferramenta utilizada:** [NOME DA FERRAMENTA DE IA UTILIZADA PELO GRUPO]

**Para que foi usada:** [DESCREVER EXATAMENTE PARA QUE A IA FOI UTILIZADA NO PROJETO.]

**Exemplo de prompt utilizado:**

> [COLE AQUI UM PROMPT REAL QUE FOI UTILIZADO PELO GRUPO.]

**O que foi ajustado manualmente:** [DESCREVER OS AJUSTES REALIZADOS MANUALMENTE PELO GRUPO APÓS A UTILIZAÇÃO DA IA.]
# 🤖 Uso de Inteligência Artificial

**Ferramenta utilizada:** ChatGPT

**Para que foi usada:** A ferramenta de Inteligência Artificial foi utilizada como auxílio na **formatação e organização do arquivo README**, contribuindo para estruturar as informações do projeto em Markdown e melhorar a apresentação do documento no GitHub.

**Exemplo de prompt utilizado:**

> "Pegar exatamente o README que eu escrevi sem alterar o que eu tinha escrito e devolver uma versão final completa, já pronta para colar no GitHub."

**O que foi ajustado manualmente:** Após o auxílio da ferramenta, o grupo realizou a revisão do conteúdo e os ajustes necessários, mantendo as informações, descrições técnicas e características do projeto elaboradas pelo grupo.


# 📊 Fonte de Dados

**Fonte oficial:** Censo Escolar 2024 — INEP.

**Link oficial:** [https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar]

**O que os dados representam:** Os dados utilizados no projeto são os microdados do **Censo Escolar 2024**, utilizados para analisar informações relacionadas às escolas e à infraestrutura educacional.

**Estrutura:** O projeto utiliza a tabela principal de **Microdados** e tabelas auxiliares relacionadas à **Dependência, Localização, Localização Diferenciada e Situação**. Entre as informações utilizadas estão variáveis relacionadas ao município, número de matrículas e infraestrutura das escolas, incluindo **Água, Energia, Esgoto e Lixo**.


# 👥 Participação do Grupo

## O que aprendemos com este projeto

Com o desenvolvimento deste projeto, aprendemos a trabalhar com uma base de dados de maior volume utilizando o **Power Query**, realizando a importação, tratamento, transformação e combinação de diferentes tabelas. Também aprendemos a utilizar **Inner Joins e Left Joins**, criar colunas condicionais, trabalhar com dados nulos e construir um fluxo automatizado que conecta o tratamento dos dados às tabelas dinâmicas e ao dashboard.

A atualização do Projeto 2 também permitiu compreender como o **filtro realizado dentro do Power Query** pode reduzir a base nacional para o município selecionado antes do processamento das tabelas dinâmicas, tornando o painel mais dinâmico e automatizado.

## Papel de cada integrante

**[NOME DO INTEGRANTE 1]:** [DESCREVER O QUE FEZ NO PROJETO.]

**[NOME DO INTEGRANTE 2]:** [DESCREVER O QUE FEZ NO PROJETO.]

**[NOME DO INTEGRANTE 3]:** [DESCREVER O QUE FEZ NO PROJETO.]

**[NOME DO INTEGRANTE 4]:** [DESCREVER O QUE FEZ NO PROJETO.]

**[NOME DO INTEGRANTE 5]:** [DESCREVER O QUE FEZ NO PROJETO.]

**[NOME DO INTEGRANTE 6]:** [DESCREVER O QUE FEZ NO PROJETO.]

