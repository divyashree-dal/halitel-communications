import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import dcc

##############################################
"""
    File Usage: Page rendered on click of Introduction tab
"""


##############################################


def introduction_tab():
    categorical_features = ['gender', 'SeniorCitizen',
                            'PhoneService', 'StreamingMovies', 'StreamingTV', 'TechSupport', 'OnlineBackup',
                            'OnlineSecurity', 'InternetService', 'MultipleLines', 'DeviceProtection',
                            'PaymentMethod', 'PaperlessBilling',
                            'Contract', 'Partner', 'Dependents', ]

    numerical_features = ['MonthlyCharges', 'TotalCharges']

    churn_boolean = ['Churn', 'Not Churn']

    return html.Div(className="output-display", children=[

        # Title
        dbc.Row([
            dbc.Col([
                html.H2('What is customer churning?',
                        style={'textAlign': 'center', 'color': 'rgb(145, 223, 210)'})
            ])
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        # Introduction detail
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody(
                        [
                            html.Ul(children=[
                                html.Li('Subscription-based companies emphasize customer retention as one of their key '
                                        'performance indicators.'),
                                html.Li(
                                    'It\'s extremely competitive, especially in the SaaS market, where customers can '
                                    'pick '
                                    'from a variety of providers.'),
                                html.Li('Churn is an indication of business health for businesses with subscribers '
                                        'and paying '
                                        'customers')
                            ])
                        ])
                ])
            ])
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        # Introduction interactivity

        dbc.Row([

            # 1. dropdown for categorical features
            dbc.Col([
                # html.Div('Categorical Features', className="bold font-sm"),
                # dbc.Label("Categorical Features", style={'font-size': '22px'}),
                dbc.InputGroup([
                    dbc.InputGroupAddon("Categorical Features", addon_type="prepend",
                                        style={'font-size': '20px',
                                               'color': 'rgb(145, 223, 210)'}),
                    dcc.Dropdown(id='categorical-dropdown', value='gender',
                                 options=[{'label': i, 'value': i} for i in categorical_features])
                ]),
            ], style={
                'textAlign': 'center',
                'width': '20%',
                'display': 'inline-block',
                'padding': 10,
                'margin-left': 120,
                'color': 'black'
            }),

            # 2. dropdown for numerical features
            dbc.Col([
                # html.Div('Numerical Features', className="bold font-sm"),
                dbc.InputGroup([
                    dbc.InputGroupAddon("Numerical Features", addon_type="prepend",
                                        style={'font-size': '20px',
                                               'color': 'rgb(145, 223, 210)'}),
                    dcc.Dropdown(id='numerical-dropdown', value='MonthlyCharges',
                                 options=[{'label': i, 'value': i} for i in numerical_features])
                ])
            ], style={
                'textAlign': 'center',
                'width': '20%',
                'display': 'inline-block',
                'padding': 10,
                'color': 'black'
            }),

            # 3 . dropdown for churn or not churn
            dbc.Col([
                # html.Div([
                # html.Div('Churn or Not Churn?!', className="bold font-sm"),
                dbc.InputGroup([
                    dbc.InputGroupAddon("Churn or Not Churn?!", addon_type="prepend",
                                        style={'font-size': '20px',
                                               'color': 'rgb(145, 223, 210)'}),
                    dcc.Dropdown(id='churn-binary-dropdown', value='Churn',
                                 options=[{'label': i, 'value': i} for i in churn_boolean])
                ])
            ], style={
                'textAlign': 'center',
                'width': '20%',
                'display': 'inline-block',
                'padding': 10,
                'color': 'black'
            }),
        ]),

        dbc.Row([
            # Graph percentage
            dbc.Spinner(dcc.Graph(id='introduction-first-graph')),
            dbc.Spinner(dcc.Graph(id='introduction-second-graph'))
        ], style={
            'display': 'flex', 'width': '100%', 'justify-content': 'space-between'
        }),

        dbc.Row([
            # Pie monthly graphs
            dbc.Spinner(dcc.Graph(id='introduction-third-no-churn-graph')),
            dbc.Spinner(dcc.Graph(id='introduction-fourth-churn-graph'))
        ], style={
            'display': 'flex', 'width': '100%', 'justify-content': 'space-between'
        })

    ])


def about_introduction_tab():
    return html.Div(children=[
        html.H3('About', style={'color': 'rgb(145, 223, 210)'}),
        html.P('This tab renders information about the definition of customer churn')
    ])
