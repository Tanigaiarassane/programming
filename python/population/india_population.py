import csv
import sys

states = ["AndhraPradesh",
        "ArunachalPradesh",
        "Assam",
        "Bihar",
        "Chandigarh",
        "Chhattisgarh",
        "Dadra&NagarHaveli",
        "Daman&Diu",
        "Delhi",
        "Goa",
        "Gujarat",
        "Haryana",
        "HimachalPradesh",
        "JammuandKashmir",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Lakshadweep",
        "MadhyaPradesh",
        "Maharastra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Puducherry",
        "Punjab",
        "Rajasthan",
        "Sikkim",
        "TamilNadu",
        "Tripura",
        "Telangana",
        "UttarPradesh",
        "Uttarakhand",
        "WestBengal" ]

def parse_state_wise_date(data):
    '''
    Function to parse the data list into state wise population
    Input: List containing state data. Each row representing a state
    Return: Dictionary of states data - Each state inturn contain the age wise data as a sub dictionary
    '''
    population_detail = {}
    for line in data:
        print "======{}====".format(line[1])

        if line[1].replace(' ','') in states:
            print line

            population_detail[line[1]] ={
                        '6to10' : {'male':line[2], 'female': line[3], 'total':line[4]},
                        '11to13': {'male':line[5], 'female': line[6], 'total':line[7]},
                        '14to15': {'male':line[8], 'female': line[9], 'total':line[10]},
                        '16to17': {'male':line[11], 'female': line[12], 'total':line[13]},
                        '18to22': {'male':line[14], 'female': line[15], 'total':line[16]},
                        '18to23': {'male':line[17], 'female': line[18], 'total':line[19]},
                      }
                 
    return population_detail

def read_csv(file_name):
    '''
    To parse the content of a CSV file
    Input: CSV file name
    Returns: Content of the CSV in csv reader format (rows of list)
    '''
    fh = open(file_name)
    csv_lines = csv.reader(fh)
    return csv_lines

if __name__ == "__main__":
    file_name=sys.argv[1]
    try:
        csv_data = read_csv(file_name)
    except IOError:
        print ('couldnt open file')
    else:
        for line in csv_data:
         print line
