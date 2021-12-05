import plotly.express as px

from preprocessing.data_experimentation import process_churn_dataset


# Generalized bar plots for every heading
def plotly_bar_plot_chart(xaxis):
    """
        Plotting the churn rate based on different parameters
        y axis : churn count

        Code referenced from: https://plotly.com/python/bar-charts/

    """

    # 1. Load the dataset
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()

    # 2. Group by
    if xaxis == 'Both':
        df = churn_df.groupby(['gender', 'SeniorCitizen', 'Churn']).size().reset_index(name='Frequency')
        df['GenderCitizen'] = df[['gender', 'SeniorCitizen']].apply(
            lambda x: f'{x[0]} Junior' if x[1] == 0 else f'{x[0]} Senior', axis=1)

        # 3. To plot bar chart
        fig = px.bar(df, x='GenderCitizen', y='Frequency',
                     color="Churn", barmode="group", template='plotly_dark')
    else:
        df = churn_df.groupby([xaxis, 'Churn']).size().reset_index(name='Frequency')
        fig = px.bar(df, x=xaxis, y='Frequency',
                     color="Churn", barmode="group", template='plotly_dark')

    # 4. Update x axis and y axis labels
    fig.update_layout(

        paper_bgcolor='#12191C',
        title=f" Churn Rate based on {xaxis}",
        xaxis_title=xaxis,
        yaxis_title="Churn Count",
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )
    return fig


# Line charts for monthly and total charges
def plotly_line_plot_chart(xaxis):
    """
        Plotting the churn rate based on different parameters
        y axis : churn count

        Code referenced from: https://plotly.com/python/bar-charts/

    """

    # 1. Load the dataset
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()

    # 2. Group by
    df = churn_df.groupby([xaxis, 'Churn']).size().reset_index(name='Frequency')

    # 3. To plot pie chart
    fig = px.scatter(df, x=xaxis, y='Frequency', color="Churn", template='plotly_dark')

    # 4. Update x axis and y axis labels
    fig.update_layout(
        paper_bgcolor='#12191C',
        title=f" Churn Rate based on {xaxis}",
        xaxis_title=xaxis,
        yaxis_title="Churn Count",
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )

    return fig


if __name__ == "__main__":
    assert plotly_bar_plot_chart("Both") is not None
    assert plotly_line_plot_chart('MonthlyCharges') is not None
    print("Basic Graphs - ok")
