from csv import reader
from random import randrange
import  numpy as np
from numpy import linalg as LA
from random import seed

def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset



# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup


def train_test_split(dataset,split):
    train = list()
    train_size = split * len(dataset)
    dataset_copy = len(dataset)
    while len(train) < (train_size):
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train,dataset_copy



def PCA(train , k):
    cov = np.zeros(train.shape[1] ,train.shape[1])
    for i in range(0, train.shape[0]):
        cov = cov + np.matmul(train[i].transpose(),train[i])
    avg_cov = (1/train[0]) * cov
    eigen_values,eigen_vectors = LA.eig(avg_cov)

    z = np.matmul(eigen_vectors.T[0:k],train.T)
    return z




seed(2)
# load and prepare data
filename = 'sonar.all-data.csv'    # we can pass any dataset we want
dataset = load_csv(filename)
# convert string attributes to integers
for i in range(0, len(dataset[0])-1):
	str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
train,test =train_test_split(dataset,split)
z = PCA(train, 1)