from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import os

def categoria_salario_acima_50k(coluna):
    if coluna == ' >50K':
        validado = 1
    else:
        validado = 0
    return validado

def categoria_salario_abaixo_ou_igual_50k(coluna):
    if coluna == ' <=50K':
        validado = 1
    else:
        validado = 0
    return validado

df = pd.read_csv('salary.csv')
df['Ganham_acima_de_50k'] = df['salary'].apply(categoria_salario_acima_50k)
df['Ganham_abaixo_ou_50k'] = df['salary'].apply(categoria_salario_abaixo_ou_igual_50k)
df['Unidade'] = 1

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

fig = px.pie(df, names='sex', title="Distribuição Geral dos registros por sexo")
fig2 = px.pie(df, names='salary', title="Distribuição Geral dos registros por faixa de salário")


# Seção do Layout
app.layout = html.Div(children=[

    html.H1(children=['Análise de salários da base kaggle', dbc.Badge("", className="ms-1")]),

    html.H3(children=['Dashboard', dbc.Badge("", className="ms-1")], id='Subtitulo'),

    html.Div(children=[
        dcc.Graph(id='distribuicao_geral_salario', figure=fig2)
        ], style={"float": "left"}),

    html.Div(children=[
        dcc.Graph(id='distribuicao_geral_sexo', figure=fig),
        ], style={"float": "right"}),  

], style={"text-align": "center"})


if __name__ == '__main__':
    app.run_server(debug=True)