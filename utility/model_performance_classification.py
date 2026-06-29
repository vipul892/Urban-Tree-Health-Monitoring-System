from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,balanced_accuracy_score,classification_report
import numpy as np

def evaluate_model(y_test,y_pred):

    return {
        "Accuracy":
            accuracy_score(y_test, y_pred),

        "Balanced Accuracy":
            balanced_accuracy_score(y_test, y_pred),

        "Precision":
            precision_score(
                y_test,
                y_pred,
                average='weighted'
            ),

        "Recall":
            recall_score(
                y_test,
                y_pred,
                average='weighted'
            ),

        "F1 Score":
            f1_score(
                y_test,
                y_pred,
                average='weighted'
            )  

    }
