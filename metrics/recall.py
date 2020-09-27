from .confusion__metrics import  *

def recall(y_true,y_pred):
    tp = true_positive(y_treu, y_pred)
    fn = falsse_negative(y_true, y_pred)
    recall = tp/(tp+fn)

    return recall
