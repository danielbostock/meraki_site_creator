# Start Import area
import csv
# End Import Area

# CSV Files (Testing)
#brandscsv = 'config/site_data/brands.csv'
#row_selected = 'Brand'

class CsvProc:
    def __init__(self, csvfile, row):
        self.csvfile = csvfile
        self.row = row
    
    def rem_dup(x):
        return list(dict.fromkeys(x))

    def read(self):
        csvdata_read = False
        while csvdata_read == False:
            csvopen = csv.DictReader(open(self.csvfile))
            csvdata = []
            for row in csvopen:
                row_csvdata_read = row[self.row]
                csvdata.append(row_csvdata_read)
                csvdata = CsvProc.rem_dup(csvdata)
                csvdata_read = True
            if csvdata_read == True:
                for count,item in enumerate(csvdata, 1):
                    csvopen = print(count,item)
                return csvdata_read
        if csvdata_read == True:
            return csvdata_read
    def read_input(self):
        csvdata_read = False
        while csvdata_read == False:
            csvopen = csv.DictReader(open(self.csvfile))
            csvdata = []
            for row in csvopen:
                row_csvdata_read = row[self.row]
                csvdata.append(row_csvdata_read)
                csvdata = CsvProc.rem_dup(csvdata)
                csvdata_read = True
            if csvdata_read == True:
                return csvdata
            else:
                break
    
        

# Tests
#brand_list = CsvProc(brandscsv,row_selected)
#brand_list.read()