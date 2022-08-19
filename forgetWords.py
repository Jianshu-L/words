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
# forget = np.zeros(df.shape[0])
# df['forget'] = forget

def assignForget(df, words):
    try:
        forget = df['forget'].values
    except:
        forget = np.zeros(df.shape[0])
    for word in words:
        if word.startswith("-"):
            index = np.where(df['words'] == word[1:])
            forget[index] = 0
        else:
            index = np.where(df['words'] == word)
            forget[index] = 1
    df['forget'] = forget
    return df

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

def showForget(df):
    return df.loc[df['forget']==1,:]

# %%
if __name__ == '__main__':
    fileNames = [fileName for fileName in os.listdir() if fileName.endswith("csv")]
    df_f = pd.DataFrame()
    for fileName in fileNames:
        df = pd.read_csv(fileName)
        # assign forget words
        if len(sys.argv) > 1:
            words = sys.argv[1:]
            df = assignForget(df, words)
            df.to_csv(fileName, index=False)
            df.to_markdown(fileName.replace("csv","md"))
        df_f_i = showForget(df).sample(frac=1)
        df_f = pd.concat([df_f,df_f_i],ignore_index=True)
        df_f_i.to_markdown(f'{fileName.replace(".csv","_")}forget.md')
df_f.to_markdown("forget.md")

