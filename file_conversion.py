import glob
import conversion_functions as cf

# Grab a list of the Training Data
data_list = glob.glob('data/H*/Tagged_*.mat')

for data in data_list:
    print "Converting %s" % data
    dataout = data.split('.')[0] + '.bin'
    cf.convertTrainingData(data, dataout)
    
