Painel do Censo Escolar 2024 — Educação Básica no Município de São Paulo

Objetivo: este projeto apresenta um painel (dashboard) interativo construído a partir dos microdados do Censo Escolar da Educação Básica 2024, com foco nas escolas do município de São Paulo. O painel permite visualizar a distribuição das escolas por dependência administrativa (Federal, Estadual, Municipal, Privada), localização (urbana/rural), porte (micro, pequena, média, grande, muito grande, mega escola) e condições de infraestrutura (abastecimento de água, energia, esgoto e destinação de lixo), cruzando essas informações com o número de matrículas por etapa, sexo, cor/raça e faixa etária.

Como usar:

Abrir o arquivo Projeto_2_Censo_2024.xlsx.
Ir até a aba "DASH DA EDUCAÇÃO" para visualizar o painel principal com os gráficos e tabelas dinâmicas.
Usar os filtros/segmentadores (slicers) do painel para explorar os dados por dependência, localização, porte da escola, etc.
Consultar a aba "Dinâmicas" para ver as tabelas dinâmicas que alimentam os gráficos do painel.
Consultar a aba "Parâmetros" para entender os códigos utilizados nas variáveis categóricas (ex: TP_DEPENDENCIA, TP_LOCALIZACAO, classificação de tamanho de escola).
Consultar a aba "Água-Energia-Esgoto-Lixo" para o dicionário das variáveis de infraestrutura (IN_AGUA_, IN_ENERGIA_, IN_ESGOTO_, IN_LIXO_).
A aba "microdados_ed_basica_2024" contém a base de dados bruta (8.023 escolas), já filtrada para o município de São Paulo, com todas as colunas utilizadas nas análises.

Prints do resultado: [inserir aqui uma ou duas capturas de tela do painel/dashboard em funcionamento]

Uso de Inteligência Artificial
Ferramenta utilizada: [ex: Claude — preencher com a ferramenta realmente usada pelo grupo]
Para que foi usada: [descrever o que foi feito com apoio de IA — ex: montagem de fórmulas, organização das tabelas dinâmicas, redação deste README, etc. Preencher apenas com o que de fato foi feito com IA]
Exemplo de prompt utilizado: [colar aqui um prompt real usado pelo grupo]
O que foi ajustado manualmente: [descrever os ajustes feitos pelo grupo depois da resposta da IA]
Fonte de Dados
Fonte oficial: Censo Escolar da Educação Básica 2024 (INEP)
Link oficial: https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar
O que os dados representam: os microdados trazem o cadastro de todas as escolas de educação básica do município de São Paulo que participaram do Censo Escolar 2024, incluindo dados de identificação e localização de cada escola, sua situação de funcionamento, condições de infraestrutura básica (água, energia, esgoto e lixo) e o número de matrículas, desagregado por etapa de ensino, sexo, cor/raça e faixa etária.
Estrutura: a base principal (microdados_ed_basica_2024) tem 8.023 linhas (uma por escola) e colunas como:
NO_MUNICIPIO, NO_ENTIDADE: município e nome da escola;
TP_DEPENDENCIA / DEPENDENCIA: dependência administrativa (1-Federal, 2-Estadual, 3-Municipal, 4-Privada);
TP_LOCALIZACAO / LOCALIZAÇÃO: zona urbana (1) ou rural (2);
TP_LOCALIZACAO_DIFERENCIADA: se a escola está em assentamento, terra indígena, comunidade quilombola ou comunidade tradicional;
TP_SITUACAO_FUNCIONAMENTO / SITUAÇÃO: se a escola está ativa ou inativa;
IN_AGUA_*, IN_ENERGIA_*, IN_ESGOTO_*, IN_LIXO_*: indicadores binários (0/1) de infraestrutura, detalhados na aba "Água-Energia-Esgoto-Lixo";
TAM_ESCOLA: classificação de porte da escola (Microescola até 50 matrículas, Pequena 51-200, Média 201-500, Grande 501-1000, Muito Grande 1001-5000, Mega escola acima de 5000), conforme faixas definidas na aba "Parâmetros";
QT_MAT_*: quantidade de matrículas totais e por etapa (infantil, fundamental, médio, profissionalizante, EJA, educação especial), por sexo, por cor/raça e por faixa etária.
