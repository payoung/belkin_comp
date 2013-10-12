# reads in np data, saves it to a panda data frame
import numpy as np
import pandas as pd

def create_df(filepath):
    
    f = file(filepath, "rb")

    d1 = {}
    d2 = {}

    taggingInfo = np.load(f)

    d1['L1_TimeTicks'] = np.load(f)
    d1['L1_Real'] = np.load(f)
    d1['L1_Imag'] = np.load(f)
    d1['L1_App'] = np.load(f)
    d1['L1_Pf'] = np.load(f)

    d2['L2_TimeTicks'] = np.load(f)
    d2['L2_Real'] = np.load(f)
    d2['L2_Imag'] = np.load(f)
    d2['L2_App'] = np.load(f)
    d2['L2_Pf'] = np.load(f)

    df1 = pd.DataFrame(d1)
    df2 = pd.DataFrame(d2)

    return taggingInfo, df1, df2
