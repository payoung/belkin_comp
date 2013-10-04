# reads in np data, saves it to a panda data frame
import numpy as np
import pandas as pd

def create_df(filepath):
    
    f = file(filepath, "rb")

    d = {}

    d['L1_Real'] = np.load(f)
    d['L1_Imag'] = np.load(f)
    d['L1_App'] = np.load(f)
    d['L1_Pf'] = np.load(f)
    d['L2_Real'] = np.load(f)
    d['L2_Imag'] = np.load(f)
    d['L2_App'] = np.load(f)
    d['L2_Pf'] = np.load(f)

    df = pd.DataFrame(d)

    return df
