import numpy as np
import pandas as pd

# convert to pandas DataFrames
X_df = pd.DataFrame(X1dot)
Y_df = pd.DataFrame(Y1dot)
Z_df = pd.DataFrame(Z1dot)

# Use pandas Excel Writer to create one Excel file with a sheet for each array
with pd.ExcelWriter('/content/3d.xlsx') as writer:
    X_df.to_excel(writer, sheet_name='XYZ', startrow=0, startcol=0, header=False, index=False)
    Y_df.to_excel(writer, sheet_name='XYZ', startrow=0, startcol=1, header=False, index=False)
    Z_df.to_excel(writer, sheet_name='XYZ', startrow=0, startcol=2, header=False, index=False)
    print("File saved")