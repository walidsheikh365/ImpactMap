from dash import html
import dash_bootstrap_components as dbc
from app.helper import cards, datatable

layout = html.Div(
    style={
        "margin-left": 10,
        "margin-right": 10,
        "margin-bottom": 10,
        "margin-top": 10,
        "text-align": "center"
    },

    children=[

        # Logo
        html.Div(
            html.Img(
                id="logo",
                src="/assets/logo.png",
                style={
                    "height": "20%",
                    "width": "20%"
                }
            )
        ),

        html.Br(),

        # Subtitle
        html.Div(
            id="subtitle",
            children="A Dash app created by Group 1 for COMP0034"
        ),

        html.Br(),

        # Cards
        dbc.Row([
            dbc.Col(cards.card_map, width=12)
        ],
            className="g-0"
        ),

        dbc.Row([
            dbc.Col(cards.card_mass, width=6),
            dbc.Col(cards.card_year, width=6)
        ],
            className="g-0",
            align="center",
        ),

        dbc.Row([
            dbc.Col(cards.card_discovery, width=4),
            dbc.Col(cards.card_type_donut, width=4),
            dbc.Col(cards.card_group_tree, width=4)
        ],
            className="g-0"
        ),

        html.Br(),

        dbc.Row([
            dbc.Col(datatable.datatable, width=12)
        ],
            className="g-0"
        )
    ]
)
