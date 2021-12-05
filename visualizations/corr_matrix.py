import numpy as np
import plotly.figure_factory as ff

from preprocessing.data_experimentation import process_churn_dataset_again


# Code reference:
# https://github.com/cherylyilu/Kaggle-telecom-customer-churn-prediction/blob/master/Telecom%20Customer%20Churn%20Prediction.ipynb

# To plot the correlation matrix from every column to other column
# Observation: Tenure, payment method, contract are highly correlated
def corrrelation_matrix():

    # Consider the label encoded churn dataset
    churn_df = process_churn_dataset_again()
    correlated_features = set()

    # To get the correlation coefficient
    correlation_matrix = churn_df.corr()
    for i in range(len(correlation_matrix.columns)):
        for j in range(i):
            if abs(correlation_matrix.iloc[i, j]) > 0.5:
                column_name = correlation_matrix.columns[i]
                column_name1 = correlation_matrix.columns[j]
                correlated_features.add(column_name)
                correlated_features.add(column_name1)

    array = correlation_matrix.to_numpy()
    z_text = np.around(array, decimals=2)
    x = correlation_matrix.columns.tolist()
    y = correlation_matrix.columns.tolist()
    fig = ff.create_annotated_heatmap(array, x=x, y=y, annotation_text=z_text, colorscale='Viridis',
                                      hoverinfo='z')

    # To set annotations
    for i in range(len(fig.layout.annotations)):
        fig.layout.annotations[i].font.size = 10

    # To update figure layout
    fig.update_layout(
        showlegend=True,
        paper_bgcolor='#12191C',
        template='plotly_dark',
        height=700,
        width=1000
    )

    return fig


if __name__ == "__main__":
    assert corrrelation_matrix() is not None
    print("Correlation Matrix - Done")
