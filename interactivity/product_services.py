import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
from dash import html

##############################################
"""
    File Usage: Page rendered on click of product services information tab
"""


##############################################


def category3_tab():
    return html.Div(className="output-display", children=[
        html.H3('Different Product Services', style={'text-align': 'center', 'color': 'rgb(145, 223, 210)'}),

        dcc.RadioItems(id="services_checklist", value="PhoneService",
                       options=[{"label": "PhoneService", "value": "PhoneService"},
                                {"label": "MultipleLines", "value": "MultipleLines"},
                                {"label": "InternetService", "value": "InternetService"},
                                {"label": "OnlineSecurity", "value": "OnlineSecurity"},
                                {"label": "OnlineBackup", "value": "OnlineBackup"},
                                {"label": "DeviceProtection", "value": "DeviceProtection"},
                                {"label": "TechSupport", "value": "TechSupport"},
                                {"label": "StreamingTV", "value": "StreamingTV"},
                                {"label": "StreamingMovies", "value": "StreamingMovies"}],
                       # labelStyle={'display': 'inline-block'}

                       ),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),
        dbc.Row([
            dbc.Col([
                dbc.Spinner(dcc.Graph(id='services-main-graph'))]),
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        dbc.Row(id='internet-services', key="internetServices", children=[
            html.Div(
                "This three quadrant subplot depicts churn and non churn frequency for Group. "
                "A Combination of Columns which are Online "
                "Security Online Backup, Streaming Tv and Streaming Movies is called a Group"),

            html.H5("Hover over any segment", style={'text-align': 'center', 'color': 'rgb(145, 223, 210)'}),
            dbc.Col([
                dcc.Graph(id='internetServicesMethod')]),
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),
    ])


def about_services_tab():
    return html.Div(children=[
        html.H3('About', style={'color': 'rgb(145, 223, 210)'}),
        html.P('This tab renders information about the different services used by the customer')
    ])
