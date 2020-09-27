'''

MSLE = (log(1 + y_true ) - log(1 + y_pred)) ** 2

'''

# we can also calculate root_mean_squarred_log_error by taking square root of MSLE

import numpy as np
def mean_squarred_log_error(y_true,y_pred):
    error = 0
    for yt,yp in zip(y_true,y_pred):
        error += (np.log(1 + yt) - np.log(1 + yp)) ** 2
    return error / len(y_true)
