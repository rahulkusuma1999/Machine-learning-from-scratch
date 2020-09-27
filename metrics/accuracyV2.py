from confusionmetrics import *

def accuracyV2(y_true,y_pred):
    tp =true_positive(y_true,y_pred)
    tn=true_negative(y_true,y_pred)
    fp= falsse_positive(y_true,y_pred)
    fn= falsse_negative(y_true,y_pred)

    accuracy_score = (tp+tn)/(tp+tn+fp+fn)
    return accuracy_score