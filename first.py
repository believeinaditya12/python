# recommendation engine
import numpy as np
import pandas as pd
import warnings
 # if we get any warnings then we can ignore that warning using 
warnings.filterwarnings('ignore')
# get the dataset
columns_names = ["user_id", "item-id", "rating", "timestamp"]
df = pd.read_csv('u.data',sep='\t', names=columns_names)
df.head()
#  100000 rows and 4 columns
df.shape
# to find the n unique id's
df['user_id']
# no of unique users
df['user_id'].unique()
