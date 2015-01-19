
# #
# © DianaCorp 2015
##


import logging
import time
import csv


##
# Read the configurable File and modify the values;
# Fix the kids SKU issue
##

fileName = "insert_configurable_pt_20141229_141500_01.csv"

try:
    with open(fileName) as csvFile:
        readCSV = csv.reader(csvFile, delimiter=',')
        header = readCSV.__next__()
        print(header)

        with open('new'+fileName, 'w', newline='') as fp:
            a = csv.writer(fp, delimiter=',')
            a.writerow(header)

            temp = ""
            for row in readCSV:
                sku = row[0]

                if sku[:3] == "PKK":
                    if sku[:-1] == temp:
                        for i in range(0,64):
                            row[i] = ""

                    else:
                        row[0] = sku[:-1]
                        temp = row[0]
                        print(row[0])

                if row[2] != "":
                    row[2] = "peuterey"
                    print(row[2])

                if row[6] != "":
                    row[6] = "world, ita, un"
                    print(row[6])

                a.writerow(row)

        fp.close()

        logging.basicConfig(filename='Success.log', level=logging.DEBUG)
        logging.debug('File conversion was successful')
    csvFile.close()

except:
    print("\nSomething went wrong!")
    time.sleep(10)
    logging.basicConfig(filename='Error.log', level=logging.DEBUG)
    logging.debug('Something went wrong!')