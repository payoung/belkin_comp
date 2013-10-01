from scipy import linspace, io
from pylab import *
from cmath import phase
from math import *


# Converts Tagged Training Data into numpy arrays
def convertTrainingData(filepathin, filepathout):

    taggingData = io.loadmat(filepathin, struct_as_record=False, squeeze_me=True)

    # Extract tables
    buf = taggingData['Buffer']
    LF1V = buf.LF1V
    LF1I = buf.LF1I
    LF2V = buf.LF2V
    LF2I = buf.LF2I
    L1_TimeTicks = buf.TimeTicks1
    L2_TimeTicks = buf.TimeTicks2
    HF = buf.HF
                         
    HF_TimeTicks = buf.TimeTicksHF

    taggingInfo = buf.TaggingInfo

    # Calculate power (by convolution)
    L1_P = LF1V * LF1I.conjugate()
    L2_P = LF2V * LF2I.conjugate()
    L1_ComplexPower = L1_P.sum(axis=1) 
    L2_ComplexPower = L2_P.sum(axis=1)

    # Extract components
    L1_Real = L1_ComplexPower.real
    L1_Imag = L1_ComplexPower.imag
    L1_App  = abs(L1_ComplexPower)
    L2_Real = L2_ComplexPower.real
    L2_Imag = L2_ComplexPower.imag
    L2_App  = abs(L2_ComplexPower)
    #
    L1_Pf = [cos(phase(L1_P[i,0])) for i in range(len(L1_P[:,0]))]
    L2_Pf = [cos(phase(L2_P[i,0])) for i in range(len(L2_P[:,0]))]
    L1_Pf = np.array(L1_Pf,dtype='float64')
    L2_Pf = np.array(L2_Pf,dtype='float64')

    f = file(filepathout, "wb")
    np.save(f, L1_Real)
    np.save(f, L1_Imag)
    np.save(f, L1_App)
    np.save(f, L1_Pf)
    np.save(f, L2_Real)
    np.save(f, L2_Imag)
    np.save(f, L2_App)
    np.save(f, L2_Pf)

    f.close()

