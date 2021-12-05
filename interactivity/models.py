import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import dcc

##############################################
"""
    File Usage: Page rendered on click of Classification Models information tab
"""
##############################################


def models_tab():
    return html.Div(className="output-display", children=[

        # Title
        dbc.Row([
            dbc.Col([
                html.H3('Classification Models', style={'textAlign': 'center', 'color': 'rgb(145, 223, 210)'})
            ], width=12)
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        dbc.Row(id='model-id', key="models", children=[
            dbc.Col([
                dbc.Spinner(dcc.Graph(id='plotly-main-graph'))]),
        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        html.Div([
            # Title
            dbc.Row([
                dbc.Col([
                    html.H3('Basic binary ROC curve', style={'textAlign': 'center', 'color': 'rgb(145, 223, 210)'})
                ], width=12)
            ]),

            dcc.Dropdown(id="auc-dropdown", value="Decision_Tree",
                         options=[
                             {"label": "Decision Tree Model", "value": "Decision_Tree"},
                             {"label": "Random Forest Model", "value": "Random_Forest"},
                             {"label": "KNN Model", "value": "Knn"},
                             {"label": "Naive Bayes Model", "value": "Naive_Bayes"},
                             {"label": "Logistic Regression Model", "value": "Logistic_Regression"},
                             {"label": "XGBoost Model", "value": "Xg_Boost"}
                         ], style={'textAlign': 'center',
                                   'color': 'black',
                                   'width': '60%', 'margin-left': 160}),
        ]),

        html.Br(),

        # 4 c.To display plotly figures
        dbc.Row([
            dbc.Col([
                dbc.Spinner(dcc.Graph(id='auc-curve'))]),
        ]),

        html.Br(),

    ])


def about_models_tab():
    return html.Div(children=[
        html.H3('About', style={'color': 'rgb(145, 223, 210)'}),
        html.P('This tab renders information about the different classification models used for prediction')
    ])
