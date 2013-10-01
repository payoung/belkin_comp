#!/bin/bash

# In order to run this script you will need a file in the directory called cookies.txt that contains the cookies associated with your Kaggle account.  You will need to log on to kaggle, accept the competition rules for the Belkin comp, and then save the cookies to a text file (you can use an extension such as 'cookie.txt' for chrome).  
# Once you have the cookies saved to a file, you need to chmod this script using the following command: 'chmod u+x data_download.sh'
# Run the script by typing the following command: './data_download.sh'

echo "Downloading H1.zip"

wget -c --load-cookies cookies.txt --read-timeout=30 "http://www.kaggle.com/c/belkin-energy-disaggregation-competition/download/H1.zip"

echo "File Downloaded, unzipping file"

unzip H1.zip

echo "File successfully unzipped, removing the zip file"

rm H1.zip

echo "Downloading H2.zip"

wget  -c --load-cookies cookies.txt --read-timeout=30 "http://www.kaggle.com/c/belkin-energy-disaggregation-competition/download/H2.zip"

echo "File Downloaded, unzipping file"

unzip H2.zip

echo "File successfully unzipped, removing the zip file"

rm H2.zip

echo "Downloading H3.zip"

wget  -c --load-cookies cookies.txt --read-timeout=30 "http://www.kaggle.com/c/belkin-energy-disaggregation-competition/download/H3.zip"

echo "File Downloaded, unzipping file"

unzip H3.zip

echo "File successfully unzipped, removing the zip file"

rm H3.zip

echo "Downloading H4.zip"

wget  -c --load-cookies cookies.txt --read-timeout=30 "http://www.kaggle.com/c/belkin-energy-disaggregation-competition/download/H4.zip"

echo "File Downloaded, unzipping file"

unzip H4.zip

echo "File successfully unzipped, removing the zip file"

rm H4.zip

echo "All done, have fun!"





