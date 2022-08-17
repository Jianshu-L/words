# %%
import sys
from IPython.display import display
import pandas as pd
import os
import numpy as np
import random

def showWords(df,index):
    print(np.floor(df.shape[0]/20))
    if index == 0:
        return df.sample(n=20)
    if index > np.floor(df.shape[0]/20):
        index = np.int8(np.floor(df.shape[0]/20))
        return df.iloc[:-index*20,:]
    elif index == 1:
        return df.tail(20)
    else:
        return df.iloc[-index*20:-(index-1)*20,:]

# %%
if __name__ == '__main__':
    # words = ["revoke","recoil","strip","vicious","relegate","shrewd", "resent","crusade","thorn","lethal","eloquent","reluctant","garb","substantial"]
    df = pd.read_csv(f"words_{sys.argv[1]}.csv")
    index = np.int8(sys.argv[2])
    try:
        Random = sys.argv[3]
    except:
        Random = 0
    if Random:
        showWords(df, index).sample(frac=1).to_markdown('temp.md')
    else:
        showWords(df, index).to_markdown('temp.md')

