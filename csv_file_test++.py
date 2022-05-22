import csv
from encodings import utf_8
def load_data_from_csv(csv_file):
    list_from_reader=[]
    with open (csv_file, encoding="utf-8") as object_file:
            reader=csv.reader(object_file)
            # list_from_reader=[]
            next(reader) # this is to remove the header
            for line in reader:
                # print(line)
                if line != []:
                    list_from_reader.append([line[0],int(line[1]), int(line[2])])
            print(list_from_reader)
    return list_from_reader
load_data_from_csv("tests\data\example_two.csv")

# ***to run this code in Weather, it should be inside the weatherproject folder.
# C:\Zohreh\SheCodes\she-codes-python-weather-project-ZoeArabshahi\tests\data