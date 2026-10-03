# Painel do Censo Escolar 2024 — Versão 2.0 (Atualizado)

Este repositório apresenta a evolução do **Projeto 2 - Painel do Censo Escolar**. Enquanto a primeira versão dependia de manipulações estáticas e filtros manuais, esta nova versão consolida um **pipeline de dados totalmente automatizado e dinâmico** utilizando recursos avançados do Power Query e do Microsoft Excel.

A grande meta desta atualização foi fechar o fluxo de engenharia de dados de ponta a ponta, permitindo que **o painel inteiro se atualize com apenas um clique**, adaptando-se instantaneamente a qualquer município escolhido pelo usuário.

---

## 🚀 Principais Evoluções (V1.0 vs. V2.0)

A tabela abaixo resume as melhorias estruturais implementadas nesta nova versão do projeto:

| Recurso / Etapa | Versão Anterior (V1.0) | Nova Versão Atualizada (V2.0) |
| :--- | :--- | :--- |
| **Cruzamento de Dados** | PROCVs estáticos no Excel tradicional. | **Left Joins** eficientes direto no Power Query. |
| **Filtro de Município** | Filtros manuais fixos na base de dados. | **Inner Join dinâmico** controlado por célula do Excel. |
| **Classificação de Tamanho**| Fórmulas manuais ou tabelas De/Até. | **Coluna Condicional customizada** via linguagem M. |
| **Mapeamento de Infraestrutura**| Dados binários isolados (0 e 1). | **Tratamento de nulos (`null`)** e consolidação categórica. |
| **Atualização do Painel** | Lentidão e necessidade de múltiplos cliques. | **Otimização de Background** (atualização imediata). |
| **Interface Visual** | Gráficos padrão com poluição visual. | **Design integrado translúcido** com segmentação textual. |

---

## 🛠️ Detalhamento Técnico das Implementações

### 1. Modelagem de Dados com Joins (Junção de Tabelas)
* **Left Outer Joins:** Substituímos o raciocínio do PROCV exato no Excel por junções externas à esquerda dentro do Power Query. Conectamos a tabela principal (`Microdados`) às tabelas de apoio de códigos (como `TP_DEPENDENCIA` e `TP_SITUACAO_FUNCIONAMENTO`), expandindo as descrições textuais correspondentes sem o risco de perder registros por incompatibilidade.
* **Inner Join Automático:** Criamos uma tabela de controle dinâmica no Excel (UF e Município). Essa tabela foi transformada em uma consulta no Power Query e ligada à base principal por meio de um *Inner Join* multivariável simultâneo (cruzando UF e Município ao mesmo tempo). Isso garante que apenas as escolas da cidade escolhida passem pelo pipeline.

### 2. Criação de Colunas Condicionais Avançadas
* **Tamanho da Escola:** Implementamos uma estrutura lógica baseada na coluna `QT_MAT_BAS` para categorizar as instituições em faixas automáticas (*Microescola, Pequena, Média, Grande, Muito Grande e Mega escola*).
* **Indicadores de Infraestrutura:** Criamos colunas calculadas para *Água, Energia, Esgoto e Lixo*. A lógica percorre sequencialmente as colunas binárias da base bruta. Caso nenhuma opção seja marcada, o sistema atribui o valor `null` (vazio), separando corretamente escolas sem recurso daquelas que não responderam ao censo.

### 3. Conexão e Otimização do Painel Visual
* **Modelagem Dinâmica:** Os gráficos dinâmicos foram conectados diretamente às tabelas dinâmicas alimentadas pelo Power Query, eliminando intervalos fixos de células.
* **Segmentação de Dados com Texto:** Substituímos os filtros de códigos numéricos por descrições textuais por extenso. As segmentações foram unificadas através de *Conexões de Relatório*, permitindo que um único clique do usuário filtre todos os gráficos do dashboard simultaneamente.
* **Desativação de Atualização em Segundo Plano:** Ajustamos as propriedades da consulta (`Microdados`) desmarcando a opção de atualização em segundo plano. Isso força o Excel a aguardar a conclusão do pipeline de dados antes de renderizar os gráficos, garantindo a sincronia perfeita do painel em um único clique no botão **Atualizar Tudo**.

---

## 📈 Como Testar a Automação do Painel

1. Abra o arquivo do projeto no Excel.
2. Navegue até a aba da tabela de controle do município.
3. Altere as células da tabela para a cidade desejada (ex: Alterar a UF para `RO` e o Município para `Alta Floresta D'Oeste`).
4. Vá até a aba **Dados** e clique em **Atualizar Tudo** (ou use o atalho `Ctrl + Alt + F5`).
5. Vá para a aba do **Painel** e observe todos os gráficos e indicadores se reajustando automaticamente para a nova localidade!

## ⚠️ IMPORTANTE: Como rodar o projeto no seu computador

Como a base de dados do Censo Escolar é muito grande, ela fica salva em um arquivo separado. Para conseguir mudar de cidade e fazer as análises sem erros, qualquer pessoa do grupo (ou o professor) precisa sincronizar o caminho do arquivo apenas uma vez.

Siga este passo a passo simples antes de testar o painel:

1. **Baixe os dois arquivos:** Faça o download do arquivo deste **Painel** e também do arquivo bruto do **Censo 2024** para o seu computador.
2. **Abra o Editor:** Abra o arquivo do Painel no Excel, vá na aba **Dados** (no menu superior) e clique em **Consultas e Conexões** (um painel se abrirá à direita).
3. **Acesse a Fonte:** Dê um duplo clique na consulta chamada **`Microdados`** para abrir a tela do Power Query.
4. **Ajuste o Caminho:** No canto direito da tela, na lista de *Etapas Aplicadas*, clique no ícone de **engrenagem (⚙️)** que fica ao lado da primeira etapa, chamada **`Fonte`**.
5. **Selecione o arquivo:** Na janela que abrir, clique em **Procurar...**, selecione o arquivo do Censo 2024 que você baixou no seu computador e clique em **OK**.
6. **Salvar e Sair:** No canto superior esquerdo da tela, clique em **Fechar e Carregar**.

Pronto! Agora o seu Excel já sabe onde a base de dados está guardada. Você já pode digitar qualquer cidade na tabela de controle e clicar em **Atualizar Tudo** para ver o painel funcionar!


