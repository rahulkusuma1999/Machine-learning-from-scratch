# precison @ k is defined as number of hits in predicted list consedering only top k predictions

def precisionAtk(y_true,y_pred,k):
    # if k=0 return 0 .we should always have k >=1
    if k == 0:
        return 0
    # we need only first K predictions
    y_pred = y_pred[:k]
    #convert to sets
    pred_set = set(y_pred)
    true_set = set(y_true)
    # find common values
    common_values = pred_set.intersection(true_set)
    #return length og common over  k
    return len(common_values)/ len(y_pred[:k])

