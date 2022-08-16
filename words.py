# %%
import sys
from IPython.display import display
import pandas as pd
import os
import numpy as np
import random
Path = "/mnt/c/Users/ljs/Documents"
fileNames = [fileName for fileName in os.listdir(Path) if fileName.endswith("csv")]
# df = pd.read_csv(f'{Path}/{fileNames[0]}',header=None, names=np.array(["words","property","meaning"]))


def assignForget(df, words):
    forget = np.zeros(df.shape[0])
    for word in words:
        index = np.where(df['words'] == word)
        forget[index] = 1
    df['forget'] = forget
    return df

def showWords(df,index):
    print(np.floor(df.shape[0]/20))
    if index == 0:
        return df.iloc[random.sample(range(0,64),20),:]
    if index > np.floor(df.shape[0]/20):
        index = np.int8(np.floor(df.shape[0]/20))
        return df.iloc[:-index*20,:]
    elif index == 1:
        return df.tail(20)
    else:
        return df.iloc[-index*20:-(index-1)*20,:]

def showForget(df):
    return df.loc[df['forget']==1,:]

# %%
if __name__ == '__main__':
    # words = ["revoke","recoil","strip","vicious","relegate","shrewd", "resent","crusade","thorn","lethal","eloquent","reluctant","garb","substantial"]
    df = pd.read_csv("words.csv")
    index = np.int8(sys.argv[1])
    showWords(df, index).to_markdown('temp.md')
    if len(sys.argv) > 2:
        words = sys.argv[2:]
        print(words)
        df = assignForget(df, words)
        df.to_csv("words.csv", index=False)
        df.to_markdown('words.md')
    showForget(df).to_markdown('forget.md')


