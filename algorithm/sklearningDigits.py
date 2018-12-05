from sklearn.datasets import load_digits,load_boston
import numpy as np
'''
digits = load_digits()
X_data = digits.data.astype(np.float32)
Y_data = digits.target.reshape(-1,1).astype(np.float32)
print(X_data.shape)
print(Y_data.shape)
'''
np.set_printoptions(threshold=np.inf)
data = load_boston()
print(data)

