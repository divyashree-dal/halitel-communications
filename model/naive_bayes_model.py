from typing import Dict

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, \
    classification_report, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from preprocessing.data_experimentation import process_churn_dataset_again

##############################################
"""
    File Usage:Naive Bayes classification Model
"""
##############################################


def naive_bayes_classifier() -> Dict:

    churn_df = process_churn_dataset_again()
    label_col = "Churn"
    feature_cols = churn_df.columns.tolist()
    feature_cols.remove(label_col)

    x = churn_df[feature_cols]
    y = churn_df[label_col]

    # To Split the dataset into train(80) and test(20)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # To Train your model using train set.

    classifier_model = GaussianNB()

    classifier_model.fit(x_train, y_train)

    # To Predict test labels/classes for test set.

    predictions = classifier_model.predict(x_test)

    # Predict probability
    y_score = classifier_model.predict_proba(x_test)[:, 1]

    fpr, tpr, thresholds = roc_curve(y_test, y_score)

    # To measure the below given performance measures on test predictions.

    nv_model = classifier_model

    nv_confusion_matrix = confusion_matrix(y_true=y_test, y_pred=predictions)

    nv_accuracy = accuracy_score(y_true=y_test, y_pred=predictions)

    nv_precision = precision_score(y_true=y_test, y_pred=predictions, average="micro")

    nv_recall = recall_score(y_true=y_test, y_pred=predictions, average="micro")

    nv_f1_score = f1_score(y_true=y_test, y_pred=predictions, average="micro")

    nv_roc_auc_score = roc_auc_score(y_true=y_test, y_score=predictions)

    nv_classification_report = classification_report(y_true=y_test, y_pred=predictions)

    return dict(model="Naive Bayes Classifier",  accuracy=nv_accuracy, precision=nv_precision,
                recall=nv_recall, f1_score=nv_f1_score,
                roc_auc_score=nv_roc_auc_score, confusion_matrix=nv_confusion_matrix,
                classification_report=nv_classification_report, fpr=fpr, tpr=tpr, thresholds=thresholds,actual_model=nv_model)


if __name__ == "__main__":

    assert naive_bayes_classifier() is not None
    print("Naive Bayes Classifier - Done")
