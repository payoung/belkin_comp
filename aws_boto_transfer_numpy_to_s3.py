import boto
import boto.s3.connection
from boto.s3.key import Key
import glob
# credentials.py should contain the access_key and secret_key which are needed for
# the boto S3 connection
import credentials as cr

# Connect to S3
conn = boto.connect_s3(
        aws_access_key_id = cr.access_key,
        aws_secret_access_key = cr.secret_key,
        host = 's3-us-west-2.amazonaws.com',
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

# Connect to bucket
bucket = conn.get_bucket('belkin-data')

# Grab a list of the np Training Data
np_data_list = glob.glob('data/H*/Tagged_*.bin')

# Save datasets to s3
for data in np_data_list:
    print "Saving %s" % data
    dataout = data.split('data/')[1]
    key = bucket.new_key(dataout)
    key.set_contents_from_filename(data)
