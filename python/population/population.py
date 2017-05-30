import csv
import sys
import india_population



if __name__ == "__main__":
    file_name=sys.argv[1]
    #population_detail = {}
    try:
        csv_data = india_population.read_csv(file_name)
        print type(csv_data)
    except IOError:
        print ('couldnt open file')
    else:
        population_detail = india_population.parse_state_wise_date(csv_data)  
        print population_detail
        print "------------------------------"
        print population_detail['Haryana']



    '''
    country = { 'tamilnadu': 'tamilnadu',
                'kerala' : 'kerala'
            }

    list_states = ['tamilnadu','kerala']

    print country
    country['tamilnadu'] = {}
    print  country['tamilnadu']
    list_states[0] = {}
    list_states1 = {} 
    detail = {'16to20': {'male':20, 'female':39, 'total': 59}}

    state= 'tamilnadu'
    list_states1[state] = detail
    
    print list_states1

    '''
   

