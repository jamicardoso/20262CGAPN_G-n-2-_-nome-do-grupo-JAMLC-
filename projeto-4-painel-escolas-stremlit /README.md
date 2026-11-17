# Projeto 4: Painel Interativo do Censo Escolar em Python

**Objetivo:** o painel mostra as escolas em atividade de 30 municípios de quatro regiões do estado de São Paulo (Região Metropolitana, Baixada Santista, Litoral Norte e Vale do Ribeira), com dados do Censo Escolar 2024. Dá para filtrar por região e dependência administrativa e ver, para as escolas escolhidas, quantas são, quantas matrículas têm, como se dividem por porte e localização, como é a infraestrutura de água e esgoto, onde ficam no mapa e quais são. Serve para comparar regiões e municípios e identificar onde a infraestrutura escolar é mais frágil.

## Como usar

1. Tenha o Python instalado e baixe esta pasta, mantendo o `painel.py` e o `escolas_sp_regioes_2024_geo.csv` juntos.
2. Instale os pacotes:

```
python -m pip install pandas streamlit
```

3. Abra o terminal dentro da pasta e rode o painel:

```
python -m streamlit run painel.py
```

4. O painel abre no navegador (normalmente em `http://localhost:8501`). Para fechar, volte ao terminal e aperte `Ctrl + C`.

**Como usar os filtros:** são duas caixas de seleção no topo da página. Escolha a região, depois a dependência (Federal, Estadual, Municipal ou Privada). Deixe em "Todas"/"Todos" para não filtrar. Todo o painel é recalculado a cada mudança. Se a combinação não tiver nenhuma escola, aparece um aviso.

## Prints do resultado
[Acesse a pasta de prints do Projeto 4  ](./printsprojeto4)

## Elementos do painel

| Elemento | Tipo | Coluna da base usada |
|---|---|---|
| Região | Filtro | `regiao` |
| Município | Filtro | `municipio` |
| Dependência | Filtro | `dependencia` |
| Qtde de escolas | Indicador | contagem de linhas (uma linha por escola) |
| Total de matrículas | Indicador | `matriculas` (soma) |
| Escolas por Porte | Gráfico de característica | `porte` (criada a partir de `matriculas`) |
| Escolas por Localização | Gráfico de característica | `localizacao` |
| Escolas por Abastecimento de Água | Gráfico de infraestrutura | `agua` |
| Escolas por Esgotamento Sanitário | Gráfico de infraestrutura | `esgoto` |
| Mapa das escolas | Mapa | `latitude` e `longitude` |
| Lista das Escolas | Tabela | `municipio`, `escola`, `dependencia`, `matriculas`, `porte` |

O gráfico de porte e o de localização usam características que **não** são filtros do painel.

## O que o painel mostra

O Vale do Ribeira se destaca das outras regiões quando trocamos o filtro de região. Ao escolher a Região Metropolitana de SP, o gráfico de localização mostra quase só escolas urbanas (apenas 0,2% são rurais); ao escolher o Vale do Ribeira, 36,7% das escolas são rurais (124 de 338). Isso vem junto com uma infraestrutura mais frágil: só 78,4% das escolas do Vale têm abastecimento de água pela rede pública, contra 99,8% na Região Metropolitana, e dois terços (66,6%) das escolas do Vale são de porte pequeno, contra 39,7% na Região Metropolitana. Dentro do Vale, escolhendo Barra do Turvo no filtro de município, só metade das 10 escolas está ligada à rede pública de esgoto.

## Organização do programa

O `painel.py` segue a ordem vista em aula: função, carregamento dos dados, filtros, indicadores, gráficos, mapa e lista.

| Parte do código | O que faz | Elemento do painel do Projeto 2 |
|---|---|---|
| `classifica_porte()` | classifica a escola em pequena, média ou grande pelo número de matrículas | coluna calculada de porte na base do Excel |
| `pd.read_csv(...)` e criação da coluna `porte` | carrega a base e aplica a função em cada escola | aba com a base de dados |
| `st.selectbox(...)` (região, município e dependência) | filtram a base antes de tudo; cada filtro parte da base já filtrada pelo anterior | segmentação de dados |
| `st.metric(...)` | mostra o total de escolas e o total de matrículas | big numbers do dash |
| `st.bar_chart(...)` (porte, localização, água e esgoto) | contagem de escolas por característica e por infraestrutura | gráficos dinâmicos |
| `st.map(...)` | plota cada escola como um ponto | elemento novo do Projeto 4 (sem equivalente direto no painel do Excel) |
| `st.dataframe(...)` | lista as escolas que atendem aos filtros | lista de escolas filtrada |

## Uso de Inteligência Artificial

**Ferramenta utilizada:** Claude (Anthropic)

**Para que foi usada:** a partir do painel da Aula 21, para completar para testar combinações de filtros e para montar a primeira versão deste README.

**Exemplo de prompt utilizado:** * "nos ajude a repensar um novo filtro e estruturar o README.md"* 

**O que foi ajustado manualmente:**: Código e README.md

## Fonte de Dados

**Fonte oficial:** Censo Escolar 2024 (INEP)

**Link oficial:** https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar

**O que os dados representam:** as escolas em atividade em 30 municípios de quatro regiões do estado de São Paulo em 2024. Cada linha é uma escola, com suas características (dependência, localização), matrículas, infraestrutura e coordenadas geográficas (latitude e longitude, com a fonte indicada na coluna `fonte_coordenada`). A base foi adaptada do Censo Escolar para a disciplina.

**Estrutura:** colunas da base usadas no painel.

| Coluna | O que significa |
|---|---|
| `regiao` | região do estado: Região Metropolitana de SP, Baixada Santista, Litoral Norte ou Vale do Ribeira |
| `municipio` | município da escola |
| `escola` | nome da escola |
| `dependencia` | Federal, Estadual, Municipal ou Privada |
| `localizacao` | Urbana ou Rural |
| `matriculas` | total de matrículas da escola |
| `agua` | principal forma de abastecimento de água |
| `esgoto` | principal forma de esgotamento sanitário |
| `latitude`, `longitude` | posição da escola no mapa |
| `porte` | **criada no painel** com `classifica_porte`: pequena (até 200 matrículas), média (201 a 400) ou grande (mais de 400) |

## Participação do Grupo

**O que aprendemos com este projeto:** a transformar o painel do Excel em um programa em Python, usando o pandas para carregar e organizar os dados e o Streamlit para montar a página interativa. Aprendemos a criar filtros que recalculam todo o painel, a fazer gráficos de contagem com `value_counts()` e a documentar o projeto para que outra pessoa consiga instalar e rodar sem ter assistido às aulas.

**Papel de cada integrante**

- Ana Clara Oliveira: partiu do painel da Aula 21 para montar a versão final do `painel.py`, escreveu o README e publicou o projeto no GitHub.
- Marcely Macedo: ajudou a criar os filtros do painel (região, município e dependência) e a lógica que recalcula os indicadores, os gráficos, o mapa e a lista a cada mudança.
- Carina Lee: ajudou a fazer os gráficos de características (porte e localização) e de infraestrutura (água e esgoto) e organizou o código na ordem vista em aula.
- Jamily Cardoso: Ofereceu suporte ao desenvolvimento do projeto e às atividades realizadas pelo grupo
- Lara Morais: Ofereceu suporte ao desenvolvimento do projeto e às atividades realizadas pelo grupo
