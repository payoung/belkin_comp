import glob
import conversion_functions

# Grab a list of the 
data_list = glob.glob('data/H*/Tagged_*.mat')

for data in data_list:
    fileout = file.split('.')[0] + '.bin'
    convertTrainingData(file, fileout)
    
