'''

precentage error = ((true_value - predicted_value) / true_value ) *100

'''

# we can also calculate mean_precentage_error by taking mean of precentage_error


def mean_precentage_error(y_true,y_pred):
    error = 0
    for yt,yp in zip(y_true,y_pred):
        error += (yt - yp) /yt
    return error / len(y_true)
