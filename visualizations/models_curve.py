import plotly.express as px
from sklearn.metrics import auc

from model.decision_tree_model import decision_tree_classifier


# Code referenced from: https://plotly.com/python/roc-and-pr-curves/

# Graph to plot the ROC - AUC curve for every classification model
def models_auc_curve(fpr, tpr):

    # Area plot with false positive rate against true positive rate
    fig = px.area(
        x=fpr, y=tpr,
        title=f'ROC Curve (AUC={auc(fpr, tpr):.4f})',
        labels=dict(x='False Positive Rate', y='True Positive Rate'),
        width=700, height=500
    )
    fig.add_shape(
        type='line', line=dict(dash='dash'),
        x0=0, x1=1, y0=0, y1=1
    )

    # To update axes
    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    fig.update_xaxes(constrain='domain')

    # To update layout
    fig.update_layout(
        height=600,
        width=900,
        showlegend=True,
        paper_bgcolor='#12191C',
        template='plotly_dark',
    )

    return fig


if __name__ == "__main__":
    decision_tree_model = decision_tree_classifier()
    fpr = decision_tree_model['fpr']
    tpr = decision_tree_model['tpr']
    thresholds = decision_tree_model['thresholds']
    # plot models auc curve
    assert models_auc_curve(fpr, tpr) is not None
    print("AUC curves - Done")
