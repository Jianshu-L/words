# %%
import sys
from IPython.display import display
import pandas as pd
import os
import numpy as np
from collections import Counter
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
    # assign forget from words
    words_minus = [word for word in words if word.startswith("-")]
    words_add = [word for word in words if not word.startswith("-")]
    NonExist = []
    for word in words_add:
        if len(forget[df['words'] == word]) == 0:
            NonExist.append(word)
        forget[df['words'] == word] = 1
    for word in words_minus:
        if len(forget[df['words'] == word]) == 0:
            NonExist.append(word)
        forget[df['words'] == word] = 0
    return forget, NonExist

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
    NonExist = []
    for fileName in fileNames:
        df = pd.read_csv(fileName)
        # assign forget words
        if len(sys.argv) > 1:
            words = sys.argv[1:]
            forget,NonExist_ = assignForget(df, words)
            df['forget'] = forget
            NonExist += NonExist_
            df.to_csv(fileName, index=False)
            df.to_markdown(fileName.replace("csv","md"))
        df_f_i = showForget(df).sample(frac=1)
        df_f = pd.concat([df_f,df_f_i],ignore_index=True)
        df_f_i.to_markdown(f'{fileName.replace(".csv","_")}forget.md')
dictWords = Counter(NonExist)
bug_words = [k for k,v in dictWords.items() if v == len(fileNames)]
print(f'{bug_words} not exist')
df_f.to_csv("forget.csv", index=False)
df_f.to_markdown("forget.md")


