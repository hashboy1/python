import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from openpyxl.workbook import Workbook

# Reading data from web
#data_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
#df = pd.read_csv(data_url)

df = pd.read_csv(r'E:\workspace\python\data.csv')
#print(df.head())


print(df.T)
#print(df.tail())
print(df.columns)
#print(df.index)
print(df.describe())
print(df)
print(type(df))

#plt.show(df.plot(kind = 'box'))




#pd.options.display.mpl_style = 'default' # Sets the plotting display theme to ggplot2
#df.plot(kind = 'box')
# Do the boxplot
#plt.show(sns.boxplot(df, widths = 0.5, color = "pastel"))
