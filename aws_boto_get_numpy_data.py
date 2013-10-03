import boto
import boto.s3.connection
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

# Get the list of numpy data sets in S3
training_data_list = []
for key in bucket.list():
    if key.name.find('.bin') != -1:
        training_data_list.append(key.name)


# Save datasets to file
for data in training_data_list:
    print "Saving %s" % data
    key = bucket.get_key(data)
    dataout = 'data/' + data
    key.get_contents_to_filename(dataout)
