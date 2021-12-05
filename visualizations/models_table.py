import pandas as pd

from model.decision_tree_model import decision_tree_classifier
from model.knn_model import knn_classifier
from model.logistic_regression import lr_classifier
from model.naive_bayes_model import naive_bayes_classifier
from model.random_forest_model import random_forest_classifier
import plotly.graph_objects as go

from model.xg_boost import xg_boost__classifier


def plotly_models_table(models):
    # classification models for Churn dataset.
    df = pd.DataFrame(models, columns=['Model Name', 'Accuracy', 'Precision', 'Recall', 'F1 Score',
                                       'ROC AUC Score'], index=list(range(6)))

    # To create a table of classification result details
    fig = go.Figure(
        data=[go.Table(
            columnwidth=[50, 30, 30, 35, 35],
            header=dict(values=df.columns,
                        fill_color='paleturquoise',
                        line_color='darkslategray',
                        font=dict(color='black', family="Times New Roman", size=15),
                        align='center',
                        height=60),

            cells=dict(values=df.values.transpose(),
                       fill_color='lavender',
                       line_color='darkslategray',
                       align='center',
                       font=dict(color='black', family="Lato", size=13),
                       height=50))
        ])

    # To update layout
    fig.update_layout(
        plot_bgcolor='#12191C',
        paper_bgcolor='#12191C',
        template='plotly_dark',
        height=500,
        margin=dict(t=50, l=25, r=25)
    )

    return fig


def getAllModels():
    decision_tree_dict = decision_tree_classifier()
    random_forest_dict = random_forest_classifier()
    knn_dict = knn_classifier()
    naive_bayes_dict = naive_bayes_classifier()
    lr_dict = lr_classifier()
    xg_boost_dict = xg_boost__classifier()
    model_dict = {
        'lr_dict': lr_dict,
        'decision_tree_dict': decision_tree_dict,
        'knn_dict': knn_dict,
        'naive_bayes_dict': naive_bayes_dict,
        'xg_boost_dict': xg_boost_dict,
        'random_forest_dict': random_forest_dict,
    }
    models = [list(decision_tree_dict.values())[:6], list(random_forest_dict.values())[:6],
              list(knn_dict.values())[:6], list(naive_bayes_dict.values())[:6], list(lr_dict.values())[:6],
              list(xg_boost_dict.values())[:6]]
    return model_dict, models


if __name__ == "__main__":
    print(" Model Table Graphs - ok")
