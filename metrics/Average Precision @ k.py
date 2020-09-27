from .precisionATk import *

def apk(y_true,y_pred,k):
    pk_values = []
    for i in range(1,k+1):
        pk_values.append(precisionAtk(y_true,y_pred,i))
    if len(pk_values)==0:
        return 0
    return sum(pk_values)/len(pk_values)