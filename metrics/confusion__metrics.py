def true_positive(y_true,y_pred):
    tp=0
    for yt,yp in zip(y_true,y_pred):
        if yt==1 and yp==1:
            tp+=1
    return tp

def true_negative(y_true,y_pred):
    tn=0
    for yt,yp in zip(y_true,y_pred):
        if yt==0 and yp ==0:
            tn+=1
    return tn

def falsse_positive(y_true,y_pred):
    fp = 0
    for yt,yp in zip(y_true,y_pred):
        if yt == 0  and yp ==1:
            fp+=1
    return fp

def falsse_negative(y_true,y_pred):
    fn = 0
    for yt,yp in zip(y_true,y_pred):
        if yt == 1  and yp ==0:
            fn+=1
    return fn