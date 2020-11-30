# Importing the required libraries
from mpl_toolkits import mplot3d

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

from matplotlib.animation import FuncAnimation
pp.style.use('seaborn-pastel')

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Array for storing the cordinates
X1dot=[]
Y1dot=[]
Z1dot=[]

# gcode file in txt format
file=open('Gcodes/chair.txt','r')

flag = 0
skin = ";TYPE:SKIN"

# Storing the cordinates to the array
# only after TYPE:SKIN line.
for line in file: 
    if skin in line:
        flag = 1   
    if line[0]=='G':
        words=line.split()
        for word in words:
            if word[0]=='X' and flag == 1:
                w=word[1:len(word)]
                X1dot.append(float(w))
            elif word[0]=='Y' and flag == 1:
                w=word[1:len(word)]
                Y1dot.append(float(w))
            elif word[0]=='E' and word[1]!='x' and flag == 1:
                w=word[1:len(word)]
                Z1dot.append(w)

# Automatically declares 0 to point clouds if not available.
for i in range(len(Z1dot)):
    if Z1dot[i]=='':
        Z1dot[i]='0'
for i in range(len(Z1dot)):
    Z1dot[i]=float(Z1dot[i])
print(X1dot)
print(Y1dot)
print(Z1dot)

# convert to pandas DataFrames
X_df = pd.DataFrame(X1dot)
Y_df = pd.DataFrame(Y1dot)
Z_df = pd.DataFrame(Z1dot)

# Use pandas Excel Writer to create one Excel file with a sheet for each array
with pd.ExcelWriter('chair_final.xlsx') as writer:
    X_df.to_excel(writer, sheet_name='XYZ', startrow=0, startcol=0, header=False, index=False)
    Y_df.to_excel(writer, sheet_name='XYZ', startrow=0, startcol=1, header=False, index=False)
    Z_df.to_excel(writer, sheet_name='XYZ', startrow=0, startcol=2, header=False, index=False)
    print("File saved")