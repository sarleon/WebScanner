from config import Config


"""
the argument should be a list of file to open

when file_type is txt
return all the lines(as a list) in the target files
"""
def read(file_list, file_type='txt'):


    if file_type=='txt':

        #
        name_list = []

        #
        for file_name in file_list :
            f=open(file_name,'r')
            name_list.extend(f.readlines())


        return name_list
    elif    file_type   == 'json':
        return

    elif   file_type == 'csv' :
        return

    else:
        return
