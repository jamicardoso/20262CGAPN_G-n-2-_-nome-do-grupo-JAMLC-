Painel do Censo Escolar 2024 — Educação Básica no Município de São Paulo

Projeto 2 — Análise de Dados para Políticas Públicas (FGV EAESP)

Créditos

Painel construído a partir dos microdados do Censo Escolar da Educação Básica 2024 (INEP), filtrados para o município de São Paulo, para o Projeto 2 do curso Análise de Dados para Pesquisas em Políticas Públicas (FGV EAESP).

O que o painel faz
Organiza os microdados de 8.023 escolas do município de São Paulo, com dados de dependência administrativa, localização, situação de funcionamento, infraestrutura e matrículas.
Classifica cada escola por porte (Microescola, Pequena, Média, Grande, Muito Grande, Mega escola), conforme faixas de matrícula total.
Cruza dependência administrativa, localização e porte com indicadores de infraestrutura (água, energia, esgoto e destinação de lixo).
Reúne, na aba "DASH DA EDUCAÇÃO", os gráficos e tabelas dinâmicas que sintetizam esses cruzamentos para leitura rápida.
Como usar
Abra o arquivo Projeto_2_Censo_2024.xlsx no Excel.
Vá até a aba "DASH DA EDUCAÇÃO" para ver o painel principal, com os gráficos e segmentadores (filtros).
Use os segmentadores para filtrar por dependência administrativa, localização (urbana/rural) e porte da escola.
Consulte a aba "Dinâmicas" para ver as tabelas dinâmicas que alimentam os gráficos do painel.
Consulte a aba "Parâmetros" para os códigos das variáveis categóricas (dependência, localização, situação de funcionamento e faixas de porte).
Consulte a aba "Água-Energia-Esgoto-Lixo" para o dicionário das variáveis de infraestrutura.
A aba "microdados_ed_basica_2024" traz a base bruta, já filtrada para São Paulo, que alimenta todo o painel.

Disclaimer de Inteligência Artificial

Este aviso vale apenas para o que realmente foi feito com apoio de IA no Projeto 2.

Ferramenta utilizada: Claude (Anthropic)

Para que foi usado: Apoiar a estruturação deste README, organizando o objetivo do painel, o passo a passo de uso e a documentação da fonte de dados a partir da planilha já construída pelo grupo.

O que foi ajustado manualmente: O grupo revisou a descrição do painel e das abas para garantir que correspondiam exatamente ao que foi construído no Excel, e ajustou a redação para o padrão de linguagem usado no README do Projeto 1.

Aviso de Isenção de Responsabilidade de Dados
Fonte de Dados
Fonte oficial: Censo Escolar da Educação Básica 2024 (INEP)
Link oficial:

O que os dados representam: Os microdados trazem o cadastro de todas as escolas de educação básica do município de São Paulo que participaram do Censo Escolar 2024, com dados de identificação e localização de cada escola, sua situação de funcionamento, condições de infraestrutura básica (água, energia, esgoto e lixo) e o número de matrículas, desagregado por etapa de ensino, sexo, cor/raça e faixa etária.

Estrutura dos Dados
Variável	O que significa
NO_MUNICIPIO, NO_ENTIDADE	Município e nome da escola
TP_DEPENDENCIA / DEPENDENCIA	Dependência administrativa: 1-Federal, 2-Estadual, 3-Municipal, 4-Privada
TP_LOCALIZACAO / LOCALIZAÇÃO	Zona urbana (1) ou rural (2)
TP_LOCALIZACAO_DIFERENCIADA	Se a escola está em assentamento, terra indígena, comunidade quilombola ou comunidade tradicional
TP_SITUACAO_FUNCIONAMENTO / SITUAÇÃO	Se a escola está ativa ou inativa
IN_AGUA_*, IN_ENERGIA_*, IN_ESGOTO_*, IN_LIXO_*	Indicadores binários (0/1) de infraestrutura, detalhados na aba "Água-Energia-Esgoto-Lixo"
TAM_ESCOLA	Porte da escola: Microescola (até 50 matrículas), Pequena (51–200), Média (201–500), Grande (501–1000), Muito Grande (1001–5000), Mega escola (acima de 5000)
QT_MAT_*	Quantidade de matrículas totais e por etapa, sexo, cor/raça e faixa etária

Disclaimer de Participação

O que aprendemos com este projeto: Este projeto nos permitiu praticar, em uma base de dados pública real e grande (mais de 8 mil escolas), a construção de tabelas dinâmicas e painéis para cruzar variáveis categóricas (dependência, localização, porte) com indicadores de infraestrutura escolar. Aprendemos a interpretar os códigos e dicionários de variáveis do Censo Escolar do INEP e a montar um painel que resume visualmente essas informações. O projeto também reforçou a importância de documentar claramente a origem e a estrutura de uma base pública antes de analisá-la.

Papel de cada um:

[Ana Clara Oliveira]: 
[Jamilly Cardoso Barros]: 
[Joohyeon Lee]: 
[Lara Morais]: 
[Marcely de Macedo]: 
