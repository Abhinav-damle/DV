import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

dfv = pd.read_csv(DATA_PATH.joinpath("Netflix.csv"))  # GregorySmith Kaggle
num_list = ['Min_length','Max_Length','Seasons','Episodes','IMDB_Rating']
v=['Major_Genre','Subgenre']


layout = html.Div([
    html.H1('Netflix Genre', style={"textAlign": "center"}),

    html.Div([
        html.Div(dcc.Dropdown(
            id='num-dropdown', value='Strategy', clearable=False,
            options=[{'label': x, 'value': x} for x in v]
        ), className='six columns'),

        html.Div(dcc.Dropdown(
            id='genre-dropdown', value='EU Sales', clearable=False,
            persistence=True, persistence_type='memory',
            options=[{'label': x, 'value': x} for x in num_list]
        ), className='six columns'),
    ], className='row'),

    dcc.Graph(id='my-bar', figure={}),
])


@app.callback(
    Output(component_id='my-bar', component_property='figure'),
    [Input(component_id='num-dropdown', component_property='value'),
     Input(component_id='genre-dropdown', component_property='value')]
)
def display_value(genre_chosen, num_chosen):
    fig = px.bar(dfv, x=genre_chosen, y=num_chosen, color=num_chosen)
    return fig