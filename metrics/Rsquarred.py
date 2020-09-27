# r2 is also known as coefficent of determination
# r2 says how good your model fits the data
# r2 closer to 1.0 says models fits data quite well
# r2 closer to 0 says models isn't that good
# r2 can also be negative

'''

r2  =  1 - (from 1 to n (yt - yp)**2) / (from 1 to  n ( yt  - yt_mean))

'''

import numpy as np
def r2(y_true,y_pred):
    # calculate mean of true values
    mean_true_values = np.mean(y_true)

    numerator = 0
    denominator = 0

    for yt,yp in zip(y_true,y_pred):
        # update numerator
        numerator += (yt - yp) **2
        # update denominator
        denominator  += ( yt - mean_true_values) ** 2

    # calculate ratio
    ratios  = numerator/denominator
    return 1 - ratios