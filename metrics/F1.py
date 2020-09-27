from .precision import *
from .recall import *

def f1(y_true,y_pred):
    p= precision(y_true,y_pred)
    r = recall(y_true,y_pred)

    score = 2*p*r / (p+r)
    return score