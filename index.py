from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_gif_component as gif

from app import app

from apps import homepage , Netflix
import dash

navbar = dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row([
                        dbc.Col([
                            dbc.NavbarBrand("Netflix", className="ms-2")
                        ],
                        width={"size":"auto"})
                    ],
                    align="center",
                    className="g-0"),

                    dbc.Row([
                        dbc.Col([
                            dbc.Nav([
                                dbc.NavItem(dbc.NavLink("Home", href="/")),
                                #dbc.NavItem(dbc.NavLink("Fundamentals", href="/fundamentals")),
                                dbc.NavItem(dbc.DropdownMenu(
                                       children=[
                                           dbc.DropdownMenuItem("Home", href="/home"),
                                           dbc.DropdownMenuItem("Netflix", href="/Netflix"),
                                       ],
                                        nav=True,
                                        in_navbar=True,
                                        label="options",
                                )),

    
                            ],
                            navbar=True
                            )
                        ],
                        width={"size":"auto"})
                    ],
                    align="center"),
                    dbc.Col(dbc.NavbarToggler(id="navbar-toggler", n_clicks=0)),
                    
                    dbc.Row([
                        dbc.Col(
                             dbc.Collapse(
                                dbc.Nav([
                                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi-github"), href="https://github.com/siddharthajuprod07/algorithms/tree/master/plotly_deep_learning_app",external_link=True) ),
                                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi bi-twitter"), href="https://twitter.com/splunk_ml",external_link=True) ),
                                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi-youtube"), href="https://www.youtube.com/channel/UC7J8myLv3tPabjeocxKQQKw",external_link=True) ),
        
                                ]
                                ),
                                id="navbar-collapse",
                                is_open=False,
                                navbar=True
                             )
                        )
                    ],
                    align="center")
                ],
            fluid=True
            ),
    color="primary",
    dark=True
)


@dash.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return homepage.layout
    elif pathname == '/Netflix':
        return Netflix.layout
    else:
        return homepage.layout

if __name__ == '__main__':
    app.run_server(port = 8079, debug=False)