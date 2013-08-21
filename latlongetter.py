#imports important tools for script
from geopy import geocoders
g = geocoders.GoogleV3()
import csv
import time

#creates an output file where the desired data will be written and stored
ofile = open('youcreatethenameofyouroutputfilehere.csv', 'wb')

#creates the "writer" which will make writing to the output file possible
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting = csv.QUOTE_NONE)

#opens your input file
test = csv.reader(open('pathtospreadsheetwithaddresseshere.csv', 'rU'), delimiter=',')

#skips the heading row
next(test)

#iterates through each row in the file
for row in test:
	#slows down the script because the api only allows you to get so much data per second
    time.sleep(1)
    #the number of the column that contains the full address of the school goes here
    full_add = row[0]
    #this is where we get the lat and lon data
    place, (lat, lng) = list(g.geocode(full_add, exactly_one=False))[0]
    #this is where the data is written to the output file 
    writer.writerow(row + [str(lat)] + [str(lng)])   
