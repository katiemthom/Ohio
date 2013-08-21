import csv

#replace output.csv with whatever you want the cleaned file to be named
ofile = open('output.csv', 'wb')
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting = csv.QUOTE_NONE)

#replace filetobecleaned.csv with your file's name 
test = csv.reader(open('filetobecleaned.csv', 'rU'), delimiter=',')

for row in test:
    writer.writerow(row)   
