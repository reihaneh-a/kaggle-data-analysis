# -*- coding: utf-8 -*-
"""ApiKaggle.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19Fcyj3-AJfNX2kOVzJnJGhxzzhPK9Shs
"""

from google.colab import files
files.upload()

mkdir ~/.kaggle

cp kaggle.json ~/.kaggle

ls ~ -a

!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d akashdeepkuila/bakery

from zipfile import  ZipFile

file_name='bakery.zip'
with ZipFile(file_name,'r') as zip:
  zip.extractall()
  print('done')

import pandas as pd
df =pd.read_csv("Bakery.csv")
df

df.head(5)

df.tail(5)

df.duplicated(keep=False).value_counts()

"""As we are interested only in item combinations, the duplicated rows can be removed:"""

df.drop_duplicates(inplace=True)
df

df.info

df.duplicated()