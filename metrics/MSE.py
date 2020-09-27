'''
squarred_error = (true_values - predicted_value) **  2

'''
# mean_squarred_error is mean of squarred_error

def mean_squarred_error(y_true,y_pred):
    error  = 0
    #loop over all values
    for yt,yp in zip(y_true,y_pred):
        #calculate squarred error
        error += (yt-yp)**2

    return error/len(y_true)