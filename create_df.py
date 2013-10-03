# reads in np data, saves it to a panda data frame
import numpy as np
import pandas as pd

def create_df(filepath):
    
    f = file(filepath, "rb")

    df = pd.DataFrame()

    df['L1_Real'] = np.load(f)
    df['L1_Imag'] = np.load(f)
    df['L1_App'] = np.load(f)
    df['L1_Pf'] = np.load(f)
    df['L2_Real'] = np.load(f)
    df['L2_Imag'] = np.load(f)
    df['L2_App'] = np.load(f)
    df['L2_Pf'] = np.load(f)

    return df
