from testrail import *

def test_print():
    print "testing"

def test_second():

    print "we welcome you"

class first:
    def __init__(self, value):
        pass

    def get_value(self, value):

        pass
if __name__ == "__main__":
    client = APIClient('http://testrail.gigamon.com')
    client.user = 'tdjearamane'
    client.password = '@2008Hemu1975'
    #test_case = client.send_get('get_runs/4',
    #                             {'milestone_id':42}
    #                        )
    '''
    test_run_update = client.send_post('update_run/59129',
                                        { "include_all": 'false',
                                          "case_ids":[ 1783923712,1783923713]
                                        }
                        )

    test_run_creation = client.send_post('add_run/4',
                                         { "milestone_id": 66,
                                            "name":"HAL test runV2",
                                           "include_all":0,
                                          "case_ids":[913225,20529]
                                          }
                            )
                             
    '''
    delete_test_run_status = client.send_post('delete_run/59821', {})

    #print delete_test_run_status 
