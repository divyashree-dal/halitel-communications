import plotly.express as px
import plotly.figure_factory as ff

from preprocessing.data_encoding import generate_label_encoder, replace_with_label_encoder
from preprocessing.data_experimentation import process_churn_dataset
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from preprocessing.data_profile import get_column_mean, get_column_min, get_column_max


# Graph to plot the total charges paid by every senior citizen according to their tenure.
def plotly_tenure_total_charges_seniorCitizen():
    # 1. Load the dataset
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()

    # 2. To consider only senior citizens
    churn_df['SeniorCitizen'] = churn_df['SeniorCitizen'].apply(lambda x: 'No' if x == 0 else 'Yes')

    # 3. to plot scatter plot
    fig = px.scatter(churn_df, x=churn_df['tenure'], y=churn_df['TotalCharges'], color=churn_df['Churn'],
                     title="Plotly Scatter Plot between tenure and total charges", template='plotly_dark')

    # 34 Update x axis and y axis labels
    fig.update_layout(
        title="Plotly Scatter Plot between tenure and total charges for senior citizens",
        xaxis_title="Tenure",
        yaxis_title="Total Charges",
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )

    return fig


# Graph to check the average monthly charges per every contract agreement
def plotly_contract_percentages():
    # 1. Load the dataset
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()

    # 2. Get three contract dataframes
    month_2_month = churn_df.loc[churn_df['Contract'] == 'Month-to-month']
    one_year = churn_df.loc[churn_df['Contract'] == 'One year']
    two_year = churn_df.loc[churn_df['Contract'] == 'Two year']

    # 3. Get average monthly charges of churned people for every contract
    two_year_value = two_year.loc[two_year['Churn'] == 'Yes']['MonthlyCharges'].mean()
    one_year_value = one_year.loc[one_year['Churn'] == 'Yes']['MonthlyCharges'].mean()
    month_2_month_value = month_2_month.loc[month_2_month['Churn'] == 'Yes']['MonthlyCharges'].mean()

    # 4. Get average monthly charges of non - churned people for every contract
    two_year_no_value = two_year.loc[two_year['Churn'] == 'No']['MonthlyCharges'].mean()
    one_year_no_value = one_year.loc[one_year['Churn'] == 'No']['MonthlyCharges'].mean()
    month_2_month_no_value = month_2_month.loc[month_2_month['Churn'] == 'No']['MonthlyCharges'].mean()

    # Code referenced from: https://plotly.com/python/gauge-charts/
    fig = go.Figure()

    # 5. Indicators
    fig.add_trace(
        go.Indicator(
            mode="number+gauge+delta",
            value=two_year_value,
            domain={'x': [0.25, 1], 'y': [0.7, 0.9]},
            title={'text': "Two year", 'font': {'size': 24}},
            delta={'reference': get_column_mean(two_year, 'MonthlyCharges')},
            gauge={
                'shape': "bullet",
                'axis': {'range': [get_column_min(two_year, 'MonthlyCharges'),
                                   get_column_max(two_year, 'MonthlyCharges')]},
                'bar': {'color': "#C4ADA8"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': get_column_mean(two_year, 'MonthlyCharges')},
                'steps': [
                    {'range': [get_column_min(two_year, 'MonthlyCharges'), two_year_no_value], 'color': "#350B02"},
                    {'range': [two_year_no_value, get_column_max(two_year, 'MonthlyCharges')], 'color': "#6B1704"}]}))

    fig.add_trace(
        go.Indicator(
            mode="number+gauge+delta",
            value=one_year_value,
            domain={'x': [0.25, 1], 'y': [0.4, 0.6]},
            title={'text': "One Year", 'font': {'size': 24}},
            delta={'reference': get_column_mean(one_year, 'MonthlyCharges')},
            gauge={
                'shape': "bullet",
                'axis': {'range': [get_column_min(one_year, 'MonthlyCharges'),
                                   get_column_max(one_year, 'MonthlyCharges')]},
                'bar': {'color': "#C4ADA8"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': get_column_mean(one_year, 'MonthlyCharges')},
                'steps': [
                    {'range': [get_column_min(one_year, 'MonthlyCharges'), one_year_no_value], 'color': "#350B02"},
                    {'range': [one_year_no_value, get_column_max(one_year, 'MonthlyCharges')], 'color': "#6B1704"}]}))

    fig.add_trace(
        go.Indicator(
            mode="number+gauge+delta",
            value=month_2_month_value,
            domain={'x': [0.25, 1], 'y': [0.08, 0.28]},
            title={'text': "Month-to-Month", 'font': {'size': 24}},
            delta={'reference': get_column_mean(month_2_month, 'MonthlyCharges')},
            gauge={
                'shape': "bullet",
                'axis': {'range': [get_column_min(month_2_month, 'MonthlyCharges'),
                                   get_column_max(month_2_month, 'MonthlyCharges')]},
                'bar': {'color': "#C4ADA8"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': get_column_mean(month_2_month, 'MonthlyCharges')},
                'steps': [
                    {'range': [get_column_min(month_2_month, 'MonthlyCharges'), month_2_month_no_value],
                     'color': "#350B02"},
                    {'range': [month_2_month_no_value, get_column_max(month_2_month, 'MonthlyCharges')],
                     'color': "#6B1704"}]}))

    fig.update_layout(paper_bgcolor="black", font={'color': "darkblue", 'family': "Arial"})

    # 6. Update x axis and y axis labels
    fig.update_layout(
        paper_bgcolor='#12191C',
        title="Mean Monthly charges based on contract agreement",
        height=500,
        width=1000,
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )

    return fig


# Function to get the total groups based on different services
def getGroups():
    groups = {}
    for i in range(16):
        bin_value = '{0:04b}'.format(i)
        groups[bin_value] = f'Group{i}'
    return groups


#
def internetServices(group_name='Group0'):
    df = process_churn_dataset()
    df = df[df["InternetService"] != 'No']
    for column in ['OnlineSecurity', 'OnlineBackup', 'StreamingTV', 'StreamingMovies']:
        label_encoder = generate_label_encoder(df[column])
        df = replace_with_label_encoder(df, column, label_encoder)
    df = df.sort_values(by=['OnlineSecurity', 'OnlineBackup', 'StreamingTV', 'StreamingMovies'], ascending=True)
    groups = getGroups()
    df['Groups'] = df[['OnlineSecurity', 'OnlineBackup', 'StreamingTV', 'StreamingMovies']].apply(
        lambda x: groups[f'{x[0]}{x[1]}{x[2]}{x[3]}'], axis=1)
    new_df = df.groupby(['Groups', 'Churn']).size().reset_index(name='Frequency')
    new_df = new_df.sort_values(by=['Groups'], ascending=True)
    churn_df = new_df.loc[new_df['Churn'] == 'Yes']
    no_churn_df = new_df.loc[new_df['Churn'] == 'No']
    fig = make_subplots(rows=2, cols=2, specs=[[{"type": 'bar'}, {"type": 'bar'}], [{'type': 'pie'}, {'type': 'pie'}]],
                        subplot_titles=("Grouping of Services vs Frequency", "Groups vs Frequency",
                                        "Percentage of Internet services based on Groups"))

    fig.add_trace(
        go.Bar(x=churn_df['Groups'], y=churn_df['Frequency'], name='Churn'),
        row=1, col=1
    )
    fig.add_trace(
        go.Bar(x=no_churn_df['Groups'], y=no_churn_df['Frequency'], name='No Churn'),
        row=1, col=1
    )

    groups_values = {v: k for k, v in groups.items()}
    y_value = [int(x) for x in groups_values[group_name]]
    fig.add_trace(
        go.Bar(x=['OnlineSecurity', 'OnlineBackup', 'StreamingTV', 'StreamingMovies'], y=y_value, name=group_name),
        row=1, col=2
    )

    nDF = df[df['Groups'] == group_name]
    internet = nDF['InternetService'].value_counts().to_dict()

    colors_1 = ['7f7f7f', 'orange', 'yellow']
    fig.add_trace(
        go.Pie(values=list(internet.values()),
               labels=list(internet.keys()), hole=0.4, title='Internet Services',
               marker_colors=colors_1, textinfo='percent+label', textfont_size=18, title_font_family="Times New Roman",
               title_font_color="white", title_font_size=20
               ),
        row=2, col=1
    )
    fig['layout']['xaxis']['title'] = 'Groups'
    fig['layout']['yaxis']['title'] = 'Frequency'
    fig['layout']['xaxis2']['title'] = 'Online Services'
    fig['layout']['yaxis2']['title'] = 'Frequency'

    for i in fig['layout']['annotations']:
        i['font'] = dict(size=16, color='#91DFD2')

    fig.update_layout(
        height=1000,
        title_text="Internet Services",
        barmode='group',
        paper_bgcolor="#12191C",
        template='plotly_dark',
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )

    return fig


#
def relationship(partner_x='Partner Yes', dependent_y='Dependent Yes'):
    partner_value = partner_x.split(' ')[1]
    dependent_value = dependent_y.split(' ')[1]
    df = process_churn_dataset()
    x = ['Partner Yes', 'Partner No']
    y = ['Dependent Yes', 'Dependent No']

    data = [[1, 2], [3, 4]]

    fig = make_subplots(rows=1, cols=2, specs=[[{"type": 'heatmap'}, {'type': 'pie'}]],
                        subplot_titles=[
                            "Heatmap of partner vs Dependents",
                            "Percentage of contracts based on partner and dependents "])

    fig.add_trace(
        go.Heatmap(z=data, x=x, y=y, coloraxis="coloraxis3", showscale=False, showlegend=False),
        row=1, col=1
    )

    nDF = df[df['Partner'] == partner_value]
    newDF = nDF[nDF['Dependents'] == dependent_value]
    contract = newDF['Contract'].value_counts().to_dict()
    colors_1 = ['black', 'orange', 'yellow']

    fig.add_trace(
        go.Pie(values=list(contract.values()),
               labels=list(contract.keys()), hole=0.4, title='Contract',
               marker_colors=colors_1, textinfo='percent+label', textfont_size=18, title_font_family="Times New Roman",
               title_font_color="red", title_font_size=20),
        row=1, col=2
    )

    fig.update_xaxes(side="bottom")

    for i in fig['layout']['annotations']:
        i['font'] = dict(size=16, color='#91DFD2')

    fig.update_layout(
        height=700,
        width=900,
        showlegend=False,
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        paper_bgcolor='#12191C',
        template='plotly_dark',
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )

    return fig


#
def kde_relationship(partner_x='Partner Yes', dependent_y='Dependent Yes', min_tenure=0, max_tenure=72,
                     numerical_column='MonthlyCharges', value=0):
    partner_value = partner_x.split(' ')[1]
    dependent_value = dependent_y.split(' ')[1]
    df = process_churn_dataset()
    nDF = df[df['Partner'] == partner_value]
    newDF = nDF[nDF['Dependents'] == dependent_value]
    min = min_tenure
    max = max_tenure
    value = value

    ChurnDFYes = newDF[newDF['Churn'] == 'Yes'][numerical_column]
    ChurnDFNo = newDF[newDF['Churn'] == 'No'][numerical_column]
    newDF = newDF[newDF['tenure'] > min]
    tenure_DF = newDF[newDF['tenure'] < max]

    tenure_ChurnYes_DF = tenure_DF[tenure_DF['Churn'] == 'Yes'][numerical_column]
    tenure_ChurnNo_DF = tenure_DF[tenure_DF['Churn'] == 'No'][numerical_column]

    if value == 0:
        fig = ff.create_distplot([ChurnDFNo, ChurnDFYes], group_labels=['General Non Churned', 'General Churned'],
                                 bin_size=3,
                                 curve_type='kde',
                                 show_rug=False,
                                 show_hist=False,
                                 show_curve=True,
                                 colors=['blue', 'red'])
        x = 'Churn'
        y = numerical_column

    else:
        fig = ff.create_distplot([tenure_ChurnNo_DF, tenure_ChurnYes_DF],
                                 group_labels=['Tenure non churned',
                                               'Tenure Churned'],
                                 bin_size=3,
                                 curve_type='kde',
                                 show_rug=False,
                                 show_hist=False,
                                 show_curve=True,
                                 colors=['white', 'orange'])
        x = 'Tenure'
        y = numerical_column

    fig['layout']['xaxis']['title'] = x
    fig['layout']['yaxis']['title'] = y

    if value == 1:
        title = f'Distplots based on {partner_x} {dependent_y}, Tenure and {numerical_column}'
    else:
        title = f'Distplots based on General, Tenure and Monthly Charges'

    fig.update_layout(
        height=600,
        width=800,
        showlegend=True,
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        paper_bgcolor='#12191C',
        template='plotly_dark',
        title=title,
        plot_bgcolor='black',
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )

    return fig


#
def graph_plotly_strip():
    df = process_churn_dataset()
    fig = px.strip(df, x="gender", y="MonthlyCharges", color="Churn")

    fig.update_layout(
        height=700,
        width=700,
        title="Strip plot of monthly charges and gender",
        showlegend=True,
        paper_bgcolor='#12191C',
        template='plotly_dark',
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )

    return fig


if __name__ == "__main__":
    assert plotly_tenure_total_charges_seniorCitizen() is not None
    assert plotly_contract_percentages() is not None
    assert internetServices() is not None
    assert relationship() is not None
    assert kde_relationship() is not None
    assert graph_plotly_strip() is not None
    print("Advanced Graphs - ok")
