import plotly.express as px
import plotly.graph_objects as go

from preprocessing.data_experimentation import process_churn_dataset


# Graph to retrieve the total percentages of a service usage with respect to a customer
def plot_pie_percentage_cat_count(categorical_column):
    # 1. Load the dataset
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()

    """
            Plotting the total churn rate
            Code referenced from : https://plotly.com/python/pie-charts/

        """
    # 2. To get the labels and values count
    labels = list(churn_df[categorical_column].value_counts().keys())
    values = list(churn_df[categorical_column].value_counts().values)

    # 3. Pie trace
    data = go.Pie(
        labels=labels,
        values=values,
        name=categorical_column
    )

    data = [data]
    fig = go.Figure(data=data)

    # 4. To update hover info
    fig.update_traces(hoverinfo='label+percent+name', textinfo='percent', hole=0.6)

    # 5. Layout figure
    fig.update_layout(
        plot_bgcolor='#12191C',
        paper_bgcolor='#12191C',
        height=500,
        width=500,
        title=f"Total percentage of {categorical_column}",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text=f'{categorical_column}', x=0.50, y=0.5, font_size=20, showarrow=False)],
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        showlegend=True,
        title_font_color='#91DFD2',
        font_color="#ffffff",
        legend_title=f"{categorical_column}:-",
    )

    return fig


# Graph to get the distribution of total/monthly charges with respect to every categorical value
def numerical_cat_churn_box_plot(categorical_column, numerical_column, churn_boolean):
    # To load the dataset
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()
    churn_df['churn_boolean'] = churn_df.Churn.copy()

    churn_df['SeniorCitizen'] = churn_df['SeniorCitizen'].apply(lambda x: 'No' if x == 0 else 'Yes')

    # If churn selected
    if churn_boolean == 'Churn':

        # a box plot containing details about the categorical column distribution with numerical columns
        fig = px.box(churn_df, x=categorical_column, y=numerical_column,
                     color=churn_df['churn_boolean'].map({'No': 'NoChurn', 'Yes': 'Churn'}),
                     color_discrete_map={'NoChurn': "lightyellow", 'Churn': 'limegreen'},
                     category_orders={str(numerical_column):
                                          churn_df[numerical_column].value_counts().sort_index().index})

        fig.update_layout(
            font=dict(
                family="Times new Roman",
                size=14,
            ),
            height=500,
            width=500,
            paper_bgcolor='#12191C',
            template='plotly_dark',
            title=f"Dist. of {categorical_column} by {numerical_column} and Churn",
            yaxis_title=f"Distribution of {numerical_column}",
            showlegend=True,
            legend_title=f"Churn:-",
            xaxis={'type': 'category'},
            title_font_color='#91DFD2',
            font_color="#ffffff",
        )

    # If Not churned
    else:
        fig = px.box(churn_df, x=categorical_column, y=numerical_column,
                     color_discrete_sequence=['limegreen'],
                     category_orders={str(numerical_column):
                                          churn_df[numerical_column].value_counts().sort_index().index})

        fig.update_layout(
            font=dict(
                family="Times new Roman",
                size=14,
            ),
            showlegend=True,
            template='plotly_dark',
            title=f"Distribution of {numerical_column} by {categorical_column}",
            yaxis_title=f"Distribution of {numerical_column}",
            legend_title=f"Churn:-",
            xaxis={'type': 'category'},
            font_color="#ffffff",
            title_font_color='#91DFD2',
            paper_bgcolor='#12191C',

        )

    return fig


# Graph to group the total count of category(percentages) values against numerical value(total percentages)
def pie_plots(numerical_column, categorical_column, churn_boolean):
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()
    if churn_boolean == 'Churn':
        value_churn = 'Yes'
    else:
        value_churn = 'No'

    group_by_category_df = churn_df[churn_df['Churn'] == value_churn]

    # Group by the categorical column with the total sum of the numerical column
    group_by_category_df = group_by_category_df.groupby(categorical_column)[numerical_column].sum().reset_index()

    group_by_category_df = group_by_category_df.sort_values(numerical_column)

    #  To get the labels and values count
    labels = group_by_category_df[categorical_column]
    values = group_by_category_df[numerical_column]

    # Pie trace
    data = go.Pie(
        labels=labels,
        values=values,
        name=churn_boolean
    )

    data = [data]
    fig = go.Figure(data=data)

    # To update hover info
    fig.update_traces(hoverinfo='label+percent+name+value', textinfo='percent', hole=0.5)

    # Layout figure
    fig.update_layout(
        height=500,
        width=500,
        showlegend=True,
        paper_bgcolor='#12191C',
        template='plotly_dark',
        title=f"{categorical_column} Ratio of {numerical_column} by {churn_boolean}",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text=f'{churn_boolean}', x=0.50, y=0.5, font_size=20, showarrow=False)],
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        legend_title=f"{categorical_column}:-",
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )

    return fig


if __name__ == "__main__":
    assert plot_pie_percentage_cat_count('Contract') is not None
    assert numerical_cat_churn_box_plot('SeniorCitizen', 'MonthlyCharges', "Churn") is not None
    assert pie_plots('MonthlyCharges', 'Contract', "Churn") is not None
    print("Introduction page graphs - Done")
