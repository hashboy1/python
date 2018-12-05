from numpy import *
import operator
def knn(k, testdata, traindata, labels):
    traindatasize = traindata.shape[0]
    dif = tile(testdata, (traindatasize, 1)) - traindata  # extend the row
    sqdif = dif ** 2
    sumsqdif = sqdif.sum(axis = 1) # summar by row
    distance = sumsqdif ** 0.5
    sortdistance = distance.argsort()
    count = {}
    for i in range(0,k):
        vote = labels[sortdistance[i]]
        count[vote] = count.get(vote, 0)
    sortcount = sorted(count.items(), key=operator.itemgetter(1),reverse = True)
    return sortcount[0][0]
# image progress
from PIL import Image
