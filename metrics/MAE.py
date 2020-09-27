# mean of of all absolute errors
'''
error= true_value - predicted_value

absolute_error = abs(true_value - predicted_value)
'''

import numpy as np
def mean_absolute_error(y_true,y_pred):
    error= 0
    # loop over all the samples
    for yt,yp in zip(y_true,y_pred):
        #calculate absolute error
        error +=np.abs(yt-yp)
        #return mean absoulte error
    return error/len(y_true)