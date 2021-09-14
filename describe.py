import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataFrame = pd.read_csv('datasets/dataset_train.csv', delimiter=',', index_col=0)
print(dataFrame.iloc[:,3]) #.describe())