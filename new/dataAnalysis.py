import pandas as pda
import numpy as np
import matplotlib.pylab as py
from sklearn.decomposition import PCA

data = pda.read_csv("for_audit.csv")

# data1 = data.T
# print(data1.values[6])
# print(data.shape())
# print(data.head())
# print(data.sort_values(by="QUANTITY").head())
# load excel,but it didn't support the excel 2016
# data = pda.read_excel("for_audit.xls")
# print(data.describe())

# chat
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# py.plot(data1.values[7], data1.values[6], 'o')
# py.show()


del data["SECTOR_CODE"]
del data["CD_NUMBER"]
del data["CD_DATE"]
del data["INBOUND_TYPE"]
del data["ITEM_NUMBER"]
del data["HS_CODE"]
del data["AMOUNT_USD"]
del data["CURRENCY_CODE"]

print(data)

# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA()
pca.fit(data)
print(pca.components_)
print(pca.explained_variance_ratio_)