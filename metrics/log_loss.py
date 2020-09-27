import numpy as np
loss = []
def log_loss(y_true,y_pred):
    for yt, yp in zip(y_true, y_pred):
        yp = np.clip(yp, epsilon, 1 - epsilon)
        temp_loss = -1.0 * (yt * np.log(yp) + (1 - yt) * np.log(1 - yp))

        loss.append(temp_loss)

    return np.mean(temp_loss)

