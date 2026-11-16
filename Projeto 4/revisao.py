#carregar o pandas na memória
import pandas as pd

#criar uma função que classifica o porte pelo numero de matricula
def classifica_porte(total):
	if total <=200:
		return "pequena"
	elif total <=400:
		return "média"
	else:
		return "grande"

#carregar arquivo CSV com a lista das escolas
censo = pd.read_csv("escolas_sp_regioes_2024_geo.csv")

#mostrar as primeiras linhas
print(censo.head())

#Fazer contagem por coluna
print(censo["regiao"].value_counts())

#filtrar escolas municipais
municipais = censo[censo["dependencia"]=="municipal"]
print(municipais.head())

dependencia = st.selectbox("Escolha a Dependência", ["Todas", "Federal", "Estadual", "Municipal", "Privada"])

if dependencia != "Todas":
    censo = censo[censo["dependencia"] == dependencia]

#fazer soma de uma coluna do Dataframe: Matriculas
print("Matriculas Totais: ", censo["matriculas"].sum())
print("Matriculas só Municipais: ", municipais["matriculas"].sum())

#criar uma nova coluna do Dataframe usando a função classidica_porte
censo["porte"] = censo["matriculas"].apply(classifica_porte)
print(censo["porte"].value_counts())

#ficar na tela
input("Digite enter para fechar")