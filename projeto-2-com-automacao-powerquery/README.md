<div align="center">
# 📊 Painel do Censo Escolar 2024
### Versão 2.0 — Pipeline de dados automatizado com Power Query e Excel
 
![Excel](https://img.shields.io/badge/Microsoft%20Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Power Query](https://img.shields.io/badge/Power%20Query-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Linguagem M](https://img.shields.io/badge/Linguagem-M-5C2D91?style=for-the-badge)
![Versão](https://img.shields.io/badge/vers%C3%A3o-2.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/status-atualizado-success?style=for-the-badge)
 
**Um clique. Qualquer município. Painel inteiro atualizado.**
 
[📂 Base de Dados](#-base-de-dados) •
[🚀 Evoluções](#-principais-evoluções-v10-vs-v20) •
[🛠️ Detalhamento Técnico](#️-detalhamento-técnico-das-implementações) •
[📈 Testar a Automação](#-como-testar-a-automação-do-painel) •
[⚙️ Como Rodar](#️-como-rodar-o-projeto-no-seu-computador)
 
</div>
---
 
## 📖 Sobre o Projeto
 
Este repositório apresenta a evolução do **Projeto 2 – Painel do Censo Escolar**.
 
Enquanto a primeira versão dependia de manipulações estáticas e filtros manuais, a **V2.0** consolida um **pipeline de dados totalmente automatizado e dinâmico**, utilizando recursos avançados do **Power Query** e do **Microsoft Excel**.
 
> 🎯 **Meta da atualização:** fechar o fluxo de engenharia de dados de ponta a ponta, permitindo que o painel inteiro se atualize com **apenas um clique**, adaptando-se instantaneamente a **qualquer município** escolhido pelo usuário.
 
---
 
## 🚀 Principais Evoluções (V1.0 vs. V2.0)
 
| 🔧 Recurso / Etapa | ⏪ Versão Anterior (V1.0) | ✅ Nova Versão (V2.0) |
|:---|:---|:---|
| **Cruzamento de Dados** | PROCVs estáticos no Excel tradicional | Left Joins eficientes direto no Power Query |
| **Filtro de Município** | Filtros manuais fixos na base de dados | Inner Join dinâmico controlado por célula do Excel |
| **Classificação de Tamanho** | Fórmulas manuais ou tabelas De/Até | Coluna condicional customizada via linguagem M |
| **Mapeamento de Infraestrutura** | Dados binários isolados (0 e 1) | Tratamento de nulos (`null`) e consolidação categórica |
| **Atualização do Painel** | Lentidão e necessidade de múltiplos cliques | Otimização de background (atualização imediata) |
| **Interface Visual** | Gráficos padrão com poluição visual | Design integrado translúcido com segmentação textual |
 
---
 
## 🛠️ Detalhamento Técnico das Implementações
 
### 1️⃣ Modelagem de Dados com Joins (Junção de Tabelas)
 
**🔗 Left Outer Joins**
Substituímos o raciocínio do PROCV exato no Excel por junções externas à esquerda dentro do Power Query. Conectamos a tabela principal (`Microdados`) às tabelas de apoio de códigos, como `TP_DEPENDENCIA` e `TP_SITUACAO_FUNCIONAMENTO`, expandindo as descrições textuais correspondentes **sem o risco de perder registros** por incompatibilidade.
 
**🎯 Inner Join Automático**
Criamos uma tabela de controle dinâmica no Excel (**UF** e **Município**). Essa tabela foi transformada em uma consulta no Power Query e ligada à base principal por meio de um **Inner Join multivariável simultâneo**, cruzando UF e Município ao mesmo tempo. Assim, apenas as escolas da cidade escolhida passam pelo pipeline.
 
### 2️⃣ Criação de Colunas Condicionais Avançadas
 
**🏫 Tamanho da Escola**
Estrutura lógica baseada na coluna `QT_MAT_BAS`, que categoriza as instituições em faixas automáticas:
 
`Microescola` → `Pequena` → `Média` → `Grande` → `Muito Grande` → `Mega escola`
 
**💧 Indicadores de Infraestrutura**
Colunas calculadas para **Água, Energia, Esgoto e Lixo**. A lógica percorre sequencialmente as colunas binárias da base bruta. Caso nenhuma opção seja marcada, o sistema atribui o valor `null`, separando corretamente as escolas **sem o recurso** daquelas que **não responderam** ao censo.
 
### 3️⃣ Conexão e Otimização do Painel Visual
 
**📈 Modelagem Dinâmica**
Os gráficos dinâmicos foram conectados diretamente às tabelas dinâmicas alimentadas pelo Power Query, eliminando intervalos fixos de células.
 
**🎛️ Segmentação de Dados com Texto**
Substituímos os filtros de códigos numéricos por descrições textuais por extenso. As segmentações foram unificadas por meio de **Conexões de Relatório**, permitindo que um único clique filtre **todos os gráficos** do dashboard simultaneamente.
 
**⚡ Desativação de Atualização em Segundo Plano**
Ajustamos as propriedades da consulta `Microdados`, desmarcando a opção de atualização em segundo plano. Isso força o Excel a aguardar a conclusão do pipeline antes de renderizar os gráficos, garantindo a **sincronia perfeita** do painel em um único clique no botão **Atualizar Tudo**.
 
---
 
## 📂 Base de Dados
 
Como os microdados do Censo Escolar 2024 possuem tamanho elevado, a base bruta é disponibilizada **separadamente** do arquivo principal do painel.
 
<div align="center">
### 📥 [**Baixar a base de dados — Censo Escolar 2024**](https://drive.google.com/uc?export=download&id=1v34Db7utOq1LZY0WIe33axuDlBm6qips)
 
</div>
> [!IMPORTANT]
> Após baixar a base, salve o arquivo em uma **pasta de fácil acesso** no seu computador. O caminho do arquivo deverá ser configurado no Power Query antes da primeira atualização do painel. Consulte a seção [⚙️ Como rodar o projeto no seu computador](#️-como-rodar-o-projeto-no-seu-computador) para realizar essa configuração.
 
---
 
## 📈 Como Testar a Automação do Painel
 
1. 📂 Abra o arquivo do projeto no Excel.
2. 🗂️ Navegue até a aba da **tabela de controle do município**.
3. ✏️ Altere as células para a cidade desejada.
   *Exemplo: UF = `RO` e Município = `Alta Floresta D'Oeste`.*
4. 🔄 Vá até a aba **Dados** e clique em **Atualizar Tudo** (atalho: `Ctrl + Alt + F5`).
5. 📊 Vá para a aba **Painel** e observe todos os gráficos e indicadores se reajustando automaticamente para a nova localidade!
---
 
## ⚙️ Como Rodar o Projeto no Seu Computador
 
> [!WARNING]
> Como a base do Censo Escolar é muito grande, ela fica salva em um arquivo separado. Para mudar de cidade e fazer as análises sem erros, é preciso sincronizar o caminho do arquivo **apenas uma vez**.
 
Siga o passo a passo antes de testar o painel:
 
| Passo | Ação |
|:---:|:---|
| **1** | **Baixe os dois arquivos:** o arquivo deste Painel e a base de dados do Censo Escolar 2024, disponibilizada na seção [📂 Base de Dados](#-base-de-dados). |
| **2** | **Abra o Editor:** abra o Painel no Excel, vá na aba **Dados** e clique em **Consultas e Conexões** (um painel se abrirá à direita). |
| **3** | **Acesse a Fonte:** dê um duplo clique na consulta chamada **`Microdados`** para abrir a tela do Power Query. |
| **4** | **Ajuste o Caminho:** no canto direito, na lista de **Etapas Aplicadas**, clique no ícone de engrenagem (⚙️) ao lado da primeira etapa, chamada **`Fonte`**. |
| **5** | **Selecione o arquivo:** na janela que abrir, clique em **Procurar...**, selecione o arquivo do Censo Escolar 2024 que você baixou e clique em **OK**. |
| **6** | **Salvar e Sair:** no canto superior esquerdo, clique em **Fechar e Carregar**. |
 
> [!TIP]
> ✅ **Pronto!** Agora o seu Excel já sabe onde a base de dados está guardada. Digite qualquer cidade na tabela de controle e clique em **Atualizar Tudo** para ver o painel funcionar.
 
---
 
<div align="center">
**📊 Dados que se atualizam sozinhos. Análises que não param.**
 
⭐ Se este projeto foi útil, deixe uma estrela no repositório!
 
</div>
 
