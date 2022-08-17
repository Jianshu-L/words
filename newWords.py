# %%
import pandas as pd
import os
import numpy as np
Path = "/mnt/c/Users/ljs/Documents"
fileNames = [fileName for fileName in os.listdir(Path) if fileName.endswith("csv")]

if __name__ == '__main__':
    for fileName in fileNames:
        df = pd.read_csv(f'{Path}/{fileName}',header=None, names=np.array(["words","property","meaning"]))
        try:
            forget = df['forget'].values
        except:
            forget = np.zeros(df.shape[0])
        df['forget'] = forget
        df.to_csv(f'words_{fileName[4:8]}.csv', index=False)
        df.to_markdown(f'words_{fileName[4:8]}.md')