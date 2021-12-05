from typing import Dict

import xgboost as xgb
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, \
    classification_report, roc_curve
from sklearn.model_selection import train_test_split

from preprocessing.data_experimentation import process_churn_dataset_again

##############################################
"""
    File Usage: XGBoost classification of data
"""
##############################################


def xg_boost__classifier() -> Dict:

    churn_df = process_churn_dataset_again()
    label_col = "Churn"
    feature_cols = churn_df.columns.tolist()
    feature_cols.remove(label_col)

    x = churn_df[feature_cols]
    y = churn_df[label_col]

    # Split the dataset into train(80) and test(20)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

    # To Train your model using train set.

    classifier_model = xgb.XGBClassifier(objective="binary:logistic", random_state=42, use_label_encoder=False,
                                         eval_metric='logloss')

    classifier_model.fit(x_train, y_train)

    # To Predict test labels/classes for test set.

    predictions = classifier_model.predict(x_test)

    # Predict probability
    y_score = classifier_model.predict_proba(x_test)[:, 1]

    fpr, tpr, thresholds = roc_curve(y_test, y_score)

    # To Measure the below given performance measures on test predictions.

    # performance measure https://towardsdatascience.com/performance-metrics-for-classification-machine-learning
    # -problems-97e7e774a007 confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

    xgb_model = classifier_model

    xgb_confusion_matrix = confusion_matrix(y_true=y_test, y_pred=predictions)

    xgb_accuracy = accuracy_score(y_true=y_test, y_pred=predictions)

    xgb_precision = precision_score(y_true=y_test, y_pred=predictions, average="micro")

    xgb_recall = recall_score(y_true=y_test, y_pred=predictions, average="micro")

    xgb_f1_score = f1_score(y_true=y_test, y_pred=predictions, average="micro")

    xgb_roc_auc_score = roc_auc_score(y_true=y_test, y_score=predictions)

    xgb_classification_report = classification_report(y_true=y_test, y_pred=predictions)

    return dict(model='XGBoost Classifier', accuracy=xgb_accuracy, precision=xgb_precision,
                recall=xgb_recall, f1_score=xgb_f1_score, roc_auc_score=xgb_roc_auc_score,
                confusion_matrix=xgb_confusion_matrix, classification_report=xgb_classification_report,
                fpr=fpr, tpr=tpr, thresholds=thresholds, actual_model=xgb_model)


if __name__ == "__main__":

    assert xg_boost__classifier() is not None
    print("XG Boost Classifier - Done")
