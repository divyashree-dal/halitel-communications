from typing import Dict

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, \
    classification_report, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from preprocessing.data_experimentation import process_churn_dataset_again

##############################################
"""
    File Usage: Decision Tree classification Model
"""
##############################################


# Decision Tree classification model
def decision_tree_classifier() -> Dict:
    churn_df = process_churn_dataset_again()

    # label column: Churn
    label_col = "Churn"

    # Other categorical columns : feature columns
    feature_cols = churn_df.columns.tolist()
    feature_cols.remove(label_col)

    x = churn_df[feature_cols]
    y = churn_df[label_col]

    # Split the dataset into train(80) and test(20)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

    # Deduce the decision tree model
    classifier_model = DecisionTreeClassifier(class_weight="balanced", criterion="entropy", max_depth=400,
                                              min_samples_split=2)

    # Train the model
    classifier_model.fit(x_train, y_train)

    # Predict the test
    predictions = classifier_model.predict(x_test)

    # Predict probability
    y_score = classifier_model.predict_proba(x_test)[:, 1]

    fpr, tpr, thresholds = roc_curve(y_test, y_score)

    # performance measure https://towardsdatascience.com/performance-metrics-for-classification-machine-learning
    # -problems-97e7e774a007 confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

    # performance measurements
    dt_model = classifier_model

    dt_confusion_matrix = confusion_matrix(y_true=y_test, y_pred=predictions)

    dt_accuracy = accuracy_score(y_true=y_test, y_pred=predictions)

    dt_precision = precision_score(y_true=y_test, y_pred=predictions, average="micro")

    dt_recall = recall_score(y_true=y_test, y_pred=predictions, average="micro")

    dt_f1_score = f1_score(y_true=y_test, y_pred=predictions, average="micro")

    dt_roc_auc_score = roc_auc_score(y_true=y_test, y_score=predictions)

    dt_classification_report = classification_report(y_true=y_test, y_pred=predictions)

    return dict(model='DecisionTreeClassifier', accuracy=dt_accuracy, precision=dt_precision,
                recall=dt_recall, f1_score=dt_f1_score, roc_auc_score=dt_roc_auc_score,
                confusion_matrix=dt_confusion_matrix, classification_report=dt_classification_report,
                fpr=fpr, tpr=tpr, thresholds=thresholds, actual_model=dt_model)


if __name__ == "__main__":
    assert decision_tree_classifier() is not None
    print("Decision Tree Classifier - Done")
