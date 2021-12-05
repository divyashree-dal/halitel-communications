import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc

##############################################
"""
    File Usage: Page rendered on click of interactive prediction tab
"""
##############################################


def prediction_tab():
    return html.Div(className="output-display", children=[

        # Title
        dbc.Row([
            dbc.Col([
                html.H1('Interactive Prediction',
                        style={'textAlign': 'center', 'margin': '10px', 'color': 'rgb(145, 223, 210)'})
            ], width=12)
        ]),

        html.Div(
            [
                html.Hr(style={'color': ''})
            ]
        ),

        html.Div(
            [
                dbc.Card([
                    dbc.CardBody(
                        [
                            ########## Customer demographic features  ############

                            # Title
                            dbc.Row([
                                dbc.Label("Demographic Columns", style={'font-size': '22px'}),
                                dbc.Col([

                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Gender", addon_type="prepend", style={'font-size': '20px',
                                                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="gender_select", value="female",
                                                     options=[
                                                         {'label': 'Male', 'value': 'male'},
                                                         {'label': 'Female', 'value': 'female'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([

                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Senior Citizen", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="senior_citizen_select", value="Yes",
                                                     options=[
                                                         {'label': 'Yes', 'value': 'Yes'},
                                                         {'label': 'No', 'value': 'No'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                })

                            ]),

                            html.Div(
                                [
                                    html.Hr(style={'color': ''})
                                ]
                            ),

                            ########## Customer Services Information ############

                            dbc.Row([
                                dbc.Label("Product Services", style={'font-size': '22px'}),
                                dbc.Col([
                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Phone Service", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="phone_service_select", value="Yes",
                                                     options=[
                                                         {'label': 'Yes', 'value': 'Yes'},
                                                         {'label': 'No', 'value': 'No'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([

                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Multiple Lines", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="multiple_line_select", value="No",
                                                     options=[
                                                         {'label': 'Yes', 'value': 'Yes'},
                                                         {'label': 'No', 'value': 'No'},
                                                         {'label': 'No Phone Service', 'value': 'No_phone_service'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([

                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Internet Service", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="internet_service_select", value="No",
                                                     options=[
                                                         {'label': 'DSL', 'value': 'DSL'},
                                                         {'label': 'Fibre optic', 'value': 'Fibre_optic'},
                                                         {'label': 'No', 'value': 'No'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([

                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Online Security", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="online_security_select", value="No",
                                                     options=[
                                                         {'label': 'Yes', 'value': 'Yes'},
                                                         {'label': 'No', 'value': 'No'},
                                                         {'label': 'No Internet Service',
                                                          'value': 'no_internet_service'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([

                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Online Backup", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="online_backup_select", value="No",
                                                     options=[
                                                         {'label': 'Yes', 'value': 'Yes'},
                                                         {'label': 'No', 'value': 'No'},
                                                         {'label': 'No Internet Service',
                                                          'value': 'no_internet_service'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([

                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Device Protection", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="device_protection_select", value="No",
                                                     options=[
                                                         {'label': 'Yes', 'value': 'Yes'},
                                                         {'label': 'No', 'value': 'No'},
                                                         {'label': 'No Internet Service',
                                                          'value': 'no_internet_service'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([

                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Tech Support", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="tech_support_select", value="No",
                                                     options=[
                                                         {'label': 'Yes', 'value': 'Yes'},
                                                         {'label': 'No', 'value': 'No'},
                                                         {'label': 'No Internet Service',
                                                          'value': 'no_internet_service'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([

                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Streaming TV", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="streaming_tv_select", value="No",
                                                     options=[
                                                         {'label': 'Yes', 'value': 'Yes'},
                                                         {'label': 'No', 'value': 'No'},
                                                         {'label': 'No Internet Service',
                                                          'value': 'no_internet_service'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([

                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Streaming Movies", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="streaming_movies_select", value="No",
                                                     options=[
                                                         {'label': 'Yes', 'value': 'Yes'},
                                                         {'label': 'No', 'value': 'No'},
                                                         {'label': 'No Internet Service',
                                                          'value': 'no_internet_service'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                })

                            ]),

                            html.Div(
                                [
                                    html.Hr(style={'color': ''})
                                ]
                            ),

                            ########## Customer Relationship Information ############

                            dbc.Row([
                                dbc.Label("Relationship", style={'font-size': '22px'}),
                                dbc.Col([
                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Contract", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="contract_select", value="Month-to-month",
                                                     options=[
                                                         {'label': 'Month-to-Month', 'value': 'Month-to-month'},
                                                         {'label': 'One Year', 'value': 'One year'},
                                                         {'label': 'Two Year', 'value': 'Two year'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([
                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Partner", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="partner_select", value="Yes",
                                                     options=[
                                                         {'label': 'Yes', 'value': 'Yes'},
                                                         {'label': 'No', 'value': 'No'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([
                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Dependents", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="dependents_select", value="Yes",
                                                     options=[
                                                         {'label': 'Yes', 'value': 'Yes'},
                                                         {'label': 'No', 'value': 'No'},
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

                            html.Div(
                                [
                                    html.Hr(style={'color': ''})
                                ]
                            ),

                            ########## Customer Billing Information ############

                            dbc.Row([
                                dbc.Label("Billing", style={'font-size': '22px'}),
                                dbc.Col([
                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Payment Method", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="payment_method_select", value="Bank Transfer(automatic)",
                                                     options=[
                                                         {'label': 'Bank Transfer(automatic)',
                                                          'value': 'Bank Transfer(automatic)'},
                                                         {'label': 'Credit card(automatic)',
                                                          'value': 'Credit card(automatic)'},
                                                         {'label': 'Electronic Check', 'value': 'Electronic Check'},
                                                         {'label': 'Mailed Check', 'value': 'Mailed Check'},
                                                     ]),
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '30%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([
                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Paperless Billing", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dcc.Dropdown(id="paperless_method_select", value="Yes",
                                                     options=[
                                                         {'label': 'Yes',
                                                          'value': 'Yes'},
                                                         {'label': 'No',
                                                          'value': 'No'}
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

                            html.Div(
                                [
                                    html.Hr(style={'color': ''})
                                ]
                            ),

                            ########## Customer Entry Information ############

                            dbc.Row([
                                dbc.Label("Enter below", style={'font-size': '22px'}),
                                dbc.Col([
                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Monthly Charges ($)", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dbc.Input(id='monthly_charges', placeholder='Amount', type='float',
                                                  value='60.12')
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([
                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Total Charges ($)", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dbc.Input(id='total_charges', placeholder='Amount', type='float',
                                                  value='160.12')
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                                dbc.Col([
                                    dbc.InputGroup([
                                        dbc.InputGroupAddon("Tenure", addon_type="prepend",
                                                            style={'font-size': '20px',
                                                                   'color': 'rgb(145, 223, 210)'}),
                                        dbc.Input(id='tenure', placeholder='Number(years)', type='float',
                                                  value='2')
                                    ])
                                ], style={
                                    'textAlign': 'center',
                                    'width': '20%',
                                    'display': 'inline-block',
                                    'padding': 10,
                                    'color': 'black'
                                }),

                            ]),

                            html.Div(
                                [
                                    html.Hr(style={'color': ''})
                                ]
                            ),

                            ### Buttons for Prediction
                            dbc.Card([
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            html.H5("Click on the button to see the probability of churn...."),
                                            dbc.Button("PREDICT", id='prediction_button', className='prediction-button',
                                                       style={'width': '250px', 'color': 'rgb(145, 223, 210)',
                                                              'align-items': 'center', 'fontWeight': 'bold',
                                                              'fontSize': '20px'})
                                        ], style={
                                            'text-align': 'center',
                                            'justify-content': 'center', 'margin-right': '10%'
                                        }),

                                        html.Div(
                                            [
                                                html.Hr(style={'color': ''})
                                            ]
                                        ),
                                    ]),

                                    dbc.Row([
                                        dbc.Card([
                                            dbc.CardBody([
                                                dbc.Spinner(
                                                    html.H3(id='logistic_regression_output',
                                                            children="?",
                                                            style={'color': 'rgb(145, 223, 210)',
                                                                   'text-align': 'center'}),
                                                    spinner_style={'margin-bottom': '5px'}
                                                ),
                                                html.P("LOGISTIC REGRESSION"),
                                            ]),
                                        ]),
                                        dbc.Card([
                                            dbc.CardBody([
                                                dbc.Spinner(
                                                    html.H3(id='decision_tree_output',
                                                            children="?",
                                                            style={'color': 'rgb(145, 223, 210)',
                                                                   'text-align': 'center'}),
                                                    spinner_style={'margin-bottom': '5px'}
                                                ),
                                                html.P("DECISION TREE CLASSIFIER"),
                                            ]),
                                        ]),
                                        dbc.Card([
                                            dbc.CardBody([
                                                dbc.Spinner(
                                                    html.H3(id='knn_output',
                                                            children="?",
                                                            style={'color': 'rgb(145, 223, 210)',
                                                                   'text-align': 'center'}),
                                                    spinner_style={'margin-bottom': '5px'}
                                                ),
                                                html.P("KNN CLASSIFIER"),
                                            ]),
                                        ]),

                                    ], style={'display': 'flex', 'justify-content': 'space-between'}),

                                    dbc.Row([
                                        dbc.Card([
                                            dbc.CardBody([
                                                dbc.Spinner(
                                                    html.H3(id='nv_output',
                                                            children="?",
                                                            style={'color': 'rgb(145, 223, 210)',
                                                                   'text-align': 'center'}),
                                                    spinner_style={'margin-bottom': '5px'}
                                                ),
                                                html.P("NAIVE BAYES CLASSIFIER"),
                                            ]),
                                        ]),

                                        dbc.Card([
                                            dbc.CardBody([
                                                dbc.Spinner(
                                                    html.H3(id='random_forest_output',
                                                            children="?",
                                                            style={'color': 'rgb(145, 223, 210)',
                                                                   'text-align': 'center'}),
                                                    spinner_style={'margin-bottom': '5px'}
                                                ),
                                                html.P("RANDOM FOREST CLASSIFIER")
                                            ]),

                                        ]),

                                        dbc.Card([
                                            dbc.CardBody([
                                                dbc.Spinner(
                                                    html.H3(id='xg_boost_output',
                                                            children="?",
                                                            style={'color': 'rgb(145, 223, 210)',
                                                                   'text-align': 'center'}),
                                                    spinner_style={'margin-bottom': '5px'}
                                                ),
                                                html.P("XG BOOST CLASSIFIER"),
                                            ]),
                                        ]),
                                    ], style={'display': 'flex', 'justify-content': 'space-between'}),

                                ])
                            ])
                        ])
                ]),

            ]),

    ]),


def about_prediction_tab():
    return html.Div(children=[
        html.H3('About', style={'color': 'rgb(145, 223, 210)'}),
        html.P('This tab renders an interactive prediction, where an audience can select the required values, '
               'and can check if the customer is churned or not')
    ])
