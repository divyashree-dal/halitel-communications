import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
from dash import html


##############################################
"""
    File Usage: Page rendered on click of billing information tab
"""
##############################################


def category2_tab():
    return html.Div(className="output-display", children=[
        html.H2('Customer Billing Information', style={'text-align': 'center', 'color': 'rgb(145, 223, 210)'}),

        # 1. Basic graphs
        dcc.RadioItems(id="billing_checklist", value="MonthlyCharges",
                       options=[{"label": "Monthly Charges", "value": "MonthlyCharges"},
                                {"label": "Total Charges", "value": "TotalCharges"},
                                {"label": "Payment Method", "value": "PaymentMethod"},
                                {"label": "PaperlessBilling", "value": "PaperlessBilling"}],
                       ),

        html.Div(
            [
                html.Hr(style={'border-top': 'dotted 1px'}),
            ]
        ),

        dbc.Row([
            dbc.Col([
                dbc.Spinner(dcc.Graph(id='billing-main-graph'))]),
        ]),

        html.Div(
            [
                html.Hr(style={'color': '', 'border-top': 'dotted 1px'})
            ]
        ),

        # 2. Advanced graph between senior citizen and tenure and total charges

        html.Div(children=[

            html.H3('Let\'s check mean Monthly charges depending on contract agreement',
                    style={'text-align': 'center', 'color': 'rgb(145, 223, 210)'}),
            html.Br(),
            html.P(' Observation : If we look at the churn based on monthly costs split by contract types we can'
                   ' see that the trend is obviously that higher paying customers, on average, are churning.'
                   'We can notice relationship between the higher average cost and the churn rate. '
                   'In all contract types the customers that churn typically have a higher monthly payment.'),
            html.Br(),
            dbc.Row(id='contract-monthly-id', key="contract_monthly", children=[
                dbc.Col([
                    dbc.Spinner(dcc.Graph(id='contract-monthly-main-graph'))]),
            ]),
        ]),

        html.Div(
            [
                html.Hr(style={'color': '', 'border-top': 'dotted 1px'})
            ]
        ),

        html.H5('Click on payment method and churn...', style={'text-align': 'center', 'color': '#ffffff'}),

        dbc.Row(id='payment-method', key="payment-key", children=[
            dbc.Col([
                dcc.Graph(id='payment-method-main-graph')]),
        ]),

        dbc.Row([
            dbc.Col([
                html.Div(id='payment-method-contract')]),
        ]),

        html.Div(
            [
                html.Hr(style={'color': '', 'border-top': 'dotted 1px'})
            ]
        ),

        dbc.Row(id='payment-strip', key="models", children=[
            dbc.Col([
                dbc.Spinner(dcc.Graph(id='plotly-strip'))
            ], style={
                'display':'inline-block', 'margin-left':120
            })
        ]),
        html.Hr(),

    ])


def about_billing_tab():
    return html.Div(children=[
        html.H3('About', style={ 'color': 'rgb(145, 223, 210)'}),
        html.P('This tab renders information about the vivid billing information utilized by customers')
    ])
