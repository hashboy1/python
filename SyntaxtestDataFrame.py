import numpy as np
import pandas as pd
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
b=np.array(a)
c= pd.DataFrame(a)
del c[2]
print(c)
