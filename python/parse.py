def is_check_for(line, type):
    if type == "function":
        return  not("def" in line and "(self" in line ) and "def " in line
    elif type == "class":
        return  "class " in line

def parse_functions_body(file_lines, search_string):
        print "search string >>>.{}".format(search_string)

        starting_def = False
        def_body = []
        definition_collection=[]

        for line in file_lines:
            starting_pos = len(line)-len(line.lstrip(' '))
            print line
            print "Space position ..{}".format(starting_pos)

            if is_check_for(line, search_string):
                starting_def = True
                def_start_pos = starting_pos 
                def_body.append(line)
                print "def pringing ..{}".format(def_body)
                #functionraw_input ("Wait >>>")


            elif starting_def:
                if starting_pos > def_start_pos:
                    def_body.append(line)
                    print "Def content ...{}".format(def_body)
                    #raw_input ("Wait >>>")
                elif (line.lstrip() not in " " and 
                          starting_pos == def_start_pos and starting_def):
                    print def_body
                    definition_collection.append(def_body) 
                    def_body = []
                    starting_def = False


if __name__ == "__main__":
    try:
        file_read = open("test.py", "r")
    except IOError (e, errstr):
        print "Error {0} .. {1}".format(e, errstr)
    else:
        print "Printing line"
        file_lines = file_read.readlines()
        functions_content = parse_functions_body(file_lines, "function")


        class_contents  = parse_functions_body(file_lines, "class")
        raw_input ("......Final output.....")
        print class_contents
        print functions_content



