import dash
import os
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash import no_update
import sys
file = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0])
dir_name = os.path.dirname(os.path.dirname(file))
sys.path.append(dir_name)
from dash.dependencies import Input, Output, State
from interactivity.billing_information import category2_tab, about_billing_tab
from interactivity.confusion_matrix import confusion_matrix_tab, about_confusion_matrix_tab
from interactivity.customer_demographic import category1_tab, about_demographic_tab
from interactivity.dataset_tab import dataset_tab, about_dataset_tab
from interactivity.header import navigation_bar
from interactivity.introduction import introduction_tab, about_introduction_tab
from interactivity.models import models_tab, about_models_tab
from interactivity.prediction import prediction_tab, about_prediction_tab
from interactivity.product_services import category3_tab, about_services_tab
from interactivity.relationship import category4_tab, about_relationship_tab
from preprocessing.load_file import read_dataset
from visualizations.advanced_graphs import plotly_tenure_total_charges_seniorCitizen, plotly_contract_percentages, \
    internetServices, kde_relationship, relationship, graph_plotly_strip
from visualizations.basic_graphs import plotly_bar_plot_chart, plotly_line_plot_chart
from visualizations.confusion_matrix_graph import confusion_matrix_graph
from visualizations.corr_matrix import corrrelation_matrix
from visualizations.introduction_page_graphs import plot_pie_percentage_cat_count, numerical_cat_churn_box_plot, \
    pie_plots
from visualizations.models_curve import models_auc_curve
from visualizations.models_table import plotly_models_table, getAllModels
from visualizations.prediction import models_predict
from visualizations.template_graphs import plotly_payment_method, plotly_contract, plotly_pie_tenure, plotly_fetch_mean

##############################################
"""
    File Usage: Main dash page
"""
##############################################

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport",
                "content": "width=device-width, initial-scale=1"}]
)

# To read the dataset
churn_df = read_dataset()
churn_df = churn_df.copy()
models_dict, classification_models = getAllModels()
tab_style = {
    'backgroundColor': '#12191C',
    'letterSpacing': '1px',
    'color': 'inherit',
    'border': '0',
    'display': 'flex',
    'flexDirection': 'column',
    'alignItems': 'flex-start',
    'justifyContent': 'center',
    'cursor': 'pointer',
    'height': '18px',
    'width': '200px',

}

tab_selected_style = {
    **tab_style,
    'backgroundColor': '#91dfd2',
    'color': '#1E2A30',
}

button_counts = {i: 0 for i in ['btn1', 'btn2', 'btn3', 'btn4', 'btn5', 'btn6']}


def childTabs():
    list_of_tabs = ['Introduction', 'Dataset', 'Demographic',
                    'Billing', 'Services', 'Relationship', 'Models', 'CFMatrix', 'Prediction']
    dash_childs = []

    for i in range(len(list_of_tabs)):
        dash_childs.append(dcc.Tab(
            id=list_of_tabs[i],
            label=f"{i + 1}. {list_of_tabs[i]}",
            value=list_of_tabs[i],
            selected_style=tab_selected_style,
            style=tab_style,
            selected_className="custom-tab--selected",
        ))
    return dash_childs


def verticalTabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="Introduction",
                className="custom-tabs",
                children=childTabs(),
                vertical=True
            ),
            html.Div(
                id="about-tabs")
        ],
    )


# callbacks for the left panel tabs
@app.callback(Output('output-tab', 'children'),
              Input('app-tabs', 'value'))
def render_content(tab):
    if tab == 'Introduction':
        return introduction_tab()

    elif tab == 'Dataset':
        return dataset_tab()

    elif tab == 'Demographic':
        return category1_tab()

    elif tab == 'Models':
        return models_tab()

    elif tab == 'Billing':
        return category2_tab()

    elif tab == 'Services':
        return category3_tab()

    elif tab == 'Relationship':
        return category4_tab()

    elif tab == 'CFMatrix':
        return confusion_matrix_tab()

    elif tab == 'Prediction':
        return prediction_tab()


# callbacks for about tabs
@app.callback(Output('about-tabs', 'children'),
              Input('app-tabs', 'value'))
def about_content(tab):
    if tab == 'Introduction':
        return about_introduction_tab()

    elif tab == 'Dataset':
        return about_dataset_tab()

    elif tab == 'Demographic':
        return about_demographic_tab()

    elif tab == 'Models':
        return about_models_tab()

    elif tab == 'Billing':
        return about_billing_tab()

    elif tab == 'Services':
        return about_services_tab()

    elif tab == 'Relationship':
        return about_relationship_tab()

    elif tab == 'CFMatrix':
        return about_confusion_matrix_tab()

    elif tab == 'Prediction':
        return about_prediction_tab()


# Callback : To display the plotly chart of the demographic features
@app.callback(Output('demographic-main-graph', "figure"),
              [Input('demographic_checklist', 'value')])
def update_fig(column):
    return plotly_bar_plot_chart(column)


# Callback : To display the plotly chart of the billing information
@app.callback(Output('billing-main-graph', "figure"),
              [Input('billing_checklist', 'value')])
def update_fig(column):
    if column == 'MonthlyCharges' or column == 'TotalCharges':
        return plotly_line_plot_chart(column)
    return plotly_bar_plot_chart(column)


# Callback : To display the plotly chart of the product services information
@app.callback(Output('services-main-graph', "figure"),
              [Input('services_checklist', 'value')])
def update_fig(column):
    return plotly_bar_plot_chart(column)


# Callback : To display the plotly chart of the payment method information
@app.callback(Output('payment-method-main-graph', "figure"),
              [Input('payment-method', 'key')])
def update_fig(pkey):
    return plotly_payment_method()


# Callback : To display the plotly chart of the internet services information
@app.callback(Output('internetServicesMethod', "figure"),
              [Input("internet-services", 'key'), Input("internetServicesMethod", "hoverData")])
def update_fig(skey, hover):
    label = 'Group0'
    if hover is not None and hover['points']:
        label = hover['points'][0]['label']
    if len(label.split('Group')) == 1:
        label = 'Group0'

    return internetServices(label)


# Callback : To display the plotly chart of the payment method and contract information
@app.callback(Output('payment-method-contract', "children"),
              [Input('payment-method-main-graph', 'clickData')])
def update_fig(value):
    if value is None:
        return None
    else:
        return html.Div([
            dbc.Row([
                html.Div([dcc.Graph(id='payment-method-main-graph-churned', figure=plotly_contract(value, "Yes")),
                          dbc.Card(dbc.CardBody(html.P("Hover over figure",
                                                       style={'text-align': 'center', 'display': 'flex',
                                                              'width': '100%',
                                                              'justify-content': 'space-between',
                                                              }), id='mean_value_churned')), ]),
                html.Div([dcc.Graph(id='payment-method-main-graph-not-churned', figure=plotly_contract(value, "No")),
                          html.Div(dbc.Card(dbc.CardBody(html.P("Hover over figure",
                                                                style={'text-align': 'center', 'display': 'flex',
                                                                       'width': '100%',
                                                                       'justify-content': 'space-between',
                                                                       }), id='mean_value_not_churned')))])

            ], style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-between'})

        ])


# Callback : To display the plotly chart of payment method of churned customer and hover segment about mean information
@app.callback(
    Output('mean_value_churned', 'children'),
    Input('payment-method-main-graph-churned', 'hoverData'))
def card_render_churned(hoverData):
    if hoverData is None:
        return "Hover over any segment"
    else:
        paymentMethod = str(hoverData['points'][0]['label'])
        return plotly_fetch_mean(paymentMethod, "Yes")


# Callback : To display the plotly chart of payment method of not churned customer and hover segment about mean
# information
@app.callback(
    Output('mean_value_not_churned', 'children'),
    Input('payment-method-main-graph-not-churned', 'hoverData'))
def card_render_not_churned(hoverData):
    if hoverData is None:
        return "Hover over any segment"
    else:
        paymentMethod = str(hoverData['points'][0]['label'])
        return plotly_fetch_mean(paymentMethod, "No")


# Callback : To display the plotly chart of the customer relationship information
@app.callback(Output('relationship-main-graph', "figure"),
              [Input('relationship_checklist', 'value')])
def update_fig(column):
    return plotly_bar_plot_chart(column)


@app.callback(Output('relationship_graph', "figure"),
              [Input('relationship', 'key'), Input("relationship_graph", "clickData")])
def update_fig(column, click):
    if click is not None:
        points = click['points'][0]
        if {'x', 'y'}.issubset(points.keys()):
            return relationship(points['x'], points['y'])

    return relationship()


# Callback : To display the kde plotly chart of the customer relationship information
@app.callback(Output('kde_relationship_graph', "figure"),
              [Input('kde-key', 'key'), Input("relationship_graph", "clickData"),
               Input('tenure-stepper', 'value'), Input('numerical-tenure-dropdown', 'value')])
def update_fig(column, click, tenure_values, numerical_column):
    print('Cslled')
    min_tenure, max_tenure = tenure_values
    if click is not None:
        points = click['points'][0]
        if {'x', 'y'}.issubset(points.keys()):
            return kde_relationship(points['x'], points['y'], min_tenure, max_tenure, numerical_column, value=1)
    return kde_relationship(min_tenure=min_tenure, max_tenure=max_tenure, numerical_column=numerical_column)


@app.callback(Output('plotly-strip', "figure"),
              [Input('payment-strip', 'key')])
def update_fig(column):
    return graph_plotly_strip()


# Callback : To display the plotly chart of the senior and tenure relationship
@app.callback(Output('senior-tenure-main-graph', "figure"),
              [Input('senior-tenure-id', 'key')])
def update_senior_tenure_fig(seniorkey):
    return plotly_tenure_total_charges_seniorCitizen()


@app.callback(Output('tenure-gender-age', "figure"),
              [Input('tenure-slider', 'value'), Input('demo_select', 'value')])
def update_tenure_gender_slider(slider_value, demo_column):
    return plotly_pie_tenure(slider_value, demo_column)


# Callback : To display the plotly chart of the contract and monthly charges
@app.callback(Output('contract-monthly-main-graph', "figure"),
              [Input('contract-monthly-id', 'key')])
def update_senior_tenure_fig(contractkey):
    return plotly_contract_percentages()


# Callback : To display the plotly chart of the classification models
@app.callback(Output('plotly-main-graph', "figure"), [Input('model-id', 'key')])
def update_models_fig(modelkey):
    return plotly_models_table(classification_models)


# Callback : To display the plotly chart of the classification models
@app.callback(Output('corr-main-graph', "figure"), [Input('corr-id', 'key')])
def update_models_fig(corrkey):
    return corrrelation_matrix()


# Callback : To display the confusion matrix of all classification models with buttons
@app.callback(
    Output('cm-main-graph', 'figure'), [
        Input('btn-n-clicks-1', 'n_clicks'),
        Input('btn-n-clicks-2', 'n_clicks'),
        Input('btn-n-clicks-3', 'n_clicks'),
        Input('btn-n-clicks-4', 'n_clicks'),
        Input('btn-n-clicks-5', 'n_clicks'),
        Input('btn-n-clicks-6', 'n_clicks')])
def displayClick(btn1, btn2, btn3, btn4, btn5, btn6):
    clicked = ''

    if btn1 is not None and btn1 > button_counts['btn1']:
        clicked = 'btn1'
        button_counts['btn1'] = btn1
    elif btn2 is not None and btn2 > button_counts['btn2']:
        clicked = 'btn2'
        button_counts['btn2'] = btn2
    elif btn3 is not None and btn3 > button_counts['btn3']:
        clicked = 'btn3'
        button_counts['btn3'] = btn3
    elif btn4 is not None and btn4 > button_counts['btn4']:
        clicked = 'btn4'
        button_counts['btn4'] = btn4

    elif btn5 is not None and btn5 > button_counts['btn5']:
        clicked = 'btn5'
        button_counts['btn5'] = btn5

    elif btn6 is not None and btn6 > button_counts['btn6']:
        clicked = 'btn6'
        button_counts['btn6'] = btn6

    if clicked == 'btn1' or clicked == '':
        decision_tree_model = models_dict['decision_tree_dict']
        cm_dtc = decision_tree_model['confusion_matrix']
        cm_m = decision_tree_model['model']
        return confusion_matrix_graph(cm_dtc, cm_m)

    elif clicked == 'btn2':
        random_forest_model = models_dict['random_forest_dict']
        cm_rf = random_forest_model['confusion_matrix']
        cm_m = random_forest_model['model']
        return confusion_matrix_graph(cm_rf, cm_m)

    elif clicked == 'btn3':
        knn_model = models_dict['knn_dict']
        cm_knn = knn_model['confusion_matrix']
        cm_m = knn_model['model']
        return confusion_matrix_graph(cm_knn, cm_m)

    elif clicked == 'btn4':
        naive_bayes_model = models_dict['naive_bayes_dict']
        cm_nv = naive_bayes_model['confusion_matrix']
        cm_m = naive_bayes_model['model']
        return confusion_matrix_graph(cm_nv, cm_m)

    elif clicked == 'btn5':
        lr_model = models_dict['lr_dict']
        cm_lr = lr_model['confusion_matrix']
        cm_m = lr_model['model']
        return confusion_matrix_graph(cm_lr, cm_m)

    elif clicked == 'btn6':
        xg_boost_model = models_dict['xg_boost_dict']
        cm_xg = xg_boost_model['confusion_matrix']
        cm_m = xg_boost_model['model']
        return confusion_matrix_graph(cm_xg, cm_m)


# Callback : To display the roc curve of all classification models with dropdown
@app.callback(Output('auc-curve', 'figure'),
              [Input('auc-dropdown', 'value')])
def update_x_axis(classifier_model):
    if classifier_model == 'Decision_Tree':
        decision_tree_model = models_dict['decision_tree_dict']
        fpr = decision_tree_model['fpr']
        tpr = decision_tree_model['tpr']
        return models_auc_curve(fpr, tpr)

    elif classifier_model == 'Random_Forest':
        rf_model = models_dict['random_forest_dict']
        fpr = rf_model['fpr']
        tpr = rf_model['tpr']
        return models_auc_curve(fpr, tpr)

    elif classifier_model == 'Knn':
        knn_model = models_dict['knn_dict']
        fpr = knn_model['fpr']
        tpr = knn_model['tpr']
        return models_auc_curve(fpr, tpr)

    elif classifier_model == 'Naive_Bayes':
        nv_model = models_dict['naive_bayes_dict']
        fpr = nv_model['fpr']
        tpr = nv_model['tpr']
        return models_auc_curve(fpr, tpr)

    elif classifier_model == 'Logistic_Regression':
        lr_model = models_dict['lr_dict']
        fpr = lr_model['fpr']
        tpr = lr_model['tpr']
        return models_auc_curve(fpr, tpr)

    elif classifier_model == 'Xg_Boost':
        xgBoost_model = models_dict['xg_boost_dict']
        fpr = xgBoost_model['fpr']
        tpr = xgBoost_model['tpr']
        return models_auc_curve(fpr, tpr)


@app.callback(Output('introduction-first-graph', 'figure'),
              [Input('categorical-dropdown', 'value')])
def update_intro_first(categorical_column):
    return plot_pie_percentage_cat_count(categorical_column)


@app.callback(Output('introduction-second-graph', 'figure'),
              [Input('categorical-dropdown', 'value'),
               Input('numerical-dropdown', 'value'),
               Input('churn-binary-dropdown', 'value')])
def update_intro_second(categorical_column, numerical_column, churn_boolean):
    if churn_boolean == 'Churn':
        return numerical_cat_churn_box_plot(categorical_column, numerical_column, churn_boolean)
    else:
        return numerical_cat_churn_box_plot(categorical_column, numerical_column, churn_boolean)


@app.callback(Output('introduction-third-no-churn-graph', 'figure'),
              [Input('numerical-dropdown', 'value'),
               Input('categorical-dropdown', 'value')])
def update_intro_third(numerical_column, categorical_column):
    return pie_plots(numerical_column, categorical_column, 'Churn')


@app.callback(Output('introduction-fourth-churn-graph', 'figure'),
              [Input('numerical-dropdown', 'value'),
               Input('categorical-dropdown', 'value')])
def update_intro_fourth(numerical_column, categorical_column):
    return pie_plots(numerical_column, categorical_column, 'Not Churn')


# Interactive Prediction Callback
@app.callback(Output('logistic_regression_output', 'children'),
              Output('decision_tree_output', 'children'),
              Output('knn_output', 'children'),
              Output('nv_output', 'children'),
              Output('xg_boost_output', 'children'),
              Output('random_forest_output', 'children'),

              [Input('prediction_button', 'n_clicks')],

              State('gender_select', 'value'),
              State('senior_citizen_select', 'value'),

              State('phone_service_select', 'value'),
              State('multiple_line_select', 'value'),
              State('online_security_select', 'value'),
              State('internet_service_select', 'value'),
              State('online_backup_select', 'value'),
              State('device_protection_select', 'value'),
              State('tech_support_select', 'value'),
              State('streaming_tv_select', 'value'),
              State('streaming_movies_select', 'value'),

              State('contract_select', 'value'),
              State('partner_select', 'value'),
              State('dependents_select', 'value'),
              State('payment_method_select', 'value'),
              State('paperless_method_select', 'value'),
              State('monthly_charges', 'value'),
              State('total_charges', 'value'),
              State('tenure', 'value')
              )
def update_prediction(n_clicks, gender_select, senior_citizen_select, phone_service_select, multiple_line_select,
                      online_security_select, internet_service_select, online_backup_select, device_protection_select,
                      tech_support_select,
                      streaming_tv_select, streaming_movies_select, contract_select, partner_select, dependents_select,
                      payment_method_select, paperless_method_select, monthly_charges, total_charges, tenure
                      ):
    churn_columns_dict = {'gender': gender_select, 'SeniorCitizen': senior_citizen_select,

                          'PhoneService': phone_service_select, 'MultipleLines': multiple_line_select,
                          'InternetService': internet_service_select, 'OnlineSecurity': online_security_select,
                          'OnlineBackup': online_backup_select, 'DeviceProtection': device_protection_select,
                          'TechSupport': tech_support_select, 'StreamingTV': streaming_tv_select,
                          'StreamingMovies': streaming_movies_select,

                          'Partner': partner_select, 'Dependents': dependents_select, 'Contract': contract_select,
                          'PaperlessBilling': paperless_method_select, 'PaymentMethod': payment_method_select,
                          'TotalCharges': total_charges, 'MonthlyCharges': monthly_charges,
                          'tenure': tenure}

    if n_clicks is not None and n_clicks > 0:
        return models_predict(churn_columns_dict, models_dict)
    return no_update


app.layout = html.Div(
    id="main-container",
    children=[
        navigation_bar(),

        html.Div(
            id="app-container",
            children=[
                verticalTabs(),
                html.Div(
                    id="output-tab"
                )

            ],
        ),
        # dcc.Store(id="value-setter-store", data=init_value_setter_store()),
        # dcc.Store(id="n-interval-stage", data=50),
        # generate_modal(),
    ],
)

# Running the server
if __name__ == "__main__":
    app.title = "Halitel Communications"
    app.config["suppress_callback_exceptions"] = True
    app.run_server(debug=True, port=8050)
