import pandas as pd
import matplotlib.pyplot as plt

train_data = pd.read_csv("test.csv")
train_data
plt.plot(train_data['Age'])
print('hi there')
print('another line')

plt.style.available
plt.style.use('seaborn-dark-palette')
