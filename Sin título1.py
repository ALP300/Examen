# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:19:59 2024

@author: aitor
"""

import pandas as pd
df= pd.read_csv('canciones.csv')
print(df.info())
print(df)
filas= len(df.index)
print("Filas: ", filas)
df.drop(df.index[[filas-1]], inplace=True)
filas= len(df.index)
print("Filas: ", filas)
print(df)