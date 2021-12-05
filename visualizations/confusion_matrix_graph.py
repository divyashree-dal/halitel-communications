import plotly.graph_objects as go

from model.decision_tree_model import decision_tree_classifier


# Code referenced from:
# https://stackoverflow.com/questions/60860121/plotly-how-to-make-an-annotated-confusion-matrix-using-a-heatmap

# Graph to plot the confusion matrix for every considered classification model to analyse
# true positives and false positives
# Observation: Logistic Regression gives the better accuracy compares to other model, true positive value is the highest
def confusion_matrix_graph(confusion_matrix, model):

    # Labels for xaxis and yaxis
    labels = ['Not Churn', "Churn"]

    # To create annotated heatmap
    data = go.Heatmap(z=confusion_matrix, x=labels, y=labels, colorscale='Viridis')
    annotations = []
    for i, row in enumerate(confusion_matrix):
        for j, value in enumerate(row):
            annotations.append(
                {
                    "x": labels[i],
                    "y": labels[j],
                    "font": {"color": "blue"},
                    "text": str(value),
                    "xref": "x1",
                    "yref": "y1",
                    "showarrow": False
                }
            )

    fig = go.Figure(data=data)

    # To update layout
    fig.update_layout(
        height=600,
        width=900,
        font=dict(
            family="Times new Roman",
            size=14,
        ),
        showlegend=True,
        annotations=annotations,
        title_text=f"Confusion matrix of {model}",
        paper_bgcolor='#12191C',
        title_font_color='#91DFD2',
        font_color="#ffffff",
    )

    # To Set x-axis title
    fig.update_xaxes(title_text="Predicted Value")

    # To Set y-axes titles
    fig.update_yaxes(title_text="Actual value")

    return fig


if __name__ == "__main__":
    decision_tree_model = decision_tree_classifier()
    cm_dtc = decision_tree_model['confusion_matrix']
    cm_m = decision_tree_model['model']
    # plot confusion matrix
    assert confusion_matrix_graph(cm_dtc, cm_m) is not None
    print("Confusion Matrix - Done")
