import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
from dash import html

##############################################
"""
    File Usage: Page rendered on click of customer demographic information tab
"""
##############################################


def category1_tab():
    return html.Div(className="output-display", children=[
        html.H2('Customer Demographic Features', style={'text-align': 'center', 'color': 'rgb(145, 223, 210)'}),
        dcc.RadioItems(id="demographic_checklist", value="gender",
                       options=[{"label": "Gender", "value": "gender"},
                                {"label": "Senior Citizen", "value": "SeniorCitizen"},
                                {"label": "Both", "value": "Both"}],
                       labelStyle={'display': 'inline-block'}

                       ),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        # 1. General graph
        dbc.Row([
            dbc.Col([
                dbc.Spinner(dcc.Graph(id='demographic-main-graph'))]),
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        # 2. Advanced graph between senior citizen and tenure and total charges

        html.Div(children=[
            html.H3('Let\'s find the total tenure of senior citizens along with their total charges',
                    style={'text-align': 'center', 'color': 'rgb(145, 223, 210)'}),
            html.P(' Observation : Less number of senior citizens with higher tenure will be churned '
                   'irrespective of heavy total charges.'),
            html.Br(),
            dbc.Row(id='senior-tenure-id', key="senior_tenure", children=[
                dbc.Col([
                    dbc.Spinner(dcc.Graph(id='senior-tenure-main-graph'))]),
            ]),
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        dbc.Row([
            dbc.Label("Select demographic Columns", style={'font-size': '22px','color': 'rgb(145, 223, 210)'}),
            dbc.Col([
                dbc.InputGroup([
                    dcc.Dropdown(id="demo_select", value="gender",
                                 options=[
                                     {'label': 'Gender', 'value': 'gender'},
                                     {'label': 'SeniorCitizen', 'value': 'SeniorCitizen'},
                                 ]),
                ])
            ], style={
                'textAlign': 'center',
                'width': '20%',
                'display': 'inline-block',
                'padding': 10,
                'color': 'black'
            }),
        ]),

        dbc.Row(id='senior-tenure-id', key="senior_tenure", children=[
            dbc.Col([
                dbc.Spinner(dcc.Graph(id='tenure-gender-age'))]),
        ]),

        html.H6("Slide through the tenure .... ", style={'text-align': 'center',
                                                                         'color': 'rgb(145, 223, 210)'}),

        html.Div([
            dcc.Slider(
                id='tenure-slider',
                min=0,
                max=72,
                step=None,
                value=0,
                marks={
                    0: {'label': '0', 'style': {'color': '#77b0b1'}},
                    12: {'label': '1 Year'},
                    24: {'label': '2 Years'},
                    36: {'label': '3 Years'},
                    48: {'label': '4 Years'},
                    60: {'label': '5 Years'},
                    72: {'label': '6 Years', 'style': {'color': '#f50'}}
                },
                tooltip={"placement": "bottom", "always_visible": True}
            ),
        ]),

    ])


def about_demographic_tab():
    return html.Div(children=[
        html.H3('About', style={'color': 'rgb(145, 223, 210)'}),
        html.P('This tab renders information about the characteristics of a particular customer')
    ])
