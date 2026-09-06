# Simulador de Repasse do PNAE 

Página HTML interativa (autossuficiente, sem dependências externas) que reproduz, célula por célula, um modelo de Excel para estimar o repasse financeiro do **Programa Nacional de Alimentação Escolar (PNAE)** a uma escola.

Criado como artefato de apoio ao **Projeto 1** do curso *Análise de Dados para Pesquisas em Políticas Públicas* (FGV EAESP), usando como estudo de caso a escola fictícia **EMEB Vila Quitaúna**, no bairro de Quitaúna, Osasco/SP.

---

## O que o simulador faz

1. Recebe o número de matrículas por modalidade de ensino.
2. Calcula o **repasse anual estimado**, o **porte da escola** e a **elegibilidade para complementação municipal**.
3. Permite aplicar um **fator de ajuste percentual** sobre as matrículas (crescimento ou queda) e ver o impacto no repasse.
4. Reconstrói, passo a passo, uma **tabela de 9 cenários** (−20% a +20%), equivalente à *Tabela de Dados* do Excel.

---

## Fórmula central

```
Repasse = SOMARPRODUTO(Matrículas; Valor per capita) × Dias letivos
```

- **Matrículas** — nº de alunos por modalidade (creche, pré-escola, fundamental, médio, EJA, indígena/quilombola, AEE).
- **Valor per capita** — valor diário oficial por modalidade (R$/dia), conforme Resolução CD/FNDE nº 1/2026.
- **Dias letivos** — fixo em 200 dias/ano.

---

## Regras de negócio

| Regra | Lógica |
|---|---|
| **Porte da escola** | Pequena (0–200 matrículas) · Média (201–400) · Grande (401+) — faixas didáticas, não oficiais |
| **Elegibilidade p/ complementação municipal** | Elegível se porte = Pequena **e** houver matrícula em creche **ou** pré-escola — regra criada para praticar `SE` aninhado com `E`/`OU` |
| **Fator de ajuste** | Aplica `(1 + fator%)` a todas as matrículas simultaneamente, recalculando total e repasse |

> ⚠️ Os valores per capita e os dias letivos são reais (fonte oficial FNDE). As faixas de porte e a regra de elegibilidade são **fictícias**, criadas apenas para fins didáticos do curso.

---

## Estrutura técnica

Arquivo único `.html` com três blocos:

- **CSS** — variáveis de tema (`:root`), cartões, tabelas e badges de status.
- **HTML** — seções: introdução/fórmula → parâmetros oficiais → dados da escola → matrículas editáveis → resultado automático → simulação com fator de ajuste → tabela de cenários → rodapé de rastreabilidade.
- **JavaScript** — toda a lógica de cálculo e interatividade, sem frameworks:

| Função | O que faz |
|---|---|
| `getPorte(total)` | Classifica o porte da escola |
| `calcTotal(mat)` | Soma o total de matrículas |
| `calcRepasse(mat)` | Aplica a fórmula do repasse |
| `calcElegibilidade(porte, mat)` | Define elegibilidade à complementação |
| `updateMain()` | Recalcula tudo a cada alteração de input (tempo real) |
| `updateAjuste(mat, repasseBase)` | Aplica o fator de ajuste e mostra a variação |
| `iniciarCenarios()` / `avancarCenario()` | Gera e percorre os 9 cenários de −20% a +20% |

---

## Como usar

1. Abra o arquivo `.html` em qualquer navegador — não requer instalação nem internet.
2. Edite os números de matrícula por modalidade: os resultados recalculam automaticamente.
3. Ajuste o **fator percentual** para simular crescimento/queda de matrículas.
4. Clique em **"Iniciar / Reiniciar cenários"** e depois em **"Avançar cenário"** para percorrer a tabela de sensibilidade, um cenário por vez.

---

## Rastreabilidade (planilha de origem)

| Elemento do simulador | Célula/aba na planilha Excel |
|---|---|
| Parâmetros oficiais (modalidades e valor per capita) | `Parametros_PNAE!A5:B11`; dias letivos em `B13` |
| Faixas de porte da escola | `Parametros_PNAE!A16:B19` |
| Dados da escola | `Simulador_Escola!B4:B6` |
| Matrículas por modalidade + PROCV do valor per capita | `Simulador_Escola!A10:C16` |
| Total de matrículas | `Simulador_Escola!B17` |
| Porte da escola (PROCV aproximado) | `Simulador_Escola!B19` |
| Repasse anual estimado | `Simulador_Escola!B21` (`SOMARPRODUTO`) |
| Elegibilidade | `Simulador_Escola!C23` (`SE` + `E`/`OU`) |
| Fator de ajuste e valores ajustados | `Simulador_Escola!C26`, `C28:C34`, `C35`, `D35` |
| Tabela de cenários | `Simulador_Escola!A39:C48` (Dados → Teste de Hipótese → Tabela de Dados) |

---

## Créditos


# Simulador de Repasse do PNAE

Projeto 1 — Análise de Dados para Políticas Públicas (FGV EAESP)

---

## 📌 Créditos

Artefato gerado com apoio de IA (Claude, Anthropic) a partir do modelo de Excel construído pelo autor para o Projeto 1 do curso *Análise de Dados para Pesquisas em Políticas Públicas* (FGV EAESP).

---

## ⚠️ Disclaimer de Inteligência Artificial

> Este aviso vale apenas para o que realmente foi feito com apoio de IA. No Projeto 1, isso inclui os artefatos HTML do simulador.

**Ferramenta utilizada:** Claude (Anthropic)

**Para que foi usado:**
Gerar os artefatos HTML interativos do simulador de repasse do PNAE, reproduzindo em código a lógica de design (fórmulas, faixas de porte e regra de elegibilidade) originalmente construída em Excel, a partir do prompt enviado pela professora. A estrutura deste README também foi elaborada com apoio do Claude.

**Exemplo de prompt utilizado:**
> "Claude, explique como fazer um README e nos ajude a fazer um do nosso projeto passo a passo."

---

## 📊 Aviso de Isenção de Responsabilidade de Dados

Explica de onde vêm os dados usados no projeto, o que eles representam e como estão estruturados.

### Fonte de Dados

- **Fonte oficial:** Resolução CD/FNDE nº 1, de 18 de fevereiro de 2026 (valores per capita do PNAE, reajustados em 14,35% em relação a 2025)
- **Link oficial:** *[https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar]*

**O que os dados representam:**
Os valores per capita diários (R$/dia) que o governo federal repassa às escolas por aluno matriculado, variando conforme a modalidade de ensino (creche, pré-escola, fundamental, médio, EJA, indígena/quilombola e atendimento educacional especializado). Esses valores, multiplicados pelo número de matrículas e pelos dias letivos do ano, determinam o repasse anual de cada escola.

### Estrutura dos Dados

| Variável | O que significa |
|---|---|
| `modalidade` | Etapa/modalidade de ensino (creche, pré-escola, fundamental, médio, EJA, indígena/quilombola, AEE) |
| `percapita` (R$/dia) | Valor diário repassado por aluno matriculado na modalidade |
| `matrículas` | Número de alunos matriculados em cada modalidade na escola |
| `dias letivos` | Quantidade de dias do ano letivo cobertos pelo repasse (200 dias) |
| `porte` | Classificação da escola (Pequena/Média/Grande) conforme total de matrículas — **critério didático, não oficial** |
| `elegibilidade` | Indicador de elegibilidade à complementação municipal — **regra didática, não oficial** |

---

## 👥 Disclaimer de Participação

Explica o que o grupo aprendeu com o projeto e o papel de cada membro.

**O que aprendemos com este projeto:**
Este projeto nos permitiu aplicar, na prática, conceitos de fórmulas do Excel em um caso real de política pública. Trabalhamos com PROCV para buscar valores de referência (como faixas de repasse por número de matrículas) e com a função SE aninhada, combinada a E/OU, para tratar as diferentes regras de cálculo do repasse do PNAE. Também usamos SOMARPRODUTO e uma Tabela de Dados para simular cenários com múltiplas variáveis ao mesmo tempo. Além do aprendizado técnico em Excel, o projeto nos ajudou a entender melhor como funciona, na prática, o repasse de recursos do Programa Nacional de Alimentação Escolar (PNAE) entre os entes federativos. Por fim, tivemos a experiência de traduzir uma planilha com lógica de cálculo já validada em um artefato HTML interativo, com apoio de inteligência artificial, o que exigiu conferir se o simulador replicava fielmente o gabarito da planilha original.

**Papel de cada um:**

- **[Ana Clara Oliveira ]:** [o que fez no projeto]
- **[Jamilly Cardoso Barros]:** [o que fez no projeto]
- **[Joohyeon Lee]:** [reuniu os prints e registrou a entrega no eClass]
- **[Lara Morais]:** [o que fez no projeto]
- **[Marcely de Macedo]:** [o que fez no projeto]

---

## 📁 Conteúdo

- `simulador_pnae (1).html` — Simulador interativo em HTML


