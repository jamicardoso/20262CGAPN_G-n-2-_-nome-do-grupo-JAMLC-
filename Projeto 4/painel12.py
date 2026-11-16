#carregar o pandas e o streamlit
import pandas as pd
import streamlit as st

#função classificar porte
def classifica_porte(total):
	if total <=200:
		return "Pequena"
	elif total <=400:
		return "Média"
	else:
		return "Grande"


#Leitura de Dados
censo = pd.read_csv("escolas_sp_regioes_2024_geo.csv")

st.title("Painel de Escolas de Regiões de SP")
st.caption("adaptado do censo escolar 2024 (INEP)")

#filtrar dados da arquivo
regiao = st.selectbox("Escola a Regiao", ["Todas", "Região Metropolitana de SP", "Baixada Santista", "Litoral Norte", "Vale do Ribeira"])

if regiao != "Todas":
	censo = censo[censo["regiao"]==regiao]

#Filtro da dependência
dependencia = st.selectbox("Escolha a Dependência", ["Todas", "Federal", "Estadual", "Municipal", "Privada"])

if dependencia != "Todas":
    censo = censo[censo["dependencia"] == dependencia]

if len(censo) == 0:
    st.warning("Nenhuma escola encontrada com esses filtros. Troque a combinação.")
    st.stop()

#montagem das contagens e soma
col1, col2 = st.columns(2)

col1.metric("Qtde de escolas", len(censo))
col2.metric("Total de matriculas", censo["matriculas"].sum())

#grafico da contagem de escolas por infra
censo["porte"] = censo["matriculas"].apply(classifica_porte)

#grafico de porte
st.subheader("Escolas por Porte")
st.bar_chart(censo["porte"].value_counts())

#grafico de localização
st.subheader("Escolas por Localização (Urbana ou Rural)")
st.bar_chart(censo["localizacao"].value_counts())

#grafico de agua 
st.subheader("Escolas por Abastecimento de Água")
st.bar_chart(censo["agua"].value_counts())

#gráfico de esgoto
st.subheader("Escolas por Esgotamento Sanitário")
st.bar_chart(censo["esgoto"].value_counts())

## plotar as escolas no mapa
st.subheader ("Mapa das escolas")
st.map(censo[["latitude", "longitude"]])

#Exibir lista das esoclas
st.subheader("Lista das Escolas")
st.dataframe(censo[["municipio", "escola", "matriculas", "porte"]])