import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import dcc

##############################################
"""
    File Usage: Page rendered on click of confusion matrix tab
    Confusion Matrix and Correlation Matrix
"""
##############################################


def confusion_matrix_tab():
    return html.Div(className="output-display", children=[

        # Title
        dbc.Row([
            dbc.Col([
                html.H1('Confusion Matrix',
                        style={'textAlign': 'center', 'margin': '10px', 'color': 'rgb(145, 223, 210)'})
            ], width=12)
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        html.H5("Click on the buttons to observe the model's confusion matrix....",  style={'textAlign': 'center'}),

        html.Br(),

        # Body
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Button('Decision Tree Classifier', id='btn-n-clicks-1',
                                style={'color': 'rgb(145, 223, 210)', 'margin-left': '10px',  'margin-bottom': '20px'}),
                    html.Button('Random Forest Classifier', id='btn-n-clicks-2',
                                style={'color': 'rgb(145, 223, 210)', 'margin-left': '10px'}),
                    html.Button('KNN Classifier', id='btn-n-clicks-3',
                                style={'color': 'rgb(145, 223, 210)', 'margin-left': '10px'}),
                    html.Button('Naive Bayes Classifier', id='btn-n-clicks-4',
                                style={'color': 'rgb(145, 223, 210)', 'margin-left': '10px'}),
                    html.Button('Logistic Regression', id='btn-n-clicks-5',
                                style={'color': 'rgb(145, 223, 210)', 'margin-left': '10px'}),
                    html.Button('XGBoost Classifier', id='btn-n-clicks-6',
                                style={'color': 'rgb(145, 223, 210)', 'margin-left': '10px'})
                ])
            ], width=12)
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        # 1. General graph
        dbc.Row([
            dbc.Col([
                dbc.Spinner(dcc.Graph(id='cm-main-graph'))]),
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        #################################
        # Title
        dbc.Row([
            dbc.Col([
                html.H1('Correlation Matrix',
                        style={'textAlign': 'center', 'margin': '10px', 'color': 'rgb(145, 223, 210)'})
            ], width=12)
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        # 1. General graph
        dbc.Row([
            dbc.Col(id="corr-id", key='corr', children=[
                dbc.Spinner(dcc.Graph(id='corr-main-graph'))]),
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

    ])


def about_confusion_matrix_tab():
    return html.Div(children=[
        html.H3('About', style={'color': 'rgb(145, 223, 210)'}),
        html.P('This tab renders information about the visualization of obtained confusion matrix')
    ])
