# Simulador de Repasse do PNAE — Versão Monitorada (Excel com macro)

Planilha de Excel (`.xlsm`) que estima o repasse financeiro do Programa Nacional de Alimentação Escolar (PNAE) a uma escola e **registra cada simulação feita** em um banco de dados dentro do próprio arquivo, por meio de uma macro em VBA.

Criada como artefato do Projeto [X] do curso Análise de Dados para Pesquisas em Políticas Públicas (FGV EAESP), usando como estudo de caso a escola fictícia EMEB Vila Quitaúna, no bairro de Quitaúna, Osasco/SP.

## O que a planilha faz

- Recebe o número de matrículas por modalidade de ensino.
- Calcula o repasse anual estimado, o porte da escola e a elegibilidade para complementação municipal.
- Permite aplicar um fator de ajuste percentual sobre as matrículas (crescimento ou queda) e ver o impacto no repasse.
- Monta uma tabela de 9 cenários (−20% a +20%) com a Tabela de Dados do Excel.
- **Novo nesta versão:** exige o racional do fator de ajuste e o nome do usuário, e grava a simulação (data/hora, fator, racional, matrículas, repasse e usuário) na aba `Banco_de_Dados` ao clicar em **Salvar Simulação**.

## Fórmula central

```
Repasse = SOMARPRODUTO(Matrículas; Valor per capita) × Dias letivos
```

- **Matrículas** — nº de alunos por modalidade (creche, pré-escola, fundamental, médio, EJA, indígena/quilombola, AEE).
- **Valor per capita** — valor diário oficial por modalidade (R$/dia), conforme Resolução CD/FNDE nº 1/2026.
- **Dias letivos** — fixo em 200 dias/ano.

Com os dados da EMEB Vila Quitaúna (60 creche, 80 pré-escola, 50 fundamental), o repasse anual estimado é de R$ 37.660,00.

## Regras de negócio

| Regra | Lógica |
|---|---|
| Porte da escola | Pequena (0–200 matrículas) · Média (201–400) · Grande (401+) — faixas didáticas, não oficiais |
| Elegibilidade p/ complementação municipal | Elegível se porte = Pequena e houver matrícula em creche ou pré-escola — regra criada para praticar SE aninhado com E/OU |
| Fator de ajuste | Aplica (1 + fator) a todas as matrículas ao mesmo tempo, recalculando total e repasse |
| Registro da simulação | Só é salvo se o fator for numérico, o racional estiver preenchido e o usuário estiver preenchido |

> ⚠️ Os valores per capita e os dias letivos são reais (fonte oficial FNDE). As faixas de porte e a regra de elegibilidade são fictícias, criadas apenas para fins didáticos do curso.

## Estrutura técnica

Arquivo único `.xlsm` com quatro abas:

| Aba | Conteúdo |
|---|---|
| `Parametros_PNAE` | Valores per capita por modalidade, dias letivos e faixas de porte |
| `Simulador_Escola` | Dados da escola, matrículas, resultado automático, simulação com fator de ajuste, campos de racional e usuário, botão "Salvar Simulação" e tabela de cenários |
| `Banco_de_Dados` | Histórico das simulações gravadas pela macro |
| `Gráfico1` | Folha de gráfico de barras ligada ao campo Usuário (`Simulador_Escola!F27:F28`) |

### Macro (módulo `modSimulador`)

| Procedimento | O que faz |
|---|---|
| `RegistrarSimulacao` | Lê fator (C26), racional (C25), usuário (F28), matrículas ajustadas (C35) e repasse ajustado (D35); chama a validação; grava uma nova linha no `Banco_de_Dados` (ID, data/hora, fator, racional, matrículas, repasse, usuário); limpa os campos e mostra a mensagem de sucesso |
| `ValidarSimulacao` | Confere se o fator é numérico e se racional e usuário foram preenchidos; se não, devolve uma mensagem de erro e impede o registro |
| `LimparCampos` | Apaga o racional e volta o fator de ajuste para 0, deixando a tela pronta para a próxima simulação (o campo Usuário é limpo em `RegistrarSimulacao`) |

### Banco de dados

| Coluna | Campo |
|---|---|
| A | ID (sequencial) |
| B | Data/hora do registro |
| C | Fator de ajuste |
| D | Racional da taxa |
| E | Total de matrículas ajustadas |
| F | Repasse ajustado (R$) |
| G | Usuário |

## Como usar

1. Abra o arquivo `.xlsm` no Excel e **habilite as macros** (sem isso o botão não funciona).
2. Na aba `Simulador_Escola`, edite as matrículas por modalidade: total, porte, repasse e elegibilidade recalculam sozinhos.
3. Digite o **Fator de Ajuste** (célula C26, ex.: `0,1` para +10%) e veja matrículas e repasse ajustados.
4. Escreva o **racional** do fator (C25) e o seu **nome** (F28).
5. Clique em **Salvar Simulação**. Se algum campo estiver vazio, a macro avisa e não registra.
6. Confira o registro na aba `Banco_de_Dados`.
7. Para atualizar os cenários: selecione A39:C48 → Dados → Teste de Hipótese → Tabela de Dados → em "Célula de entrada da coluna", informe C26.

## Rastreabilidade (planilha de origem)

| Elemento | Célula/aba |
|---|---|
| Parâmetros oficiais (modalidades e valor per capita) | `Parametros_PNAE!A4:B11`; dias letivos em B13 |
| Faixas de porte da escola | `Parametros_PNAE!A16:B19` |
| Dados da escola | `Simulador_Escola!B4:B6` |
| Matrículas por modalidade + PROCV do valor per capita | `Simulador_Escola!A10:C16` |
| Total de matrículas | `Simulador_Escola!B17` |
| Porte da escola (PROCV aproximado) | `Simulador_Escola!B19` |
| Repasse anual estimado | `Simulador_Escola!B21` (SOMARPRODUTO) |
| Elegibilidade | `Simulador_Escola!C23` (SE + E/OU) |
| Racional da taxa | `Simulador_Escola!C25` |
| Fator de ajuste e valores ajustados | `Simulador_Escola!C26`, `C28:C34`, `C35`, `D35` |
| Usuário | `Simulador_Escola!F27:F28` |
| Tabela de cenários | `Simulador_Escola!A39:C48` (Dados → Teste de Hipótese → Tabela de Dados) |
| Botão "Salvar Simulação" | `Simulador_Escola` (ligado à macro `RegistrarSimulacao`) |
| Registro das simulações | `Banco_de_Dados!A4:G` (dados a partir da linha 5) |

## Créditos

Simulador de Repasse do PNAE — Versão Monitorada
Projeto [X] — Análise de Dados para Políticas Públicas (FGV EAESP)

📌 Planilha construída pelo grupo. A macro `RegistrarSimulacao` partiu de um código-base do curso, e o grupo completou a parte do campo Usuário (variável, validação e limpeza).

## ⚠️ Disclaimer de Inteligência Artificial

Este aviso vale apenas para o que realmente foi feito com apoio de IA.

**Ferramenta utilizada:** [preencher — ou escrever "Não foi usada IA neste projeto"]

**Para que foi usado:** [preencher]

**Exemplo de prompt utilizado:** [preencher]

## 📊 Aviso de Isenção de Responsabilidade de Dados

**Fonte oficial:** Resolução CD/FNDE nº 1, de 18 de fevereiro de 2026 (valores per capita do PNAE, reajustados em 14,35% em relação a 2025)
**Link oficial:** [inserir link da resolução]

**O que os dados representam:** Os valores per capita diários (R$/dia) que o governo federal repassa às escolas por aluno matriculado, variando conforme a modalidade de ensino. Multiplicados pelo número de matrículas e pelos dias letivos do ano, determinam o repasse anual da escola. A escola, as matrículas, as faixas de porte e a regra de elegibilidade são fictícias.

**Estrutura dos dados**

| Variável | O que significa |
|---|---|
| modalidade | Etapa/modalidade de ensino (creche, pré-escola, fundamental, médio, EJA, indígena/quilombola, AEE) |
| percapita (R$/dia) | Valor diário repassado por aluno matriculado na modalidade |
| matrículas | Número de alunos matriculados em cada modalidade na escola |
| dias letivos | Quantidade de dias do ano letivo cobertos pelo repasse (200 dias) |
| porte | Classificação da escola (Pequena/Média/Grande) conforme total de matrículas — critério didático, não oficial |
| elegibilidade | Indicador de elegibilidade à complementação municipal — regra didática, não oficial |
| fator de ajuste | Variação percentual aplicada às matrículas na simulação |
| racional da taxa | Justificativa escrita do fator de ajuste escolhido |
| usuário | Nome de quem fez e registrou a simulação |

## 👥 Disclaimer de Participação

**O que aprendemos com este projeto:** [preencher com a fala do grupo. Pontos possíveis: uso de macro em VBA para gravar dados em outra aba; validação de campos com mensagem de erro; banco de dados dentro do Excel; e o que já vinha do Projeto 1 (PROCV, SE aninhado com E/OU, SOMARPRODUTO e Tabela de Dados).]

**Papel de cada um:**

- [Ana Clara Oliveira]: Fez o readme do P1
- [Jamilly Cardoso Barros]: Fez o projeto 1 
- [Joohyeon Lee]: Fez o projeto 1
- [Lara Morais]: Fez o projeto 2
- [Marcely de Macedo]: Fez o projeto 2
