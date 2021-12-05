import plotly.express as px

from preprocessing.data_experimentation import process_churn_dataset


# Payment method and churn relationship
def plotly_payment_method():
    # 1. Load the dataset
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()

    # 2. Group by Tenure
    df = churn_df.groupby(['PaymentMethod', 'Churn']).size().reset_index(name='Frequency')

    # 3. To plot bar chart
    fig = px.bar(df, x="PaymentMethod", y="Frequency", color="Churn")

    # 4. Update x axis and y axis labels
    fig.update_layout(
        showlegend=True,
        paper_bgcolor='#12191C',
        template='plotly_dark',
        title="Churn Rate based on Payment Method",
        xaxis_title="Payment Method",
        yaxis_title="Frequency",
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )
    return fig


# Contract duration and churn relationship
def plotly_contract(input, churned="Yes"):
    paymentMethod = input['points'][0]['x']

    # 1. Load the dataset
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()

    # 2. Filter out payment method
    df = churn_df.query("PaymentMethod == '" + paymentMethod + "'")
    df = df.query("Churn == '" + str(churned) + "'")
    df = df.groupby(['Contract']).size().reset_index(name='Frequency')

    # 3. To plot bar chart
    fig = px.pie(df, values='Frequency', names='Contract')

    # 4. Update x axis and y axis labels
    fig.update_layout(
        showlegend=True,
        paper_bgcolor='#12191C',
        template='plotly_dark',
        title="Contract and Customer Churned: " + str(churned),
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )
    return fig


# Total tenure
def plotly_pie_tenure(maxValue, column):
    # 1. Load the dataset
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()

    df = churn_df.loc[churn_df['tenure'] <= maxValue]
    df = df.groupby([column]).size().reset_index(name='Frequency')

    fig = px.pie(df, values="Frequency", names=column)

    fig.update_layout(
        title="Division among " + column + " based on tenure",
        showlegend=True,
        legend_title=f"{column}:",
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


# Fetch the mean of total charges against the contract type
def plotly_fetch_mean(contract, churned="Yes"):
    # 1. Load the dataset
    churn_df = process_churn_dataset()
    churn_df = churn_df.copy()
    df = churn_df.loc[churn_df['Contract'] == contract]
    df = df.loc[churn_df['Churn'] == churned]

    outputString = ""
    if churned == "Yes":
        outputString += "Mean of the total charges for contract type " + contract + " for churned customers is: " + str(
            df['TotalCharges'].mean())
    else:
        outputString += "Mean of the total charges for contract type " + contract + " for existing customers is: " + str(
            df['TotalCharges'].mean())
    return outputString


if __name__ == "__main__":
    assert plotly_payment_method() is not None
    print("template graphs - Done")
