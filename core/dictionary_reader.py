from config import config
from util.printer import printer

"""
the argument should be a list of file to open

when file_type is txt
return all the lines(as a list) in the target files
"""
def __read(file_list, file_type='txt'):


    if file_type=='txt':

        #
        results_list=[]

        # filtered comment line
        for file_name in file_list :
            f=open(config.PROJECT_DIR+config.DIR_SEPERATOR+config.DICTIONARY_DIR+config.DIR_SEPERATOR+file_name,'r')
            name_list = f.readlines()
            name_list=map(lambda x:x.strip(),name_list)
            name_list = filter(lambda x:len(x)!=0,name_list)
            name_list=filter(lambda x:x[0]!='#',name_list)


            results_list.extend(name_list)

        return results_list
    elif    file_type   == 'json':
        return

    elif   file_type == 'csv' :
        return

    else:
        return


def parse_dict():
    result = []

    result.extend(__read(config.dictionary))

    config.target_list=result



