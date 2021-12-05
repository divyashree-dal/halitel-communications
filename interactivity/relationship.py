import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
from dash import html

##############################################
"""
    File Usage: Page rendered on click of customer relationship information tab
"""


##############################################


def category4_tab():
    return html.Div(className="output-display", children=[
        html.H3('Customer Relationship variables', style={'text-align': 'center', 'color': 'rgb(145, 223, 210)'}),
        dcc.RadioItems(id="relationship_checklist", value="Contract",
                       options=[{"label": "Contract", "value": "Contract"},
                                {"label": "Tenure", "value": "tenure"},
                                {"label": "Partner", "value": "Partner"},
                                {"label": "Dependents", "value": "Dependents"}],
                       ),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        dbc.Row([
            dbc.Col([
                dbc.Spinner(dcc.Graph(id='relationship-main-graph'))]),
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        html.H4("Dependency among the relationship variables",
                style={'text-align': 'center', 'color': 'rgb(145, 223, 210)'}),
        html.H5("Click on portions of heatmap to notice changes in distplots and pie chart....",
                style={'text-align': 'center', 'color': 'white'}),

        dbc.Row(id='relationship', key="models", children=[
            dbc.Col([
                dbc.Spinner(dcc.Graph(id='relationship_graph'))
            ])
        ]),
        html.H5("Click on portions of heatmap to get tenure based on partner and dependents....",
                style={'text-align': 'center', 'color': 'white'}),

        dbc.Row(id='kde-key', key="models", children=[
            dbc.Col([
                dbc.Spinner(dcc.Graph(id='kde_relationship_graph')),
                dbc.InputGroup([
                    dbc.InputGroupAddon("Numerical Features", addon_type="prepend",
                                        style={'font-size': '20px',
                                               'color': 'rgb(145, 223, 210)'}),
                    dcc.Dropdown(id='numerical-tenure-dropdown', value='MonthlyCharges',
                                 options=[{'label': i, 'value': i} for i in ['MonthlyCharges', 'TotalCharges']])
                ], style={
                    'textAlign': 'center',
                    'width': '50%',
                    'color': 'black',
                    'margin-left': 100
                }),
            ], style={'margin-left': 120})
        ]),

        html.Hr(),

        html.H6("Slide through minimum and maximum tenure .... ", style={'text-align': 'center',
                                                                        'color': 'rgb(145, 223, 210)'}),

        dbc.Row(id='time-interval', children=[
            dcc.RangeSlider(
                id='tenure-stepper',
                min=0,
                max=72,
                value=[0, 72],
                step=None,
                marks={
                    0: {'label': '0', 'style': {'color': '#77b0b1'}},
                    12: {'label': '1 Year'},
                    24: {'label': '2 Years'},
                    36: {'label': '3 Years'},
                    48: {'label': '4 Years'},
                    60: {'label': '5 Years'},
                    72: {'label': '6 Years', 'style': {'color': '#f50'}}
                }
            )]),
        html.Hr(),

    ])


def about_relationship_tab():
    return html.Div(children=[
        html.H3('About', style={'color': 'rgb(145, 223, 210)'}),
        html.P('This tab renders information about the visualization of customer relationships')
    ])
