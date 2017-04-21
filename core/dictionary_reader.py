from config import config
from util.printer import printer

"""
the argument should be a list of file to open

when file_type is txt
return all the lines(as a list) in the target files
"""
def read(file_list, file_type='txt'):


    if file_type=='txt':

        #
        name_list = []

        # filtered comment line
        for file_name in file_list :
            f=open(file_name,'r')
            name_list.extend(f.readlines())
            name_list=filter(lambda x:x.strip()[0]!='#',name_list)

        return name_list
    elif    file_type   == 'json':
        return

    elif   file_type == 'csv' :
        return

    else:
        return
