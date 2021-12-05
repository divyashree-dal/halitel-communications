import pandas as pd

from preprocessing.data_encoding import replace_with_label_encoder
from preprocessing.data_experimentation import getLabelEncoderForCategorical
from preprocessing.data_profile import get_text_categorical_columns


def models_predict(testRow: dict, models_dict: dict):
    churndf, churnLabelEncoder = getLabelEncoderForCategorical()
    churn_present_df = pd.DataFrame(testRow, index=[0])
    churn_present_df[['TotalCharges', 'MonthlyCharges', 'tenure']] = churn_present_df[
        ['TotalCharges', 'MonthlyCharges', 'tenure']].apply(pd.to_numeric)
    categorical_columns = get_text_categorical_columns(churn_present_df)

    for column in categorical_columns:
        label_encoder = churnLabelEncoder[column]
        churn_present_df = replace_with_label_encoder(churn_present_df, column, label_encoder)

    # Other categorical columns : feature columns
    feature_cols = churn_present_df.columns.tolist()
    x = churn_present_df[feature_cols]

    # Model Dict is in order of
    # model_dict = {
    #     'lr_dict': lr_dict,
    #     'decision_tree_dict': decision_tree_dict,
    #     'knn_dict': knn_dict,
    #     'naive_bayes_dict': naive_bayes_dict,
    #     'xg_boost_dict': xg_boost_dict,
    #     'random_forest_dict': random_forest_dict,
    # }

    models_prediction = []
    for key, value in models_dict.items():
        prediciton = models_dict[key]['actual_model'].predict(x)
        print(f"Model name = {key} and Prediction is {prediciton[0]}")
        if prediciton[0]:
            models_prediction.append('Churned')
        else:
            models_prediction.append('Non Churned')

    return models_prediction
