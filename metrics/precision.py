from confusionmetrics import *

# precision is great to work with when we have imbalanced dataset


def precision(y_true,y_pred):
    tp = true_positive(y_true,y_pred)
    fp = falsse_positive(y_true,y_pred)

    precision = tp/(tp+fp)

    return precision