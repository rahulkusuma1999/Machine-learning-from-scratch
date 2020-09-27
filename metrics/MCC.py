from confusionmetrics import *
def mcc(y_true,y_pred):
    tp = true_positive(y_true, y_pred)
    tn = true_negative(y_true, y_pred)
    fp = falsse_positive(y_true, y_pred)
    fn = falsse_negative(y_true, y_pred)

    numerator =  (tp * tn) - (fp - fn)

    denominator = (
        (tp + fp ) * (fn + tn) * (fp + tn) * (tp + fn)
    )

    denominator = denominator ** 0.5

    return numerator / denominator