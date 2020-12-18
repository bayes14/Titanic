import pandas as pd
import matplotlib.pyplot as plt

train_data = pd.read_csv("test.csv")
train_data
plt.hist(train_data['Age'])
