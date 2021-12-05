import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
from dash import dash_table
from dash import html

from preprocessing.load_file import read_dataset

##############################################
"""
    File Usage: Page rendered on click of dataset tab
"""
##############################################


def dataset_tab():
    churn_df = read_dataset()
    churn_df = churn_df.copy()

    data = {'Column Name': ['Customer ID', 'Gender', 'Senior Citizen', 'Partner', 'Dependents', 'Tenure',
                            'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                            'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
                            'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'],

            'Description': ['Primary key unique identification ID of a customer',
                            'An attribute to find whether customer is male of female',
                            'To find if customer if senior citizen(1) or not(0)',
                            'To find if customer has Partner(Yes) or not(No)',
                            'To find if customer has Dependents(Yes) or not(No)',
                            'To find the total number of months, a customer has stayed with the company',
                            'To find if customer has Phone Service(Yes) or not(No)',
                            'To find if customer has Multiple Lines (Yes) or not (No) or (No Phone Service)',
                            'To find the customer\'s Internet Service provider - DSL, Fibre Optic, No',
                            'To find if customer has online security(Yes) or not (No) or (No internet service)',
                            'To find if the customer has an online backup(Yes) or not (No), or (No internet service)',
                            'To find if the customer has device protection(Yes) or not (No) or (No internet service)',
                            'To find if the customer has tech support(Yes) or not (No) or (No internet service)',
                            'To find if the customer has streaming TV(Yes) or not(No) or (No internet service)',
                            'To find if the customer has streaming movies(Yes) or not(No) or (No internet service)',
                            'To find the contract agreement of the customer - Month-to-month, One year, or Two years',
                            'To find if the customer has paperless billing(Yes) or not (No)',
                            'To find the customer’s payment method - Electronic check, Mailed check, Bank transfer '
                            '(automatic), or Credit card (automatic)',
                            'To find the monthly charges of the customer',
                            'To find tne total amount charged to the customer',
                            'To find whether the customer churned(Yes) or not (No)'
                            ]}

    dataframe = pd.DataFrame(data)

    data1 = {'Count': ['Number of rows in Churn telecom dataset', 'Number of columns in Churn telecom dataset'],
             'Value': [f": {churn_df.shape[0]}",
                       f": {churn_df.shape[1]}"]}

    dataframe_row_col = pd.DataFrame(data1)

    ############
    # Table

    return html.Div(className="output-display", children=[

        dbc.Row([
            dbc.Col([
                html.H3('Dataset: Telecom Customer Churn Dataset', style={
                    'text-align': 'center'
                }),
                dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in churn_df.columns],
                    data=churn_df.to_dict('records'),

                    page_current=0,
                    page_size=20,
                    style_as_list_view=True,
                    style_header={
                        'backgroundColor': '#91dfd2',
                        'fontWeight': 'bold',
                        'color': 'black'
                    },
                    style_cell={
                        'minWidth': '140px',
                        'whiteSpace': 'normal',
                        'font_size': '13px',
                        'text_align': 'left',
                        'backgroundColor': '#12191C',
                        'border': '1px solid black',
                        'color': '#91dfd2'
                    },
                    style_table={
                        'overflowY': 'scroll',
                        'height': 600,
                        'width': 900,
                        'color': 'black',
                        'border': '1px solid white',
                    }
                )]
            )]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        dbc.Row([
            dbc.Col([
                html.Div(
                    [
                        dbc.Label("Want to know about dataset?",
                                  style={'font-size': '25px', 'text-align': 'center'}),

                        html.Br(),

                        dbc.Card([
                            dbc.CardHeader("Churn Columns and Description", id='card-header'),

                            html.Br(),

                            dbc.CardBody(
                                [
                                    dash_table.DataTable(
                                        id='table',
                                        columns=[{"name": i, "id": i} for i in dataframe.columns],
                                        data=dataframe.to_dict('records'),

                                        page_current=0,
                                        page_size=30,
                                        style_as_list_view=True,
                                        style_header={
                                            'backgroundColor': '#91dfd2',
                                            'fontWeight': 'bold',
                                            'color': 'black'
                                        },
                                        style_cell={
                                            'minWidth': '140px',
                                            'whiteSpace': 'normal',
                                            'font_size': '13px',
                                            'text_align': 'left',
                                            'backgroundColor': '#12191C',
                                            'border': '1px solid #91dfd2',
                                            'color': 'white'
                                        },
                                        style_table={
                                            'overflowY': 'scroll',
                                            'height': 600,
                                            'width': 1000,
                                            'color': 'black',
                                            'border': '1px solid white',
                                        }
                                    )

                                ], style={
                                    'minWidth': '140px',
                                    'whiteSpace': 'normal',
                                    'font_size': '13px',
                                    'text_align': 'left',
                                    'backgroundColor': '#12191C',
                                    'border': '1px solid white',
                                    'color': '#91dfd2'
                                }
                            ),
                        ])

                    ]),
            ])

        ]),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        dbc.Row([
            dbc.Col([
                html.Div(
                    [
                        html.Br(),

                        dbc.Label("Want to know about rows and columns count?!",
                                  style={'font-size': '25px', 'text-align': 'center'}),

                        html.Br(),

                        dbc.Card([
                            dbc.CardHeader("Dataset Rows & Columns", id='card-header'),

                            html.Br(),

                            dbc.CardBody(
                                [
                                    dash_table.DataTable(
                                        id='table',
                                        columns=[{"name": i, "id": i} for i in dataframe_row_col.columns],
                                        data=dataframe_row_col.to_dict('records'),

                                        page_current=0,
                                        page_size=3,
                                        style_as_list_view=True,
                                        style_header={
                                            'backgroundColor': '#91dfd2',
                                            'fontWeight': 'bold',
                                            'color': 'black'
                                        },
                                        style_cell={
                                            'minWidth': '140px',
                                            'whiteSpace': 'normal',
                                            'font_size': '13px',
                                            'text_align': 'left',
                                            'backgroundColor': '#12191C',
                                            'border': '1px solid #91dfd2',
                                            'color': 'white'
                                        },
                                        style_table={
                                            'height': 100,
                                            'width': 900,
                                            'color': 'black',
                                            'border': '1px solid white',
                                        }
                                    )
                                ]),

                        ]),
                    ])
            ])
        ]),

        html.Br(),
        html.Br(),

    ])

    ##########


def about_dataset_tab():
    return html.Div(children=[
        html.H3('About', style={'color': 'rgb(145, 223, 210)'}),
        html.P('This tab renders information about the telecom churn dataset w.r.t. rows and columns')
    ])
